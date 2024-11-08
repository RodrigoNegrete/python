# install 
pip install ipython
pip install ipykernel
 
# install for vscode
install python extension
select interpreter
install jupyter extension

# show virtual environments on jupyter notebooks
Go to menu File → Preferences → Settings.
Click on Workspace settings.
Under Files:Association, in the JSON: Schemas section, you will find Edit in settings.json. Click on that.
Update "python.pythonPath": "Your_venv_path/bin/python" under workspace settings. (For Windows): Update "python.pythonPath": "Your_venv_path/Scripts/python.exe" under workspace settings.
Save workspace
Restart Visual Studio Code in case if it still doesn't show your venv.