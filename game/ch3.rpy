





default mc_lust = False
default mc_resist = False
default mc_careless = False
default panty_torture = False
default panty_relief = False
default ali_hug = False
default ali_kiss = False
default ali_grope = False
default ali_incelgram = False
default ali_touched = False
default liv_protect = False
default liv_uncertain = False
default liv_apologize = False
default liv_blame = False
default liv_feelings = False
default liv_deception = False
default liv_truthful = False
default liv_seduced = False
default liv_kissed = False
default disciplinarian = False
default sadist = False
default cruel_prank = False
default brk_blowjob = False
default brk_secondchance = False
default brk_upset = False
default van_judgement = False
default van_rejection = False

label chapterthree:

    stop music fadeout 04.0
    scene black with sdissolve
    $ renpy.pause (7, hard=True)
    play music "<loop 0.0>audio/glacier.ogg" fadein 12.0
    scene chapter3 with sdissolve
    $ renpy.pause (5, hard=True)
    scene black with sdissolve
    $ renpy.pause (.7, hard=True)
    mc ".{w}.{w}."
    uk "[mc]? Time to get up already."
    pause (1)
    mc "(Huh? Who's bothering me?)"
    pause (1)
    scene c3a23 with sdissolve
    mc "(Wait...)"
    mc "(It's her! How did she get here?!)"
    scene c3a22 with fadehold
    mc "Gracie!"
    scene c3a20 with sdissolve
    pause (.5)
    grc "In the flesh!"
    scene c3a19 with qdissolve
    pause (1.2)
    mc "(...Fuck. It's just another dream.)"
    scene c3a21 with qdissolve
    pause (.5)
    scene c3a18 with sdissolve
    grc "Is everything okay? You seem down."
    scene c3a17 with qdissolve
    mc "It's..."
    mc "(For a minute I thought that...)"
    mc "(I thought this was real. That she was alive.)"
    mc "(This is the first time I'm seeing her since the girls arrived. This is surreal.)"
    mc "It's nothing. Don't worry. I just missed you is all."
    scene c3a11 with dissolve
    grc "Hm... alright. But you better not be hiding something!"
    scene c3a10 with qdissolve
    mc "(I shouldn't get my hopes up... I... have to remember this is just a dream.)"
    mc "(But there's no doubt about it, looking at her now.)"
    mc "(Unless my brain is just playing tricks on me...)"
    scene c3a13 with dissolve
    mc "(Those big eyes... her nose, her complexion...)"
    mc "(It's her. She's their mother. Despite her similarity to the girls... she has her own distinct look. And even though I'm having a lucid dream... her face is so detailed and vivid.)"
    mc "(It's almost like I'm traveling to some other dimension... rather than dreaming.)"
    mc "(She's... the spitting image of [liv]...)"
    mc "(Oh God... [liv]. What have I done?)"
    scene c3a14 with qdissolve
    grc "Alright, the cat's out of the bag!"
    scene c3a13 with qdissolve
    pause (.7)
    mc "Wait, w-what?"
    scene c3a16 with dissolve
    grc "You heard me! You're being weird. Now tell me what is on your mind before I get angry. You're visibly concerned about something and you're avoiding telling me. So... out with it!"
    scene c3a15 with qdissolve
    mc "Heh..."
    scene c3a16 with qdissolve
    grc "What's so funny, [mc]?"
    scene c3a15 with qdissolve
    mc "You've always had this strange ability to cheer me up... you know that?"
    scene c3a16 with qdissolve
    grc "Well, I don't like seeing you sad. You know how I am!"
    scene c3a15 with qdissolve
    mc "That's true..."
    mc "(Dream or not... it's true. Every time I see her, it's like my worries melt away.)"
    mc "(And it may be just a dream...)"
    mc "(But I could live in these moments.)"
    mc "(It's funny... I never had trouble speaking to her before... but now that I know what I know... I'm at a loss for words.)"
    scene c3a16 with qdissolve
    grc "Are you going to tell me what's bothering you? Or would you prefer to just keep me in suspense?"
    scene c3a15 with qdissolve
    mc "Oh, right."
    mc "Sorry... I know I'm being weird, but... there's so much I need to say..."
    pause (.7)
    menu:
        mc "(Where should I start?)"
        "Everyone Misses You":
            $ pure +=1
            mc "It's just that... everyone misses you. So, so much. And while this'll sound weird, so do I."
        "Wish You Were Here":

            $ lust +=1
            mc "It's just that... I really wish you could be here now. With everything going on..."
            mc "And I know I'm not the only one."
        "This Is Ridiculous":

            $ dark +=1
            mc "I don't know what to say. This is ridiculous. How am I supposed to take our conversations seriously when I know this is all just a dream? Is it really even you... or are you just a figment of my imagination?"
            mc "I just... I wish this were real. I wish {i}you{/i} were real."
            grc "I am real! Don't be mean."
            mc "*Sigh*"

    scene c3a7 with dissolve
    $ renpy.pause (.8, hard=True)
    scene c3a6 with dissolve
    grc "I... think I understand."
    grc "But even though you can't see me, I'm always with you, love."
    grc "And my girls. I'll never leave their side. I promise. Okay?"
    scene c3a5 with qdissolve
    mc "Gracie, about that..."
    mc "I... think I did something horrible tonight."
    mc "[liv] and I were talking and I...{w} I think we both got a little caught up in the moment."

    if cc0 == True:
        mc "And then I... I might have kissed her.{w} Well, technically she kissed me..."
        mc "But I didn't stop her. I just... let it happen. The truth is... I didn't want her to stop."
    elif cc1 == True:
        mc "She kissed me. And instead of stopping her..."
        mc "Well, let's just say I got a little carried away. I have no idea what I was thinking. I just couldn't help myself."
    else:
        mc "She... kissed me. And even though I stopped her, for a moment I hesitated. The truth is, I'm not even sure if I wanted her to stop."

    mc "And now I can't help but think I've completely ruined everything. We were getting along so well, too."
    mc "There's so many thoughts running through my head."
    mc "What if she's never able to look at me the same way again? What if she thinks I took advantage of her? I'm supposed to be her [car], not a creepy bastard who preys on his own [dau]. How could I let this happen?"
    mc "Gracie... I'm so sorry. It was all so sudden, I-I didn't mean to. I promise you that it wasn't intentional. I'm..."
    scene c3a6 with qdissolve
    grc "[mc], hold on."
    grc "Before you say anything else, I need you to answer me."
    grc "Do you have bad intentions with my daughters?"
    scene c3a5 with qdissolve
    mc "No. I want nothing more than to see them happy."
    scene c3a6 with qdissolve
    grc "Do you care about them?"
    scene c3a5 with qdissolve
    mc "Deeply. We haven't known each other long... but I felt a connection with them almost right away, and it only grows stronger with each passing day."
    scene c3a6 with qdissolve
    grc "Do you promise to keep them safe?"
    scene c3a5 with qdissolve
    mc "Yes... I would never let anything happen to them."
    scene c3a7 with dissolve
    grc "Hm..."
    scene c3a6 with dissolve
    grc "Well... then..."
    grc "I trust you, [mc]. I don't know why. I've never known why I feel this way about you."
    scene c3a9 with dissolve
    grc "I guess it's true what they say... that... that everyone has a soulmate."
    grc "The type of person who, for no apparent reason, you just feel an instant connection with."
    grc "And that night... when you approached me at prom..."
    grc "I immediately felt that connection. With you."
    scene c3a8 with qdissolve
    mc "Approached you at..."
    pause (.5)
    mc "Prom?"

    scene black with ssdissolve
    $ renpy.pause (1.5, hard=True)
    scene c3a0 with ssdissolve
    "{i}.{w=1}.{w=1}.{/i}"
    mc "{i}(Is this...{w=1.6} a memory?){/i}"
    show screen system_msg3 with dissolve
    $ renpy.pause (3, hard=True)
    hide screen system_msg3 with dissolve
    scene black with sdissolve
    $ renpy.pause (2, hard=True)

    scene c3a6 with sdissolve
    grc "I don't know why tonight happened... or what went on between you and [onick]..."
    grc "But whatever it is, I'm not worried. Because it's you."
    grc "[liv] is a lot like me, in a way. She always wanted to be just like her mother."
    grc "So maybe there's something there... something... visceral."
    scene c3a5 with qdissolve
    mc "Are you saying you think she's attracted to me?"
    scene c3a6 with qdissolve
    grc "I don't know. But if she is..."
    grc "I think it's important that you find out. For the sake of your relationship with her."
    grc "Growing up my parents never paid much attention to me."
    grc "They provided for me, but they never showed me any affection. Never. For as long as I can remember, I was just kind of there. Lingering in their shadow."
    grc "But in that brief time that we spent together..."
    grc "You showed me something that I could only describe as... love."
    grc "I'm not telling you that you should make a move on my daughter... just..."
    grc "Explore your feelings... honestly. See where it goes. It's never a good idea to repress these things, after all. And whatever becomes of it, I know you'll do right by them."
    grc "Most importantly, don't let it drive a wedge between you."
    stop music fadeout 12.0
    if tbed == True:
        grc "You're finally able to bond with your [dau]s. Our [dau]s. Don't let it go to waste, okay?"

    grc "To be honest, I wouldn't be surprised if [onick] made the first move. She's always been a leader... never the type of person to follow others. She's a lot braver than I was."
    scene c3a7 with dissolve
    grc "(Speaking of repressed feelings...)"
    grc "(Why am I getting horny thinking about this?)"
    scene c3a8 with dissolve
    play music "<loop 0.0>audio/sixteen_twenty_five.ogg" fadein 15.0
    grc "(Oh, God. Am I wet? What's wrong with me!)"
    mc "What did you just say?!"
    scene c3a6 with dissolve
    grc "Wait... you heard that?!"
    scene c3a7 with dissolve
    mc "Uh... I think so. I mean, I didn't see your lips moving..."
    scene c3a9 with dissolve
    grc "Shit! I'm so embarrassed."
    scene c3a6 with dissolve
    grc "Wait. How were you able to hear what I'm thinking?"
    scene c3a5 with qdissolve
    mc "Welp..."
    mc "This is my dream, after all."
    scene c3a9 with dissolve
    grc "Hm... so where does this dream lead, handsome? I am feeling very... aroused at the moment. Perhaps we could have some fun together?"
    scene c3a8 with qdissolve
    mc "(Heh... so she wants me to fuck her again. I guess it's not that... surprising. I mean... it always seems to lead to this.)"
    mc "(I'm pretty sure I hold the world record for wet dreams. At one point I had to wash my sheets several times in a single week.)"
    mc "I think I can help you with your arousal."
    grc "Hm..."
    scene c3a4 with sdissolve
    grc "No... not this time. This time it's going to be all about you..."
    grc "My king."
    scene c3a2 with sdissolve
    mc "(Whoa. Where did her clothes go?!)"
    mc "(Benefits of the dream world, I guess.)"
    mc "(No matter how many times I see her like this, I never get tired of staring at that body.)"

label gracie_sex_scene:

    image graciefinger = Movie(play="videos/Chapter 3/gracie_fg.webm")
    image graciehj = Movie(play="videos/Chapter 3/gracie_hj.webm")
    image graciebj = Movie(play="videos/Chapter 3/gracie_bj.webm")
    mc "(So much for talking things through. Now, the only thing on my mind is how much blood is flowing through my cock.)"
    show graciefinger with sfade
    pause
    grc "Do you want to use my mouth again, my handsome king?"
    mc "I'm thinking I'll use your throat this time."
    grc "Mm... good. I think my throat would like that..."
    grc "I'll do anything for you. I exist to serve you, [mc]."
    grc "I love this big ole thing."
    show graciehj with sdissolve
    hide graciefinger
    mc "It loves you too. Now put it in your mouth again before I go mad."
    pause
    show graciebj with sdissolve
    hide graciehj
    grc "Mmlhm..."
    mc "God... you're so wet that I can {i}hear{/i} your fingers moving in and out of you. I hope you're not going to cum yet."
    mc "Not until I pound you... again and again while you scream my name. I want to feel you cum while your little pussy is wrapped tightly around me."
    grc "Mmmm..."
    mc "Would you like that?"
    grc "Mhmm!"
    mc "F-Fuck me... I'm going to cum."
    stop music fadeout 06.0
    mc "(Shit... she's not letting up like I thought she would. She's taking me deeper now. I think she wants me to cum down her throat.)"
    menu:
        mc "(Shit, I don't think I can hold out any longer...)"
        "Cum":
            mc "Ffffuuck!"

    scene black with ssdissolve
    $ renpy.pause (2, hard=True)
    na "As you spill your seed into her throat, the world suddenly fades to black."
    mc "(Fuck! Are you serious?! Not now! Noo!)"
    scene c3b19 with sdissolve
    $ renpy.pause (.5, hard=True)
    mc "{i}*Sigh*{/i}"
    mc "(At least I had enough time to cum.)"
    mc "(Literally... my briefs are soaked.{w} Good lord am I pitching a tent though.)"
    mc "(Wait... what's--)"

label wakeup1:

    scene c3b18 with sdissolve
    mc "[ali]?!"
    mc "..."
    mc "(She's sound asleep. What time is it?)"
    mc "(Did she come here to sleep? Maybe she had a bad dream?)"
    mc "(I'd assume she was sleepwalking... but she's wearing a top and I'm pretty sure she sleeps in the nude.)"
    mc "(Ah well.)"
    scene c3b19 with dissolve
    mc "{i}*Yawn*{/i}"
    mc "(Won't hear me complaining.)"
    mc "(Guess I'm not going to be able to clean myself, though. I need a shower first thing in the morning. Didn't get the chance yesterday thanks to a certain...)"
    mc "{i}*Yawn*{/i}"
    mc "(Evil brunette.)"
    mc "(I'll just... get back to sleep... and hopefully pick up where I left off. In the dream world.)"
    mc "([liv]... I'm... s-s...)"
    scene black with ssdissolve
    $ renpy.pause (4, hard=True)
    uk "[mcd]?"
    uk "Hellooo. Earth to [mcd]!"
    mc "(G-Gracie?)"
    ali "Wake up, sleeping head!"
    mc "(S-Sleeping head...?)"
    scene c3b17 with sdissolve
    ali "Good morning, [mcd]. I love you."
    play music [ "audio/urban_lullaby.ogg", "audio/si_senorita.ogg" ] fadein 13.0 fadeout 07.0
    scene c3b16 with dissolve
    ali "Mmm--{nw=1.2}"
    scene c3b15 with dissolve
    ali "Mwah."
    scene c3b12 with sdissolve
    ali "You're the best [mcd] in the world... do you know that?"
    scene c3b15 with dissolve
    ali "Mwah."
    scene c3b14 with dissolve
    mc "Good morning, [ali]. Someone's still in a good mood from the photoshoot, huh?{w} What's with-"
    scene c3b13 with dissolve
    mc "(Holy fucking shit! She's literally straddling my dick!)"
    mc "(Her pussy... I can feel her pussy pressing into my abdomen.)"
    scene c3b8 with sdissolve
    mc "(Is she wet?)"
    mc "(She's definitely wet, and I'm definitely about to cum on her if I don't get my mind out of the gutter.)"
    scene c3b11 with sdissolve
    mc "{i}*Cough*{/i}"
    mc "W-What's with all the sudden affection, sweetie?"
    scene c3b12 with qdissolve
    ali "I hope you don't mind me waking you up this way."
    ali "I just can't stop thinking about what you did for me yesterday. That really was the nicest thing anyone's ever done for me, [mcd]."
    ali "I couldn't sleep last night at all. I was so excited thinking about our day."
    scene c3b14 with qdissolve
    mc "Well you don't have to thank me, [anick]. I did it because I wanted to. And I had a lot of fun spending time with you, so it was a win-win."
    scene c3b10 with sdissolve
    ali "{i}*Sigh*{/i}"
    scene c3b9 with qdissolve
    ali "Do you think I could lay here for just another minute or two?"
    scene c3b10 with qdissolve
    na "Every time she moves an inch, you feel her tight, slightly dampened pussy pressing down into you."
    mc "(Shit. I've got a {i}massive...{w=.5} fucking...{w=.5} erection.{/i}{w=.5} I was so tired last night I totally didn't even notice how sexy she looked.)"
    menu:
        "Suggest Getting Dressed":
            $ pure +=1
            $ ali_pure +=1
            mc "U-Uh... d-do you think we should maybe put some clothes on first?"
            scene c3b9 with qdissolve
            ali "That's okay, I'm not shy around you. I don't mind if you don't! After all, you are my [mcd]. I was never shy around mommy either... so why should it be different around you?"
            scene c3b10 with qdissolve
            mc "R-Right. That's fine."
        "Just Leave It":

            $ lust +=1
            $ ali_lust +=1
            mc "U-Uh... s-sure. I don't mind."

    mc "While you're here... I actually need to talk to you about something... if you don't mind."
    scene c3b9 with qdissolve
    ali "Of course I don't mind!"
    scene c3b10 with qdissolve
    mc "Right... okay then."
    mc "You see, it's just..."
    mc "I noticed that, um..."
    mc "(Fuck! How am I supposed to even word this?)"
    mc "I noticed that you are very... open... when it comes to being in the nude... or wearing very little clothes..."
    mc "It's not that I mind it. In fact, it's the opposite, as you're quite beautiful to look at."
    if tbed == True:
        mc "But if someone were to notice or find out it might raise a few eyebrows. I guess it's just not something that is... normal between a parent and child. Especially father and daughter."
    else:
        mc "But if someone were to notice or find out it might raise a few eyebrows. I guess it's just not something that is... normal between a guy my age and an [age]-year-old girl. Especially since I'm your [car]."

    scene c3b9 with qdissolve
    ali "Huh? Really? But [liv] and [mad] would sometimes get naked around mommy."
    ali "And in the girl's locker room... we all had to change around each other."
    scene c3b10 with qdissolve
    pause (1)
    mc "(She can't be serious, right? She has to know this stuff.)"
    mc "(Then again, it is [ali].)"
    mc "Uh... yeah. That's... that's different, sweetie. Getting naked in front of other girls is one thing... but you might give the wrong impression if you do it around guys."
    scene c3b9 with qdissolve
    ali "But you're not just any guy... you're my [mcd]!"
    scene c3b10 with qdissolve
    mc "Yeah, I know what you mean. I guess it's just not socially acceptable for a girl to get naked around men... even if it's their own [car]."
    scene c3b9 with qdissolve
    ali "I see."
    ali "Well...{w} they can eat a big bag of balls! I don't care what other people think, so long as you don't, [mcd]."
    ali "But I can stop. That is... if you want me to."
    scene c3b10 with qdissolve
    mc "Eh, no. It's okay [ali]. It really doesn't bother me as long as you're comfortable. I like seeing you in every way... even {i}if{/i} your butt's out."
    scene c3b9 with qdissolve
    ali "Hehe, good."
    scene c3b10 with qdissolve
    pause (1.2)
    scene c3b7 with sdissolve
    ali "Yaaawaah!"
    ali "Mmm. Feels so good to stretch in the morning."
    scene c3b6 with dissolve
    pause (1)
    scene c3b12 with dissolve
    ali "I'll get off of you now. But first..."
    scene c3b16 with dissolve
    ali "Mwah!"
    stop music fadeout 07.0
    scene c3b7 with sdissolve
    ali "I'm going to go find [liv]. Don't go back to sleep!"
    scene c3b5 with sdissolve
    pause (2)
    mc "{i}*Sigh*{/i}"
    mc "(So much for sleeping in on my day off.)"
    scene c3b4 with fadehold
    mc "(Oh, speaking of that. I should double check and make sure Bernie got my message last night.)"
    scene c3b2 with sdissolve
    pause
    "{i}\"Hey Bernie. Looks like I'm going to have to take a few days off after all. I don't really have time to explain, but things are complicated.\"{/i}"
    pause (1.5)
    "{i}\"Sure thing, kid. You deserve it. But don't forget to come by the office at some point and deliver the goods from yesterday.\"{/i}"
    pause (1)
    mc "(Yeah, I definitely need to stop by the office today.)"
    scene c3b1 with dissolve
    mc "{i}*Sigh*{/i}"
    mc "(Come to think of it... there's a lot I need to do today... including meeting Natalie soon.{w} And then there's the issue with Glenn.)"
    mc "(What a fucking lowlife. Way to give me a huge headache to sort out at the worst time.)"
    mc "(Him breathing down my neck does not sound like fun.)"
    mc "(One thing's for sure. You picked the wrong one, Mister Cole. I'm not the naïve, punk kid you seem to think I am.)"
    mc "(And I'll do everything in my power to make your life a living hell.)"
    mc "(That said I shouldn't waste too much time or energy on him. As much as I'm going to enjoy getting revenge, I need to focus all of my attention on the girls. At least for now.)"
    pause (1)
    mc "(Alright. {i}Big day{/i} ahead of me. Time to get my ass moving.)"

label liv_montage:

    play music "<loop 0.0>audio/kate_s_waltz.ogg" fadein 07.0
    scene black with sdissolve
    $ renpy.pause (4, hard=True)
    scene c3c10 with sdissolve
    liv ".{w=1}.{w=1}."
    liv "{i}*Sigh*{/i}"
    scene c3c9 with fadehold
    pause
    scene c3c8 with ssdissolve
    pause
    scene c3c7 with fadehold
    liv "(I should call Alita. She'll know what to do. She's too smart for her own good.)"
    scene c3c6 with ssdissolve
    liv "(How could something like this happen...?)"
    scene c3c5 with fadehold
    liv "(I really messed up, didn't I?)"
    liv "(Stupid, stupid... stupid!)"
    scene c3c4 with fadehold
    pause
    scene c3c3 with dissolve
    pause
    scene c3c2 with dissolve
    liv "..."
    liv "(My life is a mess.)"
    scene c3c1 with dissolve
    liv "(I wish mom was here. She'd know what to say...)"
    stop music fadeout 06.0
    pause (2)
    liv "(Ugh! I think I feel sick.)"
    pause
    scene black with sdissolve
    $ renpy.pause (3, hard=True)

label office_stopoff:

    scene c3d21 with sdissolve
    play music "<loop 0.0>audio/this_is_not_effortless.ogg" fadein 09.0
    mc "{i}*Sigh*{/i}"
    mc "([onick] was nowhere to be seen this morning. That's not a good sign given what happened.)"
    mc "(I'm also pretty sure [mad] was avoiding me.)"
    mc "(I guess it's for the best. I was able to come straight to the office with no interruption... and my meeting with Natalie is in less than an hour.)"
    mc "(Didn't even have to deal with Bernie today since he went to the gig with Brooke.)"
    mc "(Sadly {i}still{/i} didn't have the chance to shower, though. No time.)"
    pause (1)
    mc "(Thank God this police department has an online complaint form. It's not the most satisfying resolution, however. I'll need to follow up if they don't get in contact with me about Glenn. One way or another, I'll make sure he suffers the consequences of his actions.)"
    mc "(Deep breaths, [mc]. Baby steps. You've got a lot on your plate right now.)"
    scene c3d20 with fade
    mc "(If my schedule wasn't so hectic yesterday; if not for meeting with Natalie and taking [ali] to the photoshoot, I likely would've gone straight to the department.)"
    mc "(Oh well. No sense dwelling on what I should've done. And filling out this complaint form is just the start.)"
    mc "(Brooke has that booking today. I imagine she's on her way there now. I'm glad Bernie decided to tag along. Apparently, she was having some kind of panic attack.)"
    mc "(His knowledge and familiarity with this line of work will serve her well. I honestly don't know what any of us would do without his help around this place.)"
    scene c3d19 with dissolve
    na "You finish filling out the complaint form and prepare to leave the office."
    mc "(Here's to hoping they take this as seriously as {i}I{/i} plan to.)"
    scene c3d18 with fadehold
    pause
    scene c3d17 with sdissolve
    mc "Good morning, Mira!"
    scene c3d16 with dissolve
    mir "Hey, [mc]! I didn't see you come in."
    scene c3d15 with qdissolve
    mc "Just in and out this time! Due to, uh, circumstances back home I'll be taking a few days off."
    scene c3d14 with qdissolve
    mir "Uh-huh, so I've heard. You've got quite the \"situation\" on your hands."
    scene c3d15 with qdissolve
    mc "Yeah... it's... a very long story."
    scene c3d16 with qdissolve
    mir "Well, you know how Bernie is. He made sure to fill us all in on the details of your \"home situation.\" Hopefully, it wasn't something you planned to keep private."
    scene c3d13 with sdissolve
    mc "Heh... if it were a secret, I definitely wouldn't have told Bernie."
    scene c3d12 with qdissolve
    mir "Take all the time you need, [mc]. You've got a full plate. We'll captain the ship while you're gone. You don't have to worry about a thing."
    scene c3d11 with dissolve
    mir "And if you need someone to talk to, or some female advice, I'm your gal."
    scene c3d10 with qdissolve
    mc "Hm... some advice would actually be great. Though, I'm kind of in a hurry right now..."
    mc "Maybe we could meet to discuss this some other time?"
    scene c3d11 with qdissolve
    mir "Whoa, [mc], are you asking me on a date?"
    scene c3d10 with qdissolve
    mc "No, that's not what I meant..."
    scene c3d11 with dissolve
    mir "Haha! I'm just messing with you. Besides, I heard about your date with Brooke..."
    mir "Little old me has worked here for almost a year now and we've barely had a casual conversation. I'm not going to lie... I feel left out."
    scene c3d10 with qdissolve
    mc "Y-Yeah, that's mostly my fault. For a while I was so lost in the daily grind of work that I forgot to have a social life."
    scene c3d11 with qdissolve
    mir "Hehe, it's okay. We were in the same boat."
    mir "So, what do you say? Do you want to \"hang out\" sometime?"
    scene c3d9 with sdissolve
    mir "I won't tell her if you don't."
    scene c3d7 with qdissolve
    $ renpy.pause (1, hard=True)
    scene c3d8 with qdissolve
    $ renpy.pause (.3, hard=True)
    scene c3d7 with xdissolve
    pause (1.2)
    mc "(Hm... I was just proposing a friendly chat, but now it sounds like she's expecting a date or something.)"
    scene c3d7 with purpflash
    scene c3d7 with purpflash
    scene c3d7 with purpflash
    menu:
        mc "(Not sure if she's flirting or messing with me. But that definitely adds some weight to my decision here...)"
        "Hang With Mira Secretly":
            $ lust +=3
            $ cc8 = True
            mc "Of course I want to hang with you. But yeah..."
            mc "Maybe best not to mention it to Brooke. I wouldn't want her taking us the wrong way or anything."
            scene c3d6 with qdissolve
            mir "I mean... you guys aren't a couple already, right?"
            scene c3d7 with qdissolve
            if brk_rel == True:
                mc "Uh, we... ah..."
                scene c3d5 with qdissolve
                mir "Oh my God! You fucked!"
                scene c3d7 with qdissolve
                mc "No! Not at all! What kind of girl do you take me for?"
                mc "We... kissed. And now I feel terrible for telling you all of this."
                mc "(Though... it's better than letting her think we fucked.)"
                scene c3d1 with qdissolve
                mir "Hm. I believe you, but..."
            else:
                mc "Actually, nothing like that at all."
                mc "We um... decided to keep things professional between us."
                scene c3d5 with qdissolve
                mir "Oh my God! You rejected her?!"
                scene c3d7 with qdissolve
                mc "What? No! I didn't say that..."
                scene c3d5 with qdissolve
                mir "Well she certainly wasn't the one who suggested keeping things professional! So it must have been you!"
                scene c3d7 with qdissolve
                mc "Yeah, I did. But I wouldn't go so far as to say I rejected her."
                scene c3d6 with qdissolve
                mir "Sure, maybe you don't see it that way. But she will!"
                scene c3d7 with qdissolve
                mc "(Hm. I guess she's right.)"
                scene c3d1 with qdissolve

            mir "I'm actually a little surprised she didn't pull the moves on you, given her little obsession."
            scene c3d2 with qdissolve
            mc "Hey, now. Be nice, Mira. I already feel like a high schooler for gossiping with you about this."
            scene c3d6 with qdissolve
            mir "Well, you don't have to worry at all, boss."
            mir "It'll be {i}our little secret.{/i}"
            scene c3d4 with dissolve
            mir "Mwah."
            scene c3d9 with dissolve
            mir "I'm really looking forward to this \"date,\" but go enjoy your day, sweetie. I'll see you around."
            scene c3d3 with ssdissolve
            mc "(Wow. What a flirt.)"
            mc "(I never would've taken Mira for a minx. I thought for sure she was pulling for Brooke. Now I'm not so sure.)"
            mc "(Then again, she could just be joking... like before.)"
            mc "(Or maybe I'm just a total stud and she's infatuated with me. The way the women in my life have been treating me lately I'm starting to wonder.)"
            mc "(Heh, who am I kidding? I've had this effect on girls as early as I can remember.)"
            mc "(And as for what I {i}can't{/i} remember... well... I can account for at least one.)"
        "Hang With Mira Openly":

            $ pure +=3
            $ cc9 = True
            mc "Of course we should hang out! And no, we don't have to keep it a secret. Besides, it's not like we're a couple or anything."
            scene c3d1 with qdissolve
            mir "Wait, for real? I thought for sure she'd be putting the moves on you last night, given her little obsession."
            scene c3d2 with qdissolve
            mc "Nah, it's nothing like that. Be nice!"
            if brk_rel == True:
                mc "At least... not yet."
                scene c3d6 with qdissolve
                mir "Oh...? I sense a romance brewing. But don't mind me, [mc]. I'm only joking around, not trying to pry or... you know... get in the way of anything."
                mir "Besides... we're all adults, right? I'm sure Brooke wouldn't mind knowing that we hang out sometimes!"
                scene c3d7 with qdissolve
                mc "That may be true, yeah."
                mc "(Here's to hoping. I actually noticed a bit of a jealous streak in Brooke last night. Not that I can blame her.)"
            else:
                mc "We um... decided to keep things professional between us."
                scene c3d5 with qdissolve
                mir "Oh my God! You rejected her?!"
                scene c3d7 with qdissolve
                mc "What? No! I didn't say that..."
                scene c3d5 with qdissolve
                mir "Well she certainly wasn't the one who suggested keeping things professional! So it must have been you!"
                scene c3d7 with qdissolve
                mc "Yeah, I did. But I wouldn't go so far as to say I rejected her."
                scene c3d6 with qdissolve
                mir "Sure, maybe you don't see it that way. But she will!"
                scene c3d7 with qdissolve
                mc "(Hm. I guess she's right.)"

            scene c3d9 with qdissolve
            mir "Anyways... I very much look forward to our little date."
            scene c3d7 with qdissolve
            mc "A date, huh? Well then..."
            scene c3d6 with qdissolve
            mir "Hehe. I guess we'll find out. Anyway, don't let me keep you, [mc]. Go be with your girls! Or... you know... do whatever it is you're going to do!"
            mir "And I look forward to seeing you again soon!"
            scene c3d4 with dissolve
            mir "Mwah."
            scene c3d3 with ssdissolve
            mc "(Well that was interesting! Mira is a lot more confident and down to Earth than I initially thought.)"
            mc "(I'm struggling to get a read on her, however. If I didn't know any better, I'd say she was flirting with me.)"
            mc "(Then again, she could just be joking... like before.)"
            mc "(Or maybe I'm just a total stud and she's infatuated with me. The way the women in my life have been treating me lately... I'm starting to wonder.)"
            mc "(Heh... who am I kidding? I've had this effect on girls as early as I can remember...)"
            mc "(And as for what I can't remember... well, I can account for at least one.)"
        "Turn Her Down":

            $ dark +=3
            mc "Honestly, I'm not so sure if it's a good idea now that I think about it. I have too much going on as it is."
            scene c3d2 with qdissolve
            mc "Maybe some other time, Mira. For now, let's keep things professional between us."
            scene c3d1 with qdissolve
            mir "Oh! That's... that's not what I expected you to say. But I understand, I guess."
            mir "Thank you for being honest, at least."
            scene c3d2 with qdissolve
            mc "Yeah... I'm sorry, Mira. I'm not trying to be rude about this... and the last thing I'd want is for things to be awkward between us..."
            scene c3d6 with qdissolve
            mir "Say no more. You don't owe me an explanation. So long as you don't suddenly \"forget\" to send me an invitation to the next office party, I think I can forgive you. Haha."
            scene c3d7 with qdissolve
            mc "Thanks for understanding. I should be on my way."
            scene c3d6 with qdissolve
            mir "Enjoy the rest of your day, boss. See you soon."
            scene c3d3 with sdissolve
            mc "(Oof. I feel a little bad. That was certainly a bit more awkward than I expected.)"
            mc "(But it's true... I have so many things happening right now... I just don't think it's a good idea to invite even more \"trouble\" into my life.)"
            mc "(Plus I think she was flirting with me earlier. I'm struggling to get a read on her. Then again, she could just be joking... like before.)"
            mc "(Or maybe I'm just a total stud and she's infatuated with me. The way the women in my life have been treating me lately... I'm starting to wonder.)"
            mc "(Heh... who am I kidding? I've had this effect on girls as early as I can remember...)"
            mc "(Well... doesn't matter. Even going out with her as friends... it's just not something I can make time for right now. I need to focus and choose my actions carefully.)"

    stop music fadeout 06.0
    mc "(Anyway... clocks ticking. Time to go see what this thing with Natalie's all about.)"

label natalie_massage:

    scene c3e61 with fadehold
    mc "(Well... this is the place. Let's find out what the Ukrainian Ice Queen has in store for me this morning.{w} Hopefully I'm not walking into some elaborate assassination scheme.)"
    mc "(Is that so crazy to believe?{w} No, calm down. It's not like she held me at knifepoint and confessed that she dreams about executing me.)"
    pause (1)
    mc "(Wait...)"
    pause (1.2)
    scene c3e60 with dissolve
    menu:
        mc "{i}*Sweating*{/i}"
        "Knock":
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)

    pause (1)
    nat "{i}Yes? Who is it?{/i}"
    mc "It's [mc]."
    nat "{i}Oh. One moment.{/i}"
    play music "<loop 0.0>audio/lazy_walk.ogg" fadein 07.0
    pause (1)
    play sound "audio/sounds/door_open.ogg"
    scene c3e59 with sdissolve
    scene c3e59 with vpunch
    mc "(!!!)"
    mc "(No...{w=.5} fucking...{w=.5} way.)"
    pause (.5)
    show natalie at nat_transform
    mc "(Wat?)"
    scene c3e57 with dissolve
    nat "Hello [mc]."
    nat "I appreciate you sticking by your word and coming this morning."
    scene c3e58 with sdissolve
    mc "C-Coming, yes."
    mc "Did um... did you need me to wait outside while you finished getting dressed? I don't mind."
    scene c3e56 with dissolve
    mc "You know..."
    scene c3e57 with sdissolve
    nat "Oh this? No no, that's actually one of the reasons you're here."
    nat "Though, I'd prefer not to be seen by other guests. Please, come in."
    scene c3e55 with dissolve
    mc "(Okay, what in God's name is going on here? Why is she half-naked?)"
    mc "(And what does she mean by \"one of the reasons you're here?\")"
    scene c3e54 with dissolve
    nat "Please, make yourself comfortable. We don't need to get straight to business. Unless you have somewhere to be?"
    scene c3e53 with qdissolve
    mc "No, my schedule's all cleared up."
    scene c3e54 with qdissolve
    nat "Would you like something to drink? I have wine."
    scene c3e53 with qdissolve
    mc "I'm okay, thanks."
    mc "S-So, what did you need help with?"
    scene c3e52 with dissolve
    nat "Well, I'm not a young woman, [mc]. I have a lot of pent-up stress and anxiety."
    nat "This trip has been especially stressful and tiresome."
    pause (1)
    scene c3e51 with sdissolve
    nat "I need... release."
    scene c3e50 with qdissolve
    pause (1)
    mc "R-Release?"
    scene c3e51 with dissolve
    nat "Yes. Release. I'm aching. And you're a strong boy. You could help ease some of this... tension I'm feeling."
    scene c3e50 with dissolve
    mc "(B-Boy?)"
    mc "(She wants me to fuck her, doesn't she?{w} She's going to use me like I'm some sort of male gigolo... take out all of her marital frustrations on me.)"
    mc "(...Am I okay with that?)"
    scene c3e49 with dissolve
    nat "Don't get me wrong, that's not the only reason I asked you here today. I have a big favor. But I assume this will be a good ice breaker. We can talk about that later."
    scene c3e48 with dissolve
    mc "(Is this really happening?)"
    mc "S-So... we're doing this, then?"
    scene c3e47 with dissolve
    nat "If it is really no bother. As I said, I could very much use this."
    nat "Please, allow me to get in position."
    scene c3e46 with sdissolve
    mc "(Holy fuck. This is happening?!)"
    scene c3e45 with dissolve
    mc "(But why? Why me? I thought she hated me? Isn't this wrong?)"
    scene c3e44 with sdissolve
    pause
    scene c3e43 with sdissolve
    pause (1)
    scene c3e42 with qdissolve
    nat "Is this okay?"
    scene c3e43 with qdissolve
    pause (1)
    mc "Uh.{w=.5}.{w=.5}. s-sure."
    scene c3e41 with sdissolve
    mc "(S-So I guess we're doing this. But it's not too late to back out, is it? Surely, she doesn't expect to force me into this...)"
    na "Despite your indecision, you quickly undress."
    scene c3e40 with fade
    mc "(What should I do here? Should I fuck the mother of the kid that I...)"
    scene c3e41 with dissolve
    nat "You may begin the massage."
    mc "Wait...{w} what?"
    nat "There's massage oil in the dresser if you prefer this.{w} My shoulders are especially sore. But please, don't be shy. My legs and lower back could use some work, too."
    nat "Derobe yourself if that makes you more comfortable."
    na "You let loose an exacerbated chuckle."
    mc "(I'm such an idiot. Of course she doesn't want to fuck me. I literally slaughtered her child!)"
    mc "(I can't believe broken English almost caused me to whip my cock out in front of Natalie. If she wasn't planning to kill me already, that certainly would've done it.)"
    scene c3e40 with dissolve
    mc "(Still, now I have a gigantic erection. This is going to be a problem.)"
    mc "(Not sure if relieved, or disappointed.)"
    scene c3e43 with dissolve
    mc "Can I ask why you want me to do this? I mean, surely there's a spa around here somewhere..."
    scene c3e42 with qdissolve
    nat "Have you seen this place? It's not exactly a high-end hotel. Unfortunately, a professional masseuse is not something I can afford. A good massage is something I greatly need at present."
    scene c3e43 with qdissolve
    mc "R-Right. I understand."
    mc "(I'm sensing a little dishonesty...)"
    scene c3e42 with qdissolve
    nat "{i}*Sigh*{/i} And my husband... he's useless. He never does such things or treats me to spas. In fact, most of my stress comes from him! The bastard."
    scene c3e43 with qdissolve
    mc "Got it... okay."
    mc "I'll just come around to the side there..."
    scene c3e42 with qdissolve
    nat "No, please. Don't be shy. A massage works best when you're in the correct position."
    nat "I don't bite, [mc]. You can climb on the bed."
    scene c3e43 with qdissolve
    mc "{i}*Sigh*{/i}"
    scene c3e39 with sdissolve
    na "You try to position yourself over her long, voluptuous legs."
    mc "(Shit. I need to scoot closer to reach her shoulders properly. Which means she's going to feel my...)"
    scene c3e38 with dissolve
    mc "(Yup. That did it. My erection is firmly planted between the cheeks of Natalie's ass.)"
    scene c3e37 with dissolve
    nat "(Oh my God! Is that...)"
    mc "Um... Natalie... I'm not sure if..."
    scene c3e36 with dissolve
    nat "P-Please, don't be embarrassed. It's a perfectly normal reaction to a woman's body."
    scene c3e35 with qdissolve
    mc "R-Right. I'll just get started then."
    scene c3e34 with sdissolve
    na "You begin the massage. Gently at first, but slowly increasing in intensity."
    mc "(No matter how hard I try this erection isn't going away. Why did it have to be now?!)"
    scene c3e33 with dissolve
    mc "(Her skin is so soft...)"
    scene c3e38 with dissolve
    na "And with each thrust, your erection pushes even further into her buttocks."
    nat "{i}*Moan*{/i}"
    scene c3e35 with sdissolve
    nat "(Oh my... he's quite... go-good...)"
    nat "(His manhood is...)"
    scene c3e37 with dissolve
    nat "Oh!"
    mc "I-Is that... was that too hard?"
    nat "(Mmm? H-Hard?)"
    scene c3e36 with dissolve
    nat "N-No, it feels great. Please, continue."
    scene c3e35 with qdissolve
    nat "(Mmm...)"
    nat "(W-What am I doing? I asked him for a massage, but now all I can focus on is...)"
    stop music fadeout 06.0
    scene c3e37 with dissolve
    nat "{i}*Gasp*{/i}"
    scene c3e34 with sdissolve
    mc "(Shit, hearing her gasp and moan is making me even harder. I need to focus.)"
    mc "(This is all too strange if I'm being honest. Perhaps where she's from it's normal to solicit half-naked massages from men she barely knows but...)"
    scene c3e33 with dissolve
    mc "(A part of me thinks this is all apart of some... some scheme. Or perhaps she's trying to seduce me.)"
    mc "(But why me? Of all people? Not even a few days ago she was trying to kill me. And now...)"
    nat "You look like {i}him,{/i} you know..."
    scene c3e35 with dissolve
    mc "S-Sorry. What'd you say?"
    scene c3e36 with qdissolve
    nat "My son..."
    nat "You look a lot like him. He was younger than you, of course..."
    nat "But you..."
    scene c3e37 with dissolve
    nat "{i}*Gasp*{/i}"
    scene c3e35 with dissolve
    play music "<loop 0.0>audio/summer_love.ogg" fadein 14.0
    nat "..."
    scene c3e36 with qdissolve
    nat "You remind me of him quite a bit."
    nat "You... uff... you have his eyes."
    scene c3e35 with qdissolve
    mc "..."
    mc "Were you very close... the two of you?"
    scene c3e36 with qdissolve
    nat ".{w=.5}.{w=.5}.he was my world."
    scene c3e35 with qdissolve
    mc "..."
    mc "I'm going to focus on your legs now, okay?"
    scene c3e36 with qdissolve
    nat "Y-Yes, thank you."
    scene c3e33 with dissolve
    mc "(You know, suddenly...)"
    mc "(This is all making a little more sense.)"
    mc "(She's not trying to seduce you, you asshole...)"
    mc "(She's lonely. Probably trying to fill the void that was left behind by her son.)"
    scene c3e32 with dissolve
    mc "(And while it's a bit strange that she's come to me for this...)"
    mc "(If I look like him, and I'm kind to her...{w} I suppose... I could see it.)"
    mc "(Perhaps...)"
    stop music fadeout 06.0
    scene c3e31 with dissolve
    mc "(Maybe she just... doesn't have anyone else.)"
    scene c3e30 with qdissolve
    nat "W-WAIT, NOT MY FOOT!"
    play sound "audio/sounds/smack_xhard.ogg"
    scene c3e29 with xdissolve
    scene c3e29 with vpunch
    $ renpy.pause (.8, hard=True)
    scene c3e28 with sdissolve
    mc "Fuuaa!"
    mc "(S-Shit! She just... kicked me... right in the face.)"
    scene c3e27 with dissolve
    nat "Oh my God, [mc]! I'm so sorry, I forgot to tell you..."
    nat "My feet are incredibly sensitive! I'm sorry... I wasn't prepared for..."
    mc "It's..."
    mc "It's okay, don't worry... I'll..."
    scene c3e26 with dissolve
    scene c3e26 with vpunch
    mc "(Whoa...)"
    mc "(She has {i}incredible{/i} tits!)"
    nat "No no, that was completely my fault. Your nose is bleeding."
    scene c3e25 with dissolve
    nat "Hold on! Let me go get you something! Take a seat in the chair please!"
    scene black with dissolve
    $ renpy.pause (2, hard=True)
    scene c3e24 with dissolve
    mc "(Shit... that hurt.)"
    scene c3e23 with dissolve
    nat "I am {i}so, so sorry!{/i}"
    scene c3e22 with dissolve
    nat "I can't believe I just kicked you in the face. Are you sure you're okay, honey?"
    mc "Y-Yeah, I'll be fine. You don't have to..."
    scene c3e21 with qdissolve
    scene c3e21 with vpunch
    nat "No! This is my doing. Let me care for you."
    play music "<loop 0.0>audio/passing_time.mp3" fadein 08.0
    scene c3e20 with qdissolve
    mc "{i}*Sigh*{/i}"
    mc "(This should be incredibly awkward. We barely know each other, and she's sitting half-naked on my lap... practically naked.)"
    mc "(But...)"
    mc "(I owe her, and I'm going to be nice to her no matter what.)"
    mc "(If she wants to play the mother-hen, so be it.)"
    scene c3e19 with qdissolve
    nat "Haha! I can't believe I just kicked you. You poor thing."
    scene c3e21 with qdissolve
    nat "Well, at least your nose isn't broken."
    scene c3e20 with qdissolve
    mc "Nah, it doesn't even hurt that much. I think you just nicked me."
    scene c3e21 with qdissolve
    nat "Still... I bring you here, ask you for favors... and the best I can offer is a swift kick to the face!"
    scene c3e19 with qdissolve
    nat "I guess it's a good thing you owe me a favor, huh?"
    scene c3e18 with dissolve
    mc "Heh. Yeah, that definitely helps."
    scene c3e17 with dissolve
    nat "Well..."
    nat "For what it's worth..."
    scene c3e13 with dissolve
    $ renpy.pause (1.5, hard=True)
    scene c3e12 with dissolve
    nat "I forgive you, [mc]."
    scene c3e11 with qdissolve
    mc "..."
    mc "I'm glad. I also forgive you."
    scene c3e15 with dissolve
    nat "Me? What did I do?"
    scene c3e14 with qdissolve
    mc "Oh, you know... just tried to assassinate me in broad daylight."
    scene c3e15 with qdissolve
    nat "Haha."
    nat "To be fair, you may have deserved it."
    scene c3e14 with qdissolve
    mc "I know. I really did..."
    mc "And I hope you know how sorry I am."
    scene c3e15 with qdissolve
    nat "I do..."
    nat "I'm sorry too."
    scene c3e12 with dissolve
    nat "For... for assuming you're a horrible person. For fantasizing about killing you for so long."
    nat "I know you've been through trauma yourself. And still so young..."
    scene c3e11 with qdissolve
    mc "I mean, I'm not {i}that{/i} young."
    scene c3e12 with qdissolve
    nat "Compared to me you are. Trust me. I may not look it, but you're almost young enough to..."
    nat "To be my son."
    scene c3e11 with qdissolve
    mc "W-Well... for what it's worth, you aged like a fine wine. I honestly thought you were the same age as me the first time I saw you."
    scene c3e15 with dissolve
    nat "Aw, that's very sweet of you young man."
    scene c3e14 with qdissolve
    mc "Please, don't talk like a granny. You're... a very attractive and youthful woman."
    scene c3e15 with qdissolve
    nat "Oh my, you're just full of compliments."
    nat "I'm almost fifty. You know that right?"
    nat "But I'll take it."
    nat "If only my husband were more like you."
    scene c3e14 with qdissolve
    mc "I mean... you don't need {i}me{/i} to tell you. You're obviously very... ahem."
    mc "Comfortable in your own skin."
    scene c3e13 with dissolve
    nat "..."
    scene c3e10 with sdissolve
    nat "Oh my God! Why didn't you tell me I was still topless?!"
    nat "Turn around, please!"
    pause (1)
    scene c3e9 with sdissolve
    pause (1)
    mc "Hey, for the record I did {i}try{/i} to tell you. You just weren't listening."
    nat "{i}*Sigh*{/i} It is fine."
    mc "(I guess I should've made a little more effort to uh...)"
    mc "(Remind her that she's sitting on a stranger's lap naked.)"
    $ renpy.pause (1, hard=True)
    nat "And no peeking, mister!"
    $ renpy.pause (1, hard=True)
    nat "{i}Bozhe proklyati rohovi khloptsi!{/i}"
    $ renpy.pause (1.7, hard=True)
    nat "Okay, you may turn around now."
    scene c3e8 with sdissolve
    mc "{i}*Sigh*{/i}"
    mc "Sorry about that."
    scene c3e7 with qdissolve
    nat "Don't mention it. I just didn't realize my breasts were so close to..."
    scene c3e8 with qdissolve
    mc "Y-Yeah, I get it."
    scene c3e5 with dissolve
    nat "..."
    mc "..."
    scene c3e6 with qdissolve
    nat "Thank you for the massage, [mc]. I feel... much better even though it was... cut short."
    scene c3e5 with qdissolve
    mc "Honestly, Natalie, it's the least I could do. I don't mind at all."
    mc "So, you said you had another favor to ask?"
    scene c3e6 with qdissolve
    nat "Yes... I did... but not yet, okay?"
    nat "I'm going to be here for another week, and I was hoping you could..."
    nat "You know... come back for another session... when you're able."
    nat "If you don't mind, that is?"
    scene c3e5 with qdissolve
    mc "(It's a bit inconvenient with everything that's going on but...)"
    mc "Sure, Natalie. It's the least I could do."
    scene c3e4 with dissolve
    nat "Thank you for helping me, [mc]. It means a lot. It's always nice having a strong man to lend a hand... you know?"
    scene c3e3 with dissolve
    mc "The way I see it, I'm going to be indebted to you for a while."
    mc "My parents taught me accountability and the importance of redemption. You might not think I owe you that much... but I do."
    mc "Aside from that... I enjoyed my time here today. So really, don't sweat it."
    pause (1)
    scene c3e2 with ssdissolve
    stop music fadeout 08.0
    na "In that brief moment that she hugs you... you can feel a deep weight lifting from her shoulders."
    nat "{i}*Sniff*{/i}"
    scene black with sdissolve
    $ renpy.pause (3, hard=True)

label after_natalies:

    scene c3f14 with sdissolve
    play music "<loop 0.0>audio/lazy_boy_blues.ogg" fadein 09.0
    na "As you drive home, you begin to contemplate the week's events, and the sheer insanity that is your life currently."
    mc "(Temptation... is fucking... everywhere.)"
    scene c3f11 with sdissolve
    mc "(I'm trying my hardest to be a good person. To play the \"nice gentlemen\" and treat all of the women and girls in my life with respect.)"
    mc "(But if I'm being honest...)"
    mc "(I don't think I can hold on much longer.)"
    scene c3f10 with dissolve
    mc "(I'm losing control. Just like I did all the way back in my school days.)"
    scene c3f11 with dissolve
    mc "([ali] constantly flaunting her naked body.)"
    mc "([mad]'s teasing.)"
    mc "(Vanessa... who...)"
    if van_romance == True:
        mc "(At least provided me some momentary relief. Thank God.)"
    else:
        mc "(Who basically threw herself at me. I probably should've fucked her... at least then I would've gotten some relief.)"

    if brk_rel == True:
        mc "(Then there's the kiss I shared with Brooke.)"

    mc "(...the kiss I shared with my own [age]-year-old [dau].)"
    mc "(Mira's flirting...)"
    mc "(And I just gave the mother of my manslaughter victim an oddly sensual half-naked massage... with perhaps the biggest erection I've had in my life.)"
    scene c3f12 with dissolve
    mc "(I can't take it anymore. I'm going to lose my fucking mind.)"
    mc "(Most guys would give up anything to be in my shoes... but I'm actively combatting a long-repressed sex addiction...)"
    mc "(...and I'm losing the war.)"
    scene c3f13 with dissolve
    mc "(The problem, of course, isn't the idea of sex itself...)"
    mc "(But rather... what's going to happen if things boil over, and I let my sex-drive take the wheel...)"
    mc "(It could very well mean doing something reckless... or self-destructive.)"
    scene c3f11 with dissolve
    mc "(Oblivion...)"
    scene c3f11 with blueflash
    scene c3f11 with blueflash
    scene c3f11 with blueflash
    menu:
        mc "(Do I really care, though?)"
        "Let Lust Take Over":
            $ mc_lust = True
            $ lust +=3
            mc "(You know what?)"
            mc "(It's already too late. I should stop deluding myself. The only thing on my mind right now is getting into these girls' pants as soon as humanly possible.)"
            mc "(All of them.{w}.{w}.?)"
            mc "(If it can be done... maybe.)"
            mc "(Fuck it. Time to ride the wave. I'll still tread carefully and try not to hurt anyone's feelings.)"
            scene c3f9 with dissolve
            $ renpy.pause (1, hard=True)
            mc "Good news, buddy. We're back in the game. I hope you're prepared to go full throttle."
            scene c3f8 with sdissolve
            mc "(Oh! Speaking of full throttle. I somehow completely forgot I bought that... \"thing\" for [mad] while shopping with [anick]. Oh, the fun these will bring...)"
            mc "(Just need to find a way to sneak into her room and plant them.)"
        "Resist Temptation":

            $ mc_resist = True
            $ pure +=3
            mc "(No... I can do this.)"
            mc "(I need to control myself. I care too much to let things get out of hand; to prioritize a quick, meaningless fuck over other people's well-being.)"
            scene c3f10 with dissolve
            mc "(Perhaps caring is the problem. I genuinely have feelings for multiple girls right now...)"
            scene c3f11 with dissolve
            mc "(And I just hope there's a way to go about this without hurting anyone.)"
            mc "(Or losing them...)"
            mc "(I'll need to say a quick prayer to the harem gods tonight.)"
            mc "(This is going to be a bumpy ride. But I'll do everything I can to make sure that I... I don't break anyone's heart.)"
            scene c3f8 with sdissolve
            mc "(Now I feel strange for buying that... \"thing\" for [mad] while shopping with [anick]. That was quite the impulsive buy.)"
        "Who Cares?":

            $ mc_careless = True
            $ dark +=3
            mc "(Actually... why the fuck am I even holding back?)"
            mc "(After everything I've been through... am I really deluding myself with care and concern?)"
            scene c3f10 with dissolve
            mc "(I can handle whatever comes at me...)"
            mc "(And if not, who cares?)"
            scene c3f11 with dissolve
            mc "(Yeah, fuck it. None of this is my fault anyway.)"
            mc "(And all of these... women and girls... well... let's just say they're not my responsibility.)"
            mc "(What do I want? That's what matters.)"
            scene c3f8 with sdissolve
            mc "(Heh... I almost forgot about that \"thing\" I bought for [mad] while shopping with [anick].)"
            mc "(If it's sick pleasure I want, this will certainly help me achieve my goal.)"
            mc "(Now I just need to somehow sneak in her room to plant them.)"

    stop music fadeout 10.0
    scene black with sdissolve
    $ renpy.pause (3, hard=True)
    scene c3f7 with sdissolve
    mc "(Hm... no [dau]s in sight. Where could they have gone?)"
    scene c3f6 with fadehold
    mc "(Good. [mnick]'s not in her room.)"
    mc "(Am I really doing this?)"
    mc "(.{w}.{w}.)"
    scene c3f5 with dissolve
    mc "(Yeah, fuck it. I already bought the damn things. Time to make use of them.)"
    scene c3f4 with dissolve
    mc "(This is payback. And besides, she clearly needs a little help with her \"problem,\" if what I caught her doing the other night is anything to go by.)"
    scene c3f3 with dissolve
    na "You neatly place the vibrating panties in the drawer with the rest of her underwear."
    scene c3f2 with dissolve
    mc "(The question is am I doing it to help her? Or to torture her?)"
    menu:
        mc "(Or maybe a little of both?)"
        "Help Her":
            $ pure +=1
            $ panty_relief = True
            mc "(Yeah. I should give her some release. Maybe it'll help with the mood swings.)"
        "Torture Her":

            $ dark +=1
            $ panty_torture = True
            mc "(Who am I kidding? This is going to be the perfect opportunity for revenge.)"
            mc "(I'll push her right to the edge and watch her squirm. She'll probably beg for more.)"
        "Both":

            $ lust +=1
            mc "(Eh... I might give her a little release. But it's also a good opportunity for some \"harmless\" teasing. Maybe she'll end up enjoying it.)"
            mc "(Not more than I will, of course.)"


    mc "(That's assuming she wears them.)"
    mc "(...and that she doesn't freak out and make a scene. Let's hope she's wearing them at the right time. I'm certain that once she feels what these things are capable of, she'll be reluctant to take them off.)"
    scene c3f1 with sdissolve
    mc "(And now we play the waiting game. Apparently, this app I downloaded will show me the location of the panties! So I'll know exactly when she's wearing them. That's convenient.)"
    mc "(From what I read on Gooble, the vibrations these things produce are just as, if not more intense than a high-end vibrator. If that's true, this should be fun!)"
    scene c3g36 with fadehold
    mc "(Whew. I got out of there just in time.)"
    play music "<loop 0.0>audio/parkside.ogg" fadein 14.0
    scene c3g35 with sdissolve
    mc "(Looks like the girls just arrived home. I wonder where they went?)"
    scene c3g34 with sdissolve
    ali "Oh, [amc]! You're home!"
    scene c3g33 with qdissolve
    mc "Hello again, girls. Just getting in?"
    scene c3g32 with dissolve
    mad "We decided to take a walk is all. See what kind of shopping places they have nearby."
    scene c3g31 with dissolve
    mc "I'm glad you girls are getting out of the house. I've been meaning to talk to you about that."
    mc "But first... where's [onick]?"
    scene c3g30 with dissolve
    ali "[onick] didn't want to come... she's not feeling well today."
    scene c3g29 with dissolve
    mad "Or maybe she's just avoiding me."
    scene c3g28 with dissolve
    ali "Oh, please. She loves you, [mnick]. And so do I. C'mere!"
    scene c3g27 with sdissolve
    mad "Groooss! Why are your lips wet?!"
    scene c3g26 with dissolve
    ali "I wet them just for you!"
    scene c3g25 with dissolve
    mc "(Man...)"
    scene c3g24 with dissolve
    mc "(I really messed up with [liv] didn't I?)"
    scene c3g23 with dissolve
    mad "And what if you're sick like [onick]?! Now I'm gonna get sick!"
    mc "(I need to rectify this situation. No sense putting it off any longer. The only thing that's ever gotten me anywhere in this life is tackling my problems head on. I should also try to spend some time with these two tonight. Show them that I'm interested.)"
    scene c3g24 with dissolve
    mad "{i}*Gasp*{/i}"
    scene c3g21 with sdissolve
    mad "I think I'm going to sneeze..."
    scene c3g20 with dissolve
    ali "Oh, quit being dramatic!"
    mc "(Okay. It's decided. I'll speak to [liv] about last night, then I'll try and spend some time with these two.)"
    scene c3g19 with dissolve
    mc "I'm going to check on [liv]. What are you girls going to do?"
    scene c3g18 with dissolve
    ali "I think I'm going to read my fashion magazine and practice some modeling. Wanna join me, [mad]?"
    scene c3g17 with qdissolve
    mad "No thanks, sis. There's a couple movies premiering that I wanted to watch this evening. And besides... you went and got me sick! I need to rest now!"
    scene c3g18 with qdissolve
    ali "I'm not sick! And you'll be fine."
    scene c3g16 with dissolve
    mc "There's cold medicine in the bathroom just in case."
    mad "..."
    scene c3g17 with dissolve
    mad "Anyway, I'll see you guys around."
    if maddark == True and mad_scared < 1:
        scene c3g15 with fade
        na "Before leaving, she gives you a strange look... as if remembering the previous night."
        mad "Hm..."
        mc "(Well, at least she's lost the attitude... for now.)"
    elif maddark == True and mad_scared >=1:
        scene c3g14 with fade
        na "As she leaves you see a glimmer of worry in her eyes."
        mc "(Seems she remembers who's in charge around here. At least she's lost the attitude.)"
    else:
        scene c3g13 with fade
        na "Before leaving, she eyes you suspiciously."
        scene c3g14 with dissolve
        mad "Hmph!"
        mc "(Still with the attitude. But it seems like I'm making some progress. At least she actually talks to me.)"

    scene c3g12 with fade
    ali "Hey, [amc]? Will you come tell me how [liv]'s doing when you're done?"
    scene c3g10 with qdissolve
    mc "Sure, I can do that."
    scene c3g11 with qdissolve
    ali "Thanks! I'll be in my room."
    scene c3g9 with dissolve
    ali "But first... are you forgetting something?"
    scene c3g8 with qdissolve
    mc "..."
    na "(The decision you made during your trip home lingers on your mind as you decide how to handle her affection.)"
    menu:
        mc "(Oh, is she only expecting a hug?)"
        "Kiss Her":
            $ lust +=1
            $ ali_lust +=1
            $ ali_kiss = True
            scene c3g7 with dissolve
            mc "Forget that. Come here, beautiful."
            scene c3g6 with dissolve
            ali "Mm!"
            scene c3g5 with sdissolve
            na "The kiss lingers for a moment... perhaps a little longer than it should have."
            pause (1)
            scene c3g10 with sdissolve
            na "You regain your senses and decide not to make the same mistake you made with [liv]. At least... for now."
            stop music fadeout 07.0
            mc "I'll see you in a few. Have fun, sweetie."
            ali "(That kiss felt... different.)"
        "Hug Her":

            $ pure +=1
            $ ali_pure +=1
            $ ali_hug = True
            scene c3g4 with sdissolve
            mc "Come here!"
            scene c3g3 with dissolve
            ali "Mm..."
            ali "(He's so strong. I feel safe when [mcd] hugs me.)"
            na "She presses her body firmly against yours."
            ali "(How is [mcd]'s body so solid? He smells so good, too!)"
            mc "(This feels like more than a normal hug. It feels like... an embrace. I guess I {i}have{/i} been getting pretty close with [anick] lately.{w} Well... best to not let things get out of hand.)"
            stop music fadeout 07.0
            scene c3g10 with sdissolve
            mc "I'll see you in a few. Have fun, sweetie."
            ali "({i}*Sigh*{/i} I wish he would hug me for longer...)"
        "Cop a Feel":

            $ dark +=1
            $ ali_dark +=1
            $ ali_grope = True
            stop music fadeout 07.0
            scene c3g3 with sdissolve
            mc "(If she wants to get physical all the time there's going to be consequences. She can't keep tempting me like this.)"
            scene c3g1 with dissolve
            mc "(I'm not going to be able to control these urges.)"
            ali "{i}*Giggling*{/i} What are you doing, [amc]? That tickles!"
            scene c3g2 with dissolve
            ali "Ah-{w} oh..."
            if tbed == True:
                ali "D-Daddy... what are you..."
            else:
                ali "[amc]... what are you..."
            pause (1)

            scene c3g10 with fade
            mc "I'll see you in a few. Have fun, sweetie."
            ali "(Did [amc] just grab my butt?)"
            ali "(No... it must have just been an accident.)"

    scene black with sdissolve
    $ renpy.pause (3, hard=True)

label liv_talk:

    image liv_kiss = Movie(play="videos/Chapter 3/olivia_kiss.webm")
    scene c3h28 with dissolve
    mc "(I sincerely hope [onick] doesn't think I took advantage of her.)"
    mc "(But then again... she kissed {i}me,{/i} right?)"
    mc "(What am I to even make of that? She's my [age]-year-old [dau].)"
    scene mtwoa10 with fade
    menu:
        mc "(Just knock on the door and get this over with.)"
        "Knock":
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)

    pause (1.2)
    liv "{i}Who is it?{/i}"
    mc "[onick]... it's me. Can I come in?"
    ".{w}.{w}."
    liv "{i}Y-Yeah... um... just a second.{/i}"
    pause (1.2)
    liv "{i}Okay, come in.{/i}"
    scene c3h27 with fadehold
    pause (1)
    mc "Hey, [onick]."
    scene c3h26 with dissolve
    mc "Is everything alright? I heard you were sick."
    scene c3h25 with qdissolve
    liv "Y-Yeah. Just a little. Sorry I haven't said anything today. I think I'm coming down with something so I've been... resting."
    scene c3h26 with qdissolve
    mc "I see."
    scene c3h24 with dissolve
    play music "<loop 0.0>audio/northern_lights.ogg" fadein 13.0
    mc "(I'll need to make sure she's alright. But at the moment you could cut the tension in the air with a knife.)"
    mc "(Before anything else, I need to talk to her about what happened.)"
    mc "Mind if I sit down?"
    play music "<loop 0.0>audio/northern_lights.ogg" fadein 13.0
    scene c3h23 with sdissolve
    liv "N-No. Not at all."
    scene c3h21 with dissolve
    mc "[onick]... I'm so sorry about last night. I don't know what came over me."
    scene c3h20 with qdissolve
    liv "W-What do you mean? Why would you be sorry?"
    liv "I'm the one who should be sorry."
    scene c3h21 with qdissolve
    if tbed == True:
        mc "You have nothing to apologize for either. I'm the adult, and I'm your [car]. I should've known better than to let that happen."
    else:
        mc "You have nothing to apologize for either. I'm much older than you. I should've known better than to let that happen."

    scene c3h20 with qdissolve
    liv "No, don't say that. I don't want you to think of me like I'm some kid."
    liv "I did what I did. I don't know why I did it. I just couldn't help myself."
    scene c3h22 with qdissolve
    liv "And if you hate me now or think I'm a freak, I completely understand."
    liv "I mean... you clearly regret it so..."
    scene c3h19 with qdissolve
    mc "Regret it? No no, it's not like that at all..."
    mc "And of course I don't hate you. Why would I?"

    if cc0 == False and cc1 == False:
        scene c3h22 with qdissolve
        liv "Then why did you want me to stop?"
        scene c3h19 with qdissolve
        menu:
            mc "(How should I respond?)"
            "Protecting You":
                $ liv_protect = True
                mc "I guess I..."
                mc "I just wanted to protect you."
            "Uncertainty":

                $ liv_uncertain = True
                mc "I don't know... I guess I was just caught off guard and feeling unsure."
                scene c3h22 with qdissolve
                liv "Oh..."
                scene c3h19 with qdissolve
    else:

        pass

    if cc0 and cc1 == True:
        mc "I was actually worried that {i}you'd{/i} regret it.{w} That I... took advantage of you or your vulnerability."

    pause (1)

    if cc1 == True:
        scene c3h22 with qdissolve
        liv "Then why did you... grab me?"
        scene c3h19 with qdissolve
        mc "That was... I just wasn't thinking clearly."
        menu:
            mc "(Not sure what to say about this...)"
            "Apologize":
                $ liv_apologize = True
                mc "I'm sorry I did that. I shouldn't have..."
                scene c3h20 with qdissolve
                liv "N-No, it's okay! I didn't mind it."
                scene c3h21 with qdissolve
            "Blame Her":

                $ liv_blame = True
                mc "You can't just kiss a guy out of the blue like that. It's hard to resist that kind of temptation."
                scene c3h22 with qdissolve
                liv "Oh... I see. So it was my fault."
                scene c3h19 with qdissolve

    mc "Look, before I say anything else... I need to ask."
    mc "Why did you... you know?"
    pause (.5)
    scene c3h18 with dissolve
    liv "..."
    scene c3h17 with qdissolve
    liv "Because I like..."
    scene c3h16 with dissolve
    liv "{i}I think I have feelings for you!{/i}{w} I can't explain why!{w} When my face got close to yours... it was like... every muscle in my body was screaming at me to do it! To kiss you."
    scene c3h14 with dissolve
    liv "It's not normal, is it? I'm not normal."
    scene c3h15 with qdissolve
    mc "Well... I guess I'm not normal either then, because..."
    scene c3h15 with pinkflash
    scene c3h15 with pinkflash
    scene c3h15 with pinkflash
    menu:
        mc "(What should I say here?)"
        "Be Romantic":
            $ pure +=3
            $ liv_pure +=3
            $ liv_love +=1
            mc "Because I think I have feelings for you too."
            scene c3h12 with dissolve
            liv "You do?!"
            scene c3h10 with dissolve
            pause (1)
            mc "Yes."
            pause (1)
            scene c3h9 with ssdissolve
            mc "Come here."
            scene c3h8 with dissolve
            mc "What you said, about wanting to kiss me..."
            mc "I felt the same exact way."
            scene c3h7 with sdissolve
            mc "[liv]..."
            mc "I know that what happened between us wasn't normal. You're my [dau] for God's sake."
            mc "But... I think we should explore those feelings and see where they take us."
            mc "You haven't been in my life for very long. I don't want to ruin it or do something we'll both regret. So how about we just wait and see what happens?"
            mc "No pressure, no obligation."
            jump livromance
        "Be Flirtatious":

            $ lust +=3
            $ liv_lust +=3
            $ liv_horny +1
            mc "Because I wanted to kiss you too."
            scene c3h12 with dissolve
            liv "You did?!"
            scene c3h10 with dissolve
            pause (1)
            mc "Yes."
            pause (1)
            scene c3h9 with ssdissolve
            mc "Come here."
            scene c3h8 with dissolve
            mc "What you said... about your body screaming at you..."
            mc "Well I felt that, too."
            mc "And when you kissed me... I enjoyed it. A lot. I didn't want you to stop."
            scene c3h7 with sdissolve
            mc "[liv]..."
            mc "I know that what happened between us wasn't normal. You're my [dau] for God's sake."
            mc "But... I think we should explore those feelings and see where they take us."
            mc "You haven't been in my life for very long. I don't want to ruin it or do something we'll both regret. So how about we just wait and see what happens?"
            mc "No pressure, no obligation."
            jump livromance
        "Take Advantage of Her":

            $ dark +=3
            $ liv_dark +=3
            $ liv_scared +=1
            jump livdarkscene

label livdarkscene:

    mc "Because I'm attracted to you."
    scene c3h12 with dissolve
    liv "You are?"
    scene c3h10 with dissolve
    pause (1)
    mc "Yes."
    pause (1)
    scene c3h9 with ssdissolve
    mc "Come here."
    scene c3h8 with dissolve
    mc "You're a gorgeous girl."
    mc "And when you kissed me, well... I'd be lying if I said I didn't like it."
    scene c3i11 with sdissolve
    mc "Just look at you. My little [age]-year-old [dau]..."
    mc "Do you have any idea how attractive you are?"
    scene c3i10 with dissolve
    liv "Y-You think I'm attractive?"
    scene c3i11 with dissolve
    mc "I do."
    mc "You and I could make each other feel good. You have no idea the things the things we could do together."
    scene c3i9 with dissolve
    liv "[mcd]..."
    liv "Y-You're making me feel a little bit uncomfortable..."
    scene c3i8 with qdissolve
    mc "Don't you find me attractive, too?"
    scene c3i9 with dissolve
    liv "I-I do, but I'm just really nervous and I'm not used to-"
    scene c3i8 with dissolve
    mc "Then stop looking away. Look at me."
    scene c3i11 with dissolve
    mc "You don't have to resist your feelings, [liv]."
    scene c3i10 with dissolve
    liv "I-I know, it's just..."
    scene c3i9 with dissolve
    liv "You don't feel the same way that I do, do you? I'm... having a hard time understanding if you... have feelings for me too... or if you just find me attractive."
    scene c3i8 with dissolve
    menu:
        mc "(How should I respond to this?)"
        "I Do (Truth)":
            $ liv_feelings = True
            mc "Actually... I do have feelings for you."
            scene c3i7 with dissolve
            liv "You do?!"
            scene c3i8 with dissolve
            pause (1)
            mc "Yes..."
            mc "What you said... about your body screaming at you..."
            mc "Well I felt that, too."
            mc "And when you kissed me... I enjoyed it. A lot. I didn't want you to stop."
            mc "[liv]..."
            mc "I know that what happened between us wasn't normal. You're my [dau] for God's sake."
            mc "But... I think we should explore those feelings and see where they take us."
            scene c3i7 with dissolve
            liv "I-I think so, too."
            scene c3i8 with dissolve
            mc "I'm glad you feel that way."
        "I Do (Lie)":

            $ dark +=1
            $ liv_dark +=1
            $ liv_deception = True
            mc "I didn't say that. I..."
            mc "I do have feelings for you."
            scene c3i7 with dissolve
            liv "You do?!"
            scene c3i8 with dissolve
            pause (1)
            mc "Yes..."
            mc "What you said... about your body screaming at you..."
            mc "Well I felt that, too."
            mc "And when you kissed me... I enjoyed it. A lot. I didn't want you to stop."
            mc "[liv]..."
            mc "I know that what happened between us wasn't normal. You're my [dau], for God's sake."
            mc "But... I think we should explore those feelings and see where they take us."
            scene c3i7 with dissolve
            liv "I-I think so, too."
            scene c3i8 with dissolve
            mc "I'm glad you feel that way."
        "Not Yet":

            $ dark +=1
            $ liv_dark +=1
            $ liv_truthful = True
            mc "Uh... to be honest I don't really know. I mean... I'm not ruling out the possibility."
            mc "But if you want something bad enough, you should fight for it."
            mc "And when you kissed me... I didn't want you to stop. So that's a step in the right direction, isn't it?"
            liv "(So he {i}doesn't{/i} like me... I'm so stupid. Why would he? I'm just some stupid girl.)"
            mc "[liv]..."
            mc "I know that what happened between us wasn't normal. You're my [dau], for God's sake. And I'm sure that's confusing for you, especially when you have these feelings towards me."
            mc "But don't give up. If you want this badly enough, prove it to me. I'm not saying it's impossible that I'll ever share your feelings. We won't know until we've tried, right?"
            scene c3i7 with dissolve
            liv "I-I think I could do that. I want it really, really badly."
            scene c3i8 with dissolve

    menu:
        mc "(She's extremely vulnerable right now. Should I make a move?)"
        "Kiss Her":
            $ dark +=1
            $ liv_dark +=1
            $ liv_seduced = True
            $ liv_kissed = True
            scene c3i6 with sdissolve
            mc "Good. That's my girl."
            mc "Now come here for a minute..."
            scene c3i5 with dissolve
            liv "[mcd], what are you..."
            pause (.5)
            scene c3i4 with dissolve
            pause (.5)
            liv "(Oh God... this is happening... I'm so nervous and flustered.)"
            pause (.5)
            scene c3i3 with dissolve
            liv "(N-No. I'm okay with this. Kissing him makes me feel so... strange... but in a good way.)"
            liv "(I just hope that he... that he sees me as more than just some girl he's attracted to. I just want him to like me.)"
            liv "(I'll do whatever it takes. Even...{w} this.)"
            scene c3i2 with dissolve
            $ renpy.pause (1.2, hard=True)
            scene c3i3 with dissolve
            mc "(She's really going for it now. Her tongue is fully inside my mouth.)"
            pause (1)
            show liv_kiss with sdissolve
            liv "{i}*Moan*{/i}"
            liv "(G-God my mouth feels so good. A-And my whole body is tingly...)"
            pause (.5)
            liv "(Yes... put your tongue inside my mouth [mcd].)"
            liv "(I feel so good right now. Like this was meant to be.)"
            liv "{i}*Moaning Softly*{/i}"
            mc "(If we don't stop I'm going to throw her on the bed and fuck her right here. And I don't think that will end well.)"
            scene c3i6 with sdissolve
            hide liv_kiss
            mc "I think we should stop now..."
            scene c3i10 with dissolve
            liv "Yeah. Y-You're right. Thank you."
            pause
            jump afterlivromance
        "Don't Kiss Her":

            mc "(No... now's not the right time, I don't think. I've pushed things far enough and should leave her be.)"
            jump afterlivromance

label livromance:

    scene c3h6 with qdissolve
    liv "Are you saying you'd be open to the idea of you and I..."
    scene c3h7 with qdissolve
    mc "Let me stop you right there. We shouldn't put a label on anything yet."
    mc "As I said let's just see where things lead."
    scene c3h5 with qdissolve
    liv "You have no idea how relieved I am! My God, I was freaking out all day!"
    liv "And somehow with those words you've completely alleviated all of that anxiety."
    liv "I think that's why I like you."
    liv "There's just something about you I can't put my finger on. But..."
    liv "Y-You're the best, [mcd]!"
    scene c3h4 with qdissolve
    mc "No, you're the best!"
    scene c3h5 with qdissolve
    liv "{i}*Giggle*{/i}"
    scene c3h4 with qdissolve
    pause (.7)
    scene c3h3 with sdissolve
    na "The room falls silent for a moment as you both collect your thoughts."
    pause (1)
    scene c3i9 with sdissolve
    liv "[omc], can I ask you a favor?"
    scene c3i8 with qdissolve
    mc "Of course."
    scene c3i9 with qdissolve
    liv "I hope it's not too soon, but..."
    scene c3i7 with dissolve
    liv "Can you...{w} kiss me again?"
    scene c3i8 with qdissolve
    pause (.5)
    mc "You mean right now?"
    scene c3i9 with qdissolve
    liv "Yes... I just..."
    liv "I need to be sure of something."
    scene c3i8 with qdissolve
    pause (.5)
    menu:
        mc "(What should I do?)"
        "Kiss Her":
            $ lust +=1
            $ liv_lust +=1
            $ liv_horny +=1
            $ liv_kissed = True
            scene c3i6 with sdissolve
            mc "Alright. Come here."
            scene c3i5 with dissolve
            liv "(Oh God... this is happening...)"
            pause (.5)
            scene c3i4 with dissolve
            pause (.5)
            scene c3i3 with qdissolve
            liv "Mmm..."
            scene c3i2 with dissolve
            $ renpy.pause (1.2, hard=True)
            scene c3i3 with dissolve
            mc "(She's really going for it. This kiss is way more sexual than the last one.)"
            liv "{i}*Moans*{/i}"
            scene c3i1 with qdissolve
            liv "(Yes... [mcd]...)"
            liv "(Put your tongue in my mouth.)"
            pause (.7)
            show liv_kiss with sdissolve
            liv "{i}*Moan*{/i}"
            liv "(G-God my mouth feels so good. A-And my whole body is tingly...)"
            pause (.5)
            liv "(Yes... kiss me [mcd].)"
            liv "(I feel so good right now. Like this was meant to be.)"
            liv "{i}*Moaning Softly*{/i}"
            mc "(If we don't stop I'm going to throw her on the bed and fuck her right here. And I don't think that will end well.)"
            scene c3i6 with sdissolve
            hide liv_kiss
            mc "I think we should stop now."
            scene c3i10 with dissolve
            liv "Yeah. Y-You're right."
            pause
            jump afterlivromance
        "Don't":

            $ pure +=1
            $ liv_pure +=1
            mc "I don't think it's such a good idea just yet. Let's think about what we just talked about first."
            scene c3i7 with qdissolve
            liv "Y-Yeah. I guess you're right."
            scene c3i8 with qdissolve
            pause
            jump afterlivromance

label afterlivromance:

    stop music fadeout 09.0
    scene black with sdissolve
    $ renpy.pause (3, hard=True)
    scene c3j12 with sdissolve
    liv "Thank you so much for coming to talk to me. I feel a lot better now."
    scene c3j11 with qdissolve
    mc "I do too. I was stressing about it as well."
    scene c3j10 with sdissolve
    mc "Heh. Are you going to come out of your room now?"
    scene c3j9 with qdissolve
    liv "Oh, actually... I wasn't lying when I said I'm feeling sick."
    if liv_kissed == True:
        scene c3j8 with qdissolve
        liv "Crap! Sorry! I should've said something before you kissed me..."
        scene c3j7 with qdissolve
        mc "Haha, I guess so. But it's fine. I never get sick."
    else:
        scene c3j8 with qdissolve
        liv "Crap! I probably should've said something. I guess it's a good thing you didn't kiss me."
        scene c3j7 with qdissolve
        mc "Haha, I guess so. But I'm not worried, I never get sick."

    mc "Come here, let me feel your forehead."
    scene c3j6 with dissolve
    mc "(Shit!)"
    mc "You're burning up."
    scene c3j5 with dissolve
    liv "Yeah. I'll be okay though. I don't feel {i}that{/i} bad."
    scene c3j4 with qdissolve
    mc "Alright. If you need anything at all, I'm here. Get some rest, okay?"
    scene c3j3 with qdissolve
    liv "Thank you [mcd]."
    scene c3j4 with qdissolve
    mc "You're welcome. Goodnight, sweetie."
    pause (.5)
    scene black with sdissolve
    pause (2)
    scene c3j2 with dissolve
    mc "(Good God. Did all of that really just happen? I'm beside myself right now.)"
    mc "(And hard as a rock.)"
    mc "(I can't believe my own [dau] has feelings for me. This is surreal. This is like... the plot of some fucking cliché porn flick.)"
    mc "(No time to think about it all right now though. I need to bring her this medicine.)"
    play sound "audio/sounds/toilet-flush.ogg" fadeout 05.0
    scene c3j1 with fadehold
    mc "(Oh... she's already sleeping. She must be pretty sick.)"
    mc "(And way too cute for her own good.)"
    mc "(Anyway I better not disturb her. I'll just leave the medicine on her nightstand.)"
    pause

label allieroomscene:

    scene mtwoa10 with fadehold
    mc "(What a crazy day this has been so far.)"
    scene c3k37 with fade
    mc "(Time to see what [anick]'s up to. I think she said something about practicing her modeling?)"
    menu:
        mc "(I can hear her humming. She's in a really good mood tonight. I should just knock.)"
        "Knock":
            scene c3k36 with qdissolve
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            play sound "audio/sounds/knock.ogg"
            pause (.21)
            scene c3k37 with dissolve

    mc "[anick], it's me. Can I come in?"
    ali "{i}Of course! Come on in, [mcd].{/i}"
    scene c3k35 with fade
    play music "<loop 0.0>audio/every_step.ogg" fadein 09.0
    mc "There's my angel."
    ali "Yay! You're just in time... I was just now thinking about practicing my modeling."
    mc "Oh? Did you want to do some poses for me?"
    ali "Yes, I would love to! Will you take pictures of me, [mcd]?"
    scene c3k33 with fade
    mc "Yeah, of course. I've got my phone with me so I'll just use that. What are you up to right now though?"
    scene c3k34 with qdissolve
    ali "Oh, just setting up my Incelgram."
    ali "It's this app that lets you upload pictures to a profile."
    scene c3k33 with qdissolve
    mc "Hey, I'm not {i}that{/i} old, [anick]. Of course I know what Incelgram is. It's pretty common for photographers to use it actually."
    scene c3k32 with qdissolve
    ali "Well I figured if I'm going to be a model I should have one too! Don't you think that's a good idea, [mcd]?"
    scene c3k31 with qdissolve
    pause (.5)
    menu:
        mc "(Hmm. On the one hand, there's a lot of creeps on the internet. On the other, it could really help her with modeling. I doubt she'd do anything lewd with it... but do I care?)"
        "Encourage Her":
            $ ali_incelgram = True
            mc "I think it's a great idea, so long as you're careful what you upload. Remember what we talked about this morning? Keep those clothes on young lady!"
            scene c3k32 with qdissolve
            ali "Haha that's funny, [mcd]. I wouldn't let strangers see me if I weren't fully clothed! Some creepy guy could see. That's gross!"
            scene c3k31 with qdissolve
            mc "(Whew. She has no idea how relieved I am that she just said that.)"
            scene c3k34 with qdissolve
            ali "I don't mind you seeing me without clothes, though. I really meant it when I said it! I just feel so comfortable around you."
            scene c3k33 with qdissolve
            mc "(...and that.)"
        "It Depends":

            $ ali_incelgram = True
            mc "It could be. Just be careful what you upload. Remember what we talked about this morning? Keep those clothes on young lady!"
            scene c3k32 with qdissolve
            ali "Haha that's funny, [mcd]. I wouldn't let strangers see me if I weren't fully clothed! Some creepy guy could see. That's gross!"
            scene c3k31 with qdissolve
            mc "(Whew. She has no idea how relieved I am that she just said that.)"
            scene c3k34 with qdissolve
            ali "I don't mind you seeing me without clothes, though. I really meant it when I said it! I just feel so comfortable around you."
            scene c3k33 with qdissolve
            mc "(...and that.)"
        "Discourage Her":

            mc "Eh... I feel like that stuff is a waste of time to be honest. I was never really a fan of social media and whatnot."
            scene c3k29 with qdissolve
            mc "And besides... if I'm being completely honest, I don't think it's the best idea for you to upload photos there."
            scene c3k30 with qdissolve
            ali "But why, [mcd]?"
            scene c3k29 with qdissolve
            mc "Well... I've seen how you dress... or rather... how you don't dress. And there could be a lot of perverted men on the internet."
            scene c3k30 with qdissolve
            ali "But I wouldn't post anything if I weren't fully clothed! I don't like random perverts. That's gross!"
            scene c3k29 with qdissolve
            mc "(Whew. She has no idea how relieved I am that she just said that.)"
            scene c3k34 with qdissolve
            ali "I don't mind you seeing me without clothes, though. I really meant it when I said it! I just feel so comfortable around you."
            scene c3k33 with qdissolve
            mc "(...and that.)"
            scene c3k29 with qdissolve
            mc "I still don't think it's a good idea, [ali]. But at the end of the day, it's up to you."
            scene c3k30 with qdissolve
            ali "Okay, [mcd]. I'll think about it more."

    scene c3k28 with fadehold
    ali "Speaking of clothes, I have the perfect outfit in mind for our photoshoot. I think you're going to like it... especially since you like my butt so much!"
    scene c3k27 with qdissolve
    mc "That's nice swee-{w} wait what?"
    scene c3k26 with qdissolve
    ali "You said so earlier when we were talking in your room. You said you like to see me even if I'm flaunting my butt!"
    scene c3k25 with qdissolve
    mc "That's not..."
    if ali_grope == True:
        scene c3k24 with dissolve
        ali "Then you grabbed it when you hugged me earlier."
        scene c3k23 with qdissolve
        mc "(She's got me there...)"
        mc "That was... (not an accident)."
    else:

        scene c3k24 with dissolve
        ali "Just admit it, [mcd]! You like it!"
        scene c3k23 with qdissolve

    scene c3k23 with pinkflash
    scene c3k23 with pinkflash
    scene c3k23 with pinkflash

    menu:
        mc "(She's got a point... but she's opening a rabbit hole and causing me to think about naughty things again. I'm not sure how much longer I can control myself.)"
        "Be Good":
            $ pure +=3
            $ ali_pure +=3
            $ ali_love +=1
            jump beinggood
        "Be Flirty":

            $ lust +=3
            $ ali_lust +=3
            $ ali_horny +=1
            jump beingflirty
        "Take Advantage":

            $ dark +=3
            $ ali_dark +=3
            $ alidark = True
            $ ali_scared +=2
            $ ali_touched = True
            stop music fadeout 06.0
            jump takingadvantage

label beinggood:

    stop music fadeout 08.0
    mc "Well since you're pulling my arm."
    scene c3k22 with qdissolve
    mc "You're such a beautiful girl, [ali]. It's hard not to like looking at you."
    scene c3k21 with qdissolve
    ali "Aww, that's one of the nicest things anyone's ever said to me!"
    ali "You really think I'm beautiful?"
    play music "<loop 0.0>audio/sixteen_twenty_five.ogg" fadein 13.0
    scene c3k20 with qdissolve
    mc "In every way possible. I'm quite proud, actually. I think you take after your [car]!"
    scene c3k19 with qdissolve
    ali "I actually think [mad] takes after you the most! I mean her look, not her personality."
    scene c3k22 with qdissolve
    mc "You do?"
    scene c3k21 with qdissolve
    ali "Yeah! She's got the same color hair, and she has like... the same eyebrows! And your nose is identical, except for all the freckles!"
    scene c3k22 with qdissolve
    mc "That's... true. I hadn't really thought about it much."
    mc "But anyway, if I'm being honest, the {i}fact{/i} that I like seeing your butt is... not something I should be saying as your [car]. It's considered quite inappropriate, and society would frown on me looking at you like that."
    scene c3k21 with qdissolve
    ali "Haha, that's a bit silly, [mcd]. You're the first person I've met who is obsessed with butts! But guess what? I don't care what society thinks. You're my [car], and I'd do anything to make you happy."
    scene c3k24 with qdissolve
    ali "Um... could you explain why society thinks it's bad, though?"
    scene c3k23 with qdissolve
    mc "Well, how do I explain this..."
    mc "I'm sure you know guys like to look at girls who are nude, right? Especially their boobs."
    scene c3k24 with qdissolve
    ali "I've heard... but why?"
    scene c3k23 with qdissolve
    ali "(Maybe this has something to do with the way I feel when I see [mcd] without a shirt on.{w} Or when his penis was out.{w} Or when I was younger, and I saw that one scene in a romantic movie. Is that why mom covered my eyes?)"
    ali "(Seeing [mcd]'s penis made me feel really good and funny. I didn't want him to put it away and I couldn't stop thinking about it that night. I even had trouble sleeping!)"
    mc "Well... just like a girl's boobs... the butt is an intimate and rather private part of the body. It's why we dress up when we leave the house. That's why it's not okay to get naked in front of someone unless you're really close or have a romantic relationship with each other."
    scene c3k24 with qdissolve
    ali "But I like you seeing me. And you're so sweet and romantic!"
    scene c3k19 with qdissolve
    ali "I just don't get it! Why is something that makes you happy not okay?"
    scene c3k20 with qdissolve
    ali "{i}*Pouting*{/i}"
    mc "Well... I agree with you that there's nothing wrong with enjoying things that make us happy. And as I explained, I do like seeing you. So society very well could be wrong..."
    mc "I guess I've never really thought about it before now."
    scene c3k19 with qdissolve
    ali "Well... society can go to hell! Mom always told me I made her happy, and I love making you happy, too. So I'll do whatever {i}you{/i} want! Even if it means showing you my butt right now!"
    scene c3k20 with qdissolve
    mc "*Cough* Right... now?"
    mc "(Never change, [ali].)"
    scene c3k19 with qdissolve
    ali "Yes!"
    scene c3k20 with qdissolve
    mc "I mean, you could..."
    scene c3k22 with qdissolve
    ali "(It's so cute that [mcd] likes my butt. I don't get it, but I just want to tease him now!)"
    scene c3k24 with qdissolve
    ali "I will if you want me to, [mcd]."
    scene c3k23 with qdissolve
    mc "(I can't believe this is happening right now.)"
    mc "Fine. You got me. I'm a weirdo and yes, I'd like to see your butt."
    scene c3k21 with qdissolve
    ali "Haha! You're a freak, [mcd]! I like it. But yes, like I said, it makes me happy to make you happy. So I'm taking these off!"
    scene c3k18 with dissolve
    pause
    scene c3k17 with dissolve
    pause (.5)
    scene c3k17 with vpunch
    mc "(!!!)"
    mc "(Oh {i}fuck,{/i} I thought she was wearing underwear!)"
    scene c3k16 with sdissolve
    mc "(What on God's green earth is going on right now?!)"
    ali "(His face is so cute! He really does like butts!)"
    ali "(But for some reason. I'm feeling kinda vulnerable right now. The way he's looking at me is making me feel something I've never felt before.)"
    ali "(It's a nice feeling. Just a little... intense. Like something is building up inside my tummy...)"
    scene c3k15 with sdissolve
    ali "Let me move over to the bed. You can look at me for as long and as hard as you want, [mcd]."
    scene c3k14 with fadehold
    mc "(.{w}.{w}.long and hard about sums it up.)"
    mc "(By the grace of God, her pussy is fully exposed right now. This girl is going to fucking kill me someday! I swear it.)"
    mc "(This is starting to confirm what I suspected. She's either an expert flirt, or completely clueless about sexuality. And I'm actually leaning towards the latter. She's clueless.)"
    mc "(Which means it's up to me to teach her...)"

    menu:
        mc "(Or... I could behave myself.)"
        "Enough For Now":
            $ pure +=1
            $ ali_pure +=1
            mc "(I think that's enough for now. I don't think it's a good time to push things too far.)"
            mc "So, staring at your butt is nice and all..."
            mc "But isn't it [car] [dau] photoshoot time?"
            scene c3k13 with dissolve
            ali "Oh yeah! I almost forgot!"
            stop music fadeout 07.0
            scene c3k12 with dissolve
            ali "Yay! I should get changed now!"
            jump allieposescene
        "Push It Further":

            $ lust +=1
            $ ali_lust +=1
            $ ali_touched = True
            mc "[anick]... do you think I could touch you?"
            if ali_grope == True:
                mc "Like I did earlier?"
                scene c3k12 with dissolve
                ali "(So he {i}did{/i} do that on purpose!)"

    scene c3k13 with dissolve
    ali "You want to grab my butt?"
    scene c3k14 with dissolve
    mc "Yeah."
    scene c3k13 with dissolve
    ali "O-Of course I don't mind. J-Just... be careful because of, um..."
    scene c3k12 with dissolve
    ali "Um... nevermind, [mcd]. You can touch."
    scene c3k10 with dissolve
    pause
    mc "(This feels wrong. Like I'm taking advantage of her. But I can't help myself.)"
    scene c3k8 with sdissolve
    ali "Oh!"
    mc "Everything alright? I didn't mean to startle you."
    ali "Y-Yes. I'm alright. It just feels weird, and your hands are really close to my..."
    ali "Um. Nevermind."
    scene c3k7 with sdissolve
    ali "(Oh, what have you gotten yourself into, [ali]? I'm feeling so strange right now.)"
    ali "(Like that time when mom took us horse riding, and my...)"
    scene c3k6 with dissolve
    ali "{i}*Moan*{/i}"
    scene c3k5 with qdissolve
    mc "Everything alright? Should I stop?"
    scene c3k4 with dissolve
    ali "N-No. It's okay."
    ali "I-I can tell you really like this. You're even flushed!"
    scene c3k5 with dissolve
    mc "So are you. Your face is red like a tomato. Are you feeling what I'm feeling?"
    scene c3k4 with dissolve
    ali "Yes! I'm so glad you said something. I don't know what it is, but I haven't felt this before. It's like I'm hot... but in a good way. And the more you look at me and talk about it, the more I'm feeling flushed."
    scene c3k8 with sdissolve
    mc "I'll be honest again. That means you're turned on."
    ali "Turned on?"
    mc "Y-Yeah. It's because touching you like this is... it's a little bit sexual. Normally this is something that is only done between two romantic partners."
    ali "Does that mean we're romantic partners now?"
    mc "Haha."
    mc "I mean, it could."
    scene c3k6 with sdissolve
    ali "(Oh no, something's happening. I'm starting to lose control of my legs. This is too overwhelming.)"
    scene c3k4 with dissolve
    if tbed == True:
        ali "D-Daddy... can we stop?"
    else:
        ali "[amc]... can we stop?"

    scene c3k5 with dissolve
    mc "Of course, [anick]. Whenever you want."
    scene c3k3 with fadehold
    mc "Besides..."
    na "You speak in a playful, reassuring tone."
    mc "Isn't it [car] [dau] photoshoot time?"
    scene c3k1 with qdissolve
    ali "Oh yeah! I almost forgot!"
    stop music fadeout 07.0
    scene c3k2 with qdissolve
    ali "Yay! I should get changed now!"
    jump allieposescene

label beingflirty:

    stop music fadeout 08.0
    mc "Well, since you're pulling my arm..."
    scene c3k22 with qdissolve
    mc "I... love seeing it, actually. It's really nice... and I think I could stare at it all day."
    scene c3k21 with qdissolve
    ali "You like it that much?"
    play music "<loop 0.0>audio/sixteen_twenty_five.ogg" fadein 13.0
    scene c3k20 with qdissolve
    mc "Yeah... you have an incredible butt, [ali], and if you keep letting me see it, I might start to get... certain feelings."
    mc "But if I'm being honest, that's not something I should be saying as your [car]. It's considered quite inappropriate, and society would frown on me looking at you like that."
    scene c3k21 with qdissolve
    ali "Haha, that's a bit silly, [mcd]. You're the first person I've met who is obsessed with butts! But guess what? I don't care what society thinks. You're my [car], and I'd do anything to make you happy."
    scene c3k24 with qdissolve
    ali "Um... could you explain why society thinks it's bad, though?"
    scene c3k23 with qdissolve
    mc "Well, how do I explain this..."
    mc "I'm sure you know guys like to look at girls who are nude, right? Especially their boobs."
    scene c3k24 with qdissolve
    ali "I've heard... but why?"
    scene c3k23 with qdissolve
    ali "(Maybe this has something to do with the way I feel when I see [mcd] without a shirt on.{w} Or when his penis was out.{w} Or when I was younger, and I saw that one scene in a romantic movie. Is that why mom covered my eyes?)"
    ali "(Seeing [mcd]'s penis made me feel really good and funny. I didn't want him to put it away and I couldn't stop thinking about it that night. I even had trouble sleeping!)"
    mc "Well... just like a girl's boobs... the butt is an intimate and rather private part of the body. It's why we dress up when we leave the house. That's why it's not okay to get naked in front of someone unless you're really close or have a romantic relationship with each other."
    scene c3k24 with qdissolve
    ali "But I like you seeing me. And you're so sweet and romantic!"
    scene c3k19 with qdissolve
    ali "I just don't get it! Why is something that makes you happy not okay?"
    scene c3k20 with qdissolve
    ali "{i}*Pout*{/i}"
    mc "Well... I agree with you that there's nothing wrong with making someone happy. And as I explained, I do like seeing you. So society very well could be wrong..."
    mc "I guess I've never really thought about it before now."
    scene c3k24 with qdissolve
    ali "Well... society can go to hell! Mom always told me I made her happy, and I love making you happy, too. So I'll do whatever {i}you{/i} want. Even if it means showing you my butt right now!"
    scene c3k23 with qdissolve
    mc "{i}*Cough*{/i} Right... now?"
    mc "(Never change, [ali].)"
    scene c3k24 with qdissolve
    ali "Yes!"
    scene c3k22 with qdissolve
    mc "I mean, you could..."
    ali "(It's so cute that [mcd] likes my butt. I don't get it, but I just want to tease him now!)"
    scene c3k21 with qdissolve
    ali "I will if you want me to, [mcd]."
    scene c3k22 with qdissolve
    mc "(I can't believe this is happening right now.)"
    mc "Fine. You got me. I'm a weirdo and yes, I'd like to see your butt."
    scene c3k21 with qdissolve
    ali "Haha! You're a freak, [mcd]! I like it. But yes, like I said, it makes me happy to make you happy. So I'm taking these off!"
    scene c3k18 with dissolve
    pause
    scene c3k17 with dissolve
    pause (.5)
    scene c3k17 with vpunch
    mc "(!!!)"
    mc "(Oh fuck. I thought she was wearing underwear!)"
    mc "(What on God's green earth is going on right now?!)"
    scene c3k16 with sdissolve
    ali "(His face is so cute! He really does like butts!)"
    ali "(But for some reason. I'm feeling kinda vulnerable right now. The way he's looking at me is making me feel something I've never felt before.)"
    ali "(It's a nice feeling. Just a little... intense. Like something is building up inside my tummy...)"
    scene c3k15 with sdissolve
    ali "Let me move over to the bed. You can look at me for as long and as hard as you want, [mcd]."
    scene c3k14 with fadehold
    mc "(.{w}.{w}.long and hard about sums it up.)"
    mc "(By the grace of God, her pussy is fully exposed right now. This girl is going to fucking kill me someday! I swear it.)"
    mc "(This is starting to confirm what I suspected. She's either an expert flirt, or completely clueless about sexuality. And I'm actually leaning towards the latter. She's clueless.)"
    mc "(Which means it's up to me to teach her...)"

    menu:
        mc "(Or... I could behave myself.)"
        "Enough For Now":
            $ pure +=1
            $ ali_pure +=1
            mc "(I think that's enough for now. I don't think it's a good time to push things too far.)"
            mc "So, staring at your butt is nice and all..."
            mc "But isn't it [car] [dau] photoshoot time?"
            scene c3k13 with dissolve
            ali "Oh yeah! I almost forgot!"
            stop music fadeout 07.0
            scene c3k12 with dissolve
            ali "Yay! I should get changed now!"
            jump allieposescene
        "Push It Further":

            $ lust +=2
            $ ali_lust +=2
            $ ali_touched = True
            mc "[anick]... do you think I could touch you?"
            if ali_grope == True:
                mc "Like I did earlier?"
                scene c3k12 with dissolve
                ali "(So he {i}did{/i} do that on purpose!)"

    scene c3k13 with dissolve
    ali "You want to grab my butt?"
    scene c3k14 with dissolve
    mc "Yeah."
    scene c3k13 with dissolve
    ali "O-Of course I don't mind. J-Just... be careful because of, um..."
    scene c3k12 with dissolve
    ali "Um... nevermind, [mcd]. You can touch."
    scene c3k10 with dissolve
    pause
    mc "(This feels wrong. Like I'm taking advantage of her. But I can't help myself.)"
    scene c3k8 with sdissolve
    ali "Oh!"
    mc "Everything alright? I didn't mean to startle you."
    ali "Y-Yes. I'm alright. It just feels weird, and your hands are really close to my..."
    ali "Um. Nevermind."
    scene c3k7 with sdissolve
    ali "(Oh, what have you gotten yourself into, [ali]? I'm feeling so strange right now.)"
    ali "(Like that time when mom took us horse riding, and my...)"
    scene c3k6 with dissolve
    ali "{i}*Moan*{/i}"
    scene c3k5 with dissolve
    mc "Everything alright? Should I stop?"
    scene c3k4 with dissolve
    ali "N-No. It's okay."
    ali "I-I can tell you really like this. You're even flushed!"
    scene c3k5 with dissolve
    mc "So are you. Your face is red like a tomato. Are you feeling what I'm feeling?"
    scene c3k4 with dissolve
    ali "Yes! I'm so glad you said something. I don't know what it is, but I haven't felt this before. It's like I'm hot... but in a good way. And the more you look at me and talk about it, the more I'm feeling flushed."
    scene c3k8 with sdissolve
    mc "I'll be honest again. That means you're turned on."
    ali "Turned on?"
    mc "Y-Yeah. It's because touching you like this is... it's a little bit sexual. Normally this is something that is only done between two romantic partners."
    ali "Does that mean we're romantic partners now?"
    mc "Haha."
    mc "I mean, it could."
    scene c3k6 with sdissolve
    ali "(Oh no, something's happening. I'm starting to lose control of my legs. This is too overwhelming.)"
    scene c3k4 with dissolve
    if tbed == True:
        ali "D-Daddy... can we stop?"
    else:
        ali "[amc]... can we stop?"

    scene c3k5 with dissolve
    mc "Of course, [anick]. Whenever you want."
    scene c3k3 with fadehold
    mc "Besides..."
    na "You speak in a playful, reassuring tone."
    mc "Isn't it [car] [dau] photoshoot time?"
    scene c3k1 with qdissolve
    ali "Oh yeah! I almost forgot!"
    stop music fadeout 07.0
    scene c3k2 with qdissolve
    ali "Yay! I should get changed now!"
    jump allieposescene

label takingadvantage:

    mc "Okay, you're right. I do like it. You have a beautiful butt."
    scene c3k22 with qdissolve
    mc "Every inch of you is attractive, [ali]. You're one of the most precious girls I've ever laid eyes on."
    play music "<loop 0.0>audio/nocturne.ogg" fadein 08.0
    if tbed:
        mc "I'm quite proud of the fact that you're my [dau]. I made you. And therefore I really like seeing you. Every inch of you. It makes me happy that you're so comfortable around me, so I think you should flaunt your body more often and get naked whenever you like."
    else:
        mc "I'm quite proud of the fact that you're my [dau]. And therefore I really like seeing you. Every inch of you. It makes me happy. It makes me happy that you're so comfortable around me, so I think you should flaunt your body more often and get naked whenever you like."

    scene c3k21 with qdissolve
    ali "Awww, [mcd]! You're being so sweet right now. Mom always told me I made her happy, and I love making you happy, too. So I'll do whatever you want. Always. Even if it means showing you my butt."
    scene c3k22 with qdissolve
    ali "(It's so cute that [mcd] likes my butt. I don't get it, but I just want to tease him now!)"
    mc "Would you show me right now?"
    scene c3k21 with qdissolve
    ali "Haha! You're a freak, [mcd]! I like it. But yes, like I said, it makes me happy to make you happy, so if you want to see it... I will show you."
    scene c3k22 with qdissolve
    mc "(This is starting to confirm what I suspected. She's either an expert flirt, or completely clueless about sexuality. And I'm actually leaning towards the latter. She's clueless.)"
    mc "(Which means it's up to me to teach her...)"
    if tbed == True:
        mc "(A bit strange for an [age]-year-old but I'm not complaining.)"
    else:
        mc "(A bit strange for someone who's legally an adult but I'm not complaining.)"

    scene c3k21 with qdissolve
    ali "Do you want me to take my pants off right now?"
    scene c3k22 with qdissolve
    mc "Yeah, sweetie. Take them off."
    scene c3k21 with qdissolve
    ali "Okay! Just so you know, I'm not wearing any underwear."
    scene c3k22 with qdissolve
    mc "(Oh, fuck. It's my lucky day then. This was easier than I thought.)"
    scene c3k18 with fadehold
    pause
    scene c3k17 with dissolve
    pause (.5)
    scene c3k17 with vpunch
    mc "(Holy fuck!)"
    ali "You can look at it all you want, [mcd]."
    if tbed == True:
        ali "Like you mentioned, you made it! So it's yours!"

    scene c3k16 with sdissolve
    ali "(His face is so cute! He really does like butts!)"
    ali "(But for some reason. I'm feeling kinda vulnerable right now. The way he's looking at me is making me feel something I've never felt before.)"
    ali "(It's a nice feeling. Just a little... intense. Like something is building up inside my tummy...)"
    ali "(Maybe this has something to do with the way I feel when I see [mcd] without a shirt on.{w} Or when his penis was out.{w} Or when I was younger, and I saw that one scene in a romantic movie. Is that why mom covered my eyes?)"
    ali "(Seeing [mcd]'s penis made me feel really good and funny. I didn't want him to put it away and I couldn't stop thinking about it that night. I even had trouble sleeping!)"
    mc "(If she complies with this... it means she's clueless and able to be taken complete advantage of. I mean, it's no secret that she's not the brightest girl.)"
    mc "(And eventually, mine to do whatever I want with. I can literally teach this girl that she's mine to fuck, and she won't have the first clue that what we're doing is wrong.)"
    mc "(Guess sex-ed is important. Good thing she doesn't seem to have been taught about this stuff. Speaking of that, I'll have to inquire with one of them later.)"
    if tbed == True and age <= 17:
        mc "(I still haven't even brought up school. It's the summer, but...)"
        mc "(Given their age, I doubt they've graduated and it's something I'll definitely have to think about more once summer's up.)"

    mc "(Alright. Here goes nothing.)"
    mc "Can you move to the bed so I can get a closer look?"
    scene c3k15 with sdissolve
    ali "Sure, [mcd]. How do you want me?"
    scene c3l15 with dissolve
    mc "(I fucking knew it. Score.)"
    mc "Just bend over."
    scene c3l16 with qdissolve
    ali "Hehe. Okay. You're so funny."
    scene c3k13 with fadehold
    ali "Like this?"
    scene c3k14 with qdissolve
    mc ".{w}.{w}.Yeah. Stay just like that."
    scene c3k10 with dissolve
    pause
    if tbed == True and age <= 16:
        mc "Mmm. Good. There's my little girl's butt."
    else:
        mc "Mmm. Good. There's my favorite butt."

    mc "(...I can almost see inside of her.)"
    ali "I can tell you really like this. You're even flushed!"
    mc "So are you. Your face is red like a tomato. Are you feeling what I'm feeling?"
    scene c3k4 with sdissolve
    ali "Yes! I'm so glad you said something. I don't know what it is, but I haven't felt this before. It's like I'm hot... but in a good way. And the more you look at me and talk about it, the more I'm feeling flushed."
    ali "So I think I like it too. You know. You staring at me, seeing my butt. It makes me feel really good."
    scene c3k7 with dissolve
    mc "I'm going to touch you now, [anick]."
    scene c3k4 with dissolve
    ali "O-Of course. J-Just... be careful because of, um..."
    scene c3k9 with dissolve
    ali "Actually, [mcd], wait, I'm..."
    scene c3k10 with sdissolve
    na "Sensing she might resist... you don't give her time to finish talking."
    scene c3k8 with qdissolve
    ali "Oh!"
    mc "Everything alright? I didn't mean to startle you."
    ali "Y-Yes. I'm alright. It just feels weird, and your hands are really close to my..."
    ali "Um. Nevermind."
    scene c3k5 with sdissolve
    ali "(Oh, what have you gotten yourself into, [ali]? I'm feeling so strange right now.)"
    ali "(Like that time when mom took us horse riding, and my...)"
    scene c3k8 with sdissolve
    pause
    scene c3l28 with dissolve
    ali "{i}*Moan*{/i}"
    pause (1)
    ali "(Oh no... he got closer. I'm so exposed in this position. He's going to see my... my vagina.)"
    ali "(I don't think I want him to see... he's too close, he'll see like... everything!)"
    ali "(But if it makes him happy, should I even worry about it?)"
    ali "(I-If I... if I didn't feel myself leaking... it wouldn't be so... oh God, I don't know what he's doing but it feels so good.)"
    scene c3l27 with dissolve
    ali "(Oh!)"
    ali "(Oh God, he's spreading my... thing open!)"
    ali "[mcd], wait! I'm starting to feel really embarrassed. If you don't stop..."
    scene c3k9 with sdissolve
    ali "No! Stop! You can s-see everything!"
    scene c3l28 with sdissolve
    $ renpy.pause (.7, hard=True)
    scene c3l27 with dissolve
    $ renpy.pause (1.2, hard=True)
    scene c3l28 with sdissolve
    $ renpy.pause (.7, hard=True)
    scene c3l27 with dissolve
    mc "Just a second, baby. I'm enjoying this."
    scene c3l28 with sdissolve
    $ renpy.pause (.7, hard=True)
    scene c3l27 with dissolve
    $ renpy.pause (1.2, hard=True)
    scene c3l28 with sdissolve
    $ renpy.pause (.7, hard=True)
    scene c3l27 with dissolve
    mc "(Mm... fuck. If I could just put my tongue inside her right now...)"
    scene c3l28 with sdissolve
    $ renpy.pause (.7, hard=True)
    scene c3l27 with dissolve
    $ renpy.pause (1.2, hard=True)
    scene c3l28 with sdissolve
    $ renpy.pause (.7, hard=True)
    scene c3l27 with dissolve
    mc "(I'm so close I can smell her. Now I just need to taste it.)"
    scene c3l27 with dissolve
    scene c3lb9 with dissolve
    scene c3lb9 with vpunch
    ali "No!"
    scene c3lb10 with qdissolve
    ali "{i}*Sniff*{/i}"
    mc "Oh, [anick]. I'm so sorry. I didn't realize you were feeling embarrassed."
    scene c3lb7 with dissolve
    ali "{i}*Sniff*{/i} No, I'm sorry. I told you that you could look and then I... I..."
    scene c3lb6 with dissolve
    mc "[ali], please don't be sorry. I shouldn't have taken it too far. I really enjoyed it. I'm not upset that you made me stop."
    mc "(God... you'll have to forgive me for corrupting and preying upon this one. I feel like a scumbag, but I'm going to embrace it, enjoy the ride, and hope my soul remains intact.)"
    stop music fadeout 07.0
    scene c3lb5 with dissolve
    mc "Besides..."
    scene c3lb4 with sdissolve
    na "You speak in a playful, reassuring tone."
    mc "Isn't it [mcd] [dau] photoshoot time?"
    scene c3lb3 with qdissolve
    ali "Y-You still want me to model for you now?"
    scene c3lb2 with qdissolve
    mc "Of course I do. Why wouldn't I?"
    scene c3lb1 with dissolve
    ali "Yay! I should get changed now! And I'm sorry I overreacted. I've just been so emotional lately. I don't know what's come over me, [mcd]."
    jump allieposescene

label allieposescene:

    scene c3l16 with fade
    ali "Oh...{w} and [mcd]?"
    scene c3l15 with qdissolve
    mc "Yeah?"
    scene c3l16 with qdissolve
    ali "You can watch me change if you want."
    play music "<loop 0.0>audio/cutting_it_close.ogg" fadein 07.0
    pause (1)
    scene c3l15 with qdissolve
    mc "Not going to say no to that!"
    scene c3l13 with sdissolve
    pause
    scene c3l12 with sdissolve
    pause
    scene c3l11 with sdissolve
    pause
    scene c3l10 with sdissolve
    pause
    scene c3l9 with sdissolve
    pause
    scene c3l8 with sdissolve
    pause
    scene c3l7 with qdissolve
    ali "Do you like the outfit?"
    scene c3l8 with qdissolve
    mc "You look incredible! You're not posting these on Incelgram, though."
    scene c3l7 with qdissolve
    ali "Hehe, okay [mcd]."
    scene c3l8 with qdissolve
    pause (1)
    scene c3l6 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c3l6 with flash
    pause
    scene c3l5 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c3l5 with flash
    pause (1)
    mc "(Holy fuck!)"
    pause
    scene c3l4 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c3l4 with flash
    pause (1)
    mc "(This girl is perfect.)"
    pause
    scene c3l3 with sdissolve
    play sound "audio/sounds/shutter.ogg"
    scene c3l3 with flash
    pause
    scene c3l2 with fade
    ali "That was so much fun, [mcd]. We should do this more often!"
    scene c3l1 with qdissolve
    mc "I had fun, too. And you looked incredible in your outfit!{w} Anyway, I'm off to check on [mad]. Wish me luck!"
    stop music fadeout 07.0
    scene c3l2 with qdissolve
    ali "Have fun with [mnick]... and I hope she is nice to you!"
    ali "Bye, [mcd]!"
    scene c3l1 with qdissolve
    pause (1.3)

label premovie:

    scene black with sdissolve
    $ renpy.pause (3, hard=True)
    scene c3m54 with dissolve
    mc "(So that just happened... my heart is racing. I can't believe it.)"
    mc "(What a ridiculous situation. How do I always get myself into these scenarios?)"
    mc "(The only thing that {i}hasn't{/i} happened yet is one of the girls getting stuck in the washing machine.)"
    mc "(And this confirms it...)"
    mc "(What I feared would happen has happened.)"
    scene c3m53 with sdissolve
    mc "(I'm trying to have sex with my [dau]s. I could hardly restrain myself in there.)"
    mc "(That girl is so innocent. I don't understand.)"
    mc "(I know she's only [age]-years-old, and I know she's a bit simple, but not knowing anything about sex just seems... unbelievable. It really makes me wonder how Gracie raised them.)"
    scene c3m52 with sdissolve
    mc "(I don't mean that in a bad way. There's nothing wrong with being pure hearted. It's just...)"
    mc "(It seems too good to be true.)"
    mc "(I'll use my talk with [mad] to get to the bottom of it. The girls have always struck me as a little sheltered, but I really need to know more about their life from before they came here.)"
    if tbed == True and age <= 16:
        mc "(Not to mention school. Surely, they didn't drop out, did they? Which means I'll need to figure something out this year. I'm also curious what their experience has been so far. They don't seem to have a lot of close friends.)"
    else:
        mc "(Not to mention if they're planning to enroll in college, and what it was like for them in their school years. Oddly, they don't seem to have many close friends and school isn't something they mention much.)"

    mc "(Well, now's as good a time as any to find out. Gives me something to talk about with [mnick], at least.)"
    if maddark == True:
        jump premoviedark
    else:
        jump premovieromance

label premoviedark:

    scene c3m51 with sdissolve
    mc "(Wouldn't be surprised if she's sitting funny after what I did to her last night. And probably quite upset.{w} Serves her right though... and I'll beat her again if she gives me attitude. Let's hope she's learned her place.)"
    mc "(I won't lie, my temper was flaring... and many would argue that what I did was pretty taboo. But do I see it that way? After all, I {i}am{/i} her [car].)"
    mc "(Hm. The better question is...)"
    mc "(Am I just trying to discipline her and change her behavior?)"

    menu:
        mc "(Or did I enjoy hurting her? Assuming she in no way enjoyed it?)"
        "Discipline":
            $ disciplinarian = True
            mc "(No, I'm not a monster. I would never get some sick sense of satisfaction from hurting the poor girl. After all, she just lost her mother, and she's only [age]-years-old. She's not completely at fault for her behavior.)"
            mc "(I think a little discipline, however, is good for her. She clearly has an attitude problem and I'm the only one who can fix it.)"
            mc "(After all, I'm her [car]. It's up to me to make sure she's ready to face the world.)"
            mc "(Walking around believing you can treat people however you want with no consequences is just bad behavior.)"
            mc "(Though I can't deny I lost my temper. I should probably try to go a little easier on her. My hand is still a bit sore.)"
            mc "(For now I'll just play it by ear.)"
        "Enjoyed It":

            $ sadist = True
            mc "(Mm... seeing that plump little ass wiggle with every smack.)"
            mc "(Hearing her squeals, cries, and moans.)"
            mc "(The way she was snotting-up and crying her little eyes out.)"
            mc "(Really put you in your place, didn't I [mad]?)"
            mc "(And let's be real. That went beyond just a disciplinary spank. I really laid into her. My hand is still sore from it.{w} And my cock.)"
            mc "(I could keep hurting her. She doesn't need to enjoy it, so long as I do.)"
            mc "(Does that make me a monster? She's only [age]-years-old and she's going through some heavy shit right now.)"
            mc "(Well, unfortunately for her, it's entirely up to me what I decide since she's under my control now. She's completely mine. I'll make sure there's absolutely nothing she can do. I'll turn her own sisters on her if I have to.)"
            mc "(You fucked with the wrong person, [mad]. And now you have to deal with the consequences until I decide you've had enough.)"
            mc "(...Or until you're completely broken.)"

    scene c3m50 with fade
    mc "(Speak of the devil.)"
    jump moviescene

label premovieromance:

    scene c3m51 with sdissolve
    mc "(We bonded some last night. It wasn't the most in-depth chat, but I clearly got through to her. The poor thing is clearly still very upset and confused about the situation with her mother.)"
    mc "(After my pep talk, she even showed some vulnerability and thanked me. I appreciated that, and it at least shows me she's not completely cold towards me.)"
    mc "(I don't think she's a mean person, I think she's just hurting a lot right now and harbors a lot of resentment.)"
    mc "(Whether I deserve it or not, I don't know... but I can't just invalidate the way she feels. At least there's a good reason for it.)"
    mc "(I can only hope that one of these days, with some persistence, I'll get through to her.)"
    scene c3m50 with fade
    mc "(Speak of the devil.)"

label moviescene:

    scene c3m49 with fadehold
    if maddark == False:
        play music "<loop 0.0>audio/campfire.ogg" fadein 08.0
        jump moviesceneromance
    else:
        play music "<loop 0.0>audio/magnetic_lullaby.ogg" fadein 08.0
        jump moviescenedark

label moviesceneromance:

    mc "Hi, [mad]. Do you mind if I sit down?"
    mad "..."
    scene c3m48 with qdissolve
    mad "Hello. I... I guess not."
    scene c3m47 with fadehold
    mc "Cool."
    scene c3m46 with sdissolve
    mad "Listen... about last night, I..."
    mad "Thank you for trying to cheer me up, [mc]."
    scene c3m45 with qdissolve
    mc "Hey, don't mention it. I don't like to see you sad. I know you girls are going through a lot, and I'm here if you ever need someone to talk to."
    scene c3m44 with sdissolve
    mad "You're not just saying that?"
    scene c3m43 with dissolve
    mc "Of course not..."
    scene c3m42 with fade
    mad "(Maybe he's not so bad...)"
    mc "I know we got off on the wrong foot... but I just want you to like me. We may not have known each other until about a week ago, but I'm your [car]."
    scene c3m41 with qdissolve
    mad "I know. I'm trying... it's just..."
    scene c3m42 with qdissolve
    pause (.7)
    mad "..."
    mad "(No. I shouldn't be so... gullible. I don't even know if we can trust him!)"
    mc "Just what? You can talk to me."
    scene c3m40 with sdissolve
    mad "Just...{w} just shut up, bird breath!"
    scene c3m39 with qdissolve
    mc "({i}Bird breath?{/i} What the hell?)"
    mc "Uh. Sure."
    scene c3m35 with sdissolve
    mc "(I should probably just change the subject. She clearly doesn't like talking about the whole \"[car] [dau]\" thing.)"
    pause (.7)
    jump moviescenechat

label moviescenedark:

    mc "There she is. I need to talk to you. Mind if I sit down?"
    mad "..."
    scene c3m37 with qdissolve
    mad "N-No. I don't mind."
    scene c3m35 with fadehold
    mc "Cool. I see you cleaned the place up. Thanks."
    pause (.6)
    scene c3m36 with qdissolve
    mad "You didn't give me a choice."
    scene c3m35 with qdissolve
    mc "You're right. I did not. Why should someone else have to clean your messes?"
    scene c3m34 with fade
    mad "...I don't know. I guess I was just used to mom cleaning. She always liked doing that kind of stuff. She said it was therapeutic."
    scene c3m33 with qdissolve
    mc "I see."
    scene c3m31 with fade
    mc "Listen, about what happened last night."
    if sadist == True:
        mc "I want to make something very clear. Things are going to change around here. The attitude I got from you when you first arrived is not okay, and I won't allow it."
        mc "But I have a feeling you're going to need more convincing. Which is why what happened last night is just the start of your punishment. You're not finished, yet."
        mc "(Let's see how she reacts to that.)"
        scene c3m32 with qdissolve
        mad "What?! That isn't fair! You told me to clean, and I cleaned! You already punished me! Why would you punish me a second time?"
        scene c3m31 with qdissolve
        mc "What's not fair? That there's consequences for your actions? Typical. That's exactly why I'm going to punish you again... since clearly you don't seem to get it."
        mc "Life isn't fair... and this isn't up for debate. Based on the way you're talking to me right now I clearly didn't get my message across.{w} Besides... it's not like you're being punished for something new. We're just not done with your first punishment."
    else:
        mc "Listen... I just wanted you to know that I didn't enjoy what I did last night. I don't want to hurt you. But there's rules in my house, and if I ask you to do something... you should just do it."
        mc "I'm doing my best for you girls. Giving me attitude, being defiant, and going out of your way to annoy me is not something I can allow."
        mc "I don't want to punish you... but I'll do it again if I have to."

    scene c3m33 with fade
    mad "..."
    if mad_scared >= 1:
        scene c3m34 with qdissolve
        mad "I understand... I-I'll try not to do it again."
        scene c3m33 with qdissolve
    else:
        scene c3m34 with qdissolve
        mad "You can't! It isn't fair and doing that to me wasn't right!"
        scene c3m33 with qdissolve
        mc "{i}*Sigh*{/i} See, that's the attitude that's going to get you into more trouble."
        mad "..."

    stop music fadeout 06.0
    mc "Listen... I didn't come here to argue. So can we just drop it for now?"
    scene c3m34 with qdissolve
    mad "Okay."
    scene c3m35 with fade
    mc "(Well... that went a {i}little{/i} better than I expected, I guess.)"
    play music "<loop 0.0>audio/campfire.ogg" fadein 07.0
    mc "(At least it seems like she got the message. And I'm kind of glad we're not fighting. We can't be hostile towards each other {i}all{/i} the time.)"
    mc "(Plus I still need to get to know her.)"
    jump moviescenechat

label moviescenechat:

    menu movieset:
        set menuset
        "Ask About TV":

            mc "(Let's ask her about the movie.)"
            mc "So... what are you watching?"
            scene c3m30 with sdissolve
            mad "Oh, this is a classic. It's honestly one of my favorites! It's an old movie about this guy who falls in love with his um..."
            scene c3m29 with dissolve
            mad "With his...{w} his tenant!{w=.5} Yes!{w=.5} His younger tenant."
            scene c3m28 with fade
            pause (1)
            tv "{i}I love you, Daddy.{/i}"
            tv "{i}And I love you, my hot little Daughter.{/i}"
            pause (1)
            scene c3m27 with sdissolve
            mc "His tenant calls him Daddy?"
            scene c3m25 with qdissolve
            mad "Um... yeah. I guess so. Maybe we should watch something else..."
            scene c3m27 with qdissolve
            mc "No, it's okay. Don't worry, I was just uh."
            mc "Well, surprised that you're into old movies is all. I guess I didn't take you for a big movie buff."
            scene c3m24 with qdissolve
            mad "You'd be surprised. I absolutely love movies. Though it's a little annoying that all we get lately are superhero movies and remakes. I'm more into um... romance and drama."
            scene c3m23 with qdissolve
            mc "Does your interest go beyond just watching them?"
            scene c3m22 with qdissolve
            mad "It does. Someday I'd love to be an actress. But I don't know if I'd be any good at it. I wasn't in drama class for as long as I would've... liked to be."
            mad "And if things don't work out with acting, I'd love to be a pop and folk singer."
            scene c3m21 with qdissolve
            mc "No way... you can sing?"
            scene c3m22 with qdissolve
            mad "Uh-huh."
            mad "Don't even ask me to sing for you though! It's way too embarrassing!"
            scene c3m15 with dissolve
            mc "Haha. Well, alright. It's just..."
            scene c3m14 with qdissolve
            mad "Just what?"
            scene c3m15 with qdissolve
            mc "Well you see, I happen to be one of the best photographers in the entertainment industry."
            scene c3m14 with qdissolve
            mad "No rubbing it in! Just because I'm not famous like you doesn't mean I'll never be!"
            scene c3m16 with qdissolve
            mc "Heh. Who says I'm rubbing it in? The thing is, being a big timer in the industry comes with certain perks..."
            mc "Perks like... meeting and working with celebrities and famous musicians."
            scene c3m17 with qdissolve
            mad "Oh come on! You're definitely rubbing it in!"
            scene c3m11 with dissolve
            mad "Hmph!"
            scene c3m9 with dissolve
            mad "Wait... so you like... {i}you{/i} know singers and actresses?"
            scene c3m8 with qdissolve
            mc "Quite a few, honestly. Some I'm one-hundred percent sure you've heard of."
            scene c3m7 with qdissolve
            mad "That's so cool..."
            mad "But why you? Are you really that good? Or just lucky?"
            scene c3m8 with qdissolve
            mc "Heh... probably a mix of both."
            scene c3m5 with dissolve
            mad "(He's trying to trick me, isn't he?)"
            mad "Hmph!"
            mc "Listen... if you wanted to tag along sometime, I'd be happy to invite you the next time we book a celebrity shoot."
            scene c3m7 with dissolve
            mad "Y-You'd let me come with you?"
            scene c3m8 with dissolve
            mc "[mad]... I know this is going to sound a little strange to you given our... relationship."
            if maddark == True:
                mc "Especially after what happened last night."

            mc "But you said you wanted to be a singer or an actress someday, didn't you?"
            scene c3m9 with qdissolve
            mad "I would love to... I just... I don't really know what to do."
            scene c3m8 with qdissolve
            mc "Well... we might have our fair share of problems, but you're still my [dau]. I'd love nothing more than to help you fulfill your dreams and aspirations, and I have a feeling that knowing someone inside the industry would be a huge step towards making those dreams come true."
            mc "So it's completely up to you. Just say the words, and I'll see what I can do.{w} I mean... I introduced [ali] to Tiffany Mae didn't I?"
            scene c3m5 with dissolve
            mad "(Why would he want to help me after everything? After I nearly crushed him with my butt and called him a perv?)"
            mad "(Why does he care?!{w} Ugh! He's up to something!)"
            scene c3m14 with dissolve
            mad "What's in it for you?"
            scene c3m15 with qdissolve
            if maddark == True:
                mc "Hm... I don't know. Maybe nothing. We'll see about that when the time comes. What does it matter when you have so much to gain from it?"
                scene c3m9 with qdissolve
                mad "Huh... I guess that's... true."
            else:
                mc "Haha. Nothing. I just want to do something nice for you. Is that so hard to believe?"
                scene c3m9 with qdissolve
                mad "K-Kinda..."

            scene c3m6 with sdissolve
            mad "I'll... think about it."
            scene c3m5 with dissolve
            mc "Good."
            jump movieset
        "Ask About Past":

            mc "(I should find out more about their life before moving here.)"
            if tbed == True and age <= 17:
                scene c3m21 with sdissolve
                mc "So I know it's summertime right now... but aren't you girls still enrolled in school? What was school life like for you back home?"
                scene c3m22 with qdissolve
                mad "I don't know... we just did... normal school stuff for most of our lives. We didn't go to the best schools or anything if that's what you wanted to know. Mainly because mom didn't make a lot of money."
                mad "And the other girls would sometimes pick on me and my sisters... they thought we were weird because we're triplets. But that was mostly grade school when we were still in the same classes together."
                mad "Secondary was a little better because... y'know... we had different classes and stuff."
                scene c3m34 with sdissolve
                mad "But then mom got sick... and everything changed."
                scene c3m33 with qdissolve
                pause (1)
            else:
                scene c3m21 with sdissolve
                mc "So I know it's summertime right now and you girls are [age], but what was school life like growing up? When did you graduate?"
                scene c3m22 with qdissolve
                mad "I don't know... we just did... normal school stuff for most of our lives. We didn't go to the best schools or anything if that's what you wanted to know. Mainly because mom didn't make a lot of money."
                mad "And the other girls would sometimes pick on me and my sisters... they thought we were weird because we're triplets. But that was mostly grade school when we were still in the same classes together. It started to change once we were in middle school."
                scene c3m34 with fade
                mad "High school was a lot better because... y'know... we had different classes and stuff. We weren't in high school for long though. When mom got sick... everything changed."
                scene c3m33 with qdissolve
                pause (1)

            scene c3m34 with qdissolve
            mad "We were so worried about her. We didn't want her to be alone. And she wasn't able to drive us once she started getting chemo. Plus there was no such thing as a bus where we lived."
            mad "For a while, our friend Alita's grandmother was driving us."
            scene c3m17 with sdissolve
            mad "But she's old.{w} Like, really old!{w} She kept turning around to talk to us. I'm talking, completely turning her whole body around while doing ninety down the freeway. We thought she was going to kill us!"
            scene c3m22 with dissolve
            mad "Eventually, things got too complicated. And mom wanted to spend more time with us anyway... so we all agreed it'd be best if we were homeschooled."
            mad "So we dropped out. {w} She thought it'd be bad for us at first and tried talking us out of it, but I wasn't taking no for an answer! And neither were my sisters!"
            scene c3m21 with qdissolve
            mc "(Ah... homeschooling. That actually explains a hell of a lot. And that's really sweet that they were willing to sacrifice their school and social life so they could be with their mother.)"
            mc "I see. That makes sense. Was it hard for her to keep up with your studies during chemo?"
            scene c3m22 with qdissolve
            mad "At first it was really hard. For a while, we weren't even able to do everything. But we made sure to work extra hard when she started feeling better to make up for it."
            scene c3m21 with qdissolve
            mc "I don't know what to say. That's quite the sacrifice... for all of you. I'm glad you were able to spend lots of time with your mom before she..."
            scene c3m33 with sdissolve
            mc "..."
            scene c3m34 with qdissolve
            mad "Y-Yeah. Me too."
            scene c3m21 with sdissolve
            mc "So are you planning to attend college?"
            scene c3m22 with qdissolve
            mad "Oh, God. I don't know... I don't even want to think about that right now!"
            scene c3m14 with dissolve
            mad "You're not planning to force us, are you? You can't make me! And I won't let you force [anick] or [onick] either!"
            scene c3m15 with qdissolve
            mc "Whoa, slow down there. I wasn't going to force anything, I was just wondering what {i}you{/i} wanted, that's all."
            scene c3m17 with dissolve
            mad "O-Oh.{w} Sorry..."
            scene c3m21 with dissolve
            if tbed == True:
                mc "(The more I think about it the more it makes sense. Their cluelessness surrounding sexuality, their lack of interest in \"boys,\" the fact that they don't seem to have any close friends. Well, except that one girl they always mention. Alita.)"
            else:
                mc "(The more I think about it the more it makes sense. Their cluelessness surrounding sexuality, their lack of interest in \"guys.\" They wouldn't know many people their age if they skipped high school. Well, at least they seem close with that one girl they always mention. Alita.)"

            scene c3m20 with sdissolve
            mc "(Actually, based on what I saw the other night, I'd say this girl struggles to even masturbate.)"
            mc "(Well...{w} all coming together now.)"
            jump movieset
        "Ask About Romance":

            scene c3m21 with sdissolve
            mc "So uh... any romance in your life? Ever had a boyfriend?"
            scene c3m22 with qdissolve
            mad "Huh? Why would you want to know about that?"
            scene c3m21 with qdissolve
            mad "(Isn't asking such questions considered flirting? I knew this guy was a perv!)"
            mc "Just curious."
            mad "(I knew it!)"
            scene c3m11 with sdissolve
            mad "Hmph!"
            scene c3m13 with qdissolve
            mad "No, I don't have a boyfriend if you must know!"
            scene c3m11 with qdissolve
            mc "(Huh? Why is she being defensive about it?)"
            mc "Well I figured that... but have you ever dated? Any old flings from back home?"
            scene c3m13 with qdissolve
            mad "Hell no! The guys in my town were all hillbillies and weirdos!"
            scene c3m6 with dissolve
            mad "And even if I wanted to date someone, which I didn't, it's not like we had a lot of opportunities. With everything happening with mom..."
            scene c3m5 with qdissolve
            mc "No, I understand. That makes a lot of sense. What about your sisters?"
            scene c3m4 with dissolve
            mad "Gross!"
            scene c3m3 with qdissolve
            mc "Huh? I'm confused."
            scene c3m4 with qdissolve
            mad "Nothing... nevermind. My sisters haven't had boyfriends either. There's more important things in life than romance and screwing, you know!"
            scene c3m3 with qdissolve
            mc "Whoa. I didn't say anything about \"screwing.\""
            scene c3m4 with qdissolve
            mad "No, but you thought about it!"
            scene c3m3 with qdissolve
            mc "What?"
            scene c3m4 with qdissolve
            mad "Nevermind."
            scene c3m3 with qdissolve
            mad "(I'm onto you, Mister Seducer.)"
            mc "Okay..."
            scene c3m20 with sdissolve
            mc "(Well... I can't be mad at that answer. In fact I'm quite thrilled about it. Even the thought of them \"dating around\" or seeing guys makes my blood boil. Never would've taken myself for the protective [car] type.)"
            mc "(Actually, who am I kidding? If a guy even so much as came near them I'd skin him alive and turn him into a sports coat. [age]-year-old [dau]s with no interest in boyfriends is every [car]'s dream.)"
            mc "(As much as I'd like to ask if they're virgins, I think that'd be way too creepy and I think I have my answer. I was already getting virgin vibes. Now I know they're virgins.)"
            jump movieset

    stop music fadeout 07.0
    jump shower_scene

label shower_scene:

    scene c3m23 with sdissolve
    na "You sit mostly in silence and finish watching the movie, sharing the occasional laugh about it. For the first time, you feel satisfied that your time spent with [mnick] was fulfilling and you grew a little closer."
    scene c3m1 with fadehold
    mad "Well, goodnight. Um... thanks for, you know... joining me for the movie."
    scene c3n30 with ssdissolve
    na "And you find yourself left with a quiet house once more."
    pause (1)
    mc "{i}*Yawn*{/i}"
    mc "(Guess I should hit the hay too. Big day tomorrow... unless the girls tell me they're not interested in doing anything. But who doesn't like a good road trip?)"
    scene black with sdissolve
    $ renpy.pause (3, hard=True)
    $ renpy.sound.play("audio/sounds/shower.ogg", channel='Chan4', loop=True)
    scene c3n29 with sdissolve
    na "As you're heading to your room, you can't help but notice the sound of running water."
    pause (1)
    mc "(Hm...)"
    mc "(I'm pretty sure [ali]'s still in her room. Probably sleeping. And I doubt [onick]'s in there given how she's feeling. She's most likely still resting.)"
    mc "(Which leaves...)"
    scene c3n28 with fade
    mc "([mnick].)"
    mc ".{w}.{w}."
    menu:
        mc "(Am I really considering this? Spying on my own [dau] while she's in the shower?)"
        "Let's Do This":
            $ lust +=1
            scene c3n27 with sdissolve
            mc "(Yes.{w} Yes I am considering spying on my own [dau] while she's showering. I'm only human.)"
            mc "(I'm a man. I make mistakes.)"
            scene c3n23 with sdissolve
            mc "(Unlocked. Lucky.)"
            mc "(Slowly now. Don't blow your cover. Knowing her she'd have me arrested.)"
            scene c3n22 with fadehold
            pause
            if maddark == True:
                mc "(Fuck me... there's that beautiful ass again.)"
                scene c3n21 with fade
                pause
                mc "(Seeing it now that I'm no longer pissed at her... it's a wonder I was even able to restrain myself last night. That is possibly the most incredible ass I've ever laid eyes on.)"
                mc "(Shit, I'm getting horny.)"
                mc "(I'm not going to risk getting caught. This isn't a movie. She already called me a pervert.)"
                pause
                scene c3n23 with sdissolve
                mc "(Just need to close this slowly...)"
                scene c3n25 with sdissolve
                $ renpy.music.stop(channel='Chan4', fadeout=1.0)
                stop sound fadeout 02.0
                mc "(Whew! That was a rush. Time to get the fuck out of here!)"
            else:
                mc "(?!)"
                mc "(No fucking way.)"
                scene c3n21 with fade
                pause
                mc "(Well I'll be fucked for a nanny goat! That ass is out of this world. How is she even human?)"
                mc "(At least now I know why she's so smug.{w} I'd be cocky too if I grew an ass that could entice Jesus.)"
                mc "(Shit, I'm getting horny.)"
                mc "(I'm not going to risk getting caught. This isn't a movie. She already called me a pervert.)"
                pause
                scene c3n23 with sdissolve
                mc "(Just need to close this slowly...)"
                scene c3n25 with sdissolve
                $ renpy.music.stop(channel='Chan4', fadeout=1.0)
                stop sound fadeout 02.0
                mc "(Whew! That was a rush. Time to get the fuck out of here!)"
                scene c3n24 with sfade
                mc "(Would be tragic if she noticed me. Know her she'd press charges.)"
                jump after_movie_night
        "Don't Do It":

            $ pure +=1
            mc "(Nah. That's a little too creepy even for a degenerate like me.)"
            mc "(Not to mention incredibly cliché.)"
            scene c3n25 with sdissolve
            mc "(As much as it hurts to deprive myself of what is no doubt a glorious view of my [dau], I'm trying really hard to resist temptation and do the right thing.)"
            $ renpy.music.stop(channel='Chan4', fadeout=1.0)
            stop sound fadeout 02.0
            scene c3n24 with sfade
            mc "(Here's to hoping it pays off and [mnick] realizes I'm someone she can trust.)"
            jump after_movie_night
        "Mess With Her":

            $ dark +=1
            mc "(Well, the alternative to spying won't net me any new material for the spank bank... but it'll sure as fuck make for a good laugh.)"
            scene c3n27 with dissolve
            mc "(I'm a simple guy. Not every prank needs to be... elaborate.)"
            pause (1)
            mc "(Three...{w} two...{w} one...)"
            play sound "audio/sounds/doorslam.ogg"
            pause (.5)
            scene c3n26 with xdissolve
            scene c3n26 with vpunch
            mc "(Blastoff!)"
            scene c3n27 with dissolve
            mad "{size=+10}{i}Ahhh!{w=1} What the hell was that?!{w=1} [onick]?!{/i}{/size}"
            mc "(...Better run!)"
            scene c3n25 with sdissolve
            mc "Kekekeke!"
            $ renpy.music.stop(channel='Chan4', fadeout=1.0)
            stop sound fadeout 02.0
            scene c3n24 with fadehold
            mc "(Whew. What a rush. I'm glad I got out of there in time!)"
            mc "(Oh man. I can't stop giggling like a schoolgirl. I'm way too immature for my age.)"
            mc "..."
            mc "(She hasn't barged through my door just yet so she probably doesn't suspect me. Mission accomplished. Here's to hoping I didn't scare her so bad that she shit on the bathroom floor.)"
            jump after_movie_night

label after_movie_night:

    play music "audio/neither_sweat_nor_tears.ogg" fadein 12.0
    scene c2j31 with fadehold
    mc "{i}*Yawn*{/i}"
    mc "(Got a lot done today. Dropped off my files from the photoshoot with Tiffany.)"
    if cc8 or cc9 == True:
        mc "(Sort of got a date with Mira.)"

    if liv_kissed == True:
        mc "(Also... I can't believe I just made out with [liv] again. And that she confessed to having feelings for me.)"

    mc "(Quite brave of her to open up to her own [car] about the way she's feeling. For many, [onick] would be the perfect girl. Can I really complain?)"
    mc "(And she reminds me so much of Gracie, weird as it is to say. I can't rule out the fact that I've been \"seeing\" her mom in my dreams for almost a decade.)"
    mc "(Not only does she look like her, she acts like her as well. And I'd be lying if I said I don't have real feelings for Gracie... even if I've only ever met her in my dreams.)"
    mc "(I don't know what to make of this situation. Could I be in over my head? It's no small thing to romance your own [dau]. It could come with some serious consequences. Consequences I don't think she has even considered.)"
    mc "(And things are moving so fast.)"
    mc "(No sense panicking about it now. It's too late for that. I just need to remain calm and take it in stride.)"
    mc "(I've made my bed, and if shit hits the fan, I'll need to lay in it.)"
    mc "(What could potentially complicate things is my relationship with [ali], also.)"
    mc "(Especially after what happened in her room earlier. While in her mind what happened between us was harmless, I doubt someone else would see it that way. And I've gotten really close with her as well.)"
    if brk_rel == True:
        mc "(Not to mention Brooke too! Fuck.)"
        mc "(Am I really doing this? Am I really going to romance several women, including my employee and my own [dau]s?!)"
    else:
        mc "(Am I really going down a path of romance with more than one of my own [dau]s?)"

    mc "(Actually, the more I think about it, the less that sounds like a \"bad\" thing. Just hard to believe considering I was a bachelor not even a week ago.)"
    mc "(Well, here's to hoping it...)"
    scene c2j30 with dissolve
    mc "{i}*Yawn*{/i}"
    mc "(Works out...)"
    scene black with sdissolve
    stop music fadeout 06.0
    pause (1)
    na "Before you know it, you fade into a restful sleep."
    $ renpy.pause (3, hard=True)

label roadtrip_morning:

    scene c2j27 with sdissolve
    mc "(Mm... feels good to not wake up to that damn alarm for once.)"
    mc "(Today's a big day! I should talk to the girls right away.)"
    scene c3n20 with sdissolve
    mc "(Better check my phone first.)"
    scene c3n19 with dissolve
    if van_romance == False and van_friends == False:
        mc "(Hm... new message. Looks like it's from Brooklyn.)"
    else:
        mc "(Hm... two messages. One's from Brooklyn, but I don't recognize that other number. Spam maybe? Let's see what Brooke said.)"

    scene c3n18 with dissolve
    pause (1)
    "{i}Good morning! Sorry I haven't messaged or called sooner. Especially after our date. I really had fun and have been meaning to thank you.{/i}"
    "{i}So I know this is a big request seeing as you're on vacation, but if it's not too much trouble I was wondering if we could meet briefly today for coffee?{/i}"
    "{i}I promise I wouldn't ask if it's not important. There's just something that's been bugging me, and I was wanting to tell you how the gig went as well.{/i}"
    "{i}Please feel free to say no.{/i}"
    scene c3n17 with dissolve
    "{i}Actually, disregard this message! I don't know what's wrong with me texting you out of the blue asking for stuff! You're probably so busy right now! Jeez.{/i}"
    "{i}Sorry!{/i}"
    "{i}Also sorry for bombarding you with all of these messages. Last one, I promise.{/i}"
    pause (1)
    mc "(Haha. I see Brooke is still acting like... Brooke.)"
    if brk_rel == True:
        mc "(It's actually nice to hear from her after our date the other night. We haven't spoken since that kiss we shared. She ducked out pretty quickly after.)"
    else:
        mc "(It's actually nice to hear from her, especially after that weird turn our date took the other night. I still feel bad about rejecting her and hope she's not upset with me. I may not be romantically interested, but we can still be friendly with each other.)"

    mc "(It would also be nice to see her again... though I have big plans this afternoon so meeting for coffee is not an option. Maybe I can swing by her place really quick if I leave now?"
    scene c3n16 with fadehold
    mc "(I'd better call her.)"
    scene c3n15 with fadehold
    play music "<loop 0.0>audio/just_stay.ogg" fadein 10.0
    brk "(Oh crap, it's [mc]! I wasn't expecting him to call.)"
    brk "{i}*Clears throat.*{/i}"
    scene c3n14 with sdissolve
    brk "Y-Yes? Brooklyn speaking."
    scene c3n13 with qdissolve
    brk "(Ugh! What a stupid way to answer. Of course he knows it's me speaking. He just called me!)"
    mc "{i}Hey, Brooke! Glad I was able to get in touch with you.{/i}"
    scene c3n14 with qdissolve
    brk "Oh yes. Did you get the texts I sent you?"
    scene c3n13 with qdissolve
    mc "{i}I did. That's actually why I'm calling.{/i}"
    mc "{i}I'd love to meet with you today, but there's a problem. I have plans this afternoon, early evening at the latest, so I won't have time to meet for coffee.{/i}"
    scene c3n12 with qdissolve
    brk "Shit!"
    brk "Oh! I mean—that's alright! I thought you might be busy, so it's no problem."
    scene c3n13 with qdissolve
    brk "(Fuck! I need to learn to not just blurt out the first thing that comes to mind.)"
    mc "{i}Well actually, I'm not busy right now, so I was thinking maybe I could come by and talk to you at your place?{/i}"
    scene c3n12 with qdissolve
    brk "Oh.{w} Oh! You mean now? As in right this instant?"
    scene c3n11 with qdissolve
    mc "{i}Haha. Yeah. It would sort of have to be now if I'm going to have time to meet at all.{/i}"
    scene c3n12 with qdissolve
    brk "Um... sure! I think that would work out just fine. Do you remember where I live?"
    scene c3n11 with qdissolve
    mc "{i}Yup! I remember.{/i}"
    scene c3n12 with qdissolve
    brk "Great. Um... about how long would it take you to get here? I just got out of the shower."
    scene c3n11 with qdissolve
    mc "{i}Hm... I'd say I could be there in about an hour? Would that work for you?{/i}"
    scene c3n12 with qdissolve
    brk "That should be perfect! And thank you so much for agreeing to meet up. I, uh, I was sad to not see you at the office at all yesterday. And there's some things I was hoping to talk to you about."
    scene c3n11 with qdissolve
    mc "{i}(Aw. That's pretty sweet of her to say. Glad she's opening up.){/i}"
    mc "{i}I was sad to not see you yesterday as well. It was nice to see a message from you this morning though.{/i}"
    mc "{i}So... see you soon?{/i}"
    scene c3n12 with qdissolve
    brk "Perfect! I'll be here. Bye, [mc]!"
    scene c3n10 with fade
    mc "{i}Bye!{/i}"
    scene c3n9 with fadehold
    mc "(Definitely going to be wearing a lot of cologne for this meetup.)"
    if van_romance == True:
        mc "(I haven't had the chance to shower since {i}before{/i} I was balls deep in Vanessa, and I probably don't have time now either.)"
    else:
        mc "(I haven't had a proper shower in two days, and I probably don't have time now. I still need to talk to the girls before I go to make sure they don't leave while I'm gone... not to mention figure out what the four of us are going to do while I have time off.)"

    mc "(I still need to talk to the girls before I go... to make sure they don't leave while I'm gone... not to mention figure out what the four of us are going to do while I have time off.)"
    mc "(Don't think I'll ever get used to having three girls hogging the showers. Are they ever {i}not{/i} showering?! My water bill's going to be more than my mortgage this month.)"
    mc "(Fuck it. I'll just hop in later. I'm almost used to it at this point.)"

    if van_romance == True:
        mc "(Now let's see what this other message is about.)"
        scene c3n8 with sdissolve
        mc "(Oh, this one came through last night.)"
        pause (1)
        "{i}u up?{/i}"
        "{i}Just kidding. Haha! Not sure if you remember me, but I was that annoying waitress who served your table at the restaurant.{/i}"
        "{i}My name's Vanessa by the way. In case you forgot.{/i}"
        "{i}I think I owe you... an apology. Or an explanation. Or maybe something else?{/i}"
        "{i}I know you probably think I'm crazy after what happened between us. And I have some explaining to do.{/i}"
        "{i}But if you give me a chance, I'll make it worth your while.{/i}"
        pause (1)

    elif van_friends == True:
        mc "(Now let's see what this other message is about.)"
        scene c3n7 with sdissolve
        mc "(Oh, this one came through last night.)"
        pause (1)
        "{i}u up?{/i}"
        "{i}Just kidding. Haha! I'm not sure if you remember me, but I'm that crazy waitress who threw herself at you and was promptly turned down...{/i}"
        "{i}For some strange reason you still exchanged numbers, so I'm giving this a shot.{/i}"
        "{i}My name's Vanessa by the way. In case you forgot.{/i}"
        "{i}First of all, I wanted to say thank you. I know that sounds strange coming from me, but I was in a bad place that night, and you stopped me from doing something I would've felt pretty stupid about. I don't think many guys would do the same in your position.{/i}"
        scene c3n6 with dissolve
        "{i}I think I owe you... and apology. Or an explanation. Or maybe something else?{/i}"
        "{i}Either way, I have some explaining to do.{/i}"
        "{i}If you give me a chance, I'll owe you one. The truth is... I just really need someone to talk to.{/i}"
        pause (1)
    else:

        stop music fadeout 04.0
        jump after_phonecalls

    if van_romance == False:
        mc "(Oh. It's that waitress who tried to sexually assault me in the bathroom. That's right... I forgot we still exchanged numbers.)"
    elif van_romance == True:
        mc "(Oh, it's the waitress I fucked. That's right. We exchanged numbers in the bathroom.)"
    else:
        pass

    mc "(Well shit. It sounds like she wants to meet up. And here I just went through the same thing with Brooke.)"
    scene c3n9 with sdissolve
    mc "(Hm...)"
    mc "(I'm not sure how much I trust her just yet. She's definitely mysterious, and I'd be lying if I said I wasn't wondering what her deal was that night.)"
    mc "(I guess I could always meet her at the park by Brooke's place. I'll be able to squeeze in a quick meetup without missing out on anything else. It wouldn't hurt to hear her out.)"
    mc "(Or... I could do something else. But I may ruin any future chances with her. It sounds like this is important to her.)"
    scene c3n9 with purpflash
    scene c3n9 with purpflash
    scene c3n9 with purpflash
    menu:
        mc "(I think it's a solid plan. It sounds like she {i}just{/i} wants to talk so I will have more than enough time.)"
        "Meet Vanessa":
            $ lust +=3
            $ cc7 = True
            scene c3n5 with sdissolve
            mc "(Let me just call her and set up the meeting.)"
            scene c3n4 with fadehold
            $ renpy.pause (.7, hard=True)
            scene c3n3 with qdissolve
            pause (1)
            scene c3n2 with sdissolve
            van "Hello?"
            scene c3n1 with qdissolve
            mc "{i}Hey Vanessa. It's [mc]. I got your texts.{/i}"
            scene c3n2 with qdissolve
            van "Hi, [mc]! I was pleasantly surprised by your call. To be honest I wasn't sure if you'd get back to me or not."
            scene c3n1 with qdissolve
            mc "{i}Well I'll be honest. I do have a pretty busy day ahead.{/i}"
            scene c3n2 with qdissolve
            van "Shit! I hope I'm not interrupting something important."
            scene c3n1 with qdissolve
            mc "{i}Nope. Not yet anyway! I just climbed out of bed.{/i}"
            mc "{i}That said, there's only a small window where I'll be able to meet you today. Would you be able to meet me in the city park in about two hours?{/i}"
            scene c3n2 with qdissolve
            van "Well I'm currently sprawled out in my undies... but I might be able to fit it into my busy schedule."
            scene c3n1 with qdissolve
            mc "{i}Haha, alright. How about I text you when I'm heading that way?{/i}"
            scene c3n2 with qdissolve
            van "That sounds good to me! Oh, and [mc]?"
            van "Thank you for this. It means a lot that you called. You can't see me right now but I'm literally smiling from ear to ear like an idiot."
            stop music fadeout 06.0
            scene c3n1 with qdissolve
            mc "{i}You don't have to thank me! See you soon, okay?{/i}"
            scene c3n2 with qdissolve
            van "Bye, [mc]!"
            jump after_phonecalls
        "Turn Her Down":

            $ pure +=3
            mc "(No, I really don't think I'm interested in having a fuck-buddy, and I don't know if Vanessa is the kind of girl I can romance. If this ruins my chances with her, so be it.)"
            if brk_rel == True:
                mc "(I'm already seeing Brooke, and it just wouldn't be right to continue this side-fling.)"
            scene c3n5 with sdissolve
            mc "(Let me just quickly call her and let her know.)"
            scene c3n4 with fadehold
            $ renpy.pause (.7, hard=True)
            scene c3n3 with qdissolve
            pause (1)
            scene c3n2 with sdissolve
            van "Hello?"
            scene c3n1 with qdissolve
            mc "{i}Hey Vanessa. It's [mc]. I got your texts.{/i}"
            scene c3n2 with qdissolve
            van "Oh hey, [mc]! Thanks for getting back to me. How are you?"
            scene c3n1 with qdissolve
            mc "{i}I'm quite alright. Busy day ahead, though.{/i}"
            scene c3n2 with qdissolve
            van "Oh... bummer. Anything exciting planned?"
            scene c3n1 with qdissolve
            mc "{i}Well, nothing concrete just yet but I'm off for a few days so I'd like to do something with my [dau]s.{/i}"
            scene c3n2 with qdissolve
            van "Awe, that's really sweet. I had no idea you were a [car]."
            scene c3n1 with qdissolve
            mc "{i}Neither did I to be honest.{/i}"
            scene c3n2 with qdissolve
            van "Huh?"
            scene c3n1 with qdissolve
            mc "{i}Nevermind. Listen...{/i}"
            mc "{i}I know you said you needed to talk to me in person, but I don't think I'll be able to meet with you today. I have a lot on my plate already as it is.{/i}"
            scene c3n2 with qdissolve
            van "No, that's totally cool. I understand completely. I'm just grateful that you called. I was feeling quite embarrassed about the other night, and well..."
            van "Well, nevermind. It's stupid. I guess I was just hoping to explain myself. Anyway, you said you're busy, so I won't keep you. Thank you for calling me though, [mc]. It means a lot."
            scene c3n1 with qdissolve
            mc "{i}No problem. Have a good day, Vanessa.{/i}"
            stop music fadeout 06.0
            scene c3n2 with qdissolve
            van "You too, [mc]. Maybe I'll see you around."
            scene c3n1 with qdissolve
            mc "{i}Maybe so. Talk later. Bye!{/i}"
            jump after_phonecalls
        "Cruel Prank":

            $ dark +=3
            $ cruel_prank = True
            stop music fadeout 07.0
            mc "(No. I'm not interested in this girl.)"
            if van_romance == True:
                mc "(People like her are for pumping, dumping, and not much else.)"

            mc "(That of course doesn't mean I can't have a little fun with this, however.)"
            scene c3n5 with sdissolve
            mc "(Fuck it. Let's ruin this girl's whole day.)"
            scene c3n4 with fadehold
            $ renpy.pause (.7, hard=True)
            scene c3n3 with qdissolve
            pause (1)
            scene c3n2 with sdissolve
            van "Hello?"
            scene c3n1 with qdissolve
            mc "{i}Hey, Vanessa! I'm really glad you reached out.{/i}"
            scene c3n2 with qdissolve
            van "Hi, [mc]! I was pleasantly surprised by your call."
            scene c3n1 with qdissolve
            mc "{i}Yeah, I was actually just thinking about you. Then I saw your message...{/i}"
            scene c3n2 with qdissolve
            van "Awe. That's sweet. I'm glad you didn't forget about me."
            scene c3n1 with qdissolve
            mc "{i}So listen... I'd love to meetup with you. That said I'll be busy for most of the day.{/i}"
            mc "{i}I'm free later this evening, though. Would you be interested in maybe getting dinner with me?{/i}"
            scene c3n2 with qdissolve
            if van_romance == True:
                van "That would be awesome! I wish you could see my face right now. I'm literally smiling from ear to ear! Look at you... being all sweet and offering to take a girl out after a one-night stand."
            else:
                van "That would be awesome! I wish you could see my face right now. I'm literally smiling from ear to ear! Look at you... being all sweet and offering to take a girl out after she made herself look like an idiot!"

            scene c3n1 with qdissolve
            mc "{i}Heh... well I'd be stupid not to. You seem like a really cool person, and I'd like to get to know you better. By the way, dinner's on me, but you'll have to meet me at the restaurant as I'll be cutting things close. Don't be surprised if I'm a few minutes late.{/i}"
            mc "{i}Will eight o'clock work for you?{/i}"
            scene c3n2 with qdissolve
            van "I'm free at eight!"
            scene c3n1 with qdissolve
            mc "{i}Awesome. I'll text you the name of the place and meet you there at eight tonight!{/i}"
            mc "{i}Oh, and make sure you wear something nice, okay? It's a rather expensive place. I think they have a dress code.{/i}"
            scene c3n2 with qdissolve
            van "Wow! Now you've got me super excited! I'm so happy you called, [mc]. I'm not sure why you're being so nice to me, but I'm really looking forward to seeing you and I'm also eager to explain why I acted the way I did last night. I've been feeling so lonely, I..."
            van "It'll be nice to put on a dress for once. It's been so long since I've had an excuse to doll myself up!"
            van "Thanks, [mc]."
            scene c3n1 with qdissolve
            stop music fadeout 06.0
            mc "{i}No problem. Texting you the place now. See you!{/i}"
            scene c3n2 with qdissolve
            van "Bye!"
            jump after_phonecalls

label after_phonecalls:

    scene black with sdissolve
    if cruel_prank == True:
        na "You quickly send her the address to an expensive restaurant just outside of town."
        scene c3n9 with sdissolve
        mc "(Wow. That was a little mean even for me.)"
        mc "(Serves her right, though. Have fun eating alone tonight, slut!)"
        mc "(Alright. I'd better dress myself and get going.)"
    else:
        pause (1)
        mc "(Alright. I'd better dress myself and get going.)"

    play music "audio/summer_love.ogg" fadein 08.0
    scene black with sdissolve
    pause (3)
    scene c3o21 with dissolve
    mc "Good morning, girls!"
    scene c3o20 with qdissolve
    grls "Good morning, [mcd]!"
    scene c3o21 with qdissolve
    mc "You feeling better today, [onick]? You look better."
    scene c3o19 with qdissolve
    liv "Yes! Whatever it was it seems it wasn't serious. I feel okay this morning."
    scene c3o21 with qdissolve
    mc "That's good to hear. I'm glad we're all back to normal."
    mc "Which leads me to something I need to talk to you three about..."
    mc "I've taken the next few days off work. If you girls are going to live with me from now on, we should all get to know each other."
    scene c3o17 with dissolve
    mc "I know the three of you just arrived not long ago, but I'll be honest. I'm pretty desperate to get out of this house and go do something while I have time off."
    scene c3o16 with dissolve
    ali "You mean like a road trip?!"
    scene c3o14 with dissolve
    mc "Exactly."
    scene c3o15 with dissolve
    liv "Wow! Where did you want to go?"
    scene c3o14 with dissolve
    mc "Well actually..."
    mc "I thought it'd be a good idea to leave that up to you girls. If we could go anywhere or do anything in the country for a few days... what would the three of you want?"
    mc "Take a minute to think about it and let me know what you come up with."
    pause (1)
    scene c3o13 with sdissolve
    pause (1)
    scene c3o12 with dissolve
    grls "{i}Mom...{/i}"
    scene c3o11 with sdissolve
    liv "[omc], I-I know it hasn't been very long...{w} and it probably doesn't sound very fun...{w} b-but the three of us would love the chance to... you know... see mom."
    liv "She was buried at the Oakwood Cemetery back home..."
    scene c3o10 with qdissolve
    mc "(Wow. That's... not exactly what I was expecting when I told them we could go anywhere they want.{w} B-But it makes sense. The girls really loved their mother.)"
    mc "(Oakwood Cemetery... I know the place. That's where my own parents are buried. It's not that far from my old home.)"
    scene c3o9 with dissolve
    ali "Please [mcd]. We'd really like to go see her."
    scene c3o8 with dissolve
    mc "(Well... I think we can make this work. It would be a good opportunity for us to bond...)"
    mc "(And it's not like I could say no to those faces.)"
    mc "(I have an idea.)"
    mc "No worries, girls. I meant it when I said we can go anywhere you want."
    scene c3o7 with dissolve
    mc "In fact... this could turn out to be a really nice trip. I know of the cemetery you mentioned, [onick]. Not far from there, there's a really nice lake with an old rental house."
    mc "We could go visit your mom when we arrive, then spend the next few days at the lake house."
    scene c3o6 with dissolve
    liv "When will we leave?"
    scene c3o5 with dissolve
    mc "How's this afternoon sound? It's all very last minute, but I shouldn't have trouble booking the lake house. It'll be a long drive, but we should be there by tomorrow."
    mc "(When I planned this trip... I didn't think I'd be heading back to my old hometown.)"
    mc "(This... should be fun.)"
    scene c3o4 with sdissolve
    mad "Yay! This is going to be awesome!"
    mad "Come on, [ali]! Let's go get ready!"
    scene c3o3 with fadehold
    liv "Thank you, thank you, thank you!"
    scene c3o2 with qdissolve
    mc "You're welcome. I just want us to have a good time."
    mc "By the way... I need to head out for a bit before we go, but I'll be back in a couple of hours. Think you'll be ready to go by then?"
    scene c3o3 with qdissolve
    liv "Yup! We'll be waiting! Now go! I'll see you when you get back."
    scene c3o1 with ssdissolve
    pause (1)
    na "And just like that, she scurries off... squealing excitedly for the upcoming trip."
    mc "(Heh. That went better than expected. These girls are a riot.)"
    mc "(Alright. Time to head out! I shouldn't waste too much time.)"

label rachel_meeting:

    scene c3p25 with fadehold
    mc "Ahh. What a day."
    mc "(Perfect weather for a long drive. Should be clear skies when we leave this afternoon. Got a long drive ahead of us.)"
    scene c3p24 with sdissolve
    mc "(I can't believe I'm going back home. It's been years. It will be nice to visit mom and dad at the old graveyard again.)"
    mc "(I'll get to see Gracie's burial site too. That's going to be... surreal. But I'm happy for the opportunity to pay my respects.)"
    stop music fadeout 07.0
    mc "(Feels weird to be heading back there with the girls considering they just came all this way. But I understand them wanting to visit their mom's grave again. It's all so recent. Hopefully it will be a therapeutic experience for them.)"
    scene c2m27 with fadehold
    mc "(Alright, no time to waste. Time to head over to see Brooke.){nw=3}"
    play sound "audio/sounds/scare.ogg"
    scene c3p23 with vpunch
    rac "Morning, [mc]."
    scene c3p22 with qdissolve
    mc "{size=+5}{i}Wahhh!!! Who the fuck are you?!{/i}{/size}"
    pause (1)
    mc "Wait a minute... you're..."
    mc "My neighbor?{w} You're Glenn's wife... aren't you?!"
    scene c3p21 with dissolve
    play music "<loop 0.0>audio/take_me_to_the_depths.ogg" fadein 12.0
    rac "Shh...!"
    scene c3p20 with dissolve
    rac "We have to be quiet! He can't know that I'm speaking to you."
    scene c3p19 with qdissolve
    mc "Wait, what? How the fuck did you get into my car, woman?! You scared the living shit out of me!"
    scene c3p18 with dissolve
    rac "I know, I know! I'm sorry. Just please, try not to yell anymore. If he finds me here, I'll never hear the end of it. He's in the garage playing with his tools."
    rac "I'm sorry for sneaking up on you, [mc], but I needed to speak with you privately... and without Glenn knowing."
    scene c3p17 with qdissolve
    mc "Can it not wait?! Could you not have just waited until he was at work or something? I'm not trying to be rude, but you nearly gave me a heart attack by sneaking around, crazy lady!"
    scene c3p15 with dissolve
    rac "..."
    mc "Ok... sorry. That was kind of rude. I don't think I've gotten your name, Miss..."
    scene c3p16 with qdissolve
    rac "It's Rachel. And look, I get it. I know this isn't ideal, but I had to sneak off while I had the chance, and I can't risk Glenn seeing me with you."
    scene c3p15 with qdissolve
    mc "Um... nice to meet you, Rachel. I'm [mc]."
    scene c3p16 with qdissolve
    rac "I know. Glenn told me. He's grown quite the obsession with you lately, and I'm not entirely sure what's caused it."
    scene c3p15 with qdissolve
    mc "Why? What the hell did I ever do to him?"
    scene c3p16 with qdissolve
    rac "To be frank I was hoping {i}you{/i} could tell {i}me.{/i} But it seems you're just as in the dark as I am."
    rac "Listen, to answer your question... no this couldn't wait. I needed to talk to you before, um... before it was too late."
    scene c3p15 with qdissolve
    mc "Too late? Is that psycho planning to murder me or something?"
    scene c3p14 with dissolve
    rac "{i}*Sigh*{/i}"
    scene c3p13 with qdissolve
    rac "No, he's not going to murder you.{w} The other night I caught Glenn spying on you while you were out by the pool."
    rac "Well... he doesn't know that I caught him. I slipped away before he could notice me."
    scene c3p12 with qdissolve
    mc "(What the fuck?! What's this guy's deal? He's spying on me and my [dau]s?)"
    scene c3p11 with dissolve
    rac "He wasn't just snooping. He was recording you."
    scene c3p10 with qdissolve
    mc "..."
    mc "Are you kidding me?"
    scene c3p11 with qdissolve
    rac "Unfortunately not. When he was finished with the recorder I had a quick snoop through it..."
    rac "He has footage of you making out with a young woman... and I think he's planning to use it against you somehow."
    scene c3p10 with qdissolve
    mc "This has got to be some sort of joke. Recording someone when they're on their own damn property can't be legal. And it's not like I've done something wrong."
    scene c3p11 with qdissolve
    rac "I don't think it is, however, Glenn isn't stupid. One way or another, he could likely find a way to use said recording to trap you. Unfortunately for you he's got a lot of connections and friends in high places."
    rac "He's not exactly your average policeman. He used to work for the FBI, for instance, and he has a lot of power and influence."
    scene c3p10 with qdissolve
    mc "(Oh for fuck's sake.)"
    mc "Wait..."
    mc "Why are you telling me this?"
    scene c3p9 with qdissolve
    rac ".{w}.{w}."
    scene c3p8 with qdissolve
    rac "I know it's strange..."
    rac "But I want to help you."
    rac "Let's just say, our marriage isn't doing well. Things have been going downhill for a while now."
    scene c3p9 with qdissolve
    mc "That still doesn't explain why you'd betray your husband."
    scene c3p7 with qdissolve
    rac "Betray him?! He hasn't been himself for more than a year! When he's not at work, all he ever does is play poker with his buddies, or spy on the neighbors, or sit around watching the damn TV! He hasn't taken me on a single date or done anything romantic in two years!"
    rac "When I asked him what's his deal and told him I'm not happy with the way things are going, he acted profoundly... weird! He started groveling.{w} {i}Groveling!{/i}"
    rac "He had it in his head that I was going to leave him and cried like a literal baby while begging me not to leave him! Do you have any idea how uncomfortable that made me?"
    scene c3p6 with dissolve
    rac "It's like he's a completely different man from the one I married. I'm starting to wonder if he took too many blows to the head or something."
    scene c3p7 with dissolve
    rac "I'm going mad! And I can't take it anymore."
    scene c3p4 with dissolve
    rac "So let me make you a deal."
    scene c3p3 with dissolve
    mc "..."
    scene c3p4 with dissolve
    rac "I need your... help."
    rac "I... can't tell you what it is I need help with just yet."
    rac "Glenn's going out of town soon... just for a few days to see his mother. All I ask is that you give me your number, then come by the house when I contact you."
    scene c3p3 with dissolve
    mc "Look. I'm so goddamned confused. Why should I agree to any of this? How do I even know I can trust you?"
    scene c3p4 with dissolve
    rac "Because I witnessed him harassing you the other day, and I don't think what he did was right. I was very angry with him."
    scene c3p3 with dissolve
    mc "(Yeah... you and me both!)"
    pause (.5)
    scene c3p11 with dissolve
    rac "And because I have the disc. The one Glenn used to record you. And if you agree, I'll make absolutely sure you get it. Not only that, but a guarantee that he stops bothering you."
    rac "I'm not asking you to agree to anything right now. I only ask that we exchange numbers and you wait for me to contact you."
    rac "We can discuss the...{w} details... when you come pick up that recording."
    rac "So. What's the verdict?"
    scene c3p10 with dissolve
    mc "(...What the fuck have I gotten myself into?)"
    mc "{i}*Sigh*{/i}"
    mc "(I guess if it gets that prick off my back it's not the worst thing in the world. And as she said, I don't have to agree to anything.)"
    mc "(Once I have that recording I can tell her to fuck off if I want to.)"
    mc "(I guess I don't really have anything to lose.)"
    mc "(And now that I know that Glenn is trying to fuck up my life, I'm going to do everything in my power to bring him down and destroy his career.)"
    mc "(The world is better off without corrupt bastards like him. He screwed with the wrong person.)"
    mc "Alright. Go ahead and give me your card. I'll text you so you have my number."
    mc "But I'm not agreeing to anything until I know what you need from me. You hear?"
    scene c3p2 with dissolve
    rac "I understand, [mc]. And for what it's worth, it was great to finally meet you. I'm terribly sorry for all the drama my husband has caused you. I'll be keeping him on a tight leash."
    stop music fadeout 09.0
    scene c3p11 with dissolve
    rac "I should get back now."
    rac "Oh, and sweetie?"
    scene c3p1 with ssdissolve
    rac "Thank you. I promise I'll make all of this up to you."
    rac "Buh-bye, handsome."
    scene black with sdissolve
    $ renpy.pause (3, hard=True)
    scene c3q113 with dissolve
    mc "(Fuck me! That was crazy.)"
    mc "(What is going on with my life right now? It's like I'm being tested.)"
    mc "{i}*Sigh*{/i}"
    mc "(I'll think about it later. It's time to meet Brooke.)"

label brooke_apartment:

    image brookekiss = Movie(play="videos/Chapter 3/brooke_kiss.webm")
    scene c3q112 with ssdissolve
    play music "<loop 0.0>audio/seasons.ogg" fadein 08.0
    brk "[mc]! You came!"
    show brooke2 at brooke2_transform
    brk "(Of course he came, dummy. He said he would. Now keep it together!)"
    pause (.3)
    scene c3q111 with dissolve
    if brk_rel == False:
        brk "(He already said he's not interested in you... so stop acting like a schoolgirl.)"

    mc "It's nice to see you too. Thanks for inviting me."
    scene c3q112 with qdissolve
    brk "No, thank you for being here. It means a lot."
    scene c3q111 with qdissolve
    brk "(Chelsea shouldn't be here for at least another hour, so luckily we'll be able to chat for a while. I just hope I don't say something stupid or embarrass myself.)"
    if brk_rel == True:
        brk "(I should also have time to implement my... {i}plan.{/i}{w} Oh God...)"

    scene c3q110 with sdissolve
    brk "Come in!"
    scene c3q109 with fadehold
    mc "(She looks cute today. Seems nervous though.)"
    scene c3q108 with sdissolve
    mc "(I wonder why?)"
    scene c3q107 with dissolve
    mc "Nice place you got."
    scene c3q106 with qdissolve
    brk "Oh, c'mon. I'm sure you're just being nice. It's... small! And cheap."
    scene c3q104 with qdissolve
    mc "Well I'm sure things will turn around for you now that you're working with us at the agency. Keep booking gigs like the one you got yesterday, and you'll be able to afford a better place in no time at all."
    mc "Besides, it's cozy."
    mc "Anyway, I've been looking forward to talking to you since... you know."
    scene c3q105 with qdissolve
    brk "Me too! I had a really good time with you. I think I said it already but thank you for dinner. It meant a lot to me. And talking with you helped ease my mind."
    scene c3q104 with qdissolve
    mc "I'm glad!"
    scene c3q103 with qdissolve
    brk "I was actually thinking a lot about the things you said that night... about everything you had to go through."
    brk "And I can't help but ask. How are you, [mc]? Like how are you psychologically? Emotionally? Is everything okay in life? I don't know how well I'd be holding up if I were in your shoes."
    scene c3q102 with qdissolve
    mc "(Awe, that's really nice of her to inquire. Been a while since someone asked me such a thoughtful question.)"
    pause (.5)
    mc "Well..."
    mc "I'll be honest. I haven't really had a lot of time to think about that."
    mc "So much has been happening lately, and it's really making me see the world in a different light. Whether good or bad, I guess that..."
    mc "I'm not sure how I'm doing, exactly."
    mc "But I'm so used to just focusing on work. This vacation will be the first time in years that I've been able to just sort of... reflect."
    mc "Maybe I'll have a better answer the next time we see each other."
    scene c3q101 with qdissolve
    brk "Well, the good news is you {i}seem{/i} to be holding up well!"
    scene c3q100 with qdissolve
    mc "Haha, yeah. I guess...{w} I guess I'm pretty okay."
    scene c3q99 with qdissolve
    brk "Don't you have any close friends?"
    scene c3q100 with qdissolve
    pause (.5)
    mc "Hm..."
    mc "Aside from Bernie?"
    scene c3q105 with qdissolve
    brk "Hehe, yes. Aside from Bernie."
    scene c3q104 with qdissolve
    mc "Hm... I haven't really even... thought about it."
    mc "But now that you mention it, Bernie's my only friend."
    mc "For the longest time, the only thing I even thought of was working and making the most of my career. I guess I've sort of neglected my social life."
    mc "What about you? I know you said your only close friend is a girl named, um..."
    scene c3q103 with qdissolve
    brk "Chelsea."
    scene c3q102 with qdissolve
    mc "Yeah, Chelsea."
    mc "Any reason for that? What have you been up to for the past couple of years? Or better yet what were you doing for work before coming to work at the agency?"
    scene c3q103 with qdissolve
    brk "Hm... well as I mentioned the other night, my main focus was getting my degree and practicing photography. I guess, like you, I've sort of neglected the idea of having a social life."
    brk "I also spent some time working at this little coffee shop."
    scene c3q98 with dissolve
    brk "And then, um... there's some other stuff."
    scene c3q97 with qdissolve
    brk "(God. Why am I struggling so much to tell him?)"
    mc "(She must have met someone her age during that time right? I imagine most guys would be pounding down her door, given the option.)"
    mc "And in that time, you didn't meet anyone? Ahem... any uh, romantic partners?"
    scene c3q96 with dissolve
    brk "Oh {i}God no.{/i} In fact I've always gone out of my way to avoid, uh... romantic stuff. I don't even have any guy friends."
    brk "In part that's because I was focused on my career..."
    scene c3q94 with qdissolve
    brk "But I also think it has something to do with the strange behaviors instilled in me by my nutjob parents."
    brk "I feel a bit... different now though. I guess over time, my views on relationships and romance have changed a lot."
    brk "And I think, finally, that I might be ready for something. Something serious, perhaps."
    scene c3q95 with qdissolve
    mc "(It almost sounds like...{w} she's never dated anyone. That'd be extremely odd for a girl her age, but not after everything she told me about her upbringing. Not to mention the fact that she's been focusing on her career.)"
    mc "(Not sure how direct I should be here... but I do feel the need to inquire.)"
    mc "So uh, no romantic partners at all?"
    scene c3q98 with dissolve
    brk "It's a little embarrassing..."
    brk "But no. None."
    scene c3q97 with qdissolve
    mc "(Wow. I was totally not expecting that.)"
    mc "Well, I can't say it enough. I'm sorry for what you went through. It sounds like your parents did a lot to make sure you didn't have a normal life, growing up."
    scene c3q96 with dissolve
    brk "It hurts to say it, but you're right."
    brk "My whole life, especially when I was a little girl, I always dreamed about being a mother myself. I made a vow to myself that when that day comes, I'll do everything I can to be a better parent than my own mother was."
    brk "Over time, I became fascinated with the idea of having a child."
    scene c3q95 with qdissolve
    brk "(I should use this opportunity to see what he thinks of that.)"
    scene c3q96 with qdissolve
    brk "Is that um...{w} is that weird?"
    scene c3q95 with qdissolve
    mc "Wanting to have a child? Not at all. I think it's admirable, given what you went through as a child yourself. And it makes perfect sense that you'd want to turn your own experience into something positive."
    scene c3q97 with dissolve
    brk "(Whew. That's a relief.)"
    mc "So um, not to cut things short because I'm really enjoying our talk."
    mc "(I do need to start wrapping this up though if I'm going to hit the road on time.)"
    mc "But you invited me so you could ask me something, right?"
    scene c3q93 with dissolve
    brk "Oh right, crap! I got so carried away talking that I almost forgot."
    scene c3q95 with qdissolve
    mc "Heh. It's alright."
    scene c3q94 with qdissolve
    brk "There's actually a couple of things I wanted to talk to you about."
    brk "First, I need to be honest. I'm freaking out internally over how the gig went."
    brk "The thing is nothing in particular happened. At least nothing worth mentioning."
    brk "And Bernie even said that everything was perfect. He was also really nice and helpful the entire time."
    brk "I still have to edit everything and send the photos out, but..."
    brk "I just have this nagging feeling that it all went horribly wrong, and that I was too distracted to realize it. Or that the pictures are awful, and maybe I'm just delusional. I keep looking at them over and over, finding small details I don't like or thinking about how it could've gone better."
    brk "I don't know. Am I...?"
    brk "Am I wrong to freak out?"
    scene c3q95 with qdissolve
    mc "Well first of all, was all of the equipment working?"
    scene c3q94 with qdissolve
    brk "Uh-huh. It was."
    scene c3q95 with qdissolve
    mc "And did you take lots of pictures?"
    scene c3q94 with qdissolve
    brk "Y-Yes. Of course!"
    scene c3q95 with qdissolve
    mc "Did the client seem happy with the way everything was setup and the way you went about taking said pictures?"
    scene c3q94 with qdissolve
    brk "Hm..."
    brk "S-Sure. At least, I think so."
    scene c3q95 with qdissolve
    mc "Heh. Then it sounds like everything went exactly according to plan."
    mc "Look, I know you're anxious. I get it. Like I said, I was in your shoes at one point. I've been through the exact thing you're going through right now."
    mc "But trust me when I say that if something went wrong, Bernie would be the first person to tell you. He might be a little quirky, but he's fantastic at his job. He's also not the type to say something simply because it's what you want to hear."
    scene c3q94 with qdissolve
    brk "I see."
    brk "Hmm. That... makes me feel a little better."
    scene c3q97 with dissolve
    brk "(Oh man. I'm a damn mess. Am I freaking out over nothing?)"
    mc "Tell you what..."
    mc "I'm going away for a few days, but I'll have my laptop. Email me the photos once they're ready and I'll take a look through them for you and happily provide some feedback."
    scene c3q93 with dissolve
    brk "You'd... do that for me? Even while you're on vacation?"
    scene c3q104 with qdissolve
    mc "Only because I know you'd do it for me if the roles were reversed."
    scene c3q92 with sdissolve
    brk "Oh, [mc]. That's so..."
    scene c3q90 with sdissolve
    stop music fadeout 07.0
    brk "You're so..."
    brk "Wonderful."
    scene c3q89 with qdissolve
    brk "..."
    scene c3q88 with sdissolve
    if brk_rel == False:
        mc "(What is she doing? I thought we agreed...)"
    else:
        mc "You're pretty amazing yourself."

    scene c3q86 with sdissolve
    brk "(Oh God. He's so close. I just want to...)"
    play music "<loop 0.0>audio/sunny_days.ogg" fadein 09.0
    scene c3q87 with qdissolve
    pause (1)
    if brk_rel == True:
        mc "(Whoa. This was unexpected. Did she invite me over because she wanted to make out?)"
        mc "(Not that I'm complaining. Despite her lack of experience, she's a good kisser.)"
        mc "(Stop pondering shit and kiss her back already.)"
        show brookekiss with sdissolve
        brk "Mm..."
        brk "(I don't know what's gotten into me, but I just can't help myself when I'm around him.)"
        brk "(And kissing him is all I could think about after how sweet he was during our date the other night.)"
        brk "(Not a quick, awkward peck like the one I gave him that night, either.)"
        brk "(Oh no, here comes the panic.)"
        scene c3q85 with sdissolve
        brk "Fuck! I'm sorry. I shouldn't have done that without asking."
        scene c3q83 with qdissolve
        mc "Heh. Why are you apologizing? It would've been pretty awkward if you asked first."
        scene c3q84 with qdissolve
        brk "Oh, right."
        scene c3q82 with dissolve
        brk "{i}*Sigh*{/i}"
        scene c3q81 with dissolve
        brk "I need to be honest. I'm kind of freaking out. In fact, I always freak out when I'm around you."
        brk "Not in a bad way, of course! Um, what I mean is, it's not that you did something wrong, it's totally my own fault."
        brk "I'm freaking out because..."
        brk "Because I like you. A lot. And you're...{w} gorgeous."
        scene c3q83 with dissolve
        mc "You're pretty gorgeous yourself. And a good kisser."
        mc "If anything, you should kiss me like that more often."
        scene c3q81 with dissolve
        brk "S-So that means you enjoyed it?"
        scene c3q80 with qdissolve
        mc "How about I show you instead of talking about it?"
        scene c3q79 with dissolve
        brk "Mm..."
        scene c3q87 with dissolve
        brk "{i}*Moans*{/i}"
        brk "([mc]...)"
        jump afterkiss_romance
    else:
        jump afterkiss_noromance

label afterkiss_noromance:

    mc "(What the hell? Is this really happening? I thought we agreed to keep it professional.)"
    mc "(What have I gotten myself into now?)"
    mc "(She is a pretty good kisser though. And there's no denying she's attractive.)"
    mc "(If something comes from this, is it really my fault?)"
    scene c3q87 with purpflash
    scene c3q87 with purpflash
    scene c3q87 with purpflash
    menu:
        mc "(No, wait. I can't think like that. Can I?)"
        "Stop Her":
            $ pure +=1
            stop music fadeout 07.0
            brk "(Oh God! What am I doing? I'm making out with [mc], even after he asked to keep things professional between us.)"
            scene c3q75 with sdissolve
            mc "Brooke- wait."
            mc "We can't do this.{w} I'm sorry."
            scene c3q77 with dissolve
            brk "N-No...!"
            brk "I'm the one who's sorry! That was totally out of line! I can't believe I just did that."
            scene c3q74 with dissolve
            brk "I'm so sorry, [mc]. I'm just really bad at expressing myself, and I guess when I got closer to you I just lost control for a second. I promise I'll never do that again."
            scene c3q73 with dissolve
            mc "Listen, it's not that I don't think you're an awesome person. Because you are."
            mc "But you're my employee. And I also have a lot going on in my personal life, so seeing you romantically is just not something I can consider right now."
            mc "I really do hope we can still be friends, however. Just because we're not dating doesn't mean I can't still be a part of your life."
            brk "(Oh God. I'm such a mess. How could I do this to [mc]? And right when things were going so well between us?)"
            brk "(No wonder he's not into me. I'm... desperate.)"
            scene c3q82 with dissolve
            brk "{i}*Sigh*{/i}"
            scene c3q81 with dissolve
            brk "T-That makes me really happy to hear, and I hope I haven't made our friendship awkward. As I said, I don't know what got into me. I'm not normally like this."
            brk "I hope you can forgive me and that we can just... forget about it."
            scene c3q83 with dissolve
            mc "It's okay, Brooke. We all make mistakes sometimes. Let's just forget about it."
            scene black with sdissolve
            na "You chat for a while, but the situation never gets any less awkward. Then finally..."
            jump brk_phonecall_alt
        "Get Angry":

            $ dark +=1
            stop music fadeout 07.0
            scene c3q75 with sdissolve
            mc "Brooke, what the fuck?!"
            brk "(Shit! What have I done?!)"
            mc "I thought we talked about this? You can't just kiss me like that after I asked that we keep our relationship professional."
            brk "(I'm such a mess. How could I do this to [mc]? And right when things were going so well between us?)"
            scene c3q77 with dissolve
            brk "Oh my God, I'm so sorry [mc]. I don't know what the hell is wrong with me!"
            scene c3q74 with dissolve
            brk "I-I'm... just really bad at expressing myself... and I guess when I got closer to you I just lost control for a second. I promise I'll never do that again."
            scene c3q73 with dissolve
            mc "{i}*Sigh*{/i}"
            mc "Listen, it's not that I don't think you're a cool person. Because you are."
            mc "But you're my employee. And I also have a lot going on in my personal life, so seeing you romantically is just not something I can consider right now."
            mc "I do hope we can still be friends, however. Just because we're not dating doesn't mean I can't still be a part of your life."
            brk "(Oh God. I'm such a mess. How could I do this to [mc]? And right when things were going so well between us?)"
            brk "(And I've gone and pissed him off now! Sweet mother of fuck, this is a disaster!)"
            brk "(No wonder he's not into me. I'm... desperate.)"
            scene c3q82 with dissolve
            brk "{i}*Sigh*{/i}"
            scene c3q74 with dissolve
            brk "Y-You're right."
            brk "I hope you can forgive me and that we can just... forget about it."
            scene c3q73 with dissolve
            mc "It's whatever, Brooke. You're right. Let's just forget about it."
            scene black with sdissolve
            na "You chat for a while, but the situation never gets any less awkward. Then finally..."
            jump brk_phonecall_alt
        "Kiss Her Back":

            $ lust +=3
            $ brk_lust +=3
            $ brk_secondchance = True
            mc "(Fuck it. What's the worst that could happen?)"
            show brookekiss with sdissolve
            brk "Mm..."
            brk "(Oh God! What am I doing? I'm making out with [mc], even after he asked to keep things professional between us.)"
            brk "(I just can't stop myself.)"
            brk "(He's too fucking perfect!)"
            scene c3q79 with dissolve
            brk "{i}*Gasp*{/i}"
            scene c3q77 with dissolve
            scene c3q77 with vpunch
            brk "Oh my God! I'm so sorry, [mc]. I shouldn't have just thrown myself at you like that."
            scene c3q75 with dissolve
            mc "No, you don't owe me an explanation. I uh... to be honest I didn't want you to stop."
            scene c3q77 with dissolve
            brk "Does that mean that you... like me?"
            scene c3q75 with dissolve
            mc "I... I'm not sure what I feel yet, to be honest."
            scene c3q74 with dissolve
            brk "...I'm sorry. I'm really bad at this stuff. And when we were on our date the other night, I was given the impression that you... you know... wanted to stay professional."
            scene c3q73 with qdissolve
            mc "No, you're right. I did say that. I'm sorry if I'm giving you mixed signals. I guess I..."
            jump brooke_secondchance


label brooke_secondchance:

    scene c3q73 with pinkflash
    scene c3q73 with pinkflash
    scene c3q73 with pinkflash
    menu:
        mc "(Shit. What should I do here?)"
        "Date Her":
            $ lust +=3
            $ brk_lust +=3
            $ brk_rel = True
            mc "(You know what? Screw it. Who needs to be professional when there's a girl as amazing as Brooke throwing herself at me? I don't know why I turned her down that night... but I feel differently now that I've slept on it and gotten to know her a little better.)"
            mc "I guess I was just being cautious. But now that I've had a couple of days to ponder it all... I'd be open to the idea of um, you know, dating."
            scene c3q76 with dissolve
            brk "(No way! I can't believe this is happening!)"
            brk "(Okay. Calm the fuck down! Don't blow it.)"
            scene c3q72 with dissolve
            brk "Are you sure? I don't want to cause any problems. And I know we hardly know each other, but I just can't help the feelings I have when I'm around you."
            scene c3q76 with dissolve
            mc "I feel it too. And yes, I'm sure."
            scene c3q65 with qdissolve
            pause (.5)
            scene c3q66 with dissolve
            brk "Does that mean I can..."
            scene c3q87 with dissolve
            brk "Mm..."
            jump afterkiss_romance
        "Reject Her":

            $ pure +=1
            stop music fadeout 07.0
            mc "(No. I can't risk allowing this to continue, and I don't want to lead her on.)"
            mc "(Unfortunately she's just going to have to face the music and realize she's not my type. Or at least not right now.)"
            mc "I guess when you kissed me, I just sort of got caught up in the moment."
            mc "But what I said the other night about keeping things professional between us..."
            mc "I said that for a reason, and I think I was onto something."
            mc "Look, I don't want to hurt you, but I also don't want to lead you on. And right now, a relationship between us is just not something I can afford."
            mc "I'm sorry."
            scene c3q82 with dissolve
            brk "{i}*Sigh*{/i}"
            scene c3q81 with dissolve
            brk "Please don't be sorry. It's really noble of you to be honest and up front about it.{w} You could've easily taken advantage of me, and I would've been none-the-wiser."
            brk "I-If anything, I was just being stupid. If you hadn't noticed when I met you I was a little... star struck."
            scene c3q74 with dissolve
            brk "I know it sounds stupid. I mean you're not like some big movie star or something. But I really meant it when I said I've been a fan of your work for ages."
            brk "You could say you're one of my biggest inspirations for getting into photography."
            brk "You're a really talented person, [mc]. And being friends is more than enough."
            scene c3q73 with dissolve
            mc "(Wow, that was a nice thing to say, and makes me feel a lot better about all this.)"
            mc "(She still seems pretty sad, though.)"
            mc "Thanks, that really means a lot. And I meant it when I said you're talented, too. Remember, I've seen your portfolio. We hired you for a reason."
            mc "And I'm lucky to have someone like you as a friend as well."
            scene c3q65 with dissolve
            na "She smiles and the awkwardness slowly fades. Still, you can see a hint of sadness in her smile."
            scene black with sdissolve
            na "You chat for a while, but the situation never gets any less awkward. Then finally..."
            jump brk_phonecall_alt
        "Take Advantage":

            $ dark +=3
            $ brk_dark +=3
            $ brkdark = True
            $ brk_rel = True
            mc "(You know what? Screw it. Who needs to be professional when a girl as cute as Brooke is just throwing herself at you? And I'm my own boss, so it's not like I'm going to get fired for fucking my employees.)"
            mc "(The truth is, I don't know if I have any feelings for Brooke, but she seems to want this more than I do. And it's her fault for putting the pressure on, even after I was honest with her the other night and requested we keep things friendly.)"
            mc "Hm. The more I think about it..."
            mc "I guess I was just being cautious. But now that I've had a couple of days to ponder it all... I'd be open to the idea of um, you know, dating."
            scene c3q76 with dissolve
            brk "(No way! I can't believe this is happening!)"
            brk "(Okay. Calm the fuck down! Don't blow it.)"
            scene c3q72 with dissolve
            brk "Are you sure? I don't want to cause any problems. And I know we hardly know each other, but I just can't help these feelings I have when I'm around you."
            scene c3q76 with dissolve
            mc "(What I'm about to say isn't exactly honest. But screw it.)"
            mc "I feel it too. And yes, I'm sure."
            scene c3q65 with qdissolve
            pause (.5)
            scene c3q66 with dissolve
            brk "Does that mean I can..."
            scene c3q87 with dissolve
            brk "Mm..."
            jump afterkiss_romance

label afterkiss_romance:

    scene c3q75 with sdissolve
    brk "(Chelsea, I swear to God if this backfires... I'll literally kill you.)"
    brk "(But she knows way... way more about romance than I do. And she said that this is what he probably wants.)"
    brk "(I can't believe I'm about to do this. This is so out of my element, and I'm positive I'm going to manage to screw it up somehow.)"
    brk "(But I can't deny the way I feel about him, even after such a short time. And a guy like him doesn't stay single for long.)"
    brk "(I have to make absolutely sure that he knows how much I like him, or I'll regret it for the rest of my life. Especially if he decides he doesn't like me back.)"
    scene c3q77 with dissolve
    brk "Um... [mc]?"
    scene c3q75 with dissolve
    mc "Yeah?"
    scene c3q77 with dissolve
    brk "Can you...{w} close your eyes for a moment?"
    scene c3q75 with dissolve
    mc "Huh? What for?"
    scene c3q77 with dissolve
    brk "J-Just trust me, please."
    scene c3q75 with dissolve
    mc "(Strange request, but...)"
    mc "Sure. No problem."
    scene black with sdissolve
    brk "Keep them closed! I'll let you know when you can open them."
    mc "(I'm so confused right now. What is happening?)"
    mc ".{w}.{w}."
    brk "Um."
    brk "Y-You can open your eyes now."
    pause (1)
    show brooke3 at brooke3_transform with ssdissolve
    pause (.3)
    brk "(Please don't think I'm a whore. Please don't think I'm a whore.)"
    brk "(Chelsea... what have you talked me into?)"
    mc "(Holy...{w} fucking...{w} shit!)"
    mc "Brooke, I'm..."
    scene c3q64 with sdissolve
    brk "Shh..."
    brk "Y-You've done so much for me since I started working at the office..."
    scene c3q63 with dissolve
    brk "You're always so nice..."
    scene c3q62 with sdissolve
    brk "L-Let me return the favor."
    scene c3q60 with sdissolve
    mc "(Jesus Christ!)"
    scene c3q61 with sdissolve
    mc "(Alright, calm down. I've been around long enough to know where this is going.)"
    mc "(I just hope this is what she really wants. I wouldn't want her to force herself. She seems comfortable enough, though.)"
    mc "(This wouldn't be the first time a girl who's sweet like Brooke has pushed her boundaries to impress me, come to think of it. And it's always worked itself out.)"
    mc "(Or I'm just totally thinking with my cock right now.)"
    if brkdark == True:
        $ brk_blowjob = True
        mc "(Heh. Who am I kidding? This is exactly what I wanted. She's clearly trying her hardest to get me to like her. And in return, I could get something I want.)"
        mc "(We did kind of just agree to dating, after all. Even if I wasn't being wholly honest.)"
        mc "(Seeing her naked has made me hard as a rock. And perhaps turning her down could hurt her confidence.{w} It would definitely hurt my balls.)"
        jump brooke_blowjob
    else:
        mc "(Then again, it wouldn't be the worst thing in the world to just go with it. We {i}are{/i} kind of dating after all.)"
        mc "(And I'm not going to lie, seeing her naked has made me hard as a rock.)"
        mc "(Turning her down could hurt her confidence. And it will definitely hurt my balls.)"
        jump bj_choice

label bj_choice:

    menu:
        mc "(What should I do here?)"
        "Let Her Do It":
            $ lust +=1
            $ brk_lust +=1
            $ brk_corrupted +=1
            $ brk_blowjob = True
            jump brooke_blowjob
        "Stop Her":

            $ pure +=1
            $ brk_pure +=1
            mc "..."
            mc "(No, this feels... wrong.{w} Something tells me she's going much further than {i}she{/i} actually wants.)"
            mc "(As much as I'd enjoy letting her do whatever she's planning, I'm not sure how good it would be for our relationship in the long run.)"
            scene c3q59 with sdissolve
            mc "Brooke, wait."
            scene c3q58 with dissolve
            brk "I-Is something wrong?"
            scene c3q56 with dissolve
            mc "It's not that... it's just..."
            mc "I have a feeling you're pushing yourself into doing something you maybe don't want."
            mc "Am I reading things wrong?"
            scene c3q57 with dissolve
            stop music fadeout 09.0
            brk "N-No.{w} You're not..."
            brk "{i}*Sigh*{/i}"
            brk "You're not wrong. But it's not that I don't want to do this stuff with you. That's not it at all!"
            brk "It's just... I've never done something like this before. And I thought that if I did something like this for you, you'd like me more."
            brk "Am I stupid? I'm acting like a teenager, aren't I?"
            scene c3q56 with dissolve
            mc "It's not stupid at all. I totally get it. But maybe we can wait a little while until you're more comfortable? I don't want to move too fast unless it's something you truly want."
            scene c3q47 with sdissolve
            brk "You're an amazing person, [mc]. I mean that. Thank you so much for not..."
            jump brk_phonecall

label brooke_blowjob:

    image brookeblow = Movie(play="videos/Chapter 3/brooke_blow.webm")
    image brookeblow2 = Movie(play="videos/Chapter 3/brooke_blow2.webm")
    image brookelick = Movie(play="videos/Chapter 3/brooke_lick.webm")
    mc "(Fuck it. No way am I turning this down.)"
    mc "(I'm not one to look a gift horse in the mouth.)"
    scene c3q55 with fadehold
    brk "(I'm doing this... I'm holding [mc]'s cock!)"
    brk "(And he doesn't seem to mind at all!)"
    $ renpy.pause (.5, hard=True)
    show brookelick with ssdissolve
    pause
    brk "(Please, Brooklyn. Please don't fuck this up!)"
    if van_romance == True:
        mc "(Whoops...)"
        mc "(I hope she doesn't mind the taste of Vanessa's pussy on my cock.)"
        pause (1)

    brk "(God. I love the taste of his cock.)"
    pause
    brk "(My body is on fire. This is a dream come true.)"

    if brkdark == True:
        mc "Be a dear and hurry up."
        scene c3q54 with sdissolve
        hide brookelick
        mc "Don't tease me. Put that cock in your mouth."
        brk "(Oh.{w}.{w}. shit!)"
        pause (.5)
        scene c3q53 with sdissolve
        scene c3q53 with vpunch
        brk "Mnnn!"
        scene c3q52 with dissolve
        brk "{i}*Coughing*{/i}"
        scene c3q51 with qdissolve
        brk "(Why is he being mean...?)"
        mc "That's better. Such a good little slut."
        pause (.5)
        scene c3q50 with qdissolve
        brk "(S-So he does think I'm some slut now...)"
        brk "(No... I didn't want...)"
        scene c3q54 with sdissolve
        mc "Enough. I said no more teasing."
        scene c3q53 with sdissolve
        brk "(!!!)"
        brk "(Fuck! I can't breathe. I better do as he asks...)"
        show brookelick with sdissolve
        mc "I said...{w} suck...{w} my cock."

    if brkdark == True:
        brk "Anything you want, [mc]."

    show brookeblow with sdissolve
    brk "(I can't believe I'm doing it. I'm sucking [mc] [sur]'s cock!)"
    brk "(I want to take it {i}all{/i} in. I want to taste every inch of him. But if I try going too deep right now I'll probably puke on him.)"
    brk "(...fuck. I'm getting horny. My pussy is drenched.)"
    brk "Mm..."
    brk "([mc].)"
    brk "(F-Fuck, my legs are trembling. H-How does my pussy feel like this without any stimulation at all? It's like I'm having an orgasm in my panties just by having him in my mouth.)"
    brk "(If... if this goes on for much lo-longer I'm going to end up letting him fuck me. I'm not going to be able to hold myself back. I am so fucking horny right now.)"
    show brookeblow2 with sdissolve
    hide brookeblow
    pause
    brk "(The feeling on his cock rubbing along my tongue. I can't stop licking the tip, lapping up all of his precum.)"
    mc "..."
    mc "(F-Fuck me. She's hitting all the sensitive spots. I don't think I can hold out much longer. This was not expected.)"
    show brookeblow with sdissolve
    hide brookeblow2
    pause
    mc "(She's {i}really{/i} into this.)"
    mc "I-I'm right on the edge."
    menu:
        mc "(Fuck! Here it comes. Doesn't look like she's stopping either. I think she wants it in her mouth.)"
        "Cum In Her Mouth":
            scene c3q53 with dissolve
            scene c3q53 with vpunch
            brk "Mmnn!"
            mc "(OH FUCK!)"
            scene c3q53 with flash
            scene c3q53 with flash
            scene c3q53 with flash
            mc "(FUCK! She's completely drinking me dry.)"
            mc "(I never would've thought Brooke was such a lewd girl. She seems to be loving this.)"
            scene c3q52 with sdissolve
            brk "{i}*Gasping*{/i}"
            scene c3q51 with dissolve
            brk "{i}*Gulp*{/i}"
            scene c3q50 with dissolve
            brk "Mmm..."
            scene c3q51 with dissolve
            brk "(So... so good.)"
        "Cum on Her Tits":

            scene c3q53 with dissolve
            scene c3q53 with vpunch
            pause (.5)
            mc "(Oh...{w} fuck!)"
            scene c3q52 with sdissolve
            pause (.3)
            brk "{i}*Gasping*{/i}"
            scene c3q51 with dissolve
            mc "Brooke, I-I can't hold out any longer. Bring me those beautiful tits."
            scene c3q49 with flash
            scene c3q49 with flash
            scene c3q49 with flash
            brk "Mmmmm..."

    stop music fadeout 08.0
    scene c3q61 with fadehold
    mc "Brooke, that was fucking amazing. I'm beside myself.{w} D-Do you want me to return the favor?"
    scene c3q62 with dissolve
    brk "I... I really do. But um..."
    brk "Before we go any further, there's something I really need to tell you."
    scene c3q61 with dissolve
    mc "(She better not have a fucking penis.)"
    mc "(Nah, what is wrong with me? She doesn't have a penis.)"
    scene c3q62 with dissolve
    brk "I mentioned earlier that there's something else I need to talk to you about. It's a big part of why I invited you over today, as I didn't have the courage to bring it up at our dinner."
    brk "Um... like I said before I've never really... had a boyfriend. As unbelievable as that may sound, given my age."
    brk "So as I'm sure you can guess I've never... had sex either."
    scene c3q61 with dissolve
    pause (1.3)
    scene c3q62 with dissolve
    brk "I'm... a virgin, [mc]."
    brk "But there's something else. Perhaps something even less believable."
    brk "So um, shortly after I got my first apartment..."
    jump brk_phonecall

label brk_phonecall:

    play sound "audio/sounds/phone_ring.ogg"
    scene c3q45 with fadehold
    brk "..."
    scene c3q44 with dissolve
    play sound "audio/sounds/phone_ring.ogg"
    brk "Shit! Shit! Horrible timing. That's my client!"
    if brk_blowjob == True:
        scene c3q43 with sdissolve
        play sound "audio/sounds/phone_ring.ogg"
        brk "I have to take this, [mc]. I'll be right back, and then I'll finish what I was about to tell you. I promise."
        scene c3q42 with ssdissolve
        pause (1)
        mc "(Well shit. Now I'm going to go crazy wondering what she was about to tell me.)"
        mc "(I suppose it wouldn't hurt to take a look around the place while I wait to keep my mind off all the suspense and mystery. Let me just quickly put my unbearably erect cock away.)"
    else:
        scene c3q43 with sdissolve
        play sound "audio/sounds/phone_ring.ogg"
        brk "I have to take this, [mc], and then we can talk about that other thing I was going to tell you."
        scene c3q42 with ssdissolve
        pause (1)
        mc "(Well shit. I hope I made the right decision. She seemed a little upset that I stopped her.)"
        mc "(I suppose it wouldn't hurt to take a look around the place.)"

    jump after_brk_phonecall

label brk_phonecall_alt:

    scene c3q45 with sdissolve
    play sound "audio/sounds/phone_ring.ogg"
    brk "..."
    scene c3q44 with dissolve
    brk "Shit! Shit! Horrible timing. That's my client!"
    brk "I have to take this, [mc], and then we can talk about that other thing I was going to tell you."
    scene c3q42 with fadehold
    pause (.5)
    mc "(Welp... this meeting turned out to be pretty awkward.)"
    mc "(I suppose it wouldn't hurt to take a look around the place while I wait... to keep my mind off what just went down.)"
    jump after_brk_phonecall

label after_brk_phonecall:

    scene black with ssdissolve
    $ renpy.pause (3, hard=True)
    scene c3q41 with ssdissolve
    uk "Hmm?"
    uk "(What's this {i}boy{/i} doing in my house?! Where's mom?)"
    play music "<loop 0.0>audio/leaning_on_the_everlasting_arms.ogg" fadein 08.0
    uk "(Grr! He better not be a burgerer.)"
    uk "(If only Chelsea were still here! She could help me rescue mommy! But she said she was in a hurry, so she dropped me off then drove away.)"
    uk "(Don't worry, mommy. I'll save you from the big ugly stalker!)"
    scene c3q40 with fadehold
    mc "(Huh... what a cute little bear.)"
    if brk_blowjob == True:
        mc "{i}*Yawn*{/i} (I feel so relaxed right now. That blowjob was amazing.)"

    scene c3q39 with sdissolve
    pause (1)
    mc "(Hmm? What was that sound?)"
    $ renpy.pause (1, hard=True)
    mc "Huh..."
    scene c3q40 with dissolve
    pause (1)
    mc "(Guess it was nothing. I hope Brooke hurries with that phone call. I'm dying to know what she was going to talk to me about.)"
    mc "(Maybe I'll just see what's on TV.)"
    $ renpy.pause (.5, hard=True)
    uk "{i}Ahem!{/i}"
    scene c3q39 with dissolve
    $ renpy.pause (.3, hard=True)
    mc "What the...?"
    scene c3q38 with sdissolve
    uk "{size=+10}{i}HIYAH!!!{/i}{/size}"
    play sound "audio/sounds/smack_xhard.ogg"
    scene c3q37 with xdissolve
    scene c3q37 with vpunch
    mc "{size=+5}{i}Aghr! What the fuck?!{/i}{/size}"
    scene c3q36 with dissolve
    $ renpy.pause (.5, hard=True)
    mc "{i}(Holy fuck-- my balls!!!){/i}"
    scene c3q35 with sdissolve
    $ renpy.pause (.5, hard=True)
    mc "(I... I think she crushed them. I-I can't feel my toes!)"
    scene c3q33 with dissolve
    $ renpy.pause (.5, hard=True)
    mc "What the hell are you doing, kid?!"
    scene c3q34 with dissolve
    uk "There's more where that came from, burgoolar! Now where's momma?!"
    scene c3q33 with dissolve
    mc "M-Ma... what?"
    $ renpy.pause (.7, hard=True)
    scene c3q32 with qdissolve
    scene c3q32 with vpunch
    brk "Norah! Oh my God, what did you do?!"
    scene c3q31 with sdissolve
    brk "[mc]! Are you okay?!"
    scene c3q30 with qdissolve
    mc "I...{w} I think I'm fine. I don't know what happened... she came out of nowhere! What the hell is going on?"
    scene c3q29 with qdissolve
    brk "Norah! Come speak to me in my bedroom, please!"
    scene c3q28 with sdissolve
    brk "I'm so sorry, [mc]. Can you give us a minute?"
    scene c3q27 with qdissolve
    mc "Uh... s-sure. Yeah. I'll be um... right here. I think I... need a moment."
    stop music fadeout 08.0
    scene c3q26 with ssdissolve
    mc "(...to nurse my balls back to health and pray I can still have children after being attacked by that goddamned crazy wombat!)"
    scene black with ssdissolve
    $ renpy.pause (3, hard=True)
    scene c3q25 with ssdissolve
    brk "[mc], I know I've said it already but I am so, so sorry."
    play music "<loop 0.0>audio/campfire.ogg" fadein 08.0
    scene c3q23 with qdissolve
    mc "Please, it's really okay. I already feel a hell of a lot better. I was overreacting."
    scene c3q25 with qdissolve
    brk "Are you sure you're not hurt?"
    scene c3q23 with qdissolve
    mc "Yeah, I'm fine."
    scene c3q24 with qdissolve
    brk "Oh thank God."
    scene c3q21 with dissolve
    brk "So um... I guess I have some explaining to do."
    brk "The reason I didn't tell you about Norah is um..."
    brk "Well, it's kind of embarrassing."
    scene c3q25 with dissolve
    brk "Not her, of course! She's my everything!"
    scene c3q21 with dissolve
    brk "But rather the um... circumstances surrounding her and I."
    if brk_rel == True:
        brk "You see, I wasn't lying when I said I've never... you know..."
        brk "Been with a guy."
    else:
        brk "You see, I've never actually... you know..."
        brk "Been with a guy. I'm a virgin."

    scene c3q18 with dissolve
    brk "After I moved out of my grandmother's place and got my own apartment, I was just so lonely. My best friend was busy all the time. All I ever did was work and watch television."
    brk "As I mentioned before... I always dreamed of being a mother."
    scene c3q21 with dissolve
    brk "Well, one day I was browsing the internet and I happened upon an ad. It was asking for women my age who were able to bear child for um...{w} an experiment with artificial insemination."
    brk "If you weren't aware... this is when sperm is introduced to a woman's...{w} ahem... uteris.{w} It's a common procedure used to induce pregnancy without the need for sexual intercourse."
    scene c3q20 with dissolve
    pause (1)
    mc "(Wait a second...)"
    scene c3q18 with dissolve
    brk "So..."
    brk "Norah {i}is{/i} my daughter. I just didn't have her the... traditional way."
    scene c3q19 with dissolve
    brk "{i}*Exhale*{/i}"
    scene c3q18 with dissolve
    brk "I have a daughter."
    scene c3q17 with qdissolve
    mc "..."
    scene c3q18 with qdissolve
    brk "Before you respond, I am so, so sorry I didn't say anything to you about this sooner. Like I said, it's just very embarrassing. \"I'm a virgin who happens to have conceived a child\" isn't exactly first date discussion material."
    brk "I swear I was about to tell you before I got that stupid phone call!"
    if brk_rel == False:
        brk "But I guess it... doesn't matter anyway. It's not like we're dating or anything, right?"

    scene c3q17 with dissolve
    mc "One second please. I need to process all this."
    scene c3q20 with dissolve
    mc "(This is... insane!)"
    mc "..."
    mc "So you've never had sex?"
    scene c3q18 with dissolve
    brk "Never. As I said, I've never even had a boyfriend.{w} Nor have I ever really wanted one before um... recently."
    scene c3q17 with qdissolve
    mc "And your pregnancy was... induced in some sort of medical facility?"
    scene c3q18 with dissolve
    brk "Yes..."
    scene c3q21 with dissolve
    brk "I know it's weird. And maybe even a little hard to believe if you don't know me that well. That's why I was hesitant to tell you about it. But I promise it's the truth."
    if brk_rel == True:
        brk "And I hope that..."
        brk "That knowing I have a daughter doesn't ruin things for you and me. I really like you, [mc]. And I know it's a lot, but..."

    scene c3q17 with dissolve
    mc "Brooke, hold on. Before we continue."
    mc "There's something I need to tell you as well."
    mc "Not long ago, three [age]-year-old girls, triplets, showed up at my front door."
    if tbed == True:
        mc "I had no memory of this, but the night of my accident I slept with someone."
        mc "As it turns out, those three girls are..."
        scene c3q23 with qdissolve
        mc "They're my [dau]s.{w} Prior to that day I honestly had no idea that they or their mom even existed. However, their mother passed away, so now they're living with me."
    else:
        mc "I had no memory of this, but the night of my accident I met someone."
        mc "As it turns out, their mother passed away... the same girl I met on the night of my accident."
        mc "They needed a place to stay, and their mom requested they seek me out. So I took them in as wards.{w} Prior to that day I honestly had no idea that they even existed."

    mc "So you see, you're not the only one who has a strange secret. Much like you, I planned to tell you about it when the time was right. I guess now was that time. I'm sorry I didn't bring it up sooner."
    scene c3q25 with qdissolve
    brk "Please, don't apologize! If anything, I'm just relieved that I'm not the only one with a weird, mysterious hidden tale!"
    scene c3q16 with dissolve
    brk "Thank you for telling me, [mc]. It means so much to me. And I'm glad you didn't freak out about Norah."
    scene c3q14 with fadehold
    pause (.7)
    mc "Speak of the devil..."
    pause (.5)
    scene c3q13 with qdissolve
    nor "H-Hey mommy?{w} Can I come out now?"
    scene c3q11 with sdissolve
    brk "Yes you can, sweetie. You're not in trouble. I just needed to talk to Mister [sur]."
    brk "Do you have something to say, dear?"
    scene c3q12 with qdissolve
    nor "Yes mom. I wanted to say something."
    scene c3q11 with qdissolve
    brk "Go ahead then baby."
    scene c3q10 with dissolve
    nor "I-I'm sorry I punched you in the balls, Mister [sur]. Please forgive me! I didn't know you were my mom's friend!"
    nor "She never ever has boys over! She is always here by herself when I get home, so I thought you were a burgerlar! I swear!"
    scene c3q9 with qdissolve
    mc "(Heh. \"Burgerlar.\")"
    scene c3q10 with qdissolve
    nor "I'm sorry I hurt you, Mister [sur]."
    scene c3q11 with dissolve
    nor "{i}*Sniff*{/i}"
    mc "(Shit. Now {i}I{/i} feel bad for creating a scene!)"
    mc "Norah, was it? Don't worry... I'm perfectly fine! It uh... it didn't hurt at all.{w} It just uh... startled me. Yeah, I was startled is all."
    scene c3q9 with dissolve
    mc "You did a good thing protecting your mom. Nice job!"
    mc "And you can just call me \"[mc].\""
    scene c3q8 with dissolve
    nor "Thanks Mister [mc]!"
    scene c3q7 with sdissolve
    pause
    scene c3q6 with sdissolve
    nor "Does this mean I can use the comb-puter?!"
    scene c3q5 with qdissolve
    brk "Yes Norah. Go play your game."
    scene c3q4 with qdissolve
    nor "Yay!"
    scene c3q3 with sdissolve
    nor "See you, Mister [mc]! I hope you come back and see us soon!"
    scene c3q2 with ssdissolve
    pause (.5)
    mc "(What a sweet girl.)"
    scene c3q15 with sdissolve
    brk "Anyway, [mc], there's still so much to explain and talk about... but you should get going before you're late! And thank you again for coming over. I hope we can spend more time together soon."
    if brk_rel == True:
        scene c3q1 with sdissolve
        brk "Mm."

    scene c3q16 with sdissolve
    mc "We will. See you in a few days, Brooke."

label pre_park:

    scene black with sdissolve
    $ renpy.pause (4, hard=True)
    scene c3r31 with dissolve
    mc ".{w}.{w}."
    mc "(What a day.)"
    mc "(And there's still so much left in store. It's going to be a long drive.)"
    mc "(I can feel the anxiety mounting already. It's always...{w} hard to go back home after everything that happened.)"
    pause (1)
    if brk_rel == False:
        mc "(I feel a little bad for the way things went down with Brooke, but... at least I was honest.)"
    elif brk_rel == True and brkdark == False:
        mc "(I can't actually believe things are moving so fast with Brooklyn.)"
    elif brkdark == True:
        mc "(Hard to believe Brooke's fallen for me so hard in such a short time.)"

    if cc7 == True:
        mc "(I'm about to meet up with Vanessa, too. Wonder how that will go?)"
        mc "(Come to think of it, it's a little fucked up.)"

    if brkdark == True and cc7 == True:
        mc "(Here I am pretending to romance Brooke so I can get into her pants...)"
    elif brk_rel == True and brkdark == False and cc7 == True:
        mc "(Here I am romancing Brooke...)"
    elif brk_rel == False and cc7 == True:
        mc "(I just completely rejected Brooke...)"

    if cc7 == True:
        mc "(And now I'm about to meet up with the girl who tried to steal me away from her on our very first date.)"

    pause (.5)
    mc "(Fuck. Speaking of Brooke... my balls are still sore from that little maniac.)"
    mc "(Gotta give it to her, though. For such a tiny thing, she sure knows how to throw a punch.)"
    pause (.5)
    mc "(So she has a daughter...)"
    scene c3r30 with sdissolve
    pause (.5)
    mc "(Something tells me that me and that little monster are going to get along just fine.)"
    mc "(She's absolutely adorable. Well, she's Brooke's, after all.)"
    mc "(And now Brooke knows about my own situation with the triplets.)"
    pause (.5)
    if brk_rel == True:
        mc "(I can't help but wonder if Brooke knows who the father is, but I'm sure we'll talk about it at some point. And if I had to guess, I kind of doubt it.)"
        mc "(That is, if she's telling the truth about artificial insemination.)"
        mc "(No, she's definitely telling the truth. I guess it's just strange. You certainly don't see something like this every day.{w} I wonder... has she even talked to Norah about all of this?)"
        mc "(And has she ever met her um... donor?)"
    pause (1)
    stop music fadeout 07.0
    if cruel_prank == False and cc7 == True:
        mc "(Anyway, enough pondering. I'm about to arrive at the park.)"
    else:
        mc "(Anyway, enough pondering. I'm almost home now.)"
        jump after_park

    scene black with sdissolve
    $ renpy.pause (2, hard=True)
    scene c3r29 with sdissolve
    mc "(Ah, there she is.)"
    scene c3r28 with sdissolve
    van "Hey there, stud. So you came to see me after all."
    scene c3r27 with qdissolve
    mc "Here I am."
    scene c3r28 with qdissolve
    van "Come on. Walk with me for a few."
    play music "<loop 0.0>audio/orbit.ogg" fadein 09.0
    scene c3r26 with fadehold
    pause
    scene c3r25 with fadehold
    van "Here, this is the good bench. Come sit with me."
    scene c3r24 with fadehold
    pause (.5)
    van "So, after the other night..."
    van "You probably think I'm just some worthless slut, huh?"
    scene c3r23 with qdissolve
    pause (.5)
    mc "(Whoa. Where'd that question come from?)"
    menu:
        mc "(How do I even answer that?)"
        "No I Don't":
            $ pure +=1
            mc "Nah, I really don't. I mean... I don't know what was going through your head at the time..."
            scene c3r22 with dissolve
            mc "But I'm sure there was a good reason for it. And I'm not one to judge. There's plenty of guys out there who throw themselves at girls simply because they find them attractive."
            if van_romance == True:
                mc "Besides... I went along with it, didn't I? So were kind of in the same boat. Obviously it's something I also wanted."
            else:
                mc "Besides... it's not like we actually did anything."
        "Not Complaining":

            $ lust +=1
            mc "To be honest, I haven't really thought about it. And without knowing what was going through your head the other night, I'll reserve judgement."
            scene c3r22 with sdissolve
            mc "I don't even know you that well."
            if van_romance == True:
                mc "Regardless... you won't hear me complaining. I went along with it, and even enjoyed it. So were kind of in the same boat. Obviously, it's something I also wanted."
            else:
                mc "Besides... it's not like we actually did anything. Though, I kind of regret that in hindsight."
        "Obviously":

            $ dark +=1
            $ van_judgement = True
            mc "I mean... you did throw yourself at a complete stranger moments after laying eyes on him. I don't know a lot of girls who aren't sluts who would do that."
            scene c3r20 with sdissolve
            pause (.5)
            mc "Sorry if that's hurtful. I'm just being honest."
            if van_romance == True:
                scene c3r21 with qdissolve
                van "And what about you? You didn't seem to mind it."
                scene c3r20 with sdissolve
                mc "That's different. I'm a guy."
                van "..."

    scene c3r24 with sdissolve
    van "It doesn't matter anyway."
    van "People have always thought that about me. That I'm just some dumb slut. So what do I care if one more guy jumps on the bandwagon?"
    scene c3r17 with dissolve
    van "I've heard it my entire life. In school. In my head."
    van "But they're wrong, you know..."
    scene c3r15 with qdissolve
    if van_judgement == True:
        pause (.5)
        van "({i}You're{/i} wrong...)"

    scene c3r23 with dissolve
    pause (1)
    na "You give her time to process whatever she's thinking, unsure of what to say."
    pause (1)
    scene c3r14 with dissolve
    van "Heh."
    van "I still can't believe I did that. You know... throwing myself at you like some maniac."
    if van_romance == True:
        van "Having sex with some random guy I've never met before."

    van "But it's not what you think."
    scene c3r8 with qdissolve
    van "When I was young. In my teens."
    van "I had a rather serious relationship with someone."
    van "Someone I could really trust and confide in..."
    scene c3r12 with dissolve
    van "Or so I thought. I really, really thought I could trust this person."
    van "It was dumb."
    pause (.5)
    van "So you can imagine my shock when... not even two days after he and I..."
    scene c3r11 with qdissolve
    pause (1)
    van "I caught him sleeping with my best friend."
    van "My best friend in the entire world, a girl I'd known since I was little."
    van "It hurt me so much. I mean, I already had serious trust issues thanks to my father. So I vowed to never have sex with someone until I was absolutely certain I could trust them."
    scene c3r17 with dissolve
    van "It didn't matter though. He and my so-called \"best friend\" told the entire school that I was the one who cheated, and that I was just some conniving slut who took advantage of him. They needed a cover story to explain why he suddenly dumped me, and why they were together."
    van "Of course everyone bought it. I wasn't exactly popular to begin with. And it was two against one."
    scene c3r11 with dissolve
    pause (.5)
    van "{i}*Deep Breath*{/i}"
    pause (.7)
    scene c3r12 with dissolve
    van "They bullied me... relentlessly... after that.{w} Everyone.{w} It got so bad that I had to drop out."
    scene c3r20 with dissolve
    mc "Holy shit. That's horrible. People that age can be so cruel."
    mc "I'm sorry you had to go through all that."
    scene c3r21 with qdissolve
    van "It didn't end there.{w} There's a reason I'm telling you all this, I promise."
    scene c3r8 with qdissolve
    van "Like I said before, I vowed I'd never have sex with anyone. Not until I was sure I could trust them. But I wasn't being honest with myself."
    van "The truth is... I am just broken."
    van "So broken that I wouldn't even have sex with my own boyfriend of two years."
    van "The other day... a few hours before you and your date ran into me..."
    van "He dumped me."
    van "All because I wouldn't put out."
    pause (.3)
    scene c3r12 with dissolve
    van "Two years..."
    pause (1)
    scene c3r8 with dissolve
    van "But it wasn't his fault. What guy wouldn't? After two long years with no sex, no intimacy, nothing."
    pause (.4)
    scene c3r24 with dissolve
    van "Well..."
    scene c3r23 with qdissolve
    $ renpy.pause (.7, hard=True)
    scene c3r10 with sdissolve
    $ renpy.pause (.4, hard=True)
    van "{i}*Laughing*{/i}"
    $ renpy.pause (.5, hard=True)
    van "Life goes on, right?"
    scene c3r9 with qdissolve
    pause (1.5)
    scene c3r24 with sdissolve
    van "So I went to work."
    van "As usual, my boss treated me like shit."
    van "And then just as I was contemplating walking out, saying \"fuck it all.\""
    pause (.3)
    van "(And maybe something even worse...)"
    pause (.3)
    van "You and your girl walked in."
    scene c3r23 with dissolve
    van "{i}*Sniff*{/i}"
    pause (1)
    scene c3r14 with dissolve
    van "I thought to myself, \"He's hot. Would a guy like him even be interested in someone like me?\""
    van "I'm not going to lie, I was even a little envious of you and your... romantic partner."
    scene c3r23 with dissolve
    van "..."
    scene c3r6 with dissolve
    van "And then I had this crazy idea."
    van "I'd been battling with this stigma about sex and commitment for so many years. Clinging to this stupid notion that sex shatters relationships, because you're giving the guy the only thing they're truly sticking around for."
    van "They say the best way to overcome your fear is to face it head on, right?"
    van "So I figured... if I just force myself. Put myself in a situation where I can't back out, even if I wanted to... maybe that would help me to become normal again."
    scene c3r5 with qdissolve
    mc "Hold on a second. I'm trying to process all of this."
    mc "Are you saying that by throwing yourself at me the other night, you were trying to overcome some stigma about sex?"
    scene c3r6 with dissolve
    van "Yeah..."
    van "Heh. Stupid, right?"
    scene c3r5 with dissolve
    mc "Not really. Not after everything you just told me."
    scene c3r8 with dissolve
    van "D-Do you have any idea how bad it feels to be dumped simply because you won't sleep with someone?"
    van "I know I was wrong, but..."
    van "I thought I was doing the right thing."
    van "That it would in some weird way make him respect me more."
    scene c3r17 with dissolve
    van "So the night you came into the restaurant, I lashed out. If sex is all I'm good for, then I better just get used to it."
    scene c3r15 with qdissolve
    if van_romance == True:
        mc "Did it work? Do you feel less anxious about it?"
        scene c3r6 with dissolve
        van "Oddly enough, I think so. I mean, I really liked it. It wasn't all just an act."
        scene c3r5 with qdissolve
        mc "Believe me, I could tell."
        scene c3r6 with dissolve
        van "Haha, yeah."
        van "But as for whether or not it worked, I don't know."
    else:
        mc "Did I mess up your plan? Are you resentful that I turned you down?"
        scene c3r6 with dissolve
        van "No! Not at all. If anything I'm thankful."
        van "I mean I felt pretty stupid when you stopped me that night."
        van "But I probably would've felt even dumber if you fucked me."

    scene c3r5 with dissolve
    pause (.5)
    scene c3r17 with dissolve
    pause (.7)
    van "Do you think that you could maybe..."
    van "Grow to like someone like me?{w} Or will you forever see me as just some stupid, broken whore now? After what I did and... and everything you now know?"
    scene c3r15 with qdissolve
    mc "Hm..."
    mc "You know..."
    mc "I can fully appreciate why you felt the way you did. About sex, trust, and relationships."
    mc "In your position, after the trauma you experienced in what were supposed to be the best years of your life, anyone would."
    mc "But sex doesn't just magically make relationships work. And it shouldn't break them either."
    mc "This may be hard for you to hear, but if someone leaves you simply because you wouldn't put out, then they probably never cared that much to begin with."
    scene c3r7 with dissolve
    mc "The truth is sex shouldn't be complicated or stigmatized. It's meant to be gratifying. Fulfilling, even. After all... it's one of our most basic, natural human desires."
    mc "Now as for your question about whether or not I could grow to like someone like you..."
    scene c3r7 with purpflash
    scene c3r7 with purpflash
    scene c3r7 with purpflash
    menu:
        mc "(How should I answer her?)"
        "Most Likely":
            $ pure +=3
            mc "I'll be honest. I mean I don't know anything about you."
            mc "But from where I'm sitting, there's nothing wrong with \"someone like you.\""
            mc "Just like everyone else in this crazy world we live in, you're just a good person who's plagued by problems."
            mc "So I mean... yeah. I'm sure I could grow to like you. Assuming we have the opportunity to get to know each other a little better."
            jump vanessa_friendly
        "Maybe":

            $ lust +=3
            mc "I mean, I really don't know anything about you at all."
            mc "But I don't think there's anything wrong with you."
            mc "Just like everyone else in this crazy world we live in, you could just be a good person who's plagued by problems."
            mc "So I don't really know. It's certainly... possible. We'd have to get to know each other a little better first."
            mc "And for what it's worth, I think you're pretty hot."
            jump vanessa_friendly
        "Fuck No":

            $ dark +=3
            $ van_rejection = True
            mc "{i}*Sigh*{/i}"
            stop music fadeout 07.0
            mc "Look, I'm not one to sugar coat. And I appreciate you opening up to me."
            mc "But nah, probably not. You're not really my type. Romantically speaking, anyway."
            if van_romance == True:
                mc "That said, I'd still be open to the possibility of fucking. If you still are."
            else:
                mc "There's a reason I didn't fuck you the other night."
                mc "If that's not what you wanted to hear, I'm sorry. That's just the way it is."

            scene c3r4 with dissolve
            van "Ugh! What an asshole! You're just like everyone else."
            van "I'm out of here."
            scene c3r3 with sdissolve
            mc ".{w}.{w}."
            mc "(Welp. That went well. Time to go home.)"
            jump after_park

label vanessa_friendly:

    scene c3r6 with dissolve
    van "Thank you for being honest. I really needed this talk."
    van "And I'm sorry for taking up so much of your time. I know you said you had a busy day ahead of you."
    scene c3r5 with dissolve
    mc "Yeah. I actually do need to get going but..."
    mc "Feel free to call or text me if you want to hang out sometime."
    scene c3r6 with dissolve
    van "I definitely will. You seem like a really sweet guy."
    van "And for the record... I think that stigma I had about sex is finally gone.{w} So you know... call me."
    stop music fadeout 07.0
    scene c3r2 with dissolve
    van "Bye, [mc]."
    van "Mwah."
    scene c3r3 with fadehold
    pause (1)
    mc "(Wow...)"
    mc "(I'm going to need some time to think about all of this. That conversation did not go as I was expecting.{w} I had her pegged completely wrong.)"
    mc "(No time to ponder it now though. I should head home to the girls and see if they're ready. It's time to get this ball rolling.)"
    jump after_park

label after_park:

    scene black with sdissolve
    $ renpy.pause (3, hard=True)
    scene c3s23 with dissolve
    play music "<loop 0.0>audio/please_advise.ogg" fadein 08.0
    mc "(Home sweet home.)"
    pause (1)
    scene c3s22 with fade
    ali "Oh there you are, [mcd]. We're just finishing up getting ready."
    scene c3s21 with qdissolve
    mc "Okay good! I'd like to drive for a few hours while we still have some sunlight. Tell your sisters we need to hurry, okay?"
    scene c3s22 with dissolve
    ali "Sure, no problem! Just wait right here. We'll be ready in no time."
    scene c3s23 with fade
    pause (1)
    ali "{i}[mad], [liv], hurry up! [mcd] says we need to hurry!{/i}"
    pause (.7)
    grls "{i}Okay!{/i}"
    scene black with sdissolve
    na "You grab your bag and then wait by the door."
    scene c3s23 with ssdissolve
    mc "(Hm... this is taking a little longer than I expected.{w} I hope they're almost done.)"
    pause
    scene c3s20 with ssdissolve
    na "Soon, day becomes evening..."
    mc "{size=+10}Girls! We're losing sunlight!{/size}"
    mc "{i}*Mumbling*{/i} {size=-5}God damned females, always taking forever to get ready.{/size}"
    liv "Almost done! Sorry!"
    mad "We're coming!"
    mc "{i}*Sigh*{/i}"
    pause
    scene c3s19 with ssdissolve
    na "Then nightfall."
    mc "(That does it. I'm forcing them into that car.)"
    scene c3s18 with fadehold
    mc "{i}*Mumbling*{/i}"
    ali "Woo! Road trip! I'm so hyped up right now!"
    mad "Can you believe we got our own little lake house? We never get to do these sorts of things! It's going to be sooo awesome."
    scene c3s17 with sdissolve
    liv "Sorry again that we took so long, [mcd]."
    scene c3s16 with sdissolve
    mc "It's... fine. What matters is we're on the road now."
    scene c3s18 with sdissolve
    mc "Besides... if I stay focused on driving and just sleep for a few hours when we get there, it should be right about time to visit the cemetery."
    mc "I call dibs on the shower though. No way in hell am I going another day without one.{w} It's been too long.{w} You girls hear me?"
    scene c3s15 with sdissolve
    mc ".{w}.{w}."
    mc "Really?"
    mc "{i}*Mumbling*{/i} {size=-10}I'm getting that goddamned shower.{/size}"
    pause (.5)
    mc "(I'm literally cursed to never shower again in my life.)"
    mc "(Oh well. At least with them sleeping, it will be a peaceful drive. It'd probably just be easier if they slept the whole way.)"
    scene c3s18 with dissolve
    mc "(Time to focus on the road now.)"
    stop music fadeout 07.0
    pause
    mc "(...I'm definitely pulling over if I get tired.)"
    scene black with ssdissolve
    $ renpy.pause (3, hard=True)
    scene c3s14 with sdissolve
    pause (1)
    play music "<loop 0.0>audio/green_green_garden.ogg" fadein 09.0
    ali "{i}Is this the real life?{/i}"
    mad "{i}Is this just fantasy?{/i}"
    liv "{i}Caught in the landslide... no escape from realityyy.{/i}"
    scene c3s13 with fadehold
    mc "{i}I'm just a poor boy, nobody loves me.{/i}"
    grls "{i}He's just a poor boy, from a poor family. Spare him his life from this monstrosity.{/i}"
    scene c3s12 with fadehold
    grls "{size=+10}{i}BISMILAH, NOOO! WE WILL NOT LET YOU GO!{/i}{/size}"
    scene c3s11 with fadehold
    mc "Alright girls. Better get out and pee if you have to. Just making a quick stop here. We're almost to the lake house now, so speak up if you need anything."
    pause (.5)
    scene c3s10 with qdissolve
    mad "A liquor store? What for?"
    scene c3s11 with sdissolve
    mc "It's not {i}just{/i} a liquor store."
    pause (.5)
    mc "And besides... we {i}are{/i} on vacation, aren't we?"
    mad "Hmph!"
    mc "Don't tell me you've never drank or um... partied a little."
    scene c3s9 with dissolve
    if tbed == True:
        ali "Of course not, silly. We're only [age]!"
    else:
        ali "Of course not, silly!"
    scene c3s11 with dissolve
    mc "Hm... guess you're right. Anyways, sit tight!"
    scene c3s8 with fadehold
    pause (.5)
    mc "(I actually haven't decided if I'll let them drink or not yet. I suppose it could be fun and probably rather harmless so long as it's in a responsible environment.)"
    pause (.5)
    mc "(We certainly won't be doing any driving after.)"
    scene c3s7 with sfade
    clk "Howdy, Mister! How are ya this sunny afternoon?"
    scene c3s6 with qdissolve
    mc "(Cute accent.)"
    mc "Hello, sweetheart. A little tired, but I'm fine. How are you?"
    scene c3s7 with qdissolve
    clk "Awe, aren't you just sweet and chipper-like? I'm fine, thank ya."
    scene c3s5 with sdissolve
    pause (.5)
    clk "(God, he is too handsome for his own good. A guy like him would make my toes curl.)"
    pause (.5)
    scene c3s4 with sdissolve
    clk "I'm Jade by the way."
    scene c3s3 with qdissolve
    mc "Nice to meet you Jade. Name's [mc]."
    scene c3s5 with sdissolve
    mc "(Wow, people are really friendly in this town.)"
    scene c3s2 with sdissolve
    jad "You're all set! Have a good day, hon."
    scene c3s1 with sdissolve
    mc "Thanks. It was nice meeting you! Have a wonderful day."
    scene c3s2 with sdissolve
    jad "You too, handsome."
    scene c3s1 with sdissolve
    pause
    stop music fadeout 07.0
    scene black with sdissolve
    $ renpy.pause (2, hard=True)
    na "You arrive at the lake house without a hitch and finally take that long awaited shower."
    $ renpy.pause (2.5, hard=True)
    scene c3t8 with sdissolve
    play music "audio/glacier.ogg" fadein 06.0
    pause (.5)
    mad "Were you able to get ahold of Alita?"
    scene c3t7 with sdissolve
    liv "Unfortunately I wasn't! This stupid smartphone doesn't have any service!"
    scene c3t6 with dissolve
    ali "Don't worry, [onick]. I'm sure we'll be able to see her while we're here."
    scene c3t5 with sdissolve
    mad "I mean, she lives a pretty far drive from here, and last I heard her nana is pretty sick. I don't know if she'll be able to come see us, sadly."
    scene c3t4 with sdissolve
    ali "Doesn't hurt to try though!"
    scene c3t3 with sdissolve
    liv "Yeah, I'll keep trying."
    scene c3t2 with fadehold
    mc "(Ugh. Finally settled in here. What a long drive.)"
    mc "(At least I finally got that much needed shower when we arrived. I feel {i}amazing.{/i})"
    mc "{i}*Yawn*{/i}"
    mc "(The girls are unpacking and getting ready to visit their mom at the cemetery. Given their track record, that means I have a few hours to sleep.)"
    scene c3t1 with ssdissolve
    mc "(Oh sweet, sweet relaxation. This bed feels nice.)"
    pause (1)
    mc "..."
    mc "(I don't know if I'm exaggerating or not, but...)"
    mc "(I have a feeling today's going to be...{w} rough.)"
    mc "(But also... important. I don't know why I feel this way... I just have a strange feeling.)"
    mc "(I'm also a little shaken up after passing through my old hometown. At one point I was driving but a few miles from where the accident happened.)"
    stop music fadeout 06.0
    mc "(This lakehouse is a good fifteen miles from town though. So I guess... it's a little different.)"
    pause
    mc "(...I'm sorry I wasn't there, mom.)"
    pause
    scene black with ssdissolve
    play music "<loop 0.0>audio/amazing_grace.ogg" fadein 08.0
    $ renpy.pause (5, hard=True)
    scene c3u10 with ssdissolve
    $ renpy.pause (6, hard=True)
    scene c3u9 with fadehold
    $ renpy.pause (6, hard=True)
    scene c3u8 with fadehold
    $ renpy.pause (6, hard=True)
    scene c3u7 with fadehold
    $ renpy.pause (3, hard=True)
    scene c3u6 with sdissolve
    $ renpy.pause (1, hard=True)
    scene c3u5 with sdissolve
    $ renpy.pause (6, hard=True)
    scene black with sdissolve
    $ renpy.pause (4, hard=True)
    scene c3u4 with ssdissolve
    pause (1)
    mc "..."
    mc "(So it's... really her.)"
    pause (1)
    mc "(I'm looking right at the girl I've been dreaming about for more than a decade.)"
    mc "(Must be some... fragment of my memory.)"
    pause (1)
    mc "(I just wish I could remember.)"
    pause (1)
    mc "(If I had to guess I'd say she's just as laid back and sweet in person as she is in my dreams. The kind of person whose mere existence can brighten up the lives of those around her. Especially her loved ones.)"
    mc "(I may not remember it... but I think I'm extremely lucky to have met her. Even if for a short time.)"
    pause (1)
    mc "(Gracie...)"
    pause (.5)
    menu:
        mc "(I don't know you, but at the same time I feel like I lost someone I...)"
        "Love":
            mc "..."
            pause (.5)
            mc "(Like I lost someone I love.)"
            mc "(It's like a huge part of me is missing, and I'll never be whole again.)"
            mc "(I'm sorry I wasn't there for you...)"
        "Care For":
            mc "..."
            pause (.5)
            mc "(Like I lost someone I care for deeply.)"
            mc "(If you didn't get sick I could've...{w} gotten to know you.)"
            mc "(You'll be truly missed.)"
        "...":
            mc "..."
            pause (.5)
            mc "(Rest in peace, gorgeous.)"
            mc "(I hope someday I'll see you.{w} In the afterlife.)"

    scene black with ssdissolve
    $ renpy.pause (2.3, hard=True)
    scene c3u3 with ssdissolve
    pause (1)
    mc "(Mom and dad...)"
    pause (1)
    mc "(I can't stay long because I need to be there for the girls.)"
    mc "(But...)"
    mc "(Thank you for all you've done for me.)"
    mc "(You're the reason I was born, and the reason I had a second chance at this life.)"
    mc "(I wish you could've met the triplets.{w} You would've adored them.)"
    mc "(And while I haven't known them for long... I know they would've loved you.)"
    scene c3u2 with fadehold
    stop music fadeout 08.0
    mc ".{w}.{w}."
    scene black with sdissolve
    $ renpy.pause (5, hard=True)
    play music "<loop 0.0>audio/american_idle.ogg" fadein 06.0
    ala "Yo! Over here!"
    scene c3v3 with sdissolve
    pause
    scene c3v2 with sdissolve
    ala "This is going to be a {i}long one{/i}, dude. I hope you're ready."
    pause (1.2)
    scene c3v1 with sdissolve
    pause (1)
    ala "..."
    ala "(The triplets are going to be so freaking excited.)"
    pause (2)
    ala "(.{w}.{w}.I hope they're home. I hadn't even thought about that part.)"
    scene black with ssdissolve
    if pure >= 35:
        $ purity = True
    elif lust >= 35:
        $ lustful = True
    elif dark >= 35:
        $ darkness = True

    $ ch3_complete = True
    pause (1)
    jump end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
