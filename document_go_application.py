import subprocess
import os
from _shared.widget_helper import WidgetHelper


def get_subfolder_objs(project_path: str, folder_name: str) -> list:
    cmds: list[str] = ['go', 'doc', f'{project_path}/{folder_name}']
    applicable_objs: list = [f'\n### Folder Name: {folder_name}',
                             '---------------------------------------------------------------------------------------']

    with subprocess.Popen(cmds, stdout=subprocess.PIPE, text=True) as process:
        # noinspection PyTypeChecker
        for line in process.stdout:
            if any(word in line for word in ['func', 'type']):
                applicable_objs.append(f'- {line.strip()}')

    applicable_objs.append('-----------------------------------------------------------------------------------------')

    return applicable_objs


if __name__ == '__main__':
    proj_path: str = WidgetHelper.get_selected_folder()
    folders: list[str] = []
    appl_objs: list = []

    for item in os.listdir(proj_path):
        full_path = os.path.join(proj_path, item)
        if os.path.isdir(full_path) and item not in ['.git', '.idea']:
            print(item)
            folders.append(item)

    for folder in folders:
        appl_objs += get_subfolder_objs(proj_path, folder)

    with open(f'{proj_path}/CODE-REFERENCE-README.md', 'w') as file:
        for appl_obj in appl_objs:
            file.write(appl_obj + '\n')

        file.write('-------------------------------------------------------------------------------------------------')
