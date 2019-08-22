#!/usr/bin/env python
# coding: utf-8

"""
Data Handler Module


"""

import zipfile

class data_handler:
    def get_header(self, zip_file, data_file: "file name inside zip") -> list:
        """ 
        retrieves the first line of a zipped csv file - the headers
        zip_file : name of the actual zipfile
        data_file: name of the file inside the zipfile 
        """
        with zipfile.ZipFile(zip_file) as myzipfh:
            with myzipfh.open(data_file) as fh:
                header = fh.readline()
                header = header.decode('UTF-8')
                header = header.strip()
        
        col_header = header.split(',')
        return col_header
    
    def generate_create_table_sql(self, headers):
        sql = "CREATE TABLE ( "
        header_string = " text, ".join(headers)
        sql += header_string
        sql += " );"
        return sql

def main():
    dh = data_handler()
    header = dh.get_header('data/loan.csv.zip', 'loan.csv')
    print(header)
    creat_sql = dh.generate_create_table_sql(header)
    print(creat_sql)

if __name__ == "__main__":
    main()