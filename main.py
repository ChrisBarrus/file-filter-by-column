'''
Read csv file using csv package
'''

import csv
from pathlib import Path
import sys

def read_file(fn):
    p = Path(fn)

    if not p.exists():
        print(f"Provide proper file name. File: {p.name} can not be processed.")
        return False
    
    with open(file=p.name, mode="r", encoding="utf-8") as file_handle:
        rows = csv.DictReader(file_handle)
        
        for row in rows:
            print(row)
        
        return True

def main():
    file_name = 'test-file.csv'

    if read_file(file_name):
        print("Operation done successfuly.")
    else:
        print("Operation failed.")

if __name__ == '__main__':
    args = sys.argv
    params = []
    
    for arg in args:
        param = arg.split("=")
        if( len(param) == 2 ):
            params.append(param)
    
    main(params)