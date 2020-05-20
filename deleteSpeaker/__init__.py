import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            client = pymongo.MongoClient("mongodb://testaccount111:9fR5dkHJcUwVsoEqiQM194k9qGfBQdg5ruZfbb3dsvc51J1rYUwPTWu9WWUImHyZXkbGygGKxsKc7yd6MuYPYQ==@testaccount111.documents.azure.com:10255/?ssl=true&replicaSet=globaldb")  # your mongodb URL
            database = client['azure']
            collection = database['test']
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
