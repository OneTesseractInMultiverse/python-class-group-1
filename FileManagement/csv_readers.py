import pprint
from loaders.csv_loader import CsvLoader
from real_state_sale import (
    RealStateSale, 
    convert_list_of_dict_to_list_of_real_state_sales, 
    RealStateSales
)

csv_loader = CsvLoader("sample_data.csv")
sales = RealStateSales(csv_loader.rows)
print("El total de las ventas es {}".format(sales.average_price))



