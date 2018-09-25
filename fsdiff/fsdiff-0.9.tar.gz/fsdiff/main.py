# Copyright (C) 2018 Ioannis Valasakis <code@wizofe.uk>
# Licensed under the GNU GPL-3
# The GNU Public License can be found in `/usr/share/common-licenses/GPL-3'.

import os
import sys
import time
import filecmp
from filecmp import dircmp
import os.path
import shutil
from subprocess import Popen, PIPE

import ctypes
from ctypes import cdll
from ctypes.util import find_library
from colorama import init, Fore, Back, Style

# TODO: Convert to dictionary {img, noobs} + {root, boot} mapping to the partitions
ROOT_MP = 'img/root'
BOOT_MP = 'img/boot'
BOOT_SUFFIX = 'p1'
ROOT_SUFFIX = 'p2'

ROOT_NB_MP = 'noobs/root'
BOOT_NB_MP = 'noobs/boot'
BOOT_NB_SUFFIX = 'p6'
ROOT_NB_SUFFIX = 'p7'


def load_c_library():
    """
    Loads the libc from the system to use for different calls
    like mount, et
    """
    try:
        libc_name = find_library('c')
        libc = cdll.LoadLibrary(libc_name)
        return libc
    except:
        print('Unable to load libc.')


def cmount(source, target, fs, options=''):
    """ A mount interface of the sys/mount.h from the Standard C Library
    :param source the filesystem to be attached. a path to an img, dir or a device
    :param target (pathname) the location where the source would be attached to
    :param fs the filesystem type supported by the kernel
    :param options extra options supported by the OS
    :returns 0 for Pass, -1 for Failure and sets the appropriate errno
    """
    libc = load_c_library()
    libc.mount.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_ulong, ctypes.c_char_p)

    ret = libc.mount(source, target, fs, 0, options)
    if ret < 0:
        errno = ctypes.get_errno()
        raise OSError(errno, "Error mounting {} ({}) on {} with options '{}': {}".
                      format(source, fs, target, options, os.strerror(errno)))


def mount_image(img):
    """
    Mounts a system image using loopback devices
    :param img: the image file to mount (noobs)
    :return: the location of the root, mount mountpoint and the loop device name
    """
    try:
        device_name = Popen(["sudo", "kpartx", "-vas", img],
                            stdout=PIPE).communicate()[0].split()[2][:-2].decode('utf-8')
        os.makedirs(ROOT_MP)
        os.makedirs(BOOT_MP)

        Popen(["sudo", "mount", "/dev/mapper/{}{}".format(device_name, ROOT_SUFFIX), ROOT_MP], stdout=PIPE)
        Popen(["sudo", "mount", "/dev/mapper/{}{}".format(device_name, BOOT_SUFFIX), BOOT_MP], stdout=PIPE)

        return ROOT_MP, BOOT_MP, device_name
    except:
        raise


def mount_noobs(img):
    """
    Mounts a NOOBS image using loopback devices
    :param img: the image file to mount (noobs)
    :return: the location of the root, mount mountpoint and the loop device name
    """
    try:
        device_name = Popen(["sudo", "kpartx", "-vas", img],
                            stdout=PIPE).communicate()[0].split()[2][:-2].decode('utf-8')
        os.makedirs(ROOT_NB_MP)
        os.makedirs(BOOT_NB_MP)

        Popen(["sudo", "mount", "/dev/mapper/{}{}".format(device_name, ROOT_NB_SUFFIX), ROOT_NB_MP], stdout=PIPE)
        Popen(["sudo", "mount", "/dev/mapper/{}{}".format(device_name, BOOT_NB_SUFFIX), BOOT_NB_MP], stdout=PIPE)

        return ROOT_NB_MP, BOOT_NB_MP, device_name
    except:
        raise


def unmount_image(path, device_name, noobs=False):
    """
    Unmounts an image (support both NOOBS and dd'ed images)
    :param device_name: The system device to unmount
    :param path: The image to be unmounted
    :rtype: True for success, False otherwise
    """
    try:
        # Unmount the directories
        Popen(["sudo", "umount", "-fd", BOOT_MP, ROOT_MP], stdout=PIPE) if noobs == False else Popen(
            ["sudo", "umount", "-fd", ROOT_NB_MP, BOOT_NB_MP], stdout=PIPE)
        # Remove the folders
        # TODO: Please make a dictionary and use it
        shutil.rmtree('img')
        shutil.rmtree('noobs')
        # Remove the loop mounts
        Popen(["sudo", "kpartx", "-vd", path], stdout=PIPE)
        Popen(["sudo", "dmsetup", "remove", "-f", "/dev/mapper/{}*".format(device_name)], stdout=PIPE)
        Popen(["sudo", "losetup", "-d", "/dev/{}".format(device_name)], stdout=PIPE)
        return True
    except:
        print("E: Can't unmount the loopback device: {}".format(device_name))
        return False


# class dircmp(filecmp.dircmp):
#     """ Comparison between contents of the files of dir1 and dir2 within the same path.
#     """

#     def phase3(self):
#         """
#             Discover the differences between common files and ensure that
#             we are using content comparison with shallow=False in contrast
#             with the original compare phase3 implementation.

#             It does an in depth comparison of contents and doesn't rely only on os.stat() attributes

#             Refer to Lib/filecmp.py of cpython
#             """
#         fcomp = filecmp.cmpfiles(self.left, self.right, self.common_files,
#                                  shallow=False)
#         self.same_files, self.diff_files, self.funny_files = fcomp


def get_files(rootdir):
    """
    Get the files by 'walking' recursively beginning on the rootdir
    :param rootdir: the base dir; starting point
    :return: the pathname for each of the files (minus the prefix)
    """
    for rootname, dirs, files in os.walk(rootdir):
        for file in files:
            path = os.path.join(rootname, file)
            yield path[len(rootdir):]


def is_same(path1, path2, verbose=False):
    """
    Compare the content of the two directory trees.
    :param path1: Left path to compare from
    :param path2: Right path to compare with
    :rtype True is they are the same or False if they differ
    """
    # Clear the file structure cache
    filecmp.clear_cache()
    compared = dircmp(path1, path2)

        # vbpath1 = set(get_files(path1))
        # vbpath2 = set(get_files(path2))
        # one_missing = vbpath2 - vbpath1
        # two_missing = vbpath1 - vbpath2

        # print('Only in {}: {} \n'.format(path2, one_missing))
        # print('Only in {}: {} \n'.format(path1, two_missing))

    if (compared.left_only or compared.right_only or compared.diff_files
        or compared.funny_files):
        # Displays a summary report if differences are found
        if verbose:
            compared.report_partial_closure()
            return False
        else:
            print('Files that differ: {}\n'.format(compared.diff_files))
            print('Files only in {}: {}\n'.format(path1, compared.left_only))
            print('Files only in {}: {}\n'.format(path2, compared.right_only))
            return False
    for subdir in compared.common_dirs:
        if not is_same(os.path.join(path1, subdir), os.path.join(path2, subdir)):
            return False
        return True


def colorp(text, foreground="black", background="white"):
    """
    :param text: the string to display to stdout
    :param foreground: color
    :param background: color
    :return:
    """
    init()  # initialize colorama
    fground = foreground.upper()
    bground = background.upper()
    style = getattr(Fore, fground) + getattr(Back, bground)
    print(style + text + Style.RESET_ALL)


def is_same_display(from_loc, to_loc, verbose):
    ret = is_same(from_loc, to_loc, verbose)
    colorp("LOCATIONS {} and {} are the SAME!".format(from_loc, to_loc) if ret else "LOCATIONS DIFFER",
           "green" if ret else "red",
           "white")
    return ret


def main(from_loc, to_loc, image, extract, verbose):
    """
    The simplest user case by calling is_same()
    :param image: Boolean value; Sets an image as argument
    :param extract: Extracts a compressed image
    :param from_loc: the left side path to compare from
    :param to_loc: the right side path to compare with
    :rtype: True if they are the same, False otherwise
    """

    # Ensure that the user is root
    if os.geteuid() is not 0:
        print("E: Getting the required privileges, are you root?")
        sys.exit(1)

        # if there are images extract (if needed) and mount them
    if image:
        if extract:
            # do the gunzip here, store the file names and mount
            print('E: Currently not supported.')
            sys.exit(1)
        else:
            # store the file name and mount
            # TODO: Currently from is a normal image and to is a NOOBS one
            from_boot, from_root, img_device = mount_image(from_loc)
            to_boot, to_root, noobs_device = mount_noobs(to_loc)

            # The delay is because there is a race condition that affects the loop files
            # as don't exist immediately after created from kpartx
            # see: https://github.com/mozilla-iot/wiki/blob/master/tools/mount-img.sh
            time.sleep(1)

            is_same_display(from_boot, to_boot, verbose)
            is_same_display(from_root, to_root, verbose)

            time.sleep(0.5)
            unmount_image(from_loc, img_device)
            time.sleep(0.5)
            unmount_image(to_loc, noobs_device, noobs=True)
            sys.exit(0)
    else:
        # and that directories/image files exist
        if not os.path.exists(from_loc) or not os.path.exists(to_loc):
            print("E: Can't find locations, misspelled?")
            sys.exit(1)

        is_same_display(from_loc, to_loc, verbose)
        sys.exit(0)

