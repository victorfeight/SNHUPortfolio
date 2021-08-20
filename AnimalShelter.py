from pymongo import MongoClient # this import allows to connect to our mongodb database
from bson.objectid import ObjectId #query using an ObjectID


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(
        self, username=None, password=None
    ):  # provide default values for object
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        if password and username:
            self.client = MongoClient(
                #'mongodb://%s:%s@127.0.0.1:49727/AAC' % (username, password)
                'mongodb://%s:%s@localhost:27017/AAC' % (username, password)
            )
        else:
            self.client = MongoClient(
                "mongodb://127.0.0.1:49727"
            )
        self.database = self.client["AAC"]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert_dictionary = self.database.animals.insert_one(
                data
            )  # data should be dictionary
            if insert_dictionary != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Method to implement the R in CRUD
    def read(self, search_crit=None):  # default search criteria is empty
        if search_crit:  # search if criteria exists
            animal_query = self.database.animals.find(
                search_crit, {"_id": False}
            )  # return all documents matching search critera, omitting ID of each document
        else:  # return all documents if no criteria exists
            animal_query = self.database.animals.find({}, {"_id": False})
        return animal_query
    
    # Method to implement the U in CRUD (Update)
    # Use save function to update object according to _id property
    def update(self, save):
        if save is not None:
            if save:
                result = self.database.animals.insert_one(save)
            return result;
        else:
            raise Exception("Nothing to update, save is empty")
            
    
    # Method to implement the D in CRUD (Delete)
    def delete(self, remove):
        if remove is not None:
            if remove:
                result = self.database.animals.delete_one(remove)
        else:
            raise Exception("Nothing to delete, remove is empty")
