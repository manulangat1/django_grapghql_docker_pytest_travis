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
    post = graphene.Field(PostType,id=graphene.Int())
    tag = graphene.Field(TagType,id=graphene.Int())
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
        return Post.objects.all()
    def resolve_all_tag(self,info,**kwargs):
        return Tag.objects.all()
    def resolve_post(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Post.objects.get(pk=id)
        return None
    def resolve_tag(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Tag.objects.get(pk=id)
        return None
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

class TagInput(graphene.InputObjectType):
    id = graphene.Int()
    name = graphene.String()

class PostInput(graphene.InputObjectType):
    id = graphene.Int()
    title = graphene.String()
    tags = graphene.List(TagInput)
    notes = graphene.String()
# class TagInput
class CreatePost(graphene.Mutation):
    class Arguments:
        input = PostInput(required=True)
    post = graphene.Field(PostType)
    def mutate(self,info,input=None):
        tags = []
        for tag in input.tags:
            tagS = Tag.objects.get(pk=tag.id)
            if tags is not None:
                tags.append(tagS)
            post_instance = Post(title=input.title,notes=input.notes)
            post_instance.save()
            print(tags)
            post_instance.tag.add(tagS)
            return CreatePost(post=post_instance)

class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = PostInput(required=False)
    post = graphene.Field(PostType)

    def mutate(self,info,id,input=None):
        tags = []
        post_instance = Post.objects.get(pk=id)
        if post_instance:
            for tag in input.tags:
                tagS = Tag.objects.get(pk=tag.id)
                if tagS is not None:
                    tags.append(tagS)
            post_instance.title = input.title
            post_instance.notes = input.notes
            post_instance.save()
            post_instance.tag.set(tags)
            return UpdatePost(post=post_instance)


class TagPost(graphene.Mutation):
    class Arguments:
        input = TagInput(required=True)

    tag = graphene.Field(TagType)

    def mutate(self,info,input=None):
        tag_instance = Tag(name=input.name)
        tag_instance.save()
        return TagPost(tag=tag_instance)

class TagUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = TagInput(required=True)
    tag = graphene.Field(TagType)
    def mutate(self,info,id,input=None):
        tag_instance = Tag.objects.get(pk=id)
        if tag_instance:
            tag_instance.name = input.name
            return TagUpdate(tag=tag_instance)
        return "Not Found"
class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    tag_post = TagPost.Field()