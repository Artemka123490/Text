











screen patreon_button():
    imagebutton auto "gui/button/patreonbtn_%s.png" xalign 0.483 yalign 0.60 action Null
    imagebutton auto "gui/button/patreonbtn_%s.png" xalign 0.483 yalign 0.60 action OpenURL ("https://patreon.com/radiantgame")







init -1:

    transform gracie_transform():
        alpha 3
        zoom 1.25
        xalign 0.498
        yalign 1.0
        on show:
            linear 5.5 yalign 0.08
        on hide:
            linear 1 alpha 3

    transform gracie2_transform():
        alpha 3
        zoom 1
        xalign 0.494
        yalign 1.0
        on show:
            linear 5 yalign 0.08
        on hide:
            linear 1 alpha 3

    transform brooke_transform():
        alpha 3
        zoom 1.25
        xalign 0.498
        yalign 1.0
        on show:
            linear 5.5 yalign 0.08
        on hide:
            linear 1 alpha 3

    transform allie_transform():
        alpha 3
        zoom 1.25
        xalign 0.498
        yalign 1.0
        on show:
            linear 5.5 yalign 0.08
        on hide:
            linear 1 alpha 3

    transform nat_transform():
        alpha 3
        zoom 1.25
        xalign 0.5
        yalign 1.0
        on show:
            linear 5.5 yalign 0.08
        on hide:
            linear 1 alpha 3

    transform brooke2_transform():
        alpha 3
        zoom 1.25
        xalign 0.5
        yalign 1.0
        on show:
            linear 5.5 yalign 0.08
        on hide:
            linear 1 alpha 3

    transform brooke3_transform():
        alpha 3
        zoom 1.25
        xalign 0.5
        yalign 1.0
        on show:
            linear 5.5 yalign 0.08
        on hide:
            linear 1 alpha 3

init -1:
    image gracie:
        "images/chapter 1/prom0.png"

    image gracie2:
        "images/chapter 1/grbr_c1.png"

    image brooke:
        "images/chapter 2/c2e39.webp"

    image allie:
        "images/chapter 2/c2ox2.webp"

    image natalie:
        "images/chapter 3/c3e0.png"

    image brooke2:
        "images/chapter 3/c3q0.png"

    image brooke3:
        "images/chapter 3/c3q48blush.png"
















screen system_msg1():
    text "{font=gui/fonts/handlee/handlee-regular.ttf}Press any button to skip.{/font}" xalign 0.046 yalign 0.1

screen system_msg2():
    text "{font=gui/fonts/handlee/handlee-regular.ttf}{size=+30}{b}Shit!!!{/b}{/size}{/font}" xalign 0.5 yalign 0.9

screen system_msg3():
    text "{font=gui/fonts/handlee/handlee-regular.ttf}You've unlocked a new memory.{/font}" xalign 0.046 yalign 0.1









screen liv_stats():
    vbox:
        xalign .787
        yalign .638
        spacing 33
        if tbed == True:
            text "{font=gui/fonts/handlee/handlee-regular.ttf}{size=+20}{color=#00BD42}[liv] \"[onick]\" [sur]{/color}{/size}{/font}" at center
        else:
            text "{font=gui/fonts/handlee/handlee-regular.ttf}{size=+15}{color=#00BD42}[liv] aka \"[onick]\"{/color}{/size}{/font}" at center

        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Relationship{/b}{/font}{/size}" at center
        if livpure == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#03A9FC}Purity{/color}{/font}{/size}" xalign 0.5 ypos -23
        elif livlust == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#FF6E9E}Lust{/color}{/font}{/size}" xalign 0.5 ypos -23
        elif livdark == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#CC0000}Darkness{/color}{/font}{/size}" xalign 0.5 ypos -23
        else:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#FAE500}None{/color}{/font}{/size}" xalign 0.5 ypos -23

        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Purity{/b}{/font}{/size}" at center
        text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-2}{color=#03A9FC}[liv_pure]{/color}{/font}{/size}" xalign 0.5 ypos -23
        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Lust{/b}{/font}{/size}" at center
        text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-2}{color=#FF6E9E}[liv_lust]{/color}{/font}{/size}" xalign 0.5 ypos -23
        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Darkness{/b}{/font}{/size}" at center
        text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-2}{color=#CC0000}[liv_dark]{/color}{/font}{/size}" xalign 0.5 ypos -23



screen ali_stats():
    vbox:
        xalign .787
        yalign .638
        spacing 33
        if tbed == True:
            text "{font=gui/fonts/handlee/handlee-regular.ttf}{size=+20}{color=#FF6E9E}[ali] \"[anick]\" [sur]{/color}{/size}{/font}" at center
        else:
            text "{font=gui/fonts/handlee/handlee-regular.ttf}{size=+15}{color=#FF6E9E}[ali] aka \"[anick]\"{/color}{/size}{/font}" at center

        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Relationship{/b}{/font}{/size}" at center
        if alipure == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#03A9FC}Purity{/color}{/font}{/size}" xalign 0.5 ypos -23
        elif alilust == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#FF6E9E}Lust{/color}{/font}{/size}" xalign 0.5 ypos -23
        elif alidark == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#CC0000}Darkness{/color}{/font}{/size}" xalign 0.5 ypos -23
        else:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#FAE500}None{/color}{/font}{/size}" xalign 0.5 ypos -23

        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Purity{/b}{/font}{/size}" at center
        text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-2}{color=#03A9FC}[ali_pure]{/color}{/font}{/size}" xalign 0.5 ypos -23
        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Lust{/b}{/font}{/size}" at center
        text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-2}{color=#FF6E9E}[ali_lust]{/color}{/font}{/size}" xalign 0.5 ypos -23
        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Darkness{/b}{/font}{/size}" at center
        text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-2}{color=#CC0000}[ali_dark]{/color}{/font}{/size}" xalign 0.5 ypos -23



screen mad_stats():
    vbox:
        xalign .787
        yalign .638
        spacing 33
        if tbed == True:
            text "{font=gui/fonts/handlee/handlee-regular.ttf}{size=+20}{color=#9E09B5}[mad] \"[mnick]\" [sur]{/color}{/size}{/font}" at center
        else:
            text "{font=gui/fonts/handlee/handlee-regular.ttf}{size=+15}{color=#9E09B5}[mad] aka \"[mnick]\"{/color}{/size}{/font}" at center

        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Relationship{/b}{/font}{/size}" at center
        if madpure == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#03A9FC}Purity{/color}{/font}{/size}" xalign 0.5 ypos -23
        elif madlust == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#FF6E9E}Lust{/color}{/font}{/size}" xalign 0.5 ypos -23
        elif maddark == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#CC0000}Darkness{/color}{/font}{/size}" xalign 0.5 ypos -23
        else:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#FAE500}None{/color}{/font}{/size}" xalign 0.5 ypos -23

        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Purity{/b}{/font}{/size}" at center
        text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-2}{color=#03A9FC}[mad_pure]{/color}{/font}{/size}" xalign 0.5 ypos -23
        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Lust{/b}{/font}{/size}" at center
        text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-2}{color=#FF6E9E}[mad_lust]{/color}{/font}{/size}" xalign 0.5 ypos -23
        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Darkness{/b}{/font}{/size}" at center
        text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-2}{color=#CC0000}[mad_dark]{/color}{/font}{/size}" xalign 0.5 ypos -23



screen mc_stats():
    vbox:
        xalign .787
        yalign .638
        spacing 33

        text "{font=gui/fonts/handlee/handlee-regular.ttf}{size=+20}{color=#9E09B5}[mc] [sur]{/color}{/size}{/font}" at center

        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Psyche{/b}{/font}{/size}" at center
        if purity == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#03A9FC}Purity{/color}{/font}{/size}" xalign 0.5 ypos -23
        elif lustful == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#FF6E9E}Lustful{/color}{/font}{/size}" xalign 0.5 ypos -23
        elif darkness == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#CC0000}Darkness{/color}{/font}{/size}" xalign 0.5 ypos -23
        else:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#FAE500}None{/color}{/font}{/size}" xalign 0.5 ypos -23

        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Crucial Choices{/b}{/font}{/size}" at center
        if ch2_complete == False and ch3_complete == False:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#FAE500}2{/color}{/font}{/size}" xalign 0.5 ypos -23
        if ch2_complete == True and ch3_complete == False:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#FAE500}5{/color}{/font}{/size}" xalign 0.5 ypos -23
        if ch2_complete == True and ch3_complete == True:
            text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-3}{color=#FAE500}12{/color}{/font}{/size}" xalign 0.5 ypos -23

        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Purity{/b}{/font}{/size}" at center
        text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-2}{color=#03A9FC}[pure]{/color}{/font}{/size}" xalign 0.5 ypos -23
        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Lust{/b}{/font}{/size}" at center
        text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-2}{color=#FF6E9E}[lust]{/color}{/font}{/size}" xalign 0.5 ypos -23
        text "{font=gui/fonts/roboto/roboto-regular.ttf}{size=-3}{b}Darkness{/b}{/font}{/size}" at center
        text "{font=gui/fonts/archd/architectsdaughter-regular.ttf}{size=-2}{color=#CC0000}[dark]{/color}{/font}{/size}" xalign 0.5 ypos -23
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
