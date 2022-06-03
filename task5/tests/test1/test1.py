import pytest
import sys
import os
import sqlite3

test1 = {'1.txt': 'a', '2.txt': 'b', '3.txt': 'c', '4.txt':'d', '5.txt': 'e'}

class test1Suite:

    def test_1(self,files):
        print('\n')
        print("Test init")
        print("Files to be tested : {}".format(files))
        filenames = files.split(',')
        cwd = os.getcwd()
        for name in filenames:
            val = name + '.txt'
            name = cwd + '/tests/test1/' + val
            with open(name,'r') as f:
                reader = f.readlines()
                print("{} == {}".format(reader[0].strip('\n'),test1[val]))
                assert reader[0].strip('\n') == test1[val], "Value in file : {}, should be {}".format(reader[0].strip('\n'),test1[val])
