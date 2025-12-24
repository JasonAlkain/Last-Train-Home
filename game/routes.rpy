"""
High-level flow: start, prologue, and calls to each chapter + epilogue.
This file defines the overall structure of the game.
Each chapter is defined in its own file (e.g., chapter1.rpy).
This file is automatically imported, so you don't need to import it yourself.
"""


label rt_start:
    # Call the prologue
    call prologue
    return
    # Call each chapter in sequence
    call chapter1
    call chapter2
    call chapter3

    # Call the epilogue
    call epilogue

    # End the game
    return

