from importing.importer import CsvImporter
from processing.processor import Processor

# run program from here

csv_importer = CsvImporter()

# get row with specified index
row = csv_importer.get_row(1)
print(row)
row = csv_importer.get_row(1, False)
print(row)
#print(row)
#print(len(row))
#print(row[0])

# select all rows with 2021/01/12 00:00:00
#tmp_data = csv_importer.get_by_header_term('Meldedatum', '2021/01/12 00:00:00')

#test = csv_importer.get_all_from_column('Bundesland')

#print(test)

#print(tmp_data)
#
#processor = Processor()
#
#gender_data = processor.get_infections_by_gender_by_date(tmp_data)
#
#print(gender_data.loc["W"])
#
#print("Test")
