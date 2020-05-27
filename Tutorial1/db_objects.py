from pymongo import MongoClient
import urllib
import csv

limit=5

with open("cred.txt")as f1:
    datarow=csv.reader(f1,delimiter=",")
    for row in datarow:
     id=row[0]
     pwd=row[1]
    

class db_object:
    def __init__(self,db_name,collection_name,sname,cname):
        client=MongoClient("mongodb+srv://"+id+":"+urllib.parse.quote_plus(pwd)+"@cluster0-lymvb.mongodb.net/test?retryWrites=true&w=majority")
        db=client[db_name]
        self.collection=db[collection_name]
        self.student_name=sname
        self.course_name=cname
        self.course_count=self.collection.count_documents({"course_name": self.course_name})
        
        
        
    def insert_into_collection(self):
        if (self.course_count<limit):
            self.collection.insert_one({"course_name": self.course_name,"student_name": self.student_name})
            return 'created'
            
            
        else:
            return 'not created'
        
    def read_from_collection(self):
        pass