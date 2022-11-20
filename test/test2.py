from dsa04_LinkedList.linkedlist_singly import LikedList


def removeDuplicates(llist):
    res = cur = llist
    cur = cur.next
    while cur:
        print(cur._element, res._element)
        if cur._element != res._element:
            res._next = cur
            res = res._next
        cur = cur._next

    return llist


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = LikedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.add_last(llist_item)

        llist1 = removeDuplicates(llist._head)
        llist.display()

