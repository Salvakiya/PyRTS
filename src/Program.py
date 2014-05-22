__author__ = 'Salvakiya'
import configparser
import glob
import os
import traitfile


def printred(string):
    print("\033[01;31m{0}\033[00m".format(string))


def printgrn(string):
    print("\033[1;36m{0}\033[00m".format(string))


blue_print_instances = {}
actor_instances =   {}

#retrieve which mod we are currently using
config = configparser.RawConfigParser()
if os.path.isfile("Settings.ini"):
    config.read("Settings.ini")
    GAME_MOD = config.get("Options", "mod")
else:
    printred("Cannot find Settings.ini!")


#load a list of files of given type from Assets.txt
def load_file_list(file_type):

    path = "mods/"+GAME_MOD+"/"
    file_object = open(path+"Assets.txt", 'r')
    directory_list = []

    for directory in file_object.readlines():
        append_path = path+directory.rstrip('\n')
        if not directory.startswith("#") and os.path.isdir(append_path):
            directory_list.append(append_path)

    file_list = []
    for directory in directory_list:
        printgrn(directory+"/*"+file_type)
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
                printgrn("Loading: "+name)
                trait_list = []
                for trait in config.sections():
                    if hasattr(traitfile, trait):
                        templates[name] = trait_list.append(trait)
                        printgrn("Trait "+trait+" loaded!")
                    else:
                        printred("Trait "+trait+" does not exist?")


                templates[name] = BluePrintClass(templates)
                printgrn(name+": Complete!")
            else:
                printred("Error, Missing General Trait For "+file)

        print(actor_file_list)
        return templates


class AssetLoader():
    def __init__(self):
        template_list = load_assets()
        printgrn(template_list)


class BluePrintClass:
    def __init__(self, trait_list):
        return



AssetLoader()