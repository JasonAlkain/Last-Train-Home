# Story script for Chapter 1 - Rin route (friendship + lost potential).
# This file is called from routes.rpy via label chapter1.

label chapter1:

    # Mark that we've met Rin in this run.
    $ set_flag("met_rin", True)

    # We assume we are already on the train from the prologue,
    # but we re-establish the scene just in case.
    scene bg train_interior
    with fade

    play music "sfx_train_hum.ogg" loop

    "The doors hiss open beside me. Cold air brushes across my face."

    "Out on the platform, the figure from before steps into the car."

    show rin neutral at center

    "Hood down. Headphones around his neck. Same posture I remember, like the whole world is just background noise."

    rin "Whoa."

    show rin happy

    rin "Okay, this is either the weirdest dream I've ever had..."
    rin "...or the universe finally figured out how to make a joke."

    rin "Hey, stranger."

    ########################################
    # CHOICE 1 – FIRST GREETING / TONE
    ########################################

    
    menu:
        "How should I greet Rin?"
        "Genuinely happy to see him.":
            $ change_affinity("rin", 1)
            $ truth_score += 1
            mc "Rin? ...Wow. It's really you."
            show rin happy
            rin "Damn right it's me."
            rin "You look like you just sprinted through three timelines to get here."
        "Deflect with a joke.":
            $ change_affinity("rin", 1)
            mc "Huh. I see the city still hasn't kicked you off the night shift."
            show rin happy
            rin "Please. Night shift is where all the decent stories live."
            rin "Day shift is for people who enjoy email."
        "Keep your distance.":
            $ change_affinity("rin", -1)
            mc "...Hey."
            show rin neutral
            rin "Wow. Don't sound too excited or anything."
            rin "Good to know I still have that effect on people."

    "He drops into the seat across from me like it's the most natural thing in the world."

    show rin happy

    rin "You still ride this line? Or did I just stumble into some very elaborate nostalgia trip?"

    "Outside the window, the station slides away. Tunnel darkness rises up to swallow us again."

    ########################################
    # CHOICE 2 – NOSTALGIA / WHAT YOU ADMIT
    ########################################

    rin "Remember when we used to take this all the way to the end, just because we could?"
    rin "Missed last trains, cheap coffee, terrible decisions..."

    menu:
        "What memory should I lean into?"
        "The band you planned together.":
            $ change_affinity("rin", 1)
            $ truth_score += 1
            mc "I remember us arguing over band names all the way out there."
            mc "You swore 'Midnight Static' was genius."
            show rin happy
            rin "It {i}is{/i} genius."
            rin "You just had tragically mainstream taste."
        "The dumb late-night diner adventures.":
            $ change_affinity("rin", 1)
            mc "I remember you trying to rate every late-night diner along this line."
            mc "You nearly got us banned from at least three."
            show rin happy
            rin "Look, somebody had to document the 2 a.m. grilled cheese situation."
            rin "Historical record. Very important."
        "Downplay it all as wasted time.":
            $ change_affinity("rin", -1)
            mc "I remember us wasting a lot of time on trains when we should've been doing literally anything else."
            show rin hurt
            rin "Wow. Okay."
            rin "Remind me not to ask for a Yelp review of our entire friendship."

    "His laughter hangs between us for a moment, soft and familiar."

    "The train rocks gently. Lights flicker along the ceiling."

    "Then, slowly, his smile fades."

    show rin serious

    ########################################
    # ACCUSATION – YOU BAILED
    ########################################

    rin "You know what I keep coming back to?"

    "He leans forward, elbows on his knees, eyes fixed on me."

    rin "You just... stopped showing up."

    rin "No \"I'm alive, I'm a mess.\" No \"I need to disappear for a bit.\""
    rin "Nothing. One day you were there, and then you weren't."

    "My grip tightens on the pole again."

    "We ride the silence for a few seconds. The blurred silhouettes farther down the car never look up."

    ########################################
    # CHOICE 3 – WHY YOU DISAPPEARED
    ########################################

    menu:
        "Why did you bail on Rin?"
        "Admit you were scared and ran.":
            $ change_affinity("rin", 1)
            $ truth_score += 1
            mc "I was scared."
            mc "Of failing. Of you seeing how much of a mess I was."
            mc "So I did what I always do."
            mc "I ran."
            show rin hurt
            rin "You could've just said that, you know."
            rin "I wouldn't have magically fixed you, but at least I would've known where you went."
        "Say you would've dragged him down.":
            $ change_affinity("rin", 1)
            mc "I was in a bad place. Everything I touched felt like it was falling apart."
            mc "I thought if I stuck around, I'd just drag you down with me."
            show rin serious
            rin "You decided that for me."
            rin "That's kind of the problem."
            rin "You turned me into some fragile side character in your disaster arc."
        "Deflect it as 'life happens'.":
            $ change_affinity("rin", -1)
            mc "Life happened. People drift. We weren't kids anymore."
            show rin hurt
            rin "Yeah. People drift."
            rin "It's just wild how fast {i}you{/i} managed it."

    "The hum of the train feels louder now. The clock above us still glows the same dead time."

    "23:17."

    "It hasn't moved."

    show rin serious

    rin "I kept waiting, you know."
    rin "First for a text. Then for some kind of explanation."
    rin "Then I started pretending you were dead because it was less embarrassing than admitting you just ghosted."

    "The word lands heavier than it should."

    "Ghosted."

    "I swallow against the dry sting in my throat."

    "Outside, the tunnel begins to brighten. Another station is coming up."

    ########################################
    # RIN’S REACTION – SHADED BY AFFINITY
    ########################################

    play sound "sfx_chime.ogg"

    rin "Guess this is my stop."

    "He straightens, rolling his shoulders like he's shrugging off something heavy."

    if affinity["rin"] >= 2:
        show rin happy
        rin "You know what? I'm... weirdly glad I ran into you."
        rin "It sucked, what you did. Still does."
        rin "But at least now I don't have to keep rewriting the story in my head."
        rin "Maybe I'll finally do some of that stuff we talked about."
        rin "With or without you."
    elif affinity["rin"] <= -1:
        show rin hurt
        rin "I don't know what I expected from this."
        rin "Some big explanation, I guess. Some line that would make it all add up."
        rin "But I think all I got is confirmation."
        rin "You left. That's who you were. Maybe that's who you still are."
    else:
        show rin serious
        rin "I don't know if this helped."
        rin "But it feels... different than the arguments I've had with you in my head."
        rin "That's something, I guess."

    "The train slows. The world outside resolves into another late-night platform."
    
    # scene bg platform_ext
    # with dissolve

    show rin neutral at center

    "The doors open with a tired hiss. Cold air spills in around him."

    rin "Take care of yourself, yeah?"

    if affinity["rin"] >= 2:
        show rin happy
        rin "And try not to vanish on the next person who believes you when you say you'll be there."
    elif affinity["rin"] <= -1:
        show rin hurt
        rin "If you do this again to someone else..."
        rin "At least know what you did to me."

    hide rin
    with dissolve

    "He steps out onto the platform and is gone, swallowed by silhouettes and neon and fog."


    ########################################
    # STRANGER’S BUTTON – HINT AT IMPACT
    ########################################

    # scene bg train_interior
    # with dissolve

    show stranger neutral at right

    "When I look back, the far end of the car is empty again."

    "Except for the stranger."

    stranger "He's going to be okay."

    mc "You sound sure."

    show stranger amused

    stranger "People who get to actually say the things they've been rehearsing for years?"
    stranger "They tend to move a little easier afterward."

    show stranger neutral

    stranger "Even if they wake up and tell themselves it was just a dream."

    "A glitch of an image flickers in my mind—Rin in a small room somewhere, guitar in hand, the city light bleeding in through cheap curtains."

    "He looks tired. But... lighter."

    "The vision fades with the next sway of the train."

    stranger "Next stop."

    show stranger neutral

    stranger "You ready for another ghost?"

    "The clock still reads 23:17."

    "The train rolls on."

    stop music fadeout 1.0

    # End of Chapter 1 – return control to routes.rpy
    return
