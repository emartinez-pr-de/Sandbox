import niquests
from datetime import datetime as dt

BASE_API_URL: str = 'https://cpbjr.github.io/catholic-readings-api'
# https://github.com/cpbjr/catholic-readings-api


class CatholicReadings:
    @staticmethod
    def get_month_day_yr(date: str) -> tuple[str, str, str]:
        date_time = dt.strptime(date, '%Y-%m-%d')
        month = str(date_time.month) if len(str(date_time.month)) > 1 else f'0{date_time.month}'
        day = str(date_time.day) if len(str(date_time.day)) > 1 else f'0{date_time.day}'
        year = str(date_time.year)

        return month, day, year

    @staticmethod
    def get_readings_by_date(date: str) -> None:
        month, day, year = CatholicReadings.get_month_day_yr(date)
        url: str = f'{BASE_API_URL}/readings/{year}/{month}-{day}.json'
        print(f'URL: {url}')

        results = niquests.get(url)

        if results.status_code == 200:
            print(results.json())
        else:
            print(results.status_code)

    @staticmethod
    def get_celebration_by_date(date: str) -> None:
        month, day, year = CatholicReadings.get_month_day_yr(date)
        url: str = f'{BASE_API_URL}/liturgical-calendar/{year}/{month}-{day}.json'
        print(f'URL: {url}')

        results = niquests.get(url)

        if results.status_code == 200:
            print(results.json())
        else:
            print(results.status_code)


if __name__ == '__main__':
    # date_str: str = '2026-04-07'
    date_str: str = dt.now().strftime('%Y-%m-%d')

    CatholicReadings.get_readings_by_date(date_str)
    print('')
    CatholicReadings.get_celebration_by_date(date_str)
