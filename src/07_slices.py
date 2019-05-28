"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
i = slice(1, 2)
print(a[i])

# Output the second-to-last element: 9
i = slice(4, 5)
print(a[i])

# Output the last three elements in the array: [7, 9, 6]
i = slice(3, 6)
print(a[i])

# Output the two middle elements in the array: [1, 7]
i = slice(2, 4)
print(a[i])

# Output every element except the first one: [4, 1, 7, 9, 6]
i = slice(2, 6)
print(a[i])

# Output every element except the last one: [2, 4, 1, 7, 9]
i = slice(0, (len(a) - 1))
print(a[i])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
i = slice(7, 12)
print(s[i])
