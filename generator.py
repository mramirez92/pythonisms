def line_by_line(item):
    while len(item) > 0:
        yield item[0]
        item.pop(0)


brit = [
    "My loneliness is killing me (And I)",
    "I must confess, I still believe (Still believe)",
    "When I'm not with you, I lose my mind",
    "Give me a sign",
    "Hit me, baby, one more time"
]
line_by_line(brit)
for lines in line_by_line(brit):
    print(lines)


def multiply(a, b):
    i = 1
    while i <= a:
        yield i * b
        i += 1


def test_line_by_line():
    input_list = ['cat', 'dog', 'fish']
    expected_output = ['cat', 'dog', 'fish']
    result = list(line_by_line(input_list))
    assert result == expected_output
    print("line_by_line function passed")


def test_multiply():
    result = list(multiply(5, 3))
    expected = [3, 6, 9, 12, 15]
    assert result == expected
    print("multiply function pass")


if __name__ == "__main__":
    test_multiply()
    test_line_by_line()
