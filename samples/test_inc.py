
def inc(x: int) -> int:
    return x + 1


def test_inc() -> None:
    assert inc(1) == 2


def test_inc_failed_case() -> None:
    assert inc(1) == 3
