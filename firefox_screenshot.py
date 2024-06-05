from selenium import webdriver

def take_screenshot(url):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.save_screenshot("firefox_screenshot.png")
    driver.quit()

take_screenshot("https://username.github.io")
