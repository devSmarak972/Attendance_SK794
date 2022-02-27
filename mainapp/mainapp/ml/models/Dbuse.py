import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydb"]
# mycol = mydb["employee"]
def add_details(details,mycol):
    # print(details)
    mycol.insert_one(details)
def add_encode(empid,encode,mycol):
    # print("in encode")
    mycol.update_one({"empid":empid},{'$push':{'encoding':encode}})
def get_encode(empid,mycol):
    encode=mycol.find({"empid":empid},{'encoding':1,"_id":0})
    return (list(encode)[0]['encoding'])
    
