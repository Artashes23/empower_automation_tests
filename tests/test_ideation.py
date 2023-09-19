import sys

from ..pages.create_ideation import Check_Ideations
from dotenv import load_dotenv
import os


class Test_Ideations(Check_Ideations):
    load_dotenv
    def test_create_delete_ideations_TC_6(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('Url'))
        self.check_create_delete()

    def test_without_switching_valid_error_TC_7(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('Url'))
        self.create_ideation_without_switching_any_switch()

    def test_change_anything_after_publishing_ideation_TC_8(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('Url'))
        self.change_anything_after_publishing_ideation()

    def test_ideation_results_14(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('Url'))
        self.check_ideation_result()
    
    
    
    
