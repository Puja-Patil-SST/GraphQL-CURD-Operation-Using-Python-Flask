from dataclasses import Field
from msilib import schema
import graphene
from mutation import addStudent, updateStudent, deleteStudent
from query import Query
from type import Student
from graphene import Field, String, List, Schema


class MyMutations(graphene.ObjectType):
    add_Student = addStudent.Field()
    update_Student = updateStudent.Field()
    delete_Student = deleteStudent.Field()


class MyQuery(Query):
    student = Field(Student)
    single_Student = Field(Student, id=String())
    all_Student = List(Student)


schema = Schema(query=MyQuery, mutation=MyMutations)

# result = schema.execute(
#     '''
#     query{
#         singleStudents(id:"2"){
#             name
#             id
#             age
#         }
#     }
#     '''
# )
# print(result.data)

result = schema.execute(
    '''
    mutation{
        addStudents(id:"5", name:"aaa", age:"11"){
            student{
            name
            id
            age
            }
        }
    }
    '''
)
print(result.data)
