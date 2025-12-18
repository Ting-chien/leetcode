### Task 1

# def solution(N):
#     enable_print = N % 10
#     while N > 0:
#         if enable_print == 0 and N % 10 != 0:
#             enable_print = 1
#         elif enable_print == 1:
#             print(N % 10, end="")
#         N = N // 10

def solution(N):
    enable_print = N % 10
    while N > 0:
        if enable_print == 0 and N // 10 % 10 != 0:
            enable_print = 1
        elif enable_print != 0:
            print(N % 10, end="")
        N = N // 10


# public tests
solution(54321) # 12345
print()
solution(10011) # 11001
print()
solution(1) # 1
print()

# private tests
print("Private test")
solution(999)
print()
solution(2000) # 1
print()