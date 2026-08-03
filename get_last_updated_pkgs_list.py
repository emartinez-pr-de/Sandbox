from importlib.metadata import distributions
import os
import datetime as dt


class PkgHelper:
    @staticmethod
    def get_installed_pkg_details(today_only: bool = False) -> None:
        pkg_details = []

        for pkg in distributions():
            pkg_info = {
                'datetime': dt.datetime.fromtimestamp(os.path.getctime(pkg._path)),
                'name': pkg.metadata['Name'],
                'version': pkg.version,
            }

            pkg_details.append(pkg_info)

        info_sorted = sorted(pkg_details, key=lambda x: x['name'].lower())

        for info in info_sorted:
            date_time: str = info['datetime'].strftime('%m/%d/%Y %I:%M:%S %p')

            if not today_only:
                print(f"{info['name']} | {info['version']} | {date_time}")
            elif today_only and info['datetime'].date() == dt.datetime.now().date():
                print(f"{info['name']} | {info['version']} | {date_time}")


if __name__ == '__main__':
    # PkgHelper.get_installed_pkg_details()
    PkgHelper.get_installed_pkg_details(True)
