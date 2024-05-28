import strawberry
from .playlist import Playlist



@strawberry.type
class AddItemsToPlaylistPayload:
    code: int = strawberry.field(description="code")
    success: bool = strawberry.field(description="was sucessfull")
    message: str = strawberry.field(description="some msg")
    playlist: Playlist | None = strawberry.field(description="some msg")
