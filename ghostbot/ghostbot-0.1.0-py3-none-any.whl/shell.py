# main.py   --->  primitive command line console
# shell.py  --->  rich command line console

WIZARD_MENU = """
============================================================
          Welcome to the {target} Wizard
------------------------------------------------------------
  STEP-1: Choose {target}'s directory
  STEP-2: Choose {target}'s name
  STEP-3: Create your {target} files
============================================================
"""
WIZARD_GUIDE = "[STEP-{step}] {action} {target}'s {name}:"
WIZARD_PROMPT = "         > "
WIZARD_ECHO = "         Path: {path}"
WIZARD_CONFIRM = "         Do you want continue? [Y/N] > "
WIZARD_CANCEL = "         {target} Wizard canceled."

# print(self.WIZARD_MENU.format(target="Project"))
# print(self.WIZARD_GUIDE.format(step="1", action="Input", target="Project", name="directory"))
# project_directory = input(self.WIZARD_PROMPT)
# print(self.WIZARD_GUIDE.format(step="2", action="Input", target="Project", name="name"))
# project_name = input(self.WIZARD_PROMPT)
# print(self.WIZARD_GUIDE.format(step="3", action="Create", target="Project", name="files"))
# print(self.WIZARD_ECHO.format(path=fs.join(project_directory, project_name)))
# answer = input(self.WIZARD_CONFIRM)
# answer = "y"
# if answer == "Y" or answer == "y":
