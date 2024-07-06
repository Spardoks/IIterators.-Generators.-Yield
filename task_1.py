class FlatIterator:

    def __init__(self, list_of_list):
        self.elements = []
        for lst in list_of_list:
            self.elements.extend(lst)
        self.currnet = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.currnet >= len(self.elements):
            raise StopIteration
        item = self.elements[self.currnet]
        self.currnet += 1
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
