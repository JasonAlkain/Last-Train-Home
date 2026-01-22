# script_prologue.rpy
# Prologue: "Last Service"

define flash = Fade(0.1, 0.0, 0.5, color="#fff")


label prologue:
    $ mc = renpy.input("What is your name?", length=32)
    $ mc = mc.strip()
    ########################################
    # Cold open – running / blurred streets
    ########################################

    scene bg streets_blur
    with fade

    play sound "sfx_footsteps_run.ogg"

    "I don’t remember when I started running."

    "I just know my lungs burn and my legs ache, shoes slapping wet concrete as the night smears into streaks of light and shadow."

    "Headlights flare at the edge of my memory."

    play sound "sfx_car_screech.ogg"

    scene black
    with flash

    "Screeching metal. A flash of white. A shout—"

    "Then it’s gone."

    "The subway entrance yawns ahead of me, a mouth of tile and flickering fluorescent light. I throw myself toward it, one hand catching the rail as I swing around the turn and pound down the stairs."

    stop sound fadeout 1.0

    "My heartbeat is louder than my footsteps."

    "Last train."

    "I don’t know how I know that. The thought just… arrives, fully formed."

    "Last train. Last chance."

    ########################################
    # Platform and doors – outside → inside
    ########################################

    scene bg platform_ext
    with dissolve

    play sound "sfx_turnstile.ogg"

    "The turnstile jerks against my hip as I shove through. I nearly trip, catch myself on cold metal, vision swimming white, then black, then—"

    "The platform snaps into focus."

    "The train is already here."

    "Carriage doors stand open in front of me, the yellow line at my feet a bright, accusing stripe. A few shapes move inside the car. Dark coats. Slumped shoulders. No faces. Just… suggestions of people."

    play sound "sfx_chime.ogg"

    "{i}Doors closing.{/i}"

    "My body moves before my brain can catch up. I lunge, hand outstretched, fingers splayed—"

    play sound "sfx_door_hit.ogg"

    "For one frozen instant I see my own hand under the harsh platform lights, skin pale, veins raised. Then—"

    ########################################
    # Impact flash – abstract accident hint
    ########################################

    scene bg streets_blur
    with flash

    play sound "sfx_car_screech.ogg"

    "Headlights roar out of the dark, too bright, too close."

    "Rubber screams against wet asphalt. Weightlessness, the world tilting sideways."

    "A cracked phone screen tumbles through the air and shatters against pavement, notifications trying to crawl through a spiderweb of glass."

    "Somebody shouts" "“Stay with us!”"

    "Another voice"  "“Don’t move him—”"

    stop sound fadeout 1.0

    ########################################
    # Cut to interior – train / clock / hum
    ########################################

    scene bg train_interior
    with flash

    play sound "sfx_train_hum.ogg" loop

    "Then I’m inside the train."

    "I’m sitting. I don’t remember sitting down, but my body is folded into a seat, knees bent, feet planted on the speckled floor."

    "The hum of the train buzzes under everything, a low vibration threaded through my bones."

    "My hands are the first things I recognize."

    "They’re wrapped around a cold metal pole in front of me, knuckles white, fingers shaking."

    "There’s a faint smear of something dark along my thumb. Dirt. Oil. Blood?"

    "I blink, and it isn’t there anymore."

    "The car is too quiet. Too empty."

    "A handful of passengers are scattered through the seats, but they’re blurred at the edges, like someone forgot to finish drawing them. Heads bowed. Faces lost in shadow. They move, if they move at all, in small looping motions that never quite look human."

    "Above them, an old digital clock glows a dull, sickly orange."

    "Clock" "23:17"

    "I stare at it."

    "It doesn’t tick."

    "No seconds. No blinking colon. Just that dead time, hanging over the car like a held breath."

    "My chest tightens."

    "*What…?*"

    ########################################
    # PA announcement – last service
    ########################################

    play sound "sfx_pa_crackle.ogg"

    pa "Last service to—"

    "The speakers dissolve into static, then cut back in, too clear."

    pa "End of the line. No returns. No transfers."

    "I’m not sure I heard that right."

    "I drag in a slow breath and try to steady my hands. The pole is real. The seat is real. The sway of the car is real."

    "The rest of it… I’m not so sure about."

    "I try to remember the street. The rain. The phone. The impact."

    "A hospital hallway floats up in my mind’s eye—cheap chairs, bright doors at the far end, a vending machine humming to itself."

    "The image shudders and breaks apart."

    ########################################
    # Empty seat → Stranger pops in
    ########################################

    "My gaze drifts down the car."

    "At the far end, there’s an empty row of seats. The cushions are tired and patched, overhead lights buzzing faintly."

    "Something about that spot feels… magnetized. Wrong and familiar at the same time."

    "The lights flicker."

    # Empty seat (no character shown yet).
    "For a heartbeat, the row is completely empty."

    with vpunch

    # Stranger appears with no transition.
    show stranger neutral at center

    "Then there’s someone sitting there."

    "No footsteps. No door sound. Just empty, then occupied, like a jump cut."

    "Unlike everyone else in the car, they’re in perfect focus."

    "They sit with one leg crossed over the other, hands resting lightly on a metal thermos and a battered paperback. Dark coat. Neutral scarf. No logos. Nothing to pin down."

    "Their eyes meet mine."

    ########################################
    # First conversation with Stranger
    ########################################

    stranger "Easy."

    "Their voice is warm and smooth, like it doesn’t belong under fluorescent lights."

    stranger "You almost didn’t make it."

    "My mouth is dry."

    mc "I… what?"

    "They tilt their head, considering me like a painting they’ve seen a thousand times and still haven’t decided on."

    stranger "You’re out of breath."

    stranger "Most people are, when they get here."

    "I look down at my hands again, at the way I’m still strangling the pole. My chest aches, like my ribs are bruised from the inside."

    mc "What is this? Where… is this?"

    "The train begins to slow, brakes whining softly. Outside the window, darkness gives way to streaks of light and the blurred geometry of another station."

    "The stray thought comes back, uninvited:"

    "Last train."

    stranger "This?"

    "They glance around the empty car, like it’s nothing special."

    stranger "This is the last train."

    mc "The… last train."

    play sound "sfx_chime.ogg"

    "Another chime. We’re pulling into the station."

    stranger "You caught it."

    stranger "Barely. Most don’t."

    ########################################
    # Hint of Rin on the platform
    ########################################

    "Through the window on the carriage doors ahead, a lone figure stands near the platform edge."
    # TODO: Update stanger looks as needed once art is finalized.
    "Hood up. Headphones around his neck. Foot tapping to music only he can hear."

    "Something in my chest tightens. I know that posture."

    "The stranger follows my gaze. Their eyes narrow just a fraction, like they’re checking something off in an invisible ledger."

    stranger "Looks like you’ve got company."

    stranger "Might be a good time to catch your breath."

    "The train shudders to a stop."

    "The clock above my head still says 23:17."

    play sound "sfx_door_open.ogg"

    "The doors hiss open. Cold air pours into the car."

    "Out on the platform, the figure turns just enough for me to see his face—"

    "—and my stomach drops with recognition."

    "The stranger leans back, book resting on their knee, expression unreadable."

    stranger "Next stop… old ghosts."

    "The lights flicker once."

    stop sound fadeout 1.0

    # End of prologue
    return
