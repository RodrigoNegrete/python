from selenium import webdriver
import time
import shutil

# Optional argument, if not specified will search path
# driver = webdriver.Chrome('/path/to/chromedriver')

# open browser
browser = webdriver.Chrome()

# read url
browser.get(
    'https://infosen.senado.gob.mx/formatos_INAI-INFOSEN/index.php?c=votaciones&a=data')

# read dropdown
# dropdown = browser.find_element_by_name('dataTableVotaciones_length')

# click dropdown item
click_500 = browser.find_element_by_xpath(
    '/html/body/div[2]/div[2]/div/div[2]/div[2]/div/label/select/option[6]').click()

# sort descending
click_csv = browser.find_element_by_xpath(
    '//*[@id="dataTableVotaciones"]/thead/tr/th[2]').click()

# wait for browser to reload
time.sleep(10)

# click csv button
click_csv = browser.find_element_by_xpath(
    '//*[@id="dataTableVotaciones_wrapper"]/div[1]/div[1]/div/button[3]').click()

# wait for bfile to download
time.sleep(10)

# move file to working dir
shutil.move("D:\OneDrive\Downloads\Listas de Votaciones nominales en el Pleno..csv",
            "D:\OneDrive\Documents\GitHub\Listas.csv")
