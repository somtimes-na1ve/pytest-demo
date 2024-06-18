import logging

import pytest


def test_zero_division() -> None:
    with pytest.raises(ZeroDivisionError) as exception_wrapper:
        val = 1 / 0


def test_recursion() -> None:
    with pytest.raises(RuntimeError) as exception_wrapper:
        def foo() -> None:
            foo()

        foo()

    assert "maximum recursion" in str(exception_wrapper.value)


def test_foo_not_implemented() -> None:
    def foo() -> None:
        raise NotImplementedError

    with pytest.raises(RuntimeError) as exception_wrapper:
        foo()

    # you have to check exception type explicitly
    # otherwise, pytest.raises(...) will only check iff a subclass
    assert exception_wrapper.type is RuntimeError


def test_message_match() -> None:
    def foo() -> None:
        raise ValueError("Exception 77 raised")
