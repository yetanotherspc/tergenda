import calendar
import sys
from datetime import datetime

class TerminalCalendar:
    def __init__(self):
        self.current_date = datetime.utcnow()
        self.month = self.current_date.month
        self.year = self.current_date.year

    def display_month(self):
        cal = calendar.TextCalendar(calendar.SUNDAY)
        month_calendar = cal.formatmonth(self.year, self.month)
        highlighted_date = f"\033[1;31m{self.current_date.day}\033[0m"  # Highlight current day
        month_calendar = month_calendar.replace(f"{self.current_date.day}", highlighted_date)
        print(month_calendar)

    def navigate_month(self, direction):
        if direction == "next":
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        elif direction == "prev":
            if self.month == 1:
                self.month = 12
                self.year -= 1
            else:
                self.month -= 1

    def show_week_days(self):
        print("Sun Mon Tue Wed Thu Fri Sat")

    def run(self):
        while True:
            self.show_week_days()
            self.display_month()
            command = input('Enter "next" for next month, "prev" for previous month, or "exit" to quit: ')
            if command == "exit":
                break
            self.navigate_month(command)

if __name__ == '__main__':
    TerminalCalendar().run()