def receive_input():
    number = input().split(',')
    boards = []
    for _ in range(100):
        blank = input()
        line1 = preprocess_line(input())
        line2 = preprocess_line(input())
        line3 = preprocess_line(input())
        line4 = preprocess_line(input())
        line5 = preprocess_line(input())
        board = [line1, line2, line3, line4, line5]
        boards.append(board)
    return number,boards

def preprocess_line(line):
    return list(filter(lambda x: x != '', line.split(' ')))

def check_board(number,board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == number:
                return [i,j]
    return []

def check_winner(board):
    # Check bingo in board 5x5 which X represent mark
    for i in range(len(board)):
        if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X' and board[i][3] == 'X' and board[i][4] == 'X':
            return True
        if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X' and board[3][i] == 'X' and board[4][i] == 'X':
            return True
    return False

def get_sum_of_remain(board):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 'X':
                sum += int(board[i][j])
    return sum

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()

def main():
    number,boards = receive_input()
    for n in number:
        for board in range(len(boards)):
            result = check_board(n,boards[board])
            if result != []:
                boards[board][result[0]][result[1]] = 'X'
                if check_winner(boards[board]):
                    print(int(n) * int(get_sum_of_remain(boards[board])))
                    return
        

if __name__ == '__main__':
    main()