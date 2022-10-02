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
    

# local_variables_length = len(locals().items())
# local_variables_tuples = locals().items()
# local_variables_keys = locals().keys()
# local_variables_values = locals().values()
# print(type(local_variables_keys[0]))



print("\nstart\n")

for key in locals().keys():
    print(key,"\t\t",locals()[key])

print("\nfinish\n")
# for key in locals().keys():
#     print("C")    
#     print(key)



def loop():
    x = 0
    try:
        print(locals().keys()[x])
        x += 1
        loop()
    except:       
        print("finished printing")
        # break

