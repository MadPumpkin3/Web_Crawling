from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()

browser.implicitly_wait(10) # 해당 데이터가 뜰 때까지 10초 동안 기다리고, 10초 이전에 나오면 바로 계속 진행
browser.get("https://www.naver.com")