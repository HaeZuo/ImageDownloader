from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
import urllib.request 
import os

import os.path
from os import path

# CrawlImages
def crawlImages(search, count, saveurl):
    # Chrome Driver Path
    service = Service(executable_path=r'/tf/_test/chromedriver')

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=service, options=options)

    # Google Image page
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl") 
    elem = driver.find_element(By.NAME, "q") 
    elem.send_keys(search)

    elem.send_keys(Keys.RETURN)

    # Scroll down
    SCROLL_PAUSE_TIME = 1 
    last_height = driver.execute_script("return document.body.scrollHeight") 

    while True:  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        # Page Loading Wait
        time.sleep(SCROLL_PAUSE_TIME) 
        new_height = driver.execute_script("return document.body.scrollHeight") 
        if new_height == last_height: 
            try: 
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click() 
            except: 
                break 
        last_height = new_height

    # Image Search and Download
    #images = driver.find_element(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    images = driver.find_elements(By.CSS_SELECTOR, ".YQ4gaf")

    now_count = 0
    i = 0

    while True:
        try: 
            images[i].click() # Image Click
            time.sleep(1)

            #imgUrl = driver.find_element(By.CSS_SELECTOR, ".n3VNCb").get_attribute("src")
            imgUrl = driver.find_element(By.CSS_SELECTOR, ".iPVvYb").get_attribute("src")
            print(imgUrl)
            if ".jpg" in imgUrl:
                now_count += 1
                urllib.request.urlretrieve(imgUrl, saveurl + str(now_count) + ".jpg") # Image Download

        except:
            pass

        if now_count == count:
            break

        i += 1
    driver.close()

searchs = [
#   ["Search words", <count>, "Save Path"],
    ["파인애플", 100, "/tf/workspace/training_newmit/images/total/10. Pineapple/"], 
    ["코코넛", 100, "/tf/workspace/training_newmit/images/total/11. Coconut/"], 
    ["레몬", 100, "/tf/workspace/training_newmit/images/total/12. Lemon/"], 
    ["과일 배", 100, "/tf/workspace/training_newmit/images/total/13. Pear/"], 
    ["멜론", 100, "/tf/workspace/training_newmit/images/total/14. Melon/"], 
    ["파프리카", 100, "/tf/workspace/training_newmit/images/total/15. Paprika/"], 
    ["망고", 100, "/tf/workspace/training_newmit/images/total/16. Mango/"], 
    ["체리", 100, "/tf/workspace/training_newmit/images/total/17. Cherry/"], 
    ["블루베리", 100, "/tf/workspace/training_newmit/images/total/18. Blueberry/"], 
    ["파파야", 100, "/tf/workspace/training_newmit/images/total/19. Papaya/"], 
    ["복숭아", 100, "/tf/workspace/training_newmit/images/total/20. Peach/"], 
    ["수박", 100, "/tf/workspace/training_newmit/images/total/21. Watermelon/"], 
    ["라즈베리", 100, "/tf/workspace/training_newmit/images/total/22. Raspberry/"], 
    ["딸기", 100, "/tf/workspace/training_newmit/images/total/23. Strawberry/"], 
    ["토마토", 100, "/tf/workspace/training_newmit/images/total/24. Tomato/"], 
    ["참외", 100, "/tf/workspace/training_newmit/images/total/25. Chamoe/"], 
    ["크랜베리", 100, "/tf/workspace/training_newmit/images/total/26. Cranberry/"], 
    ["감", 100, "/tf/workspace/training_newmit/images/total/27. Persimmon/"]
]

for search in searchs:
    if not path.exists(search[2]):
        os.mkdir(search[2])
    crawlImages(search[0], search[1], search[2])
