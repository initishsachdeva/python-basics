# -------------------Data types in python--------------------

# Numeric = int(long is deprecated, so every long number will fall under int),float, complex = (100 + 3j) will fall under complex.
# String = whatever you put in double or single quotes will fall under string

# Numeric and String discussed in 02_Variable.py file

# -----------List (array in another programming language)
# -- in python you can have multiple data type in list, and it starts with 0th index.

values = [1, 2, "abc", 4.5]
print(values[0])
print(values[1])
print(values[2])
print(values[3])

# To print last index from list
print(values[-1]) # this will print last index from list

# Substring
print(values[1:3]) # 3 is exclusive so it will print till abc string

# you can inject value in bw
values.insert(3, "def")
print(values)

# to add value at last index
values.append(234566)
print(values)

# Tuple


# Dictionary
