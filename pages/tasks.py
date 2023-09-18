import sys
sys.path.append("..")
from pages.base_page import BasePage
from config.config import Main_Page_Data,Create_Init_Page,Inside_Initiative_Page,Ideation_Data,Analytics,Tasks
import os
from time import sleep 
import datetime



class Check_Tasks(BasePage):
    def check_create_task(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_11")
        self.send_keys(Create_Init_Page.initiative_description,"test11")
        self.click(Create_Init_Page.select_owner_field)
        self.click(Create_Init_Page.select_owner_ani)
        self.click(Create_Init_Page.select_contributor)
        self.click(Create_Init_Page.select_contributor_ani)
        self.click(Create_Init_Page.create_btn)
        self.click(Main_Page_Data.for_tc_11)
        self.click(Inside_Initiative_Page.new_task_btn)
        self.send_keys(Tasks.task_name_field,"TC_11")
        self.send_keys(Tasks.task_description_field,'test11')
        self.click(Tasks.select_owner_drop)
        self.click(Tasks.select_owner_me)
        self.click(Tasks.task_create_btn)
        name = self.find_text(Tasks.task_name_check)
        a = self.get_elem_attribute(Tasks.for_owner_check,'data-tip')
        self.click(Main_Page_Data.home_btn)
        self.click(Create_Init_Page.new_category)
        self.hover(Create_Init_Page.for_hover)
        self.click(Create_Init_Page.delete_dropdown)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        sleep(2)
        print(a)
        assert a == "ani.bad@everse-soft.com",'wrong owner name'
        
    
    def check_create_task_without_name(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_12")
        self.send_keys(Create_Init_Page.initiative_description,"test12")
        self.click(Create_Init_Page.create_btn)
        self.click(Main_Page_Data.for_tc_12)
        self.click(Inside_Initiative_Page.new_task_btn)
        self.click(Tasks.task_create_btn)
        valid_error = self.find_text(Tasks.name_valid_error)
        self.click(Tasks.modal_close)
        self.click(Main_Page_Data.home_btn)
        self.click(Create_Init_Page.new_category)
        self.hover(Create_Init_Page.for_hover)
        self.click(Create_Init_Page.delete_dropdown)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        assert valid_error == "Name is required"
    
    def check_tasks_edit(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_13")
        self.send_keys(Create_Init_Page.initiative_description,"test13")
        self.click(Create_Init_Page.select_owner_field)
        self.click(Create_Init_Page.select_owner_ani)
        self.click(Create_Init_Page.select_contributor)
        self.click(Create_Init_Page.select_contributor_ani)
        self.click(Create_Init_Page.create_btn)
        self.click(Main_Page_Data.for_tc_13)
        self.click(Inside_Initiative_Page.new_task_btn)
        self.send_keys(Tasks.task_name_field,"TC_13")
        self.send_keys(Tasks.task_description_field,'test13')
        self.click(Tasks.task_create_btn)
        self.click(Tasks.for_hover)
        self.click(Tasks.tasks_edit_btn)
        self.click(Tasks.select_owner_drop)
        self.click(Tasks.select_owner_me)
        self.click(Tasks.task_create_btn)
        owner_namee = self.get_elem_attribute(Tasks.for_owner_check,'data-tip')
        self.click(Main_Page_Data.home_btn)
        self.click(Create_Init_Page.new_category)
        self.hover(Create_Init_Page.for_hover)
        self.click(Create_Init_Page.delete_dropdown)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        sleep(2)
        print(owner_namee)
        assert owner_namee == 'ani.bad@everse-soft.com', 'wrong owner name'
        


    def check_due_complete_interval(self):
        d_today = datetime.date.today()
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_16")
        self.send_keys(Create_Init_Page.initiative_description,"test16")
        self.click(Create_Init_Page.select_owner_field)
        self.click(Create_Init_Page.select_owner_ani)
        self.click(Create_Init_Page.select_contributor)
        self.click(Create_Init_Page.select_contributor_ani)
        self.click(Create_Init_Page.create_btn)
        
        self.click(Main_Page_Data.for_tc_16)
        self.click(Inside_Initiative_Page.new_task_btn)
        self.send_keys(Tasks.task_name_field,"TC_16")
        self.send_keys(Tasks.task_description_field,'test16')
        self.click(Tasks.task_due_date)
        due_date = int(self.find_text(Tasks.task_due_date))
        self.click(Inside_Initiative_Page.create_task_btn)
        sleep(10)
        self.click(Tasks.select_task_status)
        sleep(15)
        self.click(Tasks.select_status_completed)
        interval =  int(self.find_text(Tasks.interval)[:1])
        today = int(d_today.day)
        sleep(6)
        self.click(Main_Page_Data.home_btn)
        self.click(Create_Init_Page.new_category)
        self.hover(Create_Init_Page.for_hover)
        self.click(Create_Init_Page.delete_dropdown)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        sleep(2)
        print(due_date)
        print(interval)
        print(today)
        assert abs(due_date - today) == interval, 'Incorrect interval'

    
                
        
        


        
        
        
        

        
        
        
        