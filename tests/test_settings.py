import sys

from ..pages.settings import check_settings_page
from dotenv import load_dotenv
import os

class Test_Settings(check_settings_page):
    load_dotenv
    def test_goal_add_delete_TC_5(self,setup):
        self.browser = setup
        self.browser.get(os.getenv("URL"))
        self.check_settings_add_delete_goal()


    def test_language_switching(self,setup):
        self.browser = setup
        self.browser.get(os.getenv("URL"))
        self.check_langauge_switching()

    #def test_delete_1(self,setup):
        #self.browser = setup
        #self.browser.get(os.getenv("URL"))
        #self.delete()
