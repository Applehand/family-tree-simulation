from src.entities.network import SocialNetwork
import time
import datetime

class Simulation:

    def __init__(self, network: SocialNetwork) -> None:
        self.ongoing = False
        self.network = network
        self.start_date = datetime.date(2020, 1, 1)
        self.days_passed = 0
        self.current_date = self.start_date

    def daily_update(self):
        self.update_current_date()
        self.network.check_for_birthdays(self.current_date)
        self.network.update_random_member(self.current_date)
        print(self.current_date)
        print(f'# Alive: {len(self.network.alive_members)}')

    def update_current_date(self):
        self.days_passed += 1
        current_date = self.start_date + datetime.timedelta(days=self.days_passed)
        self.current_date = current_date

    def begin_simulation(self, interval=.1):
        self.ongoing = True
        while self.ongoing:
            self.daily_update()
            time.sleep(interval)
