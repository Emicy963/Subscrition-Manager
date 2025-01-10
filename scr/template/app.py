from decimal import Decimal
import __init__
from scr.views.view import SubscriptionService
from scr.models.model import Subscription
from scr.models.database import engine
from datetime import datetime

class UI:
    def __init__(self):
        self.subscription_service = SubscriptionService(engine)

    def add_subscription(self):
        comporation = input("Company: ")
        site = input("Site: ")
        subscription_date = datetime.strptime(input('Data de assinatura: '), '%d/%m/%Y')
        price = Decimal(input("Price: "))

        subscription = Subscription(comporation=comporation, 
                                    site=site, 
                                    subscription_date=subscription_date,
                                    price_subscription=price)
        self.subscription_service.create(subscription)
        print("Sucess in Subscription!")

    def delete_subscription(self):
        subscriptions = self.subscription_service.list_all()
        print("Choose which subscriptions do you wanna delete.")

        for i in subscriptions:
            print(f'[{i.id}] -> {i.comporation}')

        choice = int(input('Choose the subscription: '))
        self.subscription_service.delete(choice)
        print('Subscription Delete with Sucess')

    def total_values(self):
        print(f'Your total month subscriptions: {self.subscription_service.total_value()}')
    
    def start(self):
        while True:
            print('''
                  [1] -> Add Subscription.
                  [2] -> Remove the Subscription.
                  [3] -> Total Values.
                  [4] -> Expenses in the last 12 months.
                  [5] -> Exit.''')
            
            choice = int(input('Choose the a option: '))

            if choice == 1:
                self.add_subscription()
            elif choice == 2:
                self.delete_subscription()
            elif choice == 3:
                self.total_values()
            elif choice == 4:
                self.subscription_service.gen_chart()
            elif choice == 5:
                break
            else:
                print('Invalid option. Try again!')

if __name__ == '__main__':
    UI().start()
