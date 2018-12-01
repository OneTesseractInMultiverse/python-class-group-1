import pprint
from loaders.csv_loader import CsvLoader

csv_loader = CsvLoader("sample_data.csv")
pprint.pprint(csv_loader.rows)



