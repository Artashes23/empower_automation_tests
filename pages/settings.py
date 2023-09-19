import sys

from ..pages.base_page import BasePage
from ..config.config import Settings_Page,Main_Page_Data,Create_Init_Page
from dotenv import load_dotenv
import os
from time import sleep
class check_settings_page(BasePage):
    load_dotenv()
    def check_settings_add_delete_goal(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Settings_Page.settings_category_btn)
        self.click(Settings_Page.goals_category)
        self.send_keys(Settings_Page.goals_name_field,"TC_5")
        self.click(Settings_Page.goals_plus_btn)
        self.click(Main_Page_Data.home_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.click(Create_Init_Page.pick_a_goal_drop)
        matched_element = self.find_text(Create_Init_Page.pick_a_goal_first_option)
        self.click(Create_Init_Page.initiative_back_btn)
        self.click(Settings_Page.settings_category_btn)
        self.click(Settings_Page.goals_category)
        self.click(Settings_Page.goal_delete_drop)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        print(matched_element)
        assert 'TC_5' == matched_element, 'incorrect first goal'

    def check_langauge_switching(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Settings_Page.settings_category_btn)
        self.click(Settings_Page.change_to_spanish)
        self.click(Main_Page_Data.home_btn)
        new_init_spanish = self.find_text(Main_Page_Data.new_initiative_btn)
        new_category_spanish = self.find_text(Settings_Page.new_category_text)
        self.click(Settings_Page.settings_category_btn)
        self.click(Settings_Page.change_to_german)
        self.click(Main_Page_Data.home_btn)
        new_init_german = self.find_text(Main_Page_Data.new_initiative_btn)
        new_category_german = self.find_text(Settings_Page.new_category_text)
        self.click(Settings_Page.settings_category_btn)
        self.click(Settings_Page.change_to_english)
        sleep(1)
        assert new_init_spanish == 'Nueva Iniciativa','Incorrect translation'
        assert new_category_spanish == 'Nuevo','Incorrect translation'
        assert new_init_german == 'Neue Initiative','Incorrect translation'
        assert new_category_german == 'Neu','Incorrect translation'
    
    def delete(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Main_Page_Data.active_category_btn)
        for i in range(112):
            self.hover(Create_Init_Page.for_hover)
            self.click(Create_Init_Page.delete_dropdown)
            self.click(Create_Init_Page.delete_drop_delete_btn)
            self.click(Create_Init_Page.confirm_btn)
            i+= 0

        