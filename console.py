import pdb

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repo

# merchant_repo.delete_all()

merchant_1 = Merchant("Tesco")
merchant_repo.save(merchant_1)

pdb.set_trace()