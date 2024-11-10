from main import handler


class MockContext:
    pass


def test():
    ctx = MockContext()

    handler(ctx)


if __name__ == "__test__":
    test()
