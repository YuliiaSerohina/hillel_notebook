from notebook.usefull.constants import NOTEBOOK_FIELDS
import csv
import os
from pathlib import Path


class FileManager:
    def __init__(self, file_name='notebook.csv'):
        self.file_path = Path(__file__).parents[1] / 'files' / file_name
        if not os.path.exists(self.file_path):
            self.create_new_file()

    def create_new_file(self, rows=None):
        with open(self.file_path, mode='w') as csv_file:
            field_name = list(NOTEBOOK_FIELDS.keys())
            writer = csv.DictWriter(csv_file, fieldnames=field_name)
            writer.writeheader()
            if rows is not None:
                for row in rows:
                    writer.writerow(row)

    def read_file(self):
        rows = []
        with open(self.file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                rows.append(row)
            return rows

    def write_file(self, row):
        with open(self.file_path, mode='a') as csv_file:
            field_name = list(NOTEBOOK_FIELDS.keys())
            writer = csv.DictWriter(csv_file, fieldnames=field_name)
            writer.writerow(row)


