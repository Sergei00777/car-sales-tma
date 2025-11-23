# cars_data.py
from data.cars_in_stock import cars_in_stock
from data.cars_on_order import cars_on_order
from data.cities_data import cities_data

# Объединяем все автомобили в один словарь
cars_data = {**cars_in_stock, **cars_on_order}