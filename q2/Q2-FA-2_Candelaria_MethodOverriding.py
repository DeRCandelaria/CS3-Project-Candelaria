# Parent Class
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

#Get
    def get_name(self):
        return self.__name
    def get_bill_amount(self):
        return self.__bill_amount
#Set
    def set_name(self, name):
        self.__name = name
    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount
#Display
    def display_info(self):
        print("Name:", self.__name)
        print("Original Bill:", self.__bill_amount)


# Subclass 1:
class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        self.__disc_bill = bill_amount * 0.8

#Get
    def get_disc_bill(self):
        return self.__disc_bill
#Set
    def set_disc_bill(self, disc_bill):
        self.__disc_bill = disc_bill
#Display
    def display_info(self):
        super().display_info()
        print("Final Bill:", self.__disc_bill)

# Subclass 2:
class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        self.__disc_bill = bill_amount * 0.85

#Get
    def get_disc_bill(self):
        return self.__disc_bill
#Set
    def set_disc_bill(self, disc_bill):
        self.__disc_bill = disc_bill
#Display
    def display_info(self):
        super().display_info()
        print("Final Bill:", self.__disc_bill)

#Examples

print("Health Billing System")
print("---------------------")

Patient1 = Patient("Juan Dela Cruz", 15000)
Patient1.display_info()

print("space" * 0)

SeniorPatient1 = SeniorPatient("Maria Santos", 15000)
SeniorPatient1.display_info()

print("space" * 0)

PhilHealthPatient1 = PhilHealthPatient("Pedro Reyes", 15000)
PhilHealthPatient1.display_info()
