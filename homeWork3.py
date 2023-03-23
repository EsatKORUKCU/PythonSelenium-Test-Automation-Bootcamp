from selenium import webdriver  
from webdriver_manager.chrome import ChromeDriverManager  
from time import sleep
from selenium.webdriver.common.by import By 

class Home:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(5)
    username_Input = driver.find_element(By.ID, "user-name")
    password_Input = driver.find_element(By.ID,"password")
    login_Btn = driver.find_element(By.ID,"login-button")
    
    
    # Test Case 1 :When the username and password fields are empty, "Epic sadface: Username is required" should be displayed as a warning message.
    def test_case1(self):
        self.login_Btn.click()
        sleep(3)
        errorMassage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMassage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU:  {testResult}")
    
    # Test Case 2 :The warning message "Epic sadface: Password is required" should be displayed only when the password field is empty.
    def test_case2(self):
        self.username_Input.send_keys("standard_user")
        sleep(3)
        self.login_Btn.click()
        errorMassage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMassage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU:  {testResult}")
    
    # Test Case3:Sending password field "secret_sauce" sending username "locked_out_user" sending "Epic sadface: Sorry, this user has been locked out." message should be displayed.
    def test_case3(self):
       self.username_Input.send_keys("locked_out_user") 
       self.password_Input.send_keys("secret_sauce")
       sleep(2)
       self.login_Btn.click()
       errorMassage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
       testResult = errorMassage.text ==  "Epic sadface: Sorry, this user has been locked out."
       print(f"TEST SONUCU:  {testResult}")
    
    #Test Case4:When the username and password fields are blank, a red "X" icon should appear next to these two inputs. Then these "X" icons should disappear when the close button of the warning message below is clicked.
    def test_case4(self):
        self.login_Btn.click()
        sleep(5)
        errorButton = self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button > svg")
        errorButton.click()
        
    #Test Case5:When username "standard_user" password "secret_sauce" is sent, user should be sent to "/inventory.html" page.
    def test_case5(self):
       self.username_Input.send_keys("standard_user") 
       self.password_Input.send_keys("secret_sauce")
       sleep(2)
       self.login_Btn.click()
       
       currentUrl = self.driver.current_url
       print(f"User successfully sent to  :{currentUrl}")
       
    #Test Case6:After logging in, the number of products displayed to the user should be "6".
    def test_case6(self):
        self.test_case5()
        list = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"The number of products shown to the user after logging in is : {len(list)}")
        
# run each case individually
test = Home()
test.test_case1()
# test.test_case2()
# test.test_case3()
# test.test_case4()
# test.test_case5()
# test.test_case6()

