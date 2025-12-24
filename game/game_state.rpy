"""
Holds global variables (default), affinity dict, flags, and helper functions.
This file is automatically imported, so you don't need to import it yourself.
"""
# Global Variables
default mc_affinity = 0
default alex_affinity = 0
default sam_affinity = 0
default rin_affinity = 0
default stranger_affinity = 0

default game_flags = {
    "met_alex": False,
    "met_sam": False,
    "met_rin": False,
    "met_stranger": False,
}

# Helper Functions
init python:
    def increase_affinity(character, amount):
        """Increase the affinity of a character by a specified amount."""
        global_vars = renpy.store
        if character == "mc":
            global_vars.mc_affinity += amount
        elif character == "alex":
            global_vars.alex_affinity += amount
        elif character == "sam":
            global_vars.sam_affinity += amount
        elif character == "rin":
            global_vars.rin_affinity += amount
        elif character == "stranger":
            global_vars.stranger_affinity += amount

    def set_flag(flag_name, value=True):
        """Set a game flag to a specified value."""
        renpy.store.game_flags[flag_name] = value

    def get_flag(flag_name):
        """Get the value of a game flag."""
        return renpy.store.game_flags.get(flag_name, False)