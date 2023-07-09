from pymongo import MongoClient


client = MongoClient("mongodb+srv://admin:admin@cluster0.vxyt6xi.mongodb.net/?retryWrites=true&w=majority")

db = client["PyTech"]

students = db["students"]


student1 = {
    "student_id": "1007",
    "first_name": "John",
    "last_name": "Doe"
}

student2 = {
    "student_id": "1008",
    "first_name": "Jane",
    "last_name": "Smith"
}

student3 = {
    "student_id": "1009",
    "first_name": "Alex",
    "last_name": "Johnson"
}

student1_id = students.insert_one(student1).inserted_id
student2_id = students.insert_one(student2).inserted_id
student3_id = students.insert_one(student3).inserted_id


print(student1_id)
print(student2_id)
print(student3_id)
