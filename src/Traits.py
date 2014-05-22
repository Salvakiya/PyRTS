__author__ = "Salvakiya"


class General:
    def __init__(self, argument_list, owner):
        self.my_name = argument_list[0]
        self.my_owner = owner

class Buildable:
    def __init__(self, argument_list, owner):
        cost = argument_list[0]
        build_speed = argument_list[1]
        self.my_owner = owner