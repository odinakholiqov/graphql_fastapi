import strawberry

from .query import Query
from .mutation import Mutation
from .types.playlist import Playlist


schema = strawberry.Schema(query=Query, types=[Playlist], mutation=Mutation)