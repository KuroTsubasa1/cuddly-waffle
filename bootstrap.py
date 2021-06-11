from importing.importer import CsvImporter
from processing.processor import Processor

# run program from here

csv_importer = CsvImporter()

# get row with specified index
#row = csv_importer.get_row(1, False)
#print(row)
#print(len(row))
#print(row[0])

tmp_data = csv_importer.get_by_header_term('Meldedatum', '2021/01/12 00:00:00')

print(tmp_data)

processor = Processor()

gender_data = processor.get_infections_by_gender_by_date(tmp_data)

print(gender_data.loc["W"])

print("Test")

