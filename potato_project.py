from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()

# browser.implicitly_wait(10) # 해당 데이터가 뜰 때까지 10초 동안 기다리고, 10초 이전에 나오면 바로 계속 진행
# browser.get("https://www.naver.com")

# 네이버에서 식품 눌러주기
# browser.find_element('xpath', '//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[5]/a').click()

# # 식품에 채소 눌러주기
# browser.find_element('xpath', '//*[@id="content"]/div/div[1]/div/div[1]/div/div/div[1]/ul/li[7]/button').click() # 식품 클릭
# browser.find_element('xpath', '//*[@id="content"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]/a').click() # 채소 클릭

# # 검색하기
# engine = browser.find_element('xpath', '//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/form/fieldset/div[1]/input') # 검색창
# engine.click()
# engine.send_keys("고구마") # 검색엔진에 입력하고 싶은 키워드 입력
# engine.send_keys(Keys.ENTER) # 검색엔진의 엔터를 눌러줘서 검색을 가능하게 해준다.

# # 리뷰 많은 순 클릭해주기
# browser.find_element('xpath', '//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]/a[4]').click() # 리뷰 많은 순 클릭

# 데이터 가져오기
names =[]
prices = []
review_cnts = []
links = []

for i in range(1,2):
    browser.implicitly_wait(10)
    url = browser.get(f"https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EA%B3%A0%EA%B5%AC%EB%A7%88&pagingIndex={i}&pagingSize=40&productSet=total&query=%EA%B3%A0%EA%B5%AC%EB%A7%88&sort=review&timestamp=&viewType=list")

    while True:
        bh = browser.execute_script("return document.body.scrollHeight") # 브라우저 상의 처음 높이
        print(bh)
        time.sleep(4)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 스크롤 내리기
        time.sleep(2)
        ah = browser.execute_script("return document.body.scrollHeight")
        if ah == bh:
            break
    
    infos = browser.find_elements(By.CLASS_NAME, "basicList_info_area__TWvzp")
    for info in infos:
        try:
            name = info.find_element(By.CLASS_NAME, "basicList_link__JLQJf")
            price = info.find_element(By.CLASS_NAME, "price_num__S2p_v").text
            review_cnt = info.find_element(By.CLASS_NAME, "basicList_num__sfz3h").text
            link = info.find_element(By.CLASS_NAME, "basicList_link__JLQJf").get_attribute("href")
            names.append(name.text)
            prices.append(price)
            review_cnts.append(review_cnt)
            links.append(link)
        except:
            print("Exeption")
            
df = pd.DataFrame({'name':names, 'price':prices, 'review_cnt':review_cnts, 'link':links})
print(df)


# 브라우저 창 유지
# while True:
#     pass