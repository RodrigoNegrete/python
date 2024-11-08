
# How to Setup Selenium with ChromeDriver on Ubuntu 18.04 & 16.04

sudo apt-get update
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
sudo apt-get install default-jdk 
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
sudo wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
sudo wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar
sudo wget http://www.java2s.com/Code/JarDownload/testng/testng-6.8.7.jar.zip
sudo unzip testng-6.8.7.jar.zip





# start chrome driver
xvfb-run java -D webdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone.jar

# start chrome driver headless
chromedriver --url-base=/wd/hub

# install from pip
sudo apt install selenium python-chromedriver-binary

# check links
sudo webdrivermanager firefox chrome --linkpath /usr/local/bin
sudo webdrivermanager firefox --linkpath /usr/local/bin
sudo webdrivermanager chrome --linkpath /usr/local/bin