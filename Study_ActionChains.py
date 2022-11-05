'''
Author: Thrand Thrand@126.com
Date: 2022-11-05 22:59:06
LastEditors: Thrand Thrand@126.com
LastEditTime: 2022-11-05 23:05:32
FilePath: \01 MyFirstSelenium\Study_ActionChains.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# https://blog.csdn.net/qq_18671415/article/details/109059476

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

print('========= 开始执行测试 ==========')
# 导入驱动
driver = webdriver.Chrome()
print('========= 成功导入驱动 ==========')

# 加载网页
driver.get('https://blog.csdn.net/qq_18671415/article/details/109059476')
print('========= 成功加载网页 ==========')

# 查找元素控件，输入框需要点击一下才能出现搜索历史
# 使用ActionChains类来进行鼠标操作
# （1）找到输入框
# （2）点击输入框
# （3）在搜索历史里找到任意一条搜索内容

# （1）导包后，调用ActionChains类，然后将驱动传入
actions = ActionChains(driver)
print('========= 成功调用ActionChains类 ==========')
# （2）找到控件，并将控件作为参数传入模拟鼠标移动到控件上的方法move_to_element
inputs = driver.find_element(By.XPATH, "//input[@id='toolbar-search-input']")
print('========= 成功找到控件 ==========')
actions.move_to_element(inputs)
# (3) 提交存储行为
actions.perform()
print('========= 成功提交存储行为 ==========')

# 缺少cookies 导致无法记录登录状态 没有搜素历史，明日添加上cookies后验证代码
# # 找到清除历史按钮
# btn_clear = driver.find_element(
#     By.XPATH, "//span[@class='toolbar-search-clear']")
# print('========= 成功找到清除历史按钮 ==========')
# # 点击清除历史按钮
# actions.click(btn_clear)
# actions.perform()
