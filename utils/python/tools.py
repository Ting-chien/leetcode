from functools import cmp_to_key

def mycmp(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0
    

if __name__ == "__main__":

    a, b = 10, 5

    print(mycmp(a, b))
    print(mycmp(b, a))
    print(mycmp(a, a))

    fruits = ["apple", "banana", "orange", "mango"]
    sorted_fruits = sorted(fruits, key=cmp_to_key(mycmp))

    print(sorted_fruits)