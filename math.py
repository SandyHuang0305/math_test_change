math_grades = [10, 30, 50, 70, 90]
print('五次成績:',end='')
for grade in math_grades:
	print(grade,end='')
print(end='\n')	
average = sum(math_grades)/len(math_grades)
print('平均成績:', average)

print('新成績:', end='')
for grade in range (0, len(math_grades)):
	math_grades[grade] = math_grades[grade]**0.5*10
	print(math_grades[grade], end='')
	print(end='\n')
new_average = sum(math_grades)/len(math_grades)
print('新平均成績:',new_average)	
