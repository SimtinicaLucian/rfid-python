import pymongo
import signal 
import time
import json
from datetime import date 
import datetime

# connection with MongoDB
myclient = pymongo.MongoClient("localhost",27017)
mydb = myclient["accessDB"]
myuser = mydb["user"]
mylog = mydb["log"]


while True:
    print("----------------")
    print("Option Menu");
    print("add - Add user")
    print("delete - Delete user")
    print("view - View all users")
    print("logs - View all logs")
    print("----------------")
    option = input("Enter your option:")

    if(option == "add"):
        name = input("Enter name:")
        uid = input("Enter UID:")
        addQuery = { "uid": uid, "name" : name }
        myuser.insert_one(addQuery) # insert user in database
        print("User was added")
        
    elif(option == "delete"):
        name = input("Enter name:")
        deleteQuery = {"name" : name }
        myuser.delete_one(deleteQuery) # delete user in database
        print("User was deleted")
        
    elif(option == "view"):
        list = myuser.find({}); # print all users
        for document in list:
            print(document);
    elif(option == "logs"):
        list = mylog.find({});
        for document in list:
            print(document);
            
        

