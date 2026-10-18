camelCase = input("camelCase: ")
snake_case = ""
for char in camelCase:
    if char == char.capitalize():
        snake_case += "_" + char.lower()
    else:
        snake_case += char
if snake_case[0] == "_":
    snake_case = snake_case[1:]
print("snake_case:", snake_case)
