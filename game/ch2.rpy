





default van_friends = False
default van_romance = False
default van_creampie = False
default liv_first = False
default harsh_rsp = False
default bblue = False
default rred = False
default tif_romance = False

label chaptertwo:

    stop music fadeout 04.0
    scene black with sdissolve
    $ renpy.pause (5, hard=True)
    play music "<loop 0.0>audio/every_step.ogg" fadein 05.0
    scene c2a21 with ssdissolve
    pause (1.5)
    liv "[mnick]?"
    scene c2a18 with dissolve
    pause (.7)
    scene c2a20 with qdissolve
    liv "[mnick]... can I please come in?"
    scene c2a19 with qdissolve
    mad "It's open."
    scene c2a17 with fadehold
    pause (1)
    scene c2a16 with sdissolve
    $ renpy.pause (.7, hard=True)
    scene c2a15 with dissolve
    liv "H-Hey..."
    pause (.3)
    scene c2a14 with dissolve
    mad "...Hey."
    scene c2a15 with qdissolve
    liv "...You watching your cat videos?"
    scene c2a14 with qdissolve
    mad "N-No.{w} Just browsing Zuccbook."
    scene c2a15 with qdissolve
    liv "I see..."
    scene c2a12 with qdissolve
    liv "[mnick], I'm..."
    pause (.3)
    scene c2a16 with dissolve
    liv "..."
    scene c2a12 with dissolve
    liv "You don't have to hate him, [mnick]. It's not his fault that mom..."
    liv "Th-That she never, you know... looked for someone."
    scene c2a16 with dissolve
    pause (.3)
    mad "(How can she be saying this to me right now? Mom felt so guilty after the accident... she wouldn't even...)"
    scene c2a12 with dissolve
    liv "It was her decision... to raise us on her own. How many times did we try to convince her to go out and meet someone? Or to move on? The truth is, she didn't want to..."
    scene c2a11 with sdissolve
    mad "Are you kidding me? Of course she didn't want it! She blamed herself for what happened to [mc]. All because he..."
    mad "Because he decided to drive drunk. He's just a stupid... a stupid...{w} criminal!"
    scene c2a13 with dissolve
    liv "Oh my God, [mad]. How many times have we been over this? It's not [mc]'s fault that she blamed herself for the accident. It's not his fault that she had to raise us alone..."
    stop music fadeout 18.0
    scene c2a8 with sdissolve
    liv "And for the last time, it's not his fault that she worked herself until she...{w} until her health..."
    scene c2a9 with dissolve
    mad "Do you need something, [liv]? I'd like to be alone."
    scene c2a10 with dissolve
    liv "{i}*Sniff*{/i}"
    scene c2a7 with sdissolve
    liv "F-Fine."
    scene c2a6b with dissolve
    liv "She would want you to forgive him... you know..."
    liv "A-And... I have a feeling that if he {i}could've{/i} been there... that he-"
    scene c2a6 with vpunch
    mad "Close the door when you leave, please."
    scene c2a5 with fade
    liv "{i}*Sigh*{/i}"
    liv "(I'm hurting too, you know. You think it's easy for me to... to be the strong one?)"
    scene c2a4 with sdissolve
    ali "Oh hey, [liv]!"
    scene c2a3 with dissolve
    ali "Ooo..."
    ali "{i}*Whispering*{/i} Are we spying on [mnick]? Can I be your partner?"
    scene c2a2 with sdissolve
    liv "..."
    scene c2a1 with sdissolve
    liv "(You're hopeless, [ali].)"

label natalietalk1:

    play music "<loop 0.0>audio/passing_time.mp3" fadein 09.0
    scene black with sdissolve
    $ renpy.pause (1.2, hard=True)
    scene chapter2 with sdissolve
    $ renpy.pause (5, hard=True)
    scene black with sdissolve
    $ renpy.pause (.7, hard=True)
    scene c2b54 with sdissolve
    mc "Miss!{w} Um... Natalie! Hold on!{w} Please wait!"
    mc "(How long have I been following her? We're entering the park now. I can't just let her storm off, can I? Why did she even come all this way just to bail the moment she learned it's me?)"
    scene c2b53 with sdissolve
    mc "Listen! Can we please just talk? I'm s-so..."
    mc "Sorry..."
    pause (.5)
    scene c2b52 with sdissolve
    mc "(F-Finally!)"
    scene c2b51 with sdissolve
    mc "{i}*Panting*{/i}"
    mc "(Damn... she's f-fine... for a woman her age...)"
    mc "(Ugh. Now's not the time for that, brain. What's wrong with you?)"
    mc "Th-Thank you for stopping. Just need a minute to catch my breath here..."
    scene c2b50 with dissolve
    nat "I thought I was finally over it, you know..."
    nat "That I was healed..."
    scene c2b49 with sdissolve
    nat "But when I heard you were alive and well... that you'd woken up..."
    nat "The pain returned. All of it. Anger. Sadness."
    scene c2b48 with dissolve
    $ renpy.pause (.5, hard=True)
    scene c2b47 with dissolve
    $ renpy.pause (.5, hard=True)
    scene c2b46 with qdissolve
    nat "But now... seeing your face I just feel...{w} empty."
    scene c2b45 with qdissolve
    nat "So what good is it, huh? What can you possibly say to make me feel better about taking my son away?"
    scene c2b44 with qdissolve
    mc "..."
    mc "(I need to... sit on that for a moment.{w} Find the right response.)"
    pause (2)
    mc "I'm really, truly sorry that I didn't make more of an effort. You know... to contact you after I woke up."
    mc "I struggled with what I would say to you for a long, long time. But after a while... those thoughts were just sort of... replaced."
    scene c2b45 with qdissolve
    nat "So that's why you never contacted me? Contacted us?{w} What could possibly be more important than my son's life? Or saying you're sorry to his family?"
    scene c2b44 with qdissolve
    mc "..."
    mc "Nothing... if I'm being honest."
    mc "It... wasn't like that. I wanted to reach out. I really did. I wanted to think of something to say, or a way to make it up to you."
    scene c2b45 with qdissolve
    nat "Then why didn't you?"
    scene c2b44 with qdissolve
    na "You take a slow, deep breath."
    mc "I'll... start from the beginning, I guess."
    mc "When I woke up in the hospital, I had no memory of what occurred. Far as I knew, I was still just a teenage kid."
    mc "My doctor... man... he had a hell of a time explaining to me that I was in a coma for ten years."
    mc "Surprisingly... I felt nothing at first. I barely knew how to process any of it."
    mc "Little did I know, that was just the start of the bad news I'd be getting that day."
    scene c2b47 with qdissolve
    mc "The night I went under it... it destroyed my parents. I was an only child, you see; they were a little older than most couples when they had me. They wanted to make sure they were fully prepared... so they could give me the best life possible."
    mc "To put their whole focus on raising me to be the best person I could be..."
    mc "I was their everything."
    mc "But after that night... after I flushed it all down the drain they..."
    mc "As far as they knew, I was gone. They'd never see me again."
    mc "It... ruined them. And I honestly think that's why... by the time that I woke up..."
    mc "They were.{w}.{w}."
    scene c2b45 with qdissolve
    nat "Am I supposed to feel sorry for you or something?"
    scene c2b46 with qdissolve
    nat "My son... he was an only child too."
    scene c2b49 with sdissolve
    nat "My... only boy."
    scene c2b48 with qdissolve
    nat "..."
    scene c2b43 with sdissolve
    nat "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhh!!!!{nw}"
    scene c2b42 with dissolve
    nat "Brudni chortovi Amerykans`ki nehidnyky!"
    scene c2b41 with sdissolve
    pause (.7)
    nat "I dreamed of this day..."
    scene c2b40 with fadehold
    $ renpy.pause (.3, hard=True)
    scene c2b39 with qdissolve
    scene c2b38 with qdissolve
    scene c2b37 with qdissolve
    $ renpy.pause (.3, hard=True)
    scene c2b36 with qdissolve
    $ renpy.pause (1.2)
    scene c2b35 with qdissolve
    scene c2b35 with vpunch
    mc "(Holy shit! A-A knife?)"
    scene c2b34 with qdissolve
    mc "(Is she... is she just going to kill me right here in broad daylight?)"
    mc "(Well... I can't say I don't deserve it...{w} I won't fight her...)"
    scene c2b33 with sdissolve
    nat "..."
    scene c2b32 with dissolve
    nat "Ugh!"
    nat "Bastard!"
    scene c2b31 with dissolve
    pause (.5)
    scene c2b30 with qdissolve
    scene c2b30 with vpunch
    nat "Get out of my sight, pig! I never want to see your face again!"
    scene c2b29 with sdissolve
    nat "You ruined my life! You ruined my marriage! You took my boy from me! Do you have any idea how much pain you've caused me?!"
    pause (1)
    mc "(...I'm the worst person in the entire world.)"
    mc "(B-But I...{w} I can't just leave it like this. I need to do something... right?)"
    menu:
        mc "(I just need to...)"
        "Hug Her":
            $ lust +=1
            mc "(I don't know if this will comfort her... b-but I have to try, right?)"
            scene c2b28 with sdissolve
            mc "Natalie... I'm so sorry for the pain I've caused you..."
            mc "I'm sorry..."
        "Touch Her Shoulder":

            $ pure +=1
            na "You speak gently and sincerely."
            scene c2b27 with sdissolve
            mc "Natalie... I'm so sorry for the pain I've caused you..."
            mc "Truly... terribly sorry..."
        "Reprimand Her":

            $ dark +=1
            mc "What do you want from me?! What exactly am I supposed to do here? First you come to my door, then you hold a knife to my throat... and now you just want me to walk away?"
            mc "I said I was sorry, okay?! It was an accident!"

    play sound "audio/sounds/smack.ogg"
    scene c2b26 with qdissolve
    scene c2b26 with vpunch
    nat "Just go!"
    scene c2b25 with sdissolve
    mc "(Fuck that hurt... she hits like an ox.)"
    scene c2b24 with dissolve
    mc "(There's nothing I can do... I just don't know what to say.)"
    scene c2b23 with dissolve
    mc "(I'm only making things worse, now. I... I'd better just go... before she beats the living shit out of me.)"
    scene c2b22 with dissolve
    pause (2)
    mc "(No...)"
    scene c2b21 with dissolve
    mc "(I can't just leave like this. I'll live with regret for the rest of my life. I have to at least try to make it right. To find the right words.)"
    scene c2b20 with dissolve
    mc "..."
    mc "Please... hear me out for just one more moment. Then I'll go."
    mc "{i}*Sigh*{/i}"
    scene c2b19 with dissolve
    mc "For a long time... you know, after I woke up..."
    mc "Everything felt so... wrong.{w} My memory was so foggy... I hardly even knew who I was anymore."
    mc "I was so lost... disconnected from reality. A shell of a person living inside some useless, broken body."
    scene c2b18 with dissolve
    mc "Do you know what it's like to look a cute girl in the eye while you shit into a pan?{w} Well, I do..."
    mc "To be honest, I thought I was in hell. That I'd live forever in pain and suffering. I wished I were dead. I cursed my own parents for not pulling the plug... because I honestly believed that I was living a fate worse than death."
    mc "Then, one day... the doc visited me along with my case worker. They wanted to have another chat, you see..."
    mc "I dreaded it... because our previous discussions only ever brought bad news."
    mc "Well..."
    scene c2b17 with dissolve
    mc "This one was no different. He told me..."
    mc "He told me what I'd done. He told me that I...{w} killed someone. A young guy. Couple years younger than me, even.{w} Hearing that... it was hard."
    mc "I broke down..."
    mc "That was the first moment since I'd woken up... that I felt {i}real{/i} pain. That I'd felt anything, really. And then suddenly I just... I stopped pitying myself."
    mc "Instead, I started resenting myself."
    scene c2b16 with dissolve
    mc "I had no memory of that night, but I kept picturing it... imagining it in my head. It haunted me. I had nightmares."
    mc "Then... when I was at my lowest...{w} instead of a nightmare I had a dream..."
    mc "And someone told me I needed to overcome what I was going through. Because if I didn't... then the only thing that came of my life was tragedy... misery... and suffering."
    mc "\"Everyone deserves a second chance,\" she said."
    mc "I pondered this for a while..."
    scene c2b18 with dissolve
    mc "I just couldn't accept the idea that {i}I'd{/i} be the one given this \"second chance...\" when I so clearly didn't deserve it."
    mc "But, at the very least if I...{w} fought to survive... if I fought to live again..."
    mc "Then, if nothing else I could repent for what I'd done. I could... make a difference in the world. Rather than leaving behind misery and tragedy I could accomplish something meaningful."
    scene c2b17 with dissolve
    mc "She was right. I had a chance to... do something positive."
    mc "...so I took it."
    mc "Because if I didn't... then it was all for naught.{w} So I {i}have{/i} to try... right?"
    scene c2b18 with dissolve
    mc "I'm so sorry for all the pain I've caused you, Natalie. I'm sorry that because of me... your son never had a chance."
    mc "The truth is... as long as I carry this guilt I don't think I'll ever truly be... happy."
    mc "But I live because I have to... because I have a responsibility to make something positive out of this life."
    mc "I owe it to the world... to my parents..."
    scene c2b16 with dissolve
    mc "...to you. To your son..."
    mc "(To my three girls...)"
    mc "To be honest I don't know if I'm doing the right thing... but I'm trying."
    mc "(I don't really have a choice, do I...?)"
    mc "If there's anything I can do... anything at all... you know where to find me."
    pause (2)
    scene c2b18 with dissolve
    mc "I hope that you can forgive me someday, Miss Natalie. But to be honest, I wouldn't blame you if you didn't."
    scene c2b13 with sdissolve
    pause (1)
    mc "(Because I haven't.)"
    pause (1)
    scene c2b23 with fade
    menu:
        "Go Home":
            pass

    scene c2b14 with fadehold
    nat "[mc], hold on."
    scene c2b11 with fade
    nat "I'm going to be in town for a while..."
    nat "D-Do you think we can..."
    scene c2b10 with dissolve
    nat "Maybe...{w} grab a coffee or something...?"
    mc "Y-Yeah... that would be... I'd be happy to."
    scene c2b9 with dissolve
    nat "Here's my card."
    mc "Th-Thank you."
    play sound "audio/sounds/smack.ogg"
    scene c2b8 with qdissolve
    scene c2b8 with vpunch
    pause (1)
    scene c2b7 with sdissolve
    nat "Tsey hladkyy rozmovlyayuchyy hadyuk!"
    mc "(Aghh what the fuck! Now both ears are ringing. What the hell was that about?!{w} Did she have to slap the other side??)"
    scene c2b6 with sdissolve
    nat "See you soon, Mister [sur]."
    scene c2b5 with sdissolve
    mc "Fuck!"
    mc "(Forget the ox. This fucking woman hits like a truck.)"
    scene black with sdissolve
    pause (2)

label homeagain:

    scene c2b4 with sdissolve
    mc "{i}*Sigh*{/i} (Home again...)"
    stop music fadeout 05.0
    scene c2b3 with dissolve
    mc "(Good. It's quiet. I'm just going to...)"
    scene c2b2 with fadehold
    mc "{i}*Yaaawn.*{/i}"
    scene c2b1 with sdissolve
    mc "(Nap...)"
    scene black with sdissolve
    pause (.7)
    mc "(Come to think of it... I hope I don't have a concussion. That woman seriously hits like a boxer.)"
    $ renpy.pause (5, hard=True)
    mad "Hellooo?!"
    scene c2c32 with sdissolve
    mc "(...what is this... this pain?)"
    play music "<loop 0.0>audio/si_senorita.ogg" fadein 07.0
    scene c2c31 with sdissolve
    mad "Earth to [mc]. I don't have all day you know."
    scene c2c30 with qdissolve
    pause (1)
    scene c2c32 with sdissolve
    mc "{size=-5}{i}*Gasping*{/i} Ff—c-can't... br-breathe... what's happen—ing?!{/size}"
    scene c2c28 with sdissolve
    mad "You can't sleep all day, lazy pants."
    scene c2c29 with qdissolve
    pause (1.3)
    scene c2c28 with qdissolve
    mad "Don't you have adult stuff to get done or something?"
    scene c2c27 with sdissolve
    mad "Besides, my sisters have a surprise for you. Will you really leave them hanging? When you've already gotten plenty of sleep?"
    scene c2c26 with sdissolve
    mc "{size=-5}Cr-Crushed... I'm... being crushed... air... lungs...{/size}"
    scene c2c25 with dissolve
    mad "WAKE UP!!!"
    scene c2c24 with vpunch
    $ renpy.pause (1, hard=True)
    scene c2c25 with dissolve
    $ renpy.pause (.7, hard=True)
    scene c2c24 with vpunch
    mc "{size=-5}I-I'm... a-aw-ake... p-please... n-need... air...{/size}"
    scene c2c25 with dissolve
    $ renpy.pause (.7, hard=True)
    scene c2c24 with vpunch
    mc "{size=-5}Help!{/size}"
    scene c2c23 with sdissolve
    grls "{i}*Giggling*{/i}"
    scene c2c22 with sdissolve
    mad "\"Go wake him up for us,\" they said. \"It will be fine,\" they said. And here you are, sleeping like a dead person."
    scene c2c21 with qdissolve
    scene c2c21 with vpunch
    mad "{size=+5}[onick], bring me the hose! I'm going to douse him!{/size}"
    scene c2c19 with dissolve
    mc "PLEASE!"
    scene c2c18 with sdissolve
    mad "Oh? Look who finally rose from the dead. It's about time, sleepy."
    scene c2c17 with qdissolve
    mc "{size=-5}Pl-Please get off...{/size}"
    mc "{size=-5}He-Heavy...{/size}"
    scene c2c18 with qdissolve
    mad "I can't hear you; you'll have to speak like a normal human. But anyway, I doubt what you're saying is interesting or important. I'm simply here at the request of [liv] and [ali], who insisted I fetch you for some \"surprise\" or something."
    scene c2c16 with fade
    mad "Now rise and shine before I get the pressure washer, okay?"
    scene c2c15 with sdissolve
    mc "{i}*Gasping*{/i} Jesus Christ!"
    scene c2c14 with dissolve
    mc "(I almost died!)"
    scene c2c13 with sdissolve
    mad "I told you I wasn't scared of him..."
    scene c2c12 with sdissolve
    mad "Hmph!"
    scene c2c11 with fadehold
    mc "(So it's... morning again? Shit! I must've slept for nearly a full day. So much for spending time with the girls... I need to leave for work soon.)"
    mc "(Man... what a horrible way to wake up. I seriously thought I was going to suffocate! How can an [age]-year-old be that heavy?! Did she get ass implants or something?)"
    mc "(It's like... the vast majority of her body weight exists in her ass... just the ass. How can an ass even be that disproportionate to the rest of your body?)"
    mc "(I'll get her back for that. That little...)"
    menu:
        "Angel":
            $ pure +=1
            mc "(The little...)"
            mc "{i}*Sigh*{/i} (My sweet angel. Yup, totally just an angel deep down... and not out to ruin my life or anything. Just uh... very temperamental right now.)"
            mc "(I must not forget she just lost her mom. I'm sure she's a sweet girl... putting aside her recent antics. I can't be too hard on her.)"
        "Devil":
            $ lust +=1
            mc "(The little devil! She'll be the damn death of me.)"
            mc "(I guess I can't be too hard on her... but man, she's a real pain in the ass.)"
            mc "(You're going down, [mnick]. I'm going to get you back somehow.)"
        "Bitch":
            $ dark +=1
            mc "(The little bitch! I'll make her regret that.)"
            mc "(She needs to know who's in charge around here. I can't keep letting her get away with these things. I think it's time I paid her a nice visit later... when the two of us can be alone.)"

    mc "(I still feel horrible after that talk with Natalie yesterday.)"
    mc "(As if the accident weren't already hard enough...)"
    mc "(...How many people did I hurt? How many lives were ruined because of my actions that night?)"
    stop music fadeout 08.0
    mc "(Well...)"
    mc "(At least she's on the path for forgiveness and wants to get a coffee together. I don't really think there'll ever be a way to make things right... but at least I can try.)"
    scene c2c10 with dissolve
    scene c2c10 with vpunch
    mad "{size=+5}[mc]!{/size}"
    mc "I'm coming, dammit!"
    if tbed == True:
        mc "(This damn teenager will be the death of me!)"
    else:
        mc "(This girl will be the death of me!)"

    mc "(I guess I better get out there before she booty-bombs me again.)"
    play music "<loop 0.0>audio/fun_in_the_sun.ogg" fadein 09.0
    scene black with sdissolve
    pause (2)
    scene c2c9 with sdissolve
    grls "Good morning!"
    scene c2c8 with qdissolve
    if tbed == True:
        mc "(Whoa. Still can't get over those great genes I have.)"
    else:
        mc "(Whoa. Still can't get used to how cute they are.)"
    mc "Morning, girls. What's this surprise [mnick] told me about? And what smells so damn good out here?!"
    scene c2c7 with dissolve
    ali "Well... you and I were going to go shopping yesterday, remember? But it looks like you fell asleep...{w} for like, one hundred hours!"
    scene c2c8 with dissolve
    mc "(Shit!)"
    mc "Oh yeah! Damn, I'm sorry [ali]. I completely forgot about that..."
    scene c2c6 with dissolve
    liv "No, it's okay. It's obvious you were very tired... and don't worry, it wasn't \"one hundred hours.\" More like eighteen."
    scene c2c7 with dissolve
    ali "You slept all day and night! You must've been famined!"
    scene c2c8 with dissolve
    mc "(...I don't think that means what she thinks it means. But nevermind that...)"
    mc "Well, I'm so sorry I missed the opportunity to spend the day with you three. But I hope you've made yourselves at home now?"
    scene c2c6 with dissolve
    liv "We did! Actually, we kind of took it upon ourselves to go shopping. You know... gr-o-cer-y shopping? If you've heard of that."
    scene c2c8 with dissolve
    mc "(Oh yeah... there's a market just a few blocks from here. They must have walked.)"
    scene c2c7 with dissolve
    ali "Oh, and we made a huge breakfast!"
    scene c2c8 with dissolve
    mc "Wow... I don't know what to say. That's extremely kind of you girls. You mean to tell me we have food now?!"
    scene c2c6 with dissolve
    liv "Yup. The refrigerator and cabinets are completely full."
    scene c2c8 with dissolve
    mc "That's amazing! Thank you, girls. Um... where did you guys get the money to go shopping?"
    scene c2c6 with dissolve
    liv "My mom gave us a debit card, remember?"
    scene c2c8 with dissolve
    mc "Oh, right. I do remember you telling me. (I'll have to pay them back for this later.)"
    scene c2cx1 with dissolve
    ali "Come on... I'm starving!"
    scene c2cx2 with dissolve
    pause
    "{b}Reminder:{/b} You can turn on the textbox in the 'Options' menu."
    scene c2c4 with fadehold
    mc "(Wow... they really outdid themselves.)"
    scene c2c3 with sdissolve
    mc "(Well... they may only be [age], but it's nice to know they can take care of themselves.)"
    scene c2c5 with sdissolve
    mc "(This was really nice of them to do. I wonder whose idea it was?)"
    scene c2c2 with sdissolve
    mc "(After what happened yesterday I don't think I would've had the motivation to even eat breakfast today... if not for them. I hardly even have an appetite now if I'm being honest.)"
    scene c2d78 with sdissolve
    mc "(Oh God, Natalie... I'm so, so sorry for what I've done...)"
    mc "(I guess I... I've been avoiding facing the music. I realize now that it was wrong for me to not reach out... to offer some sort of apology or compensation.)"
    scene c2d77 with dissolve
    mc "(How could I be so selfish?)"
    scene c2d76 with dissolve
    mc "(The worst part is... I never had to face any real ramifications for it thanks to Natalie and her husband. If I remember correctly... the prosecutor loosely suggested the charges be dropped... and they both agreed due to the poor physical state I was in.)"
    scene c2d75 with dissolve
    mc "(I wonder... did my parents play a role in that at all? Did Natalie ever get the chance to meet my mother and father? She must have... right?)"
    mc "{i}*Sigh*{/i}"
    scene c2d74 with sdissolve
    mc "(Why is this all happening now... out of the blue like this? I've barely had time to process meeting the girls, and now...)"
    scene c2d73 with sdissolve
    mc "(Why did Natalie wait until now to face me? Could her timing be any worse?)"
    scene c2d72 with sdissolve
    ali "How's everything, [mcd]?"
    mc "Huh? Oh... it's really, truly good. I shouldn't be surprised you three can cook.{w} Thank you, girls. This means a lot to me."
    ali "You're welcome!"
    scene c2d71 with sdissolve
    liv "...is everything okay, [mcd]? Is there something bothering you?"
    scene c2d70 with dissolve
    mc "No, everything's fine. I was just... thinking. And there's something I need to talk to the three of you about later. But for now, let's enjoy our morning."
    scene c2d69 with sdissolve
    mad "Oh boy, here we go. He's going to kick us to the curb already. I knew it."
    scene c2d68 with dissolve
    liv "Oh shush, [mnick]. That's obviously not what he wants to talk about."
    scene c2d67 with sdissolve
    ali "He wouldn't do that... I can tell he likes having us here. Right, [mcd]?"
    scene c2d66 with sdissolve
    mc "I love having you girls here. Even you, [mad]. Thank you for inquiring by the way, [onick]. It's nice to have someone who cares."
    scene c2d65 with dissolve
    liv "I do care. All of us do. Even [mnick], though she's terrible at showing it."
    scene c2d64 with dissolve
    mad "Hey, speak for yourself."
    scene c2d63 with sdissolve
    liv "You can talk to us about anything. We're here for you... just like you were there for us when we needed you."
    scene c2d62 with dissolve
    mc "That's... really sweet. Thank you."
    scene c2d59 with sdissolve
    ali "Now that we're all settled in... what should we do today? I'm so glad it's summer. It feels weird not having any responsibility."
    scene c2d58 with qdissolve
    liv "Hm... pool day?!"
    scene c2d57 with qdissolve
    ali "Yes! [mnick], you in?"
    scene c2d56 with sdissolve
    mad "How could I refuse you, [anick]?"
    scene c2d55 with sdissolve
    pause (2)
    mc "(Oh...)"
    mc "I'd love to join you... but I completely forgot to tell you girls I have work today."
    mc "(Shit... I really wish I could take another day off, but there's way too much that needs to be done. Especially with the shoot coming up.)"
    mc "There's just so much work waiting for me. Unfortunately it can't wait."
    scene c2d54 with sdissolve
    liv "Don't worry about it! You don't have to put your whole life on hold for us. We'll be fine here all by ourselves."
    scene c2d53 with sdissolve
    mc "Thank you, [onick]. And don't forget to wear sunscreen! I have some in the medicine cabinet if you need it."
    scene c2d52 with sdissolve
    ali "Oh, she needs it. Otherwise she turns into a strawberry."
    scene c2d51 with dissolve
    liv "Don't remind me. I'm still traumatized from that day..."
    scene c2d50 with dissolve
    mad "She looked more like a plum than a strawberry. That was soo bad..."
    scene c2d49 with sdissolve
    mc "(It's nice to see them getting along like this. It feels... lively in here. I'm used to having a quiet cup of coffee and watching television.)"
    mc "(I don't know what it is... but they've somehow lifted my spirits. I was feeling pretty down before. That said it's unfortunately time to get ready for work. I'll just go shower and...)"
    scene c2d48 with dissolve
    scene c2d48 with vpunch
    ali "LAST ONE TO THE SHOWER IS A FILTHY COW!"
    scene c2d47 with dissolve
    liv "Hey! Who are you calling a cow?!"
    stop music fadeout 08.0
    scene c2d46 with dissolve
    mc "(...and they're off. Good thing I have more than one shower.)"
    scene c2d45 with dissolve
    mc "(What the hell? Why is she giving me that evil staredown?)"
    mc "What's up? Everything alright?"
    scene c2d44 with dissolve
    pause (1)
    scene c2d43 with dissolve
    mad "You know... we used to share a shower all the time at my mom's place... having only one bathroom and all."
    scene c2d42 with sdissolve
    mad "In fact, they're probably sharing a shower right now."
    scene c2d41 with dissolve
    mad "I bet you'd love to see that... wouldn't you?"
    scene c2d40 with dissolve
    grls "{i}*Giggling*{/i}"
    mc "(Holy fuck. She's not even bluffing.)"
    mc "...Ahem. Uhm... n-no? Y-You're my [dau]s."
    mc "And uh... what about you? Why didn't you go with them?"
    scene c2d39 with dissolve
    mad "Oh me? I'm just going to use yours."
    scene c2d38 with dissolve
    mc "H-Hey, wait! I need to get ready for—"
    scene c2d37 with dissolve
    mc "..."
    scene c2d36 with sdissolve
    mc "...work."
    mc "Well... no shower for me today, I guess. I'll just have to get dressed and go."

label workday:

    play music [ "audio/summer_love.ogg", "audio/the_crows_did_it.ogg", "audio/way_out_west.ogg", "<loop 0.0>audio/arc_of_the_sun.ogg", ] fadein 07.0 fadeout 10.0
    scene black with sdissolve
    $ renpy.pause (2, hard=True)
    scene c2d35 with sdissolve
    $ renpy.pause (1.2, hard=True)
    scene c2d34 with dissolve
    $ renpy.pause (1.5, hard=True)
    scene black with sdissolve
    $ renpy.pause (1.3, hard=True)
    scene c2d33 with dissolve
    $ renpy.pause (2, hard=True)
    scene black with sdissolve
    $ renpy.pause (2, hard=True)
    scene c2d32 with sdissolve
    pause (1)
    scene c2d31 with dissolve
    brk "And... sent!"
    scene c2d30 with dissolve
    ber "Good job, sweetheart. You'll have more clients knocking down your door in no time."
    scene c2d29 with dissolve
    ber "You know.... that reminds me of the time I knocked down the door of the Moroccan Prime Minister. The bastard thought he could get away with trying to hit on my woman..."
    scene c2d28 with sdissolve
    pause (1)
    mc "You telling your crazy stories again, Bernie?"
    scene c2d27 with dissolve
    ber "They're not stories, they're true events! Look it up."
    scene c2d26 with dissolve
    ber "Oh! So you decided to show up today. Everything okay, kid?"
    scene c2d25 with dissolve
    mc "I'll be in my office if you need me, dad."
    scene c2d24 with sdissolve
    brk "Good morning, Mister [mc]!"
    scene c2d23 with dissolve
    mc "Morning, Brooke. Good to see you again."
    scene c2d22 with fadehold
    ber "Hey, don't avoid me you damn weasel. This how you repay me for holding the place down while you're gone? What happened to you yesterday, man? You sounded stressed."
    scene c2d20 with sdissolve
    mc "*Sigh* Come in, I just need to get my stuff put up."
    scene c2d21 with dissolve
    ber "So... was it a woman? Please tell me this is all because you brought some hot broad home."
    scene c2d19 with sdissolve
    mc "Nope... that's not it at all. In fact, you're probably not even going to believe what I'm about to tell you."
    mc "This may shock you. In fact, you might want to take an aspirin for this."
    scene c2d18 with dissolve
    ber "An aspirin..."
    scene c2d17 with qdissolve
    ber "Oh, shut the hell up. My heart's in perfect condition. And you know I don't believe in pharmaceuticals. Now... out with it."
    scene c2d16 with qdissolve
    mc "(Alright... what's the best way to explain this...)"
    mc "Bernie... do you remember when I told you about those strange dreams I've been having?"
    scene c2d15 with qdissolve
    ber "Are you about to tell me that you missed a day of work because of a wet dream?"
    scene c2d14 with qdissolve
    mc "Haha. Let me finish..."
    mc "So it turns out, that girl I've been telling you about... the one from my dreams..."
    mc "She's very real. Well at least I think she is... same name and everything."
    scene c2d15 with qdissolve
    ber "You're not making any sense... you know that right?"
    scene c2d16 with qdissolve
    mc "Hold on... not finished yet."
    mc "As you know... because of the accident I can't remember a damn thing. But the day I called you..."
    mc "Three girls who look a hell of a lot like that girl I've been dreaming about showed up at my door. Young girls."
    scene c2d15 with qdissolve
    ber "Are you telling me what happened... or pitching a script for a porn film?"
    scene c2d13 with qdissolve
    ber "Because if it's the latter, I'm in!"
    scene c2d12 with qdissolve
    mc "..."
    scene c2d11 with qdissolve
    ber "How young are we talking?"
    scene c2d16 with qdissolve
    mc "Well... they're exactly [age]-years-old."
    mc "It's not just a coincidence, Bernie. The girl from my dreams... not only is she real, but she's their mother..."
    mc "And I'm..."
    mc "I'm their [car]. I'm the [car] of three girls."
    scene c2d14 with qdissolve
    pause (.6)
    scene c2d11 with dissolve
    ber "You crazy son of a bitch!{w} This porno is going to sell faster than that \"Delle\" girl's bath water."
    scene c2d12 with qdissolve
    pause (.6)
    scene c2d9 with sdissolve
    pause (.4)
    ber "Wait... you're being all weird about this. You're just screwing with me, right?"
    scene c2d10 with qdissolve
    mc "I'm not messing with you. This whole time I... I had no idea..."
    ber "..."
    scene c2d8 with qdissolve
    ber "(He's surely fucking with me! This has got to be one of those elaborate pranks... you're not fooling me, kid!)"
    if tbed == True:
        scene c2d9 with qdissolve
        ber "So you're telling me you knocked up some broad and you don't even remember it?"
    else:
        ber "So you're telling me you hooked up with some broad and you don't actually remember it?"
    scene c2d8 with qdissolve
    mc "{i}*Nods*{/i}"
    scene c2d9 with qdissolve
    ber "And then... out of the blue, some girls show up at your door... to tell you that you are, in fact, their [car]?"
    scene c2d8 with qdissolve
    mc "{i}*Nods*{/i}"
    scene c2d9 with qdissolve
    ber "And you've been dreaming about screwing their mother all this time... but you had {i}no idea{/i} who she was?"
    scene c2d8 with qdissolve
    mc "Yes."
    scene c2d7 with qdissolve
    pause (.3)
    ber "Wait... how the hell are there three of ‘em?"
    scene c2d8 with qdissolve
    mc "They're triplets."
    pause (1)
    scene c2d9 with qdissolve
    ber "Congratulations, kid.{w} You've got magic semen!"
    scene c2d8 with qdissolve
    mc "...You don't take anything seriously, do you?"
    scene c2d3 with sdissolve
    $ renpy.pause (1.3, hard=True)
    scene c2d5 with qdissolve
    ber "(He can't be serious...)"
    scene c2d6 with qdissolve
    $ renpy.pause (1.2, hard=True)
    scene c2d4 with qdissolve
    ber "Sweet mother of Jesus, you're serious!"
    scene c2d3 with qdissolve
    mc "I told you I was..."
    scene c2d4 with qdissolve
    ber "So where's the mother? Why didn't she show up?"
    scene c2d3 with qdissolve
    mc ".{w}.{w}.she got sick.{w} She's gone."
    scene c2d5 with dissolve
    pause (1.3)
    scene c2d6 with qdissolve
    ber "...Wow. Give me a minute, kid."
    scene c2d5 with qdissolve
    ber "..."
    scene c2d6 with qdissolve
    ber "I'm at a loss here..."
    scene c2d2 with sdissolve
    pause (.7)
    scene c2d1 with qdissolve
    ber "I'm... I'm sorry to hear all of that."
    scene c2d2 with qdissolve
    mc "(Is Bernie actually being sincere? You don't see that often.)"
    scene c2d5 with sdissolve
    mc "Yeah. I mean I don't remember a thing about her... and in this letter she wrote me it sounds like we just had a one-night stand..."
    scene c2d3 with qdissolve
    mc "But regardless, it really struck a chord. In that moment I felt like I'd lost a member of my own family. Someone very close to me."
    mc "It's hard to explain, but when I dream of her... it's always so real... like she's a part of me. And I feel this deep connection with her."
    scene c2d6 with qdissolve
    ber "Those poor girls..."
    scene c2d5 with qdissolve
    mc "Yeah... they seem to be taking it pretty hard..."
    scene c2d6 with qdissolve
    ber "Well, I don't know what to say, kid... this is... this is a lot to process."
    scene c2d4 with qdissolve
    ber "You okay? It must be strange having three young ones dropped at your doorstep. I admit, I still haven't wrapped my head around any of this. What are you going to do?"
    scene c2d16 with sdissolve
    mc "Honestly? I don't really know. I guess I'll..."
    menu:
        "Loving [car]":
            $ pure +=1
            mc "I'll do the only thing I can... I can't just leave them to fend for themselves. To be honest I don't think they're ready for that. I'm their [car], and from what I know so far, the only person they can truly rely on."
            mc "I'm pretty optimistic about it all. I don't really know what the future holds now, but the girls are all very sweet. I want to do right by them if I can."
            scene c2d18 with qdissolve
            ber "That's it. That's the kid I know. You always were a good one."
        "Go with the flow":
            $ lust +=1
            mc "Well, I'm not completely sure. I feel like they're not quite ready to fend for themselves... so I can't just abandon them. I'm their [car], and from what I know so far, the only person they can truly rely on."
            mc "So I guess I'll just... see what happens. I'm excited, really. They're very fun to be around. There hasn't been this much action in my life in a while."
            scene c2d13 with dissolve
            ber "What kind of \"action\" are we talking?"
            scene c2d14 with dissolve
            mc "..."
            scene c2d13 with qdissolve
            ber "Ha! I'm just yanking your chain."
            scene c2d14 with qdissolve
            mc "And the girls, they're sweethearts. Cute, too."
            scene c2d18 with qdissolve
            ber "Based on the way you've described their mother... I'm sure they are!"
            scene c2d14 with qdissolve
            pause (.4)
            scene c2d18 with qdissolve
            ber "Are they single?"
            scene c2d19 with qdissolve
            mc "..."
            mc "Don't go there."
        "Nothing":
            $ dark +=1
            mc "Ugh. Do I have a choice? They're young, naïve girls. There's no way in hell they'd make it on their own... so it's not like I can just leave them to fend for themselves."
            mc "Is it fair? Not really. Life isn't fair though. But hey... might as well have some fun with it. The girls are cute, after all."
            ber "..."
            scene c2d13 with qdissolve
            ber "Are they single at least?"
            scene c2d14 with qdissolve
            mc "..."
            mc "Don't go there, grandpa. Even if they were, they're technically mine now."
            scene c2d18 with qdissolve
            ber "Jesus, kid. All jokes aside, don't turn sadistic on me now. You have to keep it together. Not just for them, but for yourself as well."
            scene c2d19 with qdissolve
            mc "...I know. Thanks, Bernie."
            mc "{i}*Sigh*{/i}"

    scene c2d17 with qdissolve
    ber "What the hell are you doing here at work anyway? You should be at home bonding with those poor girls."
    scene c2d19 with qdissolve
    mc "I wish I could, but I actually still have a lot of work to wrap up this week before the photoshoot."
    mc "Oh, speaking of that. Could you do me a favor?"
    scene c2d18 with qdissolve
    ber "I'm your guy. Just ask."
    scene c2d19 with qdissolve
    mc "One of the girls is interested in modeling. Do you think you could get in touch with Miss Mae's agent? See if she'd be okay with my [dau] tagging along for the upcoming photoshoot? She's a big fan... and I figured it'd be good for her to see things in action."
    mc "Get a feel for how the industry operates."
    scene c2d18 with qdissolve
    ber "Sure, kid. Though, from the few talks we've had so far, the agent seems real strict. Professional, but strict. It might shine poorly on us to make such a... strange request. That said... if there's a way... I'll find it!"
    scene c2d19 with qdissolve
    mc "Thanks, Bernie. I can always count on you."
    scene c2d18 with qdissolve
    ber "No worries, my friend. Let me know if I can do anything else to help. And the same applies with those girls of yours. You need advice, you come to me you hear? Parenting isn't easy."
    ber "I'd know. I have a total of twenty-seven nieces and nephews."
    scene c2d19 with qdissolve
    mc "Jesus, I forgot about that.{w} I'm surprised you're not a father yourself by now."
    scene c2d18 with qdissolve
    ber "Nah, parenting ain't for me. I mean, sure... I'd probably be alright at it. But I get enough by just being an uncle. Those rugrats are more than a few handfuls."
    scene c2d19 with qdissolve
    mc "Heh. If you say so."
    scene c2d18 with qdissolve
    ber "So when do I get to meet them?"
    scene c2d19 with qdissolve
    mc "Eh... I still feel like {i}I've{/i} barely met them. But soon, for sure. How's Brooke holding up?"
    scene c2d18 with qdissolve
    ber "Ohh, kid. We really hit the jackpot with that one. She's sharp I tell you, and knows her stuff. She's also a fast learner. A little clumsy, though. Somehow she nearly burned the place down just by using the printer."
    scene c2d19 with qdissolve
    mc "Is that your head talking... or your cock?"
    scene c2d17 with qdissolve
    ber "My head, smart ass. Besides... it's not me she's interested in."
    scene c2d16 with qdissolve
    mc "What do you mean exactly?"
    scene c2d18 with qdissolve
    ber "Well kid... it's pretty obvious that she has a thing for you. What... you haven't noticed?"
    scene c2d19 with qdissolve
    mc "(Hm... he's serious, isn't he?)"
    mc "(I guess it wouldn't be the worst thing in the world...)"
    mc "(I haven't had any romantic endeavors in well over a year now... and I'm not getting any younger. That said, I barely know her yet so I may be getting ahead of myself. And knowing Bernie, he could be playing a trick on me or something.)"
    scene c2e46 with sdissolve
    ber "Oh, speak of the devil... here she comes now."
    scene c2e45 with sdissolve
    brk "Hello! S-Sorry. Can I come in?"
    scene c2e44 with qdissolve
    mc "Of course, Brooklyn! Come on in."
    scene c2e45 with qdissolve
    brk "Th-Thank you. I hope I'm not interrupting anything."
    scene c2e43 with sdissolve
    ber "Not at all, kiddo. I was just leaving."
    scene c2e42 with dissolve
    ber "If you need me, I'll be {i}hard{/i} at work in my office."
    scene c2e41 with dissolve
    mc "(Bernie, you freak.)"
    scene c2e40 with sdissolve
    pause (2)
    show brooke at brooke_transform
    mc "(Good God. She's really rocking that outfit this afternoon...)"
    scene c2e40 with dissolve
    mc "Nice to see you again, Brooke. I hope Bernie behaved himself while I was away."
    scene c2e38 with dissolve
    brk "It's nice to see you again too! I wasn't sure if you would be here today. And yes, Bernie has been nothing but helpful. He's so funny! You should've warned me! It really helped me to settle in and feel comfortable here."
    scene c2e37 with dissolve
    brk "Oh, um..."
    brk "Speaking of being comfortable. That's um... sort of what I wanted to talk to you about if you have a minute?"
    scene c2e36 with qdissolve
    mc "Yes, I can spare a few for you. What's up?"
    scene c2e34 with qdissolve
    brk "(Calm down Brooklyn, it's not a big deal to ask him... right?)"
    scene c2e35 with qdissolve
    brk "{i}*Sigh*{/i} Okay... so yes, Bernie has been very helpful... he actually set me up with a booking already..."
    scene c2e36 with qdissolve
    mc "That's awesome! They must have really liked your work."
    scene c2e33 with qdissolve
    brk "Y-Yes! I'm really excited about it... however..."
    scene c2e31 with qdissolve
    brk "It all happened a lot faster than I was expecting. It's actually scheduled for tomorrow afternoon... and the thing is, I'm extremely nervous. Like... \"fighting off a panic attack as we speak\" nervous."
    brk "So I was wondering... it's just that you're so good at this... and I really look up to you... I guess I was hoping that um... maybe, perhaps, um..."
    scene c2e32 with qdissolve
    mc "You don't have to be shy around me. What's on your mind?"
    scene c2e30 with qdissolve
    brk "{i}*Deep Breath*{/i} Okay. Do you think we could... maybe go do something after work tonight?"
    scene c2e29 with qdissolve
    brk "J-Just to talk, obviously!"
    scene c2e28 with qdissolve
    brk "(I can't actually believe I just asked him that!)"
    scene c2e27 with qdissolve
    mc "(Whoa. Where did that come from?)"
    scene c2e29 with qdissolve
    brk "It's just... I was hoping I could discuss my upcoming job with you some... and get some tips, advice, things like that... I-I'm... worried that I'm not prepared enough."
    scene c2e27 with qdissolve
    mc "Oh! Ah... well..."
    mc "(Shit... this kind of puts me in a tough spot, as I was planning to go straight home to the girls.)"
    mc "(At the same time this seems like it's really important to her... and she's looking at me with those puppy dog eyes...)"
    mc "(Fuck it. I guess it's not that big of a deal. It probably won't take but a couple of hours or so.)"
    scene c2e28 with qdissolve
    mc "...Actually, yeah. I'd love to go out with you..."
    scene c2e25 with dissolve
    mc "Ahem... you know. To discuss business."
    scene c2e24 with qdissolve
    brk "Right! F-For business reasons..."
    scene c2e25 with qdissolve
    brk "(Was he always this handsome? And tall?)"
    mc "(I don't think she realizes she's biting her lip...)"
    scene c2e23 with dissolve
    mc "Yeah, that sounds good. How about we go straight after work? Would that be okay?"
    scene c2e22 with dissolve
    brk "After work sounds great. Though I kind of took a bus here today... will it be somewhere far?"
    scene c2e21 with qdissolve
    mc "Don't worry about that. It wouldn't make sense for us to go separately anyway. How about once we've finished up here we ride together... and then I'll drop you at home after. Does that sound fair?"
    scene c2e20 with dissolve
    brk "That would be very kind of you. I can't thank you enough... you've just made my entire day. You're far too sweet. Thank you!"
    scene c2e19 with qdissolve
    mc "Nah, no need to thank me. I'm looking forward to getting to know you."
    scene c2e37 with qdissolve
    brk "Yes! Same here. A proper date."
    scene c2e24 with dissolve
    brk "...just said the word date out loud didn't I? Oh God, I'm going to die of embarrassment."
    scene c2e23 with qdissolve
    mc "Oh no, there's no need to be embarrassed. I mean... it is kind of a date, right?"
    scene c2e24 with qdissolve
    brk "Y-Yes... you're right. I'm just so bad at expressing myself when I get anxious or nervous."
    brk "So, um..."
    scene c2e21 with qdissolve
    brk "(Please don't sound weird. Please don't sound weird...)"
    scene c2e24 with dissolve
    brk "M-Meet you on the f-flipside..."
    scene c2e23 with dissolve
    brk "(God dammit!)"
    mc "{i}*Nervous laughter*{/i} Yeah, thanks for coming by. Talk soon, okay? Please come to me if you need help with anything today, also. It's what I'm here for."
    scene c2e24 with qdissolve
    brk "Yes! Bye, [mc]."
    scene c2e23 with qdissolve
    mc "Heh... bye. I'll be right here if you need me."
    scene c2e18 with sdissolve
    mc "(Hm...)"
    scene c2e17 with fade
    $ renpy.pause (1.2, hard=True)
    scene black with sdissolve
    pause (1)
    scene c2e15 with sdissolve
    mc "(Nice to finally spend some time working. This is the first time in a few days that I've been able to shut my mind off and just focus for a while. It's almost... therapeutic. Sad that I wasn't able to catch up on everything, though.)"
    mc "{i}*Sigh*{/i} (This is going to be impossible. I'm starting to think I need an assistant just to keep up with everything. I mean I only missed one workday. What if I get sick and I'm out of commission for days? A week?)"
    mc "(Hm...)"
    scene c2e16 with dissolve
    mc "(Well, it is what it is. No sense dwelling. I better just...)"
    play sound "audio/sounds/knock.ogg"
    pause (.21)
    play sound "audio/sounds/knock.ogg"
    pause (.21)
    play sound "audio/sounds/knock.ogg"
    pause (.21)
    scene c2e14 with dissolve
    na "There's a knock at your door. This time it's your production coordinator, Mira."
    scene c2e13 with dissolve
    mc "Come in!"
    scene c2e12 with sdissolve
    mir "Heya, [mc]. Just wanted to drop by and let you know everything's set for the photoshoot."
    scene c2e10 with sdissolve
    mc "(Ah, Mira. I've hardly had a chance to talk to her since she started working here. She's looking cute today.)"
    mc "Thanks, Mira! Anything else I should know?"
    scene c2e11 with qdissolve
    mir "Oh, just one thing. Good job on hiring the new girl. She's precious."
    scene c2e8 with dissolve
    mc "Ah, yeah. She's a good one, that's for sure."
    scene c2e9 with qdissolve
    mir "I'm glad you agree. She really looks up to you, y'know?"
    scene c2e8 with qdissolve
    mc "She does?"
    scene c2e7 with dissolve
    mir "Oh, yeah. You're her hero. It's sweet... heh."
    scene c2e6 with qdissolve
    mir "(She definitely has a thing for him.)"
    scene c2e5 with dissolve
    mir "(I can see why... he's fucking sexy. Mmm...)"
    scene c2e6 with qdissolve
    mc "Heh. I wouldn't go that far. But she's an aspiring photographer so it's only natural. Thank you for coming to see me, Mira. I wish I were less busy so we could chat more."
    scene c2e4 with qdissolve
    mir "Hey, don't worry about it handsome."
    scene c2e6 with qdissolve
    mc "(Whoa, where'd that compliment come from?)"
    mir "(I'll catch him when he's not busy one of these days. It's a shame it hasn't happened yet. Always with the bad timing, Mira.)"
    mir "(That is... if the new girl doesn't beat me to it.)"
    scene c2e3 with dissolve
    mir "Anyway, boss. See ya!"
    scene c2e2 with dissolve
    mc "See you. Thank you again for checking in."
    stop music fadeout 07.0
    scene black with sdissolve
    pause (1)
    scene c2e15 with sdissolve
    mc "(Well... at least I'm {i}mostly{/i} caught up now. And thankfully I've had no more interruptions. This will have to do.)"
    mc "(Nice that I'm finally done. Was starting to feel like I'm in purgatory.)"
    scene c2e1 with dissolve
    mc "(And I almost completely forgot I'll be taking Brooke out tonight. Alright, I'll just text the girls to let them know I'll be late, then go see if she's ready to head out. I can't help but wonder why she was so eager to talk to me tonight?)"
    mc "(I guess she's really nervous about that upcoming gig... but still... is this a date? It feels like it.{w} Guess there's only one way to find out.)"
    scene black with sdissolve
    pause (2)

label brookedate:

    $ datesetvar = 0
    play music "<loop 0.0>audio/every_step.ogg" fadein 10.0
    scene c2fx3 with sdissolve
    mc "Brooke! I was looking all over for you. Everything okay?"
    scene c2fx2 with qdissolve
    brk "Um... yes! Everything's great. I-I'm just excited, that's all. Had to get some fresh air. So... are you all finished working?"
    scene c2fx1 with qdissolve
    mc "I am. Come on, I'll show you to my car and drive us somewhere nearby."
    scene black with sdissolve
    pause (2)
    scene c2f37 with sdissolve
    mc "(Wow. Such perfect timing.)"
    scene c2f36 with sdissolve
    mc "(The two of us riding through the sunset is kind of romantic, not gonna lie. I wonder what Brooke's thinking? The same thing maybe?)"
    scene c2f33 with dissolve
    brk "(Oh God... what am I doing? This is so nervewracking.)"
    scene c2f34 with dissolve
    brk "(I can't believe I'm sitting here right now... next to [mc] [sur] of all people.)"
    brk "(My idol. It feels like it was only a few days ago that I was staring at his Clickipedia.)"
    scene c2f33 with dissolve
    brk "(How'd I even manage the courage to ask him? Does he think I'm being weird? More importantly... does he see this as a date or just a friendly get-together?)"
    mc "(I should break the silence.)"
    scene c2f32 with dissolve
    mc "I'm excited for tonight. I've been meaning to get to know you better. You?"
    scene c2f31 with qdissolve
    brk "M-Me? Oh!{w} Ah yes.{w} I'm also better..."
    scene c2f32 with qdissolve
    mc "(Heh... I have no idea what she's trying to say there... but it's sweet that she's this nervous. Her demeanor has shifted some since our first meeting. Maybe it's because we're together outside of work?)"
    scene c2f35 with dissolve
    mc "(She must not get out too much.)"
    mc "Oh, we're here!"
    stop music fadeout 12.0
    scene c2f30 with sdissolve
    brk "Oh... wow! This place looks very nice."
    scene black with sdissolve
    pause (2)
    scene c2f26 with sdissolve
    brk "[mc]... this place is really fancy. Like... way moreso than I expected..."
    scene c2f27 with qdissolve
    mc "I'm glad you like it!"
    scene c2f29 with dissolve
    brk "I do! I really do."
    brk "But..."
    brk "It's probably way too expensive for me to afford. I don't think I'll be able to..."
    scene c2f25 with dissolve
    na "You wave your hand."
    mc "Don't worry about that at all. Tonight's on me."
    mc "(Note to self: give this girl a decent living wage.)"
    scene c2f24 with qdissolve
    brk "Oh no, I couldn't let you... I'm the one who asked you! I'm sure it's fine, it's probably not as pricey as I'm thinking."
    scene c2f27 with dissolve
    mc "Nonsense. You're the newest member of our team... so consider this my welcome present. Besides, I'm glad you're here with me and I just want us both to have a good time."
    play music [ "audio/this_is_not_effortless.ogg", "audio/invisible_beauty.ogg" ] fadein 12.0 fadeout 07.0
    scene c2f26 with qdissolve
    brk "Well, thank you!"
    scene c2f27 with qdissolve
    mc "Nah, don't worry about it. Come on, let's sit."
    scene black with sdissolve
    pause (2)
    scene c2f22 with sdissolve
    mc "Hm..."
    scene c2f20 with dissolve
    mc "Finding anything interesting?"
    scene c2f21 with qdissolve
    brk "Yes, absolutely. Everything sounds delicious. I'm having trouble deciding."
    scene c2f18 with qdissolve
    mc "Haha. I tend to have the same problem when I come here."
    mc "Do you mind if we wait a little bit to talk about work? I had kind of a crazy day; a lot to catch up on so I need to unwind."
    scene c2f19 with qdissolve
    brk "Of course not! I could use some unwinding too."
    scene c2f18 with qdissolve
    mc "Good, thank you!"

    menu dinnerset2:
        set menuset
        "Where You From?":

            mc "So are you from the area? Have you lived here your whole life?"
            scene c2f15 with qdissolve
            brk "Actually... not quite. I grew up in a very small, secluded town a few hours away. I lived with my parents for most of my life. I only moved closer to the city when I was in high school. To live with my grandmother."
            scene c2f14 with qdissolve
            mc "(It's rather strange to think that her parents left her with her grandmother.)"
            scene c2f17 with qdissolve
            brk "What about you? You grew up here in the city?"
            scene c2f18 with qdissolve
            mc "Well, no. I actually grew up more than halfway across the country, believe it or not."
            scene c2f14 with qdissolve
            mc "When I... had the accident, I was in pretty bad shape, as I mentioned to you before."
            mc "Well... the doctors didn't think I would make it. But my parents... or more specifically my father... wouldn't accept their conclusions."
            mc "So he had me transferred to one of the best hospitals in the country."
            scene c2f15 with qdissolve
            brk "UCSF?"
            scene c2f14 with qdissolve
            mc "Exactly, yeah. They're well known for treating patients with brain related injuries and neuroscience. And my father was willing to do whatever it takes... pay whatever he had to so he could save me."
            scene c2f15 with qdissolve
            brk "W-Wow... that's a lot to take in."
            scene c2f9 with qdissolve
            brk "..."
            brk "(He hasn't mentioned his parents except in past tense... are they...)"
            brk "(N-No... I won't pry. I don't want to ruin the mood. Besides, he's already opening up to me quite a lot.)"
            scene c2f8 with qdissolve
            brk "So when you woke up you just decided to stay here?"
            scene c2f14 with qdissolve
            mc "Yeah, and I'm glad that I did. I really like it here... and it's nice being close to the beach. It's different... a lot busier than where I grew up. Unfortunately, there's...{w} there's frankly nothing for me back home anymore."
            mc "(...or so I thought...)"
            mc "Um, outside of maybe an old friend or two. I guess I just decided to put it all behind me... start anew."
            scene c2f9 with qdissolve
            brk "(So that confirms it then... I'll have to ask him more about this later.)"
            scene c2f8 with qdissolve
            brk "I'm really sorry all of that happened to you, [mc]. And to be honest it's impressive how strong you've become in spite of it all."
            scene c2f14 with qdissolve
            mc "Aw, thank you. That's really sweet of you to say. And you don't have to worry about me... it'd take a lot more than a decade-long coma to keep me down."
            jump dinnerset2
        "Friends?":

            mc "Do you have many friends out this way? What do you normally like to do in your spare time?"
            scene c2f15 with qdissolve
            brk "Well... if I'm being honest I'm not the most social person. But I do have a very close friend that I've known pretty much since we were kids. She and I are inseparable! We spend nearly every waking moment together."
            scene c2f13 with qdissolve
            brk "We love to drink wine, watch movies, go shopping... nothing special; typical girl stuff."
            brk "Granted... we're not quite as close as we were a couple years ago, but that's mainly just because we were both busy getting our degrees... trying to get our careers off the ground."
            scene c2f15 with qdissolve
            brk "Chelsea's currently going through a breakup... so we've been spending more time together as of late."
            scene c2f12 with qdissolve
            mc "Well, it's good that you have someone close to you like that. To be friends for such a long time... you guys must be inseperable. So just the one, then?"
            scene c2f13 with qdissolve
            brk "Hehe. Just the one. I've always kept to myself... been pretty reserved. I didn't have the most normal upbringing in the world."
            scene c2f12 with qdissolve
            jump dinnerset2
        "Family?":

            mc "How about your family, Brooke? Do you have siblings?"
            pause (.5)
            scene c2f10 with dissolve
            brk "Oh, no. I was an only child. No siblings..."
            scene c2f11 with qdissolve
            mc "(Shit... I think I've struck a bit of a sour note...)"
            pause (.6)
            scene c2f8 with dissolve
            brk "As for my parents, well... I don't want to ruin your fun by getting into the details..."
            scene c2f9 with qdissolve
            brk "(And there's no way I can tell him about... about {i}her{/i} yet... I'm not ready for that story.)"
            mc "Oh, please don't worry about ruining my mood. I can think of nothing more fun than getting to know you better. Even if it's not the most pleasant story. Of course it's up to you, though."
            scene c2f5 with qdissolve
            brk "Well... we can go into more detail another time, but let's just say my mother and father were... they are very religious, and because of that they were always really strict..."
            brk "My good friend also came from a religious background. Her parents were pretty close family friends. That's the only reason her and I know each other... as I was never allowed to go out and meet people. Especially not boys..."
            scene c2f8 with qdissolve
            brk "When I was old enough to think for myself... I realized their behavior wasn't normal. They weren't just religious... they were fanatics. I slowly began to realize I didn't believe in the same things my parents did. This didn't sit well with them. In fact..."
            brk "One day, they just dumped me off at my grandmother's place... and I haven't seen or heard from them since."
            scene c2f7 with dissolve
            mc "..."
            mc "Wow, I'm so sorry to hear that. I apologize for bringing it up."
            scene c2f6 with dissolve
            pause (1.2)
            scene c2f5 with qdissolve
            brk "No! It's okay. I wanted to tell you. Don't worry. I won't let it sour my mood. Besides..."
            scene c2f15 with qdissolve
            brk "You've been through a lot worse, and you turned out just fine!"
            scene c2f12 with qdissolve
            mc "Heh... thank you. And well... despite what you've been through you seem to have grown into an amazing person. I honestly never would have guessed you came from a religious background. You seem very... normal."
            scene c2f13 with qdissolve
            brk "You think I seem normal?"
            scene c2f12 with qdissolve
            brk "(He's bluffing! I'm a complete weirdo.)"
            mc "Yes. In a good way, of course."
            scene c2f16 with qdissolve
            brk "I don't seem too reserved? Or needy? Because I've heard those before..."
            scene c2f18 with qdissolve
            mc "No, not at all. I mean, a little reservation is a good thing... but let's be real. You seriously impressed me at the interview..."
            mc "And... even more so now that I know you a little better."
            jump dinnerset2

    jump enddinnerset2

label enddinnerset2:

    scene c2f5 with qdissolve
    brk "[mc]... I need to tell you..."
    pause (.7)
    scene c2g78 with sdissolve
    van "Hey lovelies! Thank you for dining with us on this fine evening. I'm Vanessa. What's your name, Mister...?"
    scene c2g77 with dissolve
    mc "It's [mc]. Nice to meet you."
    scene c2g76 with qdissolve
    mc "(She seems friendly... but is she only going to ask my name? What about Brooke?)"
    mc "And this is..."
    scene c2g74 with sdissolve
    brk "I'm Brooklyn. Nice to meet you to-"
    scene c2g73 with dissolve
    van "That's nice. I hope you're finding everything to your liking, [mc]. Are your drinks okay? Is there anything else I can get you?"
    scene c2g72 with qdissolve
    brk "..."
    scene c2g71 with qdissolve
    van "(He's so hot! He has wonderful eyes. I can't look away.)"
    mc "Uh no... that's fine. Thanks. If you don't mind, we were just-"
    scene c2g70 with qdissolve
    van "Great. I'll be right back with a refill and to take your order. But don't hesitate to chase me down. For {i}any reason,{/i} okay?"
    scene c2g71 with qdissolve
    mc "Uh... sure. We'll do that."
    scene c2g70 with qdissolve
    van "I can't wait! Be right back!"
    scene c2g68 with sdissolve
    pause (.7)
    mc "Uh... so that was... interesting."
    scene c2g67 with qdissolve
    brk "Yeah! What was that all about? It's like she didn't even notice I was here..."
    scene c2g66 with qdissolve
    mc "Heh... your guess is as good as mine. Do you want me to talk to her? Say something to her, maybe? I don't want her to make you uncomfortable."
    scene c2g65 with dissolve
    brk "N-No! I'm okay if you're okay. I don't want to make a scene or anything..."
    brk "Besides... it's not like she was... mean or something."
    scene c2g66 with qdissolve
    mc "(She's clearly made Brooke uncomfortable. If it happens again, I'm going to say something.)"
    mc "Yeah... you're right."
    scene c2g69 with sdissolve
    brk "(What a strange girl...)"
    scene c2f3 with sdissolve
    mc "Did you figure out what you want to order?"
    scene c2f1 with qdissolve
    brk "I did! Yes. The Ribeye sounds amazing."
    scene c2f3 with qdissolve
    mc "No way? That's what I settled on too."
    scene c2f2 with qdissolve
    brk "Oh? Are you reading my mind, [mc]?"
    scene c2f4 with qdissolve
    mc "Heh... maybe you're reading mine..."
    scene c2f1 with qdissolve
    brk "Maybe I am! Would that make you uncomfortable?"
    scene c2f3 with qdissolve
    mc "No, but you may see some crazy shit! Especially with everything that's happened in the last few days..."
    scene c2f5 with qdissolve
    brk "Hm... I'm intrigued. Nothing bad, I hope?"
    scene c2f4 with qdissolve
    mc "{i}*Sigh*{/i} You probably wouldn't even believe me, to be honest..."
    scene c2f15 with qdissolve
    brk "This sounds serious. Is everything okay?"
    scene c2f14 with qdissolve
    mc "It's not really anything bad, per se. Depends on how you look at it. But... serious... that's definitely a good way of putting it."
    mc "It's a little hard to explain...{w} but the other day I woke up to the sound of my doorbell and..."
    scene c2g64 with dissolve
    pause (1)
    mc "(The fuck?)"
    scene c2g63 with dissolve
    mc "(At least she brought one for Brooke, too. The way she ignored her... I wouldn't be surprised if she hadn't.)"
    brk "Thank you for the dri-"
    scene c2g62 with dissolve
    van "Sorry to keep you waiting, [mc]! Are you ready to order?"
    scene c2g61 with dissolve
    mc "(That's it. There's no excuse for her to act rude towards Brooke like this. I'm going to say something...)"
    scene c2g60 with dissolve
    brk "Yes, we are. Miss... Miss-"
    scene c2g59 with dissolve
    brk "Sorry, what was your name again? Vicki? Valerie?"
    scene c2g57 with dissolve
    van "Oh..."
    scene c2g56 with dissolve
    mc "(Ha! Guess Brooke decided to speak up herself. Maybe she didn't want me to say anything. Still though... I don't think I can let this slide.)"
    scene c2g55 with qdissolve
    van "It's Vanessa. Um... what would you like, Ma'am?"
    scene c2g54 with qdissolve
    brk "We decided we're having the Ribeye. Right, [mc]?"
    scene c2g53 with dissolve
    mc "That's right. We have a lot in common it seems. Two medium Ribeyes for the lady and me. Thank you, miss."
    scene c2g52 with dissolve
    van "Good choice! That's my favorite too..."
    scene c2g51 with dissolve
    pause (.7)
    scene c2g50 with dissolve
    mc "(What the hell? This girl won't take a clue. She's totally flirting right in front of Brooke.)"
    scene c2g49 with sdissolve
    pause (1.2)
    scene c2f2 with sdissolve
    brk "The nerve of some people... jeez."
    scene c2f3 with dissolve
    mc "You alright?"
    scene c2f2 with qdissolve
    brk "Oh yeah, I'm fine. Thank you for staying polite. I don't know what her deal is... or why I get the feeling she's being purposefully rude, but I'd rather not find out. Haha!"
    scene c2f4 with qdissolve
    mc "(At least Brooke seems more amused than annoyed now. Still, at this rate, the girl will ruin the mood.{w} I should say something before I find her under the table sucking my cock or something.)"
    mc "Hey... if you don't mind, I'm just going to step away and use the restroom quickly. Try not to punch out the waitress while I'm gone."
    scene c2f16 with qdissolve
    brk "Haha! Shame on you! I wouldn't lower myself to such a degree!"
    scene c2g47 with fade
    mc "Be right back."
    scene black with sdissolve
    pause (1.3)

label brookedate2:

    stop music fadeout 09.0
    scene c2g46 with sdissolve
    mc "(Here she is. Just going to politely ask what her deal is...)"
    scene c2g45 with dissolve
    mc "Excuse me? Vanessa was it?"
    scene c2g44 with dissolve
    mc "Can I have a word with you?"
    scene c2g43 with dissolve
    van "Y-Yes of course... but before you do..."
    scene c2g42 with qdissolve
    van "{i}*Whispering*{/i} Do you mind if we go somewhere else? My manager is right there..."
    scene c2g41 with qdissolve
    mc "Um... actually..."
    scene c2g40 with sdissolve
    van "Shh! Please. Right this way. She'll fire me if she sees me talking to you over here."
    scene c2g39 with dissolve
    van "Just through here..."
    scene c2g38 with fadehold
    mc "(What the hell? Why did she bring me into a bathroom?)"
    scene c2g37 with sdissolve
    mc "Vanessa... what are we..."
    scene c2g36 with dissolve
    van "Shh! Don't worry. This is the employee bathroom. Just trust me."
    scene c2g35 with qdissolve
    mc "...I can see that.{w} But why are we in it?!"
    scene c2g34 with qdissolve
    van "Well... you wanted to talk to me, right? I just didn't want my manager to hear us. She's a total bitch! She follows me around like she's my mom or something."
    scene c2g33 with qdissolve
    mc "(I can't imagine why...)"
    mc "...Right. Well..."
    play music "<loop 0.0>audio/la_danse_fetish_de_femme.ogg" fadein 13.0
    scene c2g32 with dissolve
    van "And besides, we have total privacy. Nobody else is going to come in here..."
    scene c2g32 with vpunch
    mc "Whoa! Hold on... what are you..."
    scene c2g30 with dissolve
    mc "(What the fuck is she doing?)"
    scene c2g31 with dissolve
    van "Just relax and enjoy yourself, handsome. Be honest... this is why you wanted to see me?"
    scene c2g29 with qdissolve
    mc "What in the world are you doing? You can see that I'm with someone. You've been ignoring her the whole night! I literally came to complain about you...{w} not see tits!"
    scene c2g32 with dissolve
    mc "...which is going to be just a little bit... hard now!"
    scene c2g28 with dissolve
    van "What's wrong?"
    van "D-Do you not like them?"
    scene c2g27 with qdissolve
    mc "It's not about that! I didn't come here to...{w} to judge titties!"
    scene c2g26 with qdissolve
    van "L-Listen. I'm sorry for how I acted towards your friend. It's just..."
    van "I just had a feeling you guys weren't \"together...\" you know? Not like {i}that{/i} or anything. I wouldn't have flirted if I thought you were a couple."
    van "And I don't mean to be too forward... I'm not normally like this. But has anyone told you that you're ridiculously handsome?{w} Like... captivating!"
    scene c2g28 with qdissolve
    van "You are just so freaking cute! You have beautiful eyes, too."
    van "I love green eyes..."
    van "I've had a shitty day. I planned to go out after work just to let loose.{w} But then I saw you come in. D-Do you... do you think I'm crazy?"
    scene c2g27 with qdissolve
    mc "..."
    mc "(Crazy is one way to put it.)"
    scene c2g26 with qdissolve
    van "Do you want me? I can be yours, [mc]. No strings... you can even finish your date."
    scene c2g25 with pinkflash
    scene c2g25 with pinkflash
    scene c2g25 with pinkflash
    menu:
        mc "(This girl is actually insane. She's also hot, though. Maybe there's more than meets the eye? What am I supposed to say or do here?)"
        "Have Sex With Her":
            $ lust +=3
            $ van_romance = True
            jump vanessasex
        "I Can't Do This":

            $ pure +=3
            $ van_friends = True
            jump vanessafriendly
        "Go Fuck Yourself":

            $ dark +=3
            jump vanessarejection

label vanessasex:

    image vanessakiss1 = Movie(play="videos/Chapter 2/vanessakiss1.webm")
    image vanessabj = Movie(play="videos/Chapter 2/vanessabj2.webm")
    image vanessabj2 = Movie(play="videos/Chapter 2/vanessabj1.webm")
    image vanessadoggy1 = Movie(play="videos/Chapter 2/vanessadoggy1.webm")
    image vanessadoggy2 = Movie(play="videos/Chapter 2/vanessadoggy2.webm")
    image vanessafuck1 = Movie(play="videos/Chapter 2/vanessafuck1.webm")
    image vanessafuck2 = Movie(play="videos/Chapter 2/vanessafuck2.webm")
    image vanessacreampie = Movie(play="videos/Chapter 2/vanessacreampie.webm")

    scene c2g29 with qdissolve
    mc "This is super fucked up... what if we get caught?"
    scene c2g28 with qdissolve
    van "Nobody's coming into this bathroom."
    scene c2g29 with qdissolve
    mc "...You know my date is right on the other side of that wall, right?"
    scene c2g28 with qdissolve
    van "We better make it quick then..."
    scene c2g29 with qdissolve
    mc "..."
    scene c2gx1 with sdissolve
    mc "Alright then. You asked for it."
    show vanessakiss1 with dissolve
    van "{i}*Gasp*{/i}"
    van "Mmm..."
    pause
    scene c2gx2 with dissolve
    hide vanessakiss1 with dissolve
    van "(He's an amazing kisser...)"
    scene c2g24 with fade
    van "In here..."
    scene c2g23 with sdissolve
    van "Let me take care of you..."
    scene c2g22 with dissolve
    van "Oh God... you're..."
    scene c2g21 with dissolve
    van "I don't know if I can handle this monster!"
    scene c2g20 with dissolve
    mc "Hey, give it your best shot..."
    scene c2g21 with dissolve
    van "That I can do..."
    show vanessabj with sdissolve
    pause (.7)
    van "Nnmm!"
    mc "(Oh... fuck!)"
    pause
    mc "Fu-Fuck..."
    show vanessabj2 with dissolve
    hide vanessabj
    van "Mmm..."
    pause
    scene c2g19 with fade
    hide vanessabj2
    van "Fuck mee!"
    scene c2g18 with fade
    mc "(God damn... what a horny little slut.)"
    mc "Your pussy looks incredibly tight."
    scene c2g17 with sdissolve
    van "Are you surprised? I don't do this every day you know."
    mc "If you say so..."
    show vanessadoggy1 with sdissolve
    van "OH GOD."
    van "Ugggh!"
    van "Yes... oh sh-shit... [mc]..."
    van "I'm... I feel so full..."
    menu:
        mc "(God damn. This girl's pussy is devouring my cock like a hungry monster.)"
        "Dirty Talk":
            mc "For a slut you sure have a nice, tight little pussy."
            van "F-Fuck... you... I mean fuck {i}me!{/i} Yes, fuck me. I'm your slut."
            van "Take your little slut."
            van "Make me cum all over your big cock."
            mc "Keep talking like that and I'll make sure you can't walk straight for a month."
        "Romantic Talk":

            mc "You're so fucking beautiful. Your body is absolutely perfect."
            van "T-Thank you! You're so... mhm..."
            van "Sweet."
            van "You have an amazing cock! It feels so good...{w} you're burying yourself so deep inside of me!"
        "Something Else":

            $ d2_input = renpy.input("Say something dirty to her...", pixel_width=gui.dialogue_width).strip()
            if d2_input == "":
                $ d2_input="Do you like feeling that big cock stretch you out?"
            mc "[d2_input]"
            van "God yes! How are you this amazing?"
            van "Own me... m-make me yours!"
            van "Make me cum all over your big cock."
    pause

    menu:
        "Faster":
            pass

    show vanessadoggy2 with qdissolve
    hide vanessadoggy1
    van "Mmmm..."
    van "Right there! Fucking pound me..."
    pause (.8)
    van "{size=+5}Ugh!{/size}"
    van "{size=+10}Yes! F-Fuck me! Oh God...{/size}"
    mc "Shh! Keep your goddamned voice down!"
    pause
    scene c2g17 with dissolve
    hide vanessadoggy2
    van "W-Wait... don't finish yet!"
    scene c2g16 with fade
    van "Like this..."
    scene c2g15 with dissolve
    van "Fuck me against the stall."
    show vanessafuck1 with dissolve
    van "Y-Yeah... just like that."
    van "O-Oh..."
    van "I am so fucking wet..."
    pause
    show vanessafuck2 with fade
    hide vanessafuck1
    van "Yes! Fuck me!"
    mc "You're shaking..."
    van "I... I am going to cum soon..."
    pause
    show vanessafuck1 with fade
    hide vanessafuck2
    mc "Same..."
    mc "(Is she going to let me cum inside of her?)"
    mc "(Or maybe I should cover her little tits...)"
    van "C-Cum wherever you want... pleeease... m-make me cum with you!"
    menu:
        mc "(Can't hold out much longer...)"
        "Creampie Her":
            $ van_creampie = True
            show vanessafuck1 with flash
            show vanessafuck1 with flash
            na "Her pussy tightens down around the base of your shaft as you aggressively pump stream after stream inside of her."
            show vanessafuck1 with flash
            show vanessafuck1 with flash
            na "You feel her shaking as she orgasms... the warm feeling of your cum pooling inside of her and sending her over the edge with you."
            van "O-Oh Goddd!"
            van "Holy ff-fuck!"
            show vanessacreampie with qdissolve
            $ renpy.pause (10, hard=True)
            scene c2g13 with fade
            hide vanessacreampie
            van "{i}*Panting*{/i}"
            jump aftersex
        "Pull Out":

            mc "(I'll hold out just a little longer for her...)"
            show vanessafuck1 with vpunch
            van "O-Oh Goddd! I'm cumming. A-Are you going to..."
            show vanessafuck1 with vpunch
            na "Her body trembles as she orgasms... her fluids covering your shaft as you continue to thrust yourself inside her."
            scene c2g4 with sdissolve
            hide vanessafuck1
            mc "Fuuuck-"
            scene c2g4 with flash
            scene c2g4 with flash
            scene c2g4 with flash
            scene c2g3 with qdissolve
            $ renpy.pause (.2, hard=True)
            scene c2g2 with qdissolve
            van "Yes! Cum on my tits. I'm your filthy little whore..."
            van "{i}*Panting*{/i}"
            jump aftersex

label aftersex:

    stop music fadeout 06.0
    pause
    scene c2g12 with fadehold
    pause
    van "(Mmm... how did I get so lucky?)"
    mc "W-Well... you look like you enjoyed yourself."
    scene c2g11 with qdissolve
    van "I'm in heaven."
    scene c2g12 with qdissolve
    mc "(Shit... Brooke!)"
    mc "Vanessa... this was nice... but I shouldn't leave Brooke waiting any longer..."
    scene c2g11 with qdissolve
    van "Poor naïve girl... sitting all by herself while her date; no... her crush fucks another girl."
    scene c2g12 with qdissolve
    mc "Her crush?"
    scene c2g10 with dissolve
    van "Is it not obvious? The way she looks at you... crush might even be an understatement."
    scene c2g9 with qdissolve
    mc "(Hm... first Bernie says that... now her.)"
    van "(I wish someone would look at {i}me{/i} that way...)"
    scene c2g8 with dissolve
    van "N-Now go. Don't keep the poor thing waiting any longer. And here... take my number. I'd love to steal you away from her again sometime."
    scene c2g7 with qdissolve
    mc "You're shameless."
    scene c2g6 with dissolve
    van "Please. This was... just a preview. Play your cards right, and you'll be fucking me in her bed soon."
    scene c2g5 with qdissolve
    na "You roll your eyes and leave the girl to freshen up."
    jump afterbathroom

label vanessafriendly:

    stop music fadeout 06.0
    mc "Listen, Vanessa. I'm not trying to be mean here... but I came here to ask you to be a little bit nicer to my date. Not to have sex with you."
    scene c2g28 with qdissolve
    van "Oh..."
    scene c2g27 with qdissolve
    mc "That doesn't mean we can't... maybe hang out another time or something. To be honest, I haven't even had time to decide if I {i}want{/i} to know you."
    mc "Maybe if you show that you can be nice out there..."
    scene c2g28 with qdissolve
    van "Y-Yeah. Sorry about that.{w} I'm a little weird I guess... I just thought this was what guys liked.{w} But I can do that."
    van "Will you still take my number? Pretty please?"
    scene c2g27 with qdissolve
    mc "(Wait... how old is this girl? A minute ago she was confident... but now she's acting somewhat immature.)"
    mc "(Well... as long as she doesn't burn down my loved ones it'll be fine.)"
    mc "Sure. I can. No guarantees that we'll hang out, though."
    mc "Now if you'll excuse me... I have a date to get back to."
    scene c2g26 with qdissolve
    van "A-Alright! See you out there!"
    jump afterbathroom

label vanessarejection:

    stop music fadeout 06.0
    scene c2g27 with qdissolve
    mc "Listen, lady. Are you fucking insane? I'm in the middle of a date, here!"
    mc "One you're going to ruin, if you keep at it with this schtick."
    mc "If you want dick so badly, you should go suck off the bellboy."
    mc "In the meantime... I'm going to go back to what I was doing. And if you can't be nice to the girl I came with, you probably won't have a job anymore."
    mc "Sound fair?"
    scene c2g28 with qdissolve
    van "Y-Yes. You're right. I'm sorry. I don't know what I was thinking.{w} I feel stupid..."
    scene c2g27 with qdissolve
    mc "Good. Now, out of the way..."
    jump afterbathroom

label afterbathroom:

    scene black with sdissolve
    if van_friends == False:
        mc "(Well... here's to hoping she doesn't burn down my loved ones.)"
    pause (2)
    scene c2h26 with sdissolve
    play music "<loop 0.0>audio/kiss_the_sky.ogg" fadein 07.0
    if van_romance == True:
        mc "(Shit... did that really just happen? How am I going to face Brooke now? If what Vanessa said was true... then what just happened in there is pretty...)"
        menu:
            mc "(Well...)"
            "Pretty Hot":
                $ lust +=1
                mc "(Pretty hot, honestly. I mean... I should feel guilty and deep down I kind of do... but I'm more excited and aroused than anything. And besides... it's not like Brooke and I are together or anything. She's my employee... not my girlfriend.)"
                mc "(I look forward to doing it again sometime...)"
            "Messed Up":
                $ pure +=1
                mc "(Pretty messed up, sadly. But what can you do? I'm only man, after all. And besides... it's not like Brooke and I are together or anything. She's my employee... not my girlfriend.)"
                mc "(I can't beat myself up too much about it.)"
            "Funny":
                $ dark +=1
                mc "(Honestly, it's kind of amusing that I just plowed the cute waitress behind my date's back. Sorry, Brooke... but the nice ones always finish last. Not really my job to worry about your \"feelings.\")"
    else:
        mc "(Shit, did that really just happen? It's hard to believe what just went down.)"
        mc "(I probably won't tell Brooke what happened. That'd only make our date even more awkward than it already is, and she did ask me not to say anything.)"

    scene c2h25 with sdissolve
    if van_romance == True:
        mc "(What she said... is it true? Does Brooke really have a crush on me? Bernie said the same thing actually...)"
        mc "(Come to think of it, yeah. I'm pretty sure she does. I've dated enough since coming out of hibernation to know when a girl has a thing for me... and Brooke fits the bill.)"
    else:
        mc "(Did I make the right decision by turning her down? She's clearly a troubled girl. Maybe there's more to her than meets the eye?)"

    scene c2h24 with dissolve
    brk "Hey! Welcome back! Everything okay?"
    scene c2h23 with qdissolve
    mc "Hah. Yeah, I am. Sorry about that! Some guy ended up talking my head off about the stock market in there..."
    scene c2h22 with qdissolve
    brk "Haha, really? I thought guys didn't talk in the bathroom... not like us girls do, anyway."
    scene c2h23 with qdissolve
    mc "You're right! It totally weirded me out. I wanted to call for help... but he had a weapon."
    scene c2h22 with qdissolve
    brk "Oh noo. Haha! Stop messing with me."
    scene c2h23 with qdissolve
    mc "So... did our..."
    mc "{i}*Cough*{/i} Still no waitress, huh? Wonder what's taking so long with our food..."
    scene c2h22 with qdissolve
    brk "Right?! Worst service ever! This girl must be on drugs or something!"
    scene c2h20 with qdissolve
    mc "Haha. That... that wouldn't surprise me actually."
    mc "(If you only knew just how crazy she really is...)"
    scene c2h17 with dissolve
    mc "Oh, speak of the devil..."
    scene c2h18 with dissolve
    van "Two Ribeyes for the gentleman and the wonderful lady!"
    scene c2h15 with dissolve
    van "Can I get you anything else, sweetie?"
    brk "(Huh?)"
    scene c2h16 with qdissolve
    brk "No... t-that's alright. Thank you so much though. This looks great!"
    scene c2h15 with qdissolve
    van "Oh, I'm so glad to hear that. Enjoy the meal you two!"
    scene c2h14 with sdissolve
    brk "Well that was weird...{w} one minute it's like I don't exist, the next I'm the center of her world."
    scene c2h13 with qdissolve
    mc "Heh... yeah... I'm just as confused as you are, honestly."
    if van_friends == False:
        mc "(...Perhaps even more.)"
    elif van_romance == True:
        mc "(I hope she washed her hands.)"
    else:
        pass

    scene c2h14 with qdissolve
    brk "And here I was accusing her of being a drug addict, and a psycho..."
    scene c2h12 with dissolve
    brk "Oh, I feel so guilty now. Surely, it was all in my head. I should apologize to her... for snapping a bit earlier..."
    scene c2h11 with qdissolve
    menu:
        mc "(She wants to apologize? To Vanessa?)"
        "Not At All":
            $ pure +=1
            $ brk_pure +=1
            scene c2h10 with dissolve
            mc "Nah, don't worry about it. You weren't rude at all. Just a little forthright. You were just trying to get her attention, is all."
            scene c2h9 with qdissolve
            brk "Yeah, you're right! I'm being silly. I tend to overanalyze things sometimes..."
            brk "Well, thank you. For having my back in this, [mc]. I'm having a lot of fun with you tonight."
            scene c2h8 with qdissolve
            mc "You're welcome, sweetheart. I'm having a lot of fun too."
        "Joke Around":
            $ lust +=1
            $ brk_lust +=1
            scene c2h8 with dissolve
            mc "You sure you don't want me to hold her while you beat her up instead? We could lure her into the back alley, and..."
            scene c2h22 with qdissolve
            brk "Bahaha! You're ridiculous."
            brk "No, I don't want to beat her up! But you're right... it's not that serious. I'm probably just overreacting."
            scene c2h8 with qdissolve
        "You Should":
            $ dark +=1
            $ brk_dark +=1
            scene c2h1 with qdissolve
            mc "Yeah... I guess you did overreact a little. I mean... why would she intentionally ignore you? It was probably just in your head or something."
            mc "If I'm being honest, you were acting a little childish."
            scene c2h10 with qdissolve
            brk "..."
            brk "(Why would he say that to me... now I just feel stupid.{w} Did I really overreact that much?)"
            mc "Anyway, lets worry about that if or when she comes back."
            scene c2h2 with dissolve
            brk "Y-You're right. Thank you for being honest, [mc]."

    if van_romance == True:
        jump vanessa_remark
    else:
        jump brookedate3

label vanessa_remark:

    if van_creampie == True:
        mc "(Meanwhile my cum's probably still dripping down her legs... the little slut.)"
    else:
        mc "(Meanwhile, she probably still smells like my cum... the little slut.)"

label brookedate3:

    scene c2h4 with qdissolve
    mc "So... time to enjoy our food?"
    scene c2h9 with qdissolve
    brk "Yeah! I'm starved."
    scene black with sdissolve
    na "You finish your meals with very little smalltalk."
    scene c2h3 with qdissolve
    brk "Thank you for this. That was one of the best meals I've had in a while."
    scene c2h4 with qdissolve
    mc "Don't mention it, I'm glad I could spend this time with you. Before I get the check... you wanted to talk to me about that gig you have booked, right? You said it was tomorrow?"
    scene c2h12 with dissolve
    brk "Heh... I was so caught up in our discussion that I forgot to even mention it before now... sorry about that. You must think I just conned you into coming out on a date, huh?"
    scene c2h11 with qdissolve
    mc "So it is a date, then."
    scene c2h21 with dissolve
    brk "What? Oh shit!"
    scene c2h22 with qdissolve
    brk "N-No! Actually. Damn. Fuck. That's not..."
    scene c2h23 with qdissolve
    mc "It's alright. I'm sorry for teasing you. To be honest I've been thinking and..."
    scene c2h23 with pinkflash
    scene c2h23 with pinkflash
    scene c2h23 with pinkflash
    menu:
        mc "(What kind of relationship do I want with her?)"
        "Date Brooke":
            $ pure +=3
            $ lust +=3
            $ brk_rel = True
            $ brk_lust +=3
            $ brk_pure +=3
            mc "I was honestly hoping that's what this was. Like I said, I had a good time. I think you're really easy to talk to, and possibly the most genuine person I've met in a long time."
            mc "So I'm glad you think of it as a date, too."
            scene c2h6 with qdissolve
            brk "(Oh my God! Is this really happening?)"
            brk "(But I... holy crap. So he's not worried that we're co-workers?)"
            scene c2h11 with dissolve
            brk "(I guess... I guess it doesn't matter! I mean... that's one of the perks of being the boss, right?)"
            brk "(God... he's so...)"
            mc "Is everything alright?"
            scene c2h14 with qdissolve
            brk "Yes!"
            scene c2h6 with qdissolve
            brk "(Shit... I blurted that out like a schoolgirl. I need to calm down! I'm going to freak him out!)"
            scene c2h7 with qdissolve
            brk "Well you're really amazing yourself, [mc]. And I don't just mean as a, uh... professional. I mean, sure... I've been following your work religiously for ages."
            brk "And I totally admire you and want to be just like you... professionally I mean..."
            scene c2h9 with qdissolve
            brk "But I also had a good time. Even though I wasn't just trying to trick you into dating me, it does feel like a date..."
            scene c2h23 with qdissolve
            mc "So would you like to do it again sometime?"
            scene c2h21 with qdissolve
            brk "Yes... I'd really like to."
            scene c2h6 with qdissolve
            brk "(More than anything!!!)"
            mc "Awesome! Well, I know where you work, so..."
            scene c2h20 with qdissolve
            brk "Hehe."
        "Stay Professional":

            $ brk_dark +=3
            $ brk_rel = False
            scene c2h1 with qdissolve
            mc "I was just thinking that... if the circumstances were any different, then perhaps this could be a date. But I really think we should try keep things professional, Brooke."
            scene c2h2 with qdissolve
            brk "Y-Yeah... you're right. I don't know why I blurted that out..."
            brk "But uh, I was just joking!"
            scene c2h12 with dissolve
            brk "Yeah, totally just kidding around. Forget I said that, please! I'm so embarrassed."
            scene c2h11 with qdissolve
            mc "Nah, don't be embarrassed. I was just teasing you earlier. Truth is, I've enjoyed every minute of tonight and I mean what I said: if the circumstances were different..."
            scene c2h3 with qdissolve
            brk "R-Right! I understand."
            scene c2h10 with dissolve
            brk "([mc]...)"

    scene c2h4 with qdissolve
    mc "So what would you like to go over before your big job tomorrow?"
    scene c2h9 with qdissolve
    brk "Oh, right! Well, it may sound a little silly... like I'm making a big deal out of nothing..."
    scene c2h2 with qdissolve
    brk "But I think I'm having a little meltdown. Just a few days ago I was a mere amateur..."
    scene c2h12 with dissolve
    brk "And now I have a real gig! Surely, I shouldn't be so stressed out! What will people think of me if I show up and I'm just a mess?"
    scene c2h1 with dissolve
    mc "Actually, it's completely normal that you're stressed. I remember the first time I booked a gig, I was panicking for two whole weeks leading up to it."
    mc "I thought that maybe I'd get used to the idea and eventually calm my nerves... but nope! I felt anxious every... single... day. Hell, I barely slept."
    scene c2h2 with qdissolve
    brk "Wow, that sounds awful."
    scene c2h1 with qdissolve
    mc "It was! So in a way, you're actually lucky that it happened so fast. No matter when it happens, you'll have to do it eventually, right?"
    scene c2h3 with qdissolve
    brk "True! I really hadn't thought of it like that."
    scene c2h4 with qdissolve
    mc "None of us are perfect the first time we land a big job like yours, Brooke. Just remember, there's nothing wrong with being nervous. But if you don't mind me saying..."
    mc "I've seen your work. It's phenomenal. So frankly speaking, you've nothing to worry about."
    mc "Even if everything went horribly wrong... you already have one fan."
    stop music fadeout 06.0
    scene c2h2 with qdissolve
    brk "I do...? Who?"
    scene c2h1 with qdissolve
    mc "You're looking at him."
    scene c2h9 with qdissolve
    brk "Aww... thank you."
    scene c2h8 with qdissolve
    mc "Before we wrap up, let me give you some tips and go over a few things you should know..."
    scene black with sdissolve
    play music "<loop 0.0>audio/glacier.ogg" fadein 06.0
    pause (2)
    scene c2i44 with sdissolve
    brk "Thank you so much for everything, [mc]. How can I repay you for tonight?"
    scene c2i45 with qdissolve
    if brk_rel == True:
        mc "By going out with me again sometime soon."
        scene c2i44 with qdissolve
        brk "Of course! Whenever you want!"
        scene c2ix1 with qdissolve
        mc "Alright! I'll remember that."
        mc "(I'll just go in for a hug...)"
        scene c2i43 with sdissolve
        mc ".{w}.{w}.{w}Goodnight, Brooke."
        scene c2i42 with sdissolve
        scene c2i42 with vpunch
        brk "Mm..."
        scene c2i41 with sdissolve
        mc "(No way she-{w} kissed me!)"
        scene c2i40 with sdissolve
        brk "([mc]...)"
        $ renpy.pause (1.3, hard=True)
        scene c2i39 with dissolve
        scene c2i39 with vpunch
        brk "UM... GOODNIGHT!!!"
        scene c2i38 with dissolve
        mc "(Did that...)"
        mc "(Did that just happen?)"
    else:
        mc "Your friendship is enough, Brooke. You don't need to repay me."
        scene c2i44 with qdissolve
        brk "That's really kind of you. Thank you, [mc]. And we can hang out again whenever you want."
        scene c2ix1 with qdissolve
        mc "Alright. I'll remember that."
        mc "Goodnight, Brooke."
        scene c2i44 with qdissolve
        brk "Goodnight, [mc]."
        scene c2i38 with sdissolve
        mc "(Did I make the right decision tonight? I could've had her... and she's pretty sweet.)"
        mc "(Is that type of thing just not for me?)"
        mc "(Or am I just punishing myself?)"

    mc "(Well... no sense dwelling about it. I better head home.)"
    scene black with sdissolve
    pause (2)
    scene c2i37 with sdissolve
    mc "(It's pretty late. I wonder if the girls are still up?)"
    scene c2i36 with dissolve
    mc "(I'll check on [ali] first.)"
    scene black with dissolve
    pause (1)
    scene c2i35 with dissolve
    mc "(Well, these two are up.)"
    scene c2i34 with dissolve
    mc "(Time for some eavesdropping.{w} I'm not creepy, you're creepy.)"
    scene c2i32 with sdissolve
    liv "What! You're saying he saw you topless?!"
    scene c2i31 with qdissolve
    ali "How else would he have seen me, silly? I was sleepwalking. You know I like to sleep in the nude."
    scene c2i30 with dissolve
    liv "Hmm..."
    liv "(I haven't really thought much about this but three [age]-year-old girls living with a guy we only just met.{w} I know he's our [car] and everything but...)"
    scene c2i29 with dissolve
    liv "Hey, [ali]?"
    scene c2i28 with dissolve
    ali "Heya, [onick]!"
    scene c2i27 with dissolve
    pause (1.3)
    scene c2i26 with dissolve
    liv "Do you think [mcd] is... attractive? Like um...{w} cute... or handsome or whatever? I mean he's not exactly old."
    scene c2i23 with dissolve
    ali "Of course I do! [mcd] is very cute. He's much better looking than guys our age!"
    scene c2i24 with dissolve
    liv "Was he... did you get to see him naked, too?"
    scene c2i23 with dissolve
    ali "Well... he did show me his penis."
    scene c2i20 with qdissolve
    scene c2i20 with vpunch
    liv "He {b}what!?{/b}"
    scene c2i19 with qdissolve
    ali "Just kidding! Hahaha!"
    scene c2i18 with dissolve
    ali "(I shouldn't tell her that I saw [mcd]'s penis. Besides... it wasn't his fault!)"
    scene c2i17 with dissolve
    liv "Oh my God, [ali]... you almost gave me a heart attack!"
    scene c2i30 with dissolve
    liv "(I wonder... does he find us attractive, too? He saw [ali]'s boobs the first night we met him. Did he... did he get aroused by her?)"
    liv "(Would he get aroused if he saw me that way...? If he saw my...)"
    scene c2i15 with dissolve
    ali "Why do you ask anyway, [onick]? Do you have a crush on [mcd]?"
    scene c2i16 with dissolve
    liv "What? N-No..."
    scene c2i15 with dissolve
    ali "Your face is red! You're turning into a plum! Did I make you think about [mcd]'s penis?"
    scene c2i13 with dissolve
    liv "Shut up! Stop being mean!"
    scene c2i14 with dissolve
    liv "{i}*Sigh*{/i} I'm going to bed."
    scene c2i12 with sdissolve
    mc "(Shit. That's my cue!)"
    scene c2i11 with sdissolve
    ali "Yeah, me too I think. And I'm sorry for being mean!"
    scene c2i10 with dissolve
    liv "Goodnight, [ali]."
    scene c2i9 with fadehold
    mc "(Whew. That was too close.)"
    ali "Goodnight, [oli_nick]!"
    scene c2i8 with dissolve
    mc "(These girls are a trip. I had to stop myself from bursting into laughter a few times there.)"
    scene c2i7 with dissolve
    mc "(I'm glad [ali] didn't tell [liv] that she witnessed my raging erection! Not sure how she would've taken that one... even if it wasn't my fault.)"
    scene c2i6 with dissolve
    mc "(Did [anick] say that [liv] has a crush on me? What in the seven hells was that all about? Surely... she was just teasing?)"
    mc "(They're only [age], and I'm their [car], but...{w} what if it were true?)"
    mc "(I better stop thinking about this.{w} Before the FBI blasts in here.)"
    mc "(Right. Now to check on [mnick].)"
    stop music fadeout 08.0
    scene black with sdissolve
    scene c2i5 with sdissolve
    mc "(Hm... it's quiet. Too quiet.)"
    mc "(Either she's sleeping, or she's up to something. Regardless I should proceed with caution. I'm entering the dragon's den and it feels very \"registered sex offendery.\")"
    mc "(Here goes nothing...)"
    pause
    mc "(...on second thought, I value my life. And this girl would nail me to a cross if she caught me peeping.)"
    mc "(Still, it's tempting...)"
    mc "(What was that thing a great philosopher said, again?)"
    mc "(Ah yes. Yolo.)"
    na "With your cheeks in full-clench, you turn the knob as slowly as humanly possible before gently pushing on the door."
    scene c2i4 with sdissolve
    pause
    mc "(Hm... what is this familiar scent?)"
    mc "(It's pretty dark in here. I wonder if I'll be able to see...)"
    scene c2i3 with dissolve
    mc "(There's my girl. But she doesn't seem to be sleeping...)"
    mc "(She's clearly rummaging around in there...{w} under those covers.)"
    mad "{size=-3}{i}*Huff*{/i}{/size}"
    mc "(No way... is she...)"
    mad "{i}*Sigh*{/i}"
    mc "(Is she doing what I {i}think{/i} she's doing?)"
    mad "{size=-3}{i}Hmm...{/i}{/size}"
    mad "{i}*Gasp*{/i}"
    menu:
        mc "(Part of me wants to find out more. The other part feels that's wrong. Something is also telling me I should run for my fucking life.)"
        "Listen Carefully":
            $ lust +=1
            mc "(I'm going against my better judgement, but I need to see more of this. She's being strangely quiet... like she's trying to hide something.)"
            scene c2i2 with sdissolve
            mad "{size=-3}I-It isn't... workiingg...{/size}"
            mc "(She's masturbating. There's no doubt about it. I can see her clumsily rooting around down there even though she's mostly covered.)"
            mc "(Or at least... she's trying. It doesn't sound like things are quite working out for her... the poor thing.)"
            mc "(This could explain, at least partly, why she's so damn frustrated all the time. Not that she doesn't have plenty of other valid reasons for her behavior.)"
            mc "(I should find a way to help her with this problem. I'm not sure how I'll do it... but I've seen enough porn to have at least a few ideas in mind.)"
            mc "(Time to get out of here.)"
            mad "{size=-3}{i}Mmm...{/i}{/size}"
            mc "..."
            mc "(I said, \"time to get out of here.\")"
            na "You try to leave, but your feet refuse you."
            mc "(You'd betray me now?)"
            na "You breathe deeply in a subconscious attempt to calm yourself. Unfortunately, all of the blood has left your head and made its way to your genitals."
            mc "(Fuck! I know this is a normal reaction... and I don't want to sound like a teenager seeing his first boob...)"
            mad "{i}Uff...{/i}"
            mc "(But this girl is driving me fucking crazy! All of them are! Do they not {i}have{/i} clothes?)"
            mc "(My brain is telling me this is terribly wrong. That it's my job to protect her...)"
            mc "(But right now, all I can think about is tearing those covers away and stuffing her like a Thanksgiving Turkey.)"
            scene c2i3 with dissolve
            mc "(Look at me. What would Gracie think if she saw me right now?)"
            scene c2i1 with sdissolve
            mc "(No more stalling. I'd better go.)"
        "Leave Her Be":

            $ pure +=1
            mc "(No, I need to close this right away; give the girl some privacy. This is wrong.)"
            na "You try to leave, but your feet refuse you."
            mc "(You'd betray me now?)"
            scene c2i4 with sdissolve
            mc "(No, I must resist.)"
            scene c2i5 with sdissolve
            na "You gently shut the door."
            mc "(That was the hardest thing I've ever done in my life.)"
            mc "(She's masturbating. There's no doubt about it. I could see her clumsily rooting around down there even though she's mostly covered.)"
            mc "(Or at least... she's trying. It doesn't sound like things are quite working out for her... the poor thing.)"
            mc "(This could explain, at least partly, why she's so damn frustrated all the time. Not that she doesn't have plenty of other valid reasons for her behavior.)"
            mc "(I should find a way to help her with this problem. I'm not sure how I'll do it... but I've seen enough porn to have at least a few ideas in mind.)"
            scene c2i1 with sdissolve
            mc "(Time to get out of here.)"
        "Troll Her":

            $ dark +=1
            mc "(Hm... this would be a good time for some payback.)"
            mad "{size=-3}I-It isn't... workiingg...{/size}"
            mc "(She's masturbating. There's no doubt about it. I can see her clumsily rooting around down there even though she's mostly covered.)"
            mc "(Or at least... she's trying. It doesn't sound like things are working out for her.)"
            mc "(She's also trying extremely hard to be quiet, which means...{w} she's feeling very vulnerable right about now.)"
            mc "{i}*Smile*{/i}"
            mc "(As good a time as any to give her the biggest fright of her life.)"
            scene c2i4 with dissolve
            mc "(I think that I'll just...)"
            play sound "audio/sounds/doorslam.ogg"
            pause (.43)
            scene c2i5 with xdissolve
            scene c2i5 with vpunch
            pause (.3)
            mad "{size=+3}What the hell?!{/size}"
            pause (.5)
            mc "{size=-5}{i}Kekekekeke...{/i}{/size}"
            mad "{size=+2}H-Hello?? Who's there?!{/size}"
            scene c2i1 with dissolve
            mc "(Hahaha! Oh my God, I'm dying. I better get out of here.)"

    scene black with sdissolve
    pause (1.3)
    scene c2j32 with sdissolve
    play music "<loop 0.0>audio/passing_time.mp3" fadein 08.0
    mc "{i}*Sigh*{/i}"
    mc "(Bedtime.)"
    mc "(So much to process... so little time...)"
    mc "(Where has this week gone, anyway? The girls have already been here for a few days...)"
    scene c2j31 with fade
    mc "(I wonder...)"
    mc "(What were they like? When they were little?)"
    mc "(...if only I could get my ten years back.)"
    mc "(I could...)"
    mc "{i}*Yawn*{/i}"
    mc "(Find Gracie. See her... together with the girls.)"
    mc "(So much I could do in ten years.)"
    mc "(My head is swirling.)"
    mc "(I don't know what I'm doing.)"
    mc "(I have no idea...)"
    mc "(And this empty feeling inside me...)"
    mc "(It's like... half of me is missing.)"
    mc "{i}*Sigh*{/i}"
    mc "..."
    mc "(Things seem to be going well enough. I think.)"
    mc "(So why do I feel this... incredible sense of dread? Like something's about to go horribly wrong?)"
    mc "..."
    stop music fadeout 15.0
    scene c2j30 with sdissolve
    mc "(...Will I dream of her tonight?)"
    scene black with sdissolve
    $ renpy.pause (6, hard=True)
    scene c2j29 with sdissolve
    mc "{i}*Groan*{/i}"
    scene c2j28 with sdissolve
    mc "(Morning again.)"
    scene c2j27 with sdissolve
    mc "(No more dreams of Gracie? What's going on?{w} It feels like I never get to see her when I need her the most.)"
    mc "(What if...{w} what if I'm never able to dream of her again?)"
    mc "(No... the world isn't that cruel.)"
    scene c2j26 with qdissolve
    $ renpy.pause (.5, hard=True)
    scene c2j25 with qdissolve
    $ renpy.pause (.5, hard=True)
    scene c2j26 with qdissolve
    $ renpy.pause (.5, hard=True)
    scene c2j25 with qdissolve
    $ renpy.pause (.5, hard=True)
    scene c2j26 with qdissolve
    $ renpy.pause (.5, hard=True)
    scene c2j25 with qdissolve
    mc "(Oh, it looks like I have a new notification. Better check that out.)"
    if tbed == True:
        scene c2j24 with sdissolve
    else:
        scene c2j23 with sdissolve

    "{i}Hello, [mc]! I hope you're excited for that photoshoot! As it happens, I'm pretty friendly with Tiffany's agent due to my past work... so I helped Bernie with that \"favor\" you needed.{/i}"
    "{i}Both Tiffany and her agent know you're bringing your [dau] along to the photoshoot, and they're perfectly okay with it!{/i}"
    "{i}Congratulations, by the way! That's a hell of a story. You'll have to give me the details the next time we see each other. Anyways, have fun! -Mira{/i}"
    mc "(Wow. Just in time, too. That was really nice of her to call in a favor like that. So I'll be able to bring [ali] to meet Tiffany after all.)"
    play sound "audio/sounds/knock.ogg"
    pause (.21)
    play sound "audio/sounds/knock.ogg"
    pause (.21)
    play sound "audio/sounds/knock.ogg"
    pause (.21)
    scene c2j22 with fade
    ali "[mcd]? Are you in there? C-Can I come in?"
    mc "(Oh! Speak of the devil.)"
    mc "O-Of course [ali]. Let me just put some clothes on quickly."
    scene black with sdissolve
    pause (1)
    mc "Come in!"
    scene c2j21 with sdissolve
    mc "(Oh no. She's not looking so good...)"
    play music "<loop 0.0>audio/nocturne.ogg" fadein 12.0
    scene c2j20 with fade
    mc "S-Sorry. It takes me a few to pull myself together in the morning. Is everything okay?"
    scene c2j19 with sdissolve
    ali "Um... [mcd]... can I talk to you?"
    scene c2j18 with dissolve
    mc "Of course you can. What's on your mind, [ali]?"
    scene c2j16 with dissolve
    ali "I think I need advice... from an old person."
    scene c2j15 with dissolve
    mc "{i}*Grinning*{/i} Old person?! You wound me..."
    mc "But yeah... I can try."
    mc "(Sometimes I don't even know if I'm doing the right thing myself. I hope I can help her.)"
    scene c2j14 with dissolve
    ali "{i}*Sniff*{/i}"
    mc "(Oh no... is s-she...)"
    scene c2j13 with dissolve
    $ renpy.pause (.7, hard=True)
    scene c2j12 with qdissolve
    ali "[mcd]... h-how do I make the pain go away?"
    scene c2j13 with qdissolve
    ali "{i}*Sniff*{/i}"
    scene c2j12 with qdissolve
    ali "How do I s-stop...{w} hurting...?"
    pause (.7)
    scene c2j11 with qdissolve
    mc "To be honest... I've asked myself the same question many times."
    scene c2j12x with qdissolve
    ali "Y-You have?"
    scene c2j11 with qdissolve
    mc "Yeah..."
    mc "And the honest answer is... it never really does."
    scene c2j12x with qdissolve
    ali "{i}*Sniff*{/i} It doesn't?"
    scene c2j13 with qdissolve
    na "You shake your head softly."
    scene c2j11 with qdissolve
    mc "Not completely..."
    mc "But given enough time... it does get easier. You get used to it; I think."
    scene c2j12x with qdissolve
    ali "T-That doesn't sound very nice..."
    scene c2j11 with qdissolve
    mc "I know. It isn't..."
    mc "But when the worst of it passes..."
    mc "You'll be stronger for it."
    mc "The truth is we don't get rid of pain. We just learn how to cope."
    mc "The only thing we can do... is try not to focus on the things we cannot control. Keep your head up and keep moving forward."
    mc "And eventually, you'll begin to accept what's happened."
    mc "With time comes a hard lesson: pain... death... it's simply..."
    mc "It's part of life. Without it, I don't think there'd be any meaning to it all."
    scene c2j12x with qdissolve
    ali "{i}*Sobs*{/i}"
    scene c2j13 with qdissolve
    mc "(Oh, fuck me. I think I got a little carried away there. I've just made her feel even worse...)"
    mc "(Way to go, Aristotle.)"
    scene c2j11 with qdissolve
    mc "Um... what I meant to say is..."
    pause (.7)
    scene c2j9 with sdissolve
    ali "That makes perfect sense! Thank you [mcd]. I feel better... I think."
    scene c2j10 with qdissolve
    $ renpy.pause (1, hard=True)
    scene c2j7 with sdissolve
    mc "Oh! Y-Yeah... you're welcome.{w} I uh... I knew it would help..."
    scene c2j8 with qdissolve
    mc "(...Whew.)"
    mc "(Oh... I know just the thing that will cheer her up.)"
    mc "(We can't have her being sad on a day like today. That said... I still want it to be a surprise.)"
    scene c2j5 with dissolve
    mc "Hey... you know what else will cheer you up?"
    scene c2j6 with qdissolve
    ali "Huh? Tell me!"
    scene c2j5 with qdissolve
    mc "Getting out for a while. Come with me today, just the two of us. Let's go do something exciting together!"
    scene c2j6 with qdissolve
    ali "Just me and you?"
    scene c2j5 with qdissolve
    mc "Yup. Just the two of us. Your sisters won't mind, will they?"
    scene c2j4 with qdissolve
    ali "Not at all! That sounds like a great idea, I think."
    scene c2j6 with qdissolve
    ali "So what will we do?"
    scene c2j5 with qdissolve
    mc "Hm... don't you worry about that. I know just the thing. And on the way there... we can stop and buy you the nicest outfit you can find. Would that make you feel better?"
    scene c2j4 with qdissolve
    ali "Are you kidding? I love buying new clothes! That sounds super fun!"
    scene c2j5 with qdissolve
    mc "Good. I got some things to do this morning... but I'll pick you up in the afternoon, okay?"
    scene c2j3 with dissolve
    $ renpy.pause (.8, hard=True)
    scene c2j2 with qdissolve
    ali "Mwah."
    scene c2j6 with sdissolve
    ali "Thank you, [mcd]. I will be ready."
    scene c2j5 with qdissolve
    mc "Good.{w} H-Hey, before you go... do you know what your sisters are up to?"
    scene c2j6 with qdissolve
    ali "Oh, hm... [mad] is watching TV in the living room last I checked. And I think [liv] is working on something in her room."
    stop music fadeout 10.0
    scene c2j7 with sdissolve
    mc "(Working on something? Interesting. Must have a project going on that laptop of hers.)"
    mc "Great. Thanks [ali]. See you in a little while, okay? Oh! And um... feel better!"
    scene c2j1 with dissolve
    ali "Huh? I can feel things just fine. I said I was sad... not prariepledgic!"
    mc "(...nevermind.)"
    scene black with sdissolve
    pause (1)
    scene c2j22 with sdissolve
    mc "(She's special, that one.)"
    mc "(In more ways than one... but utterly precious.)"
    play music "<loop 0.0>audio/please_advise.ogg" fadein 13.0
    mc "(Alright... I have a little bit of time before meeting Natalie. I should go check on [mnick] and [liv].)"
    mc "(Decisions, decisions...)"

    menu:
        mc "(Who will I go see first?)"
        "[liv]":
            $ lust +=2
            $ liv_lust +=2
            $ liv_first = True
            scene black with sdissolve
            pause (1.2)
            jump liv_first
        "[mad]":

            stop music fadeout 07.0
            $ pure +=2
            $ liv_pure +=2
            scene c2l23 with sdissolve
            mc "(Hm... there she is. My wonderful [dau]... who I should be uniquely cautious around.)"
            scene black with sdissolve
            pause (1.2)
            jump mad_chat

label liv_first:

    scene c2k24 with sdissolve
    mc "(I think I'll go see [liv]. I'm curious to know what she's working on.)"
    scene mtwoa10 with fadehold
    menu:
        mc "(I should probably knock.)"
        "Knock":
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)

    uk "C..m...in.."
    mc "(Well I could barely hear that, but I'm ninety-nine percent sure she just said \"come in.\""
    scene c2k23 with dissolve
    mc "Hey [onick], good morning!"
    scene c2k22 with dissolve
    scene c2k22 with vpunch
    liv "Eep! Oh my God!"
    scene c2k21 with qdissolve
    mc "S-Shit! [liv], I didn't realize... I thought you said..."
    scene c2k22 with qdissolve
    liv "I-I'm changing! E-Excuse me for a minute, please!"
    scene c2k21 with qdissolve
    mc "Fuck! I'm sorry!"
    scene mtwoa10 with qdissolve
    scene mtwoa10 with vpunch
    pause
    scene c2k20 with sdissolve
    mc "(.{w}.{w}.What have I done?)"
    mc "(That was a big mistake. My heart is racing. I think the voice I heard was that video she's watching on her laptop...)"
    scene c2k19 with dissolve
    mc "(I'm done for. I'll be the next \"To Catch a Predator.\")"
    stop music fadeout 17.0
    scene c2k18 with sdissolve
    if tbed == True:
        liv "S-Sorry about that, Dad. I should've checked to see if the door was locked..."
    else:
        liv "S-Sorry about that, [mc]. I should've checked to see if the door was locked..."

    scene c2k17 with qdissolve
    mc "[liv] I am so, so sorry, that was actually my fault. I knocked on the door and I thought you said \"come in.\" I should've been more careful."
    scene c2k18 with qdissolve
    if tbed == True:
        liv "I-It's okay. Be-Besides... we're family, right?"
    else:
        liv "I-It's okay. Be-Besides... we're housemates, right?"

    scene c2k17 with qdissolve
    mc "Uh... yeah. Totally. Completely normal."
    mc "(I'm fucked!)"
    jump liv_chat2

label liv_chat1:

    scene mtwoa10 with sdissolve
    menu:
        mc "(I should probably knock.)"
        "Knock":
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)

    scene c2k17 with fade
    liv "Oh! Hey [mcd]. I'm glad you're still here."
    jump liv_chat2

label liv_chat2:

    scene c2k15 with sdissolve
    liv "Come on in."
    scene c2k16 with qdissolve
    mc "(She looks cute this morning.)"
    play music [ "audio/campfire_song.ogg", "<loop 0.0>audio/parkside.ogg" ] fadein 07.0 fadeout 06.0
    scene c2k6 with qdissolve
    mc "How's my girl doing today?"
    scene c2k7 with qdissolve
    liv "I'm good! Thank you."
    scene c2k6 with qdissolve
    mc "Glad to hear that. I saw [ali] a few minutes ago. She said you were working on something?"
    scene c2k11 with qdissolve
    liv "Oh, yeah! We haven't really had the chance to talk about anything like that."
    scene c2k12 with qdissolve
    liv "I was actually just taking a quick break to get changed and brush my hair, but yeah! I have a little project that I've been working on for quite a while. It's just a small hobby I picked up after a project in school."
    scene c2k6 with qdissolve
    mc "Oh? What is it?"
    scene c2k9 with qdissolve
    liv "Um... well... it's..."
    scene c2k8 with qdissolve
    mc "(I guess she's a little shy about it. Aha.)"
    scene c2k12 with qdissolve
    liv "I'm actually writing a book, you see... it's a romance novel."
    scene c2k13 with qdissolve
    mc "Will you let me read it someday?"
    scene c2k9 with qdissolve
    liv "Umm...!"
    scene c2k10 with qdissolve
    liv "...maybe! Haha. I don't know..."
    liv "It's probably stupid. But... I guess if I ever plan to take writing seriously, it would be good to get someone's feedback, huh?"
    scene c2k6 with qdissolve
    mc "That's true. I would be happy to give you some pointers. I can offer my vast knowledge and expertise in the field of romance."
    scene c2k14 with qdissolve
    liv "Haha! Don't be silly..."
    scene c2k9 with qdissolve
    liv "But not now, okay? Ever since all this stuff happened with mom..."
    liv "I've been having a hard time progressing. It's like I'm stuck..."
    scene c2k8 with qdissolve
    mc "Hm... that's no good. On the one hand, I can understand why you'd be lacking in motivation: you've been through a lot."
    mc "On the other hand..."
    mc "The best artists harness their emotions... and use them to make their art more profound and emotional. I'm not saying you should rush into it... it's still so soon."
    mc "But the pain, the sadness you're feeling... or perhaps your curiosity and wonder; maybe you could harness it and give your readers the opportunity to experience those emotions through your story."
    scene c2k7 with qdissolve
    liv "T-That's actually really good advice. Thank you so much."
    scene c2k6 with qdissolve
    mc "You're welcome, [oli_nick]. So I'm going to let you get back to it, okay? I have to get going, as I'm meeting someone shortly."
    scene c2k7 with qdissolve
    liv "No problem! I'm really glad you came to see me."
    scene c2k9 with qdissolve
    liv "Um..."
    liv "...can I have a hug?"
    scene c2k8 with qdissolve
    mc "Of course. Come here."
    scene c2k5 with sdissolve
    mc "(Mm... good hug. I could tell that she needed this.)"
    liv "(He's so solid and... shapely.{w} He seriously must work out like ten times a week!)"
    liv "(Hmm... is he leaving to meet a girl again? Like last night? Could he be dating someone? And if he is... I wonder why he hasn't mentioned it yet...)"
    scene c2k3 with dissolve
    liv "(Grr...)"
    liv "(Uhm, why am I getting angry again?)"
    scene c2k4 with sdissolve
    liv "Have a good afternoon, [mcd]."
    scene c2k3 with sdissolve
    mc "Thanks [liv], you too."
    jump after_liv

label after_liv:

    scene black with sdissolve
    pause (2)
    scene c2k2 with sdissolve
    mc "(I feel like I'm growing pretty close to [liv]. That felt... productive.{w} At the same time it doesn't feel like she was too happy about me leaving again.)"
    mc "(Maybe I should take some time off work after all. There's so much to cover with the girls... so much to learn about them. I haven't really had the chance to spend time with the three of them together yet, even.)"
    if tbed == True:
        mc "(Not to mention I should ask them about school. Shouldn't they still be students?)"
        mc "(And if that's the case... what happened? Why no mention of it yet? Well... it {i}is{/i} summertime, I guess.)"
        mc "(Also, I need to start taking more of a parental role, I think. I've been more of a friend to them... knowing that they've been through so much. But a firm hand and a little guidance will likely be good for them. After all, they're still only [age].)"
    else:
        mc "(Not to mention ask them about college. Shouldn't they be students?)"
        mc "(And if that's the case... what happened? Why no mention of it yet? Well... it {i}is{/i} summertime, I guess.)"
        mc "(Also, I need to start taking more of a \"caretaker\" role I think. I've been more of a friend to them... knowing that they've been through so much. But a firm hand and a little guidance will likely be good for them. After all, they're still only [age].)"
        scene c2k1 with dissolve
    stop music fadeout 07.0
    if liv_first == True:
        mc "(Well, I better go see [mnick] now. Then it's time to leave for my meeting with Natalie. Don't want to keep {i}her{/i} waiting, that's for sure.)"
        scene c2l24 with sdissolve
        mc "(Hm... there she is. My wonderful [dau]... who I should be uniquely cautious around.)"
        scene black with sdissolve
        pause (1.2)
        jump mad_chat
    else:
        mc "(Well, almost time to meet with Natalie so I better hop to it. Don't want to keep {i}her{/i} waiting, that's for sure.)"
        $ renpy.pause (2, hard=True)
        jump glenn_driveway

label mad_chat:

    play music "<loop 0.0>audio/mysteries.ogg" fadein 09.0
    scene c2l22 with sdissolve
    mc "Oh, [mad]. There you are. Good morning."
    scene c2l21 with dissolve
    mad "Hmph!"
    mc "Still not interested in talking, I see."
    scene c2l20 with qdissolve
    mad "I... I didn't say that."
    scene c2l21 with qdissolve
    mc "(I'll carefully make my approach.)"
    scene c2l19 with dissolve
    mad "W-Why? What are you up to, anyway?"
    scene c2l18 with dissolve
    mc "Well, I have to go meet someone in a few, so there's that."
    scene c2l17 with dissolve
    mc "I guess I just wanted to say hi and ask how you're feeling."
    scene c2l14 with qdissolve
    mad "Leaving again? Typical..."
    scene c2l16 with dissolve
    mc "Y-Yeah... sorry about that. I really want to spend more time with you girls... but there's something I need to take care of first while someone I know is in town."
    scene c2l15 with qdissolve
    mad "Someone you know?"
    scene c2l16 with qdissolve
    mc "...Yeah. It's a long story."
    scene c2l14 with qdissolve
    mad "Oh, I'm sure it is! And I'm sure it's oh-so-urgent. Far more so than your..."
    scene c2l13 with qdissolve
    mad "Your housemates."
    scene c2l17 with qdissolve
    mc "You mean my [dau]s?"
    scene c2l14 with qdissolve
    mad "As if!"
    scene c2l6 with dissolve
    mc "..."
    scene c2l17 with dissolve
    mc "(She's still not into the whole [car] thing, I guess.)"
    mc "[mnick], listen..."
    scene c2l14 with qdissolve
    mad "It's [mad]!"
    scene c2l17 with qdissolve
    mc "(...I can't tell if she's being cute or annoying right now.)"
    menu:
        mc "(Regardless, I need to be careful how I respond.)"
        "Understanding Response":
            $ pure +=1
            $ mad_pure +=1
            mc "Okay, [mad] then. You're right, I'm sorry."
            scene c2l12 with qdissolve
            mc "And I get it. I can't just expect you to think of me as your [car] right away just because I'm suddenly a part of your life."
            mc "But just so you know... I want to try. To be a [car] to you girls..."
            scene c2l14 with qdissolve
            mad "Y-You do?"
            scene c2l12 with qdissolve
            mc "Yes... if that's okay with you."
            scene c2l13 with qdissolve
            mad "W-Well... I don't know..."
            scene c2l14 with qdissolve
            mad "Can I go back to my show, now?"
            scene c2l6 with qdissolve
            mc "Of course. See you!"
        "Sarcastic Response":

            $ lust +=1
            $ mad_lust +=1
            mc "So [mnick], then. Got it!"
            scene c2l10 with qdissolve
            mad "I said..."
            scene c2l9 with qdissolve
            mc "Oh, and you're right. Don't worry about the \"you're not our [car]\" thing. It makes far more sense that some random [age]-year-old girl is laid up in my house, sitting on my couch, and watching my TV."
            scene c2l5 with qdissolve
            mad "B-But..."
            scene c2l9 with qdissolve
            mc "Should I bring you a snack or something?"
            scene c2l10 with qdissolve
            mad "Sh-shutup! You know what I mean..."
            scene c2l9 with qdissolve
            mc "Ah-huh. I also know that I'm your [car], whether you like it or not... [mnick]."
            scene c2l8 with qdissolve
            mad "Y-You... do-doucheb-"
            scene c2l7 with qdissolve
            mc "Pfft. Don't blow a gasket. I'm just teasing you, okay?"
            scene c2l10 with qdissolve
            mad "F-Fine!"
            scene c2l14 with qdissolve
            mad "Can I go back to my show, now?"
            scene c2l6 with qdissolve
            mc "Of course. See you!"
        "Harsh Response":

            $ dark +=1
            $ mad_dark +=1
            $ harsh_rsp = True
            mc "...funny, I don't remember asking for permission to call you [mnick]."
            stop music fadeout 07.0
            scene c2l9 with qdissolve
            mc "Actually, now that I think about it..."
            mc "I don't need your consent to do a damn thing. It's the opposite. So listen carefully..."
            scene c2l12 with qdissolve
            mc "This attitude of yours? It's going to change. It's not going to fly around here. You're in my house... you are my [dau], whether you like it or not..."
            mc "And do you know what that means?"
            mc "That means I'm in charge."
            scene c2l8 with qdissolve
            mad "I-I don't have to listen to you!"
            scene c2l7 with qdissolve
            mc "You sure about that? Because you're welcome to try me.{w} What are you watching? Would be a shame if someone disconnected the TV."
            scene c2l8 with qdissolve
            mad "W-Why are you being mean to me?"
            scene c2l3 with qdissolve
            mc "Mean? Nah. I'm just telling you how it's going to be around here."
            mc "I have no interest in being mean to you, [mad]. But you will obey me. Understand?"
            scene c2l4 with qdissolve
            mad "Oh yeah? And what if I don't?!"
            scene c2l5 with qdissolve
            mc "Let's find out, shall we?{w} I'm going to be out for most of the day... and when I come back; I want this place to be spotless. You're going to clean the house."
            mc "If you don't... there will be consequences when I return."
            scene c2l3 with qdissolve
            mad "(He must be joking, right? I... I don't have to listen to him! I... I'm [age]! He can't boss me around... can he??)"
            mc "Heh..."
            scene c2l1 with dissolve
            mc "See you later, [mad]. Remember what I said."
            scene c2l2 with qdissolve
            mad "B-But!"
            scene c2l1 with qdissolve
            mc "No buts young lady."

    if liv_first == False:
        scene black with sdissolve
        pause (2)
        stop music fadeout 07.0
        scene c2k24 with sdissolve
        mc "(Time to see what [liv] is up to. I'm curious to know what she's working on.)"
        jump liv_chat1
    else:
        pass

    scene black with sdissolve
    if harsh_rsp == True:
        mc "(I hope I'm doing the right thing here. I don't know if I'm being too hard on her or what... but what just went down has the potential to change our relationship for good.)"
    else:
        mc "(I think that went okay. I don't know if I'm doing the right thing here... she's incredibly hard to read sometimes.)"
        stop music fadeout 07.0
    $ renpy.pause (1.2, hard=True)

label glenn_driveway:

    scene c2d35 with sdissolve
    mc "(Alright! Time for my coffee date. Let's see how this goes...)"
    mc "(I'd be lying if I said I wasn't a little nervous. Last time I saw her she held me at knifepoint.)"
    scene c2d34 with sdissolve
    mc "(She also slapped me so hard that I still feel the sting.)"
    mc "(Ah well. I owe her this much. She deserves some sort of reconciliation... or closure.)"
    scene c2m27 with sdissolve
    mc "(To be honest, I should be grateful she even agreed to do this.)"
    play sound "audio/sounds/skidbrakes.ogg"
    scene c2m26 with sdissolve
    scene c2m26 with vpunch
    $ renpy.pause (1.1, hard=True)
    mc "Holy shit what the fuck?! I almost hit this guy!"
    mc "(What's this dude doing blocking me in my own driveway? God damned Asian drivers.)"
    play music "<loop 0.0>audio/a_hand_in_the_dark.ogg" fadein 10.0
    scene c2m25 with dissolve
    mc "(Wait. Is that who I think it is...?)"
    mc "(I better get out and see what his deal is...)"
    scene c2m24 with dissolve
    gln "Stay in the fucking car!"
    mc "(What the fuck??)"
    scene c2m23 with dissolve
    mc "He's checking my license plate? He's not even on duty..."
    mc "(Fuck this... I'm getting out. He can't just-)"
    scene c2m22 with dissolve
    gln "I said stay in the God damned vehicle!"
    scene c2m21 with dissolve
    mc "(Jesus Christ. What's this guy's problem?)"
    scene c2m19 with dissolve
    mc "What the fuck is going on? Why are you..."
    scene c2m20 with dissolve
    gln "License and registration."
    scene c2m19 with dissolve
    mc "Fuck that...{w} cop or not I'm not giving you shit. I did absolutely nothing wrong. I haven't even left my driveway!"
    scene c2m18 with dissolve
    gln "Heh. You got a little attitude, huh? I could take you into the station if I wanted..."
    scene c2m17 with dissolve
    mc "..."
    mc "It's Mr. Cole, right? You're my neighbor. What's going on? Why are you yelling at me like this in my own driveway?"
    scene c2m18 with dissolve
    gln "That's Officer Cole to you, and I'm the one asking the questions here."
    scene c2m17 with dissolve
    mc "(...This guy's pissing me off.)"
    mc "Fine. What do you want?"
    scene c2m20 with dissolve
    gln "Do you like making people repeat themselves? I said license and registration."
    scene c2m19 with dissolve
    mc "...Fine. Fucking take it. I got nothing to hide."
    scene c2m16 with sdissolve
    gln "Good.{w} Now hold still... I'll be right back."
    scene c2m15 with sdissolve
    mc "(Seriously. I haven't done a single thing wrong. I'm so confused right now.)"
    scene c2m14 with dissolve
    mc "(Glenn Cole... my neighbor; police officer...)"
    scene c2m13 with sdissolve
    mc "(...and apparently: giant fucking prick.)"
    pause
    mc "(Imagine getting stopped by a guy in a Beetle.)"
    pause
    mc "(If this dickhead doesn't hurry up I'll be late to my meeting with Natalie.)"
    mc "..."
    scene c2m12 with fadehold
    gln "Here. Get this out of my sight."
    scene c2m10 with dissolve
    mc "I'm sorry... do you have a problem with me or something, officer?"
    scene c2m9 with qdissolve
    gln "Peh. A problem...?"
    gln "That's an understatement."
    gln "Maybe I'm just sick of looking at your fancy fucking sports car and intrusively large house. That cross your mind?"
    scene c2m10 with qdissolve
    mc "I mean... you could move."
    scene c2m8 with qdissolve
    gln "This is my neighborhood, shithead. If anyone's moving, it's going to be you."
    scene c2m7 with qdissolve
    mc "Jesus! Calm the fuck down. All this over some fucking car? Are you insane?"
    scene c2m6 with qdissolve
    $ renpy.pause (.7, hard=True)
    scene c2m9 with qdissolve
    gln "Don't forget the house. That house used to belong to my grandfather, you know."
    gln "Now, what's the deal with these little girls running around your place?{w} Wearing frilly bikinis and lounging about... they can't be a day older than [age]. Where'd you find them? Some Russian whorehouse?"
    scene c2m10 with qdissolve
    mc "That's none of your fucking business, and watch your mouth!"
    scene c2m8 with dissolve
    gln "I just made it my business."
    scene c2m7 with qdissolve
    mc "...Fine. They're my [dau]s, okay? Do you always {i}nose{/i} your way into other people's personal affairs?"
    scene c2m9 with qdissolve
    gln "Heh. Your [dau]s, huh? We've been neighbors for how long?{w} What made you think I'd believe that?"
    gln "They don't even have the same hair and eye colors.{w} It's genetically impossible."
    scene c2m6 with qdissolve
    mc "(Alright... this guy's really pushing my fucking buttons!{w} Also- no it isn't.)"
    mc "(And as much as I'd like to shatter every tooth in this asshole's skull... I'm ninety-nine percent sure he could take me. We can't all be professional fighters...)"
    mc "(...fuck! If only I knew Taekwondo or something.)"
    scene c2m10 with qdissolve
    mc "...I don't give a fuck what you believe. Can I go now?"
    scene c2m9 with qdissolve
    gln "Uh-huh."
    scene c2m10 with qdissolve
    $ renpy.pause (1, hard=True)
    scene c2m5 with dissolve
    gln "Be seeing you again soon, pal. Real soon."
    scene c2m4 with dissolve
    mc "Yeah, have a great fucking week!"
    scene c2m15 with sdissolve
    mc "Thinking I might stop by the station later and file a report."
    gln "Try it."
    stop music fadeout 12.0
    scene c2m3 with sdissolve
    $ renpy.pause (1.5, hard=True)
    play sound "audio/sounds/peelout.ogg"
    scene c2m2 with sdissolve
    $ renpy.pause (1, hard=True)
    scene c2m1 with sdissolve
    $ renpy.pause (1, hard=True)
    mc "Holy shit, what a fucking cocksucker!"
    pause
    scene c2m27 with dissolve
    mc "(This isn't over, pig. You fucked with the wrong person.{w} This means war.)"
    scene black with sdissolve
    mc "(Fucking prick. What the hell did I do to him? He acts like I took a shit in his cereal.)"
    $ renpy.pause (2, hard=True)

label natalie_coffee:

    scene c2n31 with sdissolve
    mc "(Ah... there she is. Thank God she didn't bail. I'm sure she's thrilled that I'm a few minutes late to our meetup.)"
    scene c2n30 with dissolve
    mc "Ms. Koval?"
    play music "<loop 0.0>audio/northern_lights.ogg" fadein 14.0
    scene c2n29 with dissolve
    mc "I'm so sorry I'm late—I ended up getting stopped by..."
    scene c2n28 with dissolve
    nat "This is normal."
    scene c2n27 with sdissolve
    nat "I've dealt with worse things than, how do you say... tardiness."
    scene c2n26 with sdissolve
    mc "(There's that thick Russian... Ukrainian? There's that thick and otherwise terrifying accent again. I wonder when she moved to the states?)"
    mc "Right. Well, I'll save the excuses then. Have you been here long?"
    scene c2n25 with dissolve
    nat "Not long enough to be interested in small talk. You must have had a reason to insist on this... continued relationship, no?"
    scene c2n19 with dissolve
    mc "A few reasons... can I order you something first?"
    scene c2n18 with dissolve
    nat "I already purchased us coffees."
    scene c2n24 with sdissolve
    pause
    scene c2n23 with dissolve
    nat "Oh, right on time. Unlike someone, yes?"
    scene c2n22 with sdissolve
    mc "(Her presence and confidence is rather commanding... something I'm not very used to seeing from women.)"
    scene c2n21 with dissolve
    mc "Ah... yeah... sorry again for my...{w} tardiness.{w} So, I guess I'll get straight to the point."
    scene c2n19 with dissolve
    mc "Is it alright if I call you Natalie?"
    scene c2n18 with qdissolve
    nat "Fine."
    scene c2n19 with qdissolve
    mc "Well firstly... thank you for agreeing to see me again. I don't know what I was thinking... it {i}was{/i} bold to ask this of you..."
    scene c2n18 with qdissolve
    nat "So why did you?"
    scene c2n19 with qdissolve
    mc "Well..."
    mc "As I said... there's a few reasons. For starters... I feel like I owe you some kind of explanation. That said..."
    mc "The truth is I... I don't really have one."
    mc "As I'm sure you're aware, I suffered some pretty serious injuries on the night of the accident... and rightfully so, I should add I'm not looking for sympathy..."
    mc "Among them, a serious head injury. When I woke up at the hospital I had no..."
    scene c2n16 with qdissolve
    mc "I didn't have any...{w} I-I'm sorry, Natalie. The truth is I don't remember anything from that night... the night of the accident. I hardly remember attending high school, for that matter."
    mc "So even if I wanted to know what happened that night, or what possessed me to drive while under the influence..."
    mc "Everything's a blur."
    scene c2n14 with qdissolve
    nat "..."
    mc "T-That's not the only reason I asked you here today. What happened to me was nothing compared to what I did to you. I... I wanted you to know that I've felt this way from the very moment I learned of the details from that night."
    scene c2n15 with qdissolve
    mc "My doctor... he didn't want to tell me at first. Wanted to give me some time. I spent days in that hospital bed just... pitying myself, I guess."
    mc "But yeah... as I told you before, all of that self-pity quickly faded when I learned what I'd done. How could I pity myself when someone else had it so much worse? Because of me?"
    mc "Hell of a way to wake up..."
    mc "Listen, I'm going to spare you more sob stories. And I know what this might seem like... asking you here. You probably think I'm just trying to find a way to clear my conscience."
    mc "But I'm not. I'll never stop feeling guilty for what I did to your family. Nothing I say or do can change that."
    mc "I asked you here today because I owe you my life. And if there's even the smallest chance that I can give you some form of closure... or even compensation... I have to try. Do you understand?"
    scene c2n14 with qdissolve
    nat "..."
    scene c2n13 with qdissolve
    nat "You have a good heart. Your parents raised you... decent."
    scene c2n12 with qdissolve
    mc "T-Thank you. Yeah... from what I can actually remember... they were wonderful."
    scene c2n11 with qdissolve
    nat "Were?"
    scene c2n10 with qdissolve
    mc ".{w}.{w}.were, yes.{w} Before I woke up from my coma... th-they passed. I guess they were pretty heartbroken about what happened... worried themselves sick. Literally."
    mc "To be honest I never have time to think about it much. Or maybe I'm just avoiding it."
    scene c2n9 with qdissolve
    nat "I am sorry. About your parents. Tragedy seems to have... lasting consequences."
    scene c2n8 with qdissolve
    nat "My husband places the blame on me for what happened. Says it's my fault... for letting our son take my car."
    scene c2n14 with qdissolve
    mc "...that's terrible. I'm sorry... for both of you..."
    scene c2n7 with qdissolve
    nat "Sorry for him? No, don't feel sorry for my husband. He's a prick! Cares more about his stupid \"legacy\" than his own son. He didn't shed a single tear."
    scene c2n11 with qdissolve
    nat "You, on the other hand. You're a nice boy. My husband could learn something from you."
    scene c2n12 with qdissolve
    mc "(I mean, she's older than me but I wouldn't say \"boy...\")"
    scene c2n6 with qdissolve
    mc "(Is she... no.{w} Surely, she's not flirting with me. She's just trying to be friendly.)"
    scene c2n11 with qdissolve
    nat "So you want to make it up to me, do you? Well, I'll think of something. You're right, you're in my debt. And you're lucky you have a good heart. It makes me feel... less angry...{w} at myself. For not killing you."
    scene c2n6 with qdissolve
    mc "(That's... strangely reassuring.)"
    scene c2n5 with qdissolve
    nat "Tomorrow. I'll need you for something. I will give you the details when you show up. If you truly want to make the effort... you'll cancel your late afternoon plans. Okay?"
    scene c2n12 with qdissolve
    mc "(Looks like I'll be taking that time off from work after all. Might as well take a few days off.)"
    mc "Alright then. Consider it done."
    scene c2n11 with qdissolve
    nat "I'm staying at the Windhymen, the hotel across the street.{w} Room sixty-nine on the fourth floor. You'll pass two hallways and it's the door at the very end. You cannot miss it. Text me the times you'll be free tomorrow and I'll let you know when I'm ready, okay?"
    scene c2n12 with qdissolve
    mc "(Wait... \"hymen...\" sixty-nine... four... two...)"
    stop music fadeout 09.0
    scene c2n4 with sdissolve
    na "She leaves you before you even have time to finish your immature thoughts."
    mc "Thank you, Natalie. I'll see you tomorrow."
    scene c2n3 with sdissolve
    nat "I'm counting on it, [mc]."
    scene c2n2 with sdissolve
    mc "(That... went much better than expected.)"
    mc "(She's surprisingly pleasant...{w} when not trying to kill you, anyway.)"
    mc "(What could she possibly need my help with? It doesn't sound very urgent, whatever it is. This is going to drive me mad, now. I hate cliffhangers.)"
    scene black with sdissolve
    play music "<loop 0.0>audio/intentions.ogg" fadein 12.0
    $ renpy.pause (2.5, hard=True)

label predate_ali:

    scene c2o37 with sdissolve
    mc "{size=+3}[ali]? You ready to go?!{/size}"
    ali "{size=-1}{i}Coming!{/i}{/size}"
    pause
    scene c2o36 with fadehold
    liv "No fair! Why do you get to go out with [mcd]? I knew you were the favorite."
    scene c2o35 with qdissolve
    mad "Right? Kiss ass!"
    scene c2o34 with sdissolve
    ali "Shut up, [mnick]! It wasn't {i}my{/i} idea!"
    scene c2o33 with qdissolve
    mad "{i}Teacher's pet.{/i}"
    scene c2o32 with sdissolve
    ali "Bluu."
    scene c2o31 with sdissolve
    liv "We're just playing, [anick]. Have fun! We'll just have to stay behind and lounge carelessly at the pool today!"
    scene c2o30 with dissolve
    mad "No way. I have to watch the Cooterfruit stream this afternoon. But maybe if we go in a little later..."
    scene c2o29 with sdissolve
    liv "Ooo. I didn't know Cooter was streaming today! Sucks to be you, [ali]."
    scene c2o28 with sdissolve
    ali "I'm not sad! I'll just watch her VOD later. Besides... I'm the one going out with {i}[mcd]{/i} today!"
    scene c2o27 with sdissolve
    mad "{i}*Groan*{/i}"
    scene c2o26 with fadehold
    mc "There you are!"
    scene c2o25 with qdissolve
    ali "[mcd]!!!"
    scene c2o24 with sdissolve
    pause
    scene c2o25 with sdissolve
    ali "Ready! So where are you taking me?"
    scene c2o26 with qdissolve
    mc "Nope! Not spoiling the secret just yet. Besides, we still need to stop and get you that outfit I promised. Let's go!"
    scene c2o25 with qdissolve
    ali "Yes, [mcd]!"
    scene black with sdissolve
    $ renpy.pause (2, hard=True)
    scene c2o23 with sdissolve
    mc "Hey... before we go in, I wanted to ask you something quickly."
    scene c2o22 with sdissolve
    ali "Yes, [mcd]?"
    scene c2o20 with dissolve
    mc "Well... you know you don't have to call me [mcd], right? I mean... you can if you want to of course. It just seems a little... sudden."
    scene c2o21 with qdissolve
    ali "I know... but for some reason it just feels... natural! I kind of like saying it... if that makes sense. I don't mind if you don't."
    scene c2o18 with qdissolve
    ali "Then again, I could call you something else if you'd like?"
    scene c2o19 with qdissolve
    mc "(I'm sure eventually we'll have plenty of petnames for each other, but in the meantime... am I okay with her calling me [mcd]?)"

    if tbed == True:
        $ amc_nick = renpy.input("What should she call you? (Leave this blank if you want her to use \"[mcd].\")")
        if amc_nick == "":
            $ amc_nick="Daddy"
        scene c2o18 with qdissolve
        ali "Understood, [amc]! I'm glad you're okay with me calling you that!"
    else:
        $ amc_nick = renpy.input("What should she call you? (Leave this blank if you want her to keep using your first name.)", length=12).strip() or player_name
        scene c2o18 with qdissolve
        ali "Understood, [amc]! I like the sound of that more."


    scene c2o19 with qdissolve
    mc "Heh, alright. Come on, let's go in."
    stop music fadeout 07.0
    scene black with sdissolve
    na "You spend what feels like an enormous amount of time awkwardly browsing women's clothing."
    scene c2o17 with sdissolve
    mc "(Hm... that was a surprising find. I wonder if what I just bought will help [mnick] with her \"problem?\")"
    play sound "audio/sounds/textmessage.ogg"
    mc "(Oh, a text from [ali].)"
    scene c2o16 with sdissolve
    "{i}[amc], cum quick! I need your help in here!{/i}"
    mc "(That sounds... strangely urgent. Guess I better hurry.)"
    pause (1)
    mc "(Haha. \"Cum.\")"
    scene black with sdissolve
    $ renpy.pause (2, hard=True)
    scene c2ox3 with sdissolve
    mc "[anick]? You in there?"
    ali "In here! It's urgent!"
    mc "Alright then. I'm coming in!"
    scene black with fadehold
    mc "[anick], is everything alright?"
    $ renpy.pause (1, hard=True)
    play music "<loop 0.0>audio/three_kinds_of_suns.ogg" fadein 12.0
    show allie at allie_transform
    ali "Not really!"
    scene c2o14 with sdissolve
    mc "(Holy shit!)"
    ali "I really need your opinion on something."
    scene c2o13 with qdissolve
    mc "[ali]..."
    mc "You do realize you're topless, right?"
    scene c2o14 with qdissolve
    ali "Huh?"
    ali "Of course I do. I'm not stupid."
    scene c2o13 with qdissolve
    mc "(JUST LOOK AT THE KNEE... LOOK ANYWHERE BUT HER...)"
    scene c2o12 with dissolve
    ali "That's what I need your help with. I can't decide if I want this dress, or this one. Oh! And I also found a cute pair of panties... but I'm having trouble choosing between blue or red!{w} What do you think, [amc]?"
    menu:
        "B-Blue?":
            $ bblue = True
            mc "Bu-Blue?"
            pass
        "R-Red?":

            $ rred = True
            mc "R-Red?"
            pass
        "K-Knee?":

            mc "K-Knee?"
            pass
        "T-Tits?":

            mc "T-Tits?"
            pass

    scene c2o14 with dissolve
    ali "Of course! Good choice!"
    scene c2o11 with sdissolve
    scene c2o11 with vpunch
    $ renpy.pause (.7, hard=True)
    mc "[ali]!"
    scene c2o10 with sdissolve
    $ renpy.pause (.5, hard=True)
    ali "Oh, be patient! I'm almost done.{w} Just need to grab this..."
    if bblue == True:
        scene c2o9 with sdissolve
    elif rred == True:
        scene c2o8 with sdissolve
    else:
        scene c2o8 with sdissolve

    pause
    mc "(My head is spinning. Just need to close my eyes for a minute.)"
    scene black with sdissolve
    mc "(Think of something else, just think of something else...{w} something... cute?)"
    scene c2ox1 with sdissolve
    mc "(Ah yes. Puppies. This will have to work for now.)"
    mc "{i}*Sigh*{/i}"
    scene black with sdissolve
    mc "(May God help me...)"
    mc "(And have mercy on my soul...)"
    ali "{i}And now for the dress! You're going to love it, [amc]!{/i}"
    mc "(Because I'm going to absolutely...)"
    menu:
        "Take an Oath of Celibacy":
            $ pure +=1
            mc "(I'm a good person. I'm a perfect angel. Nothing will happen. I can resist temptation. Yes I can{w}'t.)"
            mc "(...this is your [dau] you're thinking about, pal.)"
            mc "(...not sure if that hurts or helps, to be honest.)"
            if tbed == True:
                mc "(I wonder which religion allows for incest?)"
        "Ravish Her":

            $ lust +=1
            mc "(Tear this girls clothes off and completely ravish her, one of these days. I'm not sure how much longer I can handle her flailing her tits about.)"
            mc "(Forget her tits, actually. As nice as they are... she has a perfect ass...)"
            mc "(...this is your [dau] you're thinking about, pal.)"
            mc "(...not sure if that hurts or helps, to be honest.)"
        "Lose Control":

            $ dark +=1
            mc "(I'm going to lose control and do something I'll seriously regret. I don't want to hurt anyone.)"
            mc "(...or do I? That's yet to be seen, I guess.)"
            mc "(I can't deny that my [dau] is attractive. Very fucking attractive.)"
            mc "(I could see myself taking advantage of this. Who wouldn't?)"

    mc "(I t-think she got distracted or something. Was there any point to calling me in here at all?)"
    mc "(...aside from giving me a raging hardon?)"
    mc "(This girl... she might be the sexiest fucking thing I've ever laid eyes on.)"
    ali "[amc]?"
    scene c2o7 with sdissolve
    mc "Oh... sorry. Y-Yes?"
    scene c2o5 with qdissolve
    ali "Did you hear me? I said, \"What do you think? Does it look good?\""
    scene c2o6 with qdissolve
    mc "...de-describe \"it.\""
    mc "(A little hard to hear when all your blood has left your head and moved to your cock.)"
    scene c2o3 with qdissolve
    ali "Hehe! The outfit, you silly moose! Isn't that why you're here?"
    scene c2o7 with qdissolve
    mc "You mean \"goose,\" right? Silly goose?"
    scene c2o4 with qdissolve
    ali "Huh?"
    scene c2o6 with qdissolve
    mc "Nothing, nothing..."
    mc "You look beautiful, honey!"
    scene c2o2 with dissolve
    ali "So can I get this one?"
    scene c2o1 with qdissolve
    mc "Honestly? You can get anything you want, sweetheart. We have to get going or we'll be late, though. Keep the dress on... you'll want to be wearing it where we're going- trust me! We'll pay for everything on the way out."
    scene c2o4 with dissolve
    ali "W-Wait... you said I could've had anything?{w} W-We can shop here again when we have more time... right?"
    stop music fadeout 08.0
    scene c2o6 with qdissolve
    mc "Haha. Of course. Just not today! We got bigger plans. Come on- let's do this."
    scene c2o3 with qdissolve
    ali "Yes [amc]!"
    scene black with sdissolve
    $ renpy.pause (2, hard=True)

label alisurprise_date:

    mc "You spend some time driving to your next destination."
    play music "<loop 0.0>audio/key_to_your_heart.ogg" fadein 08.0
    scene c2p41 with sdissolve
    mc "(Here we are... get ready for the surprise of a lifetime, [anick].)"
    scene c2p42 with qdissolve
    ali "I'm confused! What is this place? This doesn't look like a restaurant... or a theater... or an amusement park... is this where you're taking me?"
    scene c2p41 with qdissolve
    mc "You'll see. It's even better than all of those things!"
    scene c2p42 with qdissolve
    ali "Seriously?! Okay, I'm getting excited now..."
    scene c2p40 with dissolve
    mc "(Good that we got here a little early. I see the place is still pretty empty. Welp, I better get set up.)"
    scene c2p39 with fadehold
    ali "Um... [amc]?"
    scene c2p38 with qdissolve
    mc "Yes honey?"
    scene c2p39 with qdissolve
    ali "...is this... is this what I think it is?"
    scene c2p37 with qdissolve
    mc "I don't know, what do you think it is exactly?"
    scene c2p39 with qdissolve
    ali "Well... based on the way this place is set up..."
    ali "And based on all that stuff you carried inside..."
    ali "Are those... are your cameras inside those bags?"
    scene c2p37 with qdissolve
    mc "My camera, my laptop, among some other things. Why?"
    ali "(Hm...)"
    scene c2p36 with dissolve
    ali "Wait! This is a photo studio, isn't it? Is this where you take pictures of the models?"
    scene c2p35 with qdissolve
    mc "Haha. You got it. That's exactly it."
    scene c2p36 with qdissolve
    ali "Oh my God, awesome! Are you going to let me model for you? Is that why you let me pick out that outfit?"
    scene c2p35 with qdissolve
    mc "You can model for a few shots if you'd like. Of course! But that's not the real reason we're here today..."
    stop music fadeout 07.0
    scene c2p36 with qdissolve
    ali "It's not? Then why are we..."
    scene c2p34 with qdissolve
    ali "..."
    scene c2p33 with sdissolve
    mc "(Uh oh... here she comes.)"
    mc "Miss Mae, nice to finally meet you! I'm looking forward to our shoot today."
    scene c2p32 with dissolve
    ali "M-Mae? Tiffany... Mae?"
    scene c2p31 with dissolve
    tif "Good to meet you finally, [mc]! And who's this beautiful young lady? Are you one of the other models, dear?"
    scene c2p30 with dissolve
    $ renpy.pause (1.2, hard=True)
    scene c2p25 with dissolve
    play music "audio/bohemian_beach.ogg" fadein 08.0
    ali "Oh my God... what are you doing here?!"
    scene c2p28 with sdissolve
    tif "Haha. I've come to work! I heard [mc] is one of the best photographers in the industry, so I'm sure it's going to be a productive day."
    tif "And what's your name?"
    scene c2p25 with dissolve
    ali "I'm [ali]... and I'm your biggest fan. Seriously. It's so nice to meet you!"
    scene c2p27 with dissolve
    tif "So I've heard! I also heard you're interested in modeling. Is that true?"
    scene c2p23 with dissolve
    ali "Y-Yes. I mean... I'm only [age] so I don't have any experience or anything, but..."
    scene c2p25 with dissolve
    ali "I know everything there is to know about the industry! In and out! And I take great selfies!"
    scene c2p27 with dissolve
    tif "Well, you look absolutely beautiful in that dress! And to be honest... I think you have the perfect look for a young model."
    scene c2p26 with dissolve
    tif "Yes... I'm certain of it... you'll make a wonderful model someday."
    scene c2p23 with dissolve
    ali "Do you really think so?"
    scene c2p21 with dissolve
    tif "Sure I do! Tell you what... why don't you come with me for a while? I still need to see my makeup artist and get dressed."
    scene c2p22 with sdissolve
    mc "That would be perfect actually, as I still need to get set up here. So I'll see you girls in a few?"
    scene c2p21 with dissolve
    tif "Sounds good! Come on, [ali]!"
    scene black with sdissolve
    na "You setup your equipment while the girls do their thing."
    scene c2p20 with sdissolve
    ali "[mcd]! I got to talk to Tiffany for ages! She even told her makeup artist to tend to me! And on top of that... she wants to pose for a few photos together!"
    scene c2p19 with qdissolve
    mc "That sounds awesome, [anick]. So how does it feel to meet your idol?"
    scene c2p18 with qdissolve
    ali "It's incredible. She's so much nicer than I could've imagined. I even got to meet her agent. He's just like one of those guys in the movies!"
    ali "Thank you, [mcd]! This is one of the nicest things anyone's ever done for me..."
    scene c2p19 with dissolve
    mc "You don't have to thank me, [ali]. You're my [dau]. I'd do anything for you."
    scene c2p18 with dissolve
    ali "So will you be the one taking our pictures, then? I guess that makes me a little less nervous..."
    scene c2p19 with dissolve
    mc "It's normal to be nervous... but don't worry. Everything will go just fine. And besides... this is just a practice run. Let's see how you feel after today, and then maybe we can try and get you a real gig, okay?"
    scene c2p18 with dissolve
    ali "But um... what should I do?"
    scene c2p19 with dissolve
    mc "Well... if you're unsure, just do what Tiffany does, okay? And besides, I'm sure she'll coach you along as we go. We can take this at our own pace."
    stop music fadeout 08.0
    mc "And since you'll be posing together after the main photoshoot... you'll have a chance to see her in action!"
    scene c2p18 with dissolve
    ali "Right! This is so cool. I can't believe this is happening! This is like a dream come true."
    scene c2p16 with dissolve
    tif "Hey again [mc]. I think we're ready. How about you?"
    scene c2p15 with dissolve
    mc "I'm ready when you are. You look great, by the way!"
    scene c2p14 with dissolve
    tif "Thank you. Pay close attention, [ali], okay?"
    scene c2p15 with dissolve
    ali "Yes, of course."
    play music "<loop 0.0>audio/dragonfly.ogg" fadein 10.0
    scene black with sdissolve
    $ renpy.pause (2, hard=True)

label photoshoot1:

    scene c2p13 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c2p13 with flash
    mc "There we go. Just like that."
    pause
    scene c2p12 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c2p12 with flash
    mc "(Damn! She has somewhat of a unique look, there's definitely more attractive girls out there... but her confidence and grace is what really sells her. Looks aren't everything in the industry.)"
    mc "You're doing great. Keep it up!"
    pause
    scene c2p8 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c2p8 with flash
    mc "Oof! Yes, that's it. That was perfect!"
    pause
    scene c2p10 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c2p10 with flash
    mc "Just a couple more and we're done. These are coming out wonderfully."
    pause
    scene c2p7 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c2p7 with flash
    mc "Wow..."
    pause
    scene c2p9 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c2p9 with flash
    mc "(One more should do it.)"
    pause
    scene c2p6 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c2p6 with flash
    mc "Nice job, beautiful."
    pause
    scene c2q21 with fadehold
    mc "And that's a wrap. You did amazing, Tiffany. That was absolutely perfect!"
    scene c2q19 with sdissolve
    tif "Hey, I can't take all the credit! You really coached me along there, [mc]. I can see why they say you're the best in the business.{w} So, [ali], are you ready to take a few photos together?"
    scene c2q18 with qdissolve
    ali "Y-Yes, Miss Mae. I'm ready!"
    scene c2q19 with qdissolve
    tif "Hehe. Just Tiffany is fine, dear. Come along now, let's do this."
    scene c2q17 with dissolve
    tif "{i}*Whispering*{/i} Just follow my lead, okay sweetie? Let's give your [car] an amazing show!"
    scene black with sdissolve
    $ renpy.pause (1.2, hard=True)
    scene c2p1 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c2p1 with flash
    mc "(Holy shit! My [dau] is a natural!)"
    pause
    scene c2p5 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c2p5 with flash
    mc "(As good as Tiffany is... I'm having a harder time keeping my eyes off of [ali]. She has a certain charm and elegance when posing for the camera.)"
    pause
    scene c2p4 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c2p4 with flash
    mc "Looking amazing, girls!"
    pause
    scene c2p3 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c2p3 with flash
    mc "(Cute!)"
    pause
    scene c2p2 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c2p2 with flash
    pause
    scene c2q21 with fadehold
    mc "Wow... you girls did an amazing job. [ali], you're a natural!"
    scene c2q20 with qdissolve
    ali "Oh come on, I wasn't that good..."
    scene c2q19 with qdissolve
    tif "You were hon. In fact, I'm confident that we'll get to work together professionally someday."
    scene c2q18 with qdissolve
    ali "That means so much to me. Thank you so much! You're my hero, Tiffany!"
    scene c2q17 with dissolve
    tif "{i}*Whispering*{/i} Make sure you thank your [mcd] too, okay? He clearly cares deeply for you."
    tif "And hopefully we'll get to see each other again soon. In a more casual environment, of course!"
    stop music fadeout 09.0
    scene c2q16 with dissolve
    ali "I love you so much, Tiffany."
    scene c2q15 with qdissolve
    tif "Hehe. I love you too, hon."
    scene c2q17 with dissolve
    mc "Come on [ali], let's pack up and head out."
    scene black with sdissolve
    pause (2)
    scene c2q13 with sdissolve
    ali "I had a lot of fun today. This was seriously the best surprise!"
    scene c2q14 with qdissolve
    mc "I'm glad. I certainly don't like seeing you sad like you were this morning."
    scene c2q13 with qdissolve
    ali "Well consider me un-saddened! I can't wait to tell my sisters about this! They're going to be sooo jealous!"
    scene c2q11 with dissolve
    tif "Hey, [mc]? Can I speak to you for a moment?"
    scene c2q12 with qdissolve
    mc "Yes, of course."
    scene c2q14 with sdissolve
    mc "I'll meet you in the car, okay? Go ahead and get the A/C running if you need to."
    scene c2q13 with qdissolve
    ali "Okay, [amc]."
    scene black with sdissolve
    pause (1.2)
    scene c2q5 with sdissolve
    tif "Thanks for coming!"
    tif "Your [dau] is a beautiful girl, [mc]. And she's incredibly charming. It was very nice of you to bring her here today.{w} I wanted to apologize for my agent's reluctance. He can be... a bit of a stiff sometimes."
    scene c2q6 with qdissolve
    mc "No, don't sweat it. This is a professional environment, after all. It was very kind of you to take her under your wing and show her the ropes. I'm sure your fans throw themselves at you all the time."
    scene c2q5 with qdissolve
    tif "They do, this is true. And I try to entertain them as much as possible. But of course, this isn't always an option. I'm just glad I could make that girl's day."
    tif "That said... I'm saddened that we didn't get to speak more. Perhaps we could meet up outside of work sometime?"
    scene c2q6 with qdissolve
    mc "(Did Tiffany Mae just ask me on a date?)"
    scene c2q5 with qdissolve
    tif "After all... it would be a great excuse to see [ali] again. And maybe I can help her get into the industry... if she's ready for that?"
    scene c2q1 with qdissolve
    mc "(Might be a date, might just be a great opportunity to help [ali]. Besides, I don't think she's romantically interested in me or anything... yet. We've barely spoken, after all.)"
    menu:
        "I'd Like That":
            $ tif_romance = True
            $ lust +=1
            mc "I'd love that. How could I say no to such a proposition? Here, put your number in my phone and I'll text you so we can setup the time and place."
            scene c2q4 with qdissolve
            tif "Great! Sounds like fun. I can hardly wait."
            scene c2q1 with qdissolve
            pause (1)
        "Not a Good Idea":

            mc "I don't know, Miss Mae. It's probably not a good idea. I typically don't fraternize with models or clients..."
            scene c2q3 with qdissolve
            tif "O-Oh! Right. I understand. That's a shame though."
            scene c2q4 with qdissolve
            tif "Maybe we'll still see each other around, then?"
            scene c2q1 with qdissolve
            mc "Sure, yes. That would be nice!"

    scene c2q4 with qdissolve
    tif "Well, thanks again for doing a wonderful job today, [mc]. I can't wait to see the finished product. My agent will be contacting you shortly, okay?"
    scene c2q1 with qdissolve
    mc "Sounds good, [tif]. Have a nice day."
    scene c2q4 with qdissolve
    tif "You too!"
    scene c2q1 with qdissolve
    tif "(Hmm. What a handsome, charming guy. And his [dau] is... quite beautiful too.)"

label aftershoot:

    scene black with sdissolve
    play music "<loop 0.0>audio/timeless.ogg" fadein 07.0
    $ renpy.pause (2, hard=True)
    scene c2r16 with sdissolve
    pause
    scene c2r15 with sdissolve
    mc "([anick] seems distracted... probably still in shock from the evening's events, so I have some time to gather my thoughts.)"
    mc "(That whole thing with Tiffany... that went extremely well didn't it?)"
    mc "(Seeing [ali] happy... that really warmed my heart. All things considered; she's been really good to me. She was the first one to call me [mcd], actually... so I guess I shouldn't be surprised.)"
    mc "(Tiffany... she's beautiful. It was pretty brazen of her to just ask me out like that. Though I'm sure she was just being friendly. While it's possible she's interested in me romantically, it's also possible that she's just trying to get closer to my [dau].)"
    mc "(Not that I can blame her. [ali] is the type of girl to just... brighten up the room.)"
    scene c2r17 with dissolve
    mc "(Still no dreams of Gracie... I'd really like to see her again. Ask her some questions. But I guess it's normal. I've been sleeping like a log.)"
    mc "(While for the most part things seem to be going well, I'm really having a hard time handling this situation with [mad]. I just don't know what I'm doing wrong.)"
    mc "(I'm also having a hard time looking at the girls as my own [dau]s. No matter how hard I try or how much progress I think I've made... it seems like around every corner I see [ali]'s boobs. I could probably make a photorealistic painting of them by now.)"
    mc "(That shit that happened back at the dressing room. That was crazy!)"
    scene c2o11 with fadehold
    mc "(Her ass reminds me of two freshly inflated balloons...)"
    mc "(I'll never get that picture out of my mind. Assuming I'd even want to.)"
    scene c2r14 with fadehold
    mc "(Ah. Home sweet home. I wonder what the girls are up to?)"
    scene black with sdissolve
    pause (2)
    scene c2r13 with sdissolve
    ali "Thank you for everything, [mcd]. If you need me, I'll be in my room!"
    scene c2r12 with dissolve
    mc "No problem!"
    scene c2r11 with sdissolve
    mc "(And she's gone. That was quick. She must need to... blog about this... or write in her diary or something.)"
    mc "(Isn't that what girls do?)"
    mc "(Wow... this place is a mess. [mad] you little slob...)"
    mc "(I seriously might consider hiring a maid. I've always wanted to but never really had a reason. Now however... with four people living in the house I just might.)"
    if harsh_rsp == True:
        mc "(Hm... I distinctly remember asking [mnick] to clean the place. I guess she decided not to do what I asked her to.)"
        mc "(And she made a nice mess while I was gone.)"
        mc "(There will be consequences for that, [mad].)"

    mc "(Time to see what the girls are up to. They did say something about populating the pool...)"
    scene c2r10 with fadehold
    mc "(Oh, there's [liv]! No sign of the unruly sister. Wonder what she's doing out here by herself?)"
    scene c2r9 with sdissolve
    mc "Hey, [oli_nick]! Everything alright?"
    scene c2r8 with qdissolve
    liv "[mcd]! Yes, everything's fine, I guess. Just thinking."
    scene c2r9 with qdissolve
    mc "Glad to hear it. Where's the sister? Decided not to join you at the pool?"
    scene c2r7 with qdissolve
    liv "Well, she was out here with me earlier..."
    scene c2r8 with qdissolve
    liv "Actually, could you do me a favor? The water is just so warm so I... I wanted to take another quick dip in the pool. But..."
    scene c2r6 with qdissolve
    mc "Of course. What do you need me to do?"
    scene c2r8 with qdissolve
    liv "Well... [mad] and I got in another fight just before you..."
    scene c2r7 with qdissolve
    liv "I said some pretty mean stuff.{w} I... didn't mean to..."
    scene c2r6 with qdissolve
    liv "{i}*Sigh*{/i}"
    scene c2r8 with qdissolve
    liv "Could you... check on her [mcd]?"
    scene c2r9 with qdissolve
    mc "I would be happy to do that for you. When I'm done how about I come join you out here? I could use the fresh air."
    scene c2r8 with qdissolve
    liv "T-That would be awesome, [mcd]. Thank you."
    scene c2r6 with qdissolve
    mc "Okay. Be right back."
    stop music fadeout 05.0
    scene black with sdissolve
    pause (1.2)
    scene c2r5 with sdissolve
    if harsh_rsp == True and tbed == True and (dark >= 5 or mad_dark >=3):
        jump mad_punished
    else:
        pass

    menu:
        mc "(Here goes nothing. I'll be surprised if she doesn't immediately bite my head off and physically throw me out of her room.)"
        "Knock":
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)

    pause
    mad "{i}Go away, [liv]! I don't want to talk to you!{/i}"
    mc "Actually [mad], it's me. Can I come in?"
    pause
    mc "I just want to quickly talk to you. I won't keep you long. I promise."
    pause
    mad "{i}Hmph!{/i}"
    pause
    mc "(I'm fighting an uphill battle here. If I don't start taking more drastic measures; really pushing myself... I'll never get through to her.)"
    mc "[mad], I'm coming in!"
    scene c2r4 with sdissolve
    play music "<loop 0.0>audio/figments_of_color.ogg" fadein 12.0
    pause
    mc "Hey, [mad]. Sorry to barge in like this. I just... wanted to check on you."
    mc "Are you okay?"
    $ renpy.pause (.8, hard=True)
    mad "{i}*Sniff*{/i}{w} Not really..."
    mc "{i}*Sigh*{/i} Let me pull up a chair..."
    scene c2r3 with fade
    pause
    mc "[mad], I know you're going through a rough time right now..."
    mc "But, even though we haven't gotten along too well since you arrived, I hate seeing you like this. If there's something I can do to make you happy, I'll figure it out. No matter what happens, I'll find a way."
    mc "In the meantime, I wanted you to know I'm here for you if you ever need to talk to me about anything."
    mc "I mean... maybe I'm not your favorite person in the world... and I'm trying to understand and come to terms with that..."
    mc "But sometimes it's nice to... talk to someone older.{w} Or even just someone with a different perspective, know what I mean?"
    mad "..."
    mc "Now that I know you're okay, I'm going to leave you alone, but..."
    mc "You'll get through this, [mnick]. And you won't have to do it alone.{w} Mark my words, no matter what it takes... I'll fix this. Things will get better."
    mc "So maybe... hopefully... that's something you can look forward to, then. Being happy again."
    mc "I promise that day will come soon. It's just around the corner."
    pause
    mc "Thanks for hearing me out, sweetheart."
    scene c2r0 with sdissolve
    $ renpy.pause (1, hard=True)
    scene c2r2 with dissolve
    mad "H-Hey [mc]?"
    scene c2r1 with sdissolve
    mc "...Y-Yeah?"
    scene c2r0 with dissolve
    pause
    scene c2r2 with sdissolve
    mad "Thank you..."
    scene c2r1 with sdissolve
    mc "{i}*Smile*{/i} You're welcome, [mad]."
    stop music fadeout 05.0
    scene black with sdissolve
    $ renpy.pause (3, hard=True)
    jump oliviaromance

label mad_punished:

    mc "(Alright. I need to make an important choice...)"
    mc "(On one hand, [liv] asked me to check on [mad], who's probably pretty upset right about now...)"
    mc "(On the other hand she's been pissing me off... this isn't the first time she's outright disobeyed me.{w} I specifically asked her to clean the house. Instead, she left a giant mess.)"
    mc "(It might be pretty cruel to punish her now though, given the circumstances. The question is... do I care? What should I do?)"
    scene c2r5 with pinkflash
    scene c2r5 with pinkflash
    scene c2r5 with pinkflash
    menu:
        mc "(This decision could change the course of my relationship with [mnick]. It could also make her hate me. I better choose carefully.)"
        "Punish Her":
            $ maddark = True
            $ dark +=3
            $ mad_dark +=3
        "Forgive Her":

            jump mad_punished_alt

    mc "(Nope. Don't care. It's time to teach my spoiled brat of a [dau] a lesson she'll remember for the rest of her life.)"
    menu:
        mc "(I'll just quickly knock to let her know I'm coming.)"
        "Knock":
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)

    play music "<loop 8.0>audio/no_8_requiem.ogg" fadein 05.0
    mc "[mad], it's me. I'm coming in."
    scene c2r4 with sdissolve
    pause (1)
    mad "W-What's the point of knocking if you're just going to come in without my permission?"
    mc "You'll get over it. Besides... your sister wanted me to check on you."
    mc "So... you okay?"
    mad "{i}*Sniff*{/i} Not really..."
    pause (1)
    mc "I see.{w}.{w}."
    mc "That's too bad."
    mc "Thing is... I specifically remember telling you to do something while I was gone. Remember that? Or did you just decide you'd rather be defiant?"
    $ renpy.pause (1, hard=True)
    scene c2u10 with sdissolve
    mad "Oh my God... seriously?! Are you really bringing {i}that{/i} up right now?"
    mad "G-Go! Get out of my room!"
    scene c2u9 with sdissolve
    pause (1.2)
    mc "Heh...{w} You don't make the rules around here, young lady. I do!"
    scene c2u11 with dissolve
    pause (1)
    na "You quietly shut the door behind you."
    pause (1.2)
    scene c2u7 with dissolve
    mad "F-Fine! What are you go-going to do? G-Ground me? Yell at me?"
    if mad_dark >=3:
        mad "Tell me I'm stupid again?!"
    mad "Do it! I don't care anymore!"
    scene c2u8 with sdissolve
    mc "Heh... you don't care, huh?"
    mc "Stand up."
    pause (1)
    scene c2v6 with sdissolve
    mad "{i}*Sniff*{/i}"
    mc "You know... I was going to go easy on you. After all, your sister asked me to talk to you. But you refused to do what I asked."
    mc "You're fighting with your sisters, you're leaving messes around the house... you broke my vase..."
    scene c2v7 with dissolve
    mad "That wasn't..."
    scene c2v6 with sdissolve
    mc "And now you have the nerve to tell me to get out of your room?"
    scene c2v5 with sdissolve
    mc "I get it, you're going through a rough time..."
    mc "Problem is you're only [age]... yet acting like you're the boss around here."
    mc "We can't have that. Can we?"
    mc "There's an easy way to sort out spoiled, bratty [age]-year-old girls like you."
    mc "Turn around."
    scene c2v2 with dissolve
    mad "W-What?!"
    scene c2v4 with dissolve
    mc "Turn around and bend over! I'm not going to ask again!"
    scene c2v1 with dissolve
    mad "{i}*Sobs*{/i} Y-You can't make me!"
    scene c2v6 with sdissolve
    mc "You're fucking pissing me off! Turn around. Now!"
    scene c2v1 with sdissolve
    mad "F-Fine!"
    scene c2v4 with dissolve
    mc "Hurry up."
    pause (1.2)
    scene c2u2 with fade
    mc "Good girl. Now we're getting somewhere."
    mad "W-What are y-you planning to..."
    mc "Quiet."
    mc "(She has an incredible body. Her plump ass will certainly cushion the blows.)"
    mc "(I know this is harsh but this needs to be done. If we can sort out her attitude, maybe I can finally get some peace around here.)"
    mc "(And having her obey me; ensuring she understands that she's {i}mine{/i} now... that will certainly make for some interesting situations. This is only the beginning. She has no idea what's in store for her here.)"
    scene c2u1 with fade
    image mad_spank = Movie(play="videos/Chapter 2/mad_spank.webm", loop=False)
    mc "(She should've...)"
    play sound "audio/sounds/smack.ogg"
    show mad_spank with dissolve
    pause (.17)
    scene c2u1 with dissolve
    mc "(Listened.)"
    mad "{size=+5}O-Ouch!{/size} N-Not so hard!"
    mc "(Heh... it's cute that she thinks {i}this{/i} is hard.)"
    play sound "audio/sounds/smack.ogg"
    show mad_spank with dissolve
    pause (.17)
    scene c2u1 with dissolve
    mc "(This is literally just a warmup; to gauge her reaction and ensure she won't freak out.)"
    if tbed == True:
        mc "(Though, I {i}am{/i} her [car]. I think I'm legally allowed to punish her in this state. So there's simply nothing she could do... even if she wanted to.)"
    play sound "audio/sounds/smack.ogg"
    show mad_spank with dissolve
    pause (.17)
    scene c2u1 with dissolve
    mc "Did I say you could talk, little lady?"
    mad "I-I'm... n-not... l-little..."
    play sound "audio/sounds/smack.ogg"
    show mad_spank with dissolve
    pause (.17)
    scene c2u1 with dissolve
    mc "Watch your mouth! I said no fucking talking!"
    mad "{i}*Crying*{/i}"
    scene c2u2 with fade
    mc "Crying already? Those were love-taps."

    menu:
        mc "(She's still not fully cooperating... but I think she gets the idea. Should I end it here, or take her punishment even further?)"
        "Keep Spanking Her":
            $ dark +=1
            $ mad_dark +=1
        "End Punishment":

            mc "You know what... I actually do feel a little sorry for you. I think I'll let you off the hook a little early.{w} Stand up young lady."
            stop music fadeout 07.0
            scene c2v4 with fade
            mc "Don't make the mistake of assuming I'll go easy on you next time.{w} If I have to, I {i}will{/i} take your punishment even further. Do you understand?"
            scene c2v1 with dissolve
            mad "Y-Yes, [mc]..."
            scene c2v4 with dissolve
            mc "[mc]...?"
            scene c2v1 with dissolve
            mad "S-Sorry. Yes, [mcd]..."
            scene c2v4 with dissolve
            mc "Good. Now... I think I'll go spend some time with your sister out by the pool. Go to bed, young lady."
            scene black with sdissolve
            pause (.6)
            mad "{i}*Sobs*{/i}"
            scene c2r5 with sdissolve
            mc "(I hope I made the right decision. I honestly don't know if I did, but she's still young and seems to be completely void of discipline. Now she'll know who the authority figure is around here.)"
            scene black with sdissolve
            $ renpy.pause (3, hard=True)
            jump oliviaromance

    mc "And since you're not cooperating.{w}.{w}. pull down your bottoms.{w} Right now... before I lose my patience."
    mad "W-What?! You can't! I won't d-do this..."
    mc "I'm your [car] and you don't have a choice in this matter. You're only [age]-years-old."
    mc "Now pull them down! Do it before I get angry and do it for you."
    mad "I c-can't... {size=-3}you-you'll see my butt!{/size}"
    mc "Alright then, I'm going to count to three."
    mad "{i}*Crying*{/i}"
    pause
    mc "One..."
    mad "P-Please!"
    pause
    mc "Two..."
    pause
    mad "{i}*Sniff*{/i}"
    scene c2w6 with fadehold
    $ renpy.pause (1)
    mc "(Holy shit!)"
    mc "(Atta' girl...{w} damn!)"
    mc "(What a perfect fucking ass.)"
    mc "Good girl.{w} Now hold still, this is going to take a while.{w} You might want to grab the sheets. I'm not going to go easy on you."
    mad "[mc], y-you can't! Please don't..."
    mc "Still using first names? No, that won't do; that's no way to address your [mcd], [mad]."
    mad "O-Okay... I-I'm sorry [mcd]. P-Please j-just..."
    mc "Quiet!"
    mad "{i}*Sniff*{/i} W-Why are you doing this... I was just"
    play sound "audio/sounds/smack_hard.ogg"
    scene c2w1 with qdissolve
    scene c2w1 with vpunch
    $ renpy.pause (.6, hard=True)
    scene c2w6 with dissolve
    mad "{size=+3}Ouch!{/size}"
    mc "I said no talking!"
    play sound "audio/sounds/smack_hard.ogg"
    scene c2w1 with qdissolve
    scene c2w1 with vpunch
    $ renpy.pause (.6, hard=True)
    scene c2w5 with dissolve
    mad "{i}*Sobs*{/i}"
    pause
    menu:
        mc "(Oh yeah... she's really feeling the sting now. Her little ass is starting to turn red. Should I keep going?)"
        "Spank Again":
            $ dark +=1
            $ mad_dark +=1
            play sound "audio/sounds/smack_hard.ogg"
            scene c2w1 with qdissolve
            scene c2w1 with vpunch
            $ renpy.pause (.6, hard=True)
            scene c2w4 with dissolve
        "Stop":

            jump end_punished

    mad "{size=+5}Aah!{/size}"
    mc "Hurts, doesn't it? You should've thought about that before you caused all this trouble."
    mad "{i}*Sniff*{/i}"
    menu:
        mc "(I can see my handprint forming. She'll be sore for a while now.)"
        "Spank Again":
            $ dark +=1
            $ mad_dark +=1
            play sound "audio/sounds/smack_hard.ogg"
            scene c2w1 with qdissolve
            scene c2w1 with vpunch
            $ renpy.pause (.6, hard=True)
            scene c2w4 with dissolve
        "Stop":

            jump end_punished

    mad "{i}Nnn!{/i}"
    mad "{i}*Crying*{/i}"
    pause
    menu:
        mc "(She's in a lot of pain. Good. She finally understands who she's been fucking with. I can probably stop...)"
        "Harder":
            $ dark +=1
            $ mad_dark +=1
            play sound "audio/sounds/smack_hard1.ogg"
            scene c2w1 with xdissolve
            scene c2w1 with hpunch
            $ renpy.pause (.6, hard=True)
            scene c2w3 with dissolve
        "Stop":

            jump end_punished

    mad "{i}*Squeal!*{/i}"
    mad "P-Ple-ase... da-daddy... it h-hurts..."
    pause
    menu:
        mc "(Her voice is shaky and it sounds like she's snotting up. Going further would be cruel, but...)"
        "Harder":
            $ dark +=1
            $ mad_dark +=1
            play sound "audio/sounds/smack_xhard.ogg"
            scene c2w1 with xdissolve
            scene c2w1 with hpunch
            $ renpy.pause (.6, hard=True)
            scene c2w2 with dissolve
        "Stop":

            jump end_punished

    mad "{i}*Screams*{/i}"
    mad "Ugggh..."
    pause
    menu:
        mc "Are you starting to understand now? Are you done acting like a spoiled little bitch?"
        "Finish Up":
            $ dark +=1
            $ mad_dark +=1
            $ mad_scared +=1
        "She's Had Enough":

            mad "P-Please, [mcd], I'm b-begging y-you! I-I've learned m-my lesson!"
            mc "Good. I hope so. Because this was just a warmup."
            jump end_punished

    mad "D-Da-[mcd]..."
    pause
    play sound "audio/sounds/smack_xhard.ogg"
    scene c2w1 with xdissolve
    scene c2w1 with vpunch
    $ renpy.pause (.6, hard=True)
    scene c2w2 with dissolve
    mc "{size=+3}Don't...{/size}"
    pause (1)
    play sound "audio/sounds/smack_xhard.ogg"
    scene c2w1 with xdissolve
    scene c2w1 with vpunch
    $ renpy.pause (.6, hard=True)
    scene c2w2 with dissolve
    mc "{size=+3}Fucking...{/size}"
    pause (1)
    play sound "audio/sounds/smack_xhard.ogg"
    scene c2w1 with xdissolve
    scene c2w1 with vpunch
    $ renpy.pause (.6, hard=True)
    scene c2w2 with dissolve
    mc "{size=+3}Piss...{/size}"
    pause (1)
    play sound "audio/sounds/smack_xhard.ogg"
    scene c2w1 with xdissolve
    scene c2w1 with vpunch
    $ renpy.pause (.6, hard=True)
    scene c2w2 with dissolve
    mc "{size=+3}Me...{/size}"
    pause (1)
    play sound "audio/sounds/smack_xhard.ogg"
    scene c2w1 with xdissolve
    scene c2w1 with vpunch
    $ renpy.pause (.6, hard=True)
    scene c2w2 with dissolve
    mc "{size=+3}Off!{/size}"
    mad "{size=+10}Hnnnaa!{/size}"
    mad "P-Pl-lease, [mcd], I-I'm b-begging y-you! I-I've learned m-my lesson! I-It hurts! Please..."
    na "She lets loose a high pitched cry... her voice is clearly shaking and she's started hyperventilating."
    mc "Good. I hope so. Because this was just a warmup.{w} Remember what you learned today, [mad]."
    mc "(I'd be surprised if [ali] didn't hear all of this from her room. I need to stop.)"
    pause (.6)
    mc "(Shit... she's trembling, squeaking, and crying her little eyes out.{w} I...{w} I think I got carried away.)"
    jump end_punished

label mad_punished_alt:

    mc "(No... I can't. Doing that to her when she's already feeling down...)"
    mc "(It would just feel... wrong.)"
    mc "(Welp. I better knock and check on her like [liv] asked.)"
    mc "(After the interactions we've had I'll be surprised if she doesn't immediately bite my head off and physically throw me out of her room.)"
    menu:
        "Knock":
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)

    pause
    mad "{i}Go away, [liv]! I don't want to talk to you!{/i}"
    mc "Actually [mad], it's me. Can I come in?"
    pause
    mc "I just want to quickly talk to you. I won't keep you long. I promise."
    pause
    mad "{i}Hmph!{/i}"
    pause
    mc "(I'm fighting an uphill battle here. If I don't start taking more drastic measures; really pushing myself... I'll never get through to her.)"
    mc "[mad], I'm coming in!"
    scene c2r4 with sdissolve
    play music "<loop 0.0>audio/figments_of_color.ogg" fadein 12.0
    pause
    mc "Hey, [mad]. Sorry to barge in like this. I just... wanted to check on you."
    mc "Are you okay?"
    $ renpy.pause (.8, hard=True)
    mad "{i}*Sniff*{/i}{w} Not really..."
    mc "{i}*Sigh*{/i} Let me pull up a chair..."
    scene c2r3 with fade
    pause
    mc "[mad], I know you're going through a rough time right now..."
    mc "But, even though we haven't gotten along too well since you arrived, I hate seeing you like this. If there's something I can do to make you happy, I'll figure it out. No matter what happens, I'll find a way."
    mc "In the meantime, I wanted you to know I'm here for you if you ever need to talk to me about anything."
    mc "I mean... maybe I'm not your favorite person in the world... and I'm trying to understand and come to terms with that..."
    mc "But sometimes it's nice to... talk to someone older.{w} Or even just someone with a different perspective, know what I mean?"
    mad "..."
    mc "Now that I know you're okay, I'm going to leave you alone, but..."
    mc "You'll get through this, [mnick]. And you won't have to do it alone.{w} Mark my words, no matter what it takes... I'll fix this. Things will get better."
    mc "So maybe... hopefully... that's something you can look forward to, then. Being happy again."
    mc "I promise that day will come soon. It's just around the corner."
    pause
    mc "Thanks for hearing me out, sweetheart."
    scene c2r0 with sdissolve
    $ renpy.pause (1, hard=True)
    scene c2r2 with dissolve
    mad "H-Hey [mc]?"
    scene c2r1 with sdissolve
    mc "...Y-Yeah?"
    scene c2r0 with dissolve
    pause
    scene c2r2 with sdissolve
    mad "Thank you..."
    scene c2r1 with sdissolve
    mc "{i}*Smile*{/i} You're welcome, [mad]."
    stop music fadeout 05.0
    scene black with sdissolve
    $ renpy.pause (3, hard=True)
    jump oliviaromance

label end_punished:

    mc "I could keep going... and I probably should. You've been a naughty girl, [mad]..."
    mc "But I think I've gotten the message across."
    mc "Do we have an understanding now?"
    mad "Y-Yes, [mcd]."
    mad "{i}*Sniff*{/i}"
    mad "P-Please let me go... it..."
    mad "I-It hu-hurts..."
    mc "Good. And I'll hurt you again if you don't start behaving yourself. You'll treat me with respect. I won't have an unruly [age]-year-old thinking she's in charge around here."
    mc "I'll be leaving now. But remember what happened tonight and I think we'll come to an understanding."
    mc "Do we understand each other?"
    mad "Yes, [mcd]."
    mc "Good. Start behaving yourself and acting your age, or there will be consequences. Now... I think I'll go spend some time with your sister out by the pool."
    mc "Go to bed, young lady. And when you wake up in the morning, I expect you to clean up your mess before breakfast."
    stop music fadeout 06.0
    mad "{i}*Sobs*{/i}"
    scene black with sdissolve
    $ renpy.pause (1.2, hard=True)
    mc "(I... hope I made the right decision. I honestly don't know if I did... but she's still young and seems to be completely void of discipline in her life. Now she'll know who the authority figure around here is.)"
    scene c2r5 with sdissolve
    mc "(One thing's for sure... she'll remember this well. She probably won't be sitting straight for a while...)"
    scene black with sdissolve
    $ renpy.pause (3, hard=True)

label oliviaromance:

    scene c2s34 with sdissolve
    liv "Hey, [mc]! There you are. Come sit with me!"
    scene c2s33 with qdissolve
    mc "Here I am! Alright, I'm coming I'm coming."
    play music "<loop 0.0>audio/passing_time.mp3" fadein 08.0
    scene c2s32 with fadehold
    mc "Ahh... it always feels great to relax out here after a long day."
    scene c2s31 with qdissolve
    liv "I can understand why! Your pool... the sky... this entire area is just so beautiful."
    scene c2s30 with qdissolve
    liv "So um... did you talk to [mad]?"
    scene c2s29 with qdissolve
    mc "I did... yeah. She's..."
    scene c2s28 with qdissolve
    if maddark == True:
        mc "I think I straightened her out."
    else:
        mc "She's going to be okay."
    scene c2s27 with qdissolve
    liv "G-Good..."
    scene c2s26 with qdissolve
    mc "Is everything okay between you two?"
    scene c2s25 with qdissolve
    liv "It will be. It's just..."
    scene c2s27 with qdissolve
    liv "I asked her if she wanted to go do something. To get our minds off of everything..."
    liv "And she seemed so keen on the idea! That is, until I...{w} um..."
    scene c2s29 with qdissolve
    mc "Until you mentioned bringing me..."
    scene c2s30 with qdissolve
    liv "Y-Yeah."
    scene c2s27 with qdissolve
    liv "We... never used to fight like this. Ever. Until mom..."
    scene c2s28 with qdissolve
    liv "..."
    liv "{i}*Sigh*{/i}"
    scene c2s27 with qdissolve
    liv "Seeing my sisters... how distraught they were... I-"
    liv "I just want us all to look forward, you know? I'm just as sad as she is about mom... but... thanks to you we're exactly where she'd want us to be."
    scene c2s25 with qdissolve
    if tbed == True:
        liv "And we're not alone like I once feared we would be.{w} We're... a family."
    else:
        liv "And we're not alone like I once feared we would be.{w} We... have you."
    scene c2s26 with qdissolve
    mc "I'm glad you look at it that way because I do too. It's taking me some adjustment to get used to this all... I mean I've been living on my own for so many years now..."
    mc "But before you girls showed up...{w} my life... this place..."
    mc "It just felt so... empty."
    scene c2s28 with qdissolve
    mc "Then you three came along, and sort of flipped everything upside down..."
    mc "I was confused at first."
    mc "Then I was nervous... like the weight of the world had just been placed on my shoulders."
    mc "But now..."
    scene c2s32 with qdissolve
    mc "I just feel so... full suddenly. Like every day has something new to offer. And a deep sense of purpose..."
    mc "But I also feel a sense of responsibility. You girls..."
    mc "You're my responsibility."
    mc "And no matter what happens... I'll do everything I can to make you three happy."
    scene c2s24 with qdissolve
    liv "Hearing you say that makes me feel really nice."
    liv "Thank you for being so good to me and my sisters."
    scene c2s23 with qdissolve
    liv "Can I... come closer?"
    scene c2s22 with sdissolve
    liv "D-Do you mind?"
    scene c2s21 with qdissolve
    mc "(Does she want to sit in my lap? I... I guess that's normal, right? She is my [dau], after all...)"
    mc "Y-Yeah. Of course."
    scene c2s20 with sdissolve
    liv "Hm..."
    scene c2s19 with qdissolve
    liv "Sorry... I'm not trying to be weird or anything but..."
    liv "I just need to get a good look at you."
    scene c2s17 with qdissolve
    liv "(Hm...)"
    scene c2s14 with qdissolve
    liv "(He's definitely my [car]...)"
    scene c2sx1 with qdissolve
    mc "(She's looking at me so strangely now. But I think she's just curious.)"
    mc "(Girls are like that. They tend to appreciate the subtle things.)"
    if tbed == True:
        mc "(Like our shared appearance.)"

    scene c2s14 with qdissolve
    mc "[liv], I spoke to [anick] about the same thing earlier..."
    mc "You know you don't have to call me [mcd], right?"
    mc "You could call me something else if you wanted..."
    scene c2s13 with qdissolve
    liv "N-No, it's okay! I really like it! It just feels natural. It should feel natural, right? But I could call you something else if that would make you more comfortable."
    scene c2sx1 with qdissolve
    if tbed == True:
        $ omc_nick = renpy.input("What should she call you? (Leave this blank if you want her to use \"[mcd].\")")
        if omc_nick == "":
            $ omc_nick="Daddy"
        mc "[omc] sounds good to me, sweetheart."
    else:
        $ omc_nick = renpy.input("What should she call you? (Leave this blank if you want her to keep using your first name.)", length=12).strip() or player_name

    scene c2s13 with qdissolve
    liv "I like it too."
    liv "Calling you [omc] makes me feel closer to you."
    liv "And I like the idea of being close with you, [omc]."
    scene c2sx1 with qdissolve
    mc "I'm glad you feel that way. I was nervous... you know? I didn't want you girls to hate me... I'm glad your mom took the time to explain what happened so you didn't think I was just some lowlife who abandons his own [dau]s."
    mc "(I guess I should consider myself lucky that they're still only [age]. A couple more years from now and things could've played out very differently.)"
    scene c2s16 with qdissolve
    liv "I really can see what she saw in you."
    scene c2s15 with qdissolve
    mc "Y-You mean... Gracie?"
    scene c2s13 with qdissolve
    liv "Yeah. I haven't known you for very long, but she obviously had a good bull-crap radar. You don't seem like one of those weird guys who only thinks about himself. You seem genuine, and honest..."
    liv "One of the good ones..."
    scene c2sx1 with qdissolve
    mc "Well damn! Now you're just flattering me. What brought this on?"
    scene c2s10 with qdissolve
    liv "..."
    mc "[liv]?"
    liv "Hm..."
    mc "You seem distracted. Are you comparing and contrasting again?"
    scene c2s12 with qdissolve
    liv "S-Something like that. I definitely...{w} see it..."
    if tbed == True:
        liv "W-We clearly have your nose..."
        scene c2s11 with qdissolve
        liv "A-And your...{w} lips..."
    else:
        liv "Just inspecting your nose..."
        scene c2s11 with qdissolve
        liv "A-And your...{w} lips..."

    scene c2s10 with qdissolve
    $ renpy.pause (1.2, hard=True)
    scene c2s9 with dissolve
    $ renpy.pause (1, hard=True)
    scene c2s7 with dissolve
    scene c2s7 with vpunch
    pause (.6)
    mc "(Holy shit... my [dau] just kissed me.{w} And for some reason I'm...)"
    scene c2s7 with pinkflash
    scene c2s7 with pinkflash
    stop music fadeout 10.0
    menu:
        mc "(???)"
        "Kiss Her Back":
            $ cc0 = True
            $ lust +=3
            $ liv_lust +=3
            mc "(I'm not sure what's gotten into me, but...)"
            mc "(I can't... help myself.)"
            liv "Mm!"
            liv "(Yes... kiss me [omc]...)"
            scene c2s6 with qdissolve
            liv "Mmm..."
            scene c2s8 with dissolve
            $ renpy.pause (1.2, hard=True)
            scene c2s5 with qdissolve
            scene c2s5 with vpunch
            liv "Oh my God, [omc]. I'm so sorry."
            scene c2s4 with qdissolve
            mc "N-No it's alright, I wanted..."
        "Stop Her":

            $ liv_pure +=3
            $ pure +=3
            scene c2s4 with dissolve
            mc "[liv], hold on... we can't..."
            scene c2s5 with vpunch
            liv "Oh my God, [omc]. I'm so sorry."
            scene c2s4 with qdissolve
            liv "(Does this mean that he doesn't...)"
        "Grope Her":

            $ liv_dark +=3
            $ dark +=3
            $ cc1 = True
            mc "(I'm not sure what's gotten into me, but...)"
            liv "Mm!"
            liv "(Y-Yes... kiss me [omc]...)"
            scene c2s6 with qdissolve
            liv "Mmm..."
            mc "(May as well slide my hands down and grab this sweet little ass of hers.)"
            liv "(W-Wait, is he...)"
            scene c2s4 with dissolve
            $ renpy.pause (1, hard=True)
            scene c2s5 with vpunch
            liv "Oh my God! Did you just..?"

    scene c2s3 with dissolve
    liv "Oh God. What have I done?"
    liv "Sorry!!!"
    pause (2)
    scene c2s2 with dissolve
    mc "[liv], wait!"
    pause
    scene c2s1 with sdissolve
    pause
    mc "(.{w}.{w}.Shit.)"
    play music [ "audio/a_call_is_upon_us.ogg", "audio/the_crows_did_it.ogg", "audio/western_spaghetti.ogg" ] fadein 10.0 fadeout 07.0
    mc "(Did that just happen..?)"
    if cc0 == True:
        mc "(I just fucked up big time, didn't I? Was kissing her back a mistake?)"
    elif cc1 == True:
        mc "(Well... sliding my fingers into her asscrack didn't seem to go over well. I fucked up, didn't I?)"
    else:
        mc "(Oh no... did she flip out like that because I... because I stopped her? Does she think I was rejecting her?)"

    mc "(Well...)"
    mc "(This is going to be an awkward breakfast...)"
    scene black with ssdissolve
    $ renpy.pause (1, hard=True)
    mc "(Where do we go from here?)"
    $ renpy.pause (2, hard=True)
    scene c2t3 with ssdissolve
    pause
    scene c2t4 with ssdissolve
    pause
    scene c2t2 with sdissolve
    $ renpy.pause (2, hard=True)
    scene c2t1 with sdissolve
    gln "I got you, cunt."
    scene c2t2 with sdissolve
    $ renpy.pause (2, hard=True)
    scene black with sdissolve
    $ ch2_complete = True
    jump end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
