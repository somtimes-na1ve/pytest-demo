import pytest


def foo() -> None:
    raise SystemExit(-1)


def test_sysexit() -> None:
    with pytest.raises(SystemExit):
        foo()
