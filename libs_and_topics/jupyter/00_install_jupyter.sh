
# install
pip3 install jupyterlab notebook
pip3 install jupyter_nbextensions_configurator voila

# start with
jupyter notebook


# get extensions
pip install jupyter_contrib_nbextensions
# jupyter contrib nbextension install --user
pip install jupyter_nbextensions_configurator
# jupyter nbextensions_configurator enable --user
# jupyter notebook --generate-config

# allow remote connections
c.NotebookApp.allow_origin = '*' #allow all origins
c.NotebookApp.ip = '0.0.0.0' # listen on all IPs - risky!
c.NotebookApp.token = ''

# go to app in browser
localhost:8000


# get themes
# not showing icons
pip install jupyterthemes
Then change your theme with
jt -t chesterish

