__author__ = 'Salvakiya'
import configparser
import glob
import os
import traitfile


def printcol(col, string):
    print( {"r": "\033[01;31m{0}\033[00m",
            "y": "\033[1;33m{0}\033[00m",
            "g": "\033[1;36m{0}\033[00m"}[col].format(string))


blue_print_instances = {}
actor_instances =   {}

#retrieve which mod we are currently using
config = configparser.RawConfigParser()
if os.path.isfile("settings.ini"):
    config.read("settings.ini")
    GAME_MOD = config.get("Options", "mod")
else:
    printcol("r", "Cannot find settings.ini!")


#load a list of files of given type from assets.txt
def load_file_list(file_type):

    path = "mods/"+GAME_MOD+"/"
    file_object = open(path+"assets.txt", 'r')
    directory_list = []

    for directory in file_object.readlines():
        append_path = path+directory.rstrip('\n')
        if not directory.startswith("#") and os.path.isdir(append_path):
            directory_list.append(append_path)

    file_list = []
    for directory in directory_list:
        printcol("g", directory+"/*"+file_type)
        files = glob.glob(directory+"/*"+file_type)
        file_list.extend(files)

    return file_list


def load_assets():
        actor_file_list = load_file_list(".ini")
        templates = {}
        for file in actor_file_list:
            config = configparser.RawConfigParser()
            config.read(file)
            if config.has_option("General", "Name"):

                name = config.get("General", "Name")
                printcol("g","Loading: "+name)
                trait_list = []
                for trait in config.sections():
                    if hasattr(traitfile, trait):
                        templates[name] = trait_list.append(trait)
                        printcol("g","Trait "+trait+" loaded!")
                    else:
                        printcol("y","Trait "+trait+" does not exist?")


                templates[name] = BluePrintClass(templates)
                printcol("g", name+": Complete!")
            else:
                printcol("r", "Error, Missing General Trait For "+file)
        return templates


class AssetLoader():
    def __init__(self):
        template_list = load_assets()
        printcol("g", template_list)


class BluePrintClass:
    def __init__(self, trait_list):
        return



AssetLoader()
