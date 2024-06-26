from typing import TYPE_CHECKING, Any, Dict, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl


T = TypeVar("T", bound="SpotifyObjectPlaylistEpisodeArtist")


@_attrs_define
class SpotifyObjectPlaylistEpisodeArtist:
    """
    Attributes:
        external_urls (SpotifyObjectExternalUrl):
        href (str):
        id (str):
        name (str):
        type (Literal['show']):
        uri (str):
    """

    external_urls: "SpotifyObjectExternalUrl"
    href: str
    id: str
    name: str
    type: Literal["show"]
    uri: str

    def to_dict(self) -> Dict[str, Any]:
        external_urls = self.external_urls.to_dict()

        href = self.href

        id = self.id

        name = self.name

        type = self.type

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "external_urls": external_urls,
                "href": href,
                "id": id,
                "name": name,
                "type": type,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl

        d = src_dict.copy()
        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        href = d.pop("href")

        id = d.pop("id")

        name = d.pop("name")

        type = cast(Literal["show"], d.pop("type"))
        if type != "show":
            raise ValueError(f"type must match const 'show', got '{type}'")

        uri = d.pop("uri")

        spotify_object_playlist_episode_artist = cls(
            external_urls=external_urls,
            href=href,
            id=id,
            name=name,
            type=type,
            uri=uri,
        )

        return spotify_object_playlist_episode_artist
