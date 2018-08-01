#!/usr/bin/python3

from pandas import read_excel
import sqlite3
import sys
import numpy as np

tableName = 'Sheet1'

def getUsage():
    return "ExcelToSql -i excel_file -o sql_file"

def printUsage():
    print(getUsage())

def checkUsage(argv):
    if len(argv) is not 5:
        printUsage()
        exit(-1);
    for i in [1, 3]:
        option = argv[i].capitalize()
        if option == '-i':
            excelFilename = argv[2];

            if not ( excelFilename.endswith('.xls') or excelFilename.endswith('.xlsx') ):
                exit(-1);

        elif option == '-o':
            sqliteDBFilename = argv[4];

            if not ( sqliteDBFilename.endswith('.sql') or sqliteDBFilename.endswith('.sqlite') ):
                print("Error sqlite filename")
                exit(-1);

    return (excelFilename, sqliteDBFilename)

def main():
    excelFilename, sqliteDBFilename = checkUsage(sys.argv);

    xlsFile = read_excel(excelFilename, tableName)

    columns = xlsFile.columns

    db = sqlite3.connect(sqliteDBFilename)
    cursor = db.cursor()

    #cursor.execute("DELETE FROM " + tableName)

    Ncolumns = len(columns)
    Nrows = len(xlsFile)

    query = "INSERT INTO " + tableName + " (id, name, cost) VALUES('{id}', '{name}', '{cost}')"

    for i in range(1, Nrows):
        record = xlsFile.loc[i]
        q = query
        for column in columns:
            data = record[column]
            if type(data) == np.int64:
                data = str(data)
            q = q.replace('{' + column +'}', data )
        cursor.execute(q)

    db.commit()
    db.close()
    print('Done')

if __name__ == '__main__':
    main()

