# Defines all Characters (MC, Alex, Sam, Rin, Stranger), name colors, and voice.

# =========================
# Main Characters
# =========================

define mc = Character(
    "MC", 
    color="#c8ffc8", 
    voice="voice/mc/"
)
define alex = Character(
    "Alex", 
    color="#ffc8c8", 
    voice="voice/alex/"
)
define sam = Character(
    "Sam", 
    color="#c8c8ff", 
    voice="voice/sam/"
)
define rin = Character(
    "Rin", 
    color="#ffffc8", 
    voice="voice/rin/"
)
define stranger = Character(
    "Stranger", 
    color="#ffc8ff", 
    voice="voice/stranger/"
)

# =========================
# Minor Characters
# =========================

# Train PA system / announcements
define pa = Character(
    "PA",
    who_color   = "#bbbbff",
    what_prefix = "\"",
    what_suffix = "\"",
)

# =========================
# Voice directories

# Default voice directory
define mc_voice = "voice/mc/"
define alex_voice = "voice/alex/"
define sam_voice = "voice/sam/"
define rin_voice = "voice/rin/"
define stranger_voice = "voice/stranger/"

# Example of how to play a voice line for a character
# play sound mc_voice + "line1.ogg"

