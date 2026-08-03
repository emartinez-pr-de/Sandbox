import niquests
import os

API_KEY = os.getenv('ExchangeRate_ApiKey')
BASE_API_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}'
# https://www.exchangerate-api.com/docs/pair-conversion-requests


class ExchangeRates:
    @staticmethod
    def get_exchange_rates(currency_unit: str) -> None:
        url: str = f'{BASE_API_URL}/latest/{currency_unit}'
        results = niquests.get(url)
        print(f'--- *[ Currency Unit: {currency_unit} ]* ---\nURL: {url}')

        if results.status_code == 200:
            print(f"{results.json()['conversion_rates']}\n")
            print(f"USD Per {currency_unit}: {results.json()['conversion_rates']['USD']} USD")
            print(f"British Pound Per {currency_unit}: {results.json()['conversion_rates']['GBP']} GBP")
            print(f"Euro Per {currency_unit}: {results.json()['conversion_rates']['EUR']} EUR")
            print(f"Philippines Peso Per {currency_unit}: {results.json()['conversion_rates']['PHP']} PHP")
        else:
            print(results.status_code)

    @staticmethod
    def convert_amt_to_other_currency(from_currency: str, to_currency: str, amt: int) -> None:
        url: str = f'{BASE_API_URL}/pair/{from_currency}/{to_currency}/{amt}'
        results = niquests.get(url)
        print(f'--- *[ {str(amt)} {from_currency} to {to_currency} ]* ---\nURL: {url}')

        if results.status_code == 200:
            print(f"{amt:,} {from_currency} = {results.json()['conversion_result']:,.2f} {to_currency}")


if __name__ == '__main__':
    # ExchangeRates.get_exchange_rates('USD')
    ExchangeRates.convert_amt_to_other_currency('PHP', 'USD', 80_000)
