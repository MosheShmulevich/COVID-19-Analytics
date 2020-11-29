

class Test:
    def __init__(self, name, age, id_num, city, num_test):
        print("dear worker,please enter all of the following so if the test will be positive the system will "
              "add the patient to the database automatically")
        print("enter patients name:")
        self.name = input(name)
        print("enter patients age:")
        self.age = input(age)
        print("enter patients id:")
        self.id = input(id_num)
        print("enter patients city:")
        self.city = input(city)
        print("enter the number of the test for the patient:")
        self.test = input(num_test)
