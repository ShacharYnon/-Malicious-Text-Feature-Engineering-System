import os

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "IranMalDB")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "tweets")
MONGODB_USERNAME = os.getenv("MONGODB_USER" ,"IRGC")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD" ,"iraniraniran")