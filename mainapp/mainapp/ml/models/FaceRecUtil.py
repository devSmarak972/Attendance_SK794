import cv2
import numpy as np
import face_recognition as face_rec
from ml.models.Dbuse import get_encode
def check_identity(empid,encodingT,mycol):
  encodinglist=get_encode(empid,mycol)
  count=0
  # print(type(encodinglist))
  for item in encodinglist:
    item=np.array(item)
  #  print(item)
  #  print("\nthis is item")
  #  print(item.shape)
    compare=face_rec.compare_faces([item],encodingT)
  #  print(compare)
    count=count+1
  #  face_Dist=face_rec.face_distance([item],encodingT)
  #  print(face_Dist)
    # if((count/len(encodinglist))>0.6):
  return count
    # else:
      # return False