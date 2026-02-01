# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Mother = Character("Pężyra")
define Husband = Character("Rządziwoj")
define Son = Character("Mieczysław")
define Daughter = Character("Jagódka")

define Advicers = Character("Advicers")
define Servant1 = Character("Young servant")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg castle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy
    #
    "Prologue"
    
    "This part will entroduce the player the characters, their relationships and lore."
    "It will show signs of comming catastrophe, but there are no way to prevent it, just to preper for it."

    jump czy_narada


    # These display lines of dialogue.

    # This ends the game.

    return

label czy_narada:

    scene bg castle_corridor

    show Mother at left 
    show Advicers at right 

    Advicers "*discussing something about the incoming deliberation*"

    "That's weird. Normally the deliberations starts after a dinner."

    show Husband

    Mother "My lord..."

    hide Advicers

    Husband "Honey, not now. A messenger has delivered us very worring news from the border. We need to talk about it imidietly."

    menu:
        "I am sorry, my husband. I have not intended to interrupt you.":
            Husband "Has something important happend? Is it about our son?"
            Mother "No, it is nothing important. We can talk about it later."
            Mother "I will go and see how our son handles with sword training."
            Husband "Of course. I will join you later."
            hide Husband
            jump trening
        "What has happend?":
            Husband "I can not speak about it here."
            menu:
                "I see. I will not interrupt you":
                    Mother "I will go and see how our son handles with sword training."
                    Husband "Of course. I will join you later."
                    jump trening
                "Let me join you":
                    Husband "Why? It is not a place for a women."
                    Mother "I should now about everything that may threaten our son and your heir."
                    Husband "You are right. He should be prepeard for all the dangers and his mother shoud not be blind on them to guid him."
                    jump narada

        "Then, I will join you at the deliberation.":
            Husband "It is not a place for a women."
            Mother "I should now about everything that may threaten our son and your heir."
            Husband "You are right. He should be prepeard for all the dangers and his mother shoud not be blind on them to guid him."
            jump narada


    jump end

label narada:
    show Advicers at right
    show Husband
    show Mother at left
    show bg deliberation_room

    "Pężyra and Rądziwoj enter deliberation room. The advicers already wait. They look at Pężyra."

    Husband "Let's begin!"
    Advicers "My lord, should we wait till..."
    Advicers "*looks again at Pężyra*"
    Husband "It is my wish to let my wife hear these news! She should now everything that can threaten our son."
    Advicers "Yes, my lord."

    Advicers "*one of them gives a report of worring news*"
    "The news shows that other clans/kingdomes continue to create an alliance against Husband and gather forces."
    "Rądziwoj and his advicors discuss about the threat and ways to replay on it."
    "There will be some dialogue options for Pężyra to join the discussions, but all her attempts will be ignored or criticalized as *women know nothing about politics*."

label trening:
    show bg training_field

    show Son
    show Servant1 at right

    "Pężyra walks into the training field just to see how Mieczysław loses sparring match with a young servant and starts to bastes on him."
    menu:
        "Mieczysław! Stop right now!":
            "Mieczysław immediately looks ashamed."
            Son "But mother, a prince should not be defeated by a servant..."
            menu:
                "That means that you have not trained hard enough. ":
                    Son "Yes mother. I will be better next time."
                "That means that you found a great warrior who might serve you well when you will become a king.":
                    Mother "If you will treat him with a respect."
                    Son "Yes, mother..."
                    Mother "And what should a future king say to his feature great warrior?"
                    Son "You fought well."
                    Mother "And you will become a glorious warrior, a protector of feature king."
                    Servant1 "Thank you, my lady. I'll do my best!"
        
        "Let him do that":
            ""
    hide Son
    hide Servant1
    show Daughter at right
    "Jagódka runs to Pężyra through training field."
    Mother "Jagódka! What are you doing here? You should go to bed!"
    Daughter "I know, mummy... but I can't sleep if you won't tell me a story!"
    menu:
        "All right. I will tell you a story.":
            Daughter "Yay!"
            jump dobranocka
        "I can not, honey. I have a lot of work to do.":
            Daughter "But mommy..."
            Mother "I will tell you one tomorrow, all right? If you will nicely go to bed now."
            Daughter "Okey...."
            jump end

label dobranocka:
    show bg daughters_room

    Mother "Which story would you like to listen today?"
    Daughter "I don't know..."
    menu:
        "I will tell you your favourite story":
            Daughter "This one about *something important for lore*?"
            Mother "Yes, this one..."
        "I will tell you a story, which have you never heard about.":
            ""

    jump end


label end:
    "THE END"
    return