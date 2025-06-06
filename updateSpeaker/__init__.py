import azure.functions as func
import pymongo
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            client = pymongo.MongoClient("mongodb://testaccount111:9fR5dkHJcUwVsoEqiQM194k9qGfBQdg5ruZfbb3dsvc51J1rYUwPTWu9WWUImHyZXkbGygGKxsKc7yd6MuYPYQ==@testaccount111.documents.azure.com:10255/?ssl=true&replicaSet=globaldb")  # your mongodb URL
            database = client['azure']
            collection = database['test']
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

