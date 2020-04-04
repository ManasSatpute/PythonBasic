class Test:
    __name = None  # Private Access Modifiers
    _roll = None   # Protected Access Modifiers
    branch = None  # public Access Modifiers

    def __init__(self, name, roll, branch):
        self.__name = name
        self._roll = roll
        self.branch = branch

    def __displayDetails(self):
        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self._roll)
        print("Branch: ", self.branch)

    def accessPrivateFunction(self):
        # accesing private member function
        self.__displayDetails()


t = Test("R2J", 1706256, "Information Technology")
t.accessPrivateFunction()