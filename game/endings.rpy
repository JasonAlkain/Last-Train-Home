# Final “terminal” scene, player’s last choice, and ending label(s).

label ending_scene:
    # Content for the ending scene goes here
    # get total affinity
    $ total_affinity = get_affinity("rin") + get_affinity("sam") + get_affinity("alex")
    if total_affinity >= 15:
        jump good_ending
    elif total_affinity <= 5:
        jump bad_ending
    else:
        jump neutral_ending

    return

# Example of multiple endings based on affinity

label good_ending:
    # Content for the good ending goes here
    return

label bad_ending:
    # Content for the bad ending goes here
    return

label neutral_ending:
    # Content for the neutral ending goes here
    return

label epilogue:
    # Content for the epilogue goes here
    return



