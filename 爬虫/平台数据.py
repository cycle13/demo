from selenium import webdriver
import requests

session = requests.Session()
first_url = 'http://10.41.100.77:8081/hnhb/login.html'

browser = webdriver.Chrome()
browser.get(first_url)