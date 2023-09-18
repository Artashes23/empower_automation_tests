import sys
sys.path.append("..")
from pages.huddles import Check_Huddles
import os


class Test_Huddles(Check_Huddles):
    def test_contributer_in_huddles_TC_9(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('URL'))
        self.check_contributor_in_huddles()