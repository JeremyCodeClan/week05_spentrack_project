import pdb

from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo
import repositories.transaction_repository as transaction_repo

merchant_repo.delete_all()
tag_repo.delete_all()
transaction_repo.delete_all()





# transaction_6 = Transaction("Blizzard games", "Starcraft_II: 1, Overwatch: 1", 40, "2021-05-05", tag_2, merchant_2)
# transaction_repo.save(transaction_6)
# transaction_5 = Transaction("Blizzard games", "Starcraft_II: 1, Overwatch: 1", 40, "2021-05-05", tag_2, merchant_2)
# transaction_repo.save(transaction_5)

# merchant, tag - pre-created

tag_4 = Tag("Utility")
tag_repo.save(tag_4)
merchant_4 = Merchant("Electricity")
merchant_repo.save(merchant_4)
transaction_4 = Transaction("Electricity_monthly", "Usage total amount: 1,000,000kv", 90, "2021-04-21", tag_4, merchant_4)
transaction_repo.save(transaction_4)

tag_3 = Tag("Education")
tag_repo.save(tag_3)
merchant_3 = Merchant("Udemy")
merchant_repo.save(merchant_3)
transaction_3 = Transaction("Udemy discount", "Html, CSS Course: 1, Python3_'you can become pro': 1", 15, "2021-04-17", tag_3, merchant_3)
transaction_repo.save(transaction_3)

tag_2 = Tag("Entertainment")
tag_repo.save(tag_2)
merchant_2 = Merchant("Blizzard")
merchant_repo.save(merchant_2)
transaction_2 = Transaction("Blizzard games", "Starcraft_II: 1, Overwatch: 1", 40, "2021-04-10", tag_2, merchant_2)
transaction_repo.save(transaction_2)

tag_1 = Merchant("Food")
tag_repo.save(tag_1)
merchant_1 = Merchant("Tesco")
merchant_repo.save(merchant_1)
transaction_1 = Transaction("Tesco food", "pizzas: 2, chocolate: 3, apple: 2", 15, "2021-04-02", tag_1, merchant_1)
transaction_repo.save(transaction_1)


pdb.set_trace()