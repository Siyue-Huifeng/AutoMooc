# coding: utf-8
# python 3.12.3
# @Author: siyue_huifeng
# @Time: 2024/12/9

import json

import lxml
import bs4
import re

from bs4.element import Tag


class Utils():
    
    @staticmethod
    def hex_xor(s, xor_str):
        decrypted = ""
        for i in range(0, len(s), 2):
            char1 = int(s[i:i + 2], 16)
            char2 = int(xor_str[i:i + 2], 16)
            xored = hex(char1 ^ char2)[2:]
            if len(xored) == 1:
                xored = "0" + xored
            decrypted += xored
        return decrypted

    @staticmethod
    def unbox(s):
        _map = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13, 6, 11, 39, 18, 20, 8, 14, 21, 32, 26,
                2, 30, 7, 4, 17, 5, 3, 28, 34, 37, 12, 36]
        unboxed = [''] * len(_map)
        for i, char in enumerate(s):
            for j in range(len(_map)):
                if _map[j] == i + 1:
                    unboxed[j] = char
        return ''.join(unboxed)

    @staticmethod
    def get_acw_sc__v2(script_str):
        encrypt_key = "3000176000856006061501533003690027800375"
        pattern = r"(?<=arg1\=')[^']+(?=';)"
        findall = re.findall(pattern, script_str)
        encrypted_id = findall[0]

        decrypted_id = Utils.unbox(encrypted_id)
        decrypted_value = Utils.hex_xor(decrypted_id, encrypt_key)
        return decrypted_value

    @staticmethod
    def format_json(resp_json) -> dict:
        return json.dumps(resp_json, indent=4, ensure_ascii=False)

class HtmlParser:

    @staticmethod
    def get_menu_root(html : str) -> Tag:
        soup = bs4.BeautifulSoup(html, "html.parser")
        div = soup.find("div", class_ = "s_learnlist")
        return div

    @staticmethod
    def get_chapter(html : str) -> list[Tag]:
        soup = bs4.BeautifulSoup(html, "html.parser")
        all_chapter_div = soup.find_all("div", class_="s_chapter chapter_new")
        return all_chapter_div

    @staticmethod
    def get_sectionlist(html : str) -> list[Tag]:
        soup = bs4.BeautifulSoup(html, "html.parser")
        all_sectionlist = soup.find_all("div", class_="s_sectionlist")
        return all_sectionlist
    
    @staticmethod
    def get_section_title(html : str) -> list[Tag]:
        soup = bs4.BeautifulSoup(html, "html.parser")
        all_section = soup.find_all("div", class_="s_section chapter_new")
        return all_section
    
    @staticmethod
    def get_section_content(html : str) -> list[Tag]:
        soup = bs4.BeautifulSoup(html, "html.parser")
        all_section_content = soup.find_all("div", class_="s_sectionwrap")
        return all_section_content
    
    @staticmethod
    def get_section_type(html : str) -> str:
        soup = bs4.BeautifulSoup(html, "html.parser")
        type_div = soup.find("div", class_="s_pointti")
        return type_div["title"]
    
    @staticmethod
    def is_section_done(html : str) -> bool:
        if "item_done_icon item_done_pos done_icon_show" in html:
            return True
        return False

    @staticmethod
    def get_courses(html : str) -> list[Tag]:
        soup = bs4.BeautifulSoup(html, "html.parser")
        courses = soup.find_all("div", class_="s_point")
        return courses
    
    @staticmethod
    def get_course_title(html : str) -> str:
        soup = bs4.BeautifulSoup(html, "html.parser")
        title = soup.find("div", class_="s_pointti")
        try:
            return title['title']
        except:
            return title.text.strip()

    @staticmethod
    def get_course_type(html : str) -> str:
        soup = bs4.BeautifulSoup(html, "html.parser")
        type_div = soup.find("div", class_="s_pointti")
        return type_div["title"]

    @staticmethod
    def get_course_id(html : str) -> str:
        soup = bs4.BeautifulSoup(html, "html.parser")
        course_id = soup.find("div", class_="s_point")
        return course_id["id"].replace("s_point_", "")
    
    @staticmethod
    def get_current_site_id(html: str):
        ...
    
    @staticmethod
    def get_current_main_id(html: str):
        ...

    @staticmethod
    def get_current_course_id(html: str):
        ...
    
    @staticmethod
    def get_current_item_id(html: str):
        ...