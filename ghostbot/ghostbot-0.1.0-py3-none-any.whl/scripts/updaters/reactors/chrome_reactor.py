from ghostbot import GhostbotProfile, StatusCode
from ghostbot.core import WebReactor
from ghostbot.utils.logger import Logger
from ghostbot.utils.os import FileSystem
from ghostbot.utils.archiver import ZipArchive


class ChromeReactor(WebReactor):
    CHECK_KEY = ["latest_release", "driver"]
    UPDATE_KEY = ["url", "version", "driver", "datetime", "size", "etag", "supports", "changes"]
    README = """
============================================================
ChromeDriver Information
============================================================
URL:           {}
Version:       {}
File:          {}
Last Modified: {}
Size:          {}
ETag:          {}
------------------------------------------------------------
{}
    
{}
"""

    def __init__(self, agent=None):
        super().__init__(agent)
        self.logger = Logger(__name__)

    def execute(self):
        options = self.options()
        if "action" in options:
            if options["action"] == "check":
                self._check()
            elif options["action"] == "update":
                self._update()
            else:
                self.error(StatusCode[203], options["action"], "action")
        else:
            self.error(StatusCode[202], "action", "options")

    def _check(self):
        scrap = self.container().scrap()
        miss = [key for key in self.CHECK_KEY if key not in scrap]
        if len(miss) == 0:
            version = scrap["latest_release"].split()[1]
            if FileSystem.exists(FileSystem.join(GhostbotProfile.assets_drivers, "chrome", version)):
                self.logger.info(StatusCode[124], scrap["driver"], version)
            else:
                # TODO feedback global objects that need for update
                self.logger.info(StatusCode[125], scrap["driver"], version)
        else:
            self.error(StatusCode[503], miss, "scrap")

    def _update(self):
        scrap = self.container().scrap()
        miss = [key for key in self.UPDATE_KEY if key not in scrap]
        if len(miss) == 0:
            datetime = scrap["datetime"]
            version = scrap["version"]
            driver = scrap["driver"]
            size = scrap["size"]
            etag = scrap["etag"]
            url = scrap["url"]
            # TODO convert from HTML to MARKDOWN
            # supports = self.markdown(scrap["supports"])
            # changes = self.markdown(scrap["changes"])
            supports = scrap["supports"].text
            changes = scrap["changes"].text
            driver_file = scrap["download_file"]
            current_path = FileSystem.join(GhostbotProfile.assets_drivers, "chrome", "_current")
            version_path = FileSystem.join(GhostbotProfile.assets_drivers, "chrome", version)
            readme_file = FileSystem.join(version_path, "README.txt")
            if FileSystem.exists(driver_file):
                self.logger.info(StatusCode[123], driver)
                try:
                    message = self.README.format(url, version, driver, datetime, size, etag, supports, changes)
                    FileSystem.remove(current_path + "/*")
                    ZipArchive.decompress(driver_file, current_path)
                    FileSystem.make_directory(version_path)
                    FileSystem.move(driver_file, version_path)
                    with open(readme_file, "w") as file:
                        file.write(message)
                    FileSystem.copy(readme_file, current_path)
                except Exception as e:
                    self.logger.error(StatusCode[515], e.args)
            else:
                self.error(StatusCode[224], driver_file)
        else:
            self.error(StatusCode[503], miss, "scrap")
