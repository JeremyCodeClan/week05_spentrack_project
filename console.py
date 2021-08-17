import pdb

import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo
import repositories.transaction_repository as transaction_repo
from console_test.console_tag import *
from console_test.console_merchant import *
from console_test.console_transaction import *

merchant_repo.delete_all()
tag_repo.delete_all()
transaction_repo.delete_all()

for tag in tags:
    tag_repo.save(tag)

for merchant in merchants:
    merchant_repo.save(merchant)

for transaction in transactions:
    transaction_repo.save(transaction)

pdb.set_trace()