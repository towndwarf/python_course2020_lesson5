class SampleClass:

    def __init__(self, a):
        # private variable or property in Python
        self.__a = a

    # getter method to get the properties using an object
    def get_a(self):
        return self.__a

    # setter method to change the value 'a' using an object
    def set_a(self, a):
        self.__a = a


# creating an object
obj = SampleClass(10)
# getting the value of 'a' using get_a() method
print(obj.get_a())
# setting a new value to the 'a' using set_a() method
obj.set_a(45)
print(obj.get_a())


# =================================================


class PythonSimpleWay:
    def __init__(self, a):
        self.a = a


# Create an object for the 'PythonSimpleWay' class
obj = PythonSimpleWay(100)

print(obj.a)


# =================================================


class SampleClass1:
    def __init__(self, a):
        # calling the set_a() method to set the value 'a' by checking certain conditions
        self.set_a(a)

    # getter method to get the properties using an object
    def get_a(self):
        return self.__a

    # setter method to change the value 'a' using an object
    def set_a(self, a):

        # condition to check whether 'a' is suitable or not
        if a > 0 and a % 2 == 0:
            self.__a = a
        else:
            self.__a = 2


# create an object for the class 'SampleClass1'
obj = SampleClass1(16)
print(obj.get_a())


# =================================================


class Property:

    def __init__(self, var):
        # initializing the attribute
        self.a = var

    @property
    def a(self):
        return self.__a

    # the attribute name and the method name must be same
    # which is used to set the value for the attribute
    @a.setter
    def a(self, var):
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2


# creating an object for the class 'Property'
obj = Property(23)
print(obj.a)


# =================================================


class FinalClass:

    def __init__(self, var):
        # calling the set_a() method to set the value 'a' by checking certain conditions
        self.__set_a(var)

    # getter method to get the properties using an object
    def __get_a(self):
        return self.__a

    # setter method to change the value 'a' using an object
    def __set_a(self, var):
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2

    a = property(__get_a, __set_a)


# creating an object for the 'FinalClass' class
obj = FinalClass(12)
