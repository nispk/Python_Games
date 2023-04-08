def permutation(str2, start, end):
    if (start == end):
        print(str2)
    else:
        for i in range(start, end+1):
            str2[start], str2[i] = str2[i], str2[start]
            permutation(str2, start+1, end)
            str2[start], str2[i] = str2[i], str2[start]


test_string = "tacocat"


permutation(list(test_string), 0, len(test_string)-1)