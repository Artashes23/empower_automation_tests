import sys
sys.path.append("..")
import os
from pages.tasks import Check_Tasks

class Test_Tasks(Check_Tasks):
    
    def test_create_tasks_TC_11(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('URL'))
        self.check_create_task()
        
    def test_task_without_name_TC_12(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('URL'))
        self.check_create_task_without_name()

    def test_task_edit_TC_13(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('URL'))
        self.check_tasks_edit()

    def test_task_due_complete_interval(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('URL'))
        self.check_due_complete_interval()

    
    

    