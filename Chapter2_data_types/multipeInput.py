x, y = input("Enter two values: ").split()
print("Number of girls: ", x)
print("Number of boys: ", y)


#Taking two inputs at a time

x, y = input("Enter two numbers: ").split()
print("First number is {} and second number is {}".format(x, y))
print()

#Taking multiple inputs at time and type casting using list() function

x = list(map(int, input("Enter multiple numbers").split()))
print("List of students: ",x)