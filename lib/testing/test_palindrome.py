import pytest
from palindrome import longest_palindromic_substring

@pytest.mark.parametrize("s, expected_options", [
    # basic examples from prompt
    ("babad", ["bab", "aba"]),
    ("cbbd", ["bb"]),
    ("a", ["a"]),
    ("ac", ["a", "c"]),
    ("racecar", ["racecar"]),

    # empty string should return empty
    ("", [""]),

    # no multi-char palindrome >1, so any single character is ok
    ("abcde", list("abcde")),
 
    # digit palindrome
    ("12321", ["12321"]),
    
    # all same letters
    ("aaaaa", ["aaaaa"]),

    # palindromes in the middle or end
    ("abacdfgdcaba", ["aba"]),           # two “aba” at ends
    ("abacdfgdcabba", ["abba"]),         # even-length
    ("forgeeksskeegfor", ["geeksskeeg"]),
])
def test_various_cases(s, expected_options):
    result = longest_palindromic_substring(s)
    assert result in expected_options

def test_long_string_performance():
    # very long string of length 1000
    s = "a" * 1000
    # should immediately return the whole string
    assert longest_palindromic_substring(s) == s