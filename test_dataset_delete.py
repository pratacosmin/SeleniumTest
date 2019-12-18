'''
Created on Oct 9, 2019

@author: azim
'''

import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
from webdriver_manager.firefox import GeckoDriverManager



class TestDatasetDelete(unittest.TestCase):
    @classmethod
    def setUp(inst):
       
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')

        # inst.driver = webdriver.Firefox('/home/cosmin/.local/lib/python3.6/site-packages/selenium/webdriver', options=chrome_options)
        # inst.driver = webdriver.Firefox('/home/cosmin/.local/lib/python3.6/site-packages/selenium/webdriver')

        inst.driver =  webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
        inst.driver.get('https://keycloak-prod.wisecube.ai/auth/realms/wisecube/protocol/openid-connect/auth?client_id=wisecube-ui&redirect_uri=https%3A%2F%2Fapp.wisecube.ai%2F&state=e2cd04ee-4868-4060-9482-82b572ef49d7&response_mode=fragment&response_type=code&scope=openid&nonce=300696d4-98be-4962-82f0-a0efeb759e1a')
        driver = inst.driver
        
        # using log in credentials
        element1 = driver.find_element_by_id('username')
        element1.send_keys('wisecube')

        element2 = driver.find_element_by_id('password')
        element2.send_keys('wise@Cube!')

        logbutton = driver.find_element_by_id('kc-login')
        logbutton.click()
        
        
    def test_Delete_dataset(self):
        driver = self.driver
        time.sleep(10)
        actions = ActionChains(self.driver)
        
        #accessing sidepanel
        side_panel = driver.find_element_by_css_selector("app-sidebar")
        actions.move_to_element(side_panel).perform()
        
        time.sleep(5)
        
        wait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Datasets"))).click()
        
        time.sleep(5)
        
        #accessing New Dataset form
        dataset_page = driver.find_element_by_css_selector("app-resources")
        actions.move_to_element(dataset_page).perform()
        
        
        time.sleep(5)
        
    
        wait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-btn.btn.waves-effect.waves-light.btn-small.blue"))).click()
        
        time.sleep(5)
        
        #adding new dataset
        element = driver.find_element_by_name('name')
        element.send_keys('Test')
        
        wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Save')]"))).click()
        
        time.sleep(5)
        
        #accessing dataset table
        dataset_table = driver.find_element_by_css_selector("app-list")
        actions.move_to_element(dataset_table).perform()
        
        dataset_row = driver.find_element_by_css_selector("tr.row")
        actions.move_to_element(dataset_row).perform()
        
        
        time.sleep(5)
        
        #clicking delete icon
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//td/i[.='delete']"))).click()
        
        time.sleep(5) 
        
        #Clicking OK through accept(), we can click cancel through dismiss()
        popup = driver.switch_to.alert
        #popup.dismiss()
        popup.accept()
        
        time.sleep(5)
       
    @classmethod    
    def tearDown(inst):    
    
        inst.driver.quit() 


if __name__ == '__main__':
    unittest.main()
