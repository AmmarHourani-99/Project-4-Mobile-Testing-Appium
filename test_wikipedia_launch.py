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

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4723",
    options=options
)

time.sleep(3)

search_bar = driver.find_element("id", "org.wikipedia:id/search_container")
assert search_bar.is_displayed(), "Search bar not visible — app launch failed!"
print("✅ App launch test PASSED")

time.sleep(2)
driver.quit()