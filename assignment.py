def make_student(name, scores):
    average = sum(scores) / len(scores) if scores else 0
    return {
        'name': name,
        'scores': scores,
        'average': average
    }

def class_summary(students):
    if not students:
        return None
    top_student = max(students, key=lambda x: x['average'])
    return top_student['name']

student1 = make_student("Bernard", [85, 90, 78])
student2 = make_student(name="Jean", scores=[92, 88, 95])
student3 = make_student("Pierre", scores=[80, 85, 82])
students = [student1, student2, student3]

top_name = class_summary(students)

print(f"The top student is: {top_name}")