import strawberry
from .types.playlist import Playlist

def get_hello():
    return "Hello!"


# List what can be asked from the GQL server
@strawberry.type(description=None, name=None)
class Query:
    hello: str = strawberry.field(resolver=get_hello, description=None, name=None)

    @strawberry.field(
        description="Playlists hand-picked to be featured to all users."
    )
    def featured_playlist(self) -> list[Playlist]:
        return [
            Playlist(id="1", name="GraphQL Groovin'", description=None),
            Playlist(id="2", name="Graph Explorer Jams", description=None),
            Playlist(id="3", name="Interpretive GraphQL Dance", description=None),
        ]

"""
The above class is equal to the following GraphQL schema

type Query {
  hello: String!
}
"""