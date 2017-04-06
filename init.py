
from appium import webdriver
import os
import unittest
from setup import startappiumserver


class ContactAppTestAppium(unittest.TestCase):
    def setUp(self):

        print("Start setup.")
        print("Veendum start setup.")
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'Z110P3016B00410'
        desired_caps['app'] = os.path.abspath('C:\ShyamaAPK\player-release-2.1.0.2138.apk')

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.success = True

    def tearDown(self):
        print("Start tear down.")

    def touch(self):
        print("Start configuration."),
        size = self.manage().window().getSize()
        print(size)
        # to gte the touch points
        x1 = int(size.width * 0.20)
        print(x1)
        y1 = int(size.height * 0.20)
        print(y1)

    def test_a(self):
        print("Start setup.")
        try:

            self.driver.find_element_by_id("uk.co.humboldt.onelan.player:id/btnNextWizardStep").click()
            self.driver.find_element_by_id("uk.co.humboldt.onelan.player:id/btnNextWizardStep").click()

            print("Set Access Code...", end="")
            self.driver.find_element_by_id("uk.co.humboldt.onelan.player:id/accessCode").send_keys("9999")
            self.driver.find_element_by_id("uk.co.humboldt.onelan.player:id/confirmAccessCode").send_keys("9999")
            self.driver.find_element_by_id("uk.co.humboldt.onelan.player:id/nextButton").click()
            print("Done.")

            print("Device Admin set...", end="")
            self.driver.find_element_by_id("uk.co.humboldt.onelan.player:id/btnNextWizardStep").click()
            self.driver.find_element_by_id("com.android.settings:id/action_button").click()
            self.driver.find_element_by_id("uk.co.humboldt.onelan.player:id/btnNextWizardStep").click()
            print("Done.")

            print("Subscription url...", end="")
            self.driver.find_element_by_xpath(
                "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[2]").click()
            self.driver.find_element_by_id("android:id/edit").send_keys("ntb42525")
            self.driver.find_element_by_id("android:id/button1").click()
            print("Done.")

            print("Username...", end="")
            self.driver.find_element_by_xpath(
                "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]").click()
            self.driver.find_element_by_id("android:id/edit").send_keys("remote")
            self.driver.find_element_by_id("android:id/button1").click()
            print("Done.")

            print("Password...", end="")
            self.driver.find_element_by_xpath(
                "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]").click()
            self.driver.find_element_by_id("android:id/edit").send_keys("9999")
            self.driver.find_element_by_id("android:id/button1").click()
            print("Done.")

            print("Apply action...", end="")
            self.driver.find_element_by_name("Apply").click()
            print("Done.")

            print("Ok before launch", end="")
            self.driver.find_element_by_id("uk.co.humboldt.onelan.player:id/btnNextWizardStep").click()
            print("Done.")
            print("Setup complete.")
        except Exception as e:
            print(e)
            print("all errors caught...")
        finally:
            # self.driver.quit()
            print("Finally.")
        if not self.success:
            raise Exception("Test failed.")


if __name__ == '__main__':
    startappiumserver()
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactAppTestAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)
