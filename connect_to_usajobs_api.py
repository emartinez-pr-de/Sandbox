import niquests
import os
# https://developer.usajobs.gov/api-reference/
# https://developer.usajobs.gov/api-reference/get-api-search

BASE_URL: str = 'https://data.usajobs.gov/api'
USA_GOV_HEADERS = {
    'Host': 'data.usajobs.gov',
    'User-Agent': str(os.getenv('UsaJobsGov_UserAgent')),
    'Authorization-Key': str(os.getenv('UsaJobsGov_AuthKey'))
}


class UsaJobsApi:
    @staticmethod
    def get_jobs_by_keyword(keyword: str) -> None:
        url: str = f'{BASE_URL}/search?keyword={keyword}'
        results = niquests.get(url, headers=USA_GOV_HEADERS)
        print(f'--- *[ Keyword: {keyword} ]* ---\nURL: {url}')

        if results.status_code == 200:
            # print(results.json())
            for result in results.json()['SearchResult']['SearchResultItems']:
                print(result)
        else:
            print(results.status_code)

    @staticmethod
    def get_results_by_endpoint(endpoint: str) -> None:
        url: str = f'{BASE_URL}/codelist/{endpoint}'
        results = niquests.get(url)
        print(f'URL: {url}')

        if results.status_code == 200:
            for result in results.json()['CodeList']:
                for code in result['ValidValue']:
                    print(code)
        else:
            print(results.status_code)


if __name__ == '__main__':
    # keywords: list[str] = ['Software', 'Python', 'Java']

    # for k in keywords:
    #     UsaJobsApi.get_jobs_by_keyword(k)
    #     print('')

    # TODO: Will likely load these end points from DuckDB or similar
    end_points: list[str] = ['academichonors', 'academiclevels', 'countries', 'documentations', 'ethnicities',
                             'hiringpaths', 'travelpercentages']

    for end_point in end_points:
        UsaJobsApi.get_results_by_endpoint(end_point)
        print('')
