import json
from collections import OrderedDict
OK = 0
ERROR = -1


class Agent:

    # Define the constructor and attributes of the class Agent (according to the data.json items).
    def __init__(self,filename = 'data.json'):
        self.create_attrs(filename)

    def create_attrs(self,filename = ''):
        if filename != '':
            ret = self.__get_key_attr(filename)
            if ret == 0:
                for key in self.keys:
                    setattr(self,'{}'.format(key),'')
            else:
                print("Couldn't set attributes")
        else:
            print("No jsonfile")
    
    def __get_key_attr(self,filename):
        self.keys = []
        try:
            with open(filename,'r') as f:
                data = json.load(f, object_pairs_hook=OrderedDict)
                for key in data[0]:
                    self.keys.append(key)
            return OK
        except Exception as e:
            print(e)
            return ERROR

    # Create a method to show all the attributes of the agent on the screen.
    def print_attrs(self):
        print('\n\n')
        if self.keys != []:
            for key in self.keys:
                print("{} : {}".format(key,json.dumps(getattr(self,'{}'.format(key)),sort_keys=False, indent=4)))