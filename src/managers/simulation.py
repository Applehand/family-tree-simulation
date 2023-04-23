from src.entities.tree import FamilyTree
import time
import calendar
import datetime

class Simulation:
    def __init__(self, family_tree: FamilyTree) -> None:
        self.tree = family_tree
        self.start_date = datetime.date(2020, 1, 1)
        self.days_passed = 0

    def daily_update(self):
        self.days_passed += 1

    def get_current_date(self):
        return self.start_date + datetime.timedelta(days=self.days_passed)

    def begin_simulation(self, interval=1):
        while True:
            self.daily_update()
            current_date = self.get_current_date()
            print(current_date)
            time.sleep(interval)
           