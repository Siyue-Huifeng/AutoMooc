# coding: utf-8
# python 3.12.3
# @Author: siyue_huifeng
# @Time: 2024/12/8

import toml

from MoocMain.Log import log
from MoocMain import AutoMoocMain


try:
    config = toml.load("config.toml")
except FileNotFoundError:
    ...

username = config["username"]
password = config["password"]

if __name__ == "__main__":
    user1 = AutoMoocMain(username, password)
    user1.run()