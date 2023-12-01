def solution():
    input = open("input.txt")
    sum = 0
    for line in input:
        first_num = None
        second_num = None
        for c in line:
            if c.isnumeric():
                if first_num is None:
                    first_num = int(c)
                second_num = int(c)

        if first_num is None:
            first_num = 0
            second_num = 0
        if second_num is None:
            second_num = 0
        sum += first_num * 10 + second_num

    return sum


if __name__ == "__main__":
    print(solution())
