from abc import abstractmethod, ABCMeta
from typing import Dict, Optional, Tuple, TypeVar, Union


class _ReturnType(metaclass=ABCMeta):

    @abstractmethod
    def assert_is_superset(self, _type: Optional["_ReturnType"]) -> None:
        ...  # pragma: no cover

    @abstractmethod
    def downcast_result(self, result: Tuple[Tuple, Dict]) -> Tuple[Tuple, Optional[Dict]]:
        ...  # pragma: no cover

    @staticmethod
    def _is_optional_type(_type) -> bool:
        # Optional[str] == Union[str, NoneType]
        return (
            hasattr(_type, "__origin__")
            and _type.__origin__ is Union
            and len(_type.__args__) == 2
            and _type.__args__[1] is type(None)
        )  # noqa: E721


    @staticmethod
    def _instance_of(value, _type) -> bool:
        result = True
        if hasattr(_type, "__origin__") and _type.__origin__ in {list, tuple, set}:
            if not isinstance(value, _type.__origin__):
                return False
            for t in _type.__args__:
                if t is Ellipsis:
                    continue
                    """
                    elif t.__class__ is TypeVar:
                        return False
                    """
                else:
                    for item in value:
                        result = result and _ReturnType._instance_of(item, t)
        elif hasattr(_type, "__origin__") and _type.__origin__ is tuple:
            if not isinstance(value, _type.__origin__):
                return False
            
            for v, t in zip(_type.__args__:
                if t is Ellipsis:
                    continue
        elif _ReturnType._is_optional_type(_type):  # noqa: E721
            """
            if _type.__args__[0].__class__ is TypeVar:
                return False
            """
            result = value is None or _ReturnType._instance_of(value, _type.__args__[0])
        elif hasattr(_type, "__origin__") and _type.__origin__ is Union:
            result = isinstance(value, _type.__args__)
        elif hasattr(_type, "__class__") and _type.__class__ is TypeVar:
            if _type.__constraints__:
                return isinstance(value, _type.__constraints__)
            elif _type.__bound__:
                return isinstance(value, _type.__bound__)
            else:
                return True
        else:
            result = isinstance(value, _type)
        return result

