# Create variables and do simple arithmetic operations with them
x = 8
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)

# Create 5 variables with people's names
student_1_name = "Alexander"
student_2_name = "Maria"
student_3_name = "Victor"
student_4_name = "Antonia"
student_5_name = "Ivan"

# Define the students' names and PINs as tuples
student_1 = ("Alexander", "8009118461")
student_2 = ("Maria", "9203108530")
student_3 = ("Victor", "9008257432")
student_4 = ("Antonia", "9405107561")
student_5 = ("Ivan", "8408268577")

# Define a list of student tuples
students_list = [student_1, student_2, student_3, student_4, student_5]

# Initialize an empty dictionary
students_names_dict = {}

# Iterate through the tuples and add them to the dictionary if the name starts with a vowel
for name, pin in students_list:
    if name[0].lower() in ["a", "e", "i", "o", "u"]:
        students_names_dict[name] = pin

# Print the resulting dictionary
print(students_names_dict)

#Fill in the following truth table. Use Python to verify the results.
#| x | y | x and y | x or y | not x | not y |
#|-------|-------|-----------|----------|---------|---------|
#| True | True | | | | |
#| True | False | | | | |
#| False | True | | | | |
#| False | False | | | | |

# Define the values of x and y in lists
x_values = [True, True, False, False]
y_values = [True, False, True, False]

# Create lists to store the results
and_results = []
or_results = []
not_x_results = []
not_y_results = []

# Fill in the truth table and compute the results
for x, y in zip(x_values, y_values):
    and_result = x and y
    or_result = x or y
    not_x_result = not x
    not_y_result = not y

    and_results.append(and_result)
    or_results.append(or_result)
    not_x_results.append(not_x_result)
    not_y_results.append(not_y_result)

# Print the truth table and results
print("| x    | y    | x and y | x or y | not x | not y |")
print("|------|------|---------|--------|-------|-------|")
for x, y, and_result, or_result, not_x_result, not_y_result in zip(x_values, y_values, and_results, or_results,
                                                                   not_x_results, not_y_results):
    print(f"| {x} | {y} | {and_result}       | {or_result}      | {not_x_result}     | {not_y_result}     |")
