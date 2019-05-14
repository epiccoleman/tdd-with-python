from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # go to the website's homepage
        print('shit')
        self.browser.get('http://localhost:8000')

        # the page title and header mention to-do lists
        self.assertIn('To-Do', browser.title)
        self.fail('Finish the test!')

        # the user is prompted to enter a to do item

        # the user types "buy concert tickets"

        # when the user hits enter, the page updates and lists
        # "1: buy concert tickets" as an item in the to do list

        # the user is prompted to enter another to do item. they enter "attend concert"

        # the page updates and shows both items

        # there is a message informing the user that the site has generated a unique url for her

        # when the user visits the url, the todo list is still present

if __name__ == '__main__':
    unittest.main(warnings="ignore")
