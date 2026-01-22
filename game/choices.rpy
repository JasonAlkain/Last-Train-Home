# Small helpers for logging choices and adjusting affinity in one place.

init python:
    def log_choice(choice_text):
        """Log the player's choice for debugging or tracking purposes."""
        renpy.log("Player chose: {}".format(choice_text))
    def adjust_affinity_and_log(character, amount, choice_text):
        """Adjust affinity for a character and log the choice made."""
        increase_affinity(character, amount)
        log_choice(choice_text)

# Example usage in a choice menu:
# menu:
#     "Help Alex with her project.":
#         $ adjust_affinity_and_log("alex", 10, "Helped Alex with her project.")
