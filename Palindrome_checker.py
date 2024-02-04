
word = input("enter the word to check palindrome")


def palindrome_checker(word):
    check = list(word)
    reverse = list(reversed(word))
    if check == reverse:
        return "this is a palindrome"
    else:
        return "this is not a palindrome"


print(palindrome_checker(word))