import pandas as pd

class extractCSV:
    def __init__(self, path):
        self.path = path

    def extract(self):
        return pd.read_csv(self.path)