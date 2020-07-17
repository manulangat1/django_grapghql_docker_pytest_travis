import graphene 
import grareact.ingredients.schema as ISchema

class Query(ISchema,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)