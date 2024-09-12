# -*- coding:utf-8 -*-
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
import time
import json
import re
from datetime import datetime, timedelta
from time import sleep
from util import load_config
import socket
from hashlib import sha1
import hashlib


class WebConfig(object):
    def __init__(self):
        self.config = load_config()
        self.option = webdriver.ChromeOptions()
        self.option.add_argument(
            r"user-data-dir=C:\Users\Zhouyuan\AppData\Local\Google\Chrome for Testing\User Data")  # 浏览器路径

        # 指定Chrome和ChromeDriver的路径
        self.chrome_path = self.config['chrome']
        self.chrome_driver_path = self.config['chrome_driver']
        self.situation = self.config['situations']
        self.option.binary_location = self.chrome_path
        

        # 使用Service指定ChromeDriver的路径
        self.service = Service(self.chrome_driver_path)


    def get_data(self):
        """初始化WebDriver并获取cookies"""
        option = webdriver.ChromeOptions()
        option.add_argument(
            r"user-data-dir=C:\Users\Zhouyuan\AppData\Local\Google\Chrome for Testing\User Data")  # 浏览器路径

        # 指定Chrome和ChromeDriver的路径
        chrome_path = self.config['chrome']
        chrome_driver_path = self.config['chrome_driver']
        option.binary_location = chrome_path

        # 使用Service指定ChromeDriver的路径
        service = Service(chrome_driver_path)

        # 初始化driver
        driver = webdriver.Chrome(service=service, options=option)
        driver.get(self.config['target_url'])
        sleep(5)  # 等待页面加载



    def run(self):
        self.get_data()


if __name__ == '__main__':
    fps = WebConfig()
    # 初始化driver
    driver = webdriver.Chrome(service=fps.service, options=fps.option)
    sleep(5)
