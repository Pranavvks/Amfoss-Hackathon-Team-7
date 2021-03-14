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

    def resolve_teams(self, info, **kwargs):
        return Team.objects.all()

class Mutation(graphene.ObjectType):
    has_user = HasUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)