import sys
 

from ..config.config import Main_Page_Data,Inside_Initiative_Page,Create_Init_Page,Ideation_Data,Analytics
from ..pages.base_page import BasePage
import os
from time import sleep


class Check_Analytics(BasePage):
    def check_top_contributors_and_active_tasks(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv("EMAIL"))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        sleep(2)
        self.click(Main_Page_Data.analytics_category)
        try:
            contributers_count = self.find_text(Analytics.top_contributors_tasks_count)
        except:
            contributers_count = 0 
        self.click(Main_Page_Data.home_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_10")
        self.send_keys(Create_Init_Page.initiative_description,"test10")
        self.click(Create_Init_Page.select_owner_field)
        self.click(Create_Init_Page.select_owner_ani)
        self.click(Create_Init_Page.select_contributor)
        self.click(Create_Init_Page.select_contributor_ani)
        self.click(Create_Init_Page.create_btn)
        self.click(Main_Page_Data.for_tc_10)
        self.click(Inside_Initiative_Page.lane_update_drop)
        self.click(Inside_Initiative_Page.lane_update_active)
        self.click(Inside_Initiative_Page.new_task_btn)
        self.send_keys(Inside_Initiative_Page.task_name_field,'TC_10')
        self.click(Inside_Initiative_Page.task_contributer_drop)
        self.click(Inside_Initiative_Page.select_me_as_contributor)
        self.click(Inside_Initiative_Page.create_task_btn)
        self.click(Inside_Initiative_Page.new_task_btn)
        self.send_keys(Inside_Initiative_Page.task_name_field,'TC_10d')
        self.click(Inside_Initiative_Page.task_contributer_drop)
        self.click(Inside_Initiative_Page.select_me_as_contributor)
        self.click(Inside_Initiative_Page.create_task_btn)
        self.click(Inside_Initiative_Page.task_status_first_drop)
        self.click(Inside_Initiative_Page.task_status_in_progress_first)
        self.click(Inside_Initiative_Page.task_status_second_drop)
        self.click(Inside_Initiative_Page.task_status_in_progress_second)
        sleep(2)
        self.click(Main_Page_Data.analytics_category)
        contributor_name = self.find_text(Analytics.top_contributers_first)
        tasks_count = self.find_text(Analytics.top_contributors_tasks_count)
        self.click(Main_Page_Data.home_btn)
        #self.click(Main_Page_Data.active_category_btn)
        self.click(Main_Page_Data.active_category_btn)
        self.hover(Main_Page_Data.for_tc_10)
        self.click(Create_Init_Page.delete_dropdown)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        sleep(2)
        print(int(tasks_count) - int(contributers_count))
        
        assert contributor_name == 'Ani Bad','wrong contributor name'
        assert int(tasks_count) - int(contributers_count) == 2,'wrong count of active tasks'


    def check_initiatives_count_in_analytics(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv("EMAIL"))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        active_inits_count_before = self.find_text(Analytics.active_init_count)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_15")
        self.send_keys(Create_Init_Page.initiative_description,"test15")
        self.click(Create_Init_Page.create_btn)
        self.click(Main_Page_Data.for_tc_15)
        self.click(Inside_Initiative_Page.lane_update_drop)
        self.click(Inside_Initiative_Page.lane_update_active)
        sleep(1)
        self.click(Main_Page_Data.home_btn)
        sleep(1)
        active_inits_count_after = self.find_text(Analytics.active_init_count)
        print(active_inits_count_after)
        print(active_inits_count_before)
        self.click(Main_Page_Data.active_category_btn)
        self.hover(Main_Page_Data.for_tc_15)
        self.click(Create_Init_Page.delete_dropdown)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        print(sys.path)
        assert int(active_inits_count_after) == int(active_inits_count_before) + 1


    def check_analytics_active_inits_graphic(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv("EMAIL"))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Main_Page_Data.analytics_category)
        
