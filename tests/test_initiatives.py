import sys

from ..pages.create_delete_initiative import Check_Create_Init
import dotenv
from dotenv import load_dotenv
import os


class Test_Create_Delete_Init(Check_Create_Init):
    load_dotenv()

    
    def test_create_delete_init_TC_1(self,setup):
        self.browser = setup
        self.browser.get(os.getenv("URL"))
        self.check_create_delete()

    def test_create_init_without_title_TC_2(self,setup):
        self.browser = setup
        self.browser.get(os.getenv("URL"))
        self.check_create_init_without_title()



    

    

    
        
    
    
    

    

    
    

