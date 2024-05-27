import strawberry
from .types.playlist import Playlist
from .types.track import Track
from mock_spotify_rest_api_client.api.playlists import get_featured_playlists
from mock_spotify_rest_api_client.api.playlists import get_playlist


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

    @strawberry.field(description="Retrieves a specific playlist.")
    async def playlist(self, id: strawberry.ID, info: strawberry.Info) -> Playlist | None:
        spotify_client = info.context["spotify_client"]
        data = await get_playlist.asyncio(client=spotify_client, playlist_id=id)

        if data:
            return Playlist(
                id=strawberry.ID(data.id),
                name=data.name,
                description=data.description,
                tracks=[
                    Track(
                        id=strawberry.ID(item.track.id),
                        name=item.track.name,
                        duration_ms=item.track.duration_ms,
                        explicit=item.track.explicit,
                        uri=item.track.uri
                    )
                    for item in data.tracks.items
                ]
            )

        return None
    
"""
The above class is equal to the following GraphQL schema

type Query {
  hello: String!
}
"""