class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element("id", "username")
        self.password_input = driver.find_element("id", "password")
        self.login_button = driver.find_element("id", "loginBtn")

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()
