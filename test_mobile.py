from appium import webdriver
from selenium.webdriver.common.by import By

def test_find_article():
    desired_capabilities = {
        "platformName": "Android",
        'app': '/Users/kseniagorkova/PycharmProjects/appium_example_test/Wikipedia_v2.7.50397-r-2022-03-09_apkpure.com.apk',
        'noReset': True
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)
    try:
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,"//android.widget.FrameLayout[@content-desc='Search']").click()
        driver.find_element(By.ID, "org.wikipedia:id/search_card").click()
        driver.find_element(By.ID, "org.wikipedia:id/search_src_text").send_keys('Nikola Tesla')
        driver.find_element(By.ID, "org.wikipedia:id/page_list_item_title").click()
        actual_text = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[1]").text
        assert "Nikola Tesla" == actual_text, f"Open age is wrong: {actual_text}"
    finally:
        driver.quit()
