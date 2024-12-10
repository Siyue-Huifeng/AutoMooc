# coding: utf-8
# python 3.12.3
# @Author: siyue_huifeng
# @Time: 2024/12/9

import json

import lxml
import bs4

class Utils:

    @staticmethod
    def format_json(resp_json):
        return json.dumps(resp_json, indent=4, ensure_ascii=False)

class HtmlParser:

    @staticmethod
    def get_learn_menu_root(html, type: int = 0) -> bs4.element.Tag:
        if type == 0:
            soup = bs4.BeautifulSoup(html, "html.parser")
            div = soup.find("div", id="learnMenu")
            return div
        else:
            lxml


    @staticmethod
    def get_learn_title_name(html, type: int = 0):
        if type == 0:
            soup = bs4.BeautifulSoup(html, "html.parser")
            all_chapter_div = soup.find_all("div", class_="s_chapter chapter_new")
            return [x["title"] for x in all_chapter_div]
        else:
            lxml

