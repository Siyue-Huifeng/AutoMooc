# coding: utf-8
# python 3.12.3
# @Author: siyue_huifeng
# @Time: 2024/12/9

import json

import lxml
import bs4
import re

from bs4.element import Tag

class Utils:

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
        course_id = soup.find("div", class_="s_pointti")
        return course_id["data-id"]