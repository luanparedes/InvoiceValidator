from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from Control.SpreadsheetTypeEnum import SpreadsheetTypeEnum
from ViewModel.WorksheetBase import WorksheetBase

Builder.load_file("View/WorksheetBaseScreen.kv")


class WorksheetBaseScreen(WorksheetBase):
    # region Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.data_tables = None

        self.initialize()
    # endregion

    def initialize(self):
        self.data_tables = MDDataTable(
            use_pagination=False,
            check=False,
            background_color_cell="#155555",
            sorted_order="ASC",
            elevation=2,
            column_data=[
                ("Access Key", dp(30)),
                ("Status", dp(30)),
                ("Signal Name", dp(60)),
                ("Severity", dp(30)),
                ("Stage", dp(30)),
                ("Schedule", dp(30)),
                ("Team devs", dp(30)),
                ("Team testers", dp(30)),
                ("Team designers", dp(30)),
                ("Team pmos", dp(30)),
            ],
        )

        self.add_widget(self.data_tables)

    def on_enter_worksheet(self):
        self.fill_table(SpreadsheetTypeEnum.BASE)
        