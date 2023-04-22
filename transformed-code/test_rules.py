class Person:

    def __init__(self, firstName, lastName):
        c = 3
        self.d = 2
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):
        return self.firstName + self.lastName

    def doit(self):
        b = '2+2'
        literal_eval(b)

    def suspicious_variable_name(self):
        a = 'Name dafault'
        self.firstName = a

    def never_used_variable_op(self):
        aa = 'variable'
        bb = aa + 'con uso en '
        cc = aa + 'sin uso'
        dd = 'return'
        return bb + dd

    def never_used_variable_op(self):
        aa = 'variable en uso en return sin operacion'
        bb = 'no uso'
        return aa

    def somethig(self):
        print('something')

class Person_Data_Class:

    def __init__(self):
        self.name

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

class PersonDataClassWithoutMethodGet:

    def __init__(self):
        self.name

    def getName(self):
        return self.name

class PersonDataClassWithTwoAttribute:

    def __init__(self):
        self.name
        self.age

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getAge(self):
        return self.age

    def setage(self, newName):
        self.age = newName