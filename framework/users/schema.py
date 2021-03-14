import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from users.models import User, Team


class UserType(DjangoObjectType):
    class Meta:
        model = User


class TeamType(DjangoObjectType):
    class Meta:
        model = Team

class AuthInput(graphene.InputObjectType):
    username = graphene.String()
    password = graphene.String()

class HasUser(graphene.Mutation):
    class Arguments:
        input = AuthInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, input=None):
    
        user_instance = User.objects.get(pk=input.username)
        ok = user_instance.password == input.password
        return HasUser(ok=ok, user=user_instance)

class Query(ObjectType):
    teams = graphene.List(TeamType)

    def resolve_teams(self, info, **kwargs):
        return Team.objects.all()

class Mutation(graphene.ObjectType):
    has_user = HasUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)