local_val = "magical unicorns"

def square(x):
    return x*x

class User:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        return "hello"

print(square(5))

user = User("Anna")

print(user.name)
print(user.say_hello())

print("A")

some_dictionary = {"aaa":1,"bbb":2,"ccc":3}

print(some_dictionary.keys())

print("B")
for key in some_dictionary.keys():
    print(key)
    
print("\nstart\n")

for key in locals().keys():
    print(key,"\t\t",locals()[key])

print("\nfinish\n")
# for key in locals().keys():
#     print("C")    
#     print(key)

print("\nC\n")

print(__name__)

if __name__ == "__main__":
    print("the file is being executed directly")

else:
    print(f"the file is being executed because it is being imported by another file.  The file is called; {__name__}")