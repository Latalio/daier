# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 09:45:24 2019

@author: Latalio
"""



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

#URL = r'https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.592428dfNjeGCK&id=598811957905'

#【中山】王若琳爱的呼唤巡回演唱会-中山站 
# 时间：2019.09.14 周六 19:30
# URL = r'https://detail.damai.cn/item.htm?id=599170255171'

# 【重庆】暑期剧优惠套票《暗恋桃花源》+《你还弹吉他吗》
# 时间：2019.08.31-09.01
URL = r'https://detail.damai.cn/item.htm?id=598889345344'
USERNAME = "15827008480"
PASSWORD = "la16987623"

driver = webdriver.Chrome()
# 设置等待时间
wait = WebDriverWait(driver, 5)
driver.get(URL)
MINUTES = 30;


def choose(seletor):
    try:
        # 控件可点击时才选定
        choice = wait.until(EC.element_to_be_clickable((By.XPATH, seletor)))
        return choice
    except TimeoutException as e:
        print("Time out!")
        return None
    except Exception:
        print("Not found!")
        return None

#假设不会卡回来
def buy():
    try:
        price = None
        plus = None
        buybtn = None
        submit = None
        booker = None
        driver.get(URL)
        # 场次
        
        # 票档
        while None == price:
            price = choose('//*[@class="select_right_list_item sku_item"][2]')
        price.click()
#         数量
        while None == plus:
            plus = choose('//*[@class="cafe-c-input-number-handler cafe-c-input-number-handler-up"]')
        plus.click()
        # 确认
        while None == buybtn:
            buybtn = choose('//*[@class="buybtn"]')
        driver.execute_script("arguments[0].scrollIntoView();", buybtn) 
        buybtn.click()
        # 选择购票人
#        while None == booker:
#            booker = choose('//*[@id="confirmOrder_1"]/div[2]/div[2]/div[1]/div[2]')
#        driver.execute_script("arguments[0].scrollIntoView();", booker) 
#        booker.click()
        # 提交订单
        while None == submit:
            submit = choose('//*[@id="confirmOrder_1"]/div[9]/button')
        driver.execute_script("arguments[0].scrollIntoView();", submit) 
        submit.click()
    except Exception:
        print("抢票失败，尝试重新抢票")
        buy()
    
    return True

def select():
    try:
        price = None
        plus = None
        buybtn = None
        submit = None
        booker = None
        driver.get(URL)
        # 场次
        
        # 票档
        while None == price:
            price = choose('//*[@class="select_right_list_item"][5]')
        price.click()
        # 数量
#        while None == plus:
#            plus = choose('//*[@class="cafe-c-input-number-handler cafe-c-input-number-handler-up"]')
#        plus.click()
        # 确认
        while None == buybtn:
            buybtn = choose('//*[@class="buybtn"]')
        driver.execute_script("arguments[0].scrollIntoView();", buybtn) 
        buybtn.click()
        # 选择购票人
        while None == booker:
            booker = choose('//*[@id="confirmOrder_1"]/div[2]/div[2]/div[1]/div[2]')
        driver.execute_script("arguments[0].scrollIntoView();", booker) 
        booker.click()
        # 提交订单
        while None == submit:
            submit = choose('//*[@id="confirmOrder_1"]/div[9]/button')
        driver.execute_script("arguments[0].scrollIntoView();", submit) 
        submit.click()
    except Exception:
        print("抢票失败，尝试重新抢票")
        buy()
    
if __name__ == "__main__":
    if input("请输入口令:") == "lala":
        while 1:
            if MINUTES == time.localtime().tm_min:
                print("开始抢票")
                if buy():
                    print("抢票成功")
                    break;

