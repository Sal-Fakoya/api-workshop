
# API-Workshop: (Application Programming Interface)

"""
--> An API is a function that works with data from an external source.
    For example, we can have a function that uses data stored from the internet.
    
--> AMAZON example:
    Log in account on amazon: 
        --> Takes your detail
        --> Checks your information in the database and see if it exists or not.
        --> Re-directs you if it does not exist
        
--> Basically, it allows you to send input and get result from the database.
--> For example, we can use Firebase to create a database online for free


Set up firebase database first: Then:
1. Set up node.js
2. Create a configuration file for your database example, firebase database
3. Get, Post, Put, and Delete:
    Get/Fetches the data from the data base: gives you a dictionary of your ide and name of your user.
    Post: takes the data from the user and sends the user data to the database, it create data in the database.
        Then call the get function in the post function to update the data being fetched.
        Remember to add the create in the url if creating new data
        
    Put: puts data in the database
    Delete: Deletes data in the database
    
API Components:
--> Headers: security data passed from the user to API call to make sure the data is valid
    Headers parameters include: Accept, User Agent. 
    Headers make the data being sent to the dataase more secure
    User agent: source where the data is coming from, such as Thunderclient or Postman
    
--> Query: is a different format to send input to a data. We use an API "customized" url.

--> body


API Request flow:
1. client sends request
2. server received client request and sends input to database to retrieve or modify data

DEBUGGING: STATUS CODES:
1. 200 level: API request successful
2. 400 level: request failed due to sending invalid input 
    ex: wrong HTTP method, missing input fields, wrong input data type, etc.
3. 500: reques failed due to server error or api error.


REST APIs:
--> Have statelessness: when you make an api call, the server clears the list of the api calls so that 
    the server doesn't store client info between reqs.
--> config.js: 


localhost3001: local host of the url server.


    

    


"""































