# complete method to create environment

## install python
install from packages on website


## install latest pip
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3.10

## install virtualenv
pip install virtualenv

## create environment
-> on windows
python -m venv C:\path\env_name
or
cd to folder
python -m venv venv
-> example
python -m venv E:\OneDrive\python\envs\tensorflow

-> on linux
python -m venv /path/name

## Activate the virtual environment 
### on windows
cd \env_name\Scripts
activate.bat
-> example
cd ..
E:
cd E:\OneDrive\python\envs\tensorflow\Scripts
activate.bat
-> Powershell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
cd E:\OneDrive\python\envs\tensorflow\Scripts
.\Activate

### on mac and linux
source /path/env_name/bin/activate  


## deactivate
deactivate # from environment folder

## remove
remove all files from directory

# pipenv
pip install pipenv
cd to app folder
pipenv install package_name # creates environment and installs package
pipenv --venv # shows where the environment is
pipenv shell # activates the environment
exit # deactivates de environment


## install pip
cd to python installation folder
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
py get-pip.py

## to create environment with specific python version
C:\Users\Rodrigo\AppData\Local\Programs\Python\Python39-32\Scripts\pip.exe install virtualenv
C:\Users\Rodrigo\AppData\Local\Programs\Python\Python39-32\python.exe -m venv e:\OneDrive\Documents\GitHub\notes\python\libs_and_topics\finance\part_time_larry\binance_tutorials\venv
cd e:\OneDrive\Documents\GitHub\notes\python\libs_and_topics\finance\part_time_larry\binance_tutorials\venv\scripts
.\Activate
switch vscode to new venv

# virtual environments in vs code runner
pipenv --env_name # gives the location of the environment
-> in the environment directory inside bin there´s a python interpreter
-> go to settings in vs code and find code-runner.executor.Map
-> create a new map before the existing one by entering "code-runner.executor.Map"
-> this creates a json config for the code-runner
-> change the value for the python variable to the identified path
-> select python interpreter through cpommand prompt or at the bottom left status bar
-> if you can´t see it create a new setting on the settings json like "python.pythonPath": "environments path" -> restart vs code -> select from command prompt or statusbar

# show virtual environments on jupyter notebooks
go to 00_0_install_jupyter_notebooks.md


# ERROR - .\Activate  cannot be loaded because running scripts is disabled on this system.
To enable running scripts in current power shell:
```
Set-ExecutionPolicy Unrestricted -Scope Process
```

