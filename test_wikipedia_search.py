
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

driver.find_element("id", "org.wikipedia:id/search_container").click()
time.sleep(2)

driver.find_element("id", "org.wikipedia:id/search_src_text").send_keys("Jordan")
time.sleep(3)

results = driver.find_element("id", "org.wikipedia:id/fragment_search_results")
assert results.is_displayed(), "Search results not displayed!"
print("✅ Search test PASSED")

time.sleep(2)
driver.quit()