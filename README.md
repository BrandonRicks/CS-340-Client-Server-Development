# CS 340 PROJECT README: GRAZIOSO SALVARE PROGRAM

## About the Project/Project Title
Grazioso Salvare is a company that trains dogs for search-and-rescue operations and requires a method to identify and categorize potential dogs for this purpose. To facilitate the company’s needs, this project is intended to implement functionality and interaction between client and server; specifically, an application that “can work with existing data from the animal shelters to identify and categorize available dogs”. 

## Database Commands (Mongo Shell and Screenshots): MongoImport and Authentication
First, we import a CSV file containing the information required for the database. This is done through the following command:
```mongoimport --port <PORT#> --db AAC --collection animals ./aac_shelter_outcomes.csv```

This command will import the .csv file into the database. A successful import is shown below:

![image](https://user-images.githubusercontent.com/79807877/129285096-c03c521c-2ed0-4d07-91e2-878bad9e8fc1.png)

We will then create an administrator account and a user account within mongo shell to ensure proper user authentication to this database. First, an admin account is created within admin database, using the following commands:

```use admin // This will change to the admin database
db.createUser ({ 
user: "admin",
pwd: passwordPrompt(),  // This will create a prompt for entering the password
roles: [{ role: "userAdminAnyDatabase", db: "admin" }, “readAnyDatabase"]
})
```

We run a similar command to create a user for the “AAC” database:

```use AAC // This will change to the proper database where you want the user
db.createUser ({ 
user: "aacuser",
pwd: passwordPrompt(),  // This will create a prompt for entering the password
roles: [{ role: "readWrite", db: "AAC" }]
})
```

Login is done using the following command:

```Mongo --authenticationDatabase “<DATABASE>” -u “<USERNAME>” -p```

Confirmation of account login is shown below for both “admin” and “aacuser”:
 
 ![image](https://user-images.githubusercontent.com/79807877/129285383-6bdd14ad-4034-459b-97c5-3dcfd608c928.png)

 ![image](https://user-images.githubusercontent.com/79807877/129285387-033018f2-19fa-487b-a503-c266d9960e9f.png)

## CRUD Python Module: CREATE, READ, UPDATE, DELETE Functionality
This portion covers the CRUD functionality of the Python module, which will serve as the middleware “glue” for this software. CRUD is an acronym for CREATE, READ, UPDATE, and DELETE, and are the basic operations to manipulate the database and view its contents. The methods for this functionality are shown in screenshots below:

Create:

 ![image](https://user-images.githubusercontent.com/79807877/129285434-f4fa33fa-636f-4bda-ac81-bc3619e54b28.png)

Read:

 ![image](https://user-images.githubusercontent.com/79807877/129285439-c79a433d-a0f1-4b77-af96-a1a383332d08.png)

Update:

 ![image](https://user-images.githubusercontent.com/79807877/129285445-da9b15fb-2c8d-4073-b478-d47a22e22fa9.png)

Delete:

 ![image](https://user-images.githubusercontent.com/79807877/129285448-d5d0362d-1ef5-4833-9ab5-7e0300796660.png)

## CRUD Python Module (Python Code and Screenshots): Script to Test CRUD Functionality
This portion covers the test script that will test each of these methods to ensure they’re working properly. This test script will run through Jupyter Notebook and output a confirmation. There will also be screenshots showing these modifications within the database. 
Create test code:

![image](https://user-images.githubusercontent.com/79807877/129285517-ac69422f-e734-4bec-b454-0edae902e691.png)
 
Create test output:

![image](https://user-images.githubusercontent.com/79807877/129285523-532e090b-fe5e-4469-95e2-81412965921c.png)
 
Create confirmation:

![image](https://user-images.githubusercontent.com/79807877/129285538-7b8f725e-8394-4c7d-87da-5c8117440fea.png)

Read test code:

![image](https://user-images.githubusercontent.com/79807877/129285552-b76a9cdf-b1c8-4ed4-87e5-2c579897e942.png)

Read output:

![image](https://user-images.githubusercontent.com/79807877/129285565-9d882423-55f4-461c-809e-c6dee154de19.png)

Update test code:

![image](https://user-images.githubusercontent.com/79807877/129285583-53b20cb5-410e-4fda-be43-fcf38df2793f.png)

Update output:

![image](https://user-images.githubusercontent.com/79807877/129285593-7019e409-b90c-40fd-b37a-08c54c2f6e1d.png)
 
Update confirmation:

![image](https://user-images.githubusercontent.com/79807877/129285605-fef7d571-c67f-4f17-87ba-e90da0de54e6.png)
 
Delete test code:

![image](https://user-images.githubusercontent.com/79807877/129285624-93a7923b-d66b-4cac-839f-2d57cd3b9ed8.png)

Delete output:

![image](https://user-images.githubusercontent.com/79807877/129285633-9b73c16e-7f99-4708-9395-61c9bd101ec0.png)

Delete confirmation:

![image](https://user-images.githubusercontent.com/79807877/129285642-64863ec6-7450-4966-92fb-daa86577d451.png)

As shown in the above screenshots, the test code creates, reads, updates, and deletes. First, a new entry is created using “data”. When reading this data, it is searched using the animal_id, and the returned to the user. Updating alters the name of the test data using the animal_id, and delete removes the data using the animal_id.

## Contact
Brandon Ricks


