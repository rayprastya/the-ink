# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.
label start:
    # Initialize variables
    $ luna_choice = ""
    $ drink_choice = ""
    
    jump day1_scene1

# --- ACT 1 - DAY 1 ---
label day1_scene1:
    # Background: TrainStation
    scene trainstation with fade
    show trainstation at bg_zoomed
    
    # Music: chill for dialogue scenes
    play music chill fadeout 1.0 fadein 1.0
    
    show luna_neutral at center
    
    show luna_neutral at center
    luna "Another late night on the rails..."
    
    luna "Brilliant. That makes it the fourth time this week I've missed dinner."

    hide luna_neutral
    
    show luna_tired at center
    
    luna "Sometimes I wonder why I even bother. All this running around for headlines no one reads."
    
    luna "Chasing politicians who don't give a toss... rewriting the same bloody press release until my eyes blur."
    
    hide luna_tired

    show luna_sad at center
    
    luna "I'm just... tired. Worn thin, like a teabag used one too many times."
    
    luna "I wish I had someone to talk to. Not just about work, but everything. Y'know?"
    
    luna "...Someone who actually gives a damn."

    hide luna_sad
    show luna_neutral at center
    
    luna "Well, maybe it's time to visit Isaiah. He always listens to my blabbering."
    
    jump day1_scene2

label day1_scene2:
    # Background: Coffee shop
    scene black with fade
    scene coffeshop with fade
    show coffeshop at bg_zoomed
    
    # Music: chill continues (already playing)
    
    show luna_neutral at right, flipped, jump
    luna "Evening, Isaiah. Still open or are you just hiding from the world again?"
    
    show isaiah_smile at left_male, jump
    isaiah "For you, Luna? Midnight Brew never closes."
    
    show isaiah_smile at left_male, jump
    isaiah "Your usual?"
    
    show luna_neutral at right, flipped, jump
    luna "Go on, guess. I dare you."
    
    show isaiah_smile at left_male, jump
    isaiah "Easy. One moody brew with a splash of milk and the crushing weight of journalistic disappointment."
    
    hide luna_neutral
    show luna_rolls_eyes at right, flipped, jump
    
    luna "Cheeky. But... yeah, spot on."
    
    show isaiah_smile at left_male, jump
    isaiah "What happened this time? Did they make you chase down another minister's dog-walker?"
    
    show luna_rolls_eyes at right, flipped, jump
    luna "Worse. I rewrote a press release about potholes. Five times. Then they printed the original draft."
    
    show isaiah_smile at left_male, jump
    isaiah "That's criminal. You should sue for emotional damage."
    
    show luna_rolls_eyes at right, flipped, jump
    luna "I should sue for caffeine."
    
    show isaiah_smile at left_male, jump
    isaiah "Good thing you've got a supplier."

    hide luna_rolls_eyes
    show luna_smile at right, flipped, jump
    
    menu:
        "What would I do without you?":
            $ luna_choice = "grateful"
            
            show luna_smile at right, flipped, jump
            luna "What would I do without you?"
            
            show isaiah_smile at left_male, jump
            isaiah "Probably perish on Platform 3 from undercaffeination and existential dread."
            
            show luna_smile at right, flipped, jump
            luna "Exactly my point."
            
            show isaiah_smile at left_male, jump
            isaiah "One existential flat white coming right up."
        
        "Stop flirting with me and make the coffee.":
            $ luna_choice = "deflect"
            
            show luna_smile at right, flipped, jump
            luna "Stop flirting with me and make the coffee."
            hide isaiah_smile
            show isaiah_grin at left_male, jump
            
            isaiah "Rude, but fair."
            
            show isaiah_grin at left_male, jump
            isaiah "One emotionally repressed flat white coming right up."
            hide isaiah_grin
        
    # Optional SFX or idle animation here like steaming milk, soft café ambient
    
    show isaiah_smile at left_male, jump
    show luna_smile at right, flipped
    
    isaiah "You ever thought about quitting?"
    
    show luna_smile at right, flipped, jump
    luna "Every day. Right after I clock in."
    
    show isaiah_smile at left_male, jump
    isaiah "Figures. But you've got something more in you, Luna. Not just newsprint and deadlines."
    
    show luna_smile at right, flipped, jump
    luna "Well... if I had it my way, I'd be writing novels and running a tiny coffee shop stacked with second-hand books."
    
    show isaiah_smile at left_male, jump
    isaiah "Now that sounds like a dream I could brew to."
    
    show luna_smile at right, flipped, jump
    luna "It's silly, isn't it? The whole writer-by-day, barista-by-heart cliché."
    
    show isaiah_smile at left_male, jump
    isaiah "Nah. It's very you, actually. Caffeine and plot twists — sounds like a bestseller."
    
    show luna_smile at right, flipped, jump
    luna "I'll trade press releases for prose any day. But dreams don't cover rent in London."
    
    show isaiah_smile at left_male, jump
    isaiah "True. But neither does burnout."
    
    hide luna_smile
    show luna_smile at right, flipped, jump
    
    luna "But thanks. For the coffee. And for listening."
    
    show isaiah_smile at left_male, jump
    isaiah "Always, luv. Midnight Brew's policy — caffeine and free therapy, all in one cup."
    
    show luna_smile at right, flipped, jump
    luna "You should put that on a sign."
    
    show isaiah_smile at left_male, jump
    isaiah "You write the copy, I'll get the chalk."
    
    show luna_smile at right, flipped, jump
    luna "Alright. I better go now."
    
    show isaiah_smile at left_male, jump
    isaiah "See you tomorrow, Luna."
    
    show luna_smile at right, flipped, jump
    luna "Yeah... same time, same tired soul."
    
    hide isaiah_smile
    hide luna_smile
    
    jump day1_scene3

label day1_scene3:
    # Background: mailbox
    narrator "Luna walks alone, the dim streetlights casting long shadows as the quiet settles in around her. She notices something…"
    
    scene black with fade
    scene bg_mailbox_street_night with fade
    show bg_mailbox_street_night at bg_zoomed
    
    # Music: mailbox for mailbox scenes
    play music mailbox fadeout 1.0 fadein 1.0
    
    show luna_walking at center
    
    luna "Huh... A mailbox?"
    
    luna "Has this always been here?"
    
    luna "I walk this street every night and I've never noticed it... Must be the overtime fogging up my brain."
    
    luna "Strange place for it though... No houses round here, Not many people come this way."
    
    hide luna_walking
    show luna_thinking at center
    
    luna "Well... it's not like anyone uses these anymore."
    
    luna "..."
    
    narrator "Luna opens the mailbox, rummaging inside of it."
    
    luna "Hmm?"
    
    luna "There's a piece of paper inside..."
    
    luna "Blank. Odd."
    
    hide luna_thinking
    show luna_smile at center
    
    luna "Well, if no one's using it... might as well make this my personal therapy box."
    
    hide luna_smile
    show luna_writing at center
    
    luna "Dear whoever finds this—today, I endured yet another day behind a desk. My coffee turned cold not once, but twice. And I swear, some part of me drifted away sometime after the clock struck three."
    
    luna "I wanted to scream into the void. Instead, I wrote to you. Whoever you are."
    
    narrator "Luna folds the paper and puts it inside the mailbox."
    
    luna "There. All folded like a proper letter."
    
    luna "Back in you go, mystery box."
    
    luna "Weirdly... that felt kind of nice."
    
    luna "Right. Time for dinner I'll probably sleep through."
    
    narrator "Luna goes home."
    
    scene black with fade
    
    jump day2_scene1

# --- DAY 2 ---
label day2_scene1:
    # Background: train station
    narrator "On the second day, the routine repeats itself—overtime again. Luna boards the commuter train home, her body aching from long hours of work. By the time she arrives, the night air outside the station feels like a quiet relief."
    narrator "Just as her feet hit the platform and she takes her first real breath of the evening... her phone rings."
    
    scene trainstation with fade
    show trainstation at bg_zoomed
    
    # Music: chill for dialogue scenes
    play music chill fadeout 1.0 fadein 1.0
    
    show luna_tired at center
    
    luna "Ugh… not now."
    
    narrator "She checks her phone. It's Mr. Phil."
    
    luna "Brilliant."
    
    narrator "She answers the call reluctantly."
    
    mrphil "Luna! Finally. Thought you were dodging my calls again."
    
    luna "Evening, Mr. Phil. I just got off the train."
    
    mrphil "Yeah, yeah. Listen, change of plans. That feature on corporate fraud? It's due next week, not in two. Editor's breathing down my bloody neck."
    
    luna "...You said two weeks, sir."
    
    mrphil "Well, I say a lot of things, don't I? Just get it done. You're fast with words. Use that fancy degree of yours."
    
    luna "Right. Of course. Anything else moved up while we're at it?"
    
    mrphil "Not unless the sky falls, no. And Luna—less grumbling, more hustling."
    
    narrator "He hangs up. Luna sighs deeply and pockets her phone."
    
    luna "Charming as ever."
    
    luna "Honestly. One of these days, I'm throwing my phone into the River Thames."
    
    jump day2_scene2

label day2_scene2:
    # Background: coffee shop
    scene black with fade
    scene coffeshop with fade
    show coffeshop at bg_zoomed
    
    # Music: chill continues (already playing)
    
    narrator "After another long day filled with sighs, deadlines, and Mr. Phil's nasal voice echoing in her head, Luna found herself once again drifting toward the only place that made sense after 9 PM—Midnight Brew."
    
    show luna_neutral at right, flipped
    
    show luna_neutral at right, flipped, jump
    luna "Isaiah, tell me you've got something strong. My supervisor just turned my week into a war zone."
    
    show isaiah_grin at left_male
    
    show isaiah_grin at left_male, jump
    isaiah "Oof, that bad? What's the old fossil done this time?"
    
    menu:
        "The usual boring order":
            $ drink_choice = "usual"
            show luna_neutral at right, flipped, jump
            luna "Just the usual. No surprises. I've had enough excitement from Mr. Phil for one lifetime."
        
        "Something sweet to calm her from that old fart":
            $ drink_choice = "sweet"
            show luna_neutral at right, flipped, jump
            luna "Hit me with something sweet. I need sugar to erase the memory of Phil's voice."
    
    if drink_choice == "usual":
        show isaiah_grin at left_male, jump
        isaiah "One moody flat white, coming up. You sure you don't want something to melt the rage?"
        show luna_neutral at right, flipped, jump
        luna "The rage is permanent. Coffee just keeps it civil."
    
    if drink_choice == "sweet":
        show isaiah_grin at left_male, jump
        isaiah "I've got just the thing. Caramel cream latte with enough syrup to drown a man."
        show luna_neutral at right, flipped, jump
        luna "Perfect. If it puts me in a coma, even better."
    
    show isaiah_grin at left_male, jump
    isaiah "So what did Sir Deadline Doom do now?"
    
    show luna_neutral at right, flipped, jump
    luna "Moved our deadline forward by a whole week. On a Friday. While I was still on the train home."
    
    show isaiah_grin at left_male, jump
    isaiah "Yikes. Did he break the news gently or...?"
    
    show luna_neutral at right, flipped, jump
    luna "He said, and I quote: 'Hey champ, quick heads-up, we're gonna need that big one done by next Friday, cool?' Like it's some casual favor, not a 30-page report."
    
    show isaiah_grin at left_male, jump
    isaiah "Classic managerial gaslighting. Was he eating crisps while saying it too?"
    
    show luna_neutral at right, flipped, jump
    luna "Yes. Loudly. I could hear every crunch."
    
    show isaiah_grin at left_male, jump
    isaiah "That should be illegal."

    hide luna_neutral
    show luna_sigh at right, flipped, jump

    luna "Anyway… after hanging up, I was too annoyed to go straight home. Took the long way round and passed that weird alley behind the train yard."
    
    show isaiah_grin at left_male, jump
    isaiah "The one no one walks through unless they've lost their will to live?"
    
    show luna_sigh at right, flipped, jump
    luna "That's the one. And guess what? Found an old mailbox. Just sitting there. No house, no building. Like it'd fallen out of time."
    
    show isaiah_grin at left_male, jump
    isaiah "That... is oddly poetic. Did it have anything inside?"
    
    show luna_sigh at right, flipped, jump
    luna "I haven't checked. But I'm tempted. Something about it felt... off. Like it was waiting."
    
    show isaiah_grin at left_male, jump
    isaiah "You sure it wasn't just caffeine withdrawal making you hallucinate?"
    
    show luna_sigh at right, flipped, jump
    luna "At this point, I wouldn't even mind if it was. At least hallucinations don't have deadlines."
    
    show isaiah_grin at left_male, jump
    isaiah "True. Unless you're writing about them."
    
    show luna_sigh at right, flipped, jump
    luna "Don't tempt me."
    
    show isaiah_grin at left_male, jump
    isaiah "Anyway, drink's almost ready. You gonna check that box today?"
    
    show luna_sigh at right, flipped, jump
    luna "Yeah. I think I will."
    
    show isaiah_grin at left_male, jump
    isaiah "Then may the beans be with you."
    
    show luna_sigh at right, flipped, jump
    luna "And also with your grind."

    hide luna_neutral
    hide isaiah_grin

    jump day2_scene3

label day2_scene3:
    # Background: mailbox
    scene black with fade
    scene bg_mailbox_street_night with fade
    show bg_mailbox_street_night at bg_zoomed
    
    # Music: mailbox for mailbox scenes
    play music mailbox fadeout 1.0 fadein 1.0
    
    narrator "On her way home, Luna's feet moved on their own, leading her back to the oddly-placed mailbox. She told herself it was just curiosity... but deep down, something pulled her there."
    
    show luna_neutral at center
    
    luna "I wonder... is my silly letter still in there?"
    
    narrator "She opened the small rusted door slowly, heart oddly quickened. But what she found made her take a step back."
    
    hide luna_neutral
    show luna_surprised at center
    
    narrator "The letter inside wasn't hers. The handwriting was different. Neater. Like ink spilled straight from an old soul."
    
    luna "What...?"
    
    narrator "She unfolded the paper, hands trembling slightly. It was a response—someone had read her letter. And replied. Poetic. Thoughtful."
    
    show letter_overlay with dissolve
    
    narrator "The letter read:"
    
    narrator "{i}Dearest stranger,{/i}"
    narrator "{i}Your words reached me like the last coal of warmth in a frostbitten trench. To survive another day — that is no small feat, you know. The world does not always reward quiet endurance, but I see it, even from afar.{/i}"
    narrator "{i}I too have known the kind of hour that saps the soul, when the hands on the clock feel more like shackles than guides. Cold coffee is a grief I know well, though mine came from tin cups near muddy boots.{/i}"
    narrator "{i}Take heart. If your soul slipped out at three, then may it return to you in dreams — or in ink, as yours did to me.{/i}"
    narrator "{i}With all the gentleness a worn heart can spare,{/i}"
    narrator "{i}— E.{/i}"
    
    hide letter_overlay with dissolve
    
    hide luna_surprised
    show luna_confused at center
    
    luna "...Okay. This is weird. Who would even bother replying?"
    
    narrator "Her first instinct was to look around. But the street was empty, just the soft hum of distant trains and the occasional breeze brushing past."
    
    hide luna_confused
    show luna_smile at center
    
    luna "Well... maybe someone out there just needed a reason to write back. Maybe it's not so bad."
    
    narrator "She stared at the blank page, then grinned to herself."
    
    luna "(Let's see if my mysterious pen pal is still listening...)"
    
    narrator "With a deep breath, she began writing."
    
    hide luna_smile
    show luna_writing at center
    
    show letter_overlay with dissolve
    
    narrator "Luna's Second Letter:"
    
    narrator "{i}To whoever dwells behind ink and kindness,{/i}"
    narrator "{i}Today, the forces of bureaucracy conspired against me, pushing my deadline forward by 1 whole week. I swear the office breathes deadlines and exhales despair.{/i}"
    narrator "{i}He speaks in sighs and scoffs, his breath stale with instant brew and authority.{/i}"
    narrator "{i}So here I am again, writing to a mailbox like I've got nowhere else to go — which is probably true. But your letter made the world feel a little less... Heavy.{/i}"
    narrator "{i}If this finds you, I hope your trench is less muddy, and your coffee warm.{/i}"
    narrator "{i}— A tired but surviving Luna{/i}"
    
    hide letter_overlay with dissolve
    
    narrator "She smiled, folded the paper, and slipped it into a new envelope."
    
    luna "(Let's see if you write back again, ghost poet.)"
    
    narrator "She walked off into the night, the hum of city life trailing behind — and something just a little magical lingering in the air."
    
    scene black with fade
    
    # End of current content
    return