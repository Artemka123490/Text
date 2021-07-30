





label chapterone:

    $ renpy.pause (.15, hard=True)
    scene black with dissolve
    $ player_name = renpy.input("Please enter your {b}first{/b} name...")
    if player_name == "":
        $ player_name="John"
    $ surname = renpy.input("Please enter your {b}last{/b} name...")
    if surname == "":
        $ surname="Evans"
    mc "My name is... [mc] [sur]."

    $ renpy.music.set_volume(0.0, delay=0, channel='Chan1')
    $ renpy.music.set_volume(1.0, delay=0, channel='Chan2')
    $ renpy.music.play("<loop 0.0>audio/scouting.ogg", channel='Chan1', loop=True, fadeout=6.0, synchro_start=True, fadein=0.6, tight=None, if_changed=False)
    $ renpy.music.play("<loop 0.0>audio/scouting_muffled.ogg", channel='Chan2', loop=True, fadeout=0.6, synchro_start=True, fadein=6.0, tight=None, if_changed=False)
    scene black with sdissolve
    $ renpy.pause (1.5, hard=True)
    scene chapter1 with sdissolve
    $ renpy.pause (5, hard=True)

    scene outs_prom4 with sdissolve
    if tbed == False:
        mc "(This is it. My first date with the girl I've had a crush on since we were kids. I can't believe I actually had the courage to ask Lindsey to the dance.)"
    else:
        mc "(This is it. My first date with the girl I've had a crush on since we were kids. I can't believe I actually had the courage to ask Lindsey to prom.)"
    mc "(Hell... I can't believe she said {i}yes!{/i})"
    mc "(It feels like my heart is going to jump out of my chest and I'm starting to get sweaty. I should relax.)"
    na "You should... but you don't."
    scene outs_prom3 with dissolve
    mc "(Should I have brought these flowers? Maybe I overdid it a little...)"
    mc "(Alright, [mc]... get it together. You're acting like a schoolgirl.)"
    scene outs_prom2 with dissolve
    mc "(The question is... am I nervous because of my date... or the fact that she's supposed to be meeting me here and hasn't answered my calls or texts?)"
    mc "(She'll be here... right?)"
    scene outs_prom4 with dissolve

    menu:
        mc "(Screw it. Let's go!)"
        "Go In":
            $ renpy.music.set_volume(0.6, delay=0.035, channel='Chan1')
            $ renpy.music.set_volume(0.0, delay=0.03, channel='Chan2')
            $ renpy.music.stop(channel='Chan2', fadeout=False)
            scene outs_prom1 with dissolve
            $ renpy.pause (.8, hard=True)

    play sound "audio/sounds/crowd_talking.ogg" loop
    scene prom16 with dissolve
    mc "..."
    if tbed == False:
        na "The event is well on its way and most of the attendees have already started to dance."
    else:
        na "Your high school prom is well on its way and most of the attendees have already started to dance."
    scene prom15 with sdissolve
    mc "(What's with all the fog? It's like a strip club in here.)"
    mc "(At least they went big with the sound system. This is going to be a good night!)"
    scene prom14 with fade
    hao "Duuude, you made it!{w} You're looking sharp, my guy."
    scene prom13 with qdissolve
    mc "(My good friend \"Hao Long,\" I see he's in typical form tonight.)"
    mc "Thanks! You're looking pretty, uh... pretty much exactly like I expected you'd look, actually. What the hell {i}is{/i} that in your nose?"
    scene prom10 with qdissolve
    hao "Chopsticks my guy. I heard they're serving sushi later."
    scene prom13 with qdissolve
    mc "That's... sanitary. Have you seen Lindsey?"
    scene prom10 with qdissolve
    hao "Who the...{w} oh you mean {i}that{/i} Lindsey! Can't say I have yet. You guys come here as friends or something?"
    scene prom13 with qdissolve
    mc "Friends? Hell no. She's my date, actually."
    scene prom14 with qdissolve
    hao "No way, haha! [mc]'s fucking Lindsey! That's legendary, bro. I didn't come with anyone but I plan to cum {i}in{/i} someone if you know what I'm saying. Get my lil ding dong a graduation present.{w} Me so horny!"
    scene prom11 with dissolve
    mc "Uh, yeah. That's... nice. Anyways thank you for the help, Hao. I gotta keep looking around. I'll talk to you later!"
    scene prom17 with fade
    mc "(She has to be here somewhere... right? We were supposed to meet twenty minutes ago...)"
    $ renpy.music.stop(channel='Chan1', fadeout=5.0)
    mc "(Don't panic. She's probably just running behind. I'm sure that's why she can't answer my calls.)"
    scene prom9 with fadehold
    play music "<loop 0.0>audio/1940_s_slow_dance.ogg" fadein 05.0
    na "Soon... a few minutes becomes an hour and your texts go unanswered. Although you cling to denial... the sound of the night's first slow song comes with the haunting realization that it's winding down to an end."
    mc "(She... she stiffed me. I... I can't believe Lindsey stood me up. What the fuck?)"
    mc "(But why? Did I say something wrong?)"
    na "You watch helplessly as your peers find dance partners... blissfully unaware of your existential crisis."
    mc "(Fuck it. I'm just going to finish my drink then head home. This is bullshit.)"
    na "But as you scan the room once more in hopes of finding your date, something else catches your eye."
    scene prom26 with sdissolve
    $ renpy.pause (.3, hard=True)
    scene prom25 with sdissolve
    $ renpy.pause (.3, hard=True)
    scene prom24 with sdissolve
    mc "(Hm... Gracie doesn't look so happy right now. I wonder what happened?)"
    pause (1)
    show gracie at gracie_transform
    mc "(Did she get stiffed too?)"
    scene prom27 with sdissolve
    mc "(Maybe I should've asked her instead. After all, I used to like her quite a lot.)"
    mc "(I never did get around to talking to her though...)"
    mc "(I mean, I know nothing about her other than she seems like a nice person.)"
    na "You contemplate asking her to dance when you notice Chad, the biggest douchebag in the district, obnoxiously approach her."
    scene promb5 with fade
    cha "Sup, slut. You are graced with the presence of Chad."
    grc "Leave me be, Chad. I'm not in the mood for whatever you're going to say."
    scene promb4 with dissolve
    cha "Are you a dictionary? Cause my... uh... dick is hairy."
    grc "That doesn't even make sense. What are you doing?"
    mc "(You've got to be kidding me. So even {i}this{/i} asshole had a date tonight? Yet I'm the one who got stiffed?)"
    grc "{size=+5}J-Just go away, Chad!{/size} That's disgusting! I already told you I'm not interested!"
    stop music fadeout 04.0
    cha "Stop resisting, slut! At least dance with me!"
    scene promb3 with dissolve
    grc "I'm not just some slut! Get your hands off of me! You're hurting my arm!"
    na "Things escalate as Chad attempts to aggressively drag her to the dance floor... ignoring her protests."
    play music "<loop 0.0>audio/carried.ogg" fadein 04.0
    scene prom8 with dissolve
    mc "Are you fucking serious right now Chad? Stop being such a prick."
    scene prom7 with dissolve
    cha "What'd you just say you fucking {i}maggot?{/i} I'll have you know..."
    scene prom6 with xdissolve
    scene prom6 with vpunch
    $ renpy.pause (.4, hard=True)
    scene prom5 with dissolve
    na "He hits the ground with a well-timed thud."
    mc "{i}Shut up,{/i} Chad."
    scene prom2 with dissolve
    na "And Gracie catches you off guard with a hug."
    scene promb1 with dissolve
    grc "Thank you for standing up for me, [mc]!{w} He was squeezing my arm really hard..."
    scene promb2 with xdissolve
    na "You remember all the times you wanted to approach her... wanted to ask her out... and the small crush you once had on her."
    na "Tonight couldn't get any worse than it already is, so despite the low chance of success you muster the courage to ask her."
    mc "Gracie... do you want to dance with me?"
    scene promb1 with xdissolve
    grc "S-Sure... I'd like that."
    jump promdance

label promdance:

    scene black with dissolve
    pause (.5)
    scene promc4 with dissolve
    grc "So that's why you never talked to me?"
    grc "You could have... you know. I'm not like those snobby girls who think they're too good to talk to others just cause they're not... popular or whatever."
    scene promb7 with qdissolve
    mc "Hey now... it's not like I'm in the Chess club. I'm a damn wide receiver."
    scene promc4 with qdissolve
    grc "Hehe, I know. I didn't mean you weren't popular."
    scene promb7 with qdissolve
    mc "Is Chad the exception, then?"
    scene promc4 with qdissolve
    grc "Haha! Yeah, except Chad. He's always saying these dirty things to me. Calling me names like \"slut\" and \"skank.\" I don't know what his problem is!"
    scene promb7 with qdissolve
    mc "Everyone's a little cringe in this town. As for Chad, he just needed a good beating."
    scene promc4 with qdissolve
    grc "Hehe! You took care of that. Did you see his dumb face?"
    grc "He's such an asshole. And you're really sweet for protecting me. I'm glad none of the chaperones saw it... wouldn't want you to get in trouble."
    scene promb7 with qdissolve
    mc "Yeah... well... it was worth it just to shut his mouth for once. And now he knows better than to talk to you that way."
    stop music fadeout 05.0
    scene prom1 with dissolve
    na "You guys chat and flirt for some time."
    na "But just as you decide you're going to make a move..."
    play music "<loop 0.0>audio/right_here_beside_you.ogg" fadein 04.0
    na "The music picks up."
    scene prom37 with sfade
    dj "{size=+3}{i}I wanna see every last one of y'all get nasty in here. Spread yo pussies, thots!{/i}{/size}"
    pause (.8)
    uk "{size=+3}{i}Young man, you can't talk like that in here! You sound like an idiot.{/i}{/size}"
    scene promb6 with dissolve
    pause (.8)
    scene prom35 with dissolve
    dj "{size=+3}{i}Man {b}fuck{/b} you. You ain't my dad.{/i}{/size}"
    scene prom34 with dissolve
    $ renpy.pause (.7)
    scene prom33 with dissolve
    $ renpy.pause (.7)
    mc "(Damn, she's pushing her ass against me pretty hard.)"
    scene prom37 with fade
    $ renpy.pause (.7)
    scene prom39 with fade
    pause (.4)
    mc "(I can feel her pussy grinding against my legs.)"
    scene prom31 with fadehold
    na "But to your disappointment the moment abruptly ends as Gracie takes a step backwards. She's visibly startled by something behind you."
    scene prom32 with dissolve
    stop sound fadeout 03.0
    grc "[mc]... we should leave."
    mc "Why? Is everything alright?"
    scene prom29 with fade
    cha "{size=+5}There's that faggot who hit me! I'm going to murder you, you fucking nerd!{/size}"
    scene prom00 with fade
    grc "Come on! We shouldn't stay here. Do you have a car?"
    mc "Y-Yes but I'm too drunk to drive I think..."
    scene prom28 with fade
    cha "Get back here you fucking retard!{w} I'm going to snap your neck!"
    scene prom00 with fade
    grc "Don't worry about it. I'll drive! We can go back to my place."
    scene aft_prom1 with fadehold
    na "You exit the building and begin sprinting towards the parking lot. Along the way, you give Gracie your keys."
    scene aft_prom5 with fade
    grc "Come on! Let's hurry."
    mc "Don't worry. I'm pretty sure we're way ahead of them..."
    scene aft_prom4 with fade
    cha "You can't run forever you fucking chode!"
    scene aft_prom3 with sdissolve
    na "You speed out of there long before Chad and the gang can catch up to you."
    stop music fadeout 06.0
    scene aft_prom2 with sdissolve
    na "And although your mind is racing, you can't take your eyes off of the cutie behind the wheel."
    jump gracieshome

label gracieshome:

    scene grbr_a13 with fadehold
    na "As promised she drives you to her house."
    scene grbr_a12 with fade
    grc "We have to be quiet! My parents can't know that you're with me."
    scene grbr_a11 with fade
    pause
    scene grbr_a3 with fadehold
    grc "Welcome to my dull, uninteresting bedroom! It's a work in progress."
    scene grbr_a2 with xdissolve
    mc "Hey... it's not that bad."
    scene grbr_a5 with qdissolve
    grc "Thanks!"
    grc "Um, I should probably warn you. If my dad finds you here, he {i}will{/i} kill you..."
    scene grbr_a6 with qdissolve
    mc "Oh... uh... thanks for the warning."
    grc "Mhm."
    pause (.3)
    mc "So um... that was really nice of you, you know."
    mc "Helping me out back there. Those lacrosse-loving cunts would've jumped me and I definitely was not in any condition to fight back... let alone escape. I drank way too much."
    scene grbr_a3 with xdissolve
    grc "Don't mention it! You'd have done the same for me... wouldn't you?"
    scene grbr_a6 with qdissolve
    pause (.3)
    mc "(I can't help but wonder what I... no... what {i}we{/i} are doing. Why she invited me here... and why I'm in the bedroom of a girl I hardly know. Am I reading too much into this?)"
    scene grbr_a3 with xdissolve
    grc "I owed you... you know? It's not everyday that someone risks their neck for you. You stood up for me..."
    scene grbr_a2 with xdissolve
    mc "I was just doing what I thought was right at the time. I don't know what came over me to be honest."
    scene grbr_a3 with xdissolve
    grc "Y-Yeah. But you didn't have to intervene. You're lucky you didn't get in trouble! But I'm glad you stepped in when you did. That was... it was really sweet of you."
    scene grbr_a2 with xdissolve
    mc "And you didn't have to invite me back to your room... but you did anyway. Why?"
    scene grbr_a3 with xdissolve
    grc "Well it's not like I could've just taken you back to your place! How would I get home then? And besides... you were in no state to drive yourself home or anything..."
    grc "S-So I guess I just figured you could um...{w} I don't know... w-wait here until you think you're okay to drive. And then sneak back out.{w} Or something... I didn't really have time to think about it!"
    scene grbr_a2 with xdissolve
    mc "Haha. It's alright. You don't have to be embarrassed; I'm just curious."
    scene grbr_a5 with qdissolve
    grc "I'm not embarrassed!"
    scene grbr_a6 with qdissolve
    mc "Uh-huh... sure. You're blushing because you're {i}not{/i} embarrassed."
    scene grbr_a3 with xdissolve
    grc "Hmph! This is what I get for being considerate, huh?"
    scene grbr_a6 with xdissolve
    na "She speaks playfully."
    mc "Heh. I'm just messing around. Thank you, Gracie. For everything. And I'm glad to be here if I'm being honest."
    scene grbr_a5 with dissolve
    pause (.3)
    grc "[mc] I... I should be the one thanking you."
    scene grbr_a7 with xdissolve
    na "She reaches forward and touches your hand..."
    scene grbr_a9 with qdissolve
    na "But a sharp pain makes you jerk away."
    scene grbr_a8 with dissolve
    grc "Oops- I'm sorry!{w} Are you okay?{w} What happened to your hand?"
    mc "It's my finger. I think I might have sprained it when I punched ole dickmouth."
    scene grbr_a9 with qdissolve
    grc "Oh no! It looks swollen. Hold on... let me go get you some ice!"
    mc "No, no... I'll be okay! Really, you don't have to."
    scene grbr_a0 with dissolve
    grc "No way! You're hurt. It will take longer to heal if we don't ice it now and reduce the swelling."
    grc "Let me just go to the kitchen quickly to get you something. I'll be right back!"
    scene grbr_b21 with fadehold
    na "She gives you no say in the matter and scurries out of the room."
    scene grbr_c5 with sdissolve
    mc "(Damn, that punch really did a number on my hand. Not sure how I didn't notice it until now. I can barely move my finger.)"
    mc "(The alcohol helps though.)"
    mc "(I can't believe I'm sitting in Gracie's room right now. I know we didn't have a lot of time to plan but... she just instinctively invited me back here. Without even so much as a second thought.)"
    mc "(Things got pretty spicy between us back on the dance floor. At one point we were pretty much dry-humping...)"
    mc "(Does she want to...)"
    scene grbr_b4 with fade
    play music "<loop 0.0>audio/summer_love.ogg" fadein 09.0
    pause (.3)
    mc "(Ah there she is.)"
    scene grbr_b3 with sdissolve
    grc "Here, I soaked this towel in some ice water. Give me your hand."
    scene grbr_b2 with dissolve
    na "You can't help but stare."
    mc "Gracie..."
    scene grbr_b1 with qdissolve
    grc "Yeah, [mc]?"
    scene grbr_b2 with qdissolve
    mc "Why did you look so upset? Back at the dance when I first noticed you... you were standing there all alone and you didn't seem very happy."
    scene grbr_b1 with qdissolve
    grc "Oh... I didn't realize anyone noticed..."
    scene grbr_b3 with qdissolve
    if tbed == False:
        grc "Well to be honest... my best guy friend asked me to go. I don't have a boyfriend or anything so I was kind of... prepared to just miss it altogether."
    else:
        grc "Well to be honest... my best guy friend asked me to prom. I don't have a boyfriend or anything so I was kind of... prepared to just miss it altogether."
    scene grbr_b1 with dissolve
    grc "So when he asked me... I was so happy! He said he was doing it because he wanted to be a good friend to me. He even made it clear that he was asking {i}as a friend...{/i} knowing that I don't see him as more than that."
    scene grbr_b3 with dissolve
    grc "But as soon as we got there he tried to kiss me. And when I told him no he just... flipped out. Told me to go fuck myself and left."
    grc "So there I was... on what was supposed to be a wonderful night... alone."
    scene grbr_b2 with qdissolve
    mc "Wow... I'm sorry. He shouldn't have reacted the way he did."
    scene grbr_b1 with dissolve
    grc "What about you? Where was your date? Oh my God! You didn't abandon your date to come here did you?"
    scene grbr_b2 with qdissolve
    mc "Actually, Gracie... my date stood {i}me{/i} up. She agreed to go with me. We even texted a little bit the night before... but when I texted her this afternoon she never replied. We were supposed to meet up at the event and she just... didn't show."
    scene grbr_b3 with qdissolve
    grc "Oh my God, that is so messed up! Who was it that stiffed you!?"
    scene grbr_b2 with qdissolve
    mc "Lindsey."
    scene grbr_b1 with qdissolve
    grc "Lindsey Brock? Oh no... that bitch! Fuck her... that totally doesn't even surprise me."
    scene grbr_b2 with qdissolve
    mc "Haha. I agree, fuck her. She could've told me if she didn't want to go..."
    scene grbr_b1 with xdissolve
    grc "Well she's an idiot! Don't even worry about her. I'm sorry I brought it up, [mc]. Do you forgive me?"
    scene grbr_b2 with xdissolve
    mc "No need to apologize. It's okay..."
    mc "And besides, if she hadn't stood me up..."
    mc "I wouldn't be here right now with you."
    scene grbr_b3 with xdissolve
    grc "I-I'm glad too. You know... that you're here with me."
    scene grbr_b2 with xdissolve
    mc "Hey. Um... could you do me a favor?"
    scene grbr_b1 with xdissolve
    grc "Of course. What kind of favor?"
    scene grbr_b2 with dissolve
    pause (1)
    scene grbr_b20 with sdissolve
    mc "Come here for a second..."
    jump gracieforeplay

label gracieforeplay:

    scene grbr_b15 with dissolve
    na "She doesn't protest."
    menu:
        mc "(I can't hold back any longer.)"
        "Kiss Her":
            scene grbr_b14 with dissolve

    na "She closes her eyes and kisses you back passionately."
    scene grbr_b15 with dissolve
    grc "[mc]..."
    scene grbr_b17 with dissolve
    mc "Yeah?"
    scene grbr_b16 with qdissolve
    grc "Thank you for being so sweet to me. I've been treated like crap my whole life. By everyone. My father... my \"friends...\""
    scene grbr_b11 with qdissolve
    grc "Thanks to you I'll remember this night forever..."
    scene grbr_b14 with dissolve
    $ renpy.pause (.6, hard=True)
    stop music fadeout 09.0
    scene grbr_b10 with dissolve
    $ renpy.pause (.7, hard=True)
    scene grbr_b9 with dissolve
    na "You slide your hand between her legs and she doesn't resist you at all. Instead, she spreads them for you. You immediately notice her wet panties."
    scene grbr_b21 with dissolve
    na "To your surprise she suddenly breaks away from your grip and gets up from the bed."
    play music "<loop 3.0>audio/lust_for_love.ogg" fadein 04.0
    mc "(Shit! Did I go too far? Did I misread the situation? I hope she doesn't think I took advantage of her...)"
    mc "I'm sorry Gracie, I should've..."
    show gracie2 at gracie2_transform
    mc "(Ohh...!)"
    mc "(I was so caught up in my thoughts that I didn't notice her undressing...)"
    scene grsx_a2 with dissolve
    grc "[mc], I need to tell you something..."
    grc "I-I've never done anything... like this before."
    scene grsx_a3 with dissolve
    mc "If this is what you want..."
    scene grsx_a1 with fade
    mc "Then I want it too."
    grc "(I'll try my best to be good for you...)"
    scene grsx_a4 with sfade
    na "You quickly undress yourself while she lays down on the bed, her fully nude body sprawled out before you."
    scene grsx_a5 with dissolve
    grc "(Yes... I really do. I want this. I want it so much right now...)"
    mc "You have such a perfect little body, Gracie..."
    grc "(Oh my...)"
    scene grsx_a7 with fade
    na "Your words fall on deaf ears as she grows visibly distracted by something."
    grc "Y-You're so... so big!"
    mc "(She's staring at my cock so curiously. Is this the first time she's seen one up close?)"
    scene grsx_a5 with dissolve
    mc "Heh... do you think so?"
    scene grsx_a6 with dissolve
    na "You kneel down before her and position yourself between her legs. She shyly spreads them open, giving you a full view of her tiny virgin pussy."
    mc "So this will be your first time, Gracie?"
    grc "Y-Yeah. S-So please be gentle with me."
    mc "Don't worry. I'll make sure it doesn't hurt, okay?"
    grc "Y-Yeah. Make me wet first."
    mc "(She doesn't need much help with that... she's already drenched. And she's breathing so heavily.{w} She {i}really{/i} wants this.)"
    menu:
        mc "(Let's get her even more wet, then...)"
        "Lick Her":
            image gracielick = Movie(play="videos/Chapter 1/gracie_lick.webm")
            jump gracieoral_1

label gracieoral_1:

    scene black with dissolve
    $ renpy.pause (.3, hard=True)
    show gracielick with sdissolve
    na "You slowly glide your tongue from the bottom of her slit all the way up to her hood. She gasps and lets out a high-pitched squeal in response."
    grc "Oh... God... [mc]. T-That feels so... ahh..."
    na "She doesn't finish her sentence. Instead she continues with heavy breaths and deep gasps."
    mc "(The last girl told me I was really good at this. Based on Gracie's reaction... I guess she was right...)"
    grc "P-Please don't stop..."
    grc "{i}*Panting*{/i}"
    mc "(I can feel her fluids slowly pooling onto my tongue... her pussy tastes so good.)"
    grc "OH! F-F-Fuck m-me... with your tongue... c-clean me..."
    na "You take care to make sure she doesn't cum. Instead, you lick her until she's completely drenched and just at the edge of climax."
    pause
    menu:
        mc "(Sorry cutie. Can't let you cum just yet.)"
        "Continue":
            hide gracielick with dissolve
            jump graciemount

label graciemount:

    scene grsx_a11 with dissolve
    na "You climb up onto the bed... mounting her."
    mc "Hi sweetie..."
    scene grsx_a10 with xdissolve
    grc "Y-You stopped! You bad boy..."
    scene grsx_a11 with xdissolve
    mc "Haha, I did. You don't have my permission to cum yet."
    mc "The more I tease you... the harder you will cum. So... should I continue then?"
    scene grsx_a10 with xdissolve
    grc "Yes!"
    scene grsx_a7 with sdissolve
    grc "F-Fuck me..."
    grc "Please... fuck me."
    scene grsx_a9 with dissolve
    grc "G-Go slow, okay?"
    mc "Don't worry. I'll make you feel good."
    scene grsx_a17 with dissolve
    na "While her words tell you she's nervous she thrusts her opening against you... letting you know she's eager to be fucked."
    menu:
        mc "I've barely pressed the tip inside and you're already so fucking tight..."
        "Penetrate Her":
            jump graciedeflower

label graciedeflower:

    "The game will optionally display moderate depictions of blood when deflowering girls who haven't yet lost their virginity."
    menu:
        "Would you like to keep this on?"
        "Yes: Blood On":
            scene grsx_a18 with dissolve
            scene grsx_a18 with redflash
            na "Her natural lubrication helps you to slide in... but not without resistence. Despite your precaution... you notice a faint red hue mixed with the fluids coating your shaft."
            mc "(Is that blood? Gracie... my cute little virgin girl. You're completely mine now...)"
            scene grsx_a7 with sdissolve
            na "Despite her pained expression she seems to enjoy every inch of you as you messily begin to conquer her womanhood."
        "No: Blood Off":
            $ blood_on = False
            scene grsx_a20 with dissolve
            scene grsx_a20 with flash
            na "Her natural lubrication helps you to slide in... but not without resistence. Her tight inner walls clench firmly around your shaft as you steal her virginity."
            mc "(My cute little virgin, Gracie. You're completely mine now...)"
            scene grsx_a7 with sdissolve
            na "Despite her pained expression she seems to enjoy every inch of you as you begin to conquer her womanhood."

    grc "I-It feels so big..."
    mc "Does it hurt?"
    grc "A little... y-yes. But..."
    grc "I want it. Please... I want it s-so bad."
    mc "(I've never wanted anything more...)"
    scene grsx_a8 with dissolve
    menu:
        mc "(She's {i}definitely{/i} ready.)"
        "Fuck Her":
            image graciemiss1 = Movie(play="videos/Chapter 1/gracie_miss1.webm")
            jump graciemiss_1

label graciemiss_1:

    show graciemiss1 with sdissolve
    na "She's completely drenched with anticipation... so there's little resistance as you push the full length of your thick cock all the way inside of her. You repeat this with quick, rhythmic motions."
    grc "Aahh... ouch..."
    na "You feel the slick, sticky walls of her pussy as they clench down tightly around you. She whimpers at first... pained... but her pained gasps quickly turn to soft moans of pleasure."
    na "Her body grows limp as she completely gives herself over to you... no longer resisting in the slightest."
    grc "This feels so... it hurts but it's amazing..."
    grc "Oh [mc]. You're making me feel so full right now..."
    grc "D-Don't slow down... d-don't worry about me. I want y-you to feel good.{w} H-Hurt me if you must.{w} My... pussy... is yours."
    mc "(God she's making me so fucking horny talking like that... I should return the favor.)"
    "You can manually respond to Gracie in the upcoming menu by selecting \"Something Else.\""
    menu:
        mc "(How should I respond?)"
        "Call Her Your Slut":
            mc "Do you like the feeling of that big cock stretching you out, you little slut?"
            grc "Y-Yes... I love it... I'm your slut."
            grc "(Oh God! He's making me so horny...)"
        "Call Her Your Slave":

            mc "From now on I completely own you. Your pussy is mine. You are my little cock slave."
            grc "Y-Yes... I love it. I'm yours now..."
        "Something Else":

            $ d1_input = renpy.input("Say something dirty to her...", pixel_width=gui.dialogue_width).strip()
            if d1_input == "":
                $ d1_input="Do you like getting loudly fucked while your mommy is sleeping in the next room?"
            mc "[d1_input]"
            grc "Mmm... you are making me so fucking wet."

    mc "Shit... I'm going to cum if we keep going like this..."
    pause
    menu:
        grc "W-Wait. Can we change positions now?"
        "Continue":
            hide graciemiss1 with sdissolve
            $ renpy.pause (1, hard=True)

    scene grsx_a11 with sdissolve
    $ renpy.pause (1.2, hard=True)
    mc "Yeah. How do you want to do it next?"
    scene grsx_a12 with sfade
    na "She turns around and gets on all fours... presenting you her perfect little ass."
    mc "(Man... what a sight.)"
    grc "Fuck me from behind. Please. I want to do it this way next."
    menu:
        mc "(Gladly...)"
        "Fuck Her":
            image graciedoggy = Movie(play="videos/Chapter 1/gracie_doggy.webm")
            jump graciedoggy

label graciedoggy:

    show graciedoggy with sdissolve
    grc "Ohh!"
    na "She can barely contain her moans as you penetrate her again; this time from behind. There is little tension left, but her virgin pussy is still the tightest hole you've ever filled."
    grc "[mc]! Y-Yes. R-Right there... oh God... p-please don't s-stop..."
    na "You feel her body quivering as you pound her. Your cock responds by twitching."
    grc "{i}*Heavy Panting*{/i}"
    na "The sight of her tight little ass staring up at you is almost enough to send you over the edge..."
    pause
    menu:
        grc "H-Hold on... you're gonna make me... cum. I don't want to cum yet... I want something else first."
        "Continue":
            hide graciedoggy with sdissolve

    na "Proving herself once again to be the perfect girl, she stops you just in time."
    grc "I want it in my mouth, please!"
    if blood_on == True:
        scene grsx_a13 with sdissolve
        na "The blood coating your cock mixed with her fluids seems to startle her a bit."
        mc "(I guess she wasn't expecting my cock to be covered in her own blood and cum...)"
    else:
        scene grsx_a14 with sdissolve
        na "The sight of your cock, mixed with her fluids, leaves her with a perplexed look."
        mc "(I guess she wasn't expecting my cock to be covered in her own cum...)"

    image gracieblow = Movie(play="videos/Chapter 1/gracie_blow2.webm")
    show gracieblow with sdissolve
    play sound "<loop 0.0>audio/sounds/sucking.ogg"
    na "But she seems possessed with arousal and, despite her initial hesitation, begins to suck you off hungrily... taking as much of your shaft into her mouth as possible."
    mc "(Oh... my- f-fuck!)"
    na "She slurps and sucks, staring up at you through her precious eyes."
    pause
    image gracieblow2 = Movie(play="videos/Chapter 1/gracie_blow1.webm")
    show gracieblow2 with sdissolve
    play sound "<loop 0.0>audio/sounds/sucking.ogg"
    grc "(I can taste myself all over him. Oh God I'm so aroused right now... I can feel my pussy leaking all over the carpet.)"
    na "You can't help but stare back at her... taking in this beautiful sight."
    mc "(She's a little clumsy but otherwise she's actually pretty fucking good at this...)"
    mc "(Where have you been all my life?)"
    pause
    menu:
        grc "(I-I think I should stop before he cums... I need him inside of me again.)"
        "Continue":
            stop sound
            hide gracieblow2 with qdissolve
            $ renpy.pause (2.18, hard=True)
            hide gracieblow with qdissolve
            scene grsx_a14 with dissolve
            if blood_on == True:
                mc "(She sucked my cock completely clean...)"
                grc "Please fuck me again. I want you to pound me until I scream..."
            else:
                grc "Please fuck me again. I want you to pound me until I scream..."

    scene grsx_a9 with sfade
    na "She lay on her back once more, this time lifting her legs straight into the air."
    scene grsx_a8 with dissolve
    menu:
        grc "Make me cum, [mc]."
        "Fuck Her":
            image graciemiss2 = Movie(play="videos/Chapter 1/gracie_miss2.webm")
            show graciemiss2 with sdissolve
            na "Her words are like a mating call and you plan to give her the best fuck of her life."
            jump graciemiss_2

label graciemiss_2:

    grc "Ahh!"
    na "She gasps loudly as you fill her with your cock. Completely this time and without hesitation."
    pause
    na "You pound her with repeated thrusts. Her body is quivering once more and she's having an orgasm."
    grc "Aah! Oh God. Mmmm!"
    mc "(Fuck, I can't hold on any longer...)"
    mc "Gracie... I'm going to cum..."
    grc "D-Don't stop."
    na "You understand her completely. She is still mid-orgasm, and you have no intention of depriving her of her experience. So, throwing caution to the wind... you decide not to pull out."
    pause
    stop music fadeout 06.0
    menu:
        mc "(It'll be fine, right?)"
        "Creampie Her":
            show graciemiss2 with flash
            $ renpy.pause (.3, hard=True)
            hide graciemiss2 with flash
            scene grsx_a19 with qdissolve
            scene grsx_a19 with flash
            na "You fill her with your load while her orgasm continues. Her pussy quivers and contracts as you slowly pull out of her."
            scene grsx_a16 with dissolve
            grc "{i}*Panting*{/i}"
            scene grsx_a15 with dissolve
            pause
            jump busted

label busted:

    scene black with dissolve
    pause (2)
    scene grbr_c4 with dissolve
    na "Between the sex you just had in the alcohol still flowing through your system your head is spinning."
    mc "{i}*Panting*{/i}{w} (I can't believe... I just fucked Gracie...)"
    na "She calls out from behind you."
    grc "Hey, [mc]?"
    mc "Yeah?"
    grc "Thank you for such a wonderful night. You were amazing."
    mc "(I should go cuddle with her for a bit... I can't forget this was her first time...)"
    scene grbr_c3 with dissolve
    $ renpy.pause (.3, hard=True)
    play sound "audio/sounds/scare.ogg"
    scene grbr_c2 with vpunch
    mc "(Holy fucking shit!!!)"
    scene grbr_c2 with vpunch
    uk "{size=+4}What in the pig loving fuck is going on in here?! {i}Gracie!?!{/i}{/size}"
    mc "(OH FUCK!)"
    scene busted5 with dissolve
    grc "Oh my God! [mc], go quick!"
    scene busted4 with dissolve
    na "Before you can register what is happening Gracie ushers you towards the window."
    scene busted3 with dissolve
    na "She gets in her father's way... potentially saving you from the beating of a lifetime."
    grc "{size=+3}Dad, no! It's not his fault!{/size}"
    uk "I'm going to skin you alive you fucking weasel!"
    na "You hesitate... not in a hurry to leave Gracie's side."
    mc "(M-Maybe I can reason with him?)"
    mc "(Then again... Gracie did say something about...)"
    mc "(Something, something... \"my dad will {i}fucking kill you?!{/i}\")"
    scene busted2 with sdissolve
    mc "(Nope... fuck that. I'm out! He scared the fucking shit out of me...)"
    scene busted1 with sdissolve
    na "You take one final glance back in the direction of her window hoping to see Gracie. Instead you see Gracie's father... taunting you."
    uk "You have five seconds to get off of my property before I snap your neck like a fucking twig!"
    mc "(Shit... guess I have no choice.)"
    uk "You better wear a butt-plug tonight, boy! That asshole is mine, you hear?!"
    play music "<loop 0.0>audio/magnetic_lullaby.ogg" fadein 04.0
    mc "(Goodbye... Gracie. I'm sorry about this.)"
    scene black with sdissolve
    jump theaccident

label theaccident:

    scene accident6 with sdissolve
    mc "(Shit... I'm still pretty drunk. Not to mention dead tired. I hope I don't get pulled over.)"
    mc "(Man... I can't believe we...)"
    scene accident5 with dissolve
    mc "{i}*Yawn*{/i}"
    mc "(....caught like that. Her dad really wanted to kill me.)"
    mc "(Should I have ran? M-Maybe I should've stayed and...)"
    mc "(Stood up for myself...?)"
    scene accident4 with qdissolve
    $ renpy.pause (.4, hard=True)
    scene accident6 with sdissolve
    mc "(I hope Gracie's okay...)"
    mc "{i}*Yawn*{/i}"
    scene accident4 with sdissolve
    $ renpy.pause (.4, hard=True)
    scene accident5 with qdissolve
    mc "(T-This alcohol is really doing a number on me.)"
    scene accident4 with dissolve
    mc "(S-So...{w} sleepy...)"
    scene accident5 with sdissolve
    mc "(F-Fuck, snap out of it... just a little further...)"
    stop music fadeout 06.0
    scene black with dissolve
    $ renpy.pause (.4, hard=True)
    scene accident3 with dissolve
    mc "{i}*Yawn*{/i}"
    $ renpy.music.set_volume(1.0, delay=0, channel='Chan5')
    $ renpy.music.set_volume(0.0, delay=0, channel='Chan6')
    $ renpy.music.play("<loop 0.0>audio/sounds/horn_silent.ogg", channel='Chan5', loop=True, fadeout=0.6, synchro_start=True, fadein=6.0, tight=None, if_changed=False)
    $ renpy.music.play("<loop 0.0>audio/sounds/horn.ogg", channel='Chan6', loop=True, fadeout=2.0, synchro_start=True, fadein=1.0, tight=None, if_changed=False)
    scene black with sdissolve
    $ renpy.pause (1.2, hard=True)
    scene accident2 with cdissolve
    $ renpy.pause (.7, hard=True)
    $ renpy.music.set_volume(0.0, delay=0, channel='Chan5')
    $ renpy.music.set_volume(1.0, delay=0.5, channel='Chan6')
    show screen system_msg2 with qdissolve
    scene accident1 with cdissolve
    $ renpy.pause (.7, hard=True)
    play sound "audio/sounds/crash.ogg" fadein 0.2
    $ renpy.music.stop(channel='Chan6', fadeout=False)
    $ renpy.music.stop(channel='Chan5', fadeout=False)
    hide screen system_msg2
    scene black with vpunch
    scene black with hpunch
    $ renpy.pause (6.5, hard=True)
    play sound "<loop 0.0>audio/sounds/heartbeat_silent.ogg" fadein 06.0
    play music "<loop 0.0>audio/sounds/sirens.ogg" fadein 0.7
    scene crashsight with cdissolve
    $ renpy.pause (1.5, hard=True)
    mc "(W-What.{w}.{w}. {w}happened...)"
    mc "(M-My head...{w} it...{w} it hurts.)"
    mc "(I-I can't feel my body...)"
    mc "(Is this...{w} am I dying?)"
    mc "(M-Mom? D...Dad?)"
    pause
    mc "(Gracie?)"
    stop sound fadeout 03.0
    stop music fadeout 03.0
    scene black with vsdissolve
    mc "(.....{w}sle...{w}eepy...)"
    uk "{size=-8}Hey... why is this guy naked?{w} Oh shit! We need some help over here!{/size}"
    uk "{size=-5}I think he's dying.{/size}"
    $ renpy.pause (3, hard=True)
    scene march5th with dissolve
    $ renpy.pause (4, hard=True)
    play sound "<loop 0.0>audio/sounds/heart_monitor.ogg" fadein 07.0
    scene hospital_d1 with sdissolve
    $ renpy.pause (.6, hard=True)
    scene black with dissolve
    mc "(What's happening? Am I dreaming?)"
    mc "(There's nothing but... darkness.)"
    mc "(Sleepy... need to sleep some more...)"
    pause (3)
    grc "{i}*Whimper*{/i}"
    mc "Gracie? What's going on?"
    grc "{i}{size=-5}*Sobs*{/size}{/i}"
    grc "[mc]... can you hear me?"
    mc "Yes! I can hear you... I just can't see anything."
    mc "..."
    mc "Gracie?"
    pause (2)
    stop sound fadeout 09.0
    grc "I really... like you, you know?{w} I had hoped we'd... we'd..."
    grc "...Please. Just come out of this... okay? T-There's something I need to tell you..."
    mc "What do you mean? I'm here! I just can't... see anything."
    ".{w}.{w}."
    grc "{size=-10}I can't do this alone...{/size}"
    $ renpy.pause (3, hard=True)
    scene jan4th with dissolve
    $ renpy.pause (4, hard=True)
    scene black with dissolve
    play music "audio/subharmonic_bliss.ogg" fadein 06.0
    mc "(F-F-uck...)"
    mc "(Um... W-Where...)"
    mc "(M-My head... it hurts... I-I can't feel anything.)"
    mc "(W-Where the fuck... am I?)"
    scene hospital_d1 with sdissolve
    mc "(Ahh!)"
    scene black with xdissolve
    mc "(Fuck that's bright...)"
    mc "(Am I hallucinating?)"
    mc "(N-No... that's not it...)"
    mc "(I n-need to...)"
    mc "(To try... to open my eyes again...)"
    scene hospital_d1 with dissolve
    mc "(Everything's so... blurry. What's going on?)"
    mc "(Am I in the hospital? Oh no... what could've happened to me?)"
    scene black with dissolve
    mc "(...)"
    mc "(Need... help...)"
    scene hospital_d2 with dissolve
    mc "..."
    scene hospital_d3 with dissolve
    pause (2)
    scene hospital_a8 with sdissolve
    uk "Oh my God!"
    scene hospital_a10 with dissolve
    uk "(He... he's awake?! Am I tripping? He's looking at me! His eyes are moving!)"
    na "You try to speak, eager to find out what's going on... but the words do not come. Instead, you're met with a strange pain in your throat and chest."
    mc "(Agh, fuck! W-Why can't I say anything?! Why is she looking at me like that?)"
    scene hospital_a1 with dissolve
    uk "D-Don't move! Uhm. Oh my God! Oh my God! Oh my God! I'll—I'll go get the doctor! Just hold on!"
    scene hospital_a3 with dissolve
    uk "D-Don't panic.{w} I'm not panicking."
    scene hospital_a2 with dissolve
    uk "You're panicking."
    scene hospital_a9 with dissolve
    mc "(I don't...{w} I-I can't remember.{w} Anything...)"
    scene hospital_d2 with sdissolve
    mc "(J-Just... need to sleep. J-Just a little more...)"
    scene black with sdissolve
    pause (1)
    stop music fadeout 05.0
    scene hospital_d3 with dissolve
    na "A short time passes before the nurse returns to the room with your doctor."
    scene hospital_a4 with fade
    na "The look of bewilderment on their faces is alarming, to say the least."
    scene hospital_d4 with fade
    na "Despite the ringing in your ears, you can still make out their conversation as they begin murmuring to one another."
    uk "Unbelievable. So you weren't joking."
    uk "It's not even possible... right?"
    uk "Hm...{w} everything's possible, dear."
    scene hospital_a6 with sdissolve
    na "The doctor diligently approaches."
    mc "(W-Why is he looking at me like that? What the hell happened to me?)"
    scene hospital_a7 with dissolve
    uk "Well I'll be damned. You really are awake."
    scene hospital_a5 with dissolve
    uk "Welcome back, Mister [sur]."
    scene hospital_b7 with fadehold
    mc "{i}I remember the time I spent in the hospital like it was yesterday.{/i}"
    play music "<loop 0.0>audio/this_is_not_effortless.ogg" fadein 06.0
    scene hospital_b14 with dissolve
    mc "{i}The medical staff were kind people.{/i}"
    scene hospital_b13 with dissolve
    mc "{i}They made my stay there extremely pleasant.{/i}"
    scene hospital_b3 with fade
    mc "{i}Especially Nurse Victoria...{/i}"
    scene hospital_b6 with fade
    mc "{i}Even if she always acted a little uh... awkward around me.{/i}"
    scene hospital_b5 with dissolve
    mc "{i}Especially when I had certain \"uncontrollable bodily functions.\"{/i}"
    scene hospital_b4 with qdissolve
    pause (.75)
    scene hospital_b5 with qdissolve
    vic "..."
    scene hospital_b2 with dissolve
    vic "{i}Eek!{/i}"
    mc "{i}She'd turn bright red and sprint out of the room like I'd just insulted her mother.{/i}"
    scene hospital_b1 with sfade
    mc "{i}But the first few days... the pain I felt... not being able to move or control a single hair on my body... it was hell.{/i}"
    mc "{i}I was a mere shell of a person. It felt like every bit of life had been drained from my mind and body.{/i}"
    scene hospital_b12 with dissolve
    mc "..."
    mc "{i}But all of that paled in comparison to my first serious talk with my doctor. And I'm not even talking about the pain in my throat and lungs... or my ill, raspy sounding voice.{/i}"
    scene hospital_c6 with fadehold
    mc "W-What happened to me, Doctor?"
    scene hospital_c8 with qdissolve
    doc "{i}*Sigh*{/i} Where should I start..."
    scene hospital_c3 with dissolve
    stop music fadeout 07.0
    doc "[mc]... you've been in a coma for nearly ten years."
    scene hospital_c3 with vpunch
    scene hospital_c4 with qdissolve
    mc "{i}The shock that sent through my system nearly caused me to pass out. Ten years of my life... gone. Flushed down the toilet.{/i}"
    mc "{i}But if you thought that was the worst of the news I received that day, you'd be wrong.{/i}"
    scene hospital_c5 with qdissolve
    doc "I'm so sorry about your parents, [mc]."
    scene hospital_c4 with qdissolve
    doc "(This poor guy has been through enough... I don't have the heart to tell him the \"other thing\" that happened that day...)"
    scene hospital_z0 with sfade
    mc "{i}I was an only child, you see. My mother gave birth to me when she was in her later years...{/i}"
    mc "{i}And my parents... they came to visit me every day of every week. They prayed, and prayed, and begged for a miracle. No matter what the medical professionals told them, they refused to believe that I'd never come out of it. That I wouldn't wake up from this nightmare.{/i}"
    mc "{i}But the toll my accident took on them; the stress of losing their only son was... irreversible.{/i}"
    mc "{i}Thankfully, they never did agree to pull the plug. Even after all those years. Even after they were gone... they made sure I was going to live. They gave me another chance at life.{/i}"
    scene hospital_c2 with sfade
    mc "Doc... why was I kept on life support? Even so long after my parents were gone?"
    scene hospital_c1 with qdissolve
    doc "Son... your parents loved you very much. They paid for your treatment for the next thirty years. Your father... he was a stubborn one. About damn convinced even me that you'd wake up one day... despite my obvious skepticism."
    scene hospital_c3 with qdissolve
    doc "He'd have brought down the entire system... sued us and the state to hell and back if we pulled the plug."
    scene hospital_c1 with qdissolve
    doc "The fact that you woke up is a miracle. In all my years as a medical professional... I've never seen anything like it. You're an anomaly. But as for whether or not you'll be able to walk again... I-I don't know."
    play music [ "audio/please_advise.ogg", "audio/arc_of_the_sun.ogg" ] fadein 07.0 fadeout 08.0
    scene hospital_c2 with qdissolve
    mc "{i}And for that reason... because my parents fought for me... I fought harder than I ever had before.{/i}"
    scene rehab4 with fadehold
    mc "{i}After a while, the pain subsided a little. Well, either that or I got used to it.{/i}"
    mc "{i}Eventually... gradually... the feeling returned to my broken body. I could move again. Albeit, weakly.{/i}"
    mc "{i}But I'd made it this far. Defied all odds. And despite what the doc said, I was going to walk again.{/i}"
    scene rehab3 with dissolve
    mc "{i}And that's exactly what I did.{/i}"
    scene rehab2 with xdissolve
    scene rehab2 with vpunch
    mc "{i}Not without a challenge, of course.{/i}"
    mc "{i}But no matter how many times I fell...{/i}"
    scene rehab3 with dissolve
    mc "{i}I always got back up.{/i}"
    scene black with sdissolve
    mc "{i}Soon... my life would return to normal.{/i}"
    mc "{i}The accident caused me to lose a rather large portion of my memory. Especially from the few years leading to it.{/i}"
    mc "{i}What bothered me the most was the struggle to remember faces. Even mom and dad's were... hazy and distorted. I can almost picture them... but something is just off.{/i}"
    scene office0 with sdissolve
    mc "{i}So I decided to take up photography. Life's memories are precious... and it's all too easy to lose them.{/i}"
    mc "(Whew, finally done. This post work will be the death of me.)"
    scene properties1 with sdissolve
    mc "{i}Thanks to the inheritance I got from my parents... I was even able to open my own agency to recruit local photographers.{/i}"
    mc "{i}I'm not sure how I did it but the business was a huge success. We booked all sorts of high-profile gigs. Weddings, modeling shoots, birthday parties for celebrities... you name it.{/i}"
    scene properties0 with dissolve
    mc "{i}Soon I was a world-renowned photographer making “fuck you money” and living a life of wealth and luxury.{/i}"
    scene properties2 with sdissolve
    mc "{i}I bought a house...{/i}"
    scene properties3 with sdissolve
    mc "{i}A damn nice one, I should add. Has a pool and everything.{/i}"
    scene properties4 with sdissolve
    mc "{i}But more important than material possessions were the friendships I developed along the way.{/i}"
    scene berncel3 with sfade
    mc "{i}I wouldn't be anywhere near as successful without the wisdom and guidance from Bernie: my partner in crime.{/i}"
    scene berncel5 with qdissolve
    ber "Welp, I'm not sure how..."
    scene berncel4 with qdissolve
    ber "But we did it!"
    scene berncel2 with dissolve
    ber "You stupid, prepubescent son of a bitch... we're going to be rich!"
    scene berncel1 with dissolve
    ber "Oouhh..."
    mc "Did you break your hip again? Should I call an ambulance?"
    scene berncel0 with dissolve
    ber "Heh... fuck yourself."
    scene berncel3 with dissolve
    ber "(Man... he really did it. The damn kid managed to make his dreams come true in such a short time. He really is an amazing photographer and businessman. He may be a prick... but I couldn't be prouder.)"
    stop music fadeout 7.0
    scene black with sdissolve
    $ renpy.pause (1, hard=True)
    scene many_years with sdissolve
    $ renpy.pause (4, hard=True)
    scene br5 with sfade
    mc "{i}It's been many years since I woke up in the hospital... thousands of miles from home... confused and unable to move. Today I spend most of my time working out at the gym... or at the office... or out doing shoots...{/i}"
    scene br8 with fade
    mc "{i}Or even hooking up with the occasional model. For all of my “problems,” I can at least say that I was blessed with unwavering good looks. And not to mention... ahem... well endowed.{/i}"
    scene br9 with dissolve
    mc "(But there's nothing I look forward to more than...)"
    mc "{i}*Yawn*{/i}"
    scene br7 with dissolve
    mc "(My bed. God damn, this bed is... way too comfortable.)"
    scene br12 with dissolve
    mc "{i}*Yaaawn*{/i}"
    mc "(Will I... dream of her again?)"
    scene br11 with dissolve
    mc "(So tired.)"
    scene black with sdissolve
    na "After a hard day's work, you slowly drift into a peaceful sleep."
    scene black with dissolve
    $ renpy.pause (4, hard=True)
    jump dayone

label dayone:

    play music "audio/neither_sweat_nor_tears.ogg" fadein 06.0
    scene drm23 with sdissolve
    mc "(Ugh. One of {i}those{/i} dreams again.)"
    mc "(I mean... not that I'm complaining. I just wish I could...)"
    scene drm20 with sdissolve
    grc "There you are!"
    scene drm22 with qdissolve
    mc "Here I am... {i}*Smile*{/i}"
    mc "(That's \"Gracie,\" aka \"mystery dream girl.\")"
    mc "(I have these intense dreams of her all the time. They're not like normal dreams. For one, I can see her face vividly... as if she were a real person.)"
    mc "(And although I have no idea who she is, she seems... familiar somehow.)"
    mc "(Did I know her in a past life? Is she someone I knew from before the accident? Another lost memory?)"
    mc "So... you going to tell me how we know each other this time?"
    scene drm20 with qdissolve
    grc "{i}*Giggle*{/i} What do you mean? Are you saying you don't remember me? You're being rude again!"
    scene drm22 with qdissolve
    mc "Yeah, yeah... don't get cheeky. You're not going to tell me anyway."
    mc "(There's just one more thing about these damn dreams. Something that makes them, ah... even more unique than the others...)"
    scene drm19 with dissolve
    mc "(And that is... one way or another... they always turn sexual. I'm like... a \"chronic wet dreamer.\")"
    image graciehlick = Movie(play="videos/chapter 1/gracie_lickh.webm")
    stop music fadeout 06.0
    show graciehlick with sdissolve
    grc "Mm, I love the way your big cock feels when you ram it down my little throat."
    pause
    scene drm18 with sdissolve
    grc "I'm already soaking wet... come."
    scene drm0 with dissolve
    $ renpy.pause (1, hard=True)
    play sound "<loop 2.9>audio/sounds/alarm.ogg"
    scene br4 with dissolve
    mc "..."
    mc "(Shit! That was starting to get good.)"
    mc "(Fffu- so tired.)"
    scene br3 with dissolve
    stop sound
    pause (1)
    scene br2 with dissolve
    play music "audio/key_to_your_heart.ogg" fadein 05.0
    mc "(Welp. No time to fret!)"
    scene black with dissolve
    na "You spend the next thirty minutes getting ready and head to the office."
    scene driveway0 with dissolve
    mc "Another day, another dollar!"
    jump officed1

label officed1:

    scene bernb8 with fadehold
    mc "Watcha doing, grandpa? Did you remember your Life Alert today?"
    scene bernb7 with dissolve
    ber "What'd I tell you about calling me grandpa?! You want me to show you my famous headlock again, cum-for-brains?"
    scene bernb6 with qdissolve
    mc "Haha, I think I'm all set on that."
    scene bernb5 with qdissolve
    ber "You better be. No new jobs just yet... but you might want to straighten up your office a bit."
    stop music fadeout 12.0
    scene bernb4 with qdissolve
    mc "Huh? Why's that?"
    scene bernb2 with qdissolve
    ber "Did you forget already? Jeez. I'm starting to think you have dementia. You got an interview with that amateur photographer today."
    scene bernb3 with qdissolve
    mc "Ahh right! The new girl. Brooklyn, was it?"
    scene bernb5 with qdissolve
    ber "That's right. You're sharper than you look."
    scene bernb4 with qdissolve
    mc "I had a look through some of her shots. She may be an amateur, but she knows what she's doing. She'll be a nice addition to the team."
    scene bernb2 with qdissolve
    ber "I hope so! And don't end up smitten, young man."
    scene bernb3 with qdissolve
    mc "Huh? Why do you say that?"
    scene bernb2 with qdissolve
    ber "Well... I heard she's a looker. (And for both of our sakes, I'm praying that's true.)"
    scene bernb3 with qdissolve
    mc "(I see Bernie's in typical fashion today. He says that about every new girl we hire.)"
    mc "Right. I'll be ready, then. Thanks for the heads up, Bern!"
    scene bernb5 with qdissolve
    ber "Yeah, yeah. I'll be in my office."
    stop music fadeout 10.0
    scene bernb3 with qdissolve
    mc "Ah-huh. Careful not to break a hip."
    scene bernb0 with qdissolve
    ber "Fuck yourself, kid."
    scene brk21 with fadehold
    play music "audio/si_senorita.ogg" fadein 08.0
    na "A short time passes before the new girl arrives. You greet her at the door."
    scene brk0 with dissolve
    brk "Mister [sur]?"
    scene brk1 with qdissolve
    mc "That's me."
    mc "(She's gorgeous. Bernie really wasn't kidding.)"
    mc "Miss Brooklyn, was it? That's a beautiful name."
    scene brk0 with qdissolve
    brk "Y-Yes sir. You can just call me Brooke, though."
    scene brk1 with qdissolve
    mc "It's a pleasure to meet you, Brooke."
    scene brk0 with qdissolve
    brk "Likewise! I'm such a big fan of your work, so forgive me if I seem a little nervous."
    scene brk1 with qdissolve
    mc "Hey, don't sweat it. We've all been there, right? Please, come have a seat."
    scene brk10 with dissolve
    na "You get a nice view of her ass as she moves to sit down."
    mc "(Shit! What a booty.)"
    na "And you return to the seat at your desk."
    scene brk6 with sdissolve
    mc "(If I didn't know better I'd mistake her for one of the junior models.)"
    scene brk5 with xdissolve
    brk "T-Thank you for your consideration. I'm very eager to join the team... i-if you'll have me."
    scene brk7 with xdissolve
    mc "(I like that she's taking some initiative here.)"
    mc "It's no problem at all. I've had a look through your portfolio and I have to say I'm impressed. I love your work!"
    scene brk5 with xdissolve
    brk "Hearing you say that makes me very happy! I'm extremely passionate about what I do, and I can see that you are as well."
    scene brk6 with xdissolve
    mc "It's true... I'd be lost without this hobby if I'm being honest. I was in a coma for many years, you see... and when I came out of it I struggled quite a lot with memory."
    mc "I often couldn't remember what day of the week it was... hell... I struggle to remember my own parents faces."
    scene brk7 with xdissolve
    mc "So I had the idea to just... take pictures. Of everything. Especially the things that mean something to me."
    mc "Anyway, I don't want to bore you with my past..."
    scene brk5 with qdissolve
    brk "Oh, not at all! Your story is quite breathtaking actually. I wish I could say my own was just as mysterious... but in reality I find that the world... no matter how filthy or rundown the location... is a beautiful place filled with mystery and wonder."
    scene brk7 with xdissolve
    mc "Well we all have our reasons. I think yours are just as good as the others."
    scene brk6 with xdissolve
    na "She smiles at you, and for a moment you find yourself admiring her before you move onto the matter at hand."
    na "You give her the usual spiel and ask a few questions."
    scene brk9 with dissolve
    na "Throughout the interview, she's completely engaged in the discussion and seems eager to learn. She even asks for tips and pointers."
    scene brk4 with dissolve
    na "But the elephant in the room... the thing you can't help but notice- she seems completely smitten by you."
    scene brk3 with dissolve
    na "Even Bernie seems to notice."
    scene brk20 with fade
    mc "(I'm positive that she will make the perfect addition to the team.)"
    scene brk15 with dissolve
    na "And she struggles to contain her excitement when you tell her."
    scene brk19 with dissolve
    brk "Wow! Thank you! You have no idea how excited I am to work with such an incredible group of people!"
    scene brk18 with dissolve
    brk "Oh, crap. S-Sorry... hugging you was probably a little unprofessional..."
    scene brk17 with xdissolve
    brk "(I need to remember that he's my boss now. But he is so... handsome. If I'm not careful I will end up crushing on him.)"
    scene brk16 with xdissolve
    mc "Heh, you don't have to apologize. It's perfectly fine."
    mc "(She has the most amazing eyes. I could easily fall for her.)"
    scene brk13 with xdissolve
    mc "S-So... come by the office again tomorrow?"
    scene brk15 with xdissolve
    brk "That would be perfect. Thank you so much."
    scene brk14 with xdissolve
    mc "No problem. I actually won't be in the office... but my associate, Bernie, will walk you through everything."
    scene brk13 with xdissolve
    brk "It was so nice to meet you. I'm so looking forward to getting to know you—{w} I mean.. I'm looking forward to working with you!"
    scene brk16 with xdissolve
    mc "It was nice to meet you as well, and I'm also looking forward to it."
    scene brk13 with xdissolve
    brk "Well... see you soon boss!"
    scene brk14 with dissolve
    mc "See you later, Brooke!"
    scene brk12 with fadehold
    na "The rest of your day goes off without a hitch. You spend most of it editing some risqué photos you'd taken at the last modeling shoot before getting ready to head home."
    scene black with sdissolve
    "Radiant uses a unique choice system called \"Crucial Choice.\" Every major decision you make will shape your personality and has the potential to impact future events. In this instance, your decision will have a greater than normal impact on your {color=#0085FA}Psyche.{/color}"
    "Just this once, you'll be shown exactly how each decision affects you. You do not have to follow any one path, since your Psyche can be multifaceted, but choose wisely. More importantly: play the game how you want to play!"
    stop music fadeout 05.0
    scene bernb8 with sdissolve
    mc "I'll see you soon, Bern. Call me if you need anything."
    scene bernb5 with dissolve
    ber "Alright man. Drive safe.{w} And don't go killing anyone again."
    scene bernb4 with xdissolve
    mc "(Ouch. That was cold even for this cranky old bastard. How do I respond to that?)"
    scene bernb4 with blueflash
    scene bernb4 with blueflash
    scene bernb4 with blueflash
    menu:
        "The blue flash means you've reached a crucial choice that will impact your {color=#0085FA}Psyche{/color}. Your Psyche contains three variables: Lust, Purity and Darkness."
        "Crack Back <Lust>":
            $ lust +=3
            scene bernb6 with xdissolve
            mc "Hah! You're one to talk. Are people even allowed to have a driver's license at your age?"
            scene bernb2 with xdissolve
            ber "Hey... I'll have you know that I once beat Jeff Gordon in a circuit."
            scene bernb3 with xdissolve
            mc "{i}*Rolling eyes*{/i} Yeah, I'm sure."
            jump homent1
        "Scold Him <Purity>":

            $ pure +=3
            scene bernb6 with xdissolve
            mc "Hey! That's not very nice, Bernie."
            scene bernb1 with xdissolve
            ber "Yeah, well... shove it! I'm still pissed off about that Life Alert comment this morning. Had to look it up on the Snoogles."
            scene bernb3 with xdissolve
            mc "You mean Snoogle? Wait... when'd you learn how to use a computer?"
            jump homent1
        "Threaten Him <Darkness>":

            $ dark +=3
            scene bernb3 with xdissolve
            mc "Hey, watch your mouth gramps or I'll break your fucking hip myself."
            scene bernb1 with xdissolve
            ber "H-Hey... take it easy. I was just kidding around."
            scene bernb3 with xdissolve
            ber "(He's been acting a little strange lately. But threats? That's not really like him...)"
            mc "Heh. Sure Bernie, me too. But I don't appreciate you bringing up my past like that."
            mc "(He's right, I should probably take it easy. I don't know why I've been so irritable lately.)"
            jump homent1

label homent1:

    scene bernb0 with dissolve
    ber "Whatever. See ya later, kid."
    scene black with sdissolve
    play music "audio/timeless.ogg" fadein 06.0
    na "You take Bernie's advice and drive home safely."
    scene tubsolo2 with sdissolve
    mc "When you arrive, you decide to take a dip in the hot tub."
    mc "(What a nice night.)"
    mc "(Working at the office was pretty fun today. As usual. Bernie cracks me up.)"
    mc "(And I got to meet Brooke today. She seems really sweet... and there's no denying that she's attractive.)"
    menu:
        mc "(The question is... am I attracted to her? Is she even my type?)"
        "Definitely":
            $ lust +=1
            mc "(God yes. She's gorgeous and she seems like my kind of girl.)"
        "Not Really":

            $ dark +=1
            mc "(Eh... not really my kind of girl to be honest. But maybe I'll change my mind when I get to know her better.)"
            mc "(Besides... if I play my cards right... who says I need to stick to one woman? Variety is the spice of life.)"

    mc "(I can't help but feel like she has a little crush on me even though we spoke for all of maybe two hours today.)"
    scene tubsolo1 with sdissolve
    mc "(I wonder if she has a boyfriend. Or a husband, maybe?)"
    mc "(But... should I think of her that way? She {i}is{/i} my employee now.)"
    menu:
        mc "(Do I want to pursue some kind of physical or intimate relationship with her?)"
        "Yes":
            $ brk_rel = True
            mc "(Heh. I don't know... would be a little hard to resist if the opportunity arose.)"
        "No":
            mc "(Heh. Probably not a good idea to think of her like that... even if the opportunity arose.)"

    mc "(But maybe I should regardless. After all...)"
    mc "(I've been a little lonely lately.)"
    mc "(Guess one-night stands can only get you so far. They're not exactly, uh... fulfilling.)"
    scene tubsolo1 with sdissolve
    mc "(Not to mention I own the place. That's one of the benefits of being your own boss. You get to make the rules.)"
    mc "(I have a feeling it's going to be a hell of a year... something big is coming.)"
    stop music fadeout 9.0
    scene tubsolo0 with sdissolve
    mc "(Eh, I should hop out of the tub. My skin is pruning. I'm a little tired anyway.)"
    scene br8 with sfade
    na "You head to bed and make it a point not to set the alarm."
    scene br12 with sdissolve
    na "After the excitement of tomorrow's day off dies down, you drift into a peaceful sleep."
    scene br11 with sdissolve
    scene black with dissolve
    jump dreamn1

label dreamn1:

    play music "audio/glacier.ogg" fadein 04.0
    scene drm23 with sdissolve
    mc "(Again? Man, these dreams are becoming more and more frequent.)"
    mc "(This one is different though. It feels more... real.)"
    scene drm16 with sdissolve
    $ renpy.pause (1, hard=True)
    scene drm17 with qdissolve
    grc "Hey good looking!"
    scene drm16 with qdissolve
    mc "Hello again, Gracie."
    scene drm15 with dissolve
    grc "Hehe. Why do you look so sad?"
    scene drm14 with qdissolve
    mc "I-I'm not sure, actually. (Why {i}do I{/i} feel sad?)"
    scene drm13 with dissolve
    $ renpy.pause (.4, hard=True)
    scene drm12 with dissolve
    grc "Come over here. I'll make you feel better."
    scene drm11 with dissolve
    na "You feel her warmth radiate through you."
    pause (1)
    scene drm7 with dissolve
    mc "Who... are you?"
    scene drm9 with qdissolve
    grc "I'm Gracie."
    scene drm8 with qdissolve
    mc "I know that already but...{w} how do we know each other? You never answer me when I ask these things."
    scene drm9 with qdissolve
    grc "{i}*Sigh*{/i} Do you really want to know?"
    scene drm8 with qdissolve
    mc "(Wait... is she actually going to tell me this time?)"
    mc "Y-Yes! I've only been asking the same question for a few years now! Of course I'd like to know."
    scene drm9 with qdissolve
    grc "We're lovers."
    scene drm8 with qdissolve
    mc "...Are you messing with me again?"
    scene drm20 with sdissolve
    grc "Heh, sorry."
    grc "The truth is..."
    grc "I'm... a lost memory."
    scene drm21 with qdissolve
    mc "..."
    mc "You're not making a whole lot of sense..."
    scene drm20 with qdissolve
    grc "It's true!"
    grc "We're connected. You changed my life."
    scene drm21 with qdissolve
    mc "How? How do we even know each other?"
    scene drm20 with qdissolve
    grc "Well... we don't, really. We only spent one night together."
    scene drm21 with qdissolve
    na "You take a moment to process what she's saying... a bit taken aback by the fact that she's actually answering you."
    mc "Just one night, huh?"
    scene drm20 with qdissolve
    grc "Yeah. The night of your accident."
    scene drm21 with qdissolve
    mc "Heh..."
    scene drm20 with qdissolve
    grc "What is it?"
    scene drm21 with qdissolve
    mc "It's..."
    mc "Nothing."
    mc "(I know this is just a dream but...)"
    mc "(If what she's saying is true that would actually make sense. I mean... I don't remember a single thing from that night. Let alone the months leading up to it.)"
    mc "Can I ask you something else?"
    scene drm20 with qdissolve
    grc "Of course!"
    scene drm21 with qdissolve
    mc "I know you said it was only one night... but the way I'm feeling now..."
    mc "Did we... love each other?"
    grc "..."
    scene drm20 with qdissolve
    grc "I don't know, we... didn't know each other for long."
    grc "But..."
    grc "I loved you."
    grc "After that night you were all I could think about."
    scene drm4 with sdissolve
    na "She rests her head on your chest and you sit together in silence."
    na "You wrestle with your thoughts... watching the passing clouds as you try to make sense of what she's told you. You desperately want to remember."
    stop music fadeout 05.0
    scene drm3 with qdissolve
    grc "Hey, [mc]?"
    scene drm4 with qdissolve
    mc "Yeah?"
    scene drm3 with dissolve
    grc "{size=-10}Wake up.{/size}"
    scene black with xdissolve
    pause (.3)
    play sound "audio/sounds/doorbell_1.ogg"
    scene br1 with vpunch
    mc "..."
    mc "(That was intense.)"
    scene br2 with dissolve
    mc "(That dream... it was the most vivid dream I think I've ever had.)"
    play sound "audio/sounds/doorbell_1.ogg"
    mc "(Huh? Is someone...?)"
    na "You glance at the clock and realize you slept in pretty late."
    mc "(Shit... it's almost noon.)"
    play sound "audio/sounds/doorbell_2.ogg"
    mc "(Ah, fuck. Someone's at the door. I better hurry up and go get that.)"
    scene br0 with dissolve
    menu:
        mc "(Should I ah... put some clothes on or just go answer it?)"
        "Get Dressed First":
            $ ali_pure +=1
            $ mad_pure +=1
            $ liv_pure +=1
            $ dressed = True
            mc "(Can't answer the door like this. I need to put some clothes on.)"
            play sound "audio/sounds/doorbell_2.ogg"
            mc "{size=+5}I'm coming, I'm coming! Hold on a damn second, would you?!{/size}"
            jump thearrival
        "Just Answer It":

            $ ali_lust +=1
            $ mad_lust +=1
            $ liv_lust +=1
            $ dressed = False
            play sound "audio/sounds/doorbell_2.ogg"
            mc "(Fuck... no time to get dressed. I better hurry up and just answer the door.)"
            jump thearrival

label thearrival:

    scene brdoor with sfade
    mc "Just a minute! I'm coming!"
    scene door2 with dissolve
    mc "(Man. Nothing like waking up to someone cranking your doorbell on your day off. This better not be a Goddammed Jehovah's Witness.)"
    scene door1 with sdissolve
    na "A strange weight rests on your shoulders as you squeeze the latch and pull open the door."
    play music "<loop 0.0>audio/hero_s_ascent.ogg" fadein 06.0
    scene black with sdissolve
    $ renpy.pause (2, hard=True)
    scene trip16 with sdissolve
    na "Before you stands three young girls... huddling together and inspecting you with a nervous curiosity."
    na "At first glance you feel the urge to tell them you're not interested in whatever cookies they're selling. But after a moment of reflection and further inspection..."
    scene trip15 with sdissolve
    na "You begin to realize what you're seeing... and it sends goosebumps down your spine."
    mc "(I-It can't be...)"
    na "The familiar redhead catches your eye first. She stares back at you with uncertainty."
    scene trip14 with dissolve
    mc "(G-Gracie? N-No... it's not her, but she looks so much like her it's scary...)"
    scene trip13 with dissolve
    mc "(They all do. What the hell is going on?)"
    na "The brunette gives off a different... almost angry vibe. Rather than staring at you like the others, she seems to avoid it at all costs."
    scene trip11 with dissolve
    mc "(I must be on an episode of \"Scare Tactics\" or something. That's what this is, right?)"
    mc "(Because unless my eyes are playing tricks on me...)"
    scene trip8 with dissolve
    mc "(I'd say that redhead is a... slightly younger version of the girl from my dreams.)"
    mc "(And they {i}all{/i} look like they could be her sisters.)"
    mc "(Alright, alright. Hold it together. It's just a strange coincidence. Stop gawking at them for fucks sake.)"
    mc "Uhm..."
    mc "H-Hello. C-Can I help you?"
    scene trip12 with dissolve
    na "The brunette doesn't seem to react but the redhead and the blonde look at each other... as if unsure how to respond."
    scene trip10 with dissolve
    na "After a few awkward moments of silence, the blonde finally speaks up."
    scene trip11 with dissolve
    bld "H-Hi. S-Sorry about this... but um..."
    bld "Is your name [mc] [sur]?"
    scene trip10 with xdissolve
    mc "Yes... that's me. Who's asking?"
    scene trip9 with dissolve
    na "The blonde and the redhead look at each other once more... wide-eyed and visibly shaken."
    scene trip8 with dissolve
    na "This time... the redhead speaks up."
    scene trip7 with xdissolve
    red "H-Hi. I know this is a little strange b-but... can we come in and talk to you?"
    scene trip8 with xdissolve
    mc "I'm sorry, but I'm really not looking to buy anything if that's what this is..."
    scene trip5 with qdissolve
    bld "N-No! We're not selling anything. Please just... hear us out for a moment. It's really important."
    scene trip2 with qdissolve
    bru "Let's just go you guys. This is ridiculous."
    scene trip3 with xdissolve
    bld "Shush, you!"
    scene trip6 with qdissolve
    na "The redhead gives you her best pleading look."
    scene trip8 with qdissolve
    red "Pretty please?"
    scene trip6 with xdissolve
    mc "(Well... I'm confused as all hell but whatever it is... it does sound important.)"
    mc "(And I can't stop staring at her. She looks so much like Gracie. Hell, they all do.)"
    mc "(It'd probably haunt me if I turned them away at this point. It's not often that three spitting images of a girl you've been fucking in your dreams just... show up at your house.)"
    mc "Y-Yeah. Forgive me if I acted rude. Please come on in."
    scene tripb20 with fadehold
    if dressed == False:
        mc "I apologize for not inviting you in sooner, girls. What is it you'd like to talk about?"
        scene tripb22 with dissolve
        na "Instead of answering, the trio all seem a little embarrassed by something..."
        scene tripb21 with dissolve
        bru "Any chance we could have this discussion while you're not half-naked?"
        scene tripb00 with dissolve
        mc "(Shit!)"
        scene tripb22 with dissolve
        mc "I-I'll be right back, ladies."
        scene black with dissolve
        na "You quickly dress and return to the front entrance to greet the girls once more."
        scene tripb20 with dissolve
        mc "Sorry about that. I rushed to the door and completely forgot to dress myself."
        scene tripb19 with dissolve
        bld "It's okay! {i}I don't mind.{/i}"
        scene tripb20 with dissolve
        mc "Thanks..."
    else:
        mc "(Whew. Guess it's a good thing I got dressed... otherwise this would be pretty awkward.)"

    mc "So what can I do for you girls?"
    scene tripb18 with fade
    na "The one that looks strikingly similar to your dream girl steps forward. She speaks as if she's rehearsed what she'll say."
    $ olivia_name = renpy.input("What is her name? (Leave this blank to use her \"true name.\")")
    if olivia_name == "":
        $ olivia_name="Olivia"

    liv "M-My name is [liv]."
    scene tripb1 with fade
    liv "And these are my triplet sisters..."
    scene tripb16 with sdissolve
    $ allison_name = renpy.input("What is her name? (Leave this blank to use her \"true name.\")")
    if allison_name == "":
        $ allison_name="Allison"

    liv "[ali]..."
    scene tripb15 with sdissolve
    $ maddison_name = renpy.input("What is her name? (Leave this blank to use her \"true name.\")")
    if maddison_name == "":
        $ maddison_name="Maddison"

    liv "And [mad]."
    scene tripb14 with sdissolve
    stop music fadeout 05.0
    liv "And uhm..."
    liv "I-I don't know how else to say this, but..."
    if tbed == True:
        pause
        scene tripb18 with dissolve
        liv "You're...{w} our father."
        liv "And we were sent by mom to seek you out and ask if we can stay with you... even if just for a little while."
        mc "(.{w}.{w}.M-My...{w} Daughters?!)"
        scene tripb0 with sdissolve
        na "While you're skeptical... the news and the flood of emotion that comes with it is too much to process. Your head throbs and you drop to your knees, stunned."
        scene tripb12 with dissolve
        ali "Daddy?!"
        scene tripb0 with sdissolve
        na "The blonde—no, \"your daughter\" [ali] rushes to your aid as you wince in agony... a flash of pain hitting you very suddenly."
        scene tripb11 with dissolve
        mad "Ugh. {i}\"Daddy?\"{/i} Are you serious right now? We don't even know him!"
    else:
        scene tripb13 with dissolve
        liv "We...{w} need a place to live..."
        liv "We were sent by mom,{w} Gracie... to seek you out and ask if we can stay with you... even if just for a little while."
        scene tripb18 with dissolve
        mc "You were... what? (Did she just say... Gracie?!)"
        scene tripb0 with dissolve
        na "Your head throbs. The pain is so severe that you drop to your knees, stunned."
        scene tripb12 with dissolve
        ali "[mc]?!"
        scene tripb11 with dissolve
        mad "Ugh. He hates the idea of us being here so much that he's having a heart attack or something! I should've known this was a bad idea!"

    scene tripb10 with dissolve
    na "Frustrated, she storms off into the nearest room... slamming the door behind her."
    mc "W-Wait! That's my..."
    play sound "audio/sounds/doorslam.ogg"
    scene tripb9 with xdissolve
    $ renpy.pause (.3, hard=True)
    scene tripb8 with xdissolve
    mc "..{w}Bedroom...."
    mc "(Did she just storm off and slam the door to my own bedroom?{w} She can't be serious...)"
    scene tripb4 with dissolve
    mc "You look up from your daze..."
    na "[liv], your [dau]... rests her hands on your shoulders to comfort you. You feel the blonde, [ali]'s little hand resting on your back."
    scene tripb7 with xdissolve
    liv "I-I'm sorry to come out with it so suddenly like that... I just didn't know how else to say it..."
    scene tripb4 with xdissolve
    mc "No... um..."
    mc "I'm the one who's sorry.{w} Here, let me get up."
    scene tripb3 with dissolve
    mc "I didn't mean to overreact like that. It's just sometimes I get these sudden migraines and... I think the shock of what you just said triggered one. I'm okay now, though."
    mc "Is she... going to be okay? Should I go... uh... talk to her?"
    scene tripc3 with qdissolve
    liv "No, you don't have to do that. I'm pretty sure she'll be okay, but..."
    scene tripb2 with qdissolve
    ali "I'll go talk to her!"
    scene tripc5 with dissolve
    liv "Thanks, [ali]... but I think she might be a little annoyed with you right now. I'll go talk to her... you stay with [mc], okay?"
    scene tripb2 with qdissolve
    ali "O-Okay, no problem!"
    scene tripc2 with sfade
    na "She leaves to comfort [mad]. You turn to [ali], who stares back at you nervously."
    mc "Can we go sit down? My head still hurts a little..."
    scene tripc1 with qdissolve
    ali "S-Sure!"
    jump alitalk1

label alitalk1:

    scene lrali8 with fadehold
    na "You make your way to the living room with her. She nervously fidgets with her hands while you speak."
    mc "It's [ali], right...?"
    scene lrali7 with dissolve
    ali "Y-Yes. But..."
    scene lrali6 with xdissolve
    $ ali_nick = renpy.input("What is her nickname? (Leave this blank to use her \"true nickname.\")")
    if ali_nick == "":
        $ ali_nick="Allie"
    scene lrali5 with xdissolve
    ali "You can just call me [anick], if you want."
    scene lrali6 with xdissolve
    play music "<loop 0.0>audio/dreamland.ogg" fadein 09.0
    mc "[anick], got it. That's a cute name."
    mc "So listen... before we talk about anything..."
    mc "And pardon me if this comes across as rude... but this isn't some sort of elaborate prank, right?"
    scene lrali7 with xdissolve
    ali "Hehe... n-no! Of course it's not! We wouldn't do that to you!"
    scene lrali2 with xdissolve
    mc "(She's telling the truth...)"
    mc "Well in that case, [anick]..."
    mc "I need to tell you something."
    mc "You see... I was in a horrible accident when I was young. It left me in a coma for a very long time and... the truth is... I don't remember much of anything. There's very little left of my memory from that time."
    mc "And well... to be honest I'm just really confused right now. I have no idea what's going on. This is all just so surreal."
    scene lrali5 with xdissolve
    ali "M-Mom told me that might be the case... about your memory. And well... she told me if it was, that I should give you this. I don't know what it says but..."
    scene lrali4 with dissolve
    na "She pulls a small sealed envelope from her pocket and hands it to you. On the front is a handwritten label with your name on it. You slowly open it and retrieve the paper from inside."
    scene letter with fade
    pause (1)
    menu:
        mc "(So this is a letter from dream girl...)"
        "Read The Letter":
            if tbed == True:
                jump lettertrue
            else:
                jump letterfalse

label lettertrue:

    grc "{i}Hi, [mc]...{/i}"
    grc "{i}You may not remember me. We didn't know each other long before your accident... but I still remember you very well. You see... you and I shared a very special moment together on the night of your accident. It wasn't expected... it wasn't planned.{/i}"
    grc "{i}Heck... we were complete strangers prior to that day...{/i}"
    grc "{i}But I've never forgotten. How could I? You were so sweet to me. You came to my rescue and swept me off my feet. And although I knew nothing about you... by the time you left I felt nothing but love for you.{/i}"
    grc "{i}I've been contemplating what to say for a very long time... but I want to keep this brief. First, I'm so sorry for what happened to you that night. I visited you every single day for nearly a year... I prayed that you'd come back to us...{/i}"
    grc "{i}But when our girls were born... I had no choice but to give them my full attention.{/i}"
    grc "{i}Second, I'm sorry I never got the chance to contact you when I heard you finally came out of it all those years later. You see, I'm very sick. I don't have a lot of time left. And the truth is... I was just scared. Scared of the unknown.{/i}"
    grc "{i}Scared that you may reject the mere idea of me... or think I'm just some crazy person trying to get free child support. Some things are just better left to mystery, I think. But our girls? That's... a different story. They deserve a chance to get to know their father.{/i}"
    pause (1.3)
    grc "{i}I did some digging and found out you're doing pretty well for yourself now. I heard you're kind of a big deal in the photography industry, too!{/i}"
    grc "{i}Well... don't take this the wrong way, I know this is a lot to take in... but I need to ask you a huge favor. You see, when I got sick... our girls were still pretty young. And over the years my health has declined pretty rapidly...{/i}"
    grc "{i}Because of this... they've had to fend for themselves for a while now... caring for their sick mom while trying to maintain good grades... it has been really hard on them and I truly worry for their futures. There is so much that I couldn't give them...{/i}"
    grc "{i}So much I couldn't show them or teach them. They're good girls, [mc], and they deserve so much better than this. But I'm afraid... I'm not going to make it much longer...{/i}"
    grc "{i}So I'm asking you, [mc]. Please care for them. Please help them grow into the fine young women that I know they'll become. They may not be perfect... all of them have their quirks and flaws... but they're beautiful, loving young girls with hearts of gold.{/i}"
    grc "{i}And they need their father. The truth is... they don't have anyone else. Most of our family are gone... and the ones who aren't have never welcomed us...{/i}"
    grc "{i}So please, [mc]. Please honor my final wish and bond with our daughters. Show them the things that I couldn't. Give them a fighting chance. I didn't know you for but a few short hours... but I didn't need to. I've known from the first night we spent together...{/i}"
    grc "{i}You are a wonderful person... and I believe you'll be an amazing father. So from the bottom of my heart, thank you. And take good care of yourself too, okay?{/i}"
    grc "{i}P.S. I felt it was only right to give the girls your last name, [sur]. We may not have had the chance to get married, but you are still their father. I hope you don't mind this...{/i}"
    stop music fadeout 10.0
    grc "{i}Thank you, [mc], for the greatest gift in the world. From the bottom of my heart.{/i}"
    grc "{i}Love...{/i}"
    grc "{i}{font=gui/fonts/handlee/handlee-regular.ttf}{size=+5}Gracie <3{/size}{/font}{/i}"
    mc "..{w}.{w}.{w}"
    scene letter2 with fade
    na "You wipe the tears from your eyes. You don't remember a thing about Gracie... but somehow the realization of her loss leaves you with a deep, unexplainable feeling of emptiness."
    scene lrali3 with fade
    mc "(This is too much...)"
    mc "(So all these years...)"
    mc "(The girl I've been dreaming about, Gracie...)"
    mc "(She's real after all. Not just real... but she's the mother of my children? I have three daughters? Twins- no... triplets?!)"
    mc "(H-How can she ask such things of me...{w} how come she never reached out to ask me directly...)"
    mc "(I feel so...)"
    pause (1)
    play music "<loop 0.0>audio/summer_love.ogg" fadein 06.0
    menu:
        "Processing emotions is an integral part of the game and can have a significant impact on your Psyche."
        "Confused":
            $ lust +=1
            mc "(I'm just confused. I have no idea how to process all of this. Is any of it even real? Could I still be dreaming?)"
            show lrali2 with sdissolve
            na "You look up at [anick], who stares eagerly at you as if waiting for you to say something."
            na "And the first thing you notice is that..."
            na "She has your eyes."
            scene lrali1 with sfade
            mc "(Despite the confusion I feel... there's no way in hell I could turn these girls away. They're...)"
            mc "(They're my daughters.)"
            jump afterletter
        "Happy":

            $ pure +=1
            mc "(For some strange reason... I'm just incredibly happy. I don't really know how to process all of this... it may be just a dream...)"
            scene lrali2 with sdissolve
            na "You look up at [anick], who stares eagerly at you as if waiting for you to say something."
            na "And the first thing you notice is that..."
            na "She has your eyes."
            scene lrali1 with sfade
            mc "(Regardless of how I feel... there's no way in hell I could turn these girls away. They're...)"
            mc "(They're my daughters.)"
            jump afterletter
        "Angry":

            $ dark +=1
            mc "(I'm angry for some reason. How could I not have known about this? Is any of it even real? Could I still be dreaming? Why can't I remember?)"
            scene lrali2 with sdissolve
            na "You look up at [anick], who stares eagerly at you as if waiting for you to say something."
            na "And the first thing you notice is that..."
            na "She has your eyes."
            scene lrali1 with sfade
            mc "(Despite the anger I feel... there's no way in hell I could turn these girls away. They're...)"
            mc "(They're my daughters.)"
            jump afterletter

label letterfalse:

    grc "{i}Hi, [mc]...{/i}"
    grc "{i}You may not remember me. We didn't know each other long before your accident... but I still remember you very well. You see... you and I shared a very special moment together on the night of your accident. It wasn't expected... it wasn't planned.{/i}"
    grc "{i}Heck... we were complete strangers prior to that day...{/i}"
    grc "{i}But I've never forgotten. How could I? You were so sweet to me. You came to my rescue and swept me off my feet. And although I knew nothing about you... by the time you left I felt nothing but love for you.{/i}"
    grc "{i}I've been contemplating what to say for a very long time... but I want to keep this brief. First, I'm so sorry for what happened to you that night. I visited you every single day for nearly a year... I prayed that you'd come back to us...{/i}"
    grc "{i}But when the girls were born... I had no choice but to give them my full attention.{/i}"
    grc "{i}Second, I'm sorry I never got the chance to contact you when I heard you finally came out of it all those years later. You see, I'm very sick. I don't have a lot of time left. And the truth is... I was just scared. Scared of the unknown.{/i}"
    grc "{i}Scared that you may reject the mere idea of me... or think I'm just some crazy person trying to get free support for her children. Some things are just better left to mystery, I think. But the girls? That's... a different story. They deserve a chance at a future.{/i}"
    pause (1.3)
    grc "{i}I did some digging and found out you're doing pretty well for yourself now. I heard you're kind of a big deal in the photography industry, too!{/i}"
    grc "{i}Well... don't take this the wrong way, I know this is a lot to take in... but I need to ask you a huge favor. You see, when I got sick... the girls were still pretty young. And over the years my health has declined pretty rapidly...{/i}"
    grc "{i}Because of this... they've had to fend for themselves for a while now... caring for their sick mom while trying to maintain good grades... it has been really hard on them and I truly worry for their futures. There is so much that I couldn't give them...{/i}"
    grc "{i}So much I couldn't show them.. or teach them. They're good girls, [mc], and they deserve so much better than this. But I'm afraid... I'm not going to make it much longer...{/i}"
    grc "{i}So I'm asking you, [mc]. Please care for them. Please help them grow into the fine young women that I know they'll become. They may not be perfect... all of them have their quirks and flaws... but they're beautiful, loving young girls with hearts of gold.{/i}"
    grc "{i}And they need someone trustworthy to guide them. The truth is... I don't know anyone else. Most of our family are gone... and the ones who aren't have never welcomed us...{/i}"
    grc "{i}So please, [mc]. Please honor my final wish and bond with my girls. Show them the things that I couldn't. Give them a fighting chance. I didn't know you for but a few short hours... but I didn't need to. I've known from the first night we spent together...{/i}"
    grc "{i}You are a wonderful person... and I believe you'll be an amazing caretaker. So from the bottom of my heart, thank you. And take good care of yourself too, okay?{/i}"
    grc "{i}P.S. It may sound crazy given the circumstances... but I've never stopped thinking of you... and I want nothing more than for my girls to get the chance to know the only person I've ever grown to trust.{/i}"
    stop music fadeout 10.0
    grc "{i}Love...{/i}"
    grc "{i}{font=gui/fonts/handlee/handlee-regular.ttf}{size=+5}Gracie <3{/size}{/font}{/i}"
    mc "..{w}.{w}.{w}"
    scene letter2 with fade
    na "You wipe the tears from your eyes. You don't remember a thing about Gracie... but somehow the realization of her loss leaves you with a deep, unexplainable feeling of emptiness."
    scene lrali3 with fade
    mc "(This is too much...)"
    mc "(So all these years...)"
    mc "(The girl I've been dreaming about, Gracie...)"
    mc "(She's real after all. Not just real... but she and I had a thing together? To the point where she trusts me to care for her own daughters?)"
    mc "(H-How can she ask such things of me...{w} how can she ask me to care for three girls who aren't even mine...)"
    mc "(I feel so...)"
    pause (1)
    play music "<loop 0.0>audio/summer_love.ogg" fadein 06.0
    menu:
        "Hint: Processing emotions is an integral part of the game and can have a significant impact on your Psyche."
        "Confused":
            $ lust +=1
            mc "(I'm just confused. I have no idea how to process all of this. Is any of it even real? Could I still be dreaming?)"
            scene lrali2 with sdissolve
            na "You look up at [anick], who stares eagerly at you as if waiting for you to say something."
            na "And the first thing you notice is that..."
            na "She seems... lost. Her eyes flicker with a deep sadness."
            scene lrali1 with sfade
            mc "(Despite the confusion I feel... there's no way in hell I could turn these girls away. They're...)"
            mc "(They're all alone in this world... and they need someone to care for them.)"
            jump afterletter
        "Happy":

            $ pure +=1
            mc "(For some strange reason... I'm just incredibly happy. I don't really know how to process all of this... it may be just a dream...)"
            scene lrali2 with sdissolve
            na "You look up at [anick], who stares eagerly at you as if waiting for you to say something."
            na "And the first thing you notice is that..."
            na "She seems... lost. Her eyes flicker with a deep sadness."
            scene lrali1 with sfade
            mc "(Regardless of how I feel... there's no way in hell I could turn these girls away. They're...)"
            mc "(They're all alone in this world... and they need someone to care for them.)"
            jump afterletter
        "Angry":

            $ dark +=1
            mc "(I'm angry for some reason. How could I not have known about this? Is any of it even real? Could I still be dreaming? Why can't I remember?)"
            scene lrali2 with sdissolve
            na "You look up at [anick], who stares eagerly at you as if waiting for you to say something."
            na "And the first thing you notice is that..."
            na "She seems... lost. Her eyes flicker with a deep sadness."
            scene lrali1 with sfade
            mc "(Despite the anger I feel... there's no way in hell I could turn these girls away. They're...)"
            mc "(They're all alone in this world... and they need someone to care for them.)"
            jump afterletter

label afterletter:

    scene black with sdissolve
    na "[ali] heads to your room to find her sisters. You spend some time carrying their bags in and helping them get settled in the guest bedrooms."
    scene girlsonbed with sdissolve
    na "The girls gather in one of their rooms to chat while you collect yourself and make an important call."
    scene black with sdissolve
    $ renpy.pause (.7, hard=True)
    scene beforedin5 with sdissolve
    mc "Hey, Bern?"
    ber "{i}Yeah, what's up? I was in the middle of watching Thirteen and Pregnant.{/i}"
    mc "I'm going to need tomorrow off as well. Can you cover for me?"
    ber "{i}Of course, kid. Is everything alright? You didn't catch that damn Heineken-virus, did you?{/i}"
    mc "I'm alright. It's... a long story. I'll have to tell you about it in person."
    ber "Like hell you will! I ain't catching the Heinekens, you hear?"
    mc "Yeah, yeah. You'll be fine. Anyway, I'll see you in a couple days. Don't {i}Bern{/i} the place down."
    ber "Har har, very \"punny.\" Stay safe, bud. Drink lots of fluids and make sure you buy a lot of toilet paper. I'm serious... you're going to want like... a lot of toilet paper."
    stop music fadeout 05.0
    scene beforedin1 with sdissolve
    na "You can hardly believe what has happened. A short time has passed since the girls arrived and you're not even sure how to feel."
    menu:
        mc "(I guess I'm feeling somewhat...)"
        "Flustered":
            $ lust +=1
            na "Your head is spinning and you're filled with doubt and curiosity."
            na "Part of you wants to bombard them with hundreds of questions about Gracie... but you feel that'd be insensitive given what you now know."
        "Hopeful":

            $ pure +=1
            na "Your head is spinning... but you're optimistic of what could come of this."
            na "All you can really think about is getting to know the girls better... and learning more about Gracie. But, you realize asking questions about her so soon would be insensitive- given what you now know."
        "Irritable":

            $ dark +=1
            na "Your head is spinning and you feel a sense of dread and disappointment."
            na "You're a little annoyed that there's three strangers sitting around somewhere in your home... but more than anything you're mad at the world. You wish things could have gone differently, especially given what you now know about Gracie."

    scene beforedin2 with fade
    mc "(Losing your mom to cancer when she's still so young... that can't be easy. But [ali] and [liv] seem to be taking it pretty well, at least. [mad]... I'm not so sure.)"
    mc "(As much as I'd love to sit around feeling sorry for myself... I think the girls need me. I should... wait... what should I do?)"
    mc "(I have no fucking clue how to take care of three girls... let alone how to be a [car].)"
    mc "(Hell... I'm still figuring out how to take care of myself.)"
    mc "(Oh right... I bet they're starving. I should see if they want me to cook for them.)"
    scene beforedin4 with fade
    mc "(I'm a damn good cook, at least.)"
    scene beforedin3 with fadehold
    mc "(Yikes... empty fridge.)"
    mc "(Can't exactly cook without food. Guess I'll order a pizza.)"
    scene din3 with fadehold
    na "You go to fetch the girls, but [liv] is already waiting for you outside of the bedroom door."
    mc "(It still feels really strange when I look at her. She looks so much like her mom.)"
    scene din2 with qdissolve
    liv "Hey! There you are."
    scene din3 with qdissolve
    mc "Here I am. Is everyone okay in there?"
    scene din2 with qdissolve
    liv "Yeah, we're doing okay. [anick] is sleeping and [mad] isn't ready to come out just yet. I was actually just coming to find you..."
    scene din3 with qdissolve
    mc "Perfect timing, then! You hungry? I just ordered some pizzas. I hope you don't mind."
    scene din1 with sdissolve
    liv "Mind? I love pizza!"
    mc "Perfect then! Let's go make the table."
    scene black with dissolve
    na "You wait for your pizza to arrive and sit down at the table with [liv]."
    jump olidinner1

label olidinner1:

    scene din20 with sdissolve
    mc "(I need to have a serious talk with her... about everything. There's so much to go over... where do I even start?)"
    scene din19 with sdissolve
    mc "(Poor girl, looks like she was starving. Traveling will do that to a person.)"
    mc "(Anyway... first thing's first...)"
    scene din17 with sdissolve
    mc "So I'm sorry, [liv]. For the way I reacted to... you know... to what you told me earlier? It's not that I was upset by it or anything like that... it was just a lot to take in all at once."
    scene din18 with sdissolve
    mc "And then I suddenly just got this terrible headache. I'm really not sure what came over me..."
    scene din15 with sdissolve
    liv "There's nothing to apologize for... [mc]. I think anyone would react like that in your shoes."
    scene din16 with sdissolve
    mc "Well thank you for that..."
    scene din17 with sdissolve
    mc "How's the pizza?"
    scene din15 with sdissolve
    liv "It's really good. I love white pizza! So yeah... nice choice!"
    scene din13 with sdissolve
    mc "I'm glad you like it! I was going to cook something but uh..."
    scene din14 with dissolve
    liv "Empty fridge?"
    scene din13 with sdissolve
    mc "Heh... yeah. Are you a psychic?"
    scene din15 with sdissolve
    liv "You're a guy... so I think that's normal. Hey... a few hours ago you were just a young bachelor."
    liv "Now you're the proud [car] of three girls! Haha."
    scene din12 with dissolve
    mc "Haha... I guess you're right. It's been a crazy day so far..."
    scene din10 with dissolve
    liv "By the way... even though my name is [liv], everyone calls me..."
    $ oli_nick = renpy.input("What is her nickname? (Leave this blank to use her \"true nickname.\")")
    if oli_nick == "":
        $ oli_nick="Liv"
    liv "[onick]."
    scene din8 with dissolve
    mc "Okay, [onick]. I like that nickname."
    pause (1.3)
    $ dinnersetvar = 0
    jump dinnerset1

menu dinnerset1:
    set menuset
    mc "(I should take this opportunity to ask her some questions...)"
    "The Girls":

        $ dinnersetvar +=1
        mc "So how are you girls holding up, [onick]?"
        scene din10 with dissolve
        liv "Well... I'm okay I think. Just confused, maybe? I guess that's a good way to put it. But I'm trying to be optimistic..."
        scene din8 with dissolve
        mc "And your sisters? How are they?"
        scene din10 with dissolve
        liv "Well, [ali] is taking it pretty well but that's not exactly a shocker. She just sort of floats through life... I wish I could be as carefree as she is! She seems to really like you a lot already, too."
        liv "And as for [mad]... well, I think she's just going through a lot, you know? She's angry."
        liv "Being her sister... I know her very well. I know what she's going through and I can feel that anger too... I guess it's just a lot less intense for me."
        scene din8 with dissolve
        mc "Is she angry with me?"
        if tbed == True:
            scene din11 with sdissolve
            liv "{i}*Sigh.*{/i} I think she feels a bit of resentment is all. It wasn't easy growing up without a dad... especially after mom got sick. But the truth is... she hasn't told us why she's suddenly acting this way."
        else:
            scene din11 with sdissolve
            liv "I don't see why she would be! You've never done anything to us. I think she is just less trusting of men since she never had a father figure in her life. The truth is... she hasn't told us why she's acting this way."

        scene din10 with sdissolve
        liv "[mad], she isn't normally like this... but after what recently happened with mom..."
        liv "She's more emotional than normal. Things are hard for us right now."
        scene din8 with dissolve
        mc "I see... is there anything I could do to help?"
        scene din10 with dissolve
        liv "She'll come around; you'll see. I think she just needs space right now."
        scene din8 with dissolve
        if dinnersetvar == 3:
            jump olidinner2
        else:
            jump dinnerset1
    "Other Family":

        $ dinnersetvar +=1
        mc "Do you guys have any other family? Brothers? Uncles? Grandparents?"
        scene din10 with dissolve
        liv "No. For as long as I can remember it was just the four of us."
        liv "I did meet my grandparents, but I was too young to remember. They weren't very nice to mom. When they found out she was pregnant they kicked her out of the house."
        liv "She never forgave them for that and they grew apart. By the time I was older, they had passed away, so I never had a chance to get to know them personally."
        liv "Our whole family is really small. Mom told us that grandma was an only child. Oh... and grandpa too, I think."
        liv "I don't have any aunts or uncles either, since Mom was also an only child."
        scene din8 with dissolve
        mc "I see... I'm sorry to hear that."
        scene din10 with dissolve
        liv "It's okay! I mean, it's not like it bothers me. I guess I'm used to it being this way. It has been the four of us for as long as I can remember and we are..."
        scene din11 with dissolve
        liv "...We {i}were{/i} all very close."
        scene din7 with dissolve
        $ renpy.pause (1.6, hard=True)
        scene din8 with dissolve
        mc "(Little by little, having three girls spontaneously sent to my doorstep is starting to make more sense.)"
        if dinnersetvar == 3:
            jump olidinner2
        else:
            jump dinnerset1
    "Living Situation":

        $ dinnersetvar +=1
        mc "[liv]... did you know about the letter your mom sent with [ali]?"
        scene din10 with dissolve
        liv "I did, yes. [anick] insisted on being the one to give it to you..."
        liv "But mom never told us what she wrote. Just that when we get here, we should give it to you right away."
        liv "We were worried about how you'd react when we got here... but she said that once you read it, everything would be okay."
        scene din8 with dissolve
        mc "What would you guys have done if for some reason I couldn't let you stay here? Where would you go? You're thousands of miles from home now..."
        scene din10 with dissolve
        liv "Originally [mad] wanted to just stay in our hometown... so we could be close to our friends."
        liv "But the truth is it was mom's dying wish for us to come find you. And none of us could deny her that... not even [mad]."
        liv "Before she passed away she asked me to be the one to take care of us; my sisters and I... but she knew deep down that you would take us in. No questions asked. And that you would take better care of us than anyone else would."
        liv "She had nothing but good things to say about you, you know..."
        liv "However she also had a lot of money saved up for us. She got me a debit card and told me that no matter what happens... to make sure we had a place to stay. She told me that after this... all that matters is that we follow our dreams."
        scene din9 with dissolve
        liv "[mc], listen... if it's any trouble for you at all..."
        liv "We could go back home. My friend's mom said she would take us... I have the money for another train ticket and we could..."
        na "You cut her off."
        mc "Actually, I wanted to talk to you about that."
        scene din8 with dissolve
        mc "I know that we only just met. I mean... I didn't know you guys existed until today. As [anick] explained to you I have no memory of even meeting your mother..."
        if tbed == True:
            mc "But that doesn't change the fact that you're family."
        else:
            mc "But that doesn't change the fact that your mom asked me to look after you."

        mc "You're... my [dau], [onick]. And no matter what happens..."
        mc "My home is your home. You will always have a place here."
        mc "And there's no chance in hell that I'm letting you sleep in a hotel... so."
        scene din7 with dissolve
        liv "Thank you..."
        scene din8 with dissolve
        if dinnersetvar == 3:
            jump olidinner2
        else:
            jump dinnerset1

label olidinner2:

    mc "So, [liv]..."
    mc "I'm sorry to bring this up... I know it's going to be hard to talk about... but if you feel comfortable enough to tell me... I feel like I need to know."
    mc "What exactly...{w} happened? To Gracie?"
    play music "<loop 0.0>audio/til_death_parts_us.ogg" fadein 14.0
    scene din9 with dissolve
    liv "No... you have the right to know what happened.{w} It's okay."
    scene din11 with dissolve
    $ renpy.pause (1.2, hard=True)
    liv "Two years ago she was diagnosed with stage four cancer.{w} It's actually a rare form of uterine cancer; a malignant mixed Müllerian tumor, or \"MMMT.\""
    scene din7 with sdissolve
    pause (1)
    liv "She fought so hard..."
    mc "..."
    mc "(I can't imagine what she must be going through. What all of them are going through. Gracie... she was my age. She was... far too young to go...)"
    liv "{i}*Sniff*{/i}"
    scene din9 with sdissolve
    liv "Her treatments cost a lot of money... and it put us into a pretty bad situation. We had to move into a dingy apartment just so she could afford to pay medical bills."
    liv "But the cancer... it never regressed."
    liv "After a while she couldn't care for herself anymore..."
    liv "So my sisters and I... we cared for her. As much as we could while balancing school."
    scene din11 with dissolve
    liv "But last week she... she asked us to bring her back to the hospital... and- and..."
    liv "S-She{w}.{w}.{w}. she couldn't fight anymore."
    mc "..."
    stop music fadeout 07.0
    scene din6 with sdissolve
    na "You hug her tightly and let her sob into your shoulder."
    mc "(There's not much I can say... these poor girls just lost their mom.)"
    mc "(But no matter what happens... I'm going to be there for them.)"
    mc "I'm so sorry, [liv]. I can't even imagine what you're going through right now."
    mc "I'm here for you, okay? No matter what happens... I'll always be here for you. You girls can rely on me."
    pause (2)
    liv "{i}*Sniff*{/i} T-Thank you...{w} [mcd]."
    scene black with sdissolve
    na "The night has grown late. [liv] heads to sleep and you do the same."

label afterdinner:

    scene br9 with dissolve
    mc "(Man, what a fucking crazy day this was...)"
    mc "(So I'm the [car] of three young girls...)"
    mc "(Wait... how young are they exactly?)"
    if tbed == True:
        mc "(According to Gracie's letter I'm pretty sure they were conceived on the same night as my accident.)"
        jump agelabel
    else:
        jump afterdinner2

label agelabel:

    mc "(That means they're...)"
    $ age = int(renpy.input("How old are the girls? (Numeric characters only. Leave this blank for their \"true age.\")", allow="0123456789", length=2).strip() or 18)
    if 12 < age < 22:
        jump afterdinner2
    else:
        jump ageerror

label ageerror:

    "ERROR: Please enter a valid number. A {b}minimum{/b} of thirteen and a {b}maximum{/b} of twenty-one years have passed since the accident. The number therefore cannot be lower than thirteen or greater than twenty-one."
    $ age = int(renpy.input("How old are the girls? (Numeric characters only. Leave this blank for their \"true age.\")", allow="0123456789", length=2).strip() or 18)
    if 12 < age < 22:
        jump afterdinner2
    else:
        jump ageerror

label afterdinner2:

    if tbed == True:
        mc "([age]-years-old. Interesting...)"
    else:
        mc "(Ah that's right... [onick] mentioned that they were eighteen-years-old when I was helping them unpack their stuff earlier.)"

    mc "(Three [age]-year-old girls who look remarkably like someone I've been screwing in my dreams...)"
    mc "(Three... absolutely beautiful [age]-year-old girls, no less...)"
    scene br8 with dissolve
    mc "(Man... Bernie is going to lose his damn mind when he hears about this one.)"
    mc "(I can't actually believe this is happening. Is it real? I'm not having one of those crazy dreams again, am I?)"
    mc "{i}*Yawn*{/i}"
    scene br7 with dissolve
    mc "(This day just... flew by. I can't even believe it's so late already. In all of the excitement I didn't even realize how...)"
    scene br12 with dissolve
    mc "{i}*Yawn*{/i}"
    mc "(How tired I am...)"
    scene br11 with dissolve
    $ renpy.pause (.3, hard=True)
    scene black with dissolve
    na "You drift into a deep, restful sleep..."
    $ renpy.pause (1, hard=True)
    scene black with dissolve
    $ renpy.pause (2.5, hard=True)
    scene br10 with dissolve
    mc "{i}*Grumble*{/i}"
    scene br12 with dissolve
    mc "(Hmmm?{w} Wow. That was...{w} the strangest fucking dream ever...)"
    mc "(Heh... \"[dau]s.\" As if that's something that would actually happen in real life.)"
    mc "(What is this... a porn game?)"
    scene sw30 with fadehold
    mc "Need... piss... {i}*Mumbling*{/i}"
    scene sw29 with sfade
    mc "(Damn... my bladder was going to explode.)"
    scene black with dissolve
    play sound "audio/sounds/toilet-flush.ogg" fadein 01.0
    pause (1.6)
    scene sw28 with dissolve
    mc "(Straight back to sleep I go...)"
    scene sw27 with dissolve
    $ renpy.pause (.8, hard=True)
    play sound "audio/sounds/scare.ogg"
    scene sw1 with vpunch
    mc "{size=+10}Ahhh!{/size}"
    mc "No fucking way...{w} it was... real?"
    scene sw26 with sdissolve
    mc "I totally thought I was dreaming... I'm so sorry if I scared you, [ali]."
    mc "(She's just... standing there? Why isn't she saying anything?)"
    mc "H-Hello?"
    scene sw25 with qdissolve
    mc "(Is she...{w} {i}sleepwalking?{/i})"
    mc "(Ohh no, no, no... t-thats creepy as fuck.{w} This is Ju-On: The Grudge levels of creepy...)"
    mc "(W-Wait a minute...)"
    scene sw23 with dissolve
    mc "(.{w}.{w}.Her tits are out.)"
    scene sw22 with dissolve
    mc "(And her panties are practically falling off...)"
    scene sw23 with dissolve
    mc "(This is the type of shit that innocent men get jailed over...)"
    mc "(Shit!{w} Fuck!{w} I'm getting an erection. Don't you dare grow right now, {i}penis!{/i})"
    mc "({i}Halt!{/i})"
    scene sw25 with dissolve
    mc "(Fuck... that doesn't work. I better wake her up before it's too late.)"
    scene sw21 with sdissolve
    mc "Hello? [ali]?"
    play sound "audio/sounds/scare.ogg"
    scene sw20 with vpunch
    ali "{size=+15}Eahhh!{/size}"
    scene sw19 with dissolve
    pause (.2)
    scene sw19 with vpunch
    mc "{size=+5}Ahh fuck!!!{/size}"
    scene sw18 with dissolve
    ali "Oh my God... [mcd]?! What happ.{w}.{w}"
    scene sw00 with dissolve
    ali "Eek! What the hell is that?"
    mc "What the hell is what--"
    scene sw16 with dissolve
    mc "what...?"
    mc "Oh... right. Heh.{w} Dick's out."
    scene sw15 with dissolve
    mc "(God dammit. Stand up and get ahold of yourself.)"
    scene black with dissolve
    na "You put your cock away and climb to your feet."
    scene sw14 with dissolve
    mc "I'm {i}so{/i} sorry [ali]... I think you were sleepwalking... so I tried to wake you and you were standing there so I..."
    pause (.7)
    mc "S-Shit.{w} I don't know what to say... d-do you think I'm a creep now?"
    $ renpy.pause (1, hard=True)
    scene sw12 with dissolve
    ali "I forgive you, [mcd]. Don't worry."
    scene sw13 with dissolve
    mc "(Wait, really?)"
    scene sw11 with dissolve
    mc "(She's... hugging me?{w} I can feel her...{w} little nipples pressing against my chest...)"
    mc "(Does she not realize that she's naked?{w} ...Yup, that did it. I'm rock solid again.)"
    scene sw7 with dissolve
    ali "It was my fault. I sleepwalk sometimes. I should have told you."
    scene sw8 with dissolve
    mc "U-Um... I'm sorry you had to see my... thing. I hope you're not freaked out... it's just a natural reaction..."
    scene sw9 with qdissolve
    ali "Your thing? What's that?"
    scene sw8 with qdissolve
    mc "(Is she serious...?)"
    mc "You know, my...{w} my {i}penis.{/i}"
    scene sw7 with qdissolve
    ali "Ohhh."
    scene sw8 with qdissolve
    pause (.3)
    scene sw9 with qdissolve
    ali "That's okay [mcd], I like it.{w} You have a handsome penis. You don't have to be ashamed of it."
    scene sw0 with sdissolve
    mc "{i}*Coughing*{/i}{w} I-It's... did you say that my penis is...{w} what?"
    pause (.6)
    scene sw6 with sdissolve
    ali "Hehe, you're silly. Goodnight, [mcd]!"
    scene sw5 with sdissolve
    mc "(This girl...)"
    mc "(Is going to give me a heart attack.)"
    scene sw4 with fadehold
    mc "(I'm really not sure if she's messing with me... or if there's something not quite right upstairs... but that had to be one of the strangest interactions I've ever had. Did she say my penis was...)"
    mc "{i}(...Handsome?){/i}"
    scene sw27 with qdissolve
    mc "(*{i}Sigh{/i}* Time to sleep some more.)"
    scene black with sdissolve
    pause (1.5)
    scene sw3 with dissolve
    "..."
    scene sw2 with sdissolve
    pause (1.2)
    mad "(Pervert...)"
    scene black with sdissolve
    pause (2)
    jump daytwo

label daytwo:

    play sound "<loop 0.0>audio/sounds/alarm.ogg"
    scene br4 with dissolve
    pause
    mc "{i}Mumble...{/i}"
    scene br3 with dissolve
    $ renpy.pause (.5, hard=True)
    stop sound
    scene br4 with dissolve
    mc "..."
    mc "(So all of that {i}was{/i} real.)"
    mc "(Man... my life just got turned on its head.)"
    mc "(But I'm not complaining. They seem like truly sweet girls. Better just embrace it and get used to this. Though I'm nervous as all hell.)"
    scene br0 with dissolve
    mc "(Will they even like me? And can I even help them like Gracie said I would?)"
    mc "(I'm not exactly the most mature person in the world. I mean I did lose ten years of my life to a \"nap.\")"
    mc "(It's still early, I wonder if the girls are awake yet? They've gotta be tired from all that traveling.)"
    scene br5 with dissolve
    mc "(Well... let's go find out and start this \"new life.\" No time to waste.)"
    scene black with dissolve
    pause (1.5)
    scene mtwoa12 with dissolve
    na "You expect to see your once empty home bustling with new faces. Instead you're met with silence."
    mc "(Hm... maybe they're still sleeping. I should go check on them.)"
    scene black with dissolve
    pause (1)
    scene mtwoa11 with dissolve
    mc "(I think [liv] was staying in this room, so I'll check on her first.)"
    scene mtwoa10 with dissolve
    menu:
        mc "(I'd better knock.)"
        "Knock":
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            na "You gently knock but there's no answer."

    $ peeked1 = 0
    mc "(Hmm. I guess she's still sleeping?)"
    menu:
        mc "(I could always sneak a quick peek inside and find out...)"
        "Peek Inside":
            $ peeked1 +=1
            scene mtwoa8 with dissolve
            mc "(Only one way to find out, though.)"
            scene black with dissolve
            na "You quietly open the door.."
            scene mtwob3 with dissolve
            mc "..."
            mc "(Oh dear God...)"
            mc "(Her body is just like her mom's...)"
            mc "(Petite, toned...{w} fuckable.)"
            scene mtwob2 with dissolve
            pause
            mc "([liv]... where have you been all my life?)"
            mc "(...{w} I should get out of here before Chris Hansen shows up.)"
        "Don't Peek":

            mc "(Nah, best not disturb her.)"
            mc "(She hasn't been here twenty-four hours... can't go creeping on her already.)"

    scene mtwoa5 with fadehold
    mc "(I'll try [anick]'s room next.)"
    mc "(Sweet [ali]. She's really nice and acts like we've known each other our whole lives. It's the strangest thing to be honest.)"
    if tbed == True:
        scene mtwoa3 with dissolve
        mc "(And she already seems keen on calling me her \"Daddy.\")"
        mc "(Am I even okay with that?)"
        mc "(I mean.. I {i}am{/i} her daddy after all. Might as well get used to it. I wonder... will the other girls call me that as well? [liv] said it last night after dinner if I remember correctly. [mad], on the other hand, just seemed disturbed by the thought of it.)"
        scene mtwoa10 with dissolve
        mc "(She's going to be a tough shell to crack, I think.)"
    else:
        scene mtwoa3 with dissolve
        mc "(And she's already grown pretty affectionate. All the hugging, and touching, and kissing.)"
        mc "(Does it mean anything?)"
        scene mtwoa10 with dissolve
        mc "(I mean... I'm her caretaker after all. But hell... guess I'm just not the type to complain about a cute young girl wanting hugs and kisses. She can have them all day.)"

    menu:
        mc "(Alright, time to see if [anick]'s awake.)"
        "Knock":
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            na "You gently knock on the door, but there's no answer."

    menu:
        mc "(Hm... nothing. These girls sleep like babies.)"
        "Peek Inside":
            $ peeked1 +=1
            scene mtwoa7 with dissolve
            mc "(Yolo.)"
            scene black with dissolve
            $ renpy.pause (1, hard=True)
            scene mtwob4 with dissolve
            pause
            mc "(Jesus{w} H.{w} Christ.)"
            mc "(I'm getting another erection thinking about [ali].{w} What is it... my fourth? Fifth already? This is... problematic.)"
            mc "(But hey... a little \"body positivity\" never hurt anybody... right?)"
            scene mtwob1 with dissolve
            mc "(What a smackable butt...)"
            mc "(This attraction I'm feeling... is going to complicate things...)"
            scene black with dissolve
            pause (1)
            scene mtwoa6 with dissolve
            mc "(Unless...)"
        "Don't Peek":

            mc "(Nah, I better not intrude on her privacy.)"
            mc "(I mean, what if she's sleeping naked? The last thing I need is to be sexually attracted to my own [dau]s.)"
            scene black with dissolve
            pause (1)
            scene mtwoa6 with dissolve
            mc "(Unless...)"

    if peeked1 == 2:
        $ lust +=1
    else:
        $ pure +=1

    scene mtwoa2 with dissolve
    mc "(What if they'd be open to some kind of intimate or sexual relationship with me?)"
    mc "(...it's genius. Way-to-go, galaxy brain.)"
    mc "(But on a serious note... it's hard to deny that I find them attractive... how could I not? They all bear a striking resemblance to their mother, whom, I've been ass-fucking in my dreams for several years now.)"
    scene mtwoa4 with dissolve
    mc "(But they're only [age]...)"
    mc "(I'm fucking nuts for even thinking such things. They haven't been in my house for twenty-four hours and I'm already thinking of them as sexual beings. But I'm a realist, so...)"
    menu:
        mc "(In a hypothetical scenario where I become more than just a [car], what is it that {i}I{/i} want?)"
        "A Loving Relationship":
            $ pure +=1
            mc "(I mean I should just wait and see what happens... but in the event that one of us ends up more intimately involved... I think I'd be open to a relationship of some kind.)"
        "I Will Seduce Them":

            $ lust +=1
            if tbed == True:
                mc "(Who am I kidding... three sexy [age]-year-old girls living in my house. I'd be crazy not to take advantage of that. If all goes well, maybe I'll be like those dudes in adult games who build their own incestuous harems!)"
            else:
                mc "(Who am I kidding... three sexy girls living in my house. I'd be crazy not to take advantage of that. If all goes well, maybe I'll be like those dudes in adult games who build their own harems!)"
        "Obedience":

            $ dark +=1
            mc "(Something deep down tells me they are the types who need a firm hand. Someone to teach them discipline, respect, and how to best serve those of us who are strong.)"

    scene mtwoa9 with fade
    menu:
        mc "(And finally... here we are at [mad]'s room.)"
        "Knock":
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            mc "(Nope. No answer. She must still be sleeping like the others. You'd think someone forced them to do manual labor or something. Bunch of rocks.)"
            scene mtwoa6 with dissolve
            mc "(You know what? Curiosity is getting the better of me... I know nothing about this girl yet and I've barely even seen her. I'm just going to take a quick peek inside.)"

    scene black with dissolve
    pause (1)
    scene mtwob0 with dissolve
    mc "(Hm... she's not in here. That's strange.)"
    scene black with dissolve
    na "You close the door and begin to search for your [dau]."
    jump madsunbath

label madsunbath:

    play music "audio/way_out_west.ogg" fadein 08.0
    scene mtwoa1 with dissolve
    mc "[mad]? Are you awake?"
    scene mtwoa0 with fade
    mc "(Oh, there she is. I guess she decided to do some sunbathing.)"
    scene mbat10 with fade
    mc "(Now's my chance to have a heart-to-heart with her I think.)"
    scene mbat9 with fade
    mc "(Such a pretty girl... I can tell she takes good care of herself... and her body.)"
    menu:
        mc "(I don't think she noticed me yet... should I...)"
        "Check Her Out":
            $ checkedout = True
            $ lust +=1
            scene mbat8 with sdissolve
            mc "(God damn. She may only be [age], but she's got some nice big tits.)"
            if tbed == True:
                mc "{i}(\"You used to live in my balls, man!)\"{/i}"
                mc "(...I'm immature, aren't I?)"
                scene mbat7 with sdissolve
                mc "(And what do we have here?)"
                mc "(...that's it. I'm done for. These girls are killing me.)"
                mc "(Heh. You could say this was the straw that broke the {i}camel's{/i} back.)"
                mc "(...{w}kill yourself, me.)"
            else:
                mc "(Well... she didn't get it from her mother based on what I know.)"
                scene mbat7 with sdissolve
                mc "(And what do we have here?)"
                mc "(...that's it. I'm done for. These girls are killing me.)"
                mc "(Heh. You could say this is the straw that broke the {i}camel's{/i} back.)"
                mc "(...{w}kill yourself, me.)"
        "Don't Do It":

            $ checkedout = False
            $ pure +=1
            mc "(Nah... that would be wrong of me. I need to learn to resist temptation around them.)"

    scene mbat6 with sdissolve
    na "You speak softly as to not startle her."
    mc "Good morning, [mad]."
    mad "Hmph..."
    scene mbat5 with qdissolve
    mad "What do {i}you{/i} want?"
    scene mbat6 with qdissolve
    menu:
        mc "(How should I respond to that...?)"
        "Be Nice":
            $ pure +=1
            $ mad_pure +=1
            mc "Sorry for disturbing you. I just want to talk. Do you think you'd be alright with that?"
            mad "..."
            scene mbat5 with qdissolve
            mad "Okay..."
            scene mbat6 with qdissolve
        "Be Blunt":

            $ lust +=1
            $ mad_lust +=1
            mc "Obviously I want to talk to you or I wouldn't be out here in the first place."
            scene mbat5 with qdissolve
            mad "Fine..."
            scene mbat6 with qdissolve
        "Tell Her Off":

            $ dark +=1
            $ mad_dark +=1
            mc "The fuck do you mean, \"what do I want?\" You're in {i}my{/i} house, sitting by {i}my{/i} pool... you could at least have the decency to entertain a quick discussion with me."
            scene mbat5 with qdissolve
            mad "Whatever... you don't have to be such a butthead about it."
            scene mbat6 with qdissolve
            mc "Hate to break it to you, [mad], but you're the butthead. Not me."
            mc "(Wait... {i}butthead?{/i})"
            scene mbat5 with qdissolve
            mad "Fine... just get it over with then."
            scene mbat6 with qdissolve

    mc "Thank you..."
    $ sunbsetvar = 0
    jump sunbathset

menu sunbathset:
    set menuset
    mc "(I better get straight to the point here. What should we talk about?)"
    "Gracie":

        $ sunbsetvar +=1
        mc "[mad]... I'm really sorry to hear what happened to your mom."
        mc "I... can only imagine what you're going through right now. All three of you. Sure, I lost my parents as well... but it was different. I was in a coma and well..."
        mc "When I woke up... I was in a great deal of pain and had so many problems to address. I guess my point is... I never had a chance to be sad about it."
        mad "..."
        scene mbat5 with qdissolve
        mad "I'm sorry about your parents, too."
        scene mbat6 with qdissolve
        mc "Th-Thanks [mad]. That means a lot."
        if sunbsetvar == 3:
            jump breakfastd2
        else:
            jump sunbathset
    "Her Temperament":

        $ sunbsetvar +=1
        mc "Err... so I should probably address the elephant in the room... I think it's pretty obvious that you're not very fond of me right now..."
        mc "...And I get it I think."
        scene mbat5 with qdissolve
        mad "...you do?"
        scene mbat6 with qdissolve
        if tbed == True:
            mc "Yeah, I think so. You're mad because I was never there for you, right? It must have been hard growing up without a father..."
        else:
            mc "Yeah, I think so. You're mad because I'm the reason you were sort of... coerced into moving away from home? It must've been hard leaving behind all of your friends..."
        mad "..."
        scene mbat4 with qdissolve
        mad "You think {i}that's{/i} what this is?"
        mad "...do you really think I'd be that selfish?"
        mad "Mom...{w} s-she..."
        scene mbat5 with qdissolve
        mad "Just forget it."
        scene mbat6 with dissolve
        mc "...(Maybe I should try a more friendly approach. What'd [liv] call her earlier, again?)"
        $ mad_nick = renpy.input("What is her nickname? (Leave this blank to use her \"true nickname.\")")
        if mad_nick == "":
            $ mad_nick="Maddie"
        mc "[mnick], [mnick], [mnick]. Listen... I'm..."
        scene mbat5 with qdissolve
        mad "Please! Just drop it."
        scene mbat6 with qdissolve
        mc "..."
        mc "Okay... I'm sorry."
        scene mbat5 with qdissolve
        mad "And it's [mad]. Not [mnick]."
        scene mbat6 with qdissolve
        mc "...Right. Okay then. (Ouch)."
        mad "(Idiot...)"
        mc "(Shit. Guess I was off base on that one. But if that's not why she's mad at me... then what could it possibly be about?)"
        mc "(There's more to the way she's feeling right now than I realize, I think. I know she's being pretty rude right now but she's only [age] and she's going through some heavy shit. I should try not to judge too harshly.)"
        mc "(Getting through to her is going to be more difficult than I thought...)"
        if sunbsetvar == 3:
            jump breakfastd2
        else:
            jump sunbathset
    "Sisters":

        $ sunbsetvar +=1
        mc "So how's your relationship with your sisters? Do you guys get along pretty well?"
        scene mbat5 with qdissolve
        mad "Of course. I love them with all of my heart."
        mad "We're triplets, you know? We think alike, dress alike, we like mostly the same foods..."
        mad "I'd do anything to protect them."
        scene mbat4 with qdissolve
        mad "And you'd better not hurt them! Or I'll... I'd..."
        scene mbat3 with qdissolve
        mad "I'll... {i}break your penis.{/i}"
        scene mbat4 with qdissolve
        pause (.3)
        scene mbat6 with qdissolve
        mc "(What the hell? Is she serious?)"
        scene mbat5 with qdissolve
        mad "Oh... and don't think I didn't see what happened last night."
        scene mbat6 with qdissolve
        mc "Huh? What are you talking about?"
        scene mbat5 with qdissolve
        mad "I saw what you were doing with my sister. And your... you know."
        scene mbat6 with qdissolve
        mc "My what?"
        scene mbat5 with qdissolve
        mad "Your... are you really going to make me say it?"
        scene mbat4 with qdissolve
        mad "Your penis! You had a b-boner!"
        scene mbat6 with qdissolve
        mc "[mad]... I can't control that. It's perfectly normal for a man to..."
        scene mbat5 with qdissolve
        mad "Please... I do {i}not{/i} want to have a discussion about your penis right now."
        if checkedout == True:
            scene mbat1 with qdissolve
            mad "Oh, and don't think I didn't notice you checking me out when you came out here."
            scene mbat2 with qdissolve
            mc "(.{w}.{w}.How the hell did she see me?)"
            mc "...Right. Sorry about that."
            mad "..."
            mc "(This girl is killing me...)"
            scene mbat1 with qdissolve
            mad "Pervert."
            scene mbat2 with qdissolve
            mc "(Oof...)"
            pause (1)
        else:
            mad "Oh, and don't let me catch you peeking on us!"
        if sunbsetvar == 3:
            jump breakfastd2
        else:
            jump sunbathset

label breakfastd2:

    scene mbat6 with qdissolve
    mc "Alright, well um..."
    mc "It was good talking to you. I'm going to go order some breakfast for you girls, and then later I will do some shopping and stock up the fridge."
    mc "Do you want anything to eat in particular?"
    scene mbat5 with qdissolve
    mad "You can just get me whatever. I'm not picky."
    scene mbat6 with qdissolve
    mc "Okay... sounds good then.{w} See you later, [mad]."
    scene mbat5 with qdissolve
    mad "S-See you.."
    stop music fadeout 09.0
    scene mbat9 with sfade
    mad "..."
    mad "(...perv.)"
    scene black with dissolve
    pause (2)
    scene phorder with dissolve
    mc "(Okay... now to order these girls the best damn breakfast they've ever seen. I feel bad for not having any real food in the house, so I'll use that GooberEats app."
    mc "Annd... done. Alright."
    scene ali4 with fade
    ali "[mcd]!{w} Good morning!"
    scene ali3 with qdissolve
    mc "Good morning, [ali]!"
    mc "(Exactly the person I was hoping to see. The reality of this situation is actually starting to set in. I have so many questions... and I wasn't getting any answers out of [mad].)"
    mc "Did you sleep well?"
    scene ali4 with qdissolve
    ali "I slept like a limp sack of potatoes. Your beds are so comfortable! Good thing you have so many extra rooms, huh? Otherwise we'd have all had to climb in bed with you."
    scene ali3 with qdissolve
    mc "Heh... yes that's... I'm glad."
    mc "(Hide the pain, [mc].)"
    scene ali4 with qdissolve
    ali "Where's [mnick]?"
    scene ali3 with qdissolve
    mc "Oh... I just talked to her actually. She's outside sunbathing at the moment."
    scene ali4 with qdissolve
    ali "You did? Does that mean you guys made up?"
    scene ali3 with qdissolve
    mc "Not quite, I'm afraid."
    mc "Do you think she will come around soon?"
    pause (1.2)
    scene ali2 with qdissolve
    ali "...Come around? Why would she come around when she can just walk through the back door?"
    scene ali3 with qdissolve
    mc "That's not what I...{w} never mind. Where's [liv]?"
    scene ali4 with qdissolve
    ali "Oh, I think she's showering... but she should be done soon."
    scene ali3 with qdissolve
    mc "Speaking of that... do you girls need anything? Like um... tampons... or shampoos... or you know, girl stuff?"
    scene ali2 with qdissolve
    ali "Well... I don't know... we all kind of hoped you had WiFi..."
    scene ali3 with qdissolve
    mc "Oh. WiFi... right. That's not a problem. I'll get something setup."
    mc "Actually, [anick], I'd been meaning to tell you girls that if you need anything at all, don't hesitate to ask. And I'm actually going to go grocery shopping soon, so if you have any requests..."
    scene ali4 with qdissolve
    ali "I'd actually love to go with you... that is if you don't mind, [mcd]."
    scene ali3 with qdissolve
    mc "That would be nice, actually. I'd enjoy having the company."
    scene ali4 with qdissolve
    ali "Great! It's settled then. And um..."
    scene ali2 with qdissolve
    ali "So there's some stuff I've been meaning to ask you..."
    scene ali3 with qdissolve
    mc "Well you're always welcome to talk to me, sweetie. What's on your mind?"
    scene ali4 with qdissolve
    ali "Okay! Well first of all what do you do for a living, [mcd]? It's just that this place is so much nicer than mom's. I don't think I've ever even been inside a house this nice before..."
    scene ali3 with qdissolve
    mc "(It makes sense that she's curious about this. Hell, there's a ton of stuff the girls don't know about me. Nor I them.)"
    mc "Well... I'm a photographer and I own a business where I recruit other photographers and find gigs for them..."
    scene ali2 with qdissolve
    ali "Oh my God... really?! That makes me so happy!"
    scene ali3 with qdissolve
    mc "Huh? What do you mean?"
    scene ali4 with qdissolve
    ali "Well... it is my dream to become a model. And if you're a photographer... that means we could maybe end up working together... right?!"
    scene ali3 with qdissolve
    mc "Well that would depend on what modeling agency you work for, sweetie."
    mc "Actually now that I think about it... that is perfect. You see, I'm not just any photographer. Not to toot my own horn or anything but... I'm kind of a big deal."
    scene ali2 with qdissolve
    ali "You are?"
    scene ali3 with qdissolve
    mc "Yes. I book all sorts of high-profile gigs... like celebrity weddings. My shots have been featured on the cover of Ramour magazine several times. And yes, I do modeling shoots too. In fact, I have a gig with Tiffany Mae next week. Have you heard of her?"
    scene ali2 with qdissolve
    ali "N-No way! Are you serious?! I am like... totally in love with her! Are you messing with me or something? That is like... a super-big deal!"
    scene ali3 with qdissolve
    mc "I'm dead serious."
    pause
    na "You're interrupted when [liv] shouts from across the house..."
    liv "{size=+5}{i}Bathroom's free!{/i}{/size}"
    mc "(Speaking of... I actually need a shower myself.)"
    mc "Listen... I'm going to go take a shower quickly... but if you want I should be able to get you booked for a modeling shoot or two. It will take me a few days but I'm sure I could pull a few strings..."
    mc "(And I may even be able to bring her with me to that shoot next week and introduce her to miss Mae. But that part's a surprise.)"
    scene ali4 with qdissolve
    ali "You've just made my entire week!{w} T-Thank you [mcd]."
    scene ali3 with qdissolve
    mc "It's no problem... but I do recommend curbing your expectations a bit. The best I'll be able to do is maybe get you in on a shoot or two. Whether or not you are successful will be totally up to you."
    scene ali4 with qdissolve
    ali "I-I understand. I'll do my best!"
    scene ali3 with qdissolve
    mc "Great. Now... you hungry?"
    scene ali4 with qdissolve
    ali "I'm starving!"
    scene ali3 with qdissolve
    mc "That's perfect then. I ordered you girls some breakfast, which should be here any minute. Would you mind actually getting the door when he gets here? It's already paid for and you guys can help yourselves."
    scene ali2 with qdissolve
    ali "No problem! Um... did you get waffles by any chance?"
    scene ali3 with qdissolve
    mc "Pumpkin waffles, blueberry pancakes, fruit salad, eggs, bacon, grits, coffee, I ordered you girls a feast so hopefully that will tide you over until we go shopping."
    scene ali4 with qdissolve
    ali "You are like... the best person ever!"
    scene ali1 with qdissolve
    ali "Mwuah."
    mc "(She sure is affectionate...)"
    pause
    scene black with sdissolve
    pause (2)
    $ renpy.sound.play("audio/sounds/shower.ogg", loop=True)
    scene shower2 with dissolve
    na "You hop in the shower and attempt to collect yourself."
    mc "(Man... I'm kind of panicking right now.)"
    mc "(On the one hand, I'm enjoying being around the girls so far. I mean, the company is nice...)"
    mc "(But on the other... I really have no idea what I'm doing...)"
    mc "(Or how to be a \"[car]\")"
    scene shower1 with dissolve
    mc "(And I may need to get a handle on these lewd feelings I'm having. But [ali] isn't exactly making it easy to avoid said feelings... walking around with her tits flopping about.{w} All the hugging and kissing...)"
    mc "(Not that I'm complaining...)"
    mc "(Rather than sitting around and repeatedly asking myself if it's \"wrong,\" I should take a little time to work out how I feel and come up with a plan.)"
    mc "(A plan... yeah. That sounds good.)"
    mc "(Realistically this should be the least of my worries right now. The most important thing is that I do right by the girls. That I make up for all those years we missed together. Growing up without a [car] is never an easy thing... and I feel terrible for them.)"
    stop sound fadeout 03.0
    scene black with sdissolve
    pause (1.2)
    scene mtwoa8 with sdissolve
    mc "(Well... here's to a new life; a new beginning.)"
    play sound "audio/sounds/breaking.ogg"
    $ renpy.pause (.4, hard=True)
    scene mtwoa8 with vpunch
    mc "(What the hell? What's all the commotion?)"
    play music "<loop 0.0>audio/lazy_boy_blues.ogg" fadein 05.0
    scene arg20 with sfade
    mc "(Uh oh... looks like an argument has broken out...)"
    scene arg19 with fade
    liv "Grow up, [mad]! You act like you're the only one going through something right now!"
    scene arg18 with fade
    mad "What do you mean \"grow up?!\" We're both [age]!"
    scene arg19 with fade
    liv "You heard me. What is even your problem? The world doesn't revolve around you, [mad]."
    scene arg20 with sdissolve
    mc "(This isn't good. They both sound really upset.)"
    mc "(Is this my fault? Am I doing something wrong?)"
    scene arg18 with fade
    mad "Why are we here, [liv]?! Why couldn't we just stay home?"
    mad "We had friends there! They were like family! And now we're across the country in some... some strange guy's home!"
    scene arg17 with sdissolve
    ali "[mcd] is a nice person! Why don't you just give him a chance?"
    scene arg16 with dissolve
    mad "Oh, don't you start, [ali]! Ever since we got here it's [mcd] this, [mcd] that. If you wanted to see your [mcd] so much... you could've just visited. We didn't have to move here and flip our whole lives upside down!"
    scene arg17 with fade
    ali "You're mean! I'm going to my room."
    scene arg15 with dissolve
    ali "{i}Hmph.{/i}"
    scene arg19 with fade
    liv "You agreed to come here, [mnick]! Just like we did! And you know that's what mom wanted! So why are you being so mean to everyone?"
    scene arg14 with sdissolve
    mad "{i}*Sigh*{/i}"
    mad "(S-She's right. Maybe I'm... overreacting.)"
    scene arg13 with fade
    mad "[liv]... I'm..."
    scene arg19 with fade
    liv "Oh, can it! You're just a spoiled princess. All you ever think about is yourself! If you want to go home so bad, then just leave! We don't need you here. We'll be better without you!"
    scene arg19 with vpunch
    liv "{size=+10}You stupid... idiot!{w}{/size} Just go home! You can stay at Alita's. We don't want you here anyway!"
    scene arg13 with fade
    mad "Y-You don't... want me here?"
    mc "([mad] is getting it pretty hard right now... I feel like I'm supposed to do something.)"
    scene arg14 with pinkflash
    scene arg14 with pinkflash
    scene arg14 with pinkflash
    menu:
        mc "(On the one hand... she's definitely been behaving like a brat. But on the other... she just lost her mom and had her entire life uprooted...)"
        "Defend [mad]":
            $ mad_pure +=3
            $ pure +=1
            scene arg12 with sdissolve
            mc "(Shit... I better do something...)"
            scene arg11 with sdissolve
            mc "Girls? Is everything okay?"
            mc "...{w}Can I say something?"
            scene arg10 with qdissolve
            liv "F-Fine..."
            scene arg11 with qdissolve
            mc "Listen... I understand that times are tough for you girls right now... I really do..."
            mc "And um... we all have our own way of processing emotions. Sometimes we say things we don't mean..."
            scene arg9 with qdissolve
            mc "S-So, [liv]... don't be so hard on [mad]. I'm sure you don't mean what you said just now... and I don't think she meant everything she said either."
            mc "When we're angry... or upset... we sometimes say things that we don't mean. But those things can be hurtful and have a lasting impact..."
            mc "You guys are triplets, and if I know anything about fraternal sisters it's that they're inseparable. So let's not fight, okay? If you want to take out your anger on someone... just take it out on me."
            mc "And [mad]..."
            mc "I don't fully understand what it is that you're upset about but..."
            mc "Whatever it is, I'm sure it's valid. You have the right to be upset... and I want you to know that...{w} that I'm sorry."
            scene arg7 with dissolve
            liv "H-He's right.{w} I'm sorry, [mnick]."
            mad "{i}*Mumble*{/i} I'm sorry too...{w} I'll be in my room..."
            scene arg2 with fadehold
            liv "I'm sorry about that. I'm going to head to my room as well. Come see me if you need anything."
            liv "Oh... and sorry about the vase, [mcd]."
            scene arg0 with dissolve
            na "And just like that you are once again left with an empty house."
        "Don't Intervene":
            $ mad_lust +=3
            $ lust +=1
            mc "([liv] is being pretty harsh on [mad]... but why would I interfere with that? She hasn't exactly been nice to me so...)"
            scene arg19 with fade
            liv "No! We literally don't. You're nothing but a burden. And you know what? I'm tired of looking at you, so get out of my face before I snap!"
            scene arg16 with vpunch
            mad "F-Fine then! I-I'll be in my room...{w} packing!"
            scene arg3 with fadehold
            mad "Y-You!{w} I'm..."
            pause (.7)
            mad "(I'm sorry{w} for the way I've been acting...)"
            mc "(...Is she going to say anything?)"
            scene black with dissolve
            na "She bites her tongue and storms off to her room."
            scene arg1 with sdissolve
            liv "..."
            scene arg2 with qdissolve
            liv "I'm sorry you had to overhear that... I'm not feeling so well, so I'm going to go to my room for a bit. I'll see you later, okay?"
            scene arg1 with qdissolve
            mc "Is there anything I can..."
            scene arg2 with qdissolve
            liv "N-No. It's okay."
            liv "S-Sorry about your vase by the way."
            scene arg0 with qdissolve
            na "And just like that you are once again left with an empty house."
        "Berate [mad]":
            $ mad_dark +=3
            $ dark +=2
            scene arg12 with fade
            mc "(I'll have to show this little spoiled baby who's in charge here.)"
            scene arg9 with dissolve
            mc "[mad]... are we really doing this right now?"
            mad "(I was just...)"
            mc "Nah, you know what? Your sister is right. You're actually just a little girl, aren't you? Are you embarrassed right now? Because you should be. You look thoroughly stupid."
            scene arg14 with sfade
            mc "If you're going to act like a spoiled little girl under my roof, you'll suffer serious consequences. How does that sound?"
            scene arg13 with qdissolve
            mad "S-Sorry..."
            scene arg14 with qdissolve
            mad "{i}*Sniff*{/i}"
            liv "Good. She needs to be taught to obey."
            mc "Actually, [mad], I think there will be some consequences for this little outburst later this afternoon. How's that sound?"
            liv "Good."
            mad "(.{w}.{w}No...)"
            liv "Sorry about your vase... I'll be in my room if you need me, [mcd]."
            scene arg0 with fadehold
            na "And with that, the girls head off to their rooms. Once again, you're left with an empty house."

    stop music fadeout 06.0
    scene black with sdissolve
    pause (2)
    scene mtwoa12 with dissolve
    mc "(Hm... looks like they ate their breakfast, at least. That's good. Man... that was intense.)"
    pause (1)
    play sound "audio/sounds/doorbell_1.ogg"
    pause
    mc "..."
    mc "(Huh? Who could it be this time?)"
    scene door2 with fadehold
    na "You cautiously approach the door... this time, somewhat anxiously."
    scene door1 with fadehold
    mc "(Last time I answered this I found out I had three estranged [dau]s. Wonder who it could be this time?)"
    scene black with sdissolve
    $ renpy.pause (1.5, hard=True)
    scene nat7 with sdissolve
    mc ".{w}."
    mc "Hello.{w} Can I help you?"
    uk "..."
    mc "(She's absolutely beautiful... but why does she look so anxious?)"
    scene nat6 with dissolve
    uk "H-Hello.{w} Are you... Mister [sur]? [mc] [sur]?"
    scene nat7 with dissolve
    mc "Y-Yeah... that's me... who's asking?"
    scene nat5 with dissolve
    uk "(.{w}.{w}.{w}it's him...)"
    mc "Everything alright?"
    $ renpy.pause (.6, hard=True)
    scene nat4 with dissolve
    nat "My name is Natalie Koval..."
    scene nat3 with dissolve
    $ renpy.pause (2.3, hard=True)
    scene nat2 with dissolve
    nat "A-And...{w} about [age] years ago..."
    nat "I b-believe you..."
    nat "You..."
    nat "Killed...{w} my son."
    scene nat1 with dissolve
    play music "<loop 0.0>audio/western_spaghetti.ogg" fadein 07.0
    mc "..."
    mc "(.{w}.{w}.Well fuck.)"
    scene black with vsdissolve
    $ renpy.pause (5, hard=True)
    scene cinali with vsdissolve
    $ renpy.pause (4, hard=True)
    scene black with vsdissolve
    $ renpy.pause (2, hard=True)
    scene cinliv with vsdissolve
    $ renpy.pause (4, hard=True)
    scene black with vsdissolve
    $ renpy.pause (1.5, hard=True)
    scene cinmad with vsdissolve
    $ renpy.pause (3, hard=True)
    mad "(Mom..)"
    jump end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
