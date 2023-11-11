from database.model import Company
from request import ATIApi
from database import FilterSheet, CompanySheet


# response = ATIApi.search(city_id=3611, balls_limit=5, firm_type_id=2)

CompanySheet.append_company(company=Company(boss_fname='Иван Иванович Иванов', inn='1312312312', name='ООО НАШ'))
