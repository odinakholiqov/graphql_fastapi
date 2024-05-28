import strawberry
from .playlist import Playlist


@strawberry.input
class AddItemsToPlaylistInput:
    playlist_id: strawberry.ID = strawberry.field(description="Playlist ID to add tracks")
    uris: list[str] = strawberry.field(description="uris to musics")