import pandas
from importing.config import *


class CsvImporter:
    # file = DEFAULT_FILEPATH + DEFAULT_FILENAME
    file = 'importing/RKI_COVID19.csv'
    data = None

    def __init__(self):
        self.data = self.read_file()

    def read_file(self):
        return pandas.read_csv(self.file, dtype='str')

    def get_row(self, row, get_as_list=True):
        if get_as_list:
            return self.data.loc[row].tolist()
        else:
            return self.data.loc[row]

    def get_by_header_term(self, header, term):
        return self.data[self.data[header].str.contains(term)]

    def get_all_from_column(self, column):
        return self.data[column].unique()
