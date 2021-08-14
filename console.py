import pdb

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repo

merchant_repo.delete_all()

merchant_1 = Merchant("Tesco")
merchant_repo.save(merchant_1)

merchant_2 = Merchant("Asda")
merchant_repo.save(merchant_2)

pdb.set_trace()