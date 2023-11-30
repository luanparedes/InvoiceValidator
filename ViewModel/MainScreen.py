from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
from datetime import date
import xlsxwriter
import openpyxl
import os

from Control.ExcelService import ExcelService
from Control.SpreadsheetTypeEnum import SpreadsheetTypeEnum

Builder.load_file("View/MainScreen.kv")


class MainScreen(Screen):
    # region Properties and variables

    folderPath = ListProperty(["", "", ""])
    excel = ExcelService()

    # endregion

    # region Constructor

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = None

    # endregion

    # region Events

    def try_button_click(self):
        self._open_file_manager()

    def generate_relatory_click(self):
        self._open_file_manager(True)
        # self.excel.write_excel()
        self.excel.read_excel(self.folderPath, SpreadsheetTypeEnum.BASE)
        self.excel.read_excel(self.folderPath, SpreadsheetTypeEnum.SMART)
        self.excel.read_excel(self.folderPath, SpreadsheetTypeEnum.RECEIVE)

    # endregion

    # region Handlers

    def select_path(self, path: str):
        self.folderPath = path
        self.exit_manager()

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    # endregion

    # region Methods

    def _open_file_manager(self, is_saving=False):
        path = os.path.expanduser("~")  # path to the directory that will be opened in the file manager
        self.file_manager = MDFileManager(exit_manager=self.exit_manager, select_path=self.select_path,)

        if is_saving:
            self.file_manager.selector = "folder"
        else:
            self.file_manager.selector = "multi"

        self.file_manager.show(path)

    def _file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    # endregion