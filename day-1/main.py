from chronal_calibrator import ChronalCalibrator
from file_reader import FileReader

frequencies = FileReader.read('./input')
chronal_calibrator = ChronalCalibrator(frequencies)

print('Part 1: ', chronal_calibrator.calibrate())
print('Part 2: ', chronal_calibrator.first_duplicated_frequency())
