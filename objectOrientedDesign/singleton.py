"""
Ensures that a class has only one instance and ensures access
to the instance through the application
    - Laakmann G., Cracking The Coding Interview (pg. 126)
"""


class SingletonClass(object):
    variable = "Assign variables"

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

    def function(self):
        return "Create Functions"


singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton is new_singleton)

if id(singleton) == id(new_singleton):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, variables contain different instances.")

singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)

print(singleton.variable)
print(singleton.function())
