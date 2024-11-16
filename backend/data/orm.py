from sqlalchemy import select, and_, func, insert, or_, not_, update
from data.database import sync_engine, session_factory, Base
from data.models import DebtsHistoryORM, TripsORM, TripDebtsORM, Tg_idsORM
from datetime import datetime, timezone
from bot.dop import bot
from aiogram.exceptions import TelegramBadRequest
import asyncio


async def send_notification(debtor):
    chat_id = SyncORM.get_tg_id(debtor)
    await bot.send_message(chat_id = chat_id, text='Уведомление о добавлении долга')
    return 


class SyncORM:
    @staticmethod
    def create_table():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
    
        
    @staticmethod
    def insert_data():
        with session_factory() as session:
            create = [
            {
                "f_tg_tag_debtor": "@ivan",
                "f_tg_tag_lender": "@petr",
                "f_debt_amount": 150
            },
            {
                "f_tg_tag_debtor": "@ivan",
                "f_tg_tag_lender": "@petr",
                "f_debt_amount": 200
            },
            {
                "f_tg_tag_debtor": "@ivan",
                "f_tg_tag_lender": "@oleg",
                "f_debt_amount": 50
            },
            {
                "f_tg_tag_debtor": "@sveta",
                "f_tg_tag_lender": "@petr",
                "f_debt_amount": 150
            },
            {
                "f_tg_tag_debtor": "@sveta",
                "f_tg_tag_lender": "@oleg",
                "f_debt_amount": 75
            },
            {
                "f_tg_tag_debtor": "@petr",
                "f_tg_tag_lender": "@ivan",
                "f_debt_amount": 300
            },
            {
                "f_tg_tag_debtor": "@oleg",
                "f_tg_tag_lender": "@ivan",
                "f_debt_amount": 25
            },
            {
                "f_tg_tag_debtor": "@oleg",
                "f_tg_tag_lender": "@sveta",
                "f_debt_amount": 100
            }
        ]
            insert_data = insert(DebtsHistoryORM).values(create)
            trips_data = [
            {
                "f_trip_name": "Trip 1",
                "f_start_date": datetime(2024, 11, 8, 0, 0, 0, tzinfo=timezone.utc),
                "f_end_date": datetime(2024, 11, 15, 0, 0, 0, tzinfo=timezone.utc),
                "f_is_ended": False
            },
            {
                "f_trip_name": "Trip 2",
                "f_start_date": datetime(2024, 11, 16, 0, 0, 0, tzinfo=timezone.utc),
                "f_end_date": datetime(2024, 11, 23, 0, 0, 0, tzinfo=timezone.utc),
                "f_is_ended": False
            },
            {
                "f_trip_name": "Trip 3",
                "f_start_date": datetime(2024, 11, 24, 0, 0, 0, tzinfo=timezone.utc),
                "f_end_date": datetime(2024, 12, 1, 0, 0, 0, tzinfo=timezone.utc),
                "f_is_ended": False
            },
            {
                "f_trip_name": "Trip 4",
                "f_start_date": datetime(2024, 12, 2, 0, 0, 0, tzinfo=timezone.utc),
                "f_end_date": datetime(2024, 12, 9, 0, 0, 0, tzinfo=timezone.utc),
                "f_is_ended": False
            }
            ]
            insert_data1 = insert(TripsORM).values(trips_data)
            trip_debts_data = [
        {
            "f_trip_id": 1,
            "f_debt_amount": 100,
            "f_tg_tag_lender": "@ivan",
            "f_tg_tag_debtor": "@petr",
            "f_event_name": "Event 1",
            "f_event_date": datetime(2024, 11, 9, 7, 23, 24, tzinfo=timezone.utc)
        },
        {
            "f_trip_id": 1,
            "f_debt_amount": 200,
            "f_tg_tag_lender": "@petr",
            "f_tg_tag_debtor": "@ivan",
            "f_event_name": "Event 2",
            "f_event_date": datetime(2024, 11, 10, 12, 0, 0, tzinfo=timezone.utc)
        },
        {
            "f_trip_id": 2,
            "f_debt_amount": 50,
            "f_tg_tag_lender": "@ivan",
            "f_tg_tag_debtor": "@alex",
            "f_event_name": "Event 3",
            "f_event_date": datetime(2024, 11, 11, 15, 30, 0, tzinfo=timezone.utc)
        },
        {
            "f_trip_id": 3,
            "f_debt_amount": 150,
            "f_tg_tag_lender": "@petr",
            "f_tg_tag_debtor": "@ivan",
            "f_event_name": "Event 4",
            "f_event_date": datetime(2024, 11, 12, 18, 0, 0, tzinfo=timezone.utc)
        }, {
            "f_trip_id": 1,
            "f_debt_amount": 75,
            "f_tg_tag_lender": "@alex",
            "f_tg_tag_debtor": "@petr",
            "f_event_name": "Event 5",
            "f_event_date": datetime(2024, 11, 13, 10, 0, 0, tzinfo=timezone.utc)
        },
        {
            "f_trip_id": 2,
            "f_debt_amount": 120,
            "f_tg_tag_lender": "@ivan",
            "f_tg_tag_debtor": "@alex",
            "f_event_name": "Event 6",
            "f_event_date": datetime(2024, 11, 14, 12, 30, 0, tzinfo=timezone.utc)
        },
        {
            "f_trip_id": 3,
            "f_debt_amount": 90,
            "f_tg_tag_lender": "@petr",
            "f_tg_tag_debtor": "@ivan",
            "f_event_name": "Event 7",
            "f_event_date": datetime(2024, 11, 15, 15, 0, 0, tzinfo=timezone.utc)
        },
        {
            "f_trip_id": 1,
            "f_debt_amount": 60,
            "f_tg_tag_lender": "@alex",
            "f_tg_tag_debtor": "@ivan",
            "f_event_name": "Event 8",
            "f_event_date": datetime(2024, 11, 16, 10, 30, 0, tzinfo=timezone.utc)
        },
        {
            "f_trip_id": 2,
            "f_debt_amount": 180,
            "f_tg_tag_lender": "@petr",
            "f_tg_tag_debtor": "@alex",
            "f_event_name": "Event 9",
            "f_event_date": datetime(2024, 11, 17, 12, 0, 0, tzinfo=timezone.utc)
        }
        ]
            insert_data2 = insert(TripDebtsORM).values(trip_debts_data)
            session.execute(insert_data)
            session.execute(insert_data1)
            session.flush()
            session.execute(insert_data2)
            session.commit()
    

    # @staticmethod
    # def get_user_history(lender_tg, debtor_tg):
    #     with session_factory() as session:
    #         query = select(DebtsHistoryORM).where(and_(DebtsHistoryORM.f_tg_tag_debtor == debtor_tg, DebtsHistoryORM.f_tg_tag_lender == lender_tg))
    #         res = session.execute(query)
    #         history = res.scalars().all() 
    #         if history:
    #             return list(map(lambda x: {'amount': x.f_debt_amount, 'event_name': x.f_event_name, 'event_date': x.f_event_date}, history))
    #         return []

    @staticmethod
    def get_user_debtors(lender_tg):
        # -> tg должников и сумма
        with session_factory() as session:
            # кто должен lender_tg и сколько
            subq = select(DebtsHistoryORM.f_tg_tag_debtor.label('tg_tag_debtor'), func.sum(DebtsHistoryORM.f_debt_amount).label('debt_amount')).where(and_(DebtsHistoryORM.f_tg_tag_lender == lender_tg, DebtsHistoryORM.f_is_closed == False)).group_by(DebtsHistoryORM.f_tg_tag_debtor).subquery()
            subq_res = {elem[0]: elem[1] for elem in session.execute(select(subq)).all()}
            # кому должен lender_tg и сколько
            subq1 = select(DebtsHistoryORM.f_tg_tag_lender.label('tg_tag_lender'), func.sum(DebtsHistoryORM.f_debt_amount).label('debt_amount')).where(and_(DebtsHistoryORM.f_tg_tag_debtor == lender_tg, DebtsHistoryORM.f_is_closed == False)).group_by(DebtsHistoryORM.f_tg_tag_lender).subquery()
            # вычитание тех, кого можно вычесть
            subq2 = select(subq.c.tg_tag_debtor, (subq.c.debt_amount-subq1.c.debt_amount).label('debt_amount')).where(or_(subq.c.tg_tag_debtor == subq1.c.tg_tag_lender, not_(subq.c.tg_tag_debtor.in_(subq_res.keys())))).subquery()
            subq2_res = {elem[0]: elem[1] for elem in session.execute(select(subq2)).all()}
            #красотаааааа
            ans = []
            for elem in subq_res.keys():
                if elem in subq2_res and subq2_res[elem] > 0:
                    ans.append({'debtor_tg': elem, 'amount': subq2_res[elem]})
                elif elem in subq2_res and subq2_res[elem] <= 0:
                    continue
                else:
                    ans.append({'debtor_tg': elem, 'amount': subq_res[elem]})
            return ans
        

    @staticmethod
    def get_user_lenders(debtor_tg):
        # -> tg кому должен и сумма
        with session_factory() as session:
            # кто должен debter_tg и сколько
            subq = select(DebtsHistoryORM.f_tg_tag_debtor.label('tg_tag_debtor'), func.sum(DebtsHistoryORM.f_debt_amount).label('debt_amount')).where(and_(DebtsHistoryORM.f_tg_tag_lender == debtor_tg, DebtsHistoryORM.f_is_closed == False)).group_by(DebtsHistoryORM.f_tg_tag_debtor).subquery()
            # кому должен debter_tg и сколько
            subq1 = select(DebtsHistoryORM.f_tg_tag_lender.label('tg_tag_lender'), func.sum(DebtsHistoryORM.f_debt_amount).label('debt_amount')).where(and_(DebtsHistoryORM.f_tg_tag_debtor == debtor_tg, DebtsHistoryORM.f_is_closed == False)).group_by(DebtsHistoryORM.f_tg_tag_lender).subquery()
            subq_res = {elem[0]: elem[1] for elem in session.execute(select(subq1)).all()}
            # вычитание тех, кого можно вычесть
            subq2 = select(subq.c.tg_tag_debtor, (subq1.c.debt_amount - subq.c.debt_amount).label('debt_amount')).where(or_(subq.c.tg_tag_debtor == subq1.c.tg_tag_lender)).subquery()
            subq2_res = {elem[0]: elem[1] for elem in session.execute(select(subq2)).all()}
            #красотаааааа
            ans = []
            for elem in subq_res.keys():
                if elem in subq2_res and subq2_res[elem] > 0:
                    ans.append({'lenders_tg': elem, 'amount': subq2_res[elem]})
                elif elem in subq2_res and subq2_res[elem] <= 0:
                    continue
                else:
                    ans.append({'lenders_tg': elem, 'amount': subq_res[elem]})
            return ans
    
    
    @staticmethod
    async def insert_debt(lender_tg, debtors_tg_debpt_dict, event_name):
        asyncio.run(send_notification(debtor=debtor))
        with session_factory() as session:
            for debtor, amount in debtors_tg_debpt_dict:
                create = DebtsHistoryORM(f_tg_tag_lender=lender_tg, f_tg_tag_debtor=debtor, f_debt_amount=amount, f_event_name=event_name)
                session.add(create)
                await send_notification(debtor=debtor)
            session.commit()
    
    @staticmethod
    def remove_debt(lender_tg, debtor_tg):
        with session_factory() as session:
            query = (update(DebtsHistoryORM)
                     .where(or_(and_(DebtsHistoryORM.f_tg_tag_debtor == debtor_tg, DebtsHistoryORM.f_tg_tag_lender == lender_tg), 
                                and_(DebtsHistoryORM.f_tg_tag_debtor == lender_tg, DebtsHistoryORM.f_tg_tag_lender == debtor_tg)))
                            .values(f_is_closed=True))
            session.execute(query)
            session.commit()
            return '1'


    @staticmethod
    def get_trips(tg_tag):
        with session_factory() as session:
            query = select(TripsORM.f_id, TripsORM.f_trip_name).where(and_(TripsORM.f_id == TripDebtsORM.f_trip_id, or_(TripDebtsORM.f_tg_tag_lender == tg_tag, TripDebtsORM.f_tg_tag_debtor == tg_tag))).distinct()
            res = session.execute(query).all()
            return [{'trip_id': elem[0], 'trip_name': elem[1]} for elem in res]

    @staticmethod
    def create_trip(lender_tg, debtors_tg_debpt_dict, trip_name, f_event_name):
        with session_factory() as session:
            new_id = session.execute(select(func.max(TripsORM.f_id))).scalar() + 1
            session.add(TripsORM(f_trip_name=trip_name, fid=new_id))
            session.commit()
            SyncORM.add_trip_debt(lender_tg, debtors_tg_debpt_dict, new_id, f_event_name)
    
    @staticmethod
    def add_trip_debt(lender_tg, debtors_tg_debpt_dict, trip_id, f_event_name):
        with session_factory() as session:
            for debtor, amount in debtors_tg_debpt_dict:
                create = TripDebtsORM(f_trip_id=trip_id, f_debt_amount=amount, f_tg_tag_lender=lender_tg, f_tg_tag_debtor=debtor, f_event_name=f_event_name)
                session.add(create)
            session.commit()

    @staticmethod
    def get_trip_debts(trip_id):
        with session_factory() as session:
            query = select(TripDebtsORM.f_tg_tag_lender, TripDebtsORM.f_tg_tag_debtor, TripDebtsORM.f_debt_amount, TripDebtsORM.f_event_name).where(TripDebtsORM.f_trip_id == trip_id)
            res = session.execute(query).all()
            return [{'lender_tg': elem[0], 'debtor_tg': elem[1], 'amount': elem[2], 'event_name': elem[3]} for elem in res]
        
    @staticmethod
    def get_trip_user_debtors(lender_tg, trip_id):
        with session_factory() as session:
            #Кто должен lender_tg и сколько
            subq = select(TripDebtsORM.f_tg_tag_debtor.label('debtor_tg'), func.sum(TripDebtsORM.f_debt_amount).label('debt_amount')).where(and_(TripDebtsORM.f_tg_tag_lender == lender_tg, TripDebtsORM.f_trip_id == trip_id)).group_by(TripDebtsORM.f_tg_tag_debtor).subquery()
            subq_res = {elem[0]: elem[1] for elem in session.execute(select(subq)).all()}
            # кому должен lender_tg и сколько
            subq1 = select(TripDebtsORM.f_tg_tag_lender.label('lender_tg'), func.sum(TripDebtsORM.f_debt_amount).label('debt_amount')).where(and_(TripDebtsORM.f_tg_tag_debtor == lender_tg, TripDebtsORM.f_trip_id == trip_id)).group_by(TripDebtsORM.f_tg_tag_lender).subquery()
            subq1_res = {elem[0]: elem[1] for elem in session.execute(select(subq1)).all()}
            return [[{elem: subq_res[elem]} for elem in subq_res], [{elem: subq1_res[elem]} for elem in subq1_res]]
        
    #close trip
    @staticmethod
    def close_trip(trip_id):
        with session_factory() as session:
            query = (update(TripsORM)
                     .where(TripsORM.f_id == trip_id)
                            .values(is_closed=True))
            session.execute(query)
            session.commit()

    @staticmethod
    def add_tg_id(username, tg_id):
        with session_factory() as session:
            insert_data = Tg_idsORM(username, tg_id)
            print(insert_data.f_username, insert_data.f_tg_id)
            session.add(insert_data)
            session.commit()

    @staticmethod
    def get_tg_id(username):
        with session_factory() as session:
            res = session.execute(select(Tg_idsORM.f_tg_id).where(Tg_idsORM.f_username == username)).scalars().all()
            return res[0]

    
    