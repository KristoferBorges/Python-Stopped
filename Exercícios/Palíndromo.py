def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True


word = 'civic'
if is_palindrome(word):
    print(f"{word} é um palíndromo.")
else:
    print(f"{word} não é um palíndromo.")
