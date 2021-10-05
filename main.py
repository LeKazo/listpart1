last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# Your code below: 
subjects = ["Stats", "english", "Science", "lab"]
grades = [98, 97, 85, 88]
gradebook = [["English", 98], ["Lab", 97], ["science", 85], ["stats", 88]]
# print(gradebook)

gradebook.append(["Computer Science", 100])
gradebook.append(["Stats", 93])
# print(gradebook)

gradebook[-1][-1] = 98
# print(gradebook)

gradebook.remove(["English", 85])
# print(gradebook)

gradebook.append(["English", "Pass"])
# print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
