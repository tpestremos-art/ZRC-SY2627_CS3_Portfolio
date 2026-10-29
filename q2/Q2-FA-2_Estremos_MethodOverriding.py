
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class Senior_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealth_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


regularp = Patient("John Doe", 5000) 
seniorp = Senior_Patient("John Delta Ruz", 5000)
philhealthp = PhilHealth_Patient("Maria Oggay", 5000)

patients = [
    regularp,
    seniorp,
    philhealthp
]

print("Hospital Billing System")
print("-----------------------")

for patient in patients:
    print(f"\nPatient Name: {patient.get_name()}")
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")