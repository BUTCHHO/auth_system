from datetime import datetime, timedelta

class TimeHandler:
    @staticmethod
    def add_days_to_current_date(days):
        time_delta = timedelta(days=days)
        now = datetime.today()
        new_date = now + time_delta
        return new_date

    @staticmethod
    def is_date_future(date):
        return datetime.now().date() < date

    @staticmethod
    def get_today_date():
        return datetime.today()

    @staticmethod
    def get_str_today_date():
        return TimeHandler.get_today_date().strftime('%d/%m/%Y')