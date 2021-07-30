













define config.name = _("Radiant")





define gui.show_name = False




define config.version = "0.3.1"





define gui.about = _p("""{size=-5}{font=gui/fonts/roboto/roboto-regular.ttf}Radiant is currently under development, meaning this is {i}not{/i} the \"completed game.\"

All characters in "Radiant," except those who are {b}not{/b} related to or depicted in sexual acts, are of the legal age (18+).
Any modifications or attempts to change a character's age, relationship, or appearance is NOT endorsed by the creators, and should in no way be used by players. You have been warned!
This game will be released in full-chapters. Each chapter is unique meaning no timeline is specified.

It is recommended that you visit one of our creator support pages to stay up-to-date!
Creating Radiant takes time, effort, and funding! We therefore rely entirely on player support.

Consider {a=https://patreon.com/radiantgame}becoming a patron{/a} to receive exclusive benefits and rewards.

Alternatively you could consider joining us over on {a=https://subscribestar.adult/radiant}SubscribeStar{/a}.

You can also join us on {a=https://discord.gg/u3TBaxH}Discord{/a}.

Thanks!{/font}{/size}
""")






define build.name = "Radiant"







define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = "audio/eternal_structures.ogg"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = Dissolve(1.8)




define config.end_game_transition = Dissolve(1.5)
















define config.window = "hide"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 30





default preferences.afm_time = 18
















define config.save_directory = "Radiant-1578122113"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('game/patch.rpy', None)
    build.classify('game/patch.rpyc', None)

    build.classify('game/patch_ned.rpy', None)
    build.classify('game/patch_ned.rpyc', None)
    build.classify('game/images/norah/**.jpg', None)
    build.classify('game/images/norah/**.webp', None)
    build.classify('game/images/norah/**.png', None)
    build.classify('game/videos/norah/**.webm', None)

    build.classify('game/**.rpy', None)
    build.classify('game/script.rpyc', "archive")
    build.classify('game/ch1.rpyc', "archive")
    build.classify('game/ch2.rpyc', "archive")
    build.classify('game/ch3.rpyc', "archive")
    build.classify('game/gui.rpyc', "archive")
    build.classify('game/options.rpyc', "archive")
    build.classify('game/screens.rpyc', "archive")
    build.classify('game/custom.rpyc', "archive")
    build.classify('game/status.rpyc', "archive")

    build.classify("game/gui/**.png", "archive")
    build.classify("game/gui/**.jpg", "archive")
    build.classify("game/gui/**.webp", "archive")
    build.classify("game/gui/buttons/**.png", "archive")
    build.classify("game/gui/fonts/Handlee/**.ttf", "archive")
    build.classify("game/gui/fonts/Roboto/**.ttf", "archive")
    build.classify("game/gui/fonts/ArchD/**.ttf", "archive")

    build.classify('game/images/**.jpg', "archive")
    build.classify('game/images/**.webp', "archive")
    build.classify('game/images/**.png', "archive")

    build.classify('game/images/Chapter 1/**.jpg', "archive")
    build.classify('game/images/Chapter 1/**.webp', "archive")
    build.classify('game/images/Chapter 1/**.png', "archive")

    build.classify('game/images/Chapter 2/**.jpg', "archive")
    build.classify('game/images/Chapter 2/**.webp', "archive")
    build.classify('game/images/Chapter 2/**.png', "archive")

    build.classify('game/images/Chapter 3/**.jpg', "archive")
    build.classify('game/images/Chapter 3/**.webp', "archive")
    build.classify('game/images/Chapter 3/**.png', "archive")

    build.classify('game/images/Status/**.jpg', "archive")
    build.classify('game/images/Status/**.webp', "archive")
    build.classify('game/images/Status/**.png', "archive")

    build.classify('game/videos/**.webm', "archive")

    build.classify('game/videos/Chapter 1/**.webm', "archive")

    build.classify('game/videos/Chapter 2/**.webm', "archive")

    build.classify('game/videos/Chapter 3/**.webm', "archive")

    build.classify('game/audio/**.ogg', "archive")
    build.classify('game/audio/**.mp3', "archive")
    build.classify('game/audio/sounds/**.ogg', "archive")









    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
