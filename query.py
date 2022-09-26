from graphene import ObjectType
from data import students

print("in query", students)


class Query(ObjectType):
    def resolve_all_Student(root, info):
        return students

    def resolve_single_Student(root, info, id):
        return list(filter(lambda student: student["id"] == id, students))[0]
