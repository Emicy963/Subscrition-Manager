import __init__
from models.database import engine
from models.model import Subscription, Payments
from sqlmodel import Session, select
from datetime import date, datetime


class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            return subscription
    
    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement).all()
        return results
    
    def delete(self, id):
        with Session(self.engine) as session:
            statement = select(Subscription).where(Subscription.id == id)
            result = session.exec(statement).one()
            session.delete(result)
            session.commit()
    
    def _has_pay(self, results):
        for result in results:
                if result.date.month == date.today().month:
                    return True
        return False

    def pay(self, subscription:Subscription):
        with Session(self.engine) as session:
            statement = select(Payments).join(Subscription).where(Subscription.comporation==subscription.comporation)
            results = session.exec(statement).all()
            print(results)

            if self._has_pay(results):
                question = input("It's count already pay that mouth, do you want pay again? Y/N ")

                if not question.upper()[0] == 'y':
                    return
            
            pay = Payments(Subscription_id=subscription.id, date=date.today())
            session.add(pay)
            session.commit()

    def total_value(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement).all()

        total = 0
        for result in results:
            total += result.price_subscription

        return float(total)
    
    def _get_last_12_months_native(self):
        today = datetime.now()
        year = today.year
        month = today.month
        last_12_month = []
        for _ in range(12):
            last_12_month.append((month, year))
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        return last_12_month[::-1]
    
    def _get_values_for_month(self, last_12_month):
        with Session(self.engine) as session:
            statement = select(Payments)
            results = session.exec(statement).all()

            values_for_month = []
            for i in last_12_month:
                values = 0
                for result in results:
                    if result.date.month == i[0] and result.date.year == i[1]:
                        values += float(result.subscription.price_subscription)
                values_for_month.append(values)
            return values_for_month

    def gen_chart(self):
        last_12_months = self._get_last_12_months_native()
        values_for_month = self._get_values_for_month(last_12_months)
        last_12_months = list(map(lambda x: x[0], self._get_last_12_months_native()))

        import matplotlib.pyplot as plt

        plt.plot([last_12_months], [values_for_month])
        plt.show()


ss = SubscriptionService(engine)
print(ss.gen_chart())