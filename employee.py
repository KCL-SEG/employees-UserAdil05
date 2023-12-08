class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class MonthlyEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."


class CommissionEmployee(MonthlyEmployee):
    def __init__(self, name, monthly_salary, commission, contracts):
        super().__init__(name, monthly_salary)
        self.commission = commission
        self.contracts = contracts

    def get_pay(self):
        return super().get_pay() + self.commission * self.contracts

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.contracts} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}."


class BonusCommissionEmployee(MonthlyEmployee):
    def __init__(self, name, monthly_salary, bonus_commission):
        super().__init__(name, monthly_salary)
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return super().get_pay() + self.bonus_commission

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."

billie = MonthlyEmployee("Billie", 4000)
charlie = ContractEmployee("Charlie", 25, 100)
renee = CommissionEmployee("Renee", 3000, 200, 4)
jan = CommissionEmployee("Jan", 25, 220, 3)
robbie = BonusCommissionEmployee("Robbie", 2000, 1500)
ariel = BonusCommissionEmployee("Ariel", 30, 600) 
billie, charlie, renee, jan, robbie, ariel

