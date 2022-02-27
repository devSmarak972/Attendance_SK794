# from django.shortcuts import render

# Create your views here.
# Edit views.py
# The last step is to update views.py. The views will be mainly responsible for two tasks:

# Process incoming POST requests.
# Make a prediction with the incoming data and give the result as a Response.


import urllib
# from Dbuse import *
from django.shortcuts import render
import numpy as np
from ml.models.Dbuse import add_details, add_encode,get_encode
from ml.models.FaceRecUtil import *
# from Dbuse import add_details, add_encode,get_encode
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
import cloudinary.uploader
import matplotlib.pyplot as plt
import cv2
import face_recognition as face_rec
import utils
import pymongo
import time

# Create your views here.
class newUpload(APIView):
    parser_classes = (MultiPartParser,JSONParser, )
    @staticmethod
    def post(request):
        file = request.data.get('picture')
        # details=request.data.get('details')
        name=dict(request.data)['name'][0]
        empid=dict(request.data)['empid'][0]
        newimg=dict(request.data)['newimg'][0]
        upload_data = cloudinary.uploader.upload(file)
        img = upload_data['url']
        print(img)
        req = urllib.request.urlopen(img)
        #processing input image
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img=cv2.imdecode(arr, -1) #load it as it is
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        
        # img = cv2.resize(img,(224,224))#model="cnn"
      
        start=time.time()
        boxes = face_rec.face_locations(img,model='hog')
        # print(boxes)
        skip=True
        # print(len(boxes))
        # number_of_times_to_upsample=0
        if(len(boxes)):
            encode=face_rec.face_encodings(img,boxes)[0]
            #connecting database
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydb"]
            mycol=mydb["employee"]
            # details={"name":"Elon Musk","empid":"123457",}
            
            details={"name":name,"empid":empid}
            #ADDING DETAILS TO DB
            if newimg:
                add_details(details,mycol)
            add_encode(details["empid"],encode.tolist(),mycol)
        else:
            skip=False   
        end=time.time()
        print(start-end)
        return Response({
            'status': 'success',
            # 'details':details,
            # 'url':img,
            'added':skip ,   
            'time':start-end,        
        }, status=201)
        
        
        
class checkIdentity(APIView):
    parser_classes = (MultiPartParser,JSONParser, )
    @staticmethod
    def post(request):
        file = request.data.get('picture')
        # details=request.data.get('details')
        # name=dict(request.data)['name'][0]
        empid=dict(request.data)['empid'][0]
    
        upload_data = cloudinary.uploader.upload(file)
        img = upload_data['url']
        req = urllib.request.urlopen(img)
        #processing input image
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img=cv2.imdecode(arr, -1) #load it as it is
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # img = cv2.resize(img,(224,224))
        boxes = face_rec.face_locations(img,model='cnn')
        encode=face_rec.face_encodings(img,boxes)[0]
        #CONNECT TO DB
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydb"]
        mycol=mydb["employee"]
        #CHECKING WITH DB
        ret=check_identity(empid,encode,mycol)
        if ret:
            add_encode(empid,encode.tolist(),mycol)
        return Response({
            'status': 'success',
            # 'details':details,
            # 'url':img,
            'value':ret            
        }, status=201)
        


