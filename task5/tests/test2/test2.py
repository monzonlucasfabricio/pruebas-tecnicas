from email import header
import pytest
import sys
import os
import sqlite3

headers = ['id', 'name', 'country', 'age']

class test2Suite:

    # This is a demostration for Task 4 - item 3
    @pytest.mark.parametrize('headerlist',[headers])
    def test_field_names(self,headerlist):
        print('\n')
        # Get dbpath
        print("Test init")
        cwd = os.getcwd()
        dbpath = cwd + '/tests/test2/' + 'clients.db'

        # Connect to database
        print("Connect to dbase")
        con = sqlite3.connect(dbpath)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM CLIENTS")
        
        # Its field structure is as follows : ['id', 'name', 'country', 'age'].
        field_names = [i[0] for i in cursor.description]
        print("Check {} == {}".format(field_names,headerlist))
        assert field_names == headerlist,"Fields structure {}".format(field_names)

    def test_age(self):

        print('\n')
        # Get dbpath
        print("Test init")
        cwd = os.getcwd()
        dbpath = cwd + '/tests/test2/' + 'clients.db'

        # Connect to database
        print("Connect to dbase")
        con = sqlite3.connect(dbpath)
        cursor = con.cursor()

        # The age field of each record is greater than 5.
        cursor.execute("SELECT age FROM CLIENTS")
        data = cursor.fetchall()
        for row in data:
            print("Check {} > {}".format(row[0],5))
            assert row[0] > 5
    
    def test_null_value(self):

        print('\n')
        # Get dbpath
        print("Test init")
        cwd = os.getcwd()
        dbpath = cwd + '/tests/test2/' + 'clients.db'

        # Connect to database
        print("Connect to dbase")
        con = sqlite3.connect(dbpath)
        cursor = con.cursor()

        # There is no null value in a record.
        cursor.execute("SELECT * FROM CLIENTS")
        data = cursor.fetchall()
        for row in data:
            for col in row:
                print("Check {} != {}".format(col,None))
                assert None != col," {} != {} ".format(None,col)
