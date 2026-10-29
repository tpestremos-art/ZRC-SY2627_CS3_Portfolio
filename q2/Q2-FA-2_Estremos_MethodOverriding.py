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

    def calculate_bill():
        bill = self.__bill_patient * 1
        return bill 

class Senior_Pateint(Patient):
        def calculate_bill(self):
            return get_bill_amount() * 0.8

class PhilHealth_Patient(Patient):
        pass

