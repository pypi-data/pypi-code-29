import os
import re
import sys
import json
import datetime
from .settings import Settings
from .regex import dir_regex, check_duplicate
from tqdm import tqdm
from .color_print import BColors
from .main import DIRNAMES

class DirectoryCleaner(Settings):
    """
    Heart of the program. Pass in argparse object and add arguments directly to class.
    """
    def __init__(self, parser):
        """
        File names and full paths of those stored in this list.
        Tuple of names and paths. Uses the great scandir added to 3.5
        to get full paths.
        """
        self.files_info = []

        self.directory = ''
        self.main_folder_name = False
        self.folder_cleanup = False
        self.change_folder_names = False
        self.group_files = False
        self.revert_settings = False
        self.change_group_names = False
        self.args = self.register_args(parser)


    def run(self, args):
        """
        Starts program
        """
        self.set_vars(args)
        self.extensions = self.open_extensions()
        self.call_flags()
        self.open_dir()


    def register_args(self, parser):
        """
        All arguments for Directory Cleaner
        """
        parser.add_argument('path', type=str, nargs=1, help='The path to the directory that you want to cleanup not actually the word path. Ex. DirectoryCleaner /Users/Username/desktop')
        parser.add_argument('--folder_cleanup', '-fc', action='store_const', const=True, help='Set this flag if you want folders to also be included in the clean up.')
        parser.add_argument('--main_folder_name', '-mfn', action='store_const', const=True, help='Set this flag and specify the name you would like the main folder to be called. The date will always be apart of the name, only DirectoryCleaner will be changed.')
        parser.add_argument('--revert_settings', '-rs', action='store_const', const=True, help='Revert the settings file to its default state when the program was downloaded. Will use the default settings to run the program as well.')
        parser.add_argument('--group_files', '-gf', action='store_const', const=True, help='Set this flag if you would like to group commonly used files like Word Docs, Excel files, PDFs, music files etc. in folders named after the type of media they are.')
        parser.add_argument('--change_folder_names', '-cfn', action='store_const', const=True, help='Set this flag if you want to rename one of the default folder names Directory Cleaner uses for that type of file.')
        parser.add_argument('--change_group_names', '-cgn', action='store_const', const=True, help="Set this flag if you'd like to rename one of the default group names.")
        args = parser.parse_args()
        return args


    def open_dir(self):
        """
        Opens the directory the user specified. If file_names and full_paths are not empty
        this means that the user has already run this method, and thus they're only here
        because they entered the wrong path and arrived back here from double_check.
        If this is the case file_names and full_paths are emptied.
        """
        if len(self.files_info) > 0:
            self.files_info = []

        #If folder cleanup is not specified ignore folders.
        try:
            print("\n" + BColors.HEADER + "Opening files..." + BColors.ENDC)
            files = os.scandir(self.directory)
            print("\n" + BColors.OKGREEN + "Files succesfully opened." + BColors.ENDC)
            for file in files:
                if self.folder_cleanup:
                    if os.path.isdir(file):
                        file_tuple = (file.name, file.path, "folder")
                        self.files_info.append(file_tuple)
                    else:
                        file_tuple = (file.name, file.path, "file")
                        self.files_info.append(file_tuple)
                else:
                    if os.path.isdir(file):
                        pass
                    else:
                        file_tuple = (file.name, file.path, "file")
                        self.files_info.append(file_tuple)
        except FileNotFoundError:
                print("\n" + BColors.FAIL + "ERROR: The directory you entered could not be found." + BColors.ENDC)
                sys.exit(1)
        self.double_check()


    def call_flags(self):
        """
        This is a horrible implementation. Will most likely rework
        the flag variables to be stored in a dict and programmatically
        call these methods.
        """
        if self.revert_settings:
            self.default_settings()

        if self.change_folder_names:
            self.change_folder_name()

        if self.main_folder_name:
            self.change_main_folder()

        if self.change_group_names:
            self.change_group_name()


    def set_vars(self, args):
        """
        Sets cmdline vars passed in to instance variables.
        """
        self.directory = args.path[0]

        if args.folder_cleanup:
            self.folder_cleanup = True
        elif args.folder_cleanup == None:
            self.folder_cleanup = False

        if args.main_folder_name:
            self.main_folder_name = True
        elif args.main_folder_name == None:
            self.main_folder_name == False

        if args.change_folder_names:
            self.change_folder_names = True
        elif args.change_folder_names == None:
            self.change_folder_names == False

        if args.revert_settings:
            self.revert_settings = True
        elif args.revert_settings == None:
            self.revert_settings = False

        if args.change_group_names:
            self.change_group_names = True
        elif args.change_group_names == None:
            self.change_group_names = False

        if args.group_files:
            self.group_files = True
        elif args.group_files == None:
            self.group_files = False


    def double_check(self):
        """
        Presents a double check to the user on if the directory entered is the correct one
        and if they would like to change it.
        """
        print("\n\n" + BColors.OKBLUE + "Directory Cleaner is about to clean this directory. Are you sure " + BColors.ENDC + self.directory + BColors.OKBLUE + " is the directory you want cleaned? Here's a short preview of some of the files in this directory..." + BColors.ENDC)
        print("----------------------------------------")
        if len(self.files_info) < 20:
            for file in self.files_info:
                print(f"{file[0]}")
        else:
            for i in range(20):
                print(f"{self.files_info[i][0]}")
        print("----------------------------------------")

        while True:
            print(BColors.OKBLUE + "Enter 'yes' or 'y' if this is correct else enter 'no' or 'n' if it is not: " + BColors.ENDC, end="")
            response = input()
            response = response.strip()
            if response in Settings.ANSWERS["yes"]:
                return
            elif response in Settings.ANSWERS["no"]:
                print("\n" + BColors.OKBLUE + "Please enter the new path of the directory you would like to be cleaned: " + BColors.ENDC, end="")
                new_dir = input()
                self.directory = new_dir.strip()
                self.open_dir()
                return
            else:
                print("\n" + BColors.FAIL + "ERROR: The input received was not a valid option. Please read the options again." + BColors.ENDC)


    # def grouping(self, file):



    def open_extensions(self):
        """
        Load extensions into dict from JSON file. File is generated from
        scraper.py. If you ever want to go back to the default settings simply
        use the command --revertsettings or -rs.
        """
        try:
            print("\n" + BColors.HEADER + "Opening settings." + BColors.ENDC)
            with open(DIRNAMES["data"], "r") as f:
                extensions = json.load(f)
        except FileNotFoundError:
            print("Data file could not be located. Please make sure 'extensions.json' is in the 'Data' directory.")
            sys.exit(1)
        print("\n" + BColors.OKGREEN + "Settings succesfully opened." + BColors.ENDC)
        return extensions


    def check_extensions(self):
        """
        Checks file extensions for the directory specified and will place them in
        lists depending on if the file type can be identified. Then calls make_dirs to actually do the
        work. Huge thanks to https://www.online-convert.com/file-type as this is where the file extensions
        data came from.
        """
        results = {
                    "total": 0,
                    "success": [],
                    "success_percent": 0,
                    "error": [],
                    "error_percent": 0
                 }

        for file in self.files_info:
                try:
                    if file[2] == "folder":
                        results["success"].append(file)
                        results["total"] += 1
                    elif file[2] == "file":
                        pos = file[0].rfind(".")
                        extension = file[0][pos + 1:]
                        if extension in self.extensions["extensions"]:
                            results["success"].append(file)
                            results["total"] += 1
                        else:
                            results["error"].append(file)
                            results["total"] += 1
                except:
                    results["error"].append(file)

        results["success_percent"] = len(results["success"]) / results["total"] * 100.00
        results["error_percent"] = len(results["error"]) / results["total"] * 100.00
        self.final_output(results)
        self.make_dirs(results)


    def make_dirs(self, results):
        """
        Will make all the required folders to store the files in the directory, will make
        a 'Folders' folder depending on the corresponding folder_cleanup flag passed in.
        """
        i = 1
        final_paths = []
        new_dir = ""
        main_folder = self.extensions["main_folder_name"] + "(" + str(datetime.date.today()) + ")"
        dir_cleaner_folder = os.path.join(self.directory, main_folder)

        try:
            os.makedirs(dir_cleaner_folder)
        except FileExistsError:
            main_folder = check_duplicate(main_folder, self.directory)
            print(main_folder)
            dir_cleaner_folder = os.path.join(self.directory, main_folder)
            os.makedirs(dir_cleaner_folder)

        for file in tqdm(results["success"], total=len(results["success"])):
            pos = file[0].rfind(".")
            extension = file[0][pos + 1:]
            if file[2] == "folder":
                new_dir = os.path.join(dir_cleaner_folder, "Folders")
            elif file[2] == "file":
                if self.group_files:
                    for group in self.extensions["groups"]:
                        if extension in self.extensions["groups"][group]["group_items"]:
                            new_dir = os.path.join(dir_cleaner_folder, self.extensions["groups"][group]["name"])
                            break
                        else:
                            new_dir = os.path.join(dir_cleaner_folder, self.extensions["extensions"][extension]) #new_dir = directorycleaner(2018 blah blah)/(png)Portable Network Graphics
                else:
                    new_dir = os.path.join(dir_cleaner_folder, self.extensions["extensions"][extension])
            try:
                old_location = os.path.join(self.directory, file[0])
                new_location = os.path.join(new_dir, file[0])
                locations = (old_location, new_location)
                os.makedirs(new_dir)
                os.rename(old_location, new_location)
                final_paths.append(locations)
            except FileExistsError:
                locations = (old_location, new_location)
                final_paths.append(locations)
                os.rename(old_location, new_location)

        new_dir = os.path.join(dir_cleaner_folder, self.extensions["unknowns_folder_name"])
        for file in results["error"]:
            try:
                old_location = os.path.join(self.directory, file[0])
                new_location = os.path.join(new_dir, file[0])
                locations = (old_location, new_location)
                os.makedirs(new_dir)
                os.rename(old_location, new_location)
                final_paths.append(locations)
            except FileExistsError:
                locations = (old_location, new_location)
                final_paths.append(locations)
                os.rename(old_location, new_location)

        txt = self.extensions["txt_file_name"] + "(" + str(datetime.date.today()) + ").txt"
        txt = check_duplicate(txt, self.directory)

        with open(os.path.join(self.directory, txt), "w") as f:
            for elem in final_paths:
                f.write(f"\nOriginal Location: {elem[0]}\nNew Location: {elem[1]}\n")

        print("\n" + BColors.OKGREEN + f"Finished cleaning directory. A text file named {txt} has been generated in the directory showing where all your files ended up." + BColors.ENDC)


    def final_output(self, results):
        print("""\nFile type checking complete

Results:
----------

% Success: {0:.1f}

% Error: {1:.1f}
""".format(results["success_percent"], results["error_percent"]))
