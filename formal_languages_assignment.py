# Lindsey West
# W
# February 18, 2026

# Task 1: Language Membership Testing
def is_in_language_L(string):
    """
    Check if a string belongs to language L = {a^n b^n | n >= 1}

    Args:
        string (str): Input string to check

    Returns:
        bool: True if string is in L, False otherwise

    Examples:
        is_in_language_L("ab") -> True
        is_in_language_L("aabb") -> True
        is_in_language_L("aaabbb") -> True
        is_in_language_L("aba") -> False
        is_in_language_L("") -> False
    """
    # Your implementation here
    pass

# Task 2: Kleene Closure Generator
def kleene_closure_generator(base_language, max_length):
    """
    Generate all strings in L* (Kleene closure) up to max_length

    Args:
        base_language (list): List of strings representing the base language
        max_length (int): Maximum length of generated strings

    Returns:
        set: Set of all strings in L* with length <= max_length

    Example:
        kleene_closure_generator(["a", "bb"], 4) should include:
        - "" (empty string, always in L*)
        - "a", "bb" (from L¹)
        - "aa", "abb", "bba", "bbbb" (from L²)
        - etc.
    """
    # Your implementation here
    pass

# Task 3: Recursive Language Definition
def generate_recursive_language_M(n):
    """
    Generate the nth string in language M using recursive definition

    Args:
        n (int): Depth of recursion (0 = base case)

    Returns:
        str: The string generated at recursion depth n

    Examples:
        generate_recursive_language_M(0) -> "x"
        generate_recursive_language_M(1) -> "yxz"
        generate_recursive_language_M(2) -> "yyxzz"
        generate_recursive_language_M(3) -> "yyyxzzz"
    """
    # Your implementation here
    pass

# Task 4: Regular Expression Validator
def regex_match(pattern, string):
    """
    Check if string matches the given regular expression pattern
    Support basic operations: concatenation, | (union), * (Kleene star)

    Args:
        pattern (str): Regular expression pattern
        string (str): String to match against pattern

    Returns:
        bool: True if string matches pattern, False otherwise

    Supported patterns:
        - Single characters: 'a' matches "a"
        - Union: 'a|b' matches "a" or "b"
        - Kleene star: 'a*' matches "", "a", "aa", "aaa", etc.
        - Concatenation: 'ab' matches "ab"
        - Combined: 'a*b|c' matches strings of a's followed by b, or just c

    Examples:
        regex_match("a*", "aaa") -> True
        regex_match("a*b", "aab") -> True
        regex_match("a|b", "a") -> True
        regex_match("a|b", "c") -> False
    """
    # Your implementation here
    pass


# Test Cases
def test_assignment():
    # Test Task 1: Language L membership
    assert is_in_language_L("ab") == True
    assert is_in_language_L("aabb") == True
    assert is_in_language_L("aaabbb") == True
    assert is_in_language_L("aabbb") == False
    assert is_in_language_L("aba") == False
    assert is_in_language_L("") == False
    assert is_in_language_L("a") == False
    assert is_in_language_L("b") == False

    # Test Task 2: Kleene closure
    result = kleene_closure_generator(["a"], 3)
    expected = {"", "a", "aa", "aaa"}
    assert result == expected

    result2 = kleene_closure_generator(["ab"], 4)
    assert "" in result2
    assert "ab" in result2
    assert "abab" in result2
    assert len([s for s in result2 if len(s) <= 4]) >= 3

    # Test Task 3: Recursive language
    assert generate_recursive_language_M(0) == "x"
    assert generate_recursive_language_M(1) == "yxz"
    assert generate_recursive_language_M(2) == "yyxzz"
    assert generate_recursive_language_M(3) == "yyyxzzz"

    # Test Task 4: Regular expressions
    assert regex_match("a*", "") == True
    assert regex_match("a*", "aaa") == True
    assert regex_match("a*b", "aaab") == True
    assert regex_match("a|b", "a") == True
    assert regex_match("a|b", "c") == False
    assert regex_match("ab", "ab") == True
    assert regex_match("ab", "a") == False

    print("All tests passed!")


if __name__ == "__main__":
    test_assignment()
