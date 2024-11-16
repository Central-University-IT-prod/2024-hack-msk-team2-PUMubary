import unittest

from data.orm import SyncORM


#команада для запуска тестов 
#ИЗ ДИРЕКТОРИИ backend ВАЖНО!!!
#python -m unittest discover -s data -p "test_*.py"
class TestORM(unittest.TestCase):
    def test_get_user_debtors(self):
        #http://127.0.0.1:5000/get_user_debtors?lender_tg=@petr

        #Должники Петра
        self.assertEqual(SyncORM.get_user_debtors('@petr')[0]['debtor_tg'], '@ivan')
        self.assertEqual(SyncORM.get_user_debtors('@petr')[0]['amount'], 50)

        self.assertEqual(SyncORM.get_user_debtors('@petr')[1]['debtor_tg'], '@sveta')
        self.assertEqual(SyncORM.get_user_debtors('@petr')[1]['amount'], 150)

        #а ивану никто ничего не должен
        #http://127.0.0.1:5000/get_user_debtors?lender_tg=@ivan
        self.assertEqual(SyncORM.get_user_debtors('@ivan'), [])

    
    def test_get_user_lenders(self):
        #petr никому ничего не должен
        #http://127.0.0.1:5000/get_user_lenders?debtor_tg=@petr
        self.assertEqual(SyncORM.get_user_lenders('@petr'), [])

        #http://127.0.0.1:5000/get_user_lenders?debtor_tg=@ivan
        #Кому должен ivan
        self.assertEqual(SyncORM.get_user_lenders('@ivan')[0]['lenders_tg'], '@oleg')
        self.assertEqual(SyncORM.get_user_lenders('@ivan')[0]['amount'], 25)

        self.assertEqual(SyncORM.get_user_lenders('@ivan')[1]['lenders_tg'], '@petr')
        self.assertEqual(SyncORM.get_user_lenders('@ivan')[1]['amount'], 50)

    def test_get_trips(self):
        #http://127.0.0.1:5000/get_trips?tg_tag=@petr
        #Петр в трех трипах
        self.assertEqual(len(SyncORM.get_trips('@petr')), 3)

    def test_get_trip_debts(self):
        #http://127.0.0.1:5000/get_trip_debts?trip_id=1
        #в первом трипе 4 записи
        self.assertEqual(len(SyncORM.get_trip_debts(1)), 4)

    def test_get_trip_user_debtors(self):
        #http://127.0.0.1:5000/get_trip_user_debtors?lender_tg=@petr&trip_id=1
        #Должник Петра в первом трипе всего 1
        self.assertEqual(list(SyncORM.get_trip_user_debtors('@petr', 1)[0][0].keys())[0], '@ivan')
        self.assertEqual(list(SyncORM.get_trip_user_debtors('@petr', 1)[0][0].values())[0], 200)

        #Петр должен двум людям, проверим первого
        self.assertEqual(list(SyncORM.get_trip_user_debtors('@petr', 1)[1][0].keys())[0], '@alex')
        self.assertEqual(list(SyncORM.get_trip_user_debtors('@petr', 1)[1][0].values())[0], 75)
        self.assertEqual(len(SyncORM.get_trip_user_debtors('@petr', 1)[1]), 2)

    # def test_get_tg_id(self):
    #     self.assertEqual(SyncORM.get_tg_id('dak_dolka'), 2147483647)

if __name__ == '__main__':
    unittest.main()