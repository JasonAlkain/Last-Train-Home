# Text/UI accessibility tweaks: font size, contrast flags, and apply function.

style default:
    font "DejaVuSans.ttf"
    size 22
    color "#FFFFFF"
    line_leading 4

# Function to adjust font size
init python:    
    def set_font_size(size):
        """Set the global font size for the game."""
        style.default.size = size
        renpy.restart_interaction()
# Example usage in script:
# $ set_font_size(24)  # Increases font size to 24
# $ set_font_size(18)  # Decreases font size to 18

# Function to toggle high contrast mode
init python:
    high_contrast_mode = False

    def toggle_high_contrast():
        """Toggle high contrast mode for better visibility."""
        global high_contrast_mode
        high_contrast_mode = not high_contrast_mode
        if high_contrast_mode:
            style.default.color = "#FFFF00"  # Yellow text
            style.default.outline = (3, "#000000")  # Thicker black outline
        else:
            style.default.color = "#FFFFFF"  # Default white text
            style.default.outline = (2, "#000000")  # Default outline
        renpy.restart_interaction()
# Example usage in script:
# $ toggle_high_contrast()  # Toggles high contrast mode on/off

# Function to apply a custom function to the UI
init python:
    def apply_ui_function(func):
        """Apply a custom function to the UI."""
        func()
        renpy.restart_interaction()