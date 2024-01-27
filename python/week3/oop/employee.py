class Employee:
    def __int__(self, name, last) -> None:
        self.name = name
        self.last_name = last


class Supervisors(Employee):
    def __int__(self, name, last, password) -> None:
        super().__int__(name, last)
        self.password = password


class Chefs(Employee):
    def request_leave(self, day):
        print("can i request " + str(day) + " sick leave")


# admin = Employee("hasib", "yousufzai", "apple")
sahar = Chefs("sahar", "A")

print(sahar.name)
