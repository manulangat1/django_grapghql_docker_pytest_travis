import graphene 

from graphene_django.types import DjangoObjectType 

from .models import Category,Ingredient,Post,Tag

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class PostType(DjangoObjectType):
    class Meta:
        model = Post 

class TagType(DjangoObjectType):
    class Meta:
        model = Tag

class Query(object):
    category = graphene.Field(CategoryType,id=graphene.Int(),name=graphene.String())
    all_categories = graphene.List(CategoryType)
    all_post = graphene.List(PostType)
    all_tag = graphene.List(TagType)
    all_ingredients = graphene.List(IngredientType)
    ingredient = graphene.Field(
        IngredientType,
        id=graphene.Int(),
        name=graphene.String()
    )


    def resolve_all_categories(self,info,**kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self,info,**kwargs):
        return Ingredient.objects.select_related('category').all()

    def resolve_all_post(self,info,**kwargs):
        return Post.objects.select_related('Tag').all()
    def resolve_all_tag(self,info,**kwargs):
        return Tag.objects.all()
    def resolve_category(self,info,**kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)
        if name is not None:
            return Category.objects.get(name=name)
        return None 

    def resolve_ingredient(self,info,**kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Ingredient.objects.get(pk=id)
        if name is not None:
            return Ingredient.objects.get(name=name)

        return None