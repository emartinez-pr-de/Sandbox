import tkinter
from tkinter import filedialog, ttk
import calendar


class WidgetHelper:
    @staticmethod
    def get_selected_folder() -> str:
        root = tkinter.Tk()
        root.withdraw()
        root.attributes('-topmost', -1)

        dir_and_folder = filedialog.askdirectory(title='Select Folder')

        print(f'Selected Folder: {dir_and_folder}\n')

        return dir_and_folder

    @staticmethod
    def get_selected_month() -> str:
        root = tkinter.Tk()
        root.title('Select Month')
        root.geometry('250x250')
        style = ttk.Style()
        style.theme_use('alt')

        combo = ttk.Combobox(root, values=list(calendar.month_abbr))
        combo.pack()

        def on_select(_) -> str:
            print(f'Selected: {combo.get()}')

            return combo.get()

        selected_month = combo.bind('<<ComboboxSelected>>', on_select)
        root.mainloop()

        return selected_month


if __name__ == '__main__':
    # WidgetHelper.get_selected_folder()
    WidgetHelper.get_selected_month()
