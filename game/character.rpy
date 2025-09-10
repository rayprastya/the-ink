# Character definition
define luna = Character("Luna", color="#b8a878")  
define mc = Character("Luna", color="#b8a878")  
define isaiah = Character("Isaiah", color="#8b4513") 
define mrphil = Character("Mr. Phil", color="#ff9999")
define narrator = Character("", color="#ffffff")
define f = Character("Fajar")
define z = Character("Zara")

# Shared transform
transform character_style:
    yalign 0.1
    # xalign 0.5
    # zoom 1.2

transform left:
    xalign 0.1
    yalign 0.1

transform left_male:
    xalign 0.1
    yalign 0.5

transform right:
    xalign 0.9
    yalign 0.1

transform center:
    xalign 0.5
    yalign 0.1

transform flipped:
    xzoom -1.0

# Background zoom transforms
transform bg_zoomed:
    zoom 0.85  # Zoom out backgrounds slightly
    
# Character talking jump animation
transform talking_jump:
    easein 0.1 yoffset -10
    easeout 0.1 yoffset 0

# Simple talking jump that can be combined with other transforms
transform jump:
    easein 0.1 yoffset -10
    easeout 0.1 yoffset 0

# Combined position + jump transforms
transform left_jump:
    xalign 0.1
    yalign 0.1
    easein 0.1 yoffset -10
    easeout 0.1 yoffset 0

transform right_jump:
    xalign 0.9
    yalign 0.1
    easein 0.1 yoffset -10
    easeout 0.1 yoffset 0

transform center_jump:
    xalign 0.5
    yalign 0.1
    easein 0.1 yoffset -10
    easeout 0.1 yoffset 0

transform left_male_jump:
    xalign 0.1
    yalign 0.5
    easein 0.1 yoffset -10
    easeout 0.1 yoffset 0

# Transition effects
define fade = Fade(0.5, 0.0, 0.5)
define slide_left = PushMove(1.0, "pushleft")
define slide_right = PushMove(1.0, "pushright")

# Character expressions - using existing sprites
image mc_neutral = "Journalist_idle_0000.png"
image mc_tired = "Journalist_idle_0001.png"
image mc_sad = "Journalist_idle_0002.png"
image mc_smile = "Journalist_idle_0003.png"

image luna_neutral = "Journalist_idle_0000.png"
image luna_tired = "Journalist_tired.png"
image luna_sad = "Journalist_sad.png"
image luna_smile = "Journalist_smile.png"
image luna_rolls_eyes = "Journalist_idle_0004.png"
image luna_softsmile = "Journalist_idle_0003.png"
image luna_surprised = "Journalist_idle_0002.png"
image luna_confused = "Journalist_idle_0001.png"
image luna_thinking = "Journalist_idle_0001.png"
image luna_writing = "Journalist_idle_0000.png"
image luna_sigh = "Journalist_idle_0002.png"
image luna_walking = "Journalist_idle_0000.png"

image isaiah_neutral = "Barista.png"
image isaiah_grin = "Barista_grin.png"
image isaiah_smile = "Barista_smile.png"

# Letter overlay system
image letter_overlay = Text("", size=24, color="#333333", outlines=[(2, "#ffffff", 0, 0)])

# Background images
image bg_mailbox_street_night = "images/mailbox.png"  # Using room as placeholder for now

# Music definitions - add your music files to audio/ folder
define audio.chill = "audio/chill.ogg"  # For dialogue scenes
define audio.mailbox = "audio/mailbox.mp3"  # For mailbox scenes
define audio.menu = "audio/menu.mp3"  # For loading screen/main menu

# Sprite definitions
image mc default:
    "Journalist_idle_0000.png"
    0.1
    "Journalist_idle_0001.png"
    0.1
    "Journalist_idle_0002.png"
    0.1
    "Journalist_idle_0003.png"
    0.1
    "Journalist_idle_0004.png"
    0.1
    repeat

image luna default:
    "Journalist_idle_0000.png"
    0.1
    "Journalist_idle_0001.png"
    0.1
    "Journalist_idle_0002.png"
    0.1
    "Journalist_idle_0003.png"
    0.1
    "Journalist_idle_0004.png"
    0.1
    repeat

image f default:
    "images/mockup_char_alter_color.png"

image z default:
    "Timeline 1_0000.png"
    0.1
    "Timeline 1_0001.png"
    0.1
    "Timeline 1_0002.png"
    0.1
    "Timeline 1_0003.png"
    0.1
    "Timeline 1_0004.png"
    0.1
    "Timeline 1_0005.png"
    0.1
    repeat