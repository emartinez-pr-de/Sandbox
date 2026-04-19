import niquests

BASE_API_URL: str = 'https://holy-bible-api.com'
# https://holy-bible-api.com/docs/


class HolyBibleApi:
    @staticmethod
    def get_available_bibles() -> None:
        url: str = f'{BASE_API_URL}/bibles'

        bibles = niquests.get(url)

        if bibles.status_code == 200:
            for bible in bibles.json():
                print(bible)

    @staticmethod
    def get_available_bibles_by_language(lang: str) -> None:
        url: str = f'{BASE_API_URL}/bibles'

        bibles = niquests.get(url)

        if bibles.status_code == 200:
            for bible in bibles.json():
                if bible['language'] == lang:
                    print(bible)

    @staticmethod
    def get_bible_verse_of_the_day(bible_id: int) -> None:
        url: str = f'{BASE_API_URL}/bibles/{bible_id}/verse-of-the-day'

        verse = niquests.get(url)

        if verse.status_code == 200:
            print(verse.json())


if __name__ == '__main__':
    # HolyBibleApi.get_available_bibles()

    '''
    for idioma in ['english', 'spanish', 'german', 'cebuano', 'tagalog']:
        HolyBibleApi.get_available_bibles_by_language(idioma)
        print('')
    '''

    for biblia_id in [230, 293, 107]:
        HolyBibleApi.get_bible_verse_of_the_day(biblia_id)
        print('')
