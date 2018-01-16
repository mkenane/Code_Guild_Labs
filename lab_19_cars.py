# reqirements:
# name
# account number
# account balance
# phone number

# accouonts = {
#         000001: {
#         'name': 'Chris',
#         'phone': 5032779710,
#         'balance': 10.00
#         }
#     }
# 1.	create a new directory called cars
# 2.	Create the following 2 files inside the cars directory: main.py and car.py
# 3.	In car.py, create a class called Car with the following characteristics:
# o	A shared property called number_of_wheels set to the value 4
# o	The following instance properties that get set upon initialization:
# 	color
# 	number_of_doors
#A honk method that, when called, prints
#
class Car:
    def  __init__(self, owner_manufacturer, owner_color, owner_number_of_doors):

        self.owner_number_of_wheels = 4
        self.color = owner_color
        self.number_of_doors= owner_number_of_doors
        self.owner_manufacturer = owner_manufacturer

    def honk(self):
        return ("honk")

    # def assign_account_number(self):
    #     global NUMBER_OF_ACCOUNTS
    #     NUMBER_OF_ACCOUNTS += 1
    #     # return BankAccount.objects.all().count() + 1
    #     return NUMBER_OF_ACCOUNTS
    #
    # def deposit(self, amount):
    #     self.balance += amount
    #     print("Thanks {}! Your balance is now ${}.".format(self.name, self.balance))
    #
    #
    # def withdraw(self, amount):
    #     if self.balance - amount >= 0:
    #         self.balance -= amount
    #         print("Thanks {}! Your balance is now ${}.".format(self.name, self.balance))
    #     else:
    #         print("I'm sorry {}, you do not have enough money for that.".format(self.name))
    #
    # def __str__(self):
    #     return '{}, Balance: ${}'.format(self.name, self.balance)
    #
    # def __repr__(self):
    #     return self.__str__()
