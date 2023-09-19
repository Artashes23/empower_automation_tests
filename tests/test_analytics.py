import sys

from ..pages.analytics import Check_Analytics

from dotenv import load_dotenv
import os
from pages.tasks import Tasks
import pytest




class Test_Analytics(Check_Analytics):
    #@pytest.mark.skip(reason="Not finished")
    def test_top_contributors_and_tasks_TC_10(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('URL'))
        self.check_top_contributors_and_active_tasks()

    def test_initiatives_count_in_analytics_TC_15(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('URL'))
        self.check_initiatives_count_in_analytics()



    def test_analytics_active_tasks_graphic(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('URL'))
        
        
        

    

