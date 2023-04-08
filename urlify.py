def replace_spaces(input_str):
    """It replaces the spaces in the string to %20."""
    output_str = input_str.replace(' ', '%20')      
    return output_str

test_str = "John Smith Websters"
url_string = replace_spaces(test_str)

print(f'The url of {test_str} is {url_string}')
