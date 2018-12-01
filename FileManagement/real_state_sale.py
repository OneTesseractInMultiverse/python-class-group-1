class RealStateSale(object):

    def __init__(self, state):
        self.__baths = self.__extract_to_int(state, "baths", int)
        self.__beds = self.__extract_to_int(state, "beds", int)
        self.__latitude = self.__extract_to_int(state, "latitude", float)
        self.__longitude = self.__extract_to_int(state, "longitude", float)
        self.__price = self.__extract_to_int(state, "price", float)
        self.__sale_date = state["sale_date"]
        self.__sq__ft = self.__extract_to_int(state, "sq__ft", int)
        self.__state = state["state"]
        self.__street = state["street"]
        self.__type = state["type"]
        self.__zip = self.__extract_to_int(state, "zip", int)

    @property
    def price(self):
        return self.__price

    def __extract_to_int(self, state, key, conv_function):
        if key in state:
            return self.__securely_convert_to_int(state[key], conv_function)
        else:
            return 0

    def __securely_convert_to_int(self, string_value, conv_function):
        try:
            return conv_function(string_value)
        except Exception as e:
            # TODO realizar un manejo granular de las excepciones
            return 0


def convert_list_of_dict_to_list_of_real_state_sales(list_of_dict):
    list_of_real_state_sales = []
    for state in list_of_dict:
        list_of_real_state_sales.append(RealStateSale(state))
    return list_of_real_state_sales


class RealStateSales(object):

    def __init__(self, list_of_sale_dictionaries):
        self.__sales = convert_list_of_dict_to_list_of_real_state_sales(list_of_sale_dictionaries)

    @property
    def total_sales(self):
        total_ventas = 0
        for sale in self.__sales:
            total_ventas = total_ventas + sale.price
        return total_ventas

    @property
    def average_price(self):
        return self.total_sales / len(self.__sales)