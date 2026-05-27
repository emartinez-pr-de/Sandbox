import re
from pathlib import Path
from importlib.metadata import version
from _shared.file_mgmt import FileMgmt
from _shared.widget_helper import WidgetHelper

REQS_FILE: str = 'requirements.txt'
TEMP_REQS_FILE: str = 'requirements_temp.txt'


class PkgDetection:
    @staticmethod
    def get_all_files(root_folder: Path) -> list[Path]:
        return [p for p in Path(root_folder).rglob('*.py')]

    @staticmethod
    def find_packages_by_pattern(root_folder: Path, project_path: str, key_word: str):
        packages = []

        for file in PkgDetection.get_all_files(root_folder):
            with open(str(file), 'r') as file_object:
                for line in file_object:
                    if f'{key_word} ' in line:
                        pattern = rf'\b{key_word}\b\s+(\w+)'
                        match = re.search(pattern, line, re.IGNORECASE)

                        if match:
                            package = match.group(1)

                            if package not in packages:
                                packages.append(package.lower())

        with open(f'{project_path}/{TEMP_REQS_FILE}', 'a') as f:
            for pkg in packages:
                try:
                    f.write(f'{pkg}=={version(str(pkg))}\n')
                except Exception:
                    pass

    @staticmethod
    def remove_duplicate_deps_from_file(project_path: str) -> None:
        seen_lines: set[str] = set()

        with open(f'{project_path}/{TEMP_REQS_FILE}', 'r') as f_in, open(f'{project_path}/{REQS_FILE}', 'w') as f_out:
            for line in f_in:
                if line not in seen_lines:
                    f_out.write(line)
                    seen_lines.add(line)


if __name__ == '__main__':
    count: int = int(input('How many trials do you want to run? '))

    for x in range(count):
        proj_path: str = WidgetHelper.get_selected_folder()
        root: Path = Path(proj_path)
        existing_file_deleted: bool = FileMgmt.delete_file(f'{proj_path}/{REQS_FILE}')

        if existing_file_deleted:
            PkgDetection.find_packages_by_pattern(root, proj_path, 'from')
            PkgDetection.find_packages_by_pattern(root, proj_path, 'import')
            PkgDetection.remove_duplicate_deps_from_file(proj_path)

            FileMgmt.delete_file(f'{proj_path}/{TEMP_REQS_FILE}')

        # TODO: Add an open explorer call here later.
