from graphene import ObjectType, String


class Student(ObjectType):
    name = String()
    id = String()
    age = String()
