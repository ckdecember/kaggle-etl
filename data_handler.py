#!/usr/bin/env python
# coding: utf-8

"""
Data Handler Module

manages data, retrieving headers from loan data files,
dynamically generate sql statements

"""

import zipfile

import pandas
import psycopg2
import xlrd

class data_handler:
    def get_zipheader(self, zip_file, data_file: "file name inside zip") -> list:
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
    
    def get_excelheader(self, excel_file, sheet_name=None):
        if sheet_name:
            df = pandas.read_excel(excel_file, sheet_name=sheet_name)
        else:
            df = pandas.read_excel(excel_file)
        #df.columns
        return df.columns
    
    def generate_create_table_sql(self, headers, reserved_keywords) -> str:
        """
        given csv headers and reserved name keywords, generate a create table sql string
        """
        sql = "CREATE TABLE loan_data ( \n"
        tmp_headers = [] 
        for h in headers:
            if h in reserved_keywords:
                tmp_headers.append("\t\"" + h + "\"")
            else:
                tmp_headers.append("\t" + h)

        headers = tmp_headers
        header_string = " text, \n".join(headers)
        sql += header_string
        sql += " text\n"
        sql += " );"

        return sql

    def execute_query(self):
        pass

def main():
    reserved_keywords = ["desc"]

    dh = data_handler()
    header = dh.get_zipheader('data/loan.csv.zip', 'loan.csv')
    creat_sql = dh.generate_create_table_sql(header, reserved_keywords)
    print(creat_sql)
    excel_header = dh.get_excelheader('data/LCDataDictionary.xlsx')
    arr = excel_header.array

if __name__ == "__main__":
    main()