# Holds global variables (default), affinity dict, flags, and helper functions.
# This file is automatically imported, so you don't need to import it yourself.

# Global Variables
default affinity = { "rin": 0, "sam": 0, "alex": 0, "stranger": 0 }
default truth_score = 0

default game_flags = {
    "met_alex": False,
    "met_sam": False,
    "met_rin": False,
    "met_stranger": False,
}


# Helper Functions
init python:    
    def change_affinity(name, amount):
        """Increase the affinity of a character by a specified amount."""
        if name in affinity:
            affinity[name] += amount
    
    def set_flag(flag_name, value=True):
        """Set a game flag to a specified value."""
        renpy.store.game_flags[flag_name] = value

    def get_flag(flag_name):
        """Get the value of a game flag."""
        return renpy.store.game_flags.get(flag_name, False)