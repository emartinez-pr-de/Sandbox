import niquests

BASE_API_URL: str = 'https://bible.helloao.org/api'


class HelloAoBible:
    @staticmethod
    def get_available_translations() -> None:
        url: str = f'{BASE_API_URL}/available_translations.json'

        results = niquests.get(url)

        if results.status_code == 200:
            for result in results.json()['translations']:
                print(result)
                print(result['id'])

    @staticmethod
    def get_available_translations_by_lang(lang: str) -> None:
        url: str = f'{BASE_API_URL}/available_translations.json'
        print(f'----- *[ Language = {lang.title()} ]* --------------------')

        results = niquests.get(url)

        if results.status_code == 200:
            for result in results.json()['translations']:
                if result['id'][:3] == lang:
                    print(result)


if __name__ == '__main__':
    # HelloAoBible.get_available_translations()

    for idioma in ('eng', 'fra', 'deu', 'ceb'):
        HelloAoBible.get_available_translations_by_lang(idioma)
        print('')
