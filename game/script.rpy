











init:
    $ tbed = False
    $ ned = False







define na = Character("Narrator", color="#FFC34A")
define mc = Character("[player_name]", color="#00A82D")
define sur = Character("[surname]", color="#00A82D")
define mcd = Character("[mc]")
define car = Character("caretaker")
define grc = Character("Gracie", color="#2EE087")
define mad = Character("[maddison_name]", color="#AF33E1")
define mnick = Character("[mad_nick]", color="#AF33E1")
define ali = Character("[allison_name]", color="#E864A4")
define anick = Character("[ali_nick]", color="#E864A4")
define liv = Character("[olivia_name]", color="#2EE087")
define onick = Character("[oli_nick]", color="#2EE087")
define dau = Character("ward")
define nor = Character("Norah", color="#C4143F")
define brk = Character("Brooke", color="#E39445")
define ber = Character("Bernie", color="#FF4545")
define ala = Character("Alita", color="#9745E3")
define vic = Character("Victoria", color="#C4143F")
define uk = Character("Unknown", color="#25354D")
define grl = Character("Girl", color="#482763")
define grls = Character("Girls", color="#EB0091")
define hao = Character("Hao", color="#6619FF")
define cha = Character("Chad", color="#BD1900")
define dj = Character("DJ", color="#BD1900")
define doc = Character("Doctor Harrington", color="#D48D00")
define bld = Character("Blonde", color="#E864A4")
define bru = Character("Brunette", color="#AF33E1")
define red = Character("Redhead", color="#2EE087")
define nat = Character("Natalie", color="#AF33E1")
define gln = Character("Glenn", color="#FF833B")
define jul = Character("Julia", color="#9E1B5A")
define tif = Character("Tiffany", color="#32A852")
define mir = Character("Mira", color="#9E1B5A")
define chs = Character("Cheslea", color="#32A852")
define van = Character("Vanessa", color="#CE03FC")
define rac = Character("Rachel", color="#FF8585")
define amc = Character("[amc_nick]")
define omc = Character("[omc_nick]")
define mmc = Character("[mmc_nick]")
define jad = Character("Jade", color="#FFC387")
define clk = Character("Clerk", color="#FFEA00")
define tv = Character("Television", color="#FFAA00")







define qdissolve = Dissolve(0.3)
define xdissolve = Dissolve(0.2)
define cdissolve = Dissolve(0.4)
define sdissolve = Dissolve(0.7)
define ssdissolve = Dissolve(1.0)
define vsdissolve = Dissolve(3.0)

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define redflash = Fade(0.1, 0.0, 0.5, color="#a30000")
define blueflash = Fade(0.1, 0.0, 0.5, color="#0085fa")
define pinkflash = Fade(0.1, 0.0, 0.5, color="#ff0059")
define purpflash = Fade(0.1, 0.0, 0.5, color="#a1009e")

define sfade = Fade(0.5, 0.7, 0.5)
define fadehold = Fade(0.5, 1.0, 0.5)
define whitefade = Fade(0.5, 0.1, 0.5, color="#fff")



define config.default_music_volume = 0.4
define config.default_sfx_volume = 0.4

init -1 python:
    renpy.music.register_channel("Chan1", mixer="music", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("Chan2", mixer="music", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("Chan3", mixer="music", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("Chan4","sfx",True,tight=True)
    renpy.music.register_channel("Chan5", mixer="music", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("Chan6", mixer="music", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)









default age = 18
default nage = 18
default menuset = set()
default menuset2 = set()
default menuset3 = set()
default blood_on = True
default urine_on = True
default ch2_complete = False
default ch3_complete = False
default ch4_complete = False





default mad_scared = 0
default ali_scared = 0
default liv_scared = 0



default mad_horny = 0
default ali_horny = 0
default liv_horny = 0



default mad_love = 0
default ali_love = 0
default liv_love = 0



default brk_corrupted = 0
default brk_broken = 0
default brk_jealousy = 0



default brk_rel = False
default lita_rel = False
default vic_rel = False
default nat_rel = False
default van_rel = False



default ali_pure = 0
default mad_pure = 0
default liv_pure = 0
default lit_pure = 0
default brk_pure = 0



default ali_lust = 0
default mad_lust = 0
default liv_lust = 0
default lit_lust = 0
default brk_lust = 0



default ali_dark = 0
default mad_dark = 0
default liv_dark = 0
default lit_dark = 0
default brk_dark = 0



default alipure = False
default madpure = False
default livpure = False
default litpure = False
default brkpure = False



default alilust = False
default madlust = False
default livlust = False
default litlust = False
default brklust = False



default alidark = False
default maddark = False
default livdark = False
default litdark = False
default brkdark = False



default cc0 = False
default cc1 = False
default cc2 = False
default cc3 = False
default cc4 = False
default cc5 = False
default cc6 = False
default cc7 = False
default cc8 = False
default cc9 = False



default lust = 0
default pure = 0
default dark = 0



default purity = False
default lustful = False
default darkness = False







label splashscreen:

    $ renpy.music.set_volume(1.0, delay=0, channel='Chan3')
    scene black
    with sdissolve
    $ renpy.pause(0.8, hard=True)
    image splashrk = Movie(play="videos/splash_rkstudios.webm")
    show splashrk with dissolve
    $ renpy.pause(10.5, hard=True)
    scene black with dissolve
    $ renpy.pause(.8, hard=True)









    scene black
    with cdissolve
    $ renpy.pause(0.2, hard=True)
    scene menuimg
    with sdissolve
    $ renpy.pause(0.2, hard=True)

    return

label start:

    stop music fadeout 03.0

    scene warning with sdissolve
    pause (6.4)
    scene black with sdissolve
    $ renpy.pause (2, hard=True)
    play music "<loop 0.0>audio/this_is_a_jazz_space.ogg" fadein 05.0
    "You must be eighteen years or older to play this game. If you are under eighteen you should close the game immediately."
    $ renpy.pause (.6, hard=True)
    scene black with dissolve
    menu:
        "Do you confirm that you are eighteen years or older?"
        "Yes: I am at least 18 years old":
            pause (.8)
        "No: Please close the game":
            $ renpy.quit()

    scene music with dissolve
    pause (4)
    scene black with dissolve
    $ renpy.pause (.4, hard=True)

label solochoicebuttons:

    menu:
        "Would you like to view a quick tutorial?"
        "Yes":
            jump tutorial
        "No":
            "Starting the game. Have fun!"
            stop music fadeout 04.0
            jump chapterone

label tutorial:

    $ renpy.pause (.3, hard=True)
    scene tutorial with sdissolve
    pause
    scene black with dissolve
    $ renpy.pause (.2, hard=True)
    scene crucial with sdissolve
    pause
    scene black with dissolve
    "Press {color=#00DB84}right-click{/color} or {color=#00DB84}esc{/color} to view the in-game menu."
    "Use this menu to {color=#00DB84}save{/color}, {color=#00DB84}load{/color}, or {color=#00DB84}exit{/color} the game at any time."
    "You may also edit your preferences in the {color=#00DB84}options{/color} menu. It is recommended that you play this game full-screen."
    "If playing in full-screen mode causes your screen to glitch simply switch to windowed mode and then maximize the window."
    "You may also roll-back the game using your {color=#00DB84}mouse-wheel{/color}, hide the interface by pressing the {color=#00DB84}MMB{/color} or {color=#00DB84}H{/color} key, and take screenshots with the {color=#00DB84}S{/color} key."
    stop music fadeout 04.0
    "Great! That's the end of the tutorial. Let's start the game!"
    jump chapterone

label end:

    scene black with sdissolve
    $ renpy.pause (.4, hard=True)
    scene save with sdissolve
    pause

    scene black with sdissolve
    $ renpy.pause (.4, hard=True)
    menu:
        "Would you like to view your status?"
        "View Status":
            jump status_show
        "Skip":
            if ch2_complete == False:
                jump chaptertwo
            elif ch2_complete == True and ch3_complete == False:
                jump chapterthree
            else:
                jump end2

label status_show:


    scene status with sdissolve
    show stat_liv with sdissolve:
        xalign 0.14
        ypos 50
    pause (.6)
    show screen liv_stats with sdissolve
    pause


    hide screen liv_stats with sdissolve
    hide stat_liv with sdissolve
    show stat_ali with sdissolve:
        xalign 0.14
        ypos 50
    pause (.6)
    show screen ali_stats with sdissolve
    pause


    hide screen ali_stats with sdissolve
    hide stat_ali with sdissolve
    show stat_mad with sdissolve:
        xalign 0.14
        ypos 50
    pause (.6)
    show screen mad_stats with sdissolve
    pause


    hide screen mad_stats with sdissolve
    hide stat_mad with sdissolve
    show stat_grc with sdissolve:
        xalign 0.14
        ypos 50
    pause (.6)
    show screen mc_stats with sdissolve
    pause
    hide screen mc_stats with dissolve
    hide stat_grc with dissolve

    if ch2_complete == False:
        jump chaptertwo
    elif ch2_complete == True and ch3_complete == False:
        jump chapterthree
    else:
        jump end2

label end2:

    scene black with sdissolve
    $ renpy.pause (.2, hard=True)
    scene patreon with sdissolve
    show screen patreon_button
    pause
    hide screen patreon_button with dissolve
    scene black with dissolve
    image credits = Movie(play="videos/credits.webm", loop=False)
    show credits with sdissolve
    $ renpy.pause (12, hard=True)
    show screen system_msg1 with dissolve
    pause (.8)
    hide screen system_msg1 with dissolve
    show screen system_msg1 with dissolve
    pause (.8)
    hide screen system_msg1 with dissolve
    show screen system_msg1 with dissolve
    pause (.8)
    hide screen system_msg1 with dissolve
    show screen system_msg1 with dissolve
    pause (.8)
    hide screen system_msg1 with dissolve
    pause
    hide credits with dissolve
    pause (1)
    stop music fadeout 04.0
    scene end with sdissolve
    pause (3)
    "Press any button to return to the main menu."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
