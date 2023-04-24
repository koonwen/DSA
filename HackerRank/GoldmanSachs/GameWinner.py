WENDY = "wendy"
BOB = "bob"


def gameWinner(colors):
    colors = [char for char in colors]
    w_ptr = 1
    b_ptr = 1
    while True:
        prev_len = len(colors)
        while w_ptr < len(colors) - 1:
            if colors[w_ptr] == colors[w_ptr + 1] == colors[w_ptr - 1] == 'w':
                colors[w_ptr] = '0'
                print("Wendy popped", w_ptr)
                break
            else:
                w_ptr += 1

        if w_ptr == len(colors)-1:
            return BOB

        while b_ptr < len(colors) - 1:
            if colors[b_ptr] == colors[b_ptr + 1] == colors[b_ptr - 1] == 'b':
                colors[b_ptr] = '0'
                print("Bob popped", b_ptr)
                break
            else:
                b_ptr += 1

        if b_ptr == len(colors)-1:
            return WENDY


if __name__ == '__main__':
    colors = "bbwwwwwbbbwbwbwwbbbbbwwbwwbbwbwwbwwbwwbbwwbwbwbbwbbwwbwbbwbbwwbwwbwbwbbwwwbwwbbwbbbbbwwwwwbwbwbwwbwbbbwbbbbwbwbwwbbwbwbbbwbwwwwwwbbwbwbwwwbwbwwwbbwwbwbbwwwbbbbwwbbbwbbbbwwwwwbbwwbbwwwwwwbwbbwwwbbbwbbwwwwwwbbwwbbwwwbbbbwwbbbbbbwwbbbbbwbwbwbwwbbbwbwbbwbbbbwwwwwbbwbwbbbbbwwbwwbwwwwbwwbbbbbbwbbbwwwwbwbbwbbbwwwwbwwwbbwwwbwwwbwbwbbbwbwwwbwwbwwwwbwbwwbwwwwwbwbwbwwbwbbbwbbwbwbwwbbbwwwbbbbwwwwwbbbbwwwwwbbbbwwwwbbwbbwbbwwwbwbbwbbwwbbbbbwbbwbwbwbwwwbwwwwwbwbwwbwbwbwbbwbbbbbbbwwbbwbbwwbwbbbbwbwwbbbwbwwbwbbwwwwwbwbwwbwbwwbbwwbbbwbwwwbbwwwwwbbbbbbbbwwbwwwwbbbbwwbbbbbbwwwbbbbbwbwbbbwwwwbbwwwbwwwwwwwbwbbbbwwwbwwwwbwbwwwbwwbwwwbwwbbbwbwbwwwbbbbwwwbbbwwbwbwwbwwbbbwbwbwwwbbwwbbwwbwbwbwwbwwwbwbwbwbbbwwbwbwbbwbwwwwbbbwbbbwwwwbwbbwbbwwwbwwwbbbbwbwbwwwwbbbwbwwbwbbwwwbbbwwbbbbwbwwbwbwwwwwbbwwbwwbwwbbbbwwbwwwbwwwwwwbbbbwbbbwbbwbwbwbbwbbbwwwbbbbbwbwwwwbbbwbwwbbwbwwbwwbwbbbwwbwwwbbbwbbwwwbbbbbwwbwwwbbwbbwbwwwbbwbwwwbwwbwwwwbbwwbbwwwwwbwwbbwwbwbwbbbwwbbwbbwwbbbwwbwbwbwbbwwwwwbbbwwwbbwbbwwwbwwwbwwbwwbbbbbwbbwwwwbb"
    print(gameWinner(colors))