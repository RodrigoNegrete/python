# Install on Ubuntu 24.04


## Install Python Latest
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3
sudo apt install python3.10
python3 --version
```


## Install Pip
```
sudo apt install -y python3-pip
pip3 --version
```


## Install Multiple Python Versions
```
sudo apt install python[version]
```

Run the following update-alternatives commands to enable multiple versions in your Python binary /usr/bin/ location. Replace python3.12 with your active Python version and python3.9 with the newly installed version.
Version 3.12.3 is the latest at installation time
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2
```

View all available Python versions you can switch between on your server.
```
sudo update-alternatives --config python3
```

Output:
```
  Selection    Path                 Priority   Status
------------------------------------------------------------
* 0            /usr/bin/python3.10    2         auto mode
  1            /usr/bin/python3.10    2         manual mode
  2            /usr/bin/python3.12    1         manual mode
```
Press <enter> to keep the current choice[*], or type selection number: 
Enter your desired Python version to activate in your server environment and press Enter to apply changes. When working with virtual environments, the selected version is only activated in your environment.


## Create Virtual Environments
```
sudo apt install -y python3-virtualenv
virtualenv newenv
source newenv/bin/activate
deactivate
```
