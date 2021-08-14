import pdb

from models.merchant import Merchant
from models.tag import Tag
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

merchant_repo.delete_all()
tag_repo.delete_all()

merchant_1 = Merchant("Tesco")
merchant_repo.save(merchant_1)

merchant_2 = Merchant("Asda")
merchant_repo.save(merchant_2)

tag_1 = Tag("Transportation")
tag_repo.save(tag_1)

tag_2 = Merchant("Entertainment")
tag_repo.save(tag_2)

pdb.set_trace()