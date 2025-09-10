screen main_menu():
    tag menu
    
    # Play menu music
    on "show" action Play("music", audio.menu, loop=True)

    # Zoomed out mailbox background with romantic atmosphere
    add "images/mailbox.png":
        zoom 0.8  # Zoom out the background
        blur 2    # Slight blur for dreamy effect
    
    # Romantic gradient overlay
    add Solid("#000000", alpha=0.4)  # Dark base
    add Solid("#4a1a2c", alpha=0.3)  # Deep romantic purple
    
    # Soft vignette effect
    add "gui/overlay/main_menu.png" alpha 0.6
    
    # Game title with romantic styling
    text "The Ink":
        size 72
        color "#f8e6d3"  # Warm cream color
        xalign 0.5
        yalign 0.15
        text_align 0.5
        outlines [(3, "#2c1810", 0, 0)]  # Dark brown shadow
    
    # Elegant menu buttons with romantic styling
    vbox:
        xalign 0.5  # Center the buttons
        yalign 0.65
        spacing 20

        # Custom styled buttons
        textbutton _("Begin Story"):
            action Start()
            text_size 32
            text_color "#f8e6d3"
            text_hover_color "#ffd4a3"
            text_outlines [(2, "#2c1810", 0, 0)]
            background None
            hover_background Frame("gui/button/hover_background.png", 10, 10)
            padding (20, 10)
            
        textbutton _("Continue Journey"):
            action ShowMenu("load")
            text_size 28
            text_color "#e6d2b8"
            text_hover_color "#ffd4a3"
            text_outlines [(2, "#2c1810", 0, 0)]
            background None
            hover_background Frame("gui/button/hover_background.png", 10, 10)
            padding (20, 8)
            
        textbutton _("Settings"):
            action ShowMenu("preferences")
            text_size 28
            text_color "#e6d2b8"
            text_hover_color "#ffd4a3"
            text_outlines [(2, "#2c1810", 0, 0)]
            background None
            hover_background Frame("gui/button/hover_background.png", 10, 10)
            padding (20, 8)
            
        textbutton _("Farewell"):
            action Quit(confirm=True)
            text_size 28
            text_color "#e6d2b8"
            text_hover_color "#ffd4a3"
            text_outlines [(2, "#2c1810", 0, 0)]
            background None
            hover_background Frame("gui/button/hover_background.png", 10, 10)
            padding (20, 8)

    # Decorative elements
    # Floating letter particles (optional - requires particle system)
    add "images/mailbox.png" alpha 0.3:
        xalign 0.5
        yalign 0.5
