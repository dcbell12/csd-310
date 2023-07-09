import pymongo


connection_string = "mongodb+srv://admin:admin>@cluster0.vxyt6xi.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)
db = client.pytech
students = db.students


print("-- DISPLAYING STUDENTS DOCUMENTS --")
for student in students.find():
    print(student)


students.update_one({"student_id": 1007}, {"$set": {"last_name": "Apple"}})


print("-- DISPLAYING STUDENT 1007 --")
student_1007 = students.find_one({"student_id": 1007})
print(student_1007)
