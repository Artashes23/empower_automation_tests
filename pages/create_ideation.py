import sys

from ..pages.base_page import BasePage
from config.config import Main_Page_Data,Create_Init_Page,Inside_Initiative_Page,Ideation_Data,Analytics
from dotenv import load_dotenv
import os
from time import sleep
from selenium.webdriver.common.keys import Keys


import os

# Get the current working directory (the directory where your Python script is located)
current_directory = os.path.dirname(__file__)

# Specify the relative path to the image file
image_path = os.path.join(current_directory, 'images.png')

# Now, you can use 'image_path' to work with the image file in your code


class Check_Ideations(BasePage):
    load_dotenv()
    def check_create_delete(self):
        logo_path = (image_path)
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        ideas_count_before = self.find_text(Ideation_Data.ideas_count)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_6")
        self.send_keys(Create_Init_Page.initiative_description,"test6")
        self.click(Create_Init_Page.pick_a_goal_drop)
        self.click(Create_Init_Page.pick_a_goal_first_option)
        self.click(Create_Init_Page.select_owner_field)
        self.click(Create_Init_Page.select_owner_ani)
        self.click(Create_Init_Page.select_contributor)
        self.click(Create_Init_Page.select_contributor_ani)
        self.click(Create_Init_Page.create_btn)
        self.click(Main_Page_Data.for_tc_6)
        self.click(Inside_Initiative_Page.ideation_category)
        self.click(Inside_Initiative_Page.new_ideation_btn)
        sleep(2)
        self.clear(Ideation_Data.ideation_title_field)
        self.clear(Ideation_Data.ideation_introduction_field)
        self.send_keys(Ideation_Data.ideation_title_field,"TC_6")
        self.send_keys(Ideation_Data.ideation_introduction_field,"test6")
        #self.click(Ideation_Data.browser_logo)
        self.send_keys(Ideation_Data.logo_input,logo_path)
        self.click(Ideation_Data.crowdsource_switch)
        self.click(Ideation_Data.promoted_idea_switch)
        self.send_keys(Ideation_Data.ideas_1,'idea1')
        self.click(Ideation_Data.first_idea_plus_btn)
        self.send_keys(Ideation_Data.ideas_2,'idea2')
        sleep(2)
        self.click(Ideation_Data.second_idea_btn)
        self.clear(Ideation_Data.ideas_3)
        self.send_keys(Ideation_Data.ideas_3,'idea3')
        self.click(Ideation_Data.comments_switch)
        sleep(2)
        self.send_keys(Main_Page_Data.body,Keys.PAGE_UP)
        self.click(Ideation_Data.draft_publish_drop)
        self.click(Ideation_Data.publish_option)
        sleep(2)
        self.click(Ideation_Data.see_live_btn)
        self.switch_windows(1)
        ideation_inroduction = self.find_text(Ideation_Data.start_page_intro)
        self.click(Ideation_Data.ideation_start_btn)
        sleep(3)
        logo_existence1 = self.element_presence(Ideation_Data.logo_existence)
        self.click(Ideation_Data.add_your_idea_btn)
        self.send_keys(Ideation_Data.add_your_idea_field,"testidea")
        self.click(Ideation_Data.idea_send_btn)
        #self.click(Ideation_Data.select_first_idea)
        #self.click(Ideation_Data.select_second_idea)
        #self.click(Ideation_Data.select_third_idea)
        sleep(1)
        self.click_all_elems(Ideation_Data.ideas)
        ideas_count = self.count_elements(Ideation_Data.ideas)
        self.click(Ideation_Data.ideation_submit_btn)
        logo_existence2 = self.element_presence(Ideation_Data.logo_existence)
        success_message = self.find_text(Ideation_Data.thank_you)
        self.switch_windows(0)
        self.click(Ideation_Data.back_ideation)
        self.click(Main_Page_Data.home_btn)
        self.hover(Ideation_Data.for_hover_top_goals)
        sleep(1)
        self.click(Main_Page_Data.new_category_btn)
        sleep(2)
        
        self.click(Main_Page_Data.for_tc_6)
        self.click(Inside_Initiative_Page.lane_update_drop)
        self.click(Inside_Initiative_Page.lane_update_active)
        self.click(Main_Page_Data.home_btn)
        ideas_count_after = self.find_text(Ideation_Data.ideas_count)
        self.hover(Ideation_Data.for_hover_top_goals)
        self.click(Main_Page_Data.active_category_btn)
        self.send_keys(Main_Page_Data.body,Keys.COMMAND + 'r')
        sleep(2)
        self.hover(Main_Page_Data.for_tc_6)
        self.click(Create_Init_Page.delete_dropdown)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        sleep(2)
        assert ideation_inroduction == 'test6','Wrong ideation title'
        assert logo_existence1 is True,"Logo is not shown in start page"
        assert ideas_count == 4,'incorrect count of ideas'
        assert logo_existence2 is True, "Logo is not shown in start page"
        assert success_message == 'Your votes have been submitted successfully!','Wrong success message'

    def create_ideation_without_switching_any_switch(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_7")
        self.send_keys(Create_Init_Page.initiative_description,"test7")
        self.click(Create_Init_Page.create_btn)
        self.click(Main_Page_Data.for_tc_7)
        self.click(Inside_Initiative_Page.ideation_category)
        self.click(Inside_Initiative_Page.new_ideation_btn)
        self.click(Ideation_Data.draft_publish_drop)
        self.click(Ideation_Data.publish_option)
        sleep(2)
        valid_error = self.find_text(Ideation_Data.without_switch_valid_error)
        
        self.click(Ideation_Data.back_ideation)
        self.click(Main_Page_Data.home_btn)
        self.click(Create_Init_Page.new_category)
        self.hover(Create_Init_Page.for_hover)
        self.click(Create_Init_Page.delete_dropdown)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        sleep(2)
        assert valid_error == 'Please enable at least one of the switches'
    
    def change_anything_after_publishing_ideation(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        sleep(2)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_8")
        self.send_keys(Create_Init_Page.initiative_description,"test8")
        self.click(Create_Init_Page.create_btn)
        self.click(Main_Page_Data.for_tc_8)
        self.click(Inside_Initiative_Page.ideation_category)
        self.click(Inside_Initiative_Page.new_ideation_btn)
        self.click(Ideation_Data.crowdsource_switch)
        sleep(2)
        self.click(Ideation_Data.draft_publish_drop)
        self.click(Ideation_Data.publish_option)
        sleep(1)
        title = self.element_presence(Ideation_Data.ideation_title_disabled)
        description = self.element_presence(Ideation_Data.ideation_description_disabled)
        logo_upload = self.element_presence(Ideation_Data.browser_logo_disabled)
        crowdsource = self.element_presence(Ideation_Data.crowdsource_switch_disabled)
        promoted_ideas = self.element_presence(Ideation_Data.promoted_idea_switch_disabled)
        comments = self.element_presence(Ideation_Data.comments_switch_disabled)
        sleep(1)
        self.click(Ideation_Data.back_ideation)
        self.click(Main_Page_Data.home_btn)
        #self.hover(Ideation_Data.for_hover_top_goals)
        self.hover(Ideation_Data.for_hover_top_goals)
        self.click(Create_Init_Page.new_category)
        self.hover(Create_Init_Page.for_hover)
        self.click(Create_Init_Page.delete_dropdown)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        assert title == True, 'Title field is not disabled'
        assert description == True, 'Description field is not disabled'
        assert crowdsource == True, "Crowdsource switch is not disabled"
        assert logo_upload == True, 'File upload is not disabled'
        assert promoted_ideas ==True, 'Promoted ideas switch is not disabled'
        assert comments ==True, 'Comments switch is not disabled'

    def check_ideation_result(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        sleep(2)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_14")
        self.send_keys(Create_Init_Page.initiative_description,"test14")
        self.click(Create_Init_Page.create_btn)
        self.click(Main_Page_Data.for_tc_14)
        self.click(Inside_Initiative_Page.ideation_category)
        self.click(Inside_Initiative_Page.new_ideation_btn)
        self.click(Ideation_Data.crowdsource_switch)
        self.click(Ideation_Data.comments_switch)
        sleep(2)
        self.click(Ideation_Data.draft_publish_drop)
        self.click(Ideation_Data.publish_option)
        idea_link = self.get_elem_attribute(Ideation_Data.for_idea_url,'value')
        self.click(Ideation_Data.see_live_btn)
        self.switch_windows(1)
        self.click(Ideation_Data.ideation_start_btn)
        self.click(Ideation_Data.add_your_idea_btn)
        self.send_keys(Ideation_Data.add_your_idea_field,"testidea")
        self.click(Ideation_Data.idea_send_btn)
        self.click(Ideation_Data.add_comment_btn)
        self.send_keys(Ideation_Data.comment_field,'test14')
        self.click(Ideation_Data.send_comment_btn)
        self.click(Ideation_Data.ideation_submit_result)
        self.switch_windows(0)
        self.click(Ideation_Data.results_category)
        self.browser.refresh()
        sleep(20)
        participants_count = self.find_text(Ideation_Data.participants_count)
        ideas_count = self.find_text(Ideation_Data.idea_count)
        comments_count = self.find_text(Ideation_Data.comments_count)
        self.click(Ideation_Data.back_ideation)
        self.click(Main_Page_Data.home_btn)
        self.hover(Ideation_Data.for_hover_top_goals)
        self.click(Create_Init_Page.new_category)
        self.hover(Create_Init_Page.for_hover)
        self.click(Create_Init_Page.delete_dropdown)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        
        assert ideas_count == '1','incorrect ideas count'
        assert comments_count == '1','incorrect comments count'
        
        
        
        
        

    
    
        

    

    


        
