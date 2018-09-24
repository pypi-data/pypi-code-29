import os

import lxml.html

from .canvas_session import CanvasSession
from .tools import create_dir, clean_dir, clean_file, create_shortcut


class Course:

    def __init__(self, course_id: int, session: CanvasSession, path: str):
        self.course_id = course_id
        self.session = session
        self.path = path

    def download(self):
        root = self.session.api_call("courses/%i/folders/root" % self.course_id)
        self.get_course_files(root["id"], self.path)

        modules = self.session.api_call("courses/%i/modules" % self.course_id)
        self.get_modules(modules)

        announcements = self.session.api_call("announcements?context_codes[]=course_%i" % self.course_id)
        announcement_path = self.path + "#ANNOUNCEMENTS/"
        create_dir(announcement_path)
        for announcement in announcements:
            time = announcement["posted_at"][:10]
            name = "%s %s.html" % (time, announcement["title"])
            file_path = announcement_path + clean_file(name)
            if os.path.isfile(file_path):
                continue
            file = open(file_path, "w")
            file.write(announcement["message"])
            file.close()

        assignments = self.session.api_call("courses/%i/assignments" % self.course_id)
        assignment_path = self.path + "#ASSIGNMENTS/"
        create_dir(assignment_path)

        for assignment in assignments:
            description = assignment["description"]
            if not description:
                continue
            content = lxml.html.fromstring(description)
            links = content.xpath("//a")
            if len(links) > 0:
                self.session.download_file(assignment_path + clean_file(assignment["name"] + ".pdf"), links[0].attrib["href"])

    def get_course_files(self, folder_id, path):
        print(path)
        create_dir(path)

        files = self.session.api_call("folders/%i/files" % folder_id)
        folders = self.session.api_call("folders/%i/folders" % folder_id)

        for file in files:
            if "id" in file:
                self.session.download_file(path + clean_file(file["display_name"]), file["url"])

        for folder in folders:
            if "id" in folder:
                self.get_course_files(folder["id"], path + clean_dir(folder["name"]))

    def get_modules(self, modules):
        path = self.path + "#MODULES/"
        create_dir(path)
        for module in modules:
            module_path = path + clean_dir(module["name"])
            create_dir(module_path)

            items = self.session.api_call("courses/%i/modules/%i/items" % (self.course_id, module["id"]))

            header = None
            for item in items:
                item_type = item["type"]
                new_path = module_path + (header if header else "")

                if item_type == "SubHeader":
                    header = clean_dir(item["title"])
                    create_dir(module_path + header)
                elif item_type == "File":
                    file = self.session.api_call("files/%i" % item["content_id"])
                    self.session.download_file(new_path + clean_file(file["display_name"]), file["url"])
                elif item_type in ["Quiz", "Assignment", "External_Link", "Page"]:
                    create_shortcut(new_path + clean_file(item["title"]), item["html_url"])

