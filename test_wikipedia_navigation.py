
from appium import webdriver
from appium.options.common.base import AppiumOptions
import time

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "org.wikipedia",
    "appActivity": "org.wikipedia.DefaultIcon",
    "automationName": "UiAutomator2",
    "noReset": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(3)

driver.find_element("id", "org.wikipedia:id/nav_tab_search").click()
time.sleep(2)

search_input = driver.find_element("id", "org.wikipedia:id/search_card")
assert search_input.is_displayed(), "Search screen not loaded!"
print("✅ Navigation test PASSED")

time.sleep(2)
driver.quit()