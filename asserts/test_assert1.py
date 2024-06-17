def foo() -> int:
    return 77


def test_foo() -> None:
    actual = foo()
    assert actual == 47, f"Expected 47, but got {actual}"
