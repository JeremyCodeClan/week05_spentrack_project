from console_test.console_tag import *
from console_test.console_merchant import *
from models.transaction import Transaction

# merchant, tag - pre-created
transaction_11 = Transaction("Unicef Charity", "donate count: 1, amount: 100", 100, "2021-06-20", tag_charity, merchant_unicef)
transaction_10 = Transaction("Citylink Bus", "travel count: 12, switched to daily: 4", 20, "2021-05-30", tag_transport, merchant_bus)
transaction_9 = Transaction("Edinburgh Zoo", "feed tiger: 2, safari ride: 2, dolphin show: 2", 60, "2021-05-15", tag_general, merchant_zoo)
transaction_8 = Transaction("Tesco food", "dark-chocolate: 5, pizzas: 2, chocolate: 3, apple: 2", 30, "2021-05-13", tag_eating, merchant_tesco)
transaction_7 = Transaction("Steam game", "Mordern warfare: 1, Dota 2: 4, Stardew Velly: 1", 40, "2021-05-10", tag_entertainment, merchant_steam)
transaction_6 = Transaction("Asos clothes", "Top: 3, Pants: 2, Socks: 2, Jacket: 1", 100, "2021-05-05", tag_shopping, merchant_asos)
transaction_5 = Transaction("Aldi food", "lemon: 3, pizzas: 2, chocolate: 3, apple: 2", 25, "2021-05-02", tag_groceries, merchant_aldi)
transaction_4 = Transaction("Electricity_monthly", "Usage total amount: 1,000,000kv", 90, "2021-04-21", tag_bills, merchant_electricity)
transaction_3 = Transaction("Udemy discount", "Html, CSS Course: 1, Python3_'you can become pro': 1", 15, "2021-04-17", tag_general, merchant_udemy)
transaction_2 = Transaction("Blizzard games", "Starcraft_II: 1, Overwatch: 1", 40, "2021-04-10", tag_entertainment, merchant_blizzard)
transaction_1 = Transaction("Tesco food", "pizzas: 2, chocolate: 3, apple: 2", 15, "2021-04-02", tag_eating, merchant_tesco)

transaction_unassi_2 = Transaction("Tesco deal", "pizzas: 5, chocolate: 3, apple: 2", 45, "2021-08-15")
transaction_unassi_1 = Transaction("Flight to Seoul", "travel count: 1, distance: something km or miles, I don't know", 550, "2021-08-13")

transactions = [
    transaction_10, transaction_9, transaction_8, transaction_7, transaction_6, transaction_5, transaction_4, transaction_3, transaction_2, transaction_1,
    transaction_unassi_2, transaction_unassi_1
]
