# Check Palindrome String
# Verify if a string is a palindrome (ignore case and non-alphanumeric characters).
# Why: simplest way to feel how pointers converge.

# test case 1 :
#Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

def check_pallindrome(string: str) -> bool:
    
    if len(string) <= 1:
        return None
    
    cleaned_array = []
    # first cleaning the string
    for character in string:
        if character.isalpha():
            cleaned_array.append(character.lower())

    # two pointer approach
    print(''.join(cleaned_array))
    left = 0
    right = len(cleaned_array) - 1

    while left <= right:
        if cleaned_array[left] == cleaned_array[right]:
            left += 1
            right -= 1
        
        else:
            return False
    
    return True

# string = "A man, a plan, a canal: Panama"
string = "anna"
print(check_pallindrome(string))