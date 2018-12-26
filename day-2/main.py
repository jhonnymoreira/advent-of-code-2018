from file_reader import FileReader
from inventory_management import InventoryManagement

box_ids = FileReader.read('./input')
inventory_management = InventoryManagement(box_ids)

print('Part 1: ', inventory_management.checksum())
