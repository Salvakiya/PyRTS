__author__ = 'Salvakiya'
import configparser
import glob
import os
import Traits


def printred(string):
    print("\033[01;31m{0}\033[00m".format(string))


def printgrn(string):
    print("\033[1;36m{0}\033[00m".format(string))


def load_file_list(file, section, option, file_type):
    # Loads a list of files from a directory path in given ini
    config = configparser.RawConfigParser()
    config.read(file)
    file_list = []

    for count in range(20):  # I assume that you wont have more than 20 directories. because that stupid
        if config.has_option(section, option + str(count)):
            rules_dir_reference = config.get(section, option + str(count))
            directory = glob.glob(os.path.join(rules_dir_reference, "*"+file_type))
            file_list.extend(directory)
        else:
            break

    return file_list