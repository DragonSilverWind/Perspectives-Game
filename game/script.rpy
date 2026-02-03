define Mother = Character("Pężyra")
define Husband = Character("Rządziwoj")
define Son = Character("Mieczysław")
define Daughter = Character("Jagódka")

define Advicers = Character("Advicers")
define Servant1 = Character("Young servant")
define Guardian = Character("Guardian")
define Messenger = Character("Messenger")

####### PROLOGUE #######

label start:

    scene bg castle

    "Prologue"
    
    "This part will entroduce the player the characters, their relationships and lore."
    "It will show signs of comming catastrophe, but there are no way to prevent it, just to preper for it."

    jump czy_narada

    return

label czy_narada:

    scene bg castle corridor

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
    show bg deliberation room

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
    hide Husband
    hide Advicers

label trening:
    show bg training field

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
            "Pężyra just watches how her son bastes a servant."
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
            jump napad

label dobranocka:
    show bg daughters room

    Mother "Which story would you like to listen today?"
    Daughter "I don't know..."
    menu:
        "I will tell you your favourite story":
            Daughter "This one about *something important for lore*?"
            Mother "Yes, this one..."
        "I will tell you a story, which have you never heard about.":
            "Something imoprtant about the lore"
    hide Daughter
    jump napad

####### Akt I #######

label napad:
    scene bg mothers room night
    "Act I"
    
    "Pężyra is waken up by some screams."
    "She can hear more of them."
    "And the sound of striking swords."
    "And she can smell smoke."
    "Her room's door opens rapidly."
    show Guardian at right
    "Pężyra sees one of her husbands soildiers."

    Guardian "My lady! We're under attack! You need to go a safty place!"

    show Mother at left
    jump informacje

label informacje:
    menu:
        "Let's go.":
            jump wybor
        "Wait! What about my children?":
            Guardian "I don't know. The lord has sent others for them."
            jump informacje
        "Who attacks us?":
            Guardian "The alliance against your husband, my lady. All of them."
            jump informacje
        "How can I trust you? You may be one of the invaders.":
            Guardian "The lord has told me that you may not trust me. He told me this message."
            jump informacje        
        "Where is my husband?":
            Guardian "He leads the defence on the walls."
            jump informacje

label wybor:
    Guardian "There is a secret passage, which leads out of the castle. The lord told me how to find it."
    menu:
        "After you.":
            "Pężyra safely escapes from the castle, but her familly dies in the attack. Smoke over the burned castle was seen through many days."
            jump ucieczka
        "I can not leave my husband in the darkest hour!":
            Guardian "But my lady! This is not safe! And he will be distructed if he'll have to protect you as well!"
            Mother "He knows I can care for myself. My presense on the walls will motivate our soldiers."
            Guardian "As you wish."
            jump klan
        "I will not leave without my children!":
            Guardian "But my lady! This is not safe!"
            Mother "As they are not safe! They need my support!"
            Guardian "As you wish, my lady. But their rooms are in different part of the palace."
            menu:
                "We will go for my son. We have to protect our heir.":
                    Guardian "Yes, my lady."
                    jump syn
                "We will go for my daughter. She must be very scared.":
                    Guardian "Yes, my lady."
                    jump corka
    jump end

label klan:
    scene bg catle wall
    "The castle is engulfed in chaos. The invaders ripped through the walls. They are everywhere."
    show Mother at left
    "Pężyra founds her husband giving orders for his soildiers."
    hide Guardian
    show Husband 
    Husband "Pężyrko! What are you doing here!? You should get to a shelter!"
    Mother "I will not hide when our clan is under an attack! And I will not leave till I will be sure our children are safe."
    Husband "I have already sent warriors for them. Messengers should be back in any moment."
    show Messenger at right
    Messenger "My lord!"
    Husband "Speak!"
    Messenger "We... we failed you, my lord..."
    "Pężyra sees smoke comming from rooms' windows of their children."
    Mother "No... I can't be..."
    Husband "You traitor! *he raises his sword*"
    Messenger "My lord! Mercy! Only I've survived a battle!"
    Husband "So you should have fallen with them!"
    menu:
        "Rządziwoj! Stop!":
            Husband "He has failed us! He has not protected our children!"
            Mother "But he can still save our clan!"
            "Rządziwój lower his sword, uncertain."
            Mother "We need every soildier. I am sure that he will not fail us again."
            Messenger "I won't! I swear on Perun!"
            "Rządziwój takes away his sword."
            Husband "I will follow my wife's wisdom. You will protect her with your life."
            Messenger "I will, my lord!"
        "He deserves death.":
            "Rządziwój cuts off messengers head."
            Husband "One traitor less."
    hide Messenger
    Husband "We lost our children. But there will be the time for grief after the battle. We can not lost our clan."
    Mother "I will fight on your site, my husband. We will avange our lost."
    "A lonely arrow rips Rządziwoj's flank."
    Mother "Rządziwój!"
    Husband "*cough* Pężyrko... listen to me... I won't survive it..."
    Mother "No, you can't! I can't lost you too!"
    Husband "Promise me... *cough* Promise me that you will take care about our clan."
    Mother "I will. You will be proud of me when we will meet again."
    Husband "I will be. *cough* I know it. I love you, Pężyrko."
    Mother "I love you too."
    hide Husband
    "Rzędzisław dies in Pężyra's arms."
    show Guardian at right
    Guardian "My lady? What are our orders?"
    menu:
        "We will fight till the last drop of blood!":
            "Pężyra takes the sword of her husband."
            Mother "We will not leave the one we lost unavanged!"
            "Pężyra led her clan's warriors to the battle."
            "The blade of her husbnad sword turned red."
            "Soldiers of the allience, who survived the battle, talked about her fury."
            "Some of them have seen how she killed all allience leaders."
            "They have seen, when she fell."
            "But they never felt safe again."
            "They known that the ghost of the mother without children, the wife without children, will hunt them till the end of their days."
            "The alliance's clans are scared of her name till this day."
            "In her clan, mothers still give her name to their daughters."
            "They believe that it will bring strength and courage to their hearts."
            "Because they know that Pężyra will overwatch their clan till the end of the time"
            jump end
        "The castle is lost. We have to retreat. We need to gather our forces.":
            Guardian "But were will we go?"
            Mother "We will hide in the caves. We know them better than our enemies. We will not find us there."
            Guardian "Yes, my lady."
            "Pężyra led the retreat."
            jump rebelia

label syn:
    scene bg castle corridor
    jump end

label corka:
    scene bg castle corridor
    jump end

label ucieczka:
    show bg village
    hide Guardian
    hide Mother
    "After her escape, Pężyra found a shelter in one of her clans village."
    "Every night she was haunted by ghosts of her children."
    "Sometimes Pężyra thought she can hear their screams or see their shadows even during the day."
    "People, who survieved attack on the castle came to Pężyra and asked her for leadership against the alliance."
    "She refused."
    "She left."
    "Some legends says that the last queen of the clan walked as long as she found the end of the world."
    "Other says that she was caught and executed by the alliance."
    "One claims that she just hung herself on a tree."
    "All of them agree, that she was never seen on her clan's land again."
    jump end

label rebelia:
    scene bg cave
    "Act II"
    jump end

label end:
    "THE END"
    return