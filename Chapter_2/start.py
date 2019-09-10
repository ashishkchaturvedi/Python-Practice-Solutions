print("Hello");
count = 5
def some_method():
    global count
    count = count + 1
    print(count)
some_method()

#Scope of the Object

def some_function():
    def the_inner_func():
        var = 10
        print("The value of var is: ", var)
    the_inner_func()
    print("you are welcome to some function")
    #print( var);
some_function()