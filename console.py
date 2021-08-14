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

merchant_1 = Merchant("Tesco")
merchant_repo.save(merchant_1)

merchant_2 = Merchant("Asda")
merchant_repo.save(merchant_2)

tag_1 = Tag("Transportation")
tag_repo.save(tag_1)

tag_2 = Merchant("Food")
tag_repo.save(tag_2)

transaction_1 = Transaction("Tesco food", "I got food from Tesco", 20, merchant_1, tag_2)
transaction_repo.save(transaction_1)

transaction_2 = Transaction("some transaction", "spent on something I don't know", 40)
transaction_repo.save(transaction_2)

pdb.set_trace()