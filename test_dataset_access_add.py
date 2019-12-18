'''
Created on Oct 8, 2019

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




class TestDatasetAdd(unittest.TestCase):
    @classmethod
    def setUp(inst):
        #logging in to wisecube
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        inst.driver = webdriver.Chrome(options=chrome_options)
        #inst.driver = webdriver.Chrome()
        inst.driver.get('https://keycloak-prod.wisecube.ai/auth/realms/wisecube/protocol/openid-connect/auth?client_id=wisecube-ui&redirect_uri=https%3A%2F%2Fapp.wisecube.ai%2F&state=e2cd04ee-4868-4060-9482-82b572ef49d7&response_mode=fragment&response_type=code&scope=openid&nonce=300696d4-98be-4962-82f0-a0efeb759e1a')
        driver = inst.driver
        
        # using log in credentials
        element1 = driver.find_element_by_id('username')
        element1.send_keys('wisecube')

        element2 = driver.find_element_by_id('password')
        element2.send_keys('wise@Cube!')

        logbutton = driver.find_element_by_id('kc-login')
        logbutton.click()
        
        
        
    def test_dataset_access_add(self):
        driver = self.driver
        time.sleep(10)
        actions = ActionChains(self.driver)
        
        #accessing sidepanel
        side_panel = driver.find_element_by_css_selector("app-sidebar")
        actions.move_to_element(side_panel).perform()
        
        time.sleep(5)
        #Clicking Datasets panel
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
        
        #Entering description
        element = driver.find_element_by_xpath('//textarea[@name="description"]')
        element.clear()
        element.send_keys('Dataset for Test')
        
        time.sleep(5)
        
        wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Save')]"))).click()
        
        time.sleep(5)
         
       
    @classmethod    
    def tearDown(inst):    
    
        inst.driver.quit() 


if __name__ == '__main__':
    unittest.main()