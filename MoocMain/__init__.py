# coding: utf-8
# python 3.12.3
# @Author: siyue_huifeng
# @Time: 2024/12/8

import requests
import time
import os

import toml
from bs4.element import Tag

from .Log import log
from .Tools import HtmlParser
from .Tools import Utils

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "mooc_api.toml")
mooc_api_url = toml.load(config_path)

class AutoMoocMain:

    session = requests.Session()
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36" }
    session.headers.update(headers)
    token = ""

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.token = self.login()

    def login(self) -> str:
        login_api = mooc_api_url["login"]
        data_json = {
            "userName": self.username,
            "password": self.password,
            "type": 1
        }

        try:
            resp = self.session.post(url = login_api, json = data_json)
            resp_json = resp.json()
            log.debug({f"登录信息: {Utils.format_json(resp_json)}"})
        except Exception as e:
            log.error(f"登录失败，正在重试...{e}")
            time.sleep(2)
            return self.login()

        if resp.status_code and resp_json['code'] == 200:
            log.info(f"登录成功! 用户: {self.username}")
            return resp_json['data']['token']
        else:
            log.error(f"登录失败! 用户: {self.username}, msg: {resp_json['msg']}")
            log.info("程序已退出...")
            os._exit(0)

    def load_courses(self) -> dict:
        self.session.get(f"https://mooc.icve.com.cn/?token=${self.token}")
        courses_api = mooc_api_url['courses']
        params = f"token={self.token}&siteCode=zhzj&curPage=1&pageSize=9999&selectType=1"

        try:
            resp = self.session.post(url = courses_api, params = params)
            resp_json = resp.json()
            log.debug(f"课程信息: {Utils.format_json(resp_json)}")
        except Exception as e:
            log.error("获取课程列表失败，正在重试...", e)
            time.sleep(2)
            return self.load_courses()
        
        if resp_json is None or 'data' not in resp_json:
            log.warn("获取课程列表失败或课程列表为空")
            log.info("程序已退出...")
            os._exit(0)
        return resp_json

    def sign_learn(self, course_id) -> None:
        join_course_api = mooc_api_url["join_course"]
        param = {
            "courseId": course_id,
            "checkType": 1,
            "sign": 0,
            "template": "blue"
        }

        try:
            self.session.post(url = join_course_api, params=param)
            resp = self.session.post(url = join_course_api, params=param)
            resp_json = resp.json()
            log.debug(f"课程列表信息 {Utils.format_json(resp_json)}")
            self.get_course_index(resp_json['data'])
        except Exception as e:
            log.error(f"加入课程失败，正在重试... {e}")
            time.sleep(2)
            return self.sign_learn(course_id)

    def get_course_index(self, url) -> None:
        try:
            course_response = self.session.get(url = url)
            log.debug(f"课程目录响应信息: {course_response.text}")
        except Exception as e:
            log.error(f"获取课程目录失败，正在重试... {e}")
            time.sleep(2)
            return self.get_course_index(url)


    def get_course_html(self, course_id) -> str:
        param = {
            "params.courseId": course_id
        }
        courseware_api = mooc_api_url["courseware"]
        try:
            resp = self.session.get(url = courseware_api, params = param)
            # log.debug(resp.text)
            return resp.text
        except Exception as e:
            log.error(f"获取课程学习列表失败，正在重试... {e}")
            time.sleep(2)
            return self.get_course_html(course_id)

    def run(self) -> None:
        mooc_course_items = self.load_courses()
        for course_item in mooc_course_items['data']:
            log.debug(Utils.format_json(course_item))
            log.info(f"检索到课程: {course_item[0]}, 时期: {course_item[1]}, 教师: {course_item[15]}")
            course_id = course_item[6]
            self.sign_learn(course_id)
            course_html_page = self.get_course_html(course_id)

            learn_menu_root = HtmlParser.get_menu_root(course_html_page)
            chapters = HtmlParser.get_chapter(str(learn_menu_root))
            sections_list = HtmlParser.get_sectionlist(str(learn_menu_root))
            chapter_index = 0
            for chapter, sections in zip(chapters, sections_list):
                log.info(f"学习章节> 第{chapter_index}章: {chapter['title']}")
                chapter_index += 1
                section_index = 0
                for sections in sections_list:
                    
                    for section in sections:
                        ...