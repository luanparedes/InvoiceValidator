from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
import os
from Control.ExcelService import ExcelService
from Control.NavigationService import ScreenEnum
from Control.SpreadsheetTypeEnum import SpreadsheetTypeEnum, SpreadsheetTypeNumberEnum

Builder.load_file("View/SelectFilesScreen.kv")


class SelectFilesScreen(Screen):
    # region Properties and variables
    folderPath = ListProperty(["", "", ""])
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
        ExcelService.write_excel(ExcelService)
        ExcelService.read_excel(ExcelService, self.folderPath,
                                SpreadsheetTypeEnum.BASE, SpreadsheetTypeNumberEnum.BASE)
        ExcelService.read_excel(ExcelService, self.folderPath,
                                SpreadsheetTypeEnum.SMART, SpreadsheetTypeNumberEnum.SMART)
        ExcelService.read_excel(ExcelService, self.folderPath,
                                SpreadsheetTypeEnum.RECEIVE, SpreadsheetTypeNumberEnum.RECEIVE)

        self.parent.screen = ScreenEnum.MAIN_WORKBOOK
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
