from pickletools import read_unicodestring8
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from collections import defaultdict
info = defaultdict(list)

import time
import datetime
import os

# Primary Setting
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(executable_path=ChromeDriverManager().install())


# data crawling
save_rootpath = 'C:/Users/Gliver/Desktop/tmp'
food_list = ['김치', '비빔밥', '콩나물무침', '치킨', '돈까스', '계란', '오렌지주스', '쌀밥', '우유', '샐러드', '고구마맛탕']
image_num = 10

for food in food_list:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()

    try:
        os.mkdir(f'{save_rootpath}/{food}')
    except:
        pass
    url = f'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={food}'

    driver.get(url)
    time.sleep(1)

    for i in range(image_num // 10):
        driver.execute_script('scrollBy(0, 500)')
        time.sleep(2)
    time.sleep(5)

    elements = driver.find_elements(By.CSS_SELECTOR, '._image')

    num = min(image_num, len(elements))
    for idx, element in enumerate(elements[:num], 1):
        image_src = element.get_attribute('src')
        url = image_src[:image_src.find('&type')]
        
        save_path = f'{save_rootpath}/{food}/img_{idx}.jpg'
        os.system(f"curl  {url}  > {save_path}")

        print(image_src)
        print(f"curl  {url}  > {save_path}")
        print()

    
    print(len(elements))
    driver.close()
    print('Good')
