import sys

def solution(file):
    input = open(file)
    sum = 0
    for line in input:
        first_num = None
        second_num = None
        # Step 1) Find arabic digits
        for i,c in enumerate(line):
            if c.isnumeric():
                if first_num is None:
                    first_num = (i, int(c))
                second_num = (i, int(c))

        possible_digits = (
            ('one', 1), ('two', 2), ('three', 3),
            ('four', 4), ('five', 5), ('six', 6),
            ('seven', 7), ('eight', 8), ('nine', 9)
        )

        # Step 2) Find digits-as-words
        for i in range(len(line)):
            for word,digit in possible_digits:
                if line[i:i + len(word)] == word:
                    if first_num is None or first_num[0] > i:
                        first_num = (i, digit)
                    if second_num is None or second_num[0] < i:
                        second_num = (i, digit)

        if first_num is None:
            first_num = (-1, 0)
        if second_num is None:
            second_num = (-1, 0)
        sum += first_num[1] * 10 + second_num[1]

    return sum


if __name__ == "__main__":
    print(solution(sys.argv[1]))
