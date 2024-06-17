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
