## Task 1

Q&A:
1) Where are located the alerts generated in the wazuh-manager?
- The alerts in the wazuh-manager are located on var/ossec/logs/alerts/alerts.json
2) How did you add the wazuh-agent to the wazuh-manager?
- I added wazuh-agent using the dathboard and following the steps:
    1) Wazuh-dashboard → Agents → Deploy new agent.
    2) Chose operating system, server address, group.
    3) Copied the command generated and pasted on a wazuh-agent instance.

3) The flow starts on the wazuh-agent that is installed on an endpoint. The agent foward security data to the central server called wazuh-server. The server decodes and analyzes the information and passes the result to the wazuh-indexer for indexing and storage. Once the data is indexed the wazuh-dashboard is used to mine and visualize the data.

4) I had two main problems:
    1) Using vagrant with virtual box without changing the hostname in the server and the agent, there
was a problem adding an agent using the same hostname. That I could see looking at the logs on ossec.log, so I fixed it changing the hostname.
    2) I had an error when creating the certificates at the beginning. It was a typo error.

```bash
$ var/ossec/bin/agent_control -l
```
<p align='center'>
<img src="/task1/image1.png" alt="image1" width="500"/>
</p>


<p align='center'>
<img src="/task1/image2.png" alt="image2" width="350"/>
</p>
<p align='center'>
Screenshot of Wasuh-agent interface on Windows
</p>


<p align='center'>
<img src="/task1/image3.png" alt="image3" width="550"/>
</p>
<p align='center'>
Screenshot of alerts generated on wazuh-dashboard
</p>

The chosen alert on the screenshot can be seen on the file : [alert.json](/task1/alert.json)


## Task 2

- Files:
    - [Evil Decoder](/task2/evil_decoder.xml)
    - [Rules](/task2/local_rules.xml)


<p align='center'>
Screenshot of wazuh-logtest result
</p>
<p align='center'>
<img src="/task2/image1.png" alt="image1" width="500"/>
</p>

## Task 3

To execute the script call the following command
```bash
cd task3 && python script.py
```
or if you want to output only one agent data
```bash
cd task3 && python script.py <agent-number>
```

- Files:
    - [agent.py](/task3/agent.py)
    - [script.py](/task3/script.py)
    - [output.json](/task3/output.json)
    - [output_2.json](/task3/output_2.json)


## Task 4

Q&A
1) How would you parameterize tests?
- To parametrize a test you can use a decorator called *pytest.mark.parametrize* that helps to pass arguments to the test function to be evaluated in the test later. Also you can use *metafunc.parametrize* which helps passing parameters when collecting a test suite.

2) What are fixtures used for? What is the importance of their scopes?
- Fixtures are to provide a fixed baseline so that tests execute realiably and produce consistent,repeatable, results. They can initialize services, states or operating environments at the beginning of tests. Fixtures are requested on tests by adding as a parameter. Also they give the ability to define a generic setup that can be reused on every test.
- The important of the scope is that you can set when is the fixture created and destroyed in a test suite. There are 5 different scopes: function, class, module, package, session. For example: you want to create just one connection to a server for all the test suite that you are running and you don't want to make in every test, so you can use **_scope_='session'** on the fixture.

3) The example test using parameterization and fixture will be the same as the **Task 5**


## Task 5
#### Test 1
**1)** Create test(s) to verify that the content of the input files has the expected value.
```python
test = {'1.txt': 'a', '2.txt': 'b', '3.txt': 'c', '4.txt':'d', '5.txt': 'e'}
```
- To choose which file you want to test, use ***--files*** fixture.
- Example : ***--files=1,2,3***

```bash
cd task5 && python -m pytest -vls --html=tests/test1/report.html tests/test1/test1.py
```

Without using fixtures
<p align='center'>
<img src="/task5/tests/test1/image1.png" alt="image1" width="600" height="200"/>
</p>

With fixtures, passing *--files=1,2* parameter
<p align='center'>
<img src="/task5/tests/test1/image2.png" alt="image1" width="600" height="200"/>
</p>

[HTML report](/task5/tests/test1/report.html)



#### Test 2
**2)** Read the clients.db database file and create test(s) that check the following:
- Its field structure is as follows: ```[‘id’, ‘name’, ‘country’, ‘age’]```.
- The age field of each record is greater than 5.
- There is no null value in a record.

```bash
cd task5 && python -m pytest -vls --html=tests/test2/report.html tests/test2/test2.py
```

**Results**

<p align='center'>
<img src="/task5/tests/test2/image1.png" alt="image1" width="600" height="150"/>
</p>


[HTML report](/task5/tests/test2/report.html)





