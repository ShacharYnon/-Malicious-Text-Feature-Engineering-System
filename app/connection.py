from pymongo import MongoClient
from app import config


class DBconnection:

    def __init__(self):
        self.client = None
        self.database = None

    def connection(self):
        try:
            self.client = MongoClient(config.MONGODB_URI)
            self.database = self.client[config.MONGODB_DATABASE]
            # Test the connection
            # self.client.admin.command('ping')
            return self.database
        
        except Exception as e:
            raise ConnectionError(f"ERROR: From DBconnection.connection : {e}")
        
    def disconnect(self):
        if self.client:
            self.client.close()
        

if __name__ == "__main__":
    mydb = DBconnection()
    coll = mydb.connection()
    my = coll[config.MONGODB_COLLECTION]
    x = my.find()
    for i in x :
        print(i)
        

    

        
    
