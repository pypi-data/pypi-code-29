import json
import sys
import tarfile
from datetime import datetime
import os
import shutil
from tqdm import tqdm
import requests

import package_updater


class update(object):
    def __init__(self, package_name, current_version, repo):
        self.REPO = repo
        self.CURRENT_VER = current_version
        self.PACKAGE_NAME = package_name
        self.CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

    def print_c(self, string, message_type, endline=True):
        """print_colored
        """
        COMMANDS = {
            "info": (33, "[!] "),
            "que": (34, "[?] "),
            "bad": (31, "[-] "),
            "good": (32, "[+] "),
            "run": (97, "[~] "),
        }
        print(
            "\033[{}m{}\033[0m{}".format(
                COMMANDS[message_type][0], COMMANDS[message_type][1], string
            ),
            end=("\n" if endline else ""),
        )

    def copytree(self, src, dst, symlinks=False, ignore=None):
        if not os.path.exists(dst):
            os.makedirs(dst)
            shutil.copystat(src, dst)
        lst = os.listdir(src)
        if ignore:
            excl = ignore(src, lst)
            lst = [x for x in lst if x not in excl]
        for item in lst:
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if symlinks and os.path.islink(s):
                if os.path.lexists(d):
                    os.remove(d)
                os.symlink(os.readlink(s), d)
            elif os.path.isdir(s):
                self.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)

    def update(self):
        self.print_c(
            f"Welcome to package updater (version {package_updater.__version__}).",
            "info",
        )
        self.print_c(
            f"Current version {self.CURRENT_VER}, looking for update at {self.REPO}",
            "run",
        )

        try:
            r = requests.get(self.REPO, headers={"Accept-Encoding": "identity"})

            if r.ok:
                response = json.loads(r.text or r.content)

                last_version_name = response["tag_name"]
                last_version_url = response["tarball_url"]

                if last_version_name > self.CURRENT_VER:
                    self.print_c(
                        f"New version {last_version_name} is available at {last_version_url} !",
                        "good",
                    )

                    self.print_c("Backing up current version to tar file..", "run")

                    backup_dir = "backups"
                    if not os.path.exists(backup_dir):
                        os.makedirs(backup_dir)
                    current_date = datetime.now().strftime("%Y-%m-%d")
                    backup_name = (
                        self.PACKAGE_NAME
                        + "-"
                        + self.CURRENT_VER
                        + "-"
                        + current_date
                        + ".tar.gz"
                    )

                    with tarfile.open(
                        backup_dir + "/" + backup_name, mode="w:gz"
                    ) as backup:
                        backup.add(
                            self.CURRENT_DIR,
                            arcname=os.path.basename(self.CURRENT_DIR),
                            recursive=True,
                        )

                    self.print_c(
                        f"{self.PACKAGE_NAME} has been backed up to {backup_dir}\{backup_name}",
                        "good",
                    )

                    self.print_c(f"Downloading new version..", "run")

                    r = requests.get(
                        last_version_url,
                        stream=True,
                        headers={"Accept-Encoding": "identity"},
                    )

                    if r.status_code == 200:
                        last_version_name += ".tar.gz"
                        with open(last_version_name, "wb") as f:
                            try:
                                total_size = r.headers["Content-Length"]
                            except KeyError:
                                self.print_c("Release length unavailable", "info")
                                total_size = None

                            if total_size is None:
                                for chunk in r:
                                    f.write(chunk)
                            else:
                                with tqdm(
                                    total=100, ncols=100, desc="\033[97m[~]\033[0m "
                                ) as pbar:
                                    for chunk in r.iter_content(
                                        chunk_size=int(int(total_size) / 99)
                                    ):
                                        f.write(chunk)
                                        pbar.update(1)

                        self.print_c(
                            f"Release downloaded <{last_version_name}>", "good"
                        )

                        self.print_c("Decompressing..", "run", False)
                        tar_release = tarfile.open(last_version_name)
                        tar_release.extractall()
                        tar_release_name = tar_release.getnames()[0]
                        print(" Done.")

                        self.print_c("Installing new version..", "run", endline=False)
                        self.copytree(tar_release_name + "/", self.CURRENT_DIR + "/")
                        print(" Done.")

                        self.print_c("Deleting temporary files..", "run", endline=False)
                        os.remove(tar_release.name)
                        shutil.rmtree(tar_release_name)
                        print(" Done.")

                        self.print_c(
                            f"New version {last_version_name} has been installed !",
                            "good",
                        )

                    else:
                        self.print_c(
                            "Error in HTTP request, please check the connection and try again.",
                            "bad",
                        )
                        sys.exit(0)
                else:
                    self.print_c(f"{self.PACKAGE_NAME} is already up to date", "good")
                    sys.exit(0)

            else:
                self.print_c(
                    "Error in HTTP request, please check the connection and try again.",
                    "bad",
                )
                sys.exit(0)

        except requests.exceptions.ConnectionError:
            self.print_c(
                "Failed to connect, please check the connection and try again.", "bad"
            )
            sys.exit(0)


# update()
