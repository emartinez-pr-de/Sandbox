from importlib.metadata import distributions
import os
import datetime as dt


class PkgHelper:
    @staticmethod
    def get_installed_pkg_details() -> None:
        pkg_details = []

        for pkg in distributions():
            pkg_info = {
                'datetime': dt.datetime.fromtimestamp(os.path.getctime(pkg._path)),
                'name': pkg.metadata['Name'],
                'version': pkg.version,
            }

            pkg_details.append(pkg_info)

        info_sorted = sorted(pkg_details, key=lambda x: x['name'].lower())

        for i in info_sorted:
            date_time: str = i['datetime'].strftime('%m/%d/%Y %I:%M:%S %p')

            print(f"{i['name']} | {i['version']} | {date_time}")


if __name__ == '__main__':
    PkgHelper.get_installed_pkg_details()
