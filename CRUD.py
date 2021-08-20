from pymongo import MongoClient

#Class definition of animal shelter object
class AnimalShelter(object):

    #Constructor
    def __init__(this, username, password):
        this.client = MongoClient('mongodb://%s:%s@localhost:37237/AAC' % (username, password))
        this.db = this.client['AAC']
        this.fields = {
            '_id':0,
            '1':0,
            'age_upon_outcome':0,
            'datetime':0,
            'monthyear':0,
            'age_upon_outcome_in_weeks':0,
            'type':0      
        }

    #Method which is used to insert a document into animals collection
    def create(this, doc):
        
        #Validate method parameters
        if (doc is None):
            raise Exception('\nERROR: No valid data was specified.')

        #Attempt to insert data
        inserted = this.db.animals.insert_one(doc)    
        if (inserted is None):
            raise Exception('\nERROR: Failed to insert document: %s' % (doc))

    #Method which is used to read records from animals collection
    def read(this, filter = None):
        if (filter is None):
            raise Exception('\nERROR: No valid data was specified.')
              
        #Retrieve documents by filter
        return this.db.animals.find(filter, this.fields)
        
    #Method which is used to update records from animals collection
    def update(this, filter = None, values = None):
        
        #Validate method parameters
        if (filter is None):
            raise Exception('\nERROR: No valid filter was specified.')
        if (values is None):
            raise Exception('\nERROR: No valid values were specified.')  
        
        #Update records based on specified filter and values
        updated = this.db.animals.update_one(filter, values)
        if (updated is None):
            raise Exception('\nERROR: Failed to update document based on filter: %s' % (filter))
          
    #Method which is used to delete records in the animals collection
    def delete(this, filter = None):
        
        #Validate method parameters
        if (filter is None):
            raise Exception('\nERROR: No valid filter was specified.')
        
        #Delete records basd on specified filter
        deleted = this.db.animals.delete_many(filter)
        if (deleted is None):
            raise Exception('\nERROR: Failed to delete records based on filter: %s' % (filter))