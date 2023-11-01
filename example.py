import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_video import VideoRecorder


class TestSeleniumVideoDemo(unittest.TestCase):

    driver = None
    video_recorder = None

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.video_recorder = VideoRecorder(self.driver)
        self.video_recorder.start()

    def tearDown(self):
        self.video_recorder.stop()
        self.driver.quit()

    def test_selenium_video_demo(self):
        self.driver.get("http://google.com")
        time.sleep(2)

        element = self.driver.find_element(By.ID, 'APjFqb')
        element.click()
        element.send_keys("hello")
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
