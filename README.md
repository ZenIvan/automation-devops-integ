# ZenRooms QA Automation 

Automate testing for API and WEBAPPS using [python](https://www.python.org/). 

Powered by [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) and [Pytest](https://docs.pytest.org/en/stable/)! 

* SeleniumBase is an all-in-one framework for web automation, end-to-end testing, presentations, charts, and website tours. Tests are run with "pytest". Browsers are controlled by WebDriver.

* Pytest is a python based test framework that makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

# Getting Started

## Pre-requisites

1. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. Setup [SSH keys](https://jdblischak.github.io/2014-09-18-chicago/novice/git/05-sshkeys.html) for Github
3. Clone the project files to your local machine
   ```
   git clone git@github.com:zenrooms/zenrooms-qa-automation.git
   ```
4. Install IDE of choice- [VSCode](https://code.visualstudio.com/) or [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC) is recommended

## Install Python 
[<img src="https://img.shields.io/pypi/pyversions/seleniumbase.svg?color=22AAEE" alt="Python:2.7|3.5|3.6|3.7|3.8" />](https://www.python.org/downloads/)

**Preferred version is 3.7 and above**

### Windows

1. Download and install python. 
2. Setup the system environment variables for python. 

Location of `python.exe` and scripts

```
Default path: 
C:\Users\(user name)\AppData\Local\Programs\Python\PythonXX 

C:\Users\(user name)\AppData\Local\Programs\Python\PythonXX\Scripts)
```
3. Navigate to the environment variable menu and add the python path.
   *  Go to Control Panel -> System and Security -> System (or Win key + Pause/Break)
   *  Click the Advanced system settings on the left sidebar 
   *  Click Environment Variables button on the bottom-right corner
   *  Find the Path vairable on the System variables list (2nd list)
   *  Double click it
   *  Click New on the right sidebar
   *  It will add blank field on the list
   *  Paste the directory of the python.exe `(Default path: C:\Users \ (user name)\AppData\Local\Programs\Python\PythonXX)`
   *  Click New again
   *  Paste the Scripts path `(Default path: C:\Users \ (user name)\AppData\Local\Programs\Python\PythonXX\Scripts)`
4. Open CMD and check if python is installed.
   ```
   python3 --version
   ```

### Mac OSX

1. Install [homebrew](https://brew.sh/).
    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```
2. Install python.
   ```
   brew install python3
   ```
3. Setup the system environment variables for python.
   * Open terminal
   * Edit `.bash_profile` file or `.zshrc`
   * Add this line `export PATH=/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/sbin:${PATH}`
   * Save and exit
4. Open terminal and check if python is installed.
   ```
   python3 --version
   ```

## Install Pip

Pip is the package manager for Python. It is already installed along with python but upgrading it to prevent warnings.
```
python -m pip install -U pip
```

## Setup Virtual Environment

1. Open CMD/Terminal
2. Install virtual environment
   ```
   pip install virtualenv
   ```
3. Go to the root of the test directory
   ```
   cd zenrooms-qa-automation
   ```
4. Activate the virtual environment
   ```
   cd /venv/Scripts
   activate
   ```
To deactivate a virtual environment input `deactivate` on command line.


## Install SeleniumBase

Enter the command line below on the CLI on your machine (CMD/Terminal) to install SeleniumBase.

```
pip install seleniumbase
```
* Add ``--upgrade`` OR ``-U`` to upgrade an installation.
* Add ``--force-reinstall`` to also upgrade dependencies. 

Install Chromedriver

```
seleniumbase install chromedriver latest
```

To install other browser drivers, use the commands below.
```bash
seleniumbase install chromedriver
seleniumbase install geckodriver
seleniumbase install edgedriver
seleniumbase install iedriver
seleniumbase install operadriver
```

## Setup on Pycharm

1. Install Pycharm for either [PC](https://www.jetbrains.com/pycharm/download/#section=windows) or [Mac](https://www.jetbrains.com/pycharm/download/#section=mac)

2. Open Pycharm and open the directory for the cloned repository

3. Add an interpreter by going to *File -> Settings/Preferences* (Press Ctrl + Alt + S for windows)

4. Open Project: zenrooms-automation-qa -> Python Interpreter

5. Click the gear icon on the upper right side of the section

6. Click Add.. on the gear icon's menu

7. Select New environment (if not selected by default)

8. Select the `Location` path outside of the project folder (zenrooms-automation-qa)

9. Set the `Base Interpreter` as your machine's local `python.exe` file (if you installed the microsoft store version of python you can select the path on the dropdown list)

10. The checkboxes `Inherit global site-packages` and `Make available to all projects` are optional

11. Click Ok button

12. Wait for the virtual environment setup

13. After the setup has finished, open `requirements.txt`

14. Wait for the install option to appear and install all dependencies (Update the dependencies, if necessary)

15. Click the `Terminal` tab below pycharm, along the `git`, `TODO`, `Problems`, etc.

16. Test the seleniumbase installation by a `demo_test` run, type the script below per line:
```
cd /demo_tests
pytest my_first_test.py
```

# Running tests

The great thing about SeleniumBase is that it runs on ``pytest`` and can be run on any CLI command interface. Therefore it can be ran locally and on servers.

For now, run locally as the CI/CD will be setup soon.

### Run API tests
```
cd /api_tests
pytest api_test.py
```

### Run a demo test that comes with SeleniumBase
```
cd /demo_tests
pytest my_first_test.py
```
### Run Pricing Model Tests
```
cd /pricing_model_tests
pytest test_login.py
```
### Run all Zenrooms Tests
```
pytest zenrooms_tests
```
Tests run on chrome by default, this is a default setting.

### Run the tests in demo mode

Demo mode runs the test while highlighting the items that are validated/verified, this will run slowly than the normal run (Keep that in mind when making tests and applying implicit waits).

```
pytest my_first_test.py --demo
```
### Run the tests on other browsers

It can run tests on other browsers by adding the command ``--browser=<browser name>``.
Example:
```
pytest test_suite.py --browser=chrome

pytest test_suite.py --browser=firefox
```
It can use the following browser names for different browsers as well: ``opera`` , ``ie`` , ``edge``.

# Creating tests
Writing tests is easy as boiler plates and samples are provided.

1. Create a new file
2. Copy existing test
3. Edit the test
4. Save and run

### Test design guidelines
* Encourage OOP principles
* Follow the page object design pattern
* Follow the page actions design pattern
* Do asserts in the test not in page objects or page actions
* For data driven tests, use parameterize feature
* Store data in a separate file or folder if possible
* Keep sensitive data secure
* Organize functions, classes, files and folders that make categorical sense
* Write comments
* Write docstrings
* Include the PR and JIRA ticket in the docstrings or comments
* Readability counts! think like the end user

## Coding standards
As a python project its encouraged to use `PEP-8` standards and naming conventions.

## Version control
* Use simple branching pattern from master
* PR should include 3-5 commits for easy review
* Minimum of 1 PR approver
* Admin will merge the branch
* Tagging and version will be used on major releases

## Contributors
Feel free to ask us on slack!

* **Mark Ivan Berbenzana** @ZenIvan- QA Engineer and Repository Admin
* **Karlo Abapo** @kvabapo- Lead QA Engineer

## Acknowledgments & References

* [Michael Mintz](https://github.com/mdmintz)- Creator of SeleniumBase
* [SeleniumBase](https://github.com/seleniumbase/SeleniumBase)- Ask questions on [gitter](https://gitter.im/seleniumbase/SeleniumBase)
* [Pytest](https://docs.pytest.org/en/stable/)
