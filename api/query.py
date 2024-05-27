import strawberry
from .types.playlist import Playlist
from mock_spotify_rest_api_client.api.playlists import get_featured_playlists


def get_hello():
    return "Hello!"


# List what can be asked from the GQL server
@strawberry.type(description=None, name=None)
class Query:
    hello: str = strawberry.field(resolver=get_hello, description=None, name=None)

    @strawberry.field(
        description="Playlists hand-picked to be featured to all users."
    )
    async def featured_playlist(self, info: strawberry.Info) -> list[Playlist]:
        spotify_client = info.context["spotify_client"]
        data = await get_featured_playlists.asyncio(client=spotify_client)

        items = data.playlists.items

        playlists = [
            Playlist(
                id=strawberry.ID(playlist.id),
                name=playlist.name,
                description=playlist.description
            ) for playlist in items] 
        
        return playlists

"""
The above class is equal to the following GraphQL schema

type Query {
  hello: String!
}
"""