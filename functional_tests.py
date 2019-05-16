from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # go to the website's homepage
        self.browser.get('http://localhost:8000')

        # the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # the user is prompted to enter a to do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )

        # the user types "buy concert tickets"
        inputbox.send_keys('Buy concert tickets')

        # when the user hits enter, the page updates and lists
        # "1: buy concert tickets" as an item in the to do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any (row.text == '1: Buy concert tickets' for row in rows)
        )

        # the user is prompted to enter another to do item. they enter "attend concert"
        self.fail('Finish the test!')

        # the page updates and shows both items

        # there is a message informing the user that the site has generated a unique url for her

        # when the user visits the url, the todo list is still present

if __name__ == '__main__':
    unittest.main(warnings="ignore")
