def print_linked_list(head):
    while head:
        print(head.val, end="")
        head = head.next
        if head: print("=>", end="")