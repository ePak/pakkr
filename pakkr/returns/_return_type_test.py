from typing import List, Optional, Union, Tuple, TypeVar
from ._return_type import _ReturnType


def test_is_optional_type():
    assert _ReturnType._is_optional_type(Optional[int])
    assert _ReturnType._is_optional_type(Union[int, None])
    assert not _ReturnType._is_optional_type(Union[int, str, float])
    assert not _ReturnType._is_optional_type(List[int])


def test_instance_of_primitive():
    assert _ReturnType._instance_of(1, int)
    assert _ReturnType._instance_of("hello", str)
    assert _ReturnType._instance_of(True, bool)
    assert _ReturnType._instance_of(1.1, float)
    assert not _ReturnType._instance_of("a", int)


def test_instance_of_list():
    assert _ReturnType._instance_of([], list)
    assert _ReturnType._instance_of([], List)
    assert _ReturnType._instance_of(["a"], List)
    assert _ReturnType._instance_of(["a"], List[str])
    assert _ReturnType._instance_of([1, 2], List[int])
    assert not _ReturnType._instance_of(["a"], List[int])
    assert not _ReturnType._instance_of(["a", 1], List[str])


def test_instance_of_tuple():
    assert _ReturnType._instance_of((1,), tuple)
    assert _ReturnType._instance_of((1,), Tuple)
    assert _ReturnType._instance_of((1,), Tuple[int])
    import pdb; pdb.set_trace()
    assert _ReturnType._instance_of((1, "hi"), Tuple[int, str])
    assert not _ReturnType._instance_of((1,), Tuple[str])

def test_instance_of_set():
    ...

def test_instance_of_dict():
    ...


def test_instance_of_Union():
    ...


def test_instance_of_Optional():
    ...


def test_instance_of_class():
    ...
