import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            client = pymongo.MongoClient("mongodb")  # your mongodb URL
            database = client['azure']
            collection = database['test']

            rec_id1 = collection.insert_one(eval(request))
            return func.HttpResponse(req.get_body())
        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )