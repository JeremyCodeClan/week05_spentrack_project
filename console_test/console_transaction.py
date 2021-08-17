from console_test.console_tag import *
from console_test.console_merchant import *
from models.transaction import Transaction

# no merchant, tag assigned
transaction_7 = Transaction("Bike Shop", "MTB Bike NC-10: 1, MTB Bike NC-40: 2", 250, "2021-05-20")
transaction_6 = Transaction("Citylink Bus", "travel count: 12, switched to daily: 4", 20, "2021-05-15")

# merchant, tag - pre-created
# tags = [tag_4, tag_3, tag_2, tag_1]
# merchants = [merchant_4, merchant_3, merchant_2, merchant_1]
transaction_5 = Transaction("Aldi food", "lemon: 3, pizzas: 2, chocolate: 3, apple: 2", 25, "2021-05-02", tag_1, merchant_1)
transaction_4 = Transaction("Electricity_monthly", "Usage total amount: 1,000,000kv", 90, "2021-04-21", tag_4, merchant_4)
transaction_3 = Transaction("Udemy discount", "Html, CSS Course: 1, Python3_'you can become pro': 1", 15, "2021-04-17", tag_3, merchant_3)
transaction_2 = Transaction("Blizzard games", "Starcraft_II: 1, Overwatch: 1", 40, "2021-04-10", tag_2, merchant_2)
transaction_1 = Transaction("Tesco food", "pizzas: 2, chocolate: 3, apple: 2", 15, "2021-04-02", tag_4, merchant_1)

transactions = [transaction_7, transaction_6, transaction_5, transaction_4, transaction_3, transaction_2, transaction_1]
