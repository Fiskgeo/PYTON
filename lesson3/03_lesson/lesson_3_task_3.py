from Address import Address
from Mailing import Mailing
to_address = Address(113326, "Москва", "Мира", 9, 18)
from_address = Address(352848, "Краснодар", "Орджоникидзе", 46, 17)


Postage = Mailing(to_address, from_address, 1500, "Tracknum-12345678")
print(f"Отправление из {Postage.from_address.index}, {Postage.from_address.city}, улица {Postage.from_address.street}, дом {Postage.from_address.building} - квартира {Postage.from_address.flat}")
print(f"в {Postage.to_address.index}, {Postage.to_address.city}, улица {Postage.to_address.street}, дом {Postage.to_address.building} - квартира {Postage.to_address.flat}.")
print(f"Стоимость {Postage.cost} рублей.")