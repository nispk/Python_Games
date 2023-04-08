def check_for_permutation(str1, str2):
    """"It checks if str2 is a permutation of str1."""
    for i in range(0,len(str2)):
        if str2[i] not in str1:
            return False
        else:
            continue
    return True

test_string1 = "aeio"
test_string2 = "aaiooaaee"

result = check_for_permutation(test_string1, test_string2)

print(f'The string {test_string2} is a permutation of string {test_string1} is {result}')
