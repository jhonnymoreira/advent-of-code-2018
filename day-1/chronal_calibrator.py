from functools import reduce

class ChronalCalibrator:
    def __init__(self, frequencies):
        self.frequencies = frequencies

    def calibrate(self):
        return reduce(self.__sum__, self.frequencies)

    def first_duplicated_frequency(self):
        print('It may take a while...')
        generated_frequencies = [0]
        duplicated_frequency = None

        i = 0
        while duplicated_frequency == None:
            x = generated_frequencies[-1]
            y = self.frequencies[i]

            i = self.__manage_index__(i)

            new_frequency =  self.__sum__(x, y)

            if new_frequency in generated_frequencies:
                duplicated_frequency = new_frequency
            else:
                generated_frequencies.append(new_frequency)

        return duplicated_frequency

    def __sum__(self, x, y):
        return int(x) + int(y)

    def __manage_index__(self, current_index):
        new_index = current_index + 1

        return 0 if new_index > len(self.frequencies) - 1 else new_index

