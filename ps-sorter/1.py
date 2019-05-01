from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
import csv

csv_file = open('PS1.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['station','accom'])

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.get('http://psd.bits-pilani.ac.in/Login.aspx')
driver.find_element_by_xpath("""//*[@id="TxtEmail"]""").send_keys("f20170344@hyderabad.bits-pilani.ac.in")
driver.find_element_by_xpath("""//*[@id="txtPass"]""").send_keys("21E652U1")
driver.find_element_by_xpath("""//*[@id="login-box"]/div/div[1]/fieldset/div[2]/label/input""").click()
driver.find_element_by_xpath("""//*[@id="Button1"]""").click()
driver.get("http://psd.bits-pilani.ac.in/Student/StudentStationPreference.aspx")
for i in range(313,347):
	pointer="""//*[@id="sortable_nav"]/li[{}]""".format(i)
	element=driver.find_element_by_xpath(pointer).text
	csv_writer.writerow([element,"0"])
# table.find_element_by_
# for(i=1;i<=312.i++):
	
# driver.get("http://10.2.102.21:9000/psp/hcsprod/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_SWAP.GBL?FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_ENROLLMENT.HC_SSR_SSENRL_SWAP&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder")
# driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ptifrmtgtframe"]"""))
# element1 = driver.find_element_by_name("DERIVED_REGFRM1_DESCR50$37$")
# drp1 = Select(element1)
# drp1.select_by_visible_text("GS F221: BUSINESS COMMUNICATION")
# driver.find_element_by_xpath("""//*[@id="DERIVED_REGFRM1_SSR_PB_SRCH$41$"]""").click()
# time.sleep(1)
# driver.find_element_by_name("CLASS_SRCH_WRK2_SUBJECT$64$")
# driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SUBJECT$64$"]/option[6]""").click()
# time.sleep(0.3)
# driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_CATALOG_NBR$72$"]""").send_keys("F385")
# driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH"]""").click()
# time.sleep(1)
# try:
# 	elem = driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SSR_PB_SELECT$0"]""")
# 	if elem.is_displayed():
# 		elem.click() # this will click the element if it is there
# 		print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
# 		time.sleep(1)
# 		driver.find_element_by_xpath("""//*[@id="DERIVED_CLS_DTL_NEXT_PB$75$"]""").click()
# 		time.sleep(1)
# 		driver.find_element_by_xpath("""//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]""").click()
# 		x = 1
# except NoSuchElementException:
#     driver.close()