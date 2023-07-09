import pymongo


connection_string = "mongodb+srv://admin:admin@cluster0.vxyt6xi.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)
db = client.pytech
students = db.students


print("-- DISPLAYING STUDENTS DOCUMENTS --")
for student in students.find():
    print(student)


new_student = {
    "student_id": 1010,
    "first_name": "Dylan",
    "last_name": "Smith",
    "enrollments": [
        {
            "term": "Fall 2023",
            "gpa": 3.8,
            "start_date": "2023-09-01",
            "end_date": "2023-12-15",
            "courses": [
                {
                    "course_id": "CS101",
                    "course_name": "Introduction to Computer Science",
                    "credits": 3
                },
                {
                    "course_id": "MATH101",
                    "course_name": "Calculus I",
                    "credits": 4
                }
            ]
        }
    ]
}
students.insert_one(new_student)


print("-- DISPLAYING STUDENT 1010 --")
student_1010 = students.find_one({"student_id": 1010})
print(student_1010)


students.delete_one({"student_id": 1010})


print("-- DISPLAYING STUDENTS DOCUMENTS AFTER DELETION --")
for student in students.find():
    print(student)
