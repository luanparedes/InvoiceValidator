from kivy.uix.screenmanager import Screen
from Control.ExcelService import ExcelService


class WorksheetBase(Screen):

    # region Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # endregion

    # region Methods
    def fill_table(self, worksheet_type):
        copied_values = []

        for row in ExcelService.access_keys[worksheet_type]:
            copied_values.clear()

            for cell in list(row):
                copied_values.append(cell.value)

            self.data_tables.row_data.append(tuple(copied_values))
    # endregion

    # region handlers
    def on_enter_worksheet(self):
        pass
    # endregion
