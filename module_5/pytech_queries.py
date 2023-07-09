from pymongo import MongoClient


client = MongoClient("mongodb+srv://admin:admin@cluster0.vxyt6xi.mongodb.net/?retryWrites=true&w=majority")

db = client["PyTech"]

students = db["students"]

docs = students.find({})
for doc in docs:
    print(doc)

student = students.find_one({"student_id": "1007"})
print(student)
