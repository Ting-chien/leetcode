def solution(N, S):
    # write your code in Python 3.6
    seats = [[True]*10 for _ in range(N)]
    # Turn occupied seat to N*10 matrix
    if S:
        for occupied in S.split(" "):
            row = int(occupied[:-1]) - 1
            col = ord(occupied[-1:]) - 65 if occupied[1] < 'I' else ord(occupied[1]) - 66
            seats[row][col] = False

    # Check if the seats are available for four-family
    availables = 0
    for row in range(N):
        if all(x for x in seats[row][1:5]) and all(x for x in seats[row][5:9]):
            availables += 2
        elif all(x for x in seats[row][1:5]) or all(x for x in seats[row][5:9]):
            availables += 1
        elif all(x for x in seats[row][3:7]):
            availables += 1

    return availables

if __name__ == '__main__':
    print(solution(1, ""))