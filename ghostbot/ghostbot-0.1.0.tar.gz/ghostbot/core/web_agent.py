import traceback
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from ghostbot import Ghostbot, GhostbotProfile, StatusCode
from ghostbot.constants import Appearances, Formats, WebDrivers
from ghostbot.utils.logger import Logger
from ghostbot.utils.os import Hash, FileSystem as fs
from ghostbot.utils.datetime import Datetime
from ghostbot.utils.decorator import api
from ghostbot.utils.json import Json
from ghostbot.scripts.drivers import Ghost
from .agent import Agent


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
    SYMBOL_RESOURCES = ":"
    DOWNLOAD_MIME = ",".join([
        "application/octet-stream",
        "application/zip",
        "application/x-gzip",
        "application/x-exe"
    ])
    CHROME_SETTINGS = {
        "arguments": [
            "--disable-infobars",
            "--ignore-certificate-errors",
            "--disable-gpu",
            "--no-sandbox"
        ],
        "options": {
            "download.default_directory": GhostbotProfile.downloads,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.plugins_disabled": ["Chrome PDF Viewer"],
            "plugins.always_open_pdf_externally": True
        }
    }
    FIREFOX_SETTINGS = {
        "arguments": [
            "--disable-gpu",
            "--no-sandbox"
        ],
        "options": {
            "browser.download.manager.showWhenStarting": False,
            "browser.download.folderList": 2,
            "browser.download.dir": GhostbotProfile.downloads,
            "browser.helperApps.neverAsk.saveToDisk": DOWNLOAD_MIME
        }
    }
    DEFAULT_WIDTH = 800
    DEFAULT_HEIGHT = 600
    IMPLICITLY_WAIT = 5
    PAGE_LOAD_TIMEOUT = 10

    def __init__(self, scenario=None, container=None, reactor=None):
        super().__init__(scenario, container, reactor)
        self.logger = Logger(__name__)
        self._browser = None
        self._url = None
        self._headless = False
        self._headers = {}
        self._exports = []
        self._resources = {}

    def execute(self, options=None):
        pass

    def url(self, url=None):
        if url:
            self._url = url
        return self._url

    def headers(self, headers=None):
        if headers:
            self._headers = headers
        return self._headers

    def is_headless(self):
        return self._headless

    def is_exports(self):
        return len(self._exports) > 0

    def exports(self, path=None, tags=None):
        if path:
            self._exports.append([path, tags])
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

    def fixtures_accounts(self, uri):
        return self._search(uri, Ghostbot.fixtures_accounts)

    def fixtures_cookies(self, uri):
        return self._search(uri, Ghostbot.fixtures_cookies)

    def fixtures_devices(self, uri):
        return self._search(uri, Ghostbot.fixtures_devices)

    def resources_bindings(self, uri):
        return self._search(uri, Ghostbot.resources_bindings)

    def resources_forms(self, uri):
        return self._search(uri, Ghostbot.resources_forms)

    def resources_schemas(self, uri):
        return self._search(uri, Ghostbot.resources_schemas)

    def resources_validators(self, uri):
        return self._search(uri, Ghostbot.resources_validators)

    def _search(self, uri, path):
        result = None
        if uri[:1] == self.SYMBOL_RESOURCES:
            uri = uri[1:]
            name = self.__module__.split(".")[-1].split("_")[0]
            file_name = "{}_{}.json".format(name, fs.split(path)[-1])
            path = fs.join(path, file_name)
            key = Hash.digest(path)
            if key not in self._resources:
                if fs.exists(path):
                    result = self._resources[key] = Json.load(path)
                else:
                    self.error(StatusCode[210], path)
            else:
                result = self._resources[key]
            if result:
                for segment in uri.split("."):
                    if segment in result:
                        result = result[segment]
                    else:
                        result = None
                        break
                if result and "nth-child" in result:
                    result = result.replace("nth-child", "nth-of-type")
        else:
            self.error(StatusCode[214], self.SYMBOL_RESOURCES)
        return result

    @api
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
                self._headless = True
            elif config["driver"] == WebDrivers.CHROME:
                options = ChromeOptions()
                options.add_experimental_option("prefs", self.CHROME_SETTINGS["options"])
                for argument in self.CHROME_SETTINGS["arguments"]:
                    options.add_argument(argument)
                if "appearance" in config and config["appearance"] == Appearances.HEADLESS:
                    options.add_argument("--headless")
                    self._headless = True
                if "size" in config:
                    options.add_argument("--window-size={}x{}".format(config["size"][0], config["size"][1]))
                else:
                    options.add_argument("--window-size={}x{}".format(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT))
                self._browser = webdriver.Chrome(chrome_options=options)
            elif config["driver"] == WebDrivers.EDGE:
                self._browser = webdriver.Edge()
            elif config["driver"] == WebDrivers.FIREFOX:
                profile = FirefoxProfile()
                for key, value in self.FIREFOX_SETTINGS["options"].items():
                    profile.set_preference(key, value)
                options = FirefoxOptions()
                for argument in self.FIREFOX_SETTINGS["arguments"]:
                    options.add_argument(argument)
                if "appearance" in config and config["appearance"] == Appearances.HEADLESS:
                    options.add_argument("--headless")
                    self._headless = True
                if "size" in config:
                    options.add_argument("--window-size={}x{}".format(config["size"][0], config["size"][1]))
                else:
                    options.add_argument("--window-size={}x{}".format(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT))
                null = fs.devnull()
                self._browser = webdriver.Firefox(firefox_options=options, firefox_profile=profile, log_path=null)
            elif config["driver"] == WebDrivers.SAFARI:
                self._browser = webdriver.Safari()
            else:
                self.error(StatusCode[510], config["driver"])
        except Exception as e:
            self.critical(StatusCode[511], e.args)
            traceback.print_exc()

    @api
    def shutdown(self):
        self.logger.info(StatusCode[128], self._browser)
        if self._browser:
            self._browser.quit()
            self._browser = None

    def fqdn(self, uri):
        result = uri
        if self._browser:
            result = urljoin(self.url(), uri)
        return result

    # TODO relational url convert to fqdn
    # TODO url utils or add listener
    @api
    def open(self, url, loading_marker=None):
        if self._browser:
            try:
                self.url(url)
                self._browser.get(url)
                if loading_marker:
                    self.wait_for(loading_marker)
                container = self.container()
                if container:
                    container.contents(url, self._browser.page_source)
                    container.url(url)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
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
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def close(self):
        if self._browser:
            try:
                self._browser.close()
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def quit(self):
        if self._browser:
            try:
                self._browser.quit()
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
            finally:
                self._browser = None
        else:
            self.error(StatusCode[512], __name__)

    @api
    def authenticate(self, user, password):
        if self._browser:
            try:
                self._browser.authenticate(user, password)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def window(self, position=None, size=None):
        result = None
        if self._browser:
            try:
                if position and size:
                    result = {
                        "position": self._browser.get_window_position(),
                        "size": self._browser.get_window_size()
                    }
                if position:
                    self._browser.set_window_position(position.x, position.y)
                if size:
                    self._browser.set_window_size(size.width, size.height)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)
        return result

    @api
    def window_minimize(self):
        if self._browser:
            try:
                self._browser.minimize_window()
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def window_maximize(self):
        if self._browser:
            try:
                self._browser.maximize_window()
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def window_fullscreen(self):
        if self._browser:
            try:
                self._browser.fullscreen_window()
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def switch_window(self, window_name):
        if self._browser:
            try:
                self._browser.switch_to_window(window_name)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def switch_dialog(self):
        if self._browser:
            try:
                self._browser.switch_to_alert()
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def dialog_accept(self):
        if self._browser:
            try:
                self._browser.accept()
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def dialog_close(self):
        if self._browser:
            try:
                self._browser.dismiss()
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def navigate_back(self):
        if self._browser:
            try:
                self._browser.back()
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def navigate_forward(self):
        if self._browser:
            try:
                self._browser.forward()
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    # TODO delete_cookie() and delete_all_cookies()
    @api
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
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)
        return result

    @api
    def focus(self, element):
        pass

    @api
    def clear(self, element, delay=None):
        if self._browser:
            self.move_to(element)
            try:
                element = self._resolve(element)
                element.clear()
                if delay:
                    self.wait(delay)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def input(self, element, text, delay=None):
        if self._browser:
            self.move_to(element)
            try:
                element = self._resolve(element)
                element.send_keys(text)
                if delay:
                    self.wait(delay)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def type(self, key_code, delay=None, modifier=None):
        if self._browser:
            try:
                actions = ActionChains(self._browser)
                if modifier:
                    actions.key_down(modifier)
                actions.key_down(key_code)
                actions.key_up(key_code)
                if modifier:
                    actions.key_up(modifier)
                actions.perform()
                if delay:
                    self.wait(delay)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def move_to(self, element, delay=None, wait_for=None, modifier=None):
        if self._browser:
            try:
                element = self._resolve(element)
                dx = element.size["width"] / 2
                dy = element.size["height"] / 2
                actions = ActionChains(self._browser)
                if modifier:
                    actions.key_down(modifier)
                actions.move_to_element_with_offset(element, dx, dy)
                if modifier:
                    actions.key_up(modifier)
                actions.perform()
                if delay:
                    self.wait(delay)
                if wait_for:
                    self.wait_for(wait_for)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def click(self, element, delay=None, wait_for=None, modifier=None):
        if self._browser:
            self.move_to(element)
            try:
                element = self._resolve(element)
                if modifier:
                    actions = ActionChains(self._browser)
                    actions.key_down(modifier)
                    actions.click(element)
                    actions.key_up(modifier)
                    actions.perform()
                else:
                    element.click()
                if delay:
                    self.wait(delay)
                if wait_for:
                    self.wait_for(wait_for)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def double_click(self, element, delay=None):
        if self._browser:
            self.move_to(element)
            try:
                element = self._resolve(element)
                element.double_click()
                if delay:
                    self.wait(delay)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def choice(self, element, value, delay=None):
        if self._browser:
            try:
                element = self._resolve(element)
                dropdown = Select(element)
                dropdown.select_by_value(value)
                if delay:
                    self.wait(delay)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def download(self, download_file, url):
        if self._browser:
            try:
                self._browser.download(download_file, url)
                while True:
                    if fs.exists(download_file):
                        break
                    else:
                        self.wait(0.5)
                self.exports(download_file)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def download_link(self, download_file, text, partial=False):
        if self._browser:
            try:
                if partial:
                    self._browser.find_element_by_partial_link_text(text).click()
                else:
                    self._browser.find_element_by_link_text(text).click()
                while True:
                    if fs.exists(download_file):
                        break
                    else:
                        self.wait(0.5)
                self.exports(download_file)
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def drag_and_drop(self, source, destination):
        if self._browser:
            try:
                source = self._resolve(source)
                destination = self._resolve(destination)
                actions = ActionChains(self._browser)
                actions.drag_and_drop(source, destination)
                actions.perform()
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
    def wait(self, seconds):
        if self._browser:
            self._browser.implicitly_wait(seconds)

    @api
    def wait_for(self, loading_marker):
        # FIXME loading_marker makes optional if possible
        # TODO can wait ajax communication?
        if self._browser:
            try:
                if loading_marker[:1] == self.SYMBOL_RESOURCES:
                    element = loading_marker[1:]
                else:
                    element = loading_marker
                wait = WebDriverWait(self._browser, self.PAGE_LOAD_TIMEOUT)
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    @api
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

    @api
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

    @api
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

    @api
    def scroll_top(self, delay=None):
        code = "window.scrollTo(0, 0);"
        if self._browser:
            try:
                self.inject(code)
                if delay:
                    self.wait(delay)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @api
    def scroll_bottom(self, delay=None):
        code = "window.scrollTo(0, document.body.scrollHeight);"
        if self._browser:
            try:
                self.inject(code)
                if delay:
                    self.wait(delay)
            except Exception as e:
                self.error(StatusCode[513], e.args)
        else:
            self.error(StatusCode[512], __name__)

    @api
    def validate(self, validator):
        # TODO
        pass

    def screenshot(self, tags=None):
        self.export(Formats.PNG, tags)

    def snapshot(self, tags=None):
        self.export(Formats.HTML, tags)

    @api
    def export(self, file_format, tags=None):
        if self._browser:
            try:
                # TODO support other file format
                timestamp = Datetime.timestamp(to_string=True)
                if file_format in [Formats.PNG, Formats.HTML_PNG]:
                    self._export("screenshots", timestamp, "png", tags,
                                 lambda path: self._browser.get_screenshot_as_file(path))
                if file_format in [Formats.HTML, Formats.HTML_PNG]:
                    self._export("snapshots", timestamp, "html", tags,
                                 lambda path: fs.save(path, self._browser.page_source))
            except Exception as e:
                self.error(StatusCode[513], e.args)
                traceback.print_exc()
        else:
            self.error(StatusCode[512], __name__)

    def _export(self, sub_directory, timestamp, extension, tags, callback):
        directory = fs.join(Ghostbot.evidence_directory(), sub_directory)
        if not fs.exists(directory):
            fs.make_directory(directory)
        file_name = "{}.{}".format(timestamp, extension)
        path = fs.join(directory, file_name)
        callback(path)
        self.exports(path, tags)

    def _resolve(self, element):
        result = None
        if isinstance(element, WebElement):
            result = element
        elif isinstance(element, str):
            if element[:1] == self.SYMBOL_RESOURCES:
                element = self.resources_forms(element)
            result = self._browser.find_element_by_css_selector(element)
        else:
            self.error(StatusCode[515], element)
        return result
