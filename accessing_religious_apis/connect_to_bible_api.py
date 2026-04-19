import niquests

BASE_API_URL: str = 'https://bible-api.com'


class BibleApi:
    @staticmethod
    def get_book_chapter_verse(book: str, chapter: int, verses: str) -> None:
        url: str = f'{BASE_API_URL}/{book} {chapter}:{verses}?translation=kjv'
        print(f'URL: {url}')

        results = niquests.get(url)

        if results.status_code == 200:
            print(results.json())

            for verse in results.json()['verses']:
                print(verse)
        else:
            print(results.status_code)


if __name__ == '__main__':
    BibleApi.get_book_chapter_verse('Matthew', 20, '26-27')
    print('')
    BibleApi.get_book_chapter_verse('Joshua', 1, '9')
