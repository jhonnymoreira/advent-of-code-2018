from collections import Counter

class InventoryManagement:
    def __init__(self, box_ids):
        self.box_ids = box_ids

    def checksum(self):
        ids_letters_frequency = map(Counter, self.box_ids)

        two_letters_frequency = 0
        three_letters_frequency = 0

        for letters_frequency in ids_letters_frequency:
            frequencies = letters_frequency.values()

            if 2 in frequencies:
                two_letters_frequency += 1
            if 3 in frequencies:
                three_letters_frequency += 1

        return two_letters_frequency * three_letters_frequency
