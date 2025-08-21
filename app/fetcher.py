from app.connection import DBconnection
from app import config

class Dal:

    def __init__(self):
        self.dbconnection = DBconnection()
        self.db = self.dbconnection.connection()
        self.collection = self.db[config.MONGODB_COLLECTION]


    def get_all(self):
        try:
            results = self.collection.find({},{"_id":0})
            return [result for result in results ]
        except Exception as e:
            print(f"Error getting all documents: {e}")
            return []
        

# if __name__ == "__main__":
#     my = Dal()
#     data = my.get_all()
#     df = pd.DataFrame(data)
#     print (df)  

    