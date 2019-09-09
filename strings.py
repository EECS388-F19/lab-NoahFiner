students = ["Batuhan", "Alex", "Yeon"]
students.sort()
print(students)
first_name = students[0]
print(first_name[:-1])
longest_name = first_name
for name in students:
    if len(longest_name) < len(name):
        longest_name = name

print(longest_name)