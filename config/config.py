from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
import time
import random
import string


def randEmail(chars = string.ascii_uppercase + string.digits, N=10):
	return  ''.join(random.choice(chars) + "@gmail.com")

def randPswd(chars = string.ascii_uppercase + string.digits, N=10):
	return  ''.join(random.choice(chars))

class Main_Page_Data():
    new_initiative_btn = (By.XPATH,"//button[@class = 'qp-button initiative-tab-container-button big-btn']")
    new_category_btn = (By.XPATH,"//div[@id = 'new']")
    active_category_btn = (By.XPATH,"//div[@id = 'active']")
    completed_category_btn = (By.XPATH,"//div[@id = 'completed']")
    closed_category_btn = (By.XPATH,"//div[@id = 'closed']")
    create_new_custom_initiative = (By.XPATH,"//li[@class = 'init-templates-modal--initiatives-block--li init-templates-modal--initiatives-block--li-new-init']")
    email_field = (By.XPATH,"//input[@id = 'EmailAddress']")
    pswd_field = (By.XPATH,"//input[@id = 'Password']")
    login_btn = (By.XPATH,"//form[@name = 'LoginForm']//button[@class = 'qp-btn primary-cta btn-loader']")
    home_btn = (By.XPATH,'//a[@href="/initiatives/Active"]')
    for_tc_4 = (By.XPATH,"//div[text() = 'TC_4']/parent::div")
    for_tc_6 = (By.XPATH,"//div[text() = 'test6']")
    for_tc_7 = (By.XPATH,"//div[text() = 'TC_7']")
    for_tc_8 = (By.XPATH,"//div[text() = 'TC_8']")
    for_tc_9 = (By.XPATH,"//div[text() = 'TC_9']")
    for_tc_10 = (By.XPATH,"//div[text() = 'TC_10']")
    for_tc_11 = (By.XPATH,"//div[text() = 'TC_11']")
    for_tc_13 = (By.XPATH,"//div[text() = 'TC_13']")
    for_tc_14 = (By.XPATH,"//div[text() = 'TC_14']")
    for_tc_12 = (By.XPATH,"//div[text() = 'TC_12']")
    for_tc_15 = (By.XPATH,"//div[text() = 'TC_15']")
    for_tc_16 = (By.XPATH,"//div[text() = 'TC_16']")
    for_gmail_login = (By.XPATH,"r'https://accounts.google.com/signin/v2/identifier?continue='+\
    'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
    '&flowName=GlifWebSignIn&flowEntry = ServiceLogin'")
    body = (By.XPATH,'//body')
    confirm_btn_popup = (By.XPATH,"//button[@id = 'confirm-confirm']")
    analytics_category = (By.XPATH,"//a[@href='/analytics']")
    first_initiative = (By.XPATH,"//div[@class = 'lane-page']/div[1]")
    
    
    

class Create_Init_Page():
    initiative_title = (By.XPATH,"//input[@name = 'name']")
    initiative_description = (By.XPATH,"//textarea[@name = 'description']")
    pick_a_goal_drop = (By.ID,"goal-dropdown")
    pick_a_goal_first_option = (By.XPATH,"//div[@id = 'goal-dropdown']/div[2]/div[1]")
    pick_a_goal_all_options = (By.XPATH,"//span[@id = 'goal-dropdown']/parent::div/following-sibling::div/div")
    select_owner_field = (By.XPATH,'//input[@placeholder="Select owner"]')
    select_owner_ani = (By.XPATH,"//div[@class = 'scrollable-select-content']/p[text() = 'Ani Bad']")
    select_contributor = (By.XPATH,"//input[@placeholder = 'Select contributor']")
    select_contributor_ani = (By.XPATH,"//input[@name = 'Ani Bad']")
    create_btn = (By.XPATH,"//div[@class = 'base-header-page']/div[2]/button")
    TC_1_title_for_checking = (By.XPATH,"//div[@class = 'lane-page']/div[1]/div/div/div[3]/div[1]")
    TC_1_description_for_check = (By.XPATH,"//div[@class = 'lane-page']/div[1]/div/div/div[3]/div[2]")
    delete_dropdown = (By.XPATH,"//div[@class = 'popover-open-icon']")
    delete_drop_delete_btn = (By.XPATH,"//span[text() = 'Delete']")
    confirm_btn = (By.ID,'confirm-confirm')
    for_hover = (By.XPATH,"//div[@class = 'lane-page']/div[1]/div//div[@class = 'initiative-card--content']")
    initiative_title_valid_error = (By.XPATH,"//input[@name = 'name']/parent::div/label")
    initiative_description_valid_error = (By.XPATH,"//div[@role = 'status']")
    initiative_back_btn = (By.XPATH,"//div[@class = 'base-header-page--go-back']/*[1]")
    new_category = (By.XPATH,"//div[@class='initiatives-wrapper--navbar']/div/div/div[3]/span[2]")
    huddles_category = (By.XPATH,"//span[@id='huddles']")
    select_my_user_contributer = (By.XPATH,"//label[text() = 'artashes.badalyan.999+outerloop@gmail.com']")

class Inside_Initiative_Page():
    lane_update_drop = (By.XPATH,"//div[@class = 'initiative-info--status']")
    lane_update_active = (By.XPATH,"//div[@id = 'active']/span")
    lane_update_completed = (By.XPATH,"//div[@id = 'completed']")
    lane_update_closed = (By.XPATH,"//div[@id = 'closed']")
    ideation_category = (By.XPATH,"//div[@id = 'ideation']")
    new_ideation_btn = (By.XPATH,"//button[@id = 'create-ideation']")
    huddles_category = (By.XPATH,"//div[@id = 'huddles']")
    new_huddle_btn = (By.XPATH,"//button[@id = 'create-huddle']")
    for_test_huddles_people = (By.XPATH,"//div[@class = 'huddle-people  ']/parent::div[@data-tip = 'ani.bad@everse-soft.com']")
    new_task_btn = (By.XPATH,"//button[@id = 'create-task']")
    task_name_field = (By.XPATH,"//input[@id = 'task-name-input']")
    task_contributer_drop = (By.XPATH,"//div[@id = 'owner-dropdown']")
    select_me_as_contributor = (By.XPATH,"//label[text() = 'Ani Bad']")
    create_task_btn = (By.XPATH,"//button[@id = 'update-or-create-task-confirm']")
    task_status_first_drop = (By.XPATH,"//table/tbody/tr[1]//div[@id = 'dropdown']")
    task_status_second_drop = (By.XPATH,"//table/tbody/tr[2]//div[@id = 'dropdown']")
    task_status_in_progress_first = (By.XPATH,"//table/tbody/tr[1]//div[@id = 'dropdown']/div[2]/div[2]")
    task_status_in_progress_second = (By.XPATH,"//table/tbody/tr[2]//div[@id = 'dropdown']/div[2]/div[2]")

class Settings_Page():
    settings_category_btn = (By.XPATH,'//a[@href="/settings?settings"]')
    goals_category = (By.ID,"goals")
    goals_name_field = (By.XPATH,"//input[@class = 'qp-textInput ']")
    goals_plus_btn = (By.XPATH,"//div[@class = 'goals-page--header-operation']")
    goal_delete_drop = (By.XPATH,"//div[@class = 'popover-open-icon']")
    delete_goal = (By.XPATH,"//span[text() = 'Delete']")
    change_to_spanish = (By.XPATH,"//input[@name = 'Spanish']")
    change_to_german = (By.XPATH,"//input[@name = 'German']")
    change_to_english = (By.XPATH,"//input[@name = 'English']")
    new_category_text = (By.XPATH,"//div[@class = 'initiatives-wrapper--navbar']/div/div/div[3]/span[1]")

class Ideation_Data():
    ideation_title_field = (By.XPATH,"//input[@placeholder='Enter a title for your ideation']")
    ideation_introduction_field = (By.XPATH,"//textarea[@placeholder = 'Enter an introduction for your ideation']")
    browser_logo = (By.XPATH,"//div[@class = 'file-uploader']")
    crowdsource_switch = (By.XPATH,"//input[@id = 'Crowdsource request']/parent::div")
    promoted_idea_switch = (By.XPATH,"//input[@id = 'Promoted Ideas']/parent::div")
    comments_switch = (By.XPATH,"//input[@id = 'Comments']/parent::div")
    draft_publish_drop = (By.XPATH,"//div[@id = 'ideation-dropdown']")
    publish_option = (By.XPATH,"//div[@id = 'publish']")
    ideas_1 = (By.XPATH,"//input[@placeholder = 'Idea 1']")
    ideas_2 = (By.XPATH,"//input[@placeholder = 'Idea 2']")
    ideas_3 = (By.XPATH,"//input[@placeholder = 'Idea 3']")
    first_idea_plus_btn = (By.XPATH,"//input[@placeholder = 'Idea 1']/parent::div/button[1]")
    second_idea_btn = (By.XPATH,"//input[@placeholder = 'Idea 2']/parent::div/button[1]")
    see_live_btn = (By.XPATH,"//span[@id = 'see-live']")
    start_page_intro = (By.XPATH,"//p[@class = 'start-page--sub-title']")
    ideation_start_btn = (By.XPATH,"//button[@class = 'qp-button start-page--start-btn']")
    logo_existence = (By.XPATH,"//img")
    add_your_idea_field = (By.XPATH,"//input[@placeholder = 'Write here your idea']")
    submit_btn = (By.XPATH,"//button[@class = 'qp-button idea-page--question--btn']")
    idea1_existence = (By.XPATH,"//div[@class = 'ideas-vote-page--voted-ideas-block']/div[1]/p")
    idea2_existence = (By.XPATH,"//div[@class = 'ideas-vote-page--voted-ideas-block']/div[2]/p")
    idea3_existence = (By.XPATH,"//div[@class = 'ideas-vote-page--voted-ideas-block']/div[3]/p")
    ideation_submit_btn = (By.XPATH,"//button[@class = 'qp-button ideas-vote-page--submit-btn']")
    thank_you = (By.XPATH,"//p[@class = 'end-page--sub-sub-title']")
    logo_input = (By.XPATH,"//input[@name = 'file']")
    validation_error_desc = (By.XPATH,"//label[@class = 'error-label']")
    without_switch_valid_error = (By.XPATH,"//div[@id = 'root']/div/div/div/div[2]")
    back_ideation = (By.XPATH,"//div[@class = 'editIdeation-container-header-block1']/*[1]")
    ideation_title_disabled = (By.XPATH,"//input[@placeholder = 'Enter a title for your ideation' and @disabled]")
    ideation_description_disabled = (By.XPATH,"//textarea[@placeholder = 'Enter an introduction for your ideation' and @disabled]")
    crowdsource_switch_disabled = (By.XPATH,"//input[@id = 'Crowdsource request' and @disabled]")
    promoted_idea_switch_disabled = (By.XPATH,"//input[@id = 'Promoted Ideas' and @disabled]")
    comments_switch_disabled = (By.XPATH,"//input[@id = 'Comments' and @disabled]")
    browser_logo_disabled = (By.XPATH,"//input[@accept = '.jpg,.png,.jpeg,.svg' and @disabled]")
    for_hover_top_goals = (By.XPATH,"//div[@class = 'top-goals initiative-sidebar--section']")
    ideation_copy_btn = (By.XPATH,"//div[@class = 'editIdeation-container-url-block']/*[2]")
    for_idea_url = (By.XPATH,"//input[@class = 'editIdeation-container-url-textField']")
    add_comment_btn = (By.XPATH,"//button[@class = 'idea-comments--btn']")
    comment_field = (By.XPATH,"//input[@class = 'qp-textInput idea-comments--input']")
    send_comment_btn = (By.XPATH,"//div[@class = 'idea-comments--input-block']/button")
    results_category = (By.XPATH,"//div[@id = 'results']")
    participants_count = (By.XPATH,"//div[@class = 'idea-flow-results--progress--content']/div[1]/span")
    idea_count = (By.XPATH,"//div[@class = 'idea-flow-results--progress--content']/div[2]/span")
    comments_count = (By.XPATH,"//div[@class = 'idea-flow-results--progress--content']/div[3]/span")
    ideas_count = (By.XPATH,"//div[@class = 'monthly-statistics']/div[3]/p")
    add_your_idea_btn = (By.XPATH,"//button[@class = 'ideas-vote-page--allow-ideas--btn']")
    idea_send_btn = (By.XPATH,"//button[@type = 'submit']")
    ideas = (By.XPATH,"//button[@class = 'idea-item--like-btn']")
    ideation_submit_result = (By.XPATH,"//div[@class = 'idea-item--likes-comments']")

    
    

class Analytics():
    top_contributers_first = (By.XPATH,"//div[@class = 'top-contributors--content']/div[2]/p[1]")
    top_contributors_tasks_count = (By.XPATH,"//p[text() = 'Ani Bad']/parent::div/p[2]")
    active_init_count = (By.XPATH,"//div[@class = 'monthly-statistics']/div[1]/p")
    

class Tasks():
    task_name_field = (By.XPATH,"//input[@id = 'task-name-input']")
    task_description_field = (By.XPATH,"//textarea[@id = 'task-description-input']")
    select_owner_drop = (By.XPATH,"//span[text() = 'Select owner']/parent::div")
    task_due_date = (By.XPATH,"//div[text() = '28']")
    select_owner_me = (By.XPATH,"//div[text() = 'Ani Bad']")
    task_create_btn = (By.XPATH,"//button[@id = 'update-or-create-task-confirm']")
    task_name_check = (By.XPATH,"//tbody/tr[1]/td[1]")
    for_owner_check = (By.XPATH,"//tbody/tr/td[3]/div/div[1]")
    name_valid_error = (By.XPATH,"//label[@class = 'error-label']")
    modal_close = (By.XPATH,"//div[@class = 'base-modal-header--close']")
    for_hover = (By.XPATH,"//td[@data-label = 'Completed on']")
    tasks_edit_btn = (By.XPATH,'//div[@class="table-operation"]/*[2]')
    task_due_date_number = (By.XPATH,"//td[@class = 'qp-table-td task-table-row--due']")
    select_task_status = (By.XPATH,"//td[@data-label='Status']/div/div")
    select_status_completed = (By.XPATH,"//div[text() = 'Completed']")
    interval = (By.XPATH,"//div[@class = 'task-table-row--due-past-day']")
    
    
    
    

    


    
    


    
    
