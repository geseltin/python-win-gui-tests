from comtypes.client import CreateObject
import os



class GroupData:
    def __init__(self):
        self.xl = CreateObject("Excel.Application")
        self.project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def create_excel_with_group_data(self):
        wb = self.xl.Workbooks.Add()
        for i in range(5):
            self.xl.Range["A%s" % (i + 1)].Value[()] = "group %s" % i
        wb.SaveAs(os.path.join(self.project_dir, "groups.xlsx"))
        self.xl.Quit()

    def read_group_data_from_excel(self):
        wb = self.xl.Workbooks.Open(self.project_dir + "\\groups.xlsx")
        worksheet = wb.Sheets[1]

        group_list = []
        for row in range(1, 6):
            data = worksheet.Cells[row, 1].Value()
            group_list.append(data)

        self.xl.Quit()
        print(group_list)
        return group_list



# a = GroupData()
# a.create_excel_with_group_data()

