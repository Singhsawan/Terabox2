# funcs
import pymongo,os


# ------------Database----------
DB_URL = os.environ.get("DB_URL", "mongodb+srv://mdisk:mdisk@cluster0.5f5kz5s.mongodb.net/?retryWrites=true&w=majority")

mongo = pymongo.MongoClient(DB_URL)
db = mongo["tarabox"]
dbcol = db["users"]



def total_user() -> str:
    user = dbcol.count_documents({})
    return str(user)


# insert user data
def insert(chat_id,NAME):
    user_id = int(chat_id)
    user_det = {"_id": user_id,"NAME": NAME, "API": None, "FOOTER": None, "INVITE_LINK": None,"DOMAIN":"urllinkshort.in"}
    try:
        dbcol.insert_one(user_det)
    except:
        return True

#find any data from just query
def find_any(id,query):
    id = {"_id": id}
    x = dbcol.find(id)
    for i in x:
        try:
            result = i[f"{query}"]
            
        except:
            result = None
    
        return result


    # return dbcol.find_one({"_id": id})

   
#add Dynamic DATA
def addDATA(chat_id,KEY, VALUE):
    dbcol.update_one({"_id": chat_id}, {"$set": {f"{KEY}": VALUE}})


#Delete DATA Dynamic
def delDATA(chat_id,KEY):
    dbcol.update_one({"_id": chat_id}, {"$set": {f"{KEY}": None}})

def getid():
    values = []
    for key in dbcol.find():
        id = key["_id"]
        values.append((id))
    return values


def delete(id):
    dbcol.delete_one(id)

