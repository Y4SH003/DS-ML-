import numpy as np 
marks = np.array([
    [85,78,92],
    [88,76,81],
    [90,91,89],
    [70,75,80]
])

print("Marks:\n", marks)

total_marks = np.sum(marks,axis=1)
print("\nTotal marks per student: ", total_marks)

average_marks = np.mean(marks,axis=0)
print("\nAverage marks per student:", average_marks)

top_student_index = np.argmax(total_marks)
print("\nTop performing student: student:", top_student_index + 1)

print("Highest total marks", total_marks[top_student_index])
