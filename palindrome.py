def is_palindrome(word):
    word = word.lower()
    length = len(word)
    for i in range(0, int(length / 2)):
        if word[i] != word[length - i - 1]:
            return False
    return True

if is_palindrome('Ala'):
    print("It's a palindrome")
else:
    print("It's not a palindrome :<")
