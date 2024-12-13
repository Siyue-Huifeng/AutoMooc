# coding: utf-8
# python 3.12.3
# @Author: siyue_huifeng
# @Time: 2024/12/9

import json

import lxml
import bs4

class Utils:

    @staticmethod
    def format_json(resp_json) -> dict:
        return json.dumps(resp_json, indent=4, ensure_ascii=False)

class HtmlParser:

    @staticmethod
    def get_menu_root(html : str) -> bs4.element.Tag:
        soup = bs4.BeautifulSoup(html, "html.parser")
        div = soup.find("div", class_ = "s_learnlist")
        return div

    @staticmethod
    def get_chapter(html : str) -> list[bs4.element.Tag]:
        soup = bs4.BeautifulSoup(html, "html.parser")
        all_chapter_div = soup.find_all("div", class_="s_chapter chapter_new")
        return all_chapter_div

    @staticmethod
    def get_sectionlist(html : str) -> list[bs4.element.Tag]:
        soup = bs4.BeautifulSoup(html, "html.parser")
        all_sectionlist = soup.find_all("div", class_="s_sectionlist")
        return all_sectionlist
    
    @staticmethod
    def get_section_title(html : str) -> list[bs4.element.Tag]:
        soup = bs4.BeautifulSoup(html, "html.parser")
        all_section = soup.find_all("div", class_="s_section chapter_new")
        return all_section
    
    @staticmethod
    def get_section_content(html : str) -> list[bs4.element.Tag]:
        soup = bs4.BeautifulSoup(html, "html.parser")
        all_section_content = soup.find_all("div", class_="s_sectionwrap")
        return all_section_content
    
    @staticmethod
    def get_section_type(html : str) -> str:
        soup = bs4.BeautifulSoup(html, "html.parser")
        type_div = soup.find("div", class_="s_pointti")
        return type_div["title"]