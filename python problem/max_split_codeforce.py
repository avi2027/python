def split_balanced_string(S):
    balanced_strings = []
    start = 0
    count_L = 0
    count_R = 0

    for i, char in enumerate(S):
        if char == 'L':
            count_L += 1
        else:
            count_R += 1

        if count_L == count_R:
            balanced_strings.append(S[start:i + 1])
            start = i + 1
            count_L = 0
            count_R = 0

    return balanced_strings


if __name__ == "__main__":
    S = input().strip()
    result = split_balanced_string(S)
    print(len(result))
    for segment in result:
        print(segment)
