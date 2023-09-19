import sys
             
from ..pages.base_page import BasePage
from ..config.config import Create_Init_Page,Main_Page_Data,Inside_Initiative_Page,Ideation_Data
import os
from time import sleep


class check_initiative_lanes(BasePage):
    def check_lane_updates(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        sleep(2)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_4")
        self.send_keys(Create_Init_Page.initiative_description,"test4")
        self.click(Create_Init_Page.pick_a_goal_drop)
        self.click(Create_Init_Page.pick_a_goal_first_option)
        self.click(Create_Init_Page.select_owner_field)
        self.click(Create_Init_Page.select_owner_ani)
        self.click(Create_Init_Page.select_contributor)
        self.click(Create_Init_Page.select_contributor_ani)
        self.click(Create_Init_Page.create_btn)
        self.click(Main_Page_Data.home_btn)
        self.hover(Ideation_Data.for_hover_top_goals)
        sleep(1)
        self.click(Create_Init_Page.new_category)
        self.click(Main_Page_Data.for_tc_4)
        self.click(Inside_Initiative_Page.lane_update_drop)
        self.click(Inside_Initiative_Page.lane_update_active)
        self.click(Main_Page_Data.home_btn)
        self.click(Main_Page_Data.active_category_btn)
        sleep(5)
        active_category = self.element_presence(Main_Page_Data.for_tc_4)
        self.click(Main_Page_Data.for_tc_4)
        self.click(Inside_Initiative_Page.lane_update_drop)
        self.click(Inside_Initiative_Page.lane_update_completed)
        self.click(Main_Page_Data.home_btn)
        sleep(2)
        self.click(Main_Page_Data.completed_category_btn)
        completed_category = self.element_presence(Main_Page_Data.for_tc_4)
        sleep(2)
        closed_category = self.element_presence(Main_Page_Data.for_tc_4)
        self.click(Main_Page_Data.for_tc_4)
        self.click(Inside_Initiative_Page.lane_update_drop)
        self.click(Inside_Initiative_Page.lane_update_closed)
        self.click(Main_Page_Data.home_btn)
        self.click(Main_Page_Data.closed_category_btn)
        sleep(2)
        self.hover(Main_Page_Data.for_tc_4)
        self.click(Create_Init_Page.delete_dropdown)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        assert active_category == True, 'Was not switched to active category'
        assert completed_category == True,'Was not switched to completed category'
        assert closed_category == True,'Was not switched to closed category'

    


        
