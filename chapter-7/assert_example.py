#!/usr/bin/env python3

def is_palindrome(word):
    cleaned_word = word.lower()
    return cleaned_word == cleaned_word[::-1]

def run_tests():
    # 1st test case
    assert is_palindrome("madam    ") == True, "Madam should be a palindrome"

    # 2nd test case
    assert is_palindrome("hello") == False, "hello should not be a palindrome"
    
    # 3rd test case
    assert is_palindrome("") == True, "Empty string should be a palindrome"

    print("All tests passed")


run_tests()