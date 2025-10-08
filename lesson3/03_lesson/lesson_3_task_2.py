from smartphone import Smartphone

Phone1 = Smartphone("Samsung", "Galaxy S21", "+79123456789")
Phone2 = Smartphone("Apple", "iPhone 13", "+79234567890")
Phone3 = Smartphone("Poco", "POCO 14", "+79234756290")
Phone4 = Smartphone("Sony", "Super100", "+79454567890")
Phone5 = Smartphone("Alcatel", "Big200", "+79234512340")

catalog = [Phone1, Phone2, Phone3, Phone4, Phone5]
for smartphone in catalog:
    print(f"{smartphone.firma} - {smartphone.model}. {smartphone.number}")