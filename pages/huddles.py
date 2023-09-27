import sys

from ..config.config import Main_Page_Data,Inside_Initiative_Page,Create_Init_Page,Ideation_Data
from ..pages.base_page import BasePage
import os
from time import sleep

class Check_Huddles(BasePage):
    def check_contributor_in_huddles(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv("EMAIL"))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        sleep(2)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_9")
        self.send_keys(Create_Init_Page.initiative_description,"test9")
        self.click(Create_Init_Page.select_contributor)
        self.click(Create_Init_Page.select_contributor_ani)
        self.click(Create_Init_Page.create_btn)
        self.click(Main_Page_Data.for_tc_9)
        self.click(Inside_Initiative_Page.huddles_category)
        self.click(Inside_Initiative_Page.new_huddle_btn)
        a = self.element_presence(Inside_Initiative_Page.for_test_huddles_people)
        self.click(Main_Page_Data.home_btn)
        self.hover(Ideation_Data.for_hover_top_goals)
        sleep(1)
        self.click(Create_Init_Page.new_category)
        self.hover(Create_Init_Page.for_hover)
        self.click(Create_Init_Page.delete_dropdown)
        sleep(3)
        try:
            self.click(Create_Init_Page.delete_drop_delete_btn)
        except:
            self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        sleep(2)
        assert a == True, 'Wrong contributer in huddles'
