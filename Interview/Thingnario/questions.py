# Problem 1 - Bubble sort
def bubble_sort(sequence):
    # Write your bubble sort code here.
    n = len(sequence)
    for i in range(n):
        for j in range(1, n-i):
            # Compare two elements, switch if seq[j-1] > seq[j]
            if sequence[j-1] > sequence[j]:
                sequence[j], sequence[j-1] = sequence[j-1], sequence[j]
    return sequence

assert bubble_sort([5, 1, 3, 2, 4]) == [1, 2, 3, 4, 5]


# Problem 2 - Find second largest
def find_second_largest(sequence):
    # Write your algorithm with O(n) time complexity here.

    if len(sequence) < 2:
        return
    
    first_largest, second_largest = None, None
    for num in sequence:
        if first_largest is None or num > first_largest:
            first_largest, second_largest = num, first_largest
        elif num < first_largest and (second_largest is None or num > second_largest):
            second_largest = num

    return second_largest

assert find_second_largest([3, 3, 2, 1]) == 2
assert find_second_largest([3, 3, 3, 3, 3, 2, 2, 1]) == 2
assert find_second_largest([-1, 2, 3, 5, 3, 1, 2, 4]) == 4


# Problem 3 - Inheritance
# Write some examples with inheritance code here.


# Case 1. A parent class Animal with say_hi() function
# and a child class Dog inheriate from Animal

class Animal:

    def __init__(self, name: str):
        self.name = name

    def say_hi(self):
        print(f"Hi! My name is {self.name}!")

class Dog(Animal):

    def __init__(self, name: str):
        super().__init__(name)

dog = Dog(name="Fakerrr")
dog.say_hi() # Hi! My name is Fakerrr!


# Problem 4 - *args, **kwargs
# Write some examples with *args, **kwargs here.


# Case 1. Use *args as input parameters to sum all input data
def total(*args) -> int:
    return sum(args)

print(total(1, 2, 3)) # 6

# Case 2. Use *args and **kwargs as input parameters to 
# handle all kind of input in decorator
def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            return "I don't think its an error 🤔"
    return wrapper

@error_handler
def divide(a: int, b: int):
    return a / b

print(divide(10, 5)) # 2
print(divide(10, 0)) # I don't think its an error 🤔


# Problem 5 - lambda
# Write some examples using python lambda here.


# Case 1. Use lambda as a key to sort by age
colleagues = [
    {
        "name": "Eric", 
        "age": 20
    },
    {
        "name": "Jessie", 
        "age": 40
    },
    {
        "name": "Alex", 
        "age": 30
    },
]

# Sort colleagues by age
# [{'name': 'Eric', 'age': 20}, {'name': 'Alex', 'age': 30}, {'name': 'Jessie', 'age': 40}]
colleagues.sort(key=lambda x: x.get("age", 0)) 


# Problem 6 - comprehension
# Write some examples using python comprehension here.

# Case 1. Turn colleauges' name to uppercase 

colleagues = ["eric", "jessie", "alex"]
colleagues = [c.upper() for c in colleagues]
print(colleagues) # ['ERIC', 'JESSIE', 'ALEX']



# Problem 7 - decorator
# Write some examples using python decorator here.


# Case 1. A decorator to count time spend in function
from datetime import datetime

def timer(func):
    def wrapper(*args, **kwargs):
        started_at = datetime.now()
        res = func(*args, **kwargs)
        ended_at = datetime.now()
        print(f"func: {func.__name__} cost {ended_at-started_at}")
        return res 
    return wrapper

@timer
def add(a: int, b: int):
    return a + b

print(add(1, 2)) 
# func: add cost 0:00:00.000007
# 3



# Problem 8 - generator
# Write some examples using python generator here.

# Case 1. Replce list comprehension to generator to get name's uppercase

colleagues = ["eric", "jessie", "alex"]
def get_upper_name(names):
    for name in names:
        yield name.upper()

upper_name_getter_1 = get_upper_name(colleagues)
print(next(upper_name_getter_1)) # ERIC
print(next(upper_name_getter_1)) # JESSIE
print(next(upper_name_getter_1)) # ALEX

# Case 2. Get all at once
upper_name_getter_2 = get_upper_name(colleagues)
print(list(upper_name_getter_2)) # ['ERIC', 'JESSIE', 'ALEX']


# Explain the benefit of generators here.
#
# Generator is a efficiency way to handle large amount of data since
# we don't need to calculate all data at once. We can use this advantage
# to load large amount of file or data stream.


# Problem 9 - context manager
# Write some examples using python context manager here.

# Case 1. Read files
with open("example.txt", "r") as f:
    for line in f:
        print(line)

# Case 2. db session (Python SQLAlchemy)

engine = create_engine("sqlite:///example.db")
Session = sessionmaker(bind=engine)

with Session() as session:
    try:
        # Do something here in this session...
        session.commit()
    except:
        session.rollback()



# Problem 10 - magic methods
# Write some examples using python magic methods here.


# Case 1. Use __repr__ to show class information
class Dog:

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Dog({self.name})"

dog = Dog(name="Husky")
print(dog) # Dog(Husky)


# Case 2. Use __enter__ and __exit__ to rewrite db_session manager

engine = create_engine("sqlite:///example.db")
Session = sessionmaker(bind=engine)

class DBSessionManager:

    def __init__(self, session_factory: Session):
        self.session_factory = session_factory
        self.session = None

    def __enter__(self):
        self.session = session_factory()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            # Something went wrong
            self.session.rollback()
            print(f"DB error: [{exc_val}] {exc_tb}")
        else:
            self.session.commit()
        self.session.close()
        return False

with DBSessionManager as session:
    # Do something here in this session...

# Session auto commit after leave the context
# or exception thrown and caught out of context