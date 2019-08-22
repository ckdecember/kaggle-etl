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
        keywords = ["desc"]
        sql = "CREATE TABLE loan_data ( "

        # check for keywords

        tmp_headers = [] 
        for h in headers:
            if h in keywords:
                tmp_headers.append("\"" + h + "\"")
            else:
                tmp_headers.append(h)

        headers = tmp_headers
        header_string = " text, ".join(headers)
        sql += header_string
        sql += " text"
        sql += " );"

        return sql

def main():
    dh = data_handler()
    header = dh.get_header('data/loan.csv.zip', 'loan.csv')
    creat_sql = dh.generate_create_table_sql(header)
    print(creat_sql)

if __name__ == "__main__":
    main()