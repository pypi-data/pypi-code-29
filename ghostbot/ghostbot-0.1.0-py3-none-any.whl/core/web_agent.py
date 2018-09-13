from urllib.parse import urljoin
from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ghostbot import GhostbotProfile, StatusCode
from ghostbot.utils.logger import Logger
from ghostbot.utils.os import FileSystem
from ghostbot.utils.datetime import Datetime
from ghostbot.utils.decorator import action
from ghostbot.scripts.drivers import Ghost
from .agent import Agent, Appearances, Formats


class WebDrivers(Enum):
    DEFAULT = "default"
    GHOST = "ghost"
    CHROME = "chrome"
    EDGE = "edge"
    FIREFOX = "firefox"
    SAFARI = "safari"


class WebWidgets(Enum):
    IMAGE = "image"
    LINK = "link"
    TEXT = "text"
    LIST_BOX = "list_box"
    LIST_ITEM = "list_item"
    INPUT_BOX = "input_box"
    CHECK_BOX = "check_box"
    RADIO_BUTTON = "radio_button"
    BUTTON = "button"
    UNKNOWN = "unknown"


class WebElement(object):
    ID = "id"
    NAME = "name"
    TAG_NAME = "tag_name"
    CLASS_NAME = "class_name"
    LINK_TEXT = "link_text"
    PARTIAL_LINK_TEXT = "partial_link_text"
    XPATH = "xpath"
    CSS_SELECTOR = "css_selector"

    def __init__(self):
        self._attributes = {}

    def __getattr__(self, item):
        pass

    def __setattr__(self, key, value):
        pass


class WebAgent(Agent):
    DOWNLOAD_MIME = ",".join([
        "application/octet-stream",
        "application/zip",
        "application/x-gzip",
        "application/x-exe"
    ])
    DEFAULT_WIDTH = 800
    DEFAULT_HEIGHT = 600
    IMPLICITLY_WAIT = 5
    PAGE_LOAD_TIMEOUT = 10

    def __init__(self, scenario=None, container=None, reactor=None):
        super().__init__(scenario, container, reactor)
        self.logger = Logger(__name__)
        self._browser = None
        self._url = None
        self._headers = {}
        self._exports = []

    def url(self, url=None):
        if url:
            self._url = url
        return self._url

    def headers(self, headers=None):
        if headers:
            self._headers = headers
        return self._headers

    def is_exports(self):
        return len(self._exports) > 0

    def exports(self, path=None):
        if path:
            self._exports.append(path)
        return self._exports

    def summary(self):
        return {
            "basis": {
                "is_continuable": self.is_continuable(),
                "has_warnings": self.has_warnings(),
                "has_errors": self.has_errors(),
                "warnings": self.warnings(),
                "errors": self.errors()
            },
            "asserter": {
                "is_success": self.is_success(),
                "asserts": self.asserts()
            },
            "web_agent": {
                "is_exports": self.is_exports(),
                "exports": self.exports()
            }
        }

    def startup(self, config=None):
        self.logger.info(StatusCode[127], config)
        config = config if config else {"driver": WebDrivers.DEFAULT}
        if "driver" not in config:
            config["driver"] = WebDrivers.DEFAULT
        if config["driver"] == WebDrivers.DEFAULT:
            # TODO choice most reasonable WebDriver
            config["driver"] = WebDrivers.FIREFOX
        try:
            if config["driver"] == WebDrivers.GHOST:
                self._browser = Ghost()
            elif config["driver"] == WebDrivers.CHROME:
                options = ChromeOptions()
                options.binary_location("/usr/bin/google-chrome")
                options.add_argument("--disable-gpu")
                options.add_argument("--no-sandbox")
                options.add_argument("--ignore-certificate-errors")
                options.add_experimental_option("profile.default_content_settings.popups", 0)
                options.add_experimental_option("safebrowsing.enabled", True)
                options.add_experimental_option("download.prompt_for_download", False)
                options.add_experimental_option("download.directory_upgrade", True)
                options.add_experimental_option("download.default_directory", GhostbotProfile.downloads)
                if "appearance" in config and config["appearance"] == Appearances.HEADLESS:
                    options.add_argument("--headless")
                if "size" in config:
                    options.add_argument("--window-size={}x{}".format(config["size"][0], config["size"][1]))
                else:
                    options.add_argument("--window-size={}x{}".format(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT))
                self._browser = webdriver.Chrome(chrome_options=options)
            elif config["driver"] == WebDrivers.EDGE:
                self._browser = webdriver.Edge()
            elif config["driver"] == WebDrivers.FIREFOX:
                profile = FirefoxProfile()
                profile.set_preference("browser.download.manager.showWhenStarting", False)
                profile.set_preference("browser.download.folderList", 2)
                profile.set_preference("browser.download.dir", GhostbotProfile.downloads)
                profile.set_preference("browser.helperApps.neverAsk.saveToDisk", self.DOWNLOAD_MIME)
                options = FirefoxOptions()
                options.add_argument("--disable-gpu")
                options.add_argument("--no-sandbox")
                if "appearance" in config and config["appearance"] == Appearances.HEADLESS:
                    options.add_argument("--headless")
                if "size" in config:
                    options.add_argument("--window-size={}x{}".format(config["size"][0], config["size"][1]))
                else:
                    options.add_argument("--window-size={}x{}".format(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT))
                null = FileSystem.devnull()
                self._browser = webdriver.Firefox(firefox_options=options, firefox_profile=profile, log_path=null)
            elif config["driver"] == WebDrivers.SAFARI:
                self._browser = webdriver.Safari()
            else:
                self.error(StatusCode[510], config["driver"])
        except Exception as e:
            self.critical(StatusCode[511], e.args)

    def shutdown(self):
        self.logger.info(StatusCode[128], self._browser)
        if self._browser:
            for handle in self._browser.window_handles:
                self._browser.close(handle)
            self._browser.quit()
            self._browser = None

    def fqdn(self, uri):
        result = uri
        if self._browser:
            result = urljoin(self.url(), uri)
        return result

    # TODO relational url convert to fqdn
    # TODO url utils or add listener
    @action
    def open(self, url, loading_marker=None):
        if self._browser:
            try:
                self.url(url)
                self._browser.get(url)
                if loading_marker:
                    wait = WebDriverWait(self._browser, self.PAGE_LOAD_TIMEOUT)
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, loading_marker)))
                container = self.container()
                if container:
                    container.contents(url, self._browser.page_source)
                    container.url(url)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def refresh(self, loading_marker=None):
        if self._browser:
            try:
                self._browser.refresh()
                if loading_marker:
                    wait = WebDriverWait(self._browser, self.PAGE_LOAD_TIMEOUT)
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, loading_marker)))
                container = self.container()
                if container:
                    container.contents(self.url(), self._browser.page_source)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def close(self):
        if self._browser:
            try:
                self._browser.close()
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def quit(self):
        if self._browser:
            try:
                self._browser.quit()
            except Exception as e:
                self.error(StatusCode[513], e.args)
            finally:
                self._browser = None
        else:
            self.error(StatusCode[512], __name__)

    @action
    def authenticate(self, user, password):
        if self._browser:
            try:
                self._browser.authenticate(user, password)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def window(self, position=None, size=None):
        result = None
        if self._browser:
            if position and size:
                result = {
                    "position": self._browser.get_window_position(),
                    "size": self._browser.get_window_size()
                }
            if position:
                self._browser.set_window_position(position.x, position.y)
            if size:
                self._browser.set_window_size(size.width, size.height)
        else:
            self.error(StatusCode[512], __name__)
        return result

    @action
    def window_minimize(self):
        if self._browser:
            try:
                self._browser.minimize_window()
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def window_maximize(self):
        if self._browser:
            try:
                self._browser.maximize_window()
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def window_fullscreen(self):
        if self._browser:
            try:
                self._browser.fullscreen_window()
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def switch_window(self, window_name):
        if self._browser:
            try:
                self._browser.switch_to_window(window_name)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def switch_dialog(self):
        if self._browser:
            try:
                self._browser.switch_to_alert()
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def dialog_accept(self):
        if self._browser:
            try:
                self._browser.accept()
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def dialog_close(self):
        if self._browser:
            try:
                self._browser.dismiss()
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def navigate_back(self):
        if self._browser:
            try:
                self._browser.back()
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def navigate_forward(self):
        if self._browser:
            try:
                self._browser.forward()
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    # TODO delete_cookie() and delete_all_cookies()
    @action
    def cookie(self, name=None, cookies=None):
        result = None
        if self._browser:
            try:
                if cookies:
                    result = self._browser.add_cookie(cookies)
                elif name:
                    result = self._browser.get_cookie(name)
                else:
                    result = self._browser.get_cookies()
                self._browser.forward()
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)
        return result

    @action
    def focus(self, element):
        pass

    @action
    def clear(self, element=None, delay=None):
        if self._browser:
            if delay:
                self.wait(delay)
            try:
                self._browser.clear()
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def type(self, text, element=None, delay=None):
        if self._browser:
            if delay:
                self.wait(delay)
            try:
                target = self._browser.find_element_by_id(element)
                target.send_key(text)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def click(self, element, delay=None, modifier=None):
        if self._browser:
            if delay:
                self.wait(delay)
            try:
                if modifier:
                    actions = ActionChains(self._browser)
                    actions.key_down(modifier)
                    actions.click(element)
                    actions.key_up(modifier)
                    actions.perform()
                else:
                    self._browser.click(element)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def double_click(self, element, delay=None):
        if self._browser:
            if delay:
                self.wait(delay)
            try:
                self._browser.double_click(element)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def download(self, download_file, url):
        if self._browser:
            try:
                self._browser.download(download_file, url)
                while True:
                    if FileSystem.exists(download_file):
                        break
                    else:
                        self.wait(0.5)
                self.exports(download_file)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def download_link(self, download_file, text, partial=False):
        if self._browser:
            try:
                if partial:
                    self._browser.find_element_by_partial_link_text(text).click()
                else:
                    self._browser.find_element_by_link_text(text).click()
                while True:
                    if FileSystem.exists(download_file):
                        break
                    else:
                        self.wait(0.5)
                self.exports(download_file)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def drag_and_drop(self, source, destination):
        if self._browser:
            try:
                actions = ActionChains(self._browser)
                actions.drag_and_drop(source, destination)
                actions.perform()
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def wait(self, seconds):
        if self._browser:
            self._browser.implicitly_wait(seconds)

    @action
    def find(self, css_selector):
        result = None
        if self._browser:
            try:
                result = self._browser.find_element_by_css_selector(css_selector)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)
        return result

    @action
    def find_all(self, css_selector):
        result = None
        if self._browser:
            try:
                result = self._browser.find_elements_by_css_selector(css_selector)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)
        return result

    @action
    def inject(self, javascript, *args, async=False):
        if self._browser:
            try:
                if async:
                    self._browser.execute_async_script(javascript, *args)
                else:
                    self._browser.execute_script(javascript, *args)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @action
    def export(self, file_name=None, file_format=Formats.PNG):
        if self._browser:
            try:
                if file_format == Formats.PNG:
                    # TODO resolve export directory
                    if file_name is None:
                        file_name = "{}.png".format(Datetime.timestamp(True))
                    directory = "TODO"
                    path = FileSystem.join(directory, file_name)
                    self._browser.get_screenshot_as_file(path)
                    self.exports(path)
                else:
                    # TODO
                    pass
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    def _resolve(self, element):
        result = None
        if isinstance(element, WebElement):
            pass
        elif isinstance(element, str):
            pass
        else:
            self.error(StatusCode[515], element)
        try:
            result = self._browser.find_element_by_id(element)
        except Exception as e:
            self.error(StatusCode[513], e.args)
        return result
