# квадратичные сортировки - время затраченное на обработку O(N^2)
# К квадратичным относятся: сортировка вставкой (insert sort), выбора (chose sort), пузырьковая (babble sort)


class ListNode:
    """Node for single linked list"""
    def __init__(self, value=0, next_node=None, head=False):
        self.value = value
        self.next = next_node
        self.head = self if head else head

    def __str__(self):
        return f'Class {self.__class__.__name__} contain {vars(self)}.'


if __name__ == '__main__':
    arr = ListNode(555, ListNode(10), head=True)
    print(arr)

