import pytest


def foo() -> None:
    raise ExceptionGroup(
        "Error Message",
        [
            RuntimeError()
        ])


def test_exception_group() -> None:
    with pytest.raises(ExceptionGroup) as exception_group_wrapper:
        foo()

    assert exception_group_wrapper.group_contains(RuntimeError)
    assert not exception_group_wrapper.group_contains(KeyError)
