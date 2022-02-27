from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):

    client = MongoClient(host=host,
                      port=int(port),
                      username=username,
                      password=password
                     )
    db_handle = client['db_name']
    return db_handle, client
def get_db_handle():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydb"]
    return myclient,mydb
     