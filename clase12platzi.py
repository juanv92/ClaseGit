# Indexing and slicing
# Indexing starts at 0, so the first character is at index 0, the second at index 1, and so on.

# Negative indexing allows you to access characters from the end of the string. 
# The last character is at index -1, the second to last at index -2, and so on.
text = "This is a text for string manipulation in Python."
print(text[0]) # Output: 'T'
print(text[-2]) # Output: 'n'
print(text[-7]) # Output: 'P'

# Slicing allows you to extract a portion of the string using the syntax: string[start:end]
# The start index is inclusive, while the end index is exclusive.
print(text[:7]) # Output: 'This is'
print(text[42:]) # Output: 'Python.'
print(text[-7:-1]) # Output: 'Python'

# Find the index of a substring using the find() method. 
# It returns the index of the first occurrence of the substring, or -1 if not found.
index = text.find("manipulation") # Find the index of the substring "manipulation"
print(index) # Output: 26
index = text.find("Python") # Find the index of the substring "Python"
print(index) # Output: 42
index = text.find("JavaScript") # Find the index of the substring "JavaScript"
print(index) # Output: -1 (not found)

# Replace a substring with another substring using the replace() method.
course = "This is a course of JavaScript Fundamentals."
print(course) # Output: This is a course of JavaScript Fundamentals.
print(course.replace("JavaScript", "Python")) # Output: This is a course of Python Fundamentals.
course = "This is a course of JavaScript Fundamentals. JavaScript is the most popular programming language."
print(course) # Output: This is a course of JavaScript Fundamentals. JavaScript is the most popular programming language.
print(course.replace("JavaScript", "Python")) # Output: This is a course of Python Fundamentals. Python is the most popular programming language.

# The split() method divides a string into a list of substrings based on a specified separator.
text_divided = text.split(" ") # Split the text into a list of words using space as the separator
print(text_divided) # Output: ['This', 'is', 'a', 'text', 'for', 'string', 'manipulation', 'in', 'Python.']

# lower() and upper() methods can be used to convert the string to lowercase or uppercase, respectively.
text = "This text have UPPERCASE and lowercase and I need find some words in it."
print("uppercase" in text) # Output: False
print("uppercase" in text.lower()) # Output: True
print("lowercase" in text) # Output: True
print("lowercase" in text.upper()) # Output: False

word = "uppercase"
print(word.upper() in text) # Output: True
word = "UpperCase"
print(word.upper() in text) # Output: True
word = "UpperCase"
print(word.lower() in text.lower()) # Output: True