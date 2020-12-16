import unittest
from selenium import webdriver


class RoamingDestinationsPageTest(unittest.TestCase):
    @classmethod
    def setUp(inst):
        # create a new Firefox session """
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

        # navigate to the roaming destinations page """
        inst.driver.get(
            "http://www.three.co.uk/Support/Roaming_and_international/Roaming_Abroad/Destinations?#countries2")

    def test_country_button_link(self):
        # check button link works on the page
        button_link = self.driver.find_element_by_link_text("Brazil.")
        button_link.click()

    @classmethod
    def tearDown(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
