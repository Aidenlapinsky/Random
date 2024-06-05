from selenium import webdriver

def take_screenshot(url):
    driver = webdriver.Servo()
    driver.get(url)
    driver.save_screenshot("screenshot.png")
    driver.quit()

take_screenshot("https://username.github.io")
