"""Provides functions related to Html page."""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# CONSTANTS
WAIT_TIME = 3

class Page():
    """Page class"""
    def __init__(self, driver):
        """Constructor of Page class"""
        self.driver = driver

    def click_with_key_down(self, element, key):
        """Click the element while pressing the specified button.

        :rtype: selenium.webdriver.remote.webelement.WebElement element
        :rtype: string key
        """
        actions = ActionChains(self.driver)
        actions.key_down(key).click(element).key_up(key).perform()

    def scroll_to_element(self, id_or_class):
        """Scroll to the element specified by the selector.

        :rtype: string id_or_class
        """
        element = self.get_element_by_id(id_or_class)
        if element is None:
            element = self.get_element_by_class_name(id_or_class)
        if element is None:
            print('Cannot scroll to [' + id_or_class + '].')
        else:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        return element

    def activate_tab(self, index=-1):
        """Activate the window tab, which is specified by index.

        If index is not specified, activate the last tab.

        :rtype: number index
        """
        target_tab = self.driver.window_handles[index]
        self.driver.switch_to.window(target_tab)

    def close_inactive_tabs(self):
        """Close all the window tabs, which are not active."""
        while len(self.driver.window_handles) > 1:
            self.activate_tab(1)
            self.driver.close()
            self.activate_tab()

    def force_click(self, element):
        """Click the element via JavaScript.

        It is possible to click an element even when element.is_displayed() is False.
        """
        self.driver.execute_script('$(arguments[0]).click();', element)

    def get_element(self, selected_by, value):
        """Get the element by the specified selector.

        Wait until the element is fully loaded.

        :rtype: selenium.webdriver.remote.webelement.WebElement element
        """
        try:
            is_located = EC.presence_of_element_located((selected_by, value))
            return WebDriverWait(self.driver, WAIT_TIME).until(is_located)
        except TimeoutException:
            return None

    def get_elements(self, selected_by, value):
        """Get all the elements by the specified selector.

        Wait until the elements are fully loaded.

        :rtype: selenium.webdriver.remote.webelement.WebElement element
        """
        try:
            is_located = EC.presence_of_all_elements_located((selected_by, value))
            return WebDriverWait(self.driver, WAIT_TIME).until(is_located)
        except TimeoutException:
            return None

    def get_element_by_id(self, element_id):
        """Get the element specified by id.

        Wait until the element is fully loaded.

        :rtype: selenium.webdriver.remote.webelement.WebElement element
        """
        return self.get_element(By.ID, element_id)

    def get_element_by_class_name(self, class_name):
        """Get the element specified by class name.

        Wait until the element is fully loaded.

        :rtype: selenium.webdriver.remote.webelement.WebElement element
        """
        return self.get_element(By.CLASS_NAME, class_name)

    def get_elements_by_class_name(self, class_name):
        """Get all the elements specified by class name.

        Wait until the elements are fully loaded.

        :rtype: selenium.webdriver.remote.webelement.WebElement element
        """
        return self.get_elements(By.CLASS_NAME, class_name)
