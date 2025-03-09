def is_palindrome(line: str) -> bool:
    line_sanitized = "".join([char.lower() for char in line if char.isalnum()])
    return line_sanitized == line_sanitized[::-1]


print(is_palindrome(input().strip()))
