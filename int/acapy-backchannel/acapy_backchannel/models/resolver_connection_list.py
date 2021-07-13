from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.resolver_connection import ResolverConnection

T = TypeVar("T", bound="ResolverConnectionList")


@attr.s(auto_attribs=True)
class ResolverConnectionList:
    """ """

    results: List[ResolverConnection]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()

            results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = ResolverConnection.from_dict(results_item_data)

            results.append(results_item)

        resolver_connection_list = cls(
            results=results,
        )

        resolver_connection_list.additional_properties = d
        return resolver_connection_list

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
