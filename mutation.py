import graphene
from type import Student
from data import students


class addStudent(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        id = graphene.String()
        age = graphene.String()

    student = graphene.Field(lambda: Student)

    def mutate(root, info, name, id, age):
        student = Student(name=name, id=id, age=age)
        students.append({
            "name": name,
            "id": id,
            "age": age,
        })
        return addStudent(student=student)


class updateStudent(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        id = graphene.String()
        age = graphene.String()

    student = graphene.Field(lambda: Student)

    def mutate(root, info, name, id, age):
        student = Student(name=name, id=id, age=age)
        old_student = list(
            filter(lambda student: student["id"] == id, students))[0]
        students.remove(old_student)
        students.append({
            "name": name,
            "id": id,
            "age": age,
        })
        return updateStudent(student=student)


class deleteStudent(graphene.Mutation):
    class Arguments:
        id = graphene.String()
    student = graphene.Field(lambda: Student)

    def mutate(root, info, id):
        old_student = list(
            filter(lambda student: student["id"] == id, students))[0]
        student = Student(
            name=old_student["name"], id=old_student["id"], age=old_student["age"])
        students.remove(old_student)

        return deleteStudent(student=student)
