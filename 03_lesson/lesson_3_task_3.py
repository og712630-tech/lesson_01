from address import Address
from mailing import Mailing

def format_address(address):
    return f"{address.index}, {address.city}, {address.street}, {address.house} - {address.apartment}"

to_address = Address("123456", "Москва", "Тверская", "10", "45")
from_address = Address("654321", "Санкт-Петербург", "Невский", "25", "12")

mailing = Mailing(to_address, from_address, 350.50, "TRACK123456789")

print(f"Отправление {mailing.track} из {format_address(mailing.from_address)} в {format_address(mailing.to_address)}. Стоимость {mailing.cost} рублей.")
