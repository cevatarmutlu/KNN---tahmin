import xlrd
import math
from heapq import nsmallest
from xlwt import Workbook

def print_rows(excel):
    for row in range(excel.nrows):
        print(excel.row_values(row), row)


def euclidean(process_row, center):
    return math.sqrt(sum([pow(x[0] - x[1], 2) for x in zip(process_row, center)]))


def knn_sorgu_excel(excel_path, excel_sheet_index: int):
    wb = xlrd.open_workbook(excel_path)
    sheet = wb.sheet_by_index(excel_sheet_index)
    return sheet


def tahmin_deger_getir(array):
    top = 0
    for i in range(len(array)):
        top += float(knn.excel.row_values(array[i])[sorgu_index]) / len(array)
    return top

class KNN:
    def __init__(self, num_k: int, excel_path, excel_sheet_index: int):
        self.k = num_k
        self.path = excel_path
        self.sheet_index = excel_sheet_index
        self.excel = self.__open_excel()

    def __open_excel(self):
        wb = xlrd.open_workbook(self.path)
        sheet = wb.sheet_by_index(self.sheet_index)
        return sheet

if __name__ == "__main__":
    wb = Workbook()
    sheet = wb.add_sheet("tahmin")

    knn_sorgu = knn_sorgu_excel("knn_sorgu.xlsx", 0)
    knn = KNN(3, "bezdekIris.xlsx", 0)
    for a in range(knn_sorgu.nrows):
        sorgu = knn_sorgu.row_values(a)
        sorgu_index = sorgu.index('')
        sorgu.pop(sorgu_index)
        uzaklik_array = []
        knn_uzaklik = []
        tahmin_deger = 0

        for i in range(knn.excel.nrows):
            kayit = list(map(float, knn.excel.row_values(i)))
            kayit.pop(sorgu_index)
            sorgu = list(map(float, sorgu))
            uzaklik_array.append(euclidean(sorgu, kayit))

        en_yakin_sorgu_index = nsmallest(knn.k, uzaklik_array)
        for i in range(len(en_yakin_sorgu_index)):
            knn_uzaklik.append(uzaklik_array.index(en_yakin_sorgu_index[i]))

        tahmin_deger = tahmin_deger_getir(knn_uzaklik)
        sheet.write(a, 0, tahmin_deger)
        print(tahmin_deger)

    wb.save("knn_tahmin.xlsx")
