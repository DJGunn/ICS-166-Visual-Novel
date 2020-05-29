# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_("Eileen"), color="#cc88cc", image="eileen")
define l = Character(_("Loki"), color="#2ae6ff", image="loki")
define g = Character(_("Garm"), color="#fffc30", image="garm")
define lg = Character(_("Loki and Garm"), color="#ff3033")
define h = Character(_("Helpful Person"), color="#3033ff")
define ge = Character(_("Grand Entrance"), color="33cc33")
define ggse = Character(_("GG Store Employee"), color="#f10ee1", image="ggse")

transform singlebounce:
    pause .15
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    yoffset 0

# stop bouncing by showing character again without bounce
transform multibounce:
    pause .15
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    yoffset 0
    repeat

# moves character downwards
transform depress:
    pause .15
    yoffset 0
    easein .175 yoffset 20

# define colors for use
init:
    image black = Solid((0, 0, 0, 255))
    image white = Solid((255, 255, 255, 255))
    image grey = Solid((128, 128, 128, 255))

# python code for credits-related things
init python:
    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

    class Inventory:
        # credits == credits
        def __init__(self, credits=20):
            self.credits = credits
            self.items = []

        def buy(self, item):
            if self.credits >= item.cost:
                self.credits -= item.cost
                self.items.append(item)
                return True
            else:
                return False

        def earn(self, amount):
            self.credits += amount

        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False


# The game starts here.

default gq_menuset = set()

label start:

    # python runs at the moment the game starts
    # this means that all items that need to be bought need to be put here
    python:
        inventory = Inventory() # initializes number of credits too
        # for shop1
        choco = Item("Choco", 5)
        sushi = Item("Sushi", 20)
        fries = Item("Fries", 10)
        # for shop2
        tophat = Item("Golden Top Hat", 250000)
        suit = Item("Golden Suit", 750000)
        maxGGG = Item("Diamond Morph Suit", 1000050)

    # how to declare chapter
    scene black with dissolve

    show text "Chapter 2\nA True Gentleman?!" with Pause(5)

    # actual scene start
    scene black with dissolve
    show loki neutral   # this would use loki neutral.png/loki neutral.jpg when character is added to the images directory

    # you can have multi-line text
    l """
    {i}Ah yes, happy birthday to me, woo...{/i}

    {i}I really don't understand why people care so much about birthdays, for me it's basically a day to eat cake.{/i}

    {i}I don't like cake, but company is always welcome.{/i}
    """
    # scenes
    scene greenaurora with dissolve
    show loki neutral
    show garm happy at multibounce, right

    # These display lines of dialogue.

    g "KNOCK KNOCK!"

    l "Ugh, who's there?"

    g "IT'S ME!"

    l "What kind of joke is that?!"

    # b is for bold text
    "{b}Garm opens the door and enters Loki's room.{/b}"

    show loki neutral at left
    with move

    g "How are you doing on this fine day?!"

    # this is an example of what a route would look like, usually if you want to put a bad end in your chapter
    menu:

        "Now, how am I feeling today..."

        "Positive":

            jump positive

        "Negative":

            jump negative

# this is an example of what a more complex series of events could look like
label positive:

    # Initialize a variable.
    $ gg_power = 5

    scene greenaurora
    with dissolve

    show loki neutral at center

    # you can do multi-line dialogue with tags used sometimes
    l """
    {i}I guess I have no real reason to feel sad since I'm used to being poor, and also I'd be such a downer if I said I -wasn't- in a good mood today.{/i}

    {i}Sure, why not at least play along to being happy today?{/i}
    """
    show loki happy at singlebounce, center
    l "I can't wait to see what today has in store for me!"

    show garm happy at singlebounce, right
    g "Haha okay! Sorry I couldn't find a gift for you, so I'll just give you the credits I would have spent on a gift! What's your NeoMo?"

    l "{i}Aw they're so nice to me. They really didn't have to, but I can't turn them down when they're so willing to give me something for my birthday can I?{/i}"

    l "It's uh..."

    l @ neutral "{i}Man why did I name my NeoMo account this...{/i}"

    l @ neutral "TheRealLokiGG."

    # showing characters after they've already been shown will have the most recent effect happen
    # this removes the previous instance of that character
    show garm happy at multibounce, right
    g "HAHAHA, THAT'S SO FUNNY!"

    show loki sad at depress, center
    l "Please don't speak of it again, haaaa..."

    g "In any case, here you go!"

    # how to earn credits
    $ inventory.earn(20)
    $ current_credits = inventory.credits
    # to show a variable's value in dialogue, put brackets around it


    show loki happy at singlebounce, center
    l "Alright, I got it! Thanks so much! Now I have %(current_credits)d!"

    show garm happy at singlebounce, right
    g "You're welcome!"

    l "Well um... time to share it with you in the form of food!"

    show loki neutral at left
    show garm neutral at right
    with move

    jump preshop1
    jump shop1

label preshop1:
    $ chococost = choco.cost
    $ sushicost = sushi.cost
    $ friescost = fries.cost
    $ inventory.earn(1000000)
label shop1:

    menu store1:

        "What do I want..."

        # multiple things can happen after every menu choice
        "Chocolate %(chococost)d":
            if inventory.buy(choco):

                $ current_credits = inventory.credits
                "Your order will be delivered to your location in the next 30 minutes. You have %(current_credits)d credits remaining, thank you for using NeoFood!"
                jump resume1

        "Sushi %(sushicost)d":
            if inventory.buy(sushi):
                $ current_credits = inventory.credits
                "Your order will be delivered to your location in the next 30 minutes. You have %(current_credits)d credits remaining, thank you for using NeoFood!"
                jump resume1

        "French Fries %(friescost)d":
            if inventory.buy(fries):
                $ current_credits = inventory.credits
                "Your order will be delivered to your location in the next 30 minutes. You have %(current_credits)d credits remaining, thank you for using NeoFood!"
                jump resume1

label resume1:
    l "..."

    g "..."

    "{b}Looks at each other{/b}"

    lg "WHAAAAAAAAT?!" with vpunch

    lg "WHERE THE HECK DID THOSE CREDITS COME FROM?!"

    scene black with dissolve

    """
    They enjoyed their food and began to live the good life together.

    They weren't a couple, but Garm was Loki's only real friend and they both lived alone so it was Loki's choice for them to live together.

    Of course Garm refused at first, but Loki insisted since there would be no point in being rich with no one to share the riches with.

    Speaking of Fenrir...
    """
    show text "1 year later" with Pause(5)

    show loki neutral at depress, center

    "Loki woke up at 8AM per usual, but what was on his mind was unusual."

    l """

    {i}Living rich is nice since I don't really have a care in the world, but...{/i}

    {i}That thing that appeared by Fenrir way back when, what was that?{/i}
    """

    "Like, who thinks like that? Oh well, this makes my job easier."

    "Onwards with the story!"

    show garm happy at right

    g "You're awake right?"

    l "Yea-"

    show garm happy at multibounce, left
    with move

    "{b}Garm bounces into Loki's room and immediately rushes to open the blinds.{/b}"

    scene white with dissolve
    show loki neutral at depress, center
    show garm happy at multibounce, left

    l "MY EYES!" with hpunch

    g "GOOOOOOD MORNING!"

    "{b}Loki gets out of bed.{/b}"

    scene lokiroom with dissolve
    show loki neutral at center
    show garm happy at multibounce, left

    l "Agh... Um, Garm?"

    show garm happy at left

    g "Oh, what is it, Loki?"

    l "I just randomly had this thought this morning, but what was that thing way back when Fenrir-"

    show garm neutral at left

    l """
    Um, got taken away?

    There was something that appeared by her and I'm not sure if I'm just misremembering, but was that like a pet of hers or something?

    I still don't understand why Fenrir got taken away for something like that...
    """

    g """
    ...You're not crazy.

    That thing you're talking about is a Gentle Guy, but everyone calls them GGs.

    Well, people who know about them, that is.
    """

    l "Wait, you said that people know about them, who are these people?"

    g """
    The people include those of us with GGs, those who know others with GGs, and the LOLs.

    These are pretty self-explanatory, but the LOLs have the strongest GGs.
    """

    l "Oh, that makes sense. A year ago I was actually feeling pretty hopeless, you know being poor and not being able to do anything about it."

    show garm happy at left

    g "Haha, there's actually no real reason to feel totally hopeless!"

    l "{i}Thank goodness I'm not crazy, but now I have even more questions.{/i}"

    show loki neutral at right

    show garm neutral at left
    with move
    $ gqcount = 0
    $ gqbonus = 0

label garmquestions:
    menu:
        set gq_menuset
        l "What should I ask about..."

        "Wait, you said that people know about them, who are these people?":
            $ gqcount+=1

            g """
            The people include those of us with GGs, those who know others with GGs, and the LOLs.

            These are pretty self-explanatory, but the LOLs have the strongest GGs.
            """

            l "Wait, you said \"us\", do you mean to say that we both have GGs?"

            show garm happy at singlebounce, left

            g "Yep, that's exactly what that means!"

            l """
            Oh okay!

            ...

            ACTUALLY, WHY DIDN'T YOU TELL ME THIS BEFORE?!
            """

            g "You never asked!"

            menu:

                l "Oh um, well I guess that's true..."

                "Wait, but how do I have one?":

                    $ gqbonus = 1
                    show garm neutral at depress, left
                    g "Actually your parents and my parents were a part of the previous uprising against to LOLs, but they're either exiled from this area or dead now..."

                    l "Oh, can you teach me how to manifest a GG later? I'm probably going to have to sit and think for things a bit after I'm either done asking you questions or you get tired of answering them, haha."

                    show garm happy at left

                    g "Sure thing!"

                    show garm neutral at left

                    jump garmquestions

                "{i}Ask nothing{/i}":

                    jump garmquestions

        "Why did Fenrir have to be taken away for manifesting their GG?":
            $ gqcount+=1

            g "They probably didn't want some kind of force strong enough to cause an uprising against the LOLs so Tyr made the decision to lock her up."

            l "But she was only acting in self-defense!"

            g "Yeah, but the LOLs care more about maintaining their power than human rights."

            l "That's not good at all..."

            jump garmquestions

        "Wait, you said LOLs have the strongest GGs, so how do GGs get stronger?":
            $ gqcount+=1

            #g "Usually if one is related to someone who has a GG and/or a strong will to obtain something."

            #l "Wait, so since you're Fenrir's sister, does that mean you have a GG?"

            #https://www.finaltouchschool.com/business/10-qualities-of-a-modern-gentleman/
            g """
            GGs become stronger based on their owner. In principle, the more gentlemanly, ladylike for girls, you are, the stronger your GG will be.

            This can include showing a geniuine interest in the people you're interacting with, helping someone in need, being a truthful and effective communicator, being virtuous, and the list goes on.

            However, the LOLs don't show many of these qualities so they make their GGs stronger by from making their GG looking sharper since that's where they can have unlimited possibilities through sheer credits.
            """

            l "Um, so basically either be more of a gentleman or just use money?"

            g "Or..."

            show garm happy at singlebounce, left

            g "BOTH!"
            show loki happy at singlebounce, right
            l "HAHA alright gotcha!"

            show garm neutral at left
            show loki neutral at right

            jump garmquestions

        "I think I'm done asking questions.":
            jump resume2

label resume2:
    show garm neutral at left
    show loki neutral at center

    if gqcount==3 and gqbonus==1:
        $ gg_power+=10
        g "Alright! In the future, do remember that your decisions will influence the power of your GG, for better or for worse!"

        g "Good job on showing interest in everything I was saying or leading up to in our conversation!"

        l "Thanks for talking with me about all of those things, Garm!"

        l "{i}Wait, is Garm an esper? Oh well, Garm is Garm and that's all that matters.{/i}"

    elif gqcount==3:
        $ gg_power+=5
        g "Alright! In the future, do remember that your decisions will influence the power of your GG, for better or for worse!"

        l "Thanks for letting me know about things, Garm!"
    elif gqcount < 3 and gqcount!=0:
        $ gg_power+=3
        g """
        Alright! In the future, do remember that your decisions will influence the power of your GG, for better or for worse!

        I was super eager to tell you things, but you didn't ask me about everything you were wondering about, wink wink!
        """
        l "I don't know what you mean, but thanks for letting me know about things, Garm!"

        l "{i}Wait, is Garm an esper? Oh well, Garm is Garm and that's all that matters.{/i}"
    else:
        $ gg_power-=10
        show garm sad at depress, left
        g "Oh, I thought you wanted to know things..."

        l "Sorry, I think I'm okay."

        g "Hmm... if you say so."

        l "{i}It seems like I didn't do something right, or as right as I could have... I'll be more careful in the future, hopefully.{/i}"

    g "Alright! On to breakfast!"

    l "That sounds good, I'm starving."

    scene black with dissolve
    "Loki and Garm prepare some food and begin to eat."

    scene diningroom with dissolve
    show loki neutral at left
    show garm neutral at right

    l "After we eat, can you teach me how to use a GG?"

    g "Ah right, sure!"

    l "Wow you make that sound like it's easy to manifest a GG."

    hide garm neutral
    show garm happy at singlebounce, right

    g "It's not that it's easy, it's that I'm amazing!"

    g "Alright, time to go to the basement gym!"

    l "Okay, gotcha."

    scene indoorgym with dissolve
    show loki neutral at center
    show garm neutral at right

    g "Okay so think of what an ideal gentleman is to you, like really visualize it."

    l "Um okay got it."

    g "Now try REALLY hard to believe that it'll just pop out and become real."

    l "Mmmm... No actually can't do that part."

    g "Oh right, remember that episode of GoGo's Strange Venture where the main guy yells out \"SMOOTH PALMS\"?"

    l "Wait are you serious so I'm supposed to try to be all epic and come up with a name?"

    g @ happy "That's exactly what I'm telling you to do!"

    l """

    {i}Hmm, well a gentleman does stand out looking all cool and stuff...{/i}

    {i}Mmmm, he needs to have a pocket watch, monocle, and some cool looking suit...{/i}

    {i}So basically he stands out and people's eyes go towards him as he enters an area...{/i}

    {i}What do you even call that, a grand entrance?{/i}

    {i}Well, here goes nothing!{/i}

    IT'S TIME TO MAKE YOUR APPEARANCE, GRAAAAAND ENTRAAAAANCE!!!
    """

    show grandentrance at left with hpunch

    l "Ah okay."

    g "Yep, nice."

    lg "HOLY CRAP IT ACTUALLY WORKED!" with vpunch

    g """
    ... Alright, so that's how to manifest your GG! Now, if you have watched Dokimon you can tell your GG to do things.

    Also, the more enthusiastic you are about what you're saying when you control your GG, it will do the thing you want better.
    """
    menu:
        l "{i}Oh, well in that case I guess I can just choose some gentlemanly trait and make it more dramatic right?{/i}"

        "GRAND ENTRANCE, USE A DAZZLING GAZE AT GARM!":
            $ gg_power +=10
            g "Wha-"

            g @ happy "Oooo well hello handsome!"

            "Garm is now smitten with your GG, it was super effective!"

            l "AAAA THAT'S WEIRD YOU CAN STOP NOW GRAND ENTRANCE!"

            g "Ahm, wow yeah that's something I haven't seen before, good job!"

        "Grand Entrance, use fly?":
            $ gg_power -=5

            g "Didn't I just tell you that were were supposed to be enthusiastic? Dang it Loki..."

            g "Also if you didn't already notice, your GG is already flying..."

            l "Oh, you're right..."

            l "{i}I should really pay attention to what people are saying...{/i}"

    g "Yep, there are plenty of ways to use and not use your GG, but it'll be up to you to figure that out!"

    l "Um, so the LOL's don't really use the GGs by being all enthusiastic or gentlemanly right?"

    g "Right yeah, they buy stuff. Actually, do you want to go buy things for your GG?"

    menu:
        l "{i}That doesn't sound like a bad idea.{/i}"

        "Yes":
            g "Alright! Though, why did you pause for a second?"
        "Yes":
            g "Alright! Though, why did you pause for a second?"

    l "Um, no reason, lets go!"

    scene mall with dissolve
    show loki neutral at left
    show garm neutral at right

    l "You made it sound like a really casual thing by the way, Garm."

    g "What do you mean?"

    l "A store for GG stuff? If most people can't even have a GG, wouldn't that mean that a store for GGs would not be a common thing?"

    g "You're right, but it's actually a gaming shop as a front, but there's a section in the back for actual GG items!"

    l "Oh wow okay, what is it called?"

    g "You'll know, Loki, you'll know."

    scene ggstoresign with dissolve

    g "Yep, here we are!"

    l "ARE YOU KIDDING ME!" with vpunch

    l "Okay lets just go in..."

    g @ happy "HAHA! Yeah, lets!"

    scene ggstore with dissolve

    # credits to buy GG upgrades example

    jump preshop2
    jump shop2

label preshop2:
    $ tophatcost = tophat.cost
    $ suitcost = suit.cost
    $ maxGGGcost = maxGGG.cost

label shop2:

    menu store2:

        ggse "Welcome to the GG store, what can I get for you? You have %(current_credits)d credits."

        "Golden Top Hat (%(tophatcost)d credits)":
            if inventory.buy(tophat):
                l "This top hat defines a GG!"
                $ gg_power+=5
                $ current_credits = inventory.credits
                "You have %(current_credits)d credits remaining, thank you for using the GG Store!"
                jump resume3

        "Golden Suit (%(suitcost)d credits)":
            if inventory.buy(suit):
                l "A suit to enhance my GG!"
                $ gg_power+=10
                $ current_credits = inventory.credits
                "You have %(current_credits)d credits remaining, thank you for using the GG Store!"
                jump resume3

        "GG Max Level Book (%(maxGGGcost)d credits)":
            if inventory.buy(maxGGG):
                $ gg_power+=9001
                $ current_credits = inventory.credits
                "You have %(current_credits)d credits remaining, thank you for using the GG Store!"
                jump resume3

        "Actually, I think I'm done buying things.":
            jump resume3

label fallthrough:
    l "Not enough credits..."
    jump shop2

label resume3:

    # this is how to show a variable's value
    #"After all that the gg_power is now %(gg_power)d."
    if "tophat" or "suit" in items:
        g "Oho nice upgrade!"
    else:
        $ gg_power+=20
        g "Ooo, you don't want to buy things because you want to find your own strength, unlike the LOLs? That's pretty admirable!"

    # CONTINUE MARC

    "{b}Good Ending{/b}."
    # This ends the game.
    return

label negative:

    scene black
    with dissolve

    show loki neutral at depress, center

    l "I don't feel so good."

    g """
    Loki..?
    Loki?
    LOOOOOOOKIIIIIII!!!
    """

    "Loki died of..."
    "WAIT, HOW?!"

    "{b}Bad Ending{/b}."
    # This ends the game.
    return
