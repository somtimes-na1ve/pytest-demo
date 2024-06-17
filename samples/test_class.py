class TestClass:

    def test_one(self) -> None:
        x = "this"
        assert "h" in x

    def test_two(self) -> None:
        x = "hello"
        assert hasattr(x, "check")
