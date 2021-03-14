import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from users.models import User, Team, Task


class UserType(DjangoObjectType):
    class Meta:
        model = User


class TeamType(DjangoObjectType):
    class Meta:
        model = Team

class TaskType(DjangoObjectType):
    class Meta:
        model = Task

class AuthInput(graphene.InputObjectType):
    username = graphene.String()
    password = graphene.String()

class TasksInput(graphene.InputObjectType):
    username = graphene.String()

class HasUser(graphene.Mutation):
    class Arguments:
        input = AuthInput(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input=None):
        try:
            user_instance = User.objects.get(pk=input.username)
            ok = user_instance.password == input.password
            return HasUser(ok=ok)
        except Exception:
            ok = False
            return HasUser(ok=ok)

        

class Query(ObjectType):
    teams = graphene.List(TeamType)
    tasks = graphene.List(TaskType, username = graphene.String())
    user = graphene.Field(UserType, username = graphene.String())

    def resolve_teams(self, info, **kwargs):
        return Team.objects.all()
    
    def resolve_tasks(self, info, **kwargs):
        username = kwargs.get('username')

        if username is not None:
            return Task.objects.filter(assigned=username)
        return None

    def resolve_user(self, info, **kwargs):
        username = kwargs.get('username')
        if username is not None:
            return User.objects.get(pk=username)
    

class Mutation(graphene.ObjectType):
    has_user = HasUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)