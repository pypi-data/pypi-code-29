import os
import sys
import re
from subprocess import check_output, call
from difflib import Differ

red_begin = "\033[91m"
red_end = "\033[0m"


def die(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def check_git_status():
    ret = call(["git", "diff-index", "--quiet", "HEAD", "--"])
    if ret > 0:
        print("{}There are unstaged changes in the working tree.{}\n"
              "Are you sure you want to continue?".format(
                  red_begin, red_end
              ))
        wait_for_ret()


def chdir():
    scriptpath = sys.argv[0]
    os.chdir(os.path.dirname(scriptpath))


def parse_version_string(ver):
    try:
        ver = tuple(map(int, ver.split(".")))
        if len(ver) != 3:
            raise ValueError
        return ver
    except ValueError:
        die("Invalid version string. Please provide a version of the form "
            "X.Y.Z (all integers).")


def wait_for_ret():
    try:
        input("Hit return to continue or ^C to cancel ...")
    except KeyboardInterrupt:
        die("\nCancelled")


def diff_lines(old, new):
    d = Differ()
    diff = list(d.compare(old, new))
    for line in diff[:]:
        if line.startswith(" "):
            diff.remove(line)

    return diff


def update_readme():
    branch = check_output(["git", "rev-parse",
                           "--abbrev-ref", "HEAD"]).decode().strip()
    print("Current branch is '{}'".format(branch))
    wait_for_ret()

    readmefn = "../README.rst"

    with open(readmefn) as oldreadme:
        oldrmtext = oldreadme.readlines()

    newrmtext = []
    for line in oldrmtext:
        if ("travis-ci.org" in line or
                "coveralls.io" in line or
                "ci.appveyor.com" in line):
            line = line.replace("master", branch)
        newrmtext.append(line)

    diff = diff_lines(oldrmtext, newrmtext)

    if len(diff) == 0:
        print("No changes required in README.")
        wait_for_ret()
        return False

    print("".join(diff))
    print("{}The above changes will be written to README.rst{}".format(
        red_begin, red_end
    ))
    wait_for_ret()
    print(">>> with open(readmefn) as readme:\n"
          "       readme.writelines(newrmtext)")
    return True


def update_info(newver):
    infofn = "../nixio/info.py"
    with open(infofn) as infofile:
        oldinfo = infofile.readlines()

    newinfo = []
    for line in oldinfo:
        if line.startswith("VERSION"):
            line = re.sub("'[1-9\.a-z]+'", "'" + newver + "'", line)
        newinfo.append(line)

    diff = diff_lines(oldinfo, newinfo)

    if len(diff) == 0:
        print("No changes required in info.py")
        wait_for_ret()
        return False

    print("".join(diff))
    print("{}The above changes will be written to info.py{}".format(
        red_begin, red_end
    ))
    wait_for_ret()
    print(">>> with open(infofn) as infofile:\n"
          "       infofile.writelines(newinfo)")
    return True


def main():
    check_git_status()

    chdir()

    newverstr = sys.argv[1]
    parse_version_string(newverstr)

    prepline = "Preparing new release: {}".format(newverstr)
    banner = "="*len(prepline) + "\n" + prepline + "\n" + "="*len(prepline)
    print(banner)

    chg = update_readme()

    chg = chg | update_info(newverstr)

    if chg:
        print("Files have changed. Commit these changes and rerun the script.")
        # sys.exit(0)

    check_git_status()  # might have been external changes (?) check again
    print("{}Tagging current commit with '{}'{}".format(
        red_begin, newverstr, red_end))
    wait_for_ret()
    print("{}$ git tag {}{}".format(red_begin, newverstr, red_end))

    print("Creating archive...")
    os.chdir("..")
    ret = call(["python", "setup.py", "sdist"])

    if ret == 0:
        print("Package ready. See 'dist' directory under project root.")
    else:
        print("Error creating package.")


if __name__ == "__main__":
    main()
