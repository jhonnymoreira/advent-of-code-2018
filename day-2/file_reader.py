class FileReader:
    @staticmethod
    def read(file_path):
        return open(file_path, 'r').read().splitlines()
