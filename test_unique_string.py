
def check_unique(str1):
    """It checks whether the string argument is unique or not and returns boolean value."""
    str2 = '' + str1
    for i in range(0, len(str1)):
        for j in range(0, len(str2)):
            if ((i != j) and (str1[i] == str2[j])):
                return False
    return True


test_String = "Duolingolanguage application"
Is_Unique = check_unique(test_String)

if Is_Unique is True:
    print(f'\n The string {test_String} is unique \n')
else:
    print(f' \n The string {test_String} is not unique \n')
