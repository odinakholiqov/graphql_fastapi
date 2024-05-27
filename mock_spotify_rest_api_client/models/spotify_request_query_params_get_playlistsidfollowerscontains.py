from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETPlaylistsidfollowerscontains")


@_attrs_define
class SpotifyRequestQueryParamsGETPlaylistsidfollowerscontains:
    """
    Attributes:
        ids (str):
    """

    ids: str

    def to_dict(self) -> Dict[str, Any]:
        ids = self.ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ids": ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = d.pop("ids")

        spotify_request_query_params_get_playlistsidfollowerscontains = cls(
            ids=ids,
        )

        return spotify_request_query_params_get_playlistsidfollowerscontains
