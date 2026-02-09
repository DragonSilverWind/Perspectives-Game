define Mother = Character("Pężyra")
define Husband = Character("Rządziwoj")
define Son = Character("Mieczysław")
define Daughter = Character("Jagódka")

define Advicers = Character("Advicers")
define Servant1 = Character("Young servant")
define Guardian = Character("Guardian")
define Messenger = Character("Messenger")

####### ACCT I #######

label start:

    scene bg castle

    "Act I"
    
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
    "The news shows that other clans/kingdomes continue to create an alliance against Rządziwoj's clan and gather forces."
    "Rądziwoj and his advicors discuss about the threat and ways to replay on it."
    "There will be some dialogue options for Pężyra to join the discussions, but all her attempts will be ignored or criticalized as *women know nothing about politics*."
    hide Husband
    hide Advicers
    "After the deiberation, Pężyra decided to chceck how her son handles with a sword training."

label trening:
    show bg training field

    show Son
    show Servant1 at right

    "Pężyra walks into the training field just to see how Mieczysław loses sparring match with a young servant and starts to bastes on him."
    menu:
        "Mieczysław! Stop right now!":
            $ lojalny = True
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
            $ lojalny = False
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
            $ swieca = False
            jump napad

label dobranocka:
    show bg daughters room

    Mother "Which story would you like to listen today?"
    Daughter "I don't know..."
    menu:
        "I will tell you your favourite story":
            "Pężyra tells Jagódka her favourite story. It gives player some important informations about a lore (but different than in other option)."
        "I will tell you a story, which have you never heard about.":
            "Pężyra tells Jagódka her favourite story. It gives player some important informations about a lore (but different than in other option)."
    Mother "Good night, Jagódko."
    Daughter "Mommy, wait! Can you leave me a candle?"
    Mother "You are seven years old, Jagórdka. Are not you a little to old to be afraid of darkness?"
    Daughter "I'm not afraid!"
    menu:
        "Okey, I will leave you a candle.":
            $ swieca = True
            Daughter "Thank you, mommy! I love you!"
            Mother "I love you too, Jagódka. Good night."
            Daughter "Good night, mommy!"
        "So that means that you are brave enough to sleep without a candle.":
            $ swieca = False
            "Pężyra snuffs the candle."
            Mother "Good night, Jagódka. You are very brave."
            Daughter "Good night."

    hide Daughter
    jump napad

####### Akt II #######

label napad:
    scene bg mothers room night
    "Act II"
    
    "Pężyra is waken up by some screams."
    "She can hear more of them."
    "And the sound of striking swords."
    "And she can smell smoke."
    "Her room's door opens rapidly."
    show Guardian at right
    "Pężyra sees one of her husbands soldiers."

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
            Guardian "The lord has told me that you may not trust me. He told me this secret code. *tells secret code*" 
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
            Guardian "As you wish, my lady. But their rooms are in different part of the palace. We can't be in two places in the same time.!"
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
    "Fortunately, on the way through the castle's corridors, Pężyra gathers her clans warriors into a one group."
    show Mother at left
    "Pężyra founds her husband giving orders for his soldiers."
    hide Guardian
    show Husband 
    Husband "Pężyrko! What are you doing here!? You should get to a shelter!"
    Mother "I will not hide when our clan is under an attack! And I will not leave till I will be sure our children are safe."
    Husband "I have already sent warriors for them. Messengers should be back in any moment."
    show Messenger at right
    Messenger "My lord!"
    Husband "Speak! Where is my son!?"
    Messenger "We... we failed you, my lord..."
    "Pężyra hears Jagódka's scream from her room's window."
    "If the player has choosen to snuff Jagódka's candle, her scream end quickly. Otherwise, Pężyra sees a fire in Jagódka's room. Her daugher screams stops after a longer time."
    Mother "No... I can't be..."
    Husband "You traitor! *he raises his sword*"
    Messenger "My lord! Mercy! Only I've survived a battle!"
    Husband "So you should have fallen with your prince!"
    menu:
        "Rządziwoj! Stop!":
            Husband "He has failed us! He has not protected our children!"
            Mother "But he can still save our clan!"
            "Rządziwój lower his sword, uncertain."
            Mother "We need every soldier. I am sure that he will not fail us again."
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
            "They have seen how she fell."
            "But they never felt safe again."
            "They known that the ghost of the mother without children, the wife without children, will hunt them till the end of their days."
            "The alliance's clans are scared of her name till this day."
            "In her clan, mothers still give her name to their daughters."
            "They believe that it will bring strength and courage to their hearts."
            "Because they know that Pężyra will overwatch their clan till the end of the time"
            jump end
        "The castle is lost. We have to retreat. We need to gather our forces.":
            Guardian "But were will we go?"
            Mother "We will hide in the caves. We know them better than our enemies. They will not find us there."
            Guardian "Yes, my lady."
            "Pężyra led the retreat. She manages to save some soldiers and servants, but the castle burns to the ground."
            jump rebelia

label syn:
    scene bg castle corridor
    "The castle is engulfed in chaos. The invaders ripped through the walls. They are everywhere."
    show Mother at left
    show Guardian at right
    "On the way through the castle's corridors, Pężyra gathers her clans warriors into a one group. "
    scene bg training field
    show Mother at left
    show Guardian at right
    "Pężyra finally find Mieczysław on the training field, where he and some soldiers try to fight invaders."
    show Son 
    "Mieczysław warriors were outnumbered, but with Pężyra's warriors' support, the chances are equal."
    if lojalny:
        "One of the invaders shoot from a bow to Mieczysław. The young servant shields the prince with his own body."
        "Other inviders on the training field are killed by Pężyra's soldiers."
        "But only half a dozen is able to fight. Many were killed or wounded."
        "The young servant's state is the worst."
        Mother "Is there any healer?"
        Guardian "No, my lady."
        Son "How many of our warriors are still able to fight?"
        Guardian "Seven, my prince."
        Mother "We can not stay here. Jagódka may be in danger and our lord..."

        "Pężyra hears Jagódka's scream from her room's window."
        "If the player has choosen to snuff Jagódka's candle, her scream end quickly. Otherwise, Pężyra sees a fire in Jagódka's room. Her daugher screams stops after a longer time."
        "In the same time Pężyra hears screams of triumf. The invaders have killed her husband."
        Guardian "Our lord, what our orders?"
        Son "Lord... I?... But..."
        Guardian "Your father has fallen, my lord. Now you are our ruler."
        Son "I... we... we have to revenge my father!"
        Guardian "As you wish, my lord."
        menu:
            "You will. After you will gather your forces and prepere a plan.":
                Son "No! I won't run away! I am not a coward!"
                menu:
                    "You won't revenge him if you will die to!":
                        Son "Do you think I am weak, mother?!"
                        Son "I will prove you're wrong!"
                        Son "Follow me, those who are still loyal to our clan! We will show our strength!"
                        hide Son
                        hide Guardian
                        "Soldiers follow Mieczysław. All of them dies in the battle."
                        "Pężyra was captured by the allience forces and executed, as she was the last of her clan."
                        jump end
                    "You are not ready for this fight. The enemy outnumbers us. Your soldiers are wounded.":
                        Son "It is not important! The true warrior do not escape!"
                        Mother "True warriors protect their clan. Who will protect our villages, if all protectors fall here?"
                        Son "But..."
                        Guardian "Your mother is right, my lord."
                        Son "Then... then we reatret."
                        Guardian "As you command, my lord."
                        jump dziedzic
                    "It is not an escape. Let our enemies think they won. They will be not prepared when you will strike back.":
                        Son "Yes! My revenge will be legendary! We reatreat!"
                        "Pężyra, Mieczysław and their soldiers safely escapes through the secret passage. The invaders have burned the castle to the ground."
                        jump dziedzic
            "Your father would be proud of you.":
                Son "Mother, it is not safe here. You should run away."
                menu:
                    "You are right, my son. You will find me, after you will revenge your father.":
                        "With her guardian help, Pężyra safely escapes from the castle. But her son dies in the battle."
                        hide Son
                        hide Guardian
                        jump ucieczka
                    "There is no safe place now. I will fight on your side.":
                        Son "It will be an honour."
                        "Mieczysław and Pężyra led their soldiers to the battle."
                        "They fought bravely, but they were outnumbered by the enemy."
                        "Pężyra and Mieczysław fell with swords in their hands."
                        "The clan died with them."
                        jump end
        jump dziedzic
    else:
        "The fight comes to the end, but rappidly Mieczysław is backstabbed by a young servant, the one who trained the previous day with him."
        hide Son
        "Pężyra's guard quickly kills the traitor, but Mieczysław's wound is deep."
        "Other invaders on the training field are killed by Pężyra's soldiers."
        "But only half a dozen is able to fight. Many were killed or wounded."
        "Mieczysław state is the worst."
        Mother "Where is a healer!?"
        Guardian "I know some basics, my lady. But your son needs a quick medical help. He must be taken to a safe place."
        Mother "But Jagódka and Rądziwoj..."
        "Pężyra hears Jagódka's scream from her room's window."
        "If the player has choosen to snuff Jagódka's candle, her scream end quickly. Otherwise, Pężyra sees a fire in Jagódka's room. Her daugher screams stops after a longer time."
        "In the same time Pężyra hears screams of triumf. The invaders have killed her husband."
        Guardian "My lady?"
        Mother "Take us to the secret "
        "Pężyra decides to retreat survivors and take her son into a safe place."

        jump dziedzic

    jump end

label corka:
    scene bg castle corridor
    "The castle is engulfed in chaos. The invaders ripped through the walls. They are everywhere."
    show Mother at left
    "On the way through the castle's corridors, Pężyra gathers her clans warriors into a one group."
    "When they reach Jagódka's room, they see three invaders entering into it."
    "They hear Jagódka's scream."
    "Pężyra's soldiers rapidly get into the room."
    scene bg daughters room
    show Mother at left
    show Daughter at right
    if swieca:
        "The lonely candle, which Pężyra has left to Jagódka, lights the room."
        "An invader tries to attack Jagódka with his sword. She jumps away." 
        "But she falls on a table with a candle."
        "The candle fires toys on the table. Jagódka screams, when her face hits the fire."
        "Everyone can smell the burned skin."
    else:
        "A torch in one of Pężyra's soldier hand lights the room."
        "They see how an invader attacks Jagódka with a sword."
        "She tries to jump away."
        "But she is to slow."
        "An end of the sword cuts her face."
    Mother "Jagódka!"
    hide Daughter
    "Pężyra runs for Jagódka and gets her out of the room."
    show Daughter at center
    "Her soldiers kills the invaders. Jagódka cries."
    Mother "Is it here any healer?!"
    show Guardian at right
    Guardian "No, my lady. We have to take her out of the castle now!"

    show Messenger at right
    Messenger "My lady! Thank Perun! I was scared that they've hunted you too!"
    Mother "Me too? What do you mean?"
    Messenger "I'm sorry, my lady. We fought with our all strengh, but..."
    Messenger "Your son has fallen."
    Mother "No!"
    hide Messenger
    Daughter "Mommy? What has happend to Mieczysław?"
    menu:
        "Don't worry, Jagódka. We will speak about it later.":
            Daughter "Okey, mommy."
            "Jagódka tries to not cry."
        "Your brother has fought the enemies but there were more of them. He is in Nawia now.":
            Daughter "He left us?"
            Mother "He did not want to, but he had to."
    "Pężyra takes Jagódka in her armes."
    Mother "Shhh, my honey. I am with you."
    "Jagódka hugs Pężyra."
    show Guardian at right
    Guardian "My lady, what are our orders?"
    Mother "We have to find my hus..."
    "Pężyra hears screams of triumf. The invaders have killed her husband."
    Mother "Take us to the secret passage. Quickly!"
    "Pężyra with her daughter and soldiers escaped, but the castle was burned to the ground."
    show bg village
    show Mother
    show Daughter at left
    "After the escape, Pężyra and Jagódka found a shelter in one of her clans village."


    jump trauma

label ucieczka:
    show bg village
    show Mother
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

####### Akt III #######

label rebelia:
    scene bg cave
    "Act III"
    
    show Mother 
    "On this path, Pężyra joins a rebelion against the alliance."
    "Because she is a women, many soldiers and nobels don't want to follow her orders."
    "Players choices determinates, if she becomes a leader of the rebelion or if soldiers will left her or some else will take leadership from her."
    "By the whole time she is haunted by the ghosts of her children, begging her for revenge (son) or help (daughter)."
    "There will be options to help the ghosts, for example by traditional slavic rituals (dziady), but then she will not be able to fully get involved into rebelion, which will weaken her position and the whole rebelion."
    "If the player will always choose children, they ghosts will finally leave the world in peace, but the rebelion will fall."
    "If the player will fully focus on the rebelion, Pężyra will become a queen again. She will be a good ruler, but because of the trauma, she won't marry and have children again, so after her death her clan will go to a chaos again."
    "If the player will try to balance both rebelion and children, both goals will not be achived."

    jump end

label dziedzic:
    scene bg cave
    "Act III"

    show Mother at left
    show Son at right
    "On this path, Mieczysław takes a lead over the rebelion against the alliance and aimes to sit on his father's throne."
    "But Mieczysław is young and most of his decisions are not wise."
    "The player has to choose if Pężyra lets her son do whatever he wants or if she tries to change his decisions."
    "By integrating too much Mieczysław will be frustrated of lack of control and he will lose respect of his people."
    "There will be an options to advice Mieczysław in maniplative way, making him think it was all his idea. He will go to megalomania and loose respect to his mother."
    "By the whole time Pężyra is haunted by the ghosts of her daughter, calling for help from darkness/fire (candle decision)."
    "There will be options to help the ghost, for example by traditional slavic rituals (dziady), but then Pężyra will have to leave Mieczysław and the rebelion."
    "Focusing on Jagódka's ghost she will finally find peace, but leaving the power in Mieczysław hands will lead the rebelion to fall."
    "Focusing on the rebelion and Mieczysław will lead to sucesfull revenge and Mieczysław will take over the throne, but Pężyra will be always hanted by the ghost and with time she will not be able to help Mieczysław."
    "Based on player decidions, Mieczysław will totaly ignore advices, won't be able to act without them. It can be balanced."


    #"Secret ending option: Mieczysław runs away with the servant. (I have no idea which decision will led to it but my friend told me I had to put it here.)"
    jump end

label trauma:
    #show bg village
    #show Mother
    #show Daughter at left
    "On this path, Pężyra is asked to led the rebelion against the alliance."
    "The player can agree or refuse and focus on Jagódka."
    "She has to deal with big trauma after the attack. The trigger is darkness or fire (depending on the candle choice)."
    "By the whole time Pężyra is haunted by the ghost of her son, demanding for a revenge."
    "There will be options to help the ghost, for example by traditional slavic rituals (dziady), but then Pężyra will have to ignore Jagódka's needs and the rebelion."
    "Even with the player will choose to focus on the rebelion, her lidership will be challenged all time, because she is a women."
    "If the player will focus on rebelion, it will succed. Pężyra will become a queen and Jagódka after her. Because of her trauma, Jagódka will not be a good ruler and the clan will come to chaos."
    "If the player will focus on Jagódka, she will finally recover from a trauma, but Pężyra will be haunted by her son ghost and never find peace."
    "Focusing on Mieczysław's ghost will let him finally find peace in the afterlife, but Jagódka will never recover from trauma and the rebelion will fall."


    jump end

label end:
    "THE END"
    return