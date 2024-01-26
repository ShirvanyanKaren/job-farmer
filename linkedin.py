from selenium import webdriver
from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

user_prompts = True


def login():
    email_phone = ''
    password = ''
    try:
        if user_prompts:
            email_phone = input("Enter the email address or phone number to your LinkedIn account: ")
            password = input("Enter the password for your LinkedIn account: ")
        driver.get("https://www.linkedin.com")
        time.sleep(.5)
        driver.find_element(By.ID, "session_key").send_keys(email_phone)
        driver.find_element(By.ID, "session_password").send_keys(password)
        driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/button").click()
    except NoSuchElementException as e:
        print("Some elements were not found:", e)
    except Exception as e:
        print("An error occurred:", e)
    if driver.current_url == "https://www.linkedin.com/feed/?trk=homepage-basic_sign-in-submit":
        print(f'Successfully logged into LinkedIn.com using the account associated with: {email_phone}')
        return True
    else:
        raise Exception(f'Expected URL to be https://www.linkedin.com but got {driver.current_url} instead.')


def search_jobs(**kwargs):
    try:
        driver.get("https://www.linkedin.com/jobs/")
        time.sleep(5)
        search_bar = driver.find_element(By.XPATH, "/html/body/div[4]/header/div/div/div/div[2]/div[2]/div/div/input[1]")
        search_bar.send_keys(kwargs["search_key"])
        search_bar.send_keys(Keys.ENTER)
        time.sleep(5)
        if kwargs["remote"]:
            setting_button = driver.find_element(By.XPATH, '//*[@id="searchFilter_workplaceType"]')
            setting_button.click()
            time.sleep(1)
            remote_check = driver.find_element(By.XPATH, "//span[text()='Remote']")
            remote_check.click()
            results_button = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[4]/section/div/section/div/div/div/ul/li[7]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]/span')
            results_button.click()
            time.sleep(1)
        if kwargs["easy_apply"]:
            easy_apply_button = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button')
            easy_apply_button.click()
            time.sleep(1)
        print(f'Searching for jobs using the keyword {kwargs["search_key"]}.')
        return True
    except NoSuchElementException as e:
        print("Some elements were not found:", e)
    except Exception as e:
        print("An error occurred:", e)

