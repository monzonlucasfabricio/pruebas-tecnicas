# Import the Agent class from the agent.py module previously defined.
from agent import Agent
import json
import sys
from collections import OrderedDict

agents = []
ids = []

# New agent to add
agent_6 = { 
            "id": 6,
            "name": "agent_6",
            "version": "4.1.3",
            "os": "ubuntu 22.04",
            "inventory": ["nano", "git", "aws-cli"],
            "modules": {
                "fim": {"status": "enabled", "frequency": 5, "eps": 100},
                "syscollector": {"status": "enabled", "frequency": 10, "eps": 20},
                "rootcheck": {"status": "disabled", "frequency": 20, "eps": 40},
                "winevt": {"status": "disabled", "frequency": 12, "eps": 300},
                "logcollector": {"status": "disabled", "frequency": 5, "eps": 20}
            },
            "status": "active"
        }       

class Agent(Agent):

    # Create a method to load the agents data from the data.json file.
    def load_data(self,idn,filename = ''):
        if filename != '':
            try:
                with open(filename,'r') as f:
                    data = json.load(f)
                    for row in data:
                        if row['id'] == int(idn):
                            self.__load_data(row)
            except Exception as e:
                print(e)
        else:
            print("No jsonfile")

    def __load_data(self,data):
        for key in self.keys:
            setattr(self,str(key),data[str(key)])

    # Create a method to write the agents data to an external json file.
    def export(self,filename = '', opt = 'w'):
        tmp = {}
        for key in self.keys:
            tmp[key] = getattr(self,key)

        if filename != '' and opt == 'w':
            jsondata = json.dumps(OrderedDict(tmp),sort_keys=True, indent=2)
            with open(filename,opt) as outfile:
                outfile.write(jsondata)
        else:
            return OrderedDict(tmp)
                    

def set_agents_data(inputfile,ids):
    for idn in ids:
        new = Agent()
        new.load_data(idn,inputfile)
        agents.append(new)

def output_agents_data(outputfile = ''):
    jsonlist = []
    if outputfile != '' and len(agents) != 0:
        for agent in agents:
            dictret = agent.export(opt = 'a') # 'a' for append 
            jsonlist.append(dictret)
        jsondata = json.dumps(jsonlist, sort_keys=True, indent=4)
        with open(outputfile,'w') as outfile:
            outfile.write(jsondata)

def print_all_agents():
    if len(agents) != 0:
        for agent in agents:
            agent.print_attrs()

# Create a main function to do the following:
# - Read all agent information from data.json.
# - Add a new agent to the list (you can choose the attribute values you want).
# - Print all agents information (6 items).
# - Export the agents information (6 items) to an external json file called output.json .
def main(idn = None):
    ids = []
    if idn != None:
        ids = [idn]
        # - Read all agent information from data.json.
        set_agents_data('data.json',ids)
    else:
        ids = list(range(1,6))
        # - Read all agent information from data.json.
        set_agents_data('data.json',ids)

        # - Add a new agent to the list (you can choose the attribute values you want).
        newagent = Agent()
        for attr in newagent.keys:
            setattr(newagent,attr,agent_6[attr])
        agents.append(newagent)
        ids.append(newagent.id)
    
    # - Print all agents information (6 items).
    print_all_agents()

    # - Export the agents information (6 items) to an external json file called output.json.
    output_agents_data('output.json')


if __name__=="__main__":
    if len(sys.argv) > 1:
        try:
            idn = int(sys.argv[1])
            if idn in range(1,6):
                main(sys.argv[1])
        except:
            print('Parameter = {} , not valid as INT'.format(sys.argv[1]))
    else:
        main()
        
