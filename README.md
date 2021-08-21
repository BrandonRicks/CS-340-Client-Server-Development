# CS 340 PROJECT README: GRAZIOSO SALVARE PROGRAM

## About the Project/Project Title
Grazioso Salvare is a company that trains dogs for search-and-rescue operations, and requires a method to identify and categorize potential dogs for this purpose. To facilitate the company’s needs, this project is intended to implement functionality and interaction between client and server; specifically, an application that “can work with existing data from the animal shelters to identify and categorize available dogs”. 

## Functionality
This project combines the client side, server side, and middleware into full stack development. This project allows for filtered viewing of data, retrieved from the database using a Python module, and shown in an easy-to-use web dashboard. This dashboard comes with company branding, as well as widgets that offer visual representation of the data. The dashboard is also interactive, allowing for filtering options that respond dynamically.

## Tools Used
### Database is in MongoDB (https://www.mongodb.com/). 

*MongoDB is a great tool for use in scalable applications and projects emphasizing agile methodologies. It is both document-oriented and NoSQL, which offers great flexibility and stability with many concurrent users. Combined with Python, database applications and modules can be developed quickly and relatively easily.*

### Middleware was created with Python (https://www.python.org/). 

*Combined with built-in functionality to MongoDB, Python is a great choice for programming language. The driver library PyMongo allows for compatibility between dictionaries and lists, allowing for easy manipulation and iteration functionality.*

### Client-side dashboard was created with Jupyter Notebook (https://jupyter.org/). 

*Jupyter Notebook is part IDE, part data science environment. It supports many languages, and as a web source application, offers ease-of-use and access as a web tool.*

### Maps, graphs, and UI were created with Plotly and Dash (https://plotly.com/) 

*Plotly is a graphing and analytics library that is functional with Python, among many other languages. Dash is a Python framework that is used for building web-based applications. Combined, these tools offer graphing and widgets within a web-based dashboard.*

## Steps To Project Completion

### Database Commands (Mongo Shell and Screenshots): MongoImport and Authentication
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

### CRUD Python Module: CREATE, READ, UPDATE, DELETE Functionality
This portion covers the CRUD functionality of the Python module, which will serve as the middleware “glue” for this software. CRUD is an acronym for CREATE, READ, UPDATE, and DELETE, and are the basic operations to manipulate the database and view its contents. The methods for this functionality are shown in screenshots below:

Create:

![Screenshot_71](https://user-images.githubusercontent.com/79807877/130303183-86d3599a-2ead-4daf-bb91-69365f504e00.png)

Read:

![Screenshot_72](https://user-images.githubusercontent.com/79807877/130303187-07ea2f55-644c-48ff-8e93-4715d757d10f.png)

Update:

![Screenshot_73](https://user-images.githubusercontent.com/79807877/130303189-93e8aff6-7de1-4c41-91ad-b66ff8c018bc.png)

Delete:

![Screenshot_74](https://user-images.githubusercontent.com/79807877/130303192-c274f8c7-c612-4473-be3d-075ca92f6785.png)

### Dashboard Interactivity
This portion covers the interactivity of the dashboard, serving as the client-side. The user is able to interact with the dashboard and move around the map, as well as select individual data points within the dashboard. The dashboard also allows for filtering, based on 5 key requirements: Water Rescue, Mountain or Wilderness Rescue, Disaster or Individual Tracking, Elderly 15+, and a reset function, returning all widgets to an unfiltered state. These requirements are shown below:

Water Rescue

![Screenshot_66 (2)](https://user-images.githubusercontent.com/79807877/130303258-4785ffd8-7a40-465f-87a8-de528db0b612.png)

Mountain Rescue

![Screenshot_67 (2)](https://user-images.githubusercontent.com/79807877/130303261-0272e5eb-a618-4726-9b50-37a4a5162625.png)

Disaster Rescue

![Screenshot_68 (2)](https://user-images.githubusercontent.com/79807877/130303268-0c2f88f6-20e5-4bf6-97c6-3d6c4469c39a.png)

Elderly 15+

![Screenshot_69 (2)](https://user-images.githubusercontent.com/79807877/130303270-9bb6f983-ba71-4aaf-bd78-7df6f70a18e3.png)

Reset
 
![Screenshot_70 (2)](https://user-images.githubusercontent.com/79807877/130303278-f39a27cb-bd95-4818-b39b-530ae4f89e47.png)

## Challenges/Potential Issues

The biggest challenge I faced making this project was functionality in the dashboard. I ran into occasional issues with connection as well, primarily due to connection between the dashboard and the database. Below are a few solutions to such issues:

*Authorization/Database Connectivity Issues*

If a user runs into issues with authorization when running the dashboard, check these possible solutions:

- Make sure the username and password exist 
- Make sure the username and password are correct
- Check the port and host information
- Make sure the dashboard and/or database process closed successfully. If not seek out the process id and stop the process
- If you are able to start the database, but not connect, attempt to unalias mongo, and re-enter the port, using the following commands: 
  - ```unalias mongo``` 
  - ```mongo --port <PORT#>```

## Contact
Brandon Ricks

brandon.ricks@snhu.edu

CS-340 Client/Server Development
