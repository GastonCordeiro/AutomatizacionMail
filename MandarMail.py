from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path='/home/administrador/PycharmProjects/test1/DriverFirefox')
driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1578407211&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3db8e7fdd8-9889-7e4c-8c36-d1fda0dbc6e2&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")

usuario = driver.find_element_by_id("i0116")
usuario.send_keys("rambosix@outlook.com.ar")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_id("i0118")
clave.send_keys("robertito1P")
clave.send_keys(Keys.ENTER)
time.sleep(3)

redactar = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button')
time.sleep(2)
redactar.click()
time.sleep(5)

para = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/input')
para.send_keys("lucas_n13@hotmail.com")
time.sleep(3)


asunto = driver.find_element_by_xpath("//*[@id='subjectLine0']")
asunto.send_keys("que lo que")

dice = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div[1]")
dice.send_keys("hola, te llego el mail?")
time.sleep(3)

enviar = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/div[2]/div[1]/button[1]').click()

"""
aceptar = driver.find_element_by_xpath('//*[@id="ok-1"]').click()
"""

