# UI471
Automated UI tests for challenge by Intel471

IDE used:
PyCharm 2022.3.2 (Professional Edition)

Dependencies:
Go to PyCharm terminal and run the following command:
pip install -r requirements.txt

Playwright v1.31.1
PyCharm Preferences --> Python Interpreter --> [+] Install Package --> Playwright

Pytest v7.2.2
Pytest Reporter Tool v0.8.2

Install browsers images for Playwright from the PyCharm terminal with the following command:
playwright install

Executing tests file:
Open project in PyCharm
Right click on file tests_add_2products.py

For executing tests with report:
Go to PyCharm terminal and run the following command:
pytest --template=html1/index.html --report=report.html
