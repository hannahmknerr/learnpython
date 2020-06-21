from random import *
def chopped_app():
    """appetizer round of chopped"""
    print()
    print("You know the rules. 3 rounds. Mandatory mystery ingredients. If your dish doesn't cut it, you will be chopped.")
    print('-'*50)
    print("Please check out your ingredients for the appetizer round!")
    app_mystery_basket_options = ['pizza dough', 'onions', 'carrots', 'spinach', 'basil', 'tortillas', 'apple', 'seafood', 'avocado', 'cheese', 'vegan cheese', 'vegan milk', 'jam', 'strawberries','granola','salsa']
    print("And you've got...")
    app_mystery_basket = [choice(app_mystery_basket_options), choice(app_mystery_basket_options), choice(app_mystery_basket_options)]
    print('-'*50)
    print(app_mystery_basket)
    print()

    """testing if any ingredients need to be swapped"""
    app_chop_swap = input("Need to swap out any ingredients? (Y/N):").strip('!?.').lower()
    pos = ['yes', 'y', 'si', 'oui']
    if app_chop_swap in pos:
        app_bad_basket = True
        while app_bad_basket == True:
            app_chop_swap_choice = input("Sorry about that! Which one?:")
            app_mystery_basket.pop(app_mystery_basket.index(app_chop_swap_choice))
            app_mystery_basket.append(choice(app_mystery_basket_options))
            print(app_mystery_basket)
            app_good_basket = input("All better? (Y/N)?").strip('!?.').lower()
            if app_good_basket in pos:
                app_bad_basket = False

    print('-'*50)
    print(app_mystery_basket)
    print("20 minutes for the first round. Clock starts...NOW!")
    print('-'*50)

    """beginning of the scoring"""
    app_score = 0
    print("Appetizer Round: \n Chef Jeff, what have you made for us today?")
    app_creativity = input().split()
#    print(app_creativity)
    boring_app_options = ['cheese plate', 'quesadillas', 'deconstructed', 'basic']
    for i in app_creativity:
        if i in boring_app_options:
            app_score = app_score - 5
    app_usage = input("Were you able to use all 3 ingredients? (Y/N):")
    if app_usage in pos:
        app_score = app_score + 5
    app_taste = int(input("How does it taste? (0-10):"))
    app_score = app_score + app_taste
    app_presentation = int(input("How is your presentation? (0-10):"))
    app_score = app_score + app_presentation

    if app_score > (25/2):
        print("Congratulations. You were not chopped.")
        return True
    else:
        print("I'm sorry. You've been chopped.")
        return False
def chopped_main():
    """main course round of chopped"""
    print()
    print("Welcome to the entree round.")
    print('-'*50)
    print("Open your baskets!")
    main_mystery_basket_options = ['puff pastry', 'shallots', 'celery', 'arugula', 'cilantro', 'tortilla chips', 'banana', 'plant based protein', 'zucchini', 'parmesean', 'vegan cheddar cheese', 'fruit beverage', 'peanut butter', 'noodles','lemon','soy sauce']
    print("And you've got...")
    main_mystery_basket = [choice(main_mystery_basket_options), choice(main_mystery_basket_options), choice(main_mystery_basket_options)]
    print('-'*50)
    print(main_mystery_basket)
    print()

    """testing if any ingredients need to be swapped"""
    main_chop_swap = input("Need to swap out any ingredients? (Y/N):").strip('!?.').lower()
    pos = ['yes', 'y', 'si', 'oui']
    if main_chop_swap in pos:
        main_bad_basket = True
        while main_bad_basket == True:
            main_chop_swap_choice = input("Sorry about that! Which one?:")
            main_mystery_basket.pop(main_mystery_basket.index(main_chop_swap_choice))
            main_mystery_basket.append(choice(main_mystery_basket_options))
            print(main_mystery_basket)
            main_good_basket = input("All better? (Y/N)?").strip('!?.').lower()
            if main_good_basket in pos:
                main_bad_basket = False

    print('-'*50)
    print(main_mystery_basket)
    print("30 minutes for this round. Clock starts...NOW!")
    print('-'*50)

    """beginning of the scoring"""
    main_score = 0
    print("Entree Round: \n Chef Jeff, what do you have for the judges?")
    main_creativity = input().split()
#    print(app_creativity)
    boring_main_options = ['sandwhich', 'quesadillas', 'deconstructed', 'pizza', 'basic']
    for i in main_creativity:
        if i in boring_main_options:
            main_score = main_score - 5
    main_usage = input("Were you able to use all 3 ingredients? (Y/N):")
    if main_usage in pos:
        main_score = main_score + 5
    main_taste = int(input("How does it taste? (0-10):"))
    main_score = main_score + main_taste
    main_presentation = int(input("How is your presentation? (0-10):"))
    main_score = main_score + main_presentation

    if main_score > (25/6.5):
        print("You were not chopped!!")
        return True
    else:
        print("Chef Jeff, your dish is on the chopping block.")
        return False
def chopped_dessert():
    """dessert course round of chopped"""
    print()
    print("Welcome to the last round.")
    print('-'*50)
    print("Let's see what's in those baskets.")
    d_mystery_basket_options = ['waffle cones', 'ice cream', 'gummy bears', 'sprinkles', 'icing', 'ganache', 'fudge', 'whipped cream', 'banana', 'cherries', 'salt', 'sugar', 'peanut butter', 'noodles','lemon','honey', 'yogurt']
    print("And you've got...")
    d_mystery_basket = [choice(d_mystery_basket_options), choice(d_mystery_basket_options), choice(d_mystery_basket_options)]
    print('-'*50)
    print(d_mystery_basket)
    print()

    """testing if any ingredients need to be swapped"""
    d_chop_swap = input("Need to swap out any ingredients? (Y/N):").strip('!?.').lower()
    pos = ['yes', 'y', 'si', 'oui']
    if d_chop_swap in pos:
        d_bad_basket = True
        while d_bad_basket == True:
            d_chop_swap_choice = input("Sorry about that! Which one?:")
            d_mystery_basket.pop(d_mystery_basket.index(d_chop_swap_choice))
            d_mystery_basket.append(choice(d_mystery_basket_options))
            print(d_mystery_basket)
            d_good_basket = input("All better? (Y/N)?").strip('!?.').lower()
            if d_good_basket in pos:
                d_bad_basket = False

    print('-'*50)
    print(d_mystery_basket)
    print("30 minutes for this round. Clock starts...NOW!")
    print('-'*50)

    """beginning of the scoring"""
    d_score = 0
    print("Dessert Round: \n Chef Jeff, what do you have for the judges?")
    d_creativity = input().split()
#    print(app_creativity)
    boring_d_options = ['cheese plate', 'quesadillas', 'deconstructed', 'basic', 'sandwhich', 'bread pudding', 'cupcake']
    for i in d_creativity:
        if i in boring_d_options:
            d_score = d_score - 5
    d_usage = input("Were you able to use all 3 ingredients? (Y/N):")
    if d_usage in pos:
        d_score = d_score + 5
    d_taste = int(input("How does it taste? (0-10):"))
    d_score = d_score + d_taste
    d_presentation = int(input("How is your presentation? (0-10):"))
    d_score = d_score + d_presentation

    if d_score > (25/8):
        print("You were not chopped!!")
        return True
    else:
        print("Chef Jeff, your dish is on the chopping block.")
        return False
def chopped_full():
    """full game of chopped"""
    if chopped_app() == True:
        print("On to the main course!")
        if chopped_main() == True:
            print("And now for dessert...")
            if chopped_dessert() == True:
                print("Congratulations! You are a chopped champion!")
    else:
        print("Try again next time.")
def chopped():
    chopped_input = False
    while chopped_input == False:
        print("Would you like to play the full game or just one round?")
        chopped_options = ['full', 'app', 'main', 'dessert']
        print(chopped_options)
        chopped_choice = input().strip('!?.').lower()
        if chopped_choice == 'app':
            chopped_app()
            chopped_input = True
        elif chopped_choice == 'main':
            chopped_main()
            chopped_input = True
        elif chopped_choice == 'dessert':
            chopped_dessert()
            chopped_input = True
        elif chopped_choice == 'full':
            chopped_full()
            chopped_input = True
        else:
            print("I don't recognize that option?")
def making_it_fast():
    fast_craft_options = ['write', 'draw', 'color', 'paint', 'compose', 'knit']
    fast_craft_topics = ['childhood', 'family', 'love', 'books','the future', 'the past', 'dogs', 'science', 'history', 'the ocean']
    print("Welcome to the Faster Challenge. For this week's faster challenge you will need to:", choice(fast_craft_options), "something inspired by", choice(fast_craft_topics),".")
    print("Let's....make it!")
    making_it_fast_sat = int(input("How satisfied are you with your craft? (0-10)"))
    making_it_fast_fun = input("Did you have some good fun doing it? (Y/N)").strip('!?.').lower()
    if making_it_fast_sat > 5 and making_it_fast_fun == "yes":
        print("Good work then! Come on up and get your patch!")
    else:
        print("Well practice makes perfect. Better luck next time!")
def making_it_craft():
    making_it_craft_options = ["Build a family heirloom", "Make a collection of childen's toys and books", "Create a new outdoor game", "Turn Sammy's poop table into something beautiful", "Design a backdrop for a party", "Paint a mural", "Design a mailbox", "Curate the ultimate playlist", "Build a lawn display"]
    print("Welcome to the Master Challenge. For this week's faster challenge you will:", choice(making_it_craft_options))
    print("Let's...MAKE IT!!!")
    input("How's it look?")
    print()
    print("Instead of judgement, enjoy this quote about how silly the judgement in this show is:")
    print()
    print("Together, though, Simon and Dayna are just picky in all the wrong ways. They get disappointed when the artists don’t do things that no one told the artists to do. Sometimes the judges want perfection; other times they savor messiness. There are no clear standards to work from. What are the criteria? How do you even compare these various kinds of crafts when they use entirely different materials? Why are there even judges, except to stick to a typical reality TV competition elimination format? I’m not sure this show needs judging at all. Why critique what people create? writes the TV critic shitting all over two people’s work on summer’s most joyful reality show. --https://www.realityblurred.com/realitytv/2018/09/making-it-judge-problem/")
    print()
def making_it():
    print("Welcome to another year of... \n \n \n **** MAKING IT **** \n \n \n I'm Nick Offerman: actor, husband, host, and woodworker.  \n And I'm Amy Poehler: two of those things.")
    print()
    print("Here are your options for Making It: \n 1. Faster Craft \n 2. Master Craft \n 3. Whole Episode!")
    mioptions = False
    while mioptions == False:
        making_it_choice = input("How would you like to proceed?").strip(".)(:)")
        if making_it_choice == '1':
            print("Faster Crafter:")
            making_it_fast()
            mioptions = True
        elif making_it_choice == '2':
            print("Master Crafter:")
            making_it_craft()
            mioptions = True
        elif making_it_choice == '3':
            making_it_fast()
            making_it_craft()
            print("Congratulations! You are the master maker!")
            mioptions = True
        else:
            print("Please pick 1 2 or 3 ?")
def bake_off():
    print("baking")
    gbb_chooser = 0
    while gbb_chooser == 0:
        gbb_choice = input("Would you like a signature bake, technical bake, or showstopper bake?").lower().strip("!?.,()")
        if gbb_choice == "signature bake":
            print("Ready, Set, Bake!")
            print()
            signatures = ["https://thegreatbritishbakeoff.co.uk/recipes/all/terry-penguin-snowmen-cake-pops/", "https://thegreatbritishbakeoff.co.uk/recipes/all/steph-black-forest-chocolate-cake/", "https://thegreatbritishbakeoff.co.uk/recipes/all/steph-zest-spice-hot-cross-buns/", "https://thegreatbritishbakeoff.co.uk/recipes/all/rosie-salted-caramel-chocolate-raspberry-stack/", "https://thegreatbritishbakeoff.co.uk/recipes/all/michael-mango-lime-ginger-tarts/", "https://thegreatbritishbakeoff.co.uk/recipes/all/steph-raspberry-chocolate-fudge-cake/", "https://thegreatbritishbakeoff.co.uk/recipes/all/david-cinnamon-swirls/", "https://thegreatbritishbakeoff.co.uk/recipes/all/phil-pancetta-gruyere-padano-focaccia/", "https://thegreatbritishbakeoff.co.uk/recipes/all/priya-smoky-jalapeno-bread/", "https://thegreatbritishbakeoff.co.uk/recipes/all/briony-espresso-martini-madeleines/", "https://thegreatbritishbakeoff.co.uk/recipes/all/kate-espresso-martini-cannoli/"]
            print(choice(signatures))
            gbb_chooser = 1
        elif gbb_choice == "technical bake":
            print("Ready, Set, Bake!")
            print()
            technicals = ["https://thegreatbritishbakeoff.co.uk/recipes/all/paul-hollywood-raspberry-millefeuille/", "https://thegreatbritishbakeoff.co.uk/recipes/all/liam-charles-salted-caramel-chocolate-tart/", "https://thegreatbritishbakeoff.co.uk/recipes/all/prue-leith-apple-and-cinnamon-buns/", "https://thegreatbritishbakeoff.co.uk/recipes/all/paul-hollywood-chocolate-ricotta-cassatelle/", "https://thegreatbritishbakeoff.co.uk/recipes/all/prue-leith-choux-swans/", "https:// thegreatbritishbakeoff.co.uk/recipes/all/chocolate-crumpets-with-black-cherry-jam/", "https://thegreatbritishbakeoff.co.uk/recipes/all/paul-hollywood-cream-horns/", "https://thegreatbritishbakeoff.co.uk/recipes/all/prue-leith-snow-eggs/", "https://thegreatbritishbakeoff.co.uk/recipes/all/paul-hollywood-campfire-pitta-breads/", "https://thegreatbritishbakeoff.co.uk/recipes/all/prue-leith-torta-setteveli/", "https://thegreatbritishbakeoff.co.uk/recipes/all/paul-hollywood-molten-puddings/", "https://thegreatbritishbakeoff.co.uk/recipes/all/prue-leith-pizza-margherita/", "https://thegreatbritishbakeoff.co.uk/recipes/all/prue-leith-stroopwafels/"]
            print(choice(technicals))
            gbb_chooser = 1
        elif gbb_choice == "showstopper bake":
            print("Ready, Set, Bake!")
            print()
            showstoppers = ["https://thegreatbritishbakeoff.co.uk/recipes/all/david-cheese-board-cake/", "https://thegreatbritishbakeoff.co.uk/recipes/all/alice-save-our-oceans-lemon-honey-white-chocolate-raspberry-cake/", "https://thegreatbritishbakeoff.co.uk/recipes/all/henry-a-white-russian/", "https://thegreatbritishbakeoff.co.uk/recipes/all/alice-coffee-walnut-ragsulla/", "https://thegreatbritishbakeoff.co.uk/recipes/all/alice-chocolate-coconut-new-zealand-lamb/", "https://thegreatbritishbakeoff.co.uk/recipes/all/rahul-edible-rock-garden-chocolate-cake/", "https://thegreatbritishbakeoff.co.uk/recipes/all/briony-hazelnut-mocha-cake/", "https://thegreatbritishbakeoff.co.uk/recipes/all/karen-chateau-du-chambord-framboise/", "https://thegreatbritishbakeoff.co.uk/recipes/all/rav-frozen-fantasy-cake/", "https://thegreatbritishbakeoff.co.uk/recipes/all/sophie-ode-to-the-honey-bee-entremet/", "https://thegreatbritishbakeoff.co.uk/recipes/all/sophie-snakes-ladders-biscuit-board-game/"]
            print(choice(showstoppers))
            gbb_chooser = 1
def workout():
    print("Welcome to your workout builder!")

    """Input Questions"""

    lengthw = input("Would you like today's workout to be short, medium, or long?").lower().strip(",.!?")
    while (lengthw != "short" and lengthw != "medium" and lengthw != "long"):
            lengthw = input("Didn't get that. Would you like today's workout to be short, medium, or long?").lower().strip(",.!?")
    challengew = input("Would you like today's workout to be easy, moderate, or hard?").lower().strip(",.!?")
    while (challengew != "easy" and challengew != "moderate" and challengew != "hard"):
        challengew = input("Sorry, one more time. Easy, moderate or hard?")
    focusw = input("Any areas you'd like to focus on? Options are core, arms, legs, cardio, none!").lower().strip(",.!?").split()
    avoidw = input("Any areas you'd like to avoid? Options are core, arms, legs, cardio, none!").lower().strip(",.!?").split()

    """Data to Pull From"""

    short = ["20 Min AMRAP", "30,15,5", "Tabata", "One and Done", "Yoga", "Bike"]
    medium = ["30 Min AMRAP", "40,20,10", "One and Done", "Rounds for Time"]
    long = ["40 Min AMRAP", "50, 25, 15", "One and Done", "The Killer", "Pyramid"]

    easycore = ["sit ups", "crunches", "3 seconds of side plank", "flutter kicks", "oblique crunches"]
    easyarms = ["bicep curls", "dips", "overhead press", "lawn mower", "arm circles"]
    easylegs = ["squats", "5 seconds of wall sit", "lunges", "side lunge", "calf raises"]
    easycardio = ["march in place", "shuffles", "4 square hops", "jog in the yard", "jumping jacks"]
    moderatecore = ["lying leg raises", "crunchy frogs", "5 seconds of plank", "5 seconds of six inches", "crunch twists"]
    moderatearms = ["plank to push up", "push ups", "lateral raise", "upright row", "bench press"]
    moderatelegs = ["box jumps", "squat jumps", "jump rope", "lunge hold", "kettlebell swing"]
    moderatecardio = ["mat jumps", "stair squats", "bike sprint", "yard sprint", "1 min kickboxing"]
    hardcore =  ["russian twists", "CK sprinter sit ups", "clean and press with dumbbells", "lower body russian twists", "V sit"]
    hardarms = ["(wo)man maker", "pull ups", "hand stand pushups", "shooting the arrow", "overhead press"]
    hardlegs = ["wall ball", "weighted wall sit", "pistol squat", "weighted squats", "chair pose hold"]
    hardcardio = ["burpees", "lap around the block", "double unders", "mountain climbers", "toe touches"]

    """making sense of the input"""

    print("your workout type for today will be:")
    if lengthw == "short":
        typewchosen = choice(short)
    elif lengthw == "medium":
        typewchosen = choice(medium)
    elif lengthw == "long":
        typewchosen = choice(long)
    print(typewchosen)

    easy = [easycore, easyarms, easylegs, easycardio]
    moderate = [moderatecore, moderatearms, moderatelegs, moderatecardio]
    hard = [hardcore, hardarms, hardlegs, hardcardio]

    if challengew == "easy":
        for i in focusw:
            if i == "core":
                easy.append(easycore)
            elif i == "arms":
                easy.append(easyarms)
            elif i == "legs":
                easy.append(easylegs)
            elif i == "cardio":
                easy.append(easycardio)
        for i in avoidw:
            if i == "core":
                easy.pop(easy.index(easycore))
            elif i == "arms":
                easy.pop(easy.index(easyarms))
            elif i == "legs":
                easy.pop(easy.index(easylegs))
            elif i == "cardio":
                easy.pop(easy.index(easycardio))
    if challengew == "moderate":
        for i in focusw:
            if i == "core":
                moderate.append(moderatecore)
            elif i == "arms":
                moderate.append(moderatearms)
            elif i == "legs":
                moderate.append(moderatelegs)
            elif i == "cardio":
                moderate.append(moderatecardio)
        for i in avoidw:
            if i == "core":
                moderate.pop(moderate.index(moderatecore))
            elif i == "arms":
                moderate.pop(moderate.index(moderatearms))
            elif i == "legs":
                moderate.pop(moderate.index(moderatelegs))
            elif i == "cardio":
                moderate.pop(moderate.index(moderatecardio))
    if challengew == "hard":
        for i in focusw:
            if i == "core":
                hard.append(hardcore)
            elif i == "arms":
                hard.append(hardarms)
            elif i == "legs":
                hard.append(hardlegs)
            elif i == "cardio":
                hard.append(hardcardio)
        for i in avoidw:
            if i == "core":
                hard.pop(hard.index(hardcore))
            elif i == "arms":
                hard.pop(hard.index(hardarms))
            elif i == "legs":
                hard.pop(hard.index(hardlegs))
            elif i == "cardio":
                hard.pop(hard.index(hardcardio))

    numbersw = [0,1,2,3,4]

    """types of workouts and their constraints"""

    if typewchosen == "20 Min AMRAP" or typewchosen == "30 Min AMRAP" or typewchosen == "40 Min AMRAP":
        if challengew == "easy":
            for z in range(8):
                print(choice(easy)[choice(numbersw)])
        elif challengew == "moderate":
            for z in range(12):
                print(choice(moderate)[choice(numbersw)])
        elif challengew == "hard":
            for z in range(15):
                print(choice(hard)[choice(numbersw)])
    if typewchosen == "30,15,5" or typewchosen == "40,20,10" or typewchosen == "50, 25, 15":
        if challengew == "easy":
            for z in range(3):
                print(choice(easy)[choice(numbersw)])
        elif challengew == "moderate":
            for z in range(3):
                print(choice(moderate)[choice(numbersw)])
        elif challengew == "hard":
            for z in range(3):
                print(choice(hard)[choice(numbersw)])
    if typewchosen == "One and Done":
        if challengew == "easy" and lengthw == "short":
            for z in range(10):
                print(choice(easy)[choice(numbersw)])
        elif challengew == "moderate" and lengthw == "short":
            for z in range(10):
                print(choice(moderate)[choice(numbersw)])
        elif challengew == "hard" and lengthw == "short":
            for z in range(10):
                print(choice(hard)[choice(numbersw)])
        elif challengew == "easy" and lengthw == "medium":
            for z in range(16):
                print(choice(easy)[choice(numbersw)])
        elif challengew == "moderate" and lengthw == "medium":
            for z in range(16):
                print(choice(moderate)[choice(numbersw)])
        elif challengew == "hard" and lengthw == "medium":
            for z in range(16):
                print(choice(hard)[choice(numbersw)])
        elif challengew == "easy" and lengthw == "long":
            for z in range(24):
                print(choice(easy)[choice(numbersw)])
        elif challengew == "moderate" and lengthw == "long":
            for z in range(24):
                print(choice(moderate)[choice(numbersw)])
        elif challengew == "hard" and lengthw == "long":
            for z in range(24):
                print(choice(hard)[choice(numbersw)])

    if typewchosen == "Bike":
        minutes = [15,20,25]
        sprints = [4,6,8]
        print("Go ahead and bike for", choice(minutes), "minutes with", choice(sprints), "30 second sprints worked in.")
    if typewchosen == "Yoga":
        print("Do a nice calming yoga routine! 20-40 minutes should do it.")

    if typewchosen == "Rounds for Time" and challengew == "easy":
        roundoptions = [3,4,5,6]
        amountoptions = [10,15,20,25]
        rounds = choice(roundoptions)
        print(rounds, "rounds of:")
        for x in range(4):
            print(choice(amountoptions), choice(easy)[choice(numbersw)])
    if typewchosen == "Rounds for Time" and challengew == "moderate":
        roundoptions = [3,4,5,6]
        amountoptions = [10,15,20,25]
        rounds = choice(roundoptions)
        print(rounds, "rounds of:")
        for x in range(4):
            print(choice(amountoptions), choice(moderate)[choice(numbersw)])
    if typewchosen == "Rounds for Time" and challengew == "hard":
        roundoptions = [3,4,5,6]
        amountoptions = [10,15,20,25]
        rounds = choice(roundoptions)
        print(rounds, "rounds of:")
        for x in range(4):
            print(choice(amountoptions), choice(hard)[choice(numbersw)])

    if typewchosen == "The Killer" and challengew == "easy":
        killerlist = []
        print("You know how this one works. 3 exercises rotate on the minute for 15 minutes. 4 Rounds")
        print("Set one:")
        for q in range(3):
            list_chosen = choice(easy)
            killer_chosen = (list_chosen[choice(numbersw)])
            print(q+1,":",killer_chosen)
            killerlist.append(killer_chosen)
#            list_chosen.pop(list_chosen.index(killer_chosen))
#            numbersw.pop(-1)
        print("Set two:")
        for q in range(3):
            list_chosen = choice(easy)
            killer_chosen = (list_chosen[choice(numbersw)])
            print(q+4, ":", killer_chosen)
            killerlist.append(killer_chosen)
#            list_chosen.pop(list_chosen.index(killer_chosen))
#            numbersw.pop(-1)
        print("Set three:")
        for q in range(3):
            list_chosen = choice(easy)
            killer_chosen = (list_chosen[choice(numbersw)])
            print(q+7,":",killer_chosen)
            killerlist.append(killer_chosen)
#            list_chosen.pop(list_chosen.index(killer_chosen))
#            numbersw.pop(-1)
        print("Set four:")
        for q in range(3):
            list_chosen = choice(easy)
            killer_chosen = (list_chosen[choice(numbersw)])
            print(q+10,":",killer_chosen)
            killerlist.append(killer_chosen)
#            list_chosen.pop(list_chosen.index(killer_chosen))
#            numbersw.pop(-1)
        suboutkiller = 0
        while suboutkiller == 0:
            replacementkiller = input("Need to replace anything? Enter the number!").lower().strip(" .,!?@()")
            replacementoptionspos = [1,2,3,4,5,6,7,8,9,10,11,12]
            replacementoptionsneg = ["no", "nope", "n", "none"]
            if replacementkiller in str(replacementoptionspos):
                killerlist.pop(int(replacementkiller)-1)
                killerlist.insert(int(replacementkiller)-1, choice(easy)[choice(numbersw)])
                for p in range(12):
                    if p == 0:
                        print("Set one:")
                    elif p == 3:
                        print("Set two:")
                    elif p == 6:
                        print("Set three:")
                    elif p == 9:
                        print("Set four:")
                    print(p+1, ":", killerlist[p])
            elif replacementkiller in replacementoptionsneg:
                print("Okay, get started!")
                suboutkiller = 1
    if typewchosen == "The Killer" and challengew == "moderate":
        killerlist = []
        print("You know how this one works. 3 exercises rotate on the minute for 15 minutes. 4 Rounds")
        print("Set one:")
        for q in range(3):
            list_chosen = choice(moderate)
            killer_chosen = (list_chosen[choice(numbersw)])
            print(q+1,":",killer_chosen)
            killerlist.append(killer_chosen)
    #            list_chosen.pop(list_chosen.index(killer_chosen))
    #            numbersw.pop(-1)
        print("Set two:")
        for q in range(3):
            list_chosen = choice(moderate)
            killer_chosen = (list_chosen[choice(numbersw)])
            print(q+4, ":", killer_chosen)
            killerlist.append(killer_chosen)
    #            list_chosen.pop(list_chosen.index(killer_chosen))
    #            numbersw.pop(-1)
        print("Set three:")
        for q in range(3):
            list_chosen = choice(moderate)
            killer_chosen = (list_chosen[choice(numbersw)])
            print(q+7,":",killer_chosen)
            killerlist.append(killer_chosen)
    #            list_chosen.pop(list_chosen.index(killer_chosen))
    #            numbersw.pop(-1)
        print("Set four:")
        for q in range(3):
            list_chosen = choice(moderate)
            killer_chosen = (list_chosen[choice(numbersw)])
            print(q+10,":",killer_chosen)
            killerlist.append(killer_chosen)
    #            list_chosen.pop(list_chosen.index(killer_chosen))
    #            numbersw.pop(-1)
        suboutkiller = 0
        while suboutkiller == 0:
            replacementkiller = input("Need to replace anything? Enter the number!").lower().strip(" .,!?@()")
            replacementoptionspos = [1,2,3,4,5,6,7,8,9,10,11,12]
            replacementoptionsneg = ["no", "nope", "n", "none"]
            if replacementkiller in str(replacementoptionspos):
                killerlist.pop(int(replacementkiller)-1)
                killerlist.insert(int(replacementkiller)-1, choice(moderate)[choice(numbersw)])
                for p in range(12):
                    if p == 0:
                        print("Set one:")
                    elif p == 3:
                        print("Set two:")
                    elif p == 6:
                        print("Set three:")
                    elif p == 9:
                        print("Set four:")
                    print(p+1, ":", killerlist[p])
            elif replacementkiller in replacementoptionsneg:
                print("Okay, get started!")
                suboutkiller = 1
    if typewchosen == "The Killer" and challengew == "hard":
        killerlist = []
        print("You know how this one works. 3 exercises rotate on the minute for 15 minutes. 4 Rounds")
        print("Set one:")
        for q in range(3):
            list_chosen = choice(hard)
            killer_chosen = (list_chosen[choice(numbersw)])
            print(q+1,":",killer_chosen)
            killerlist.append(killer_chosen)
    #            list_chosen.pop(list_chosen.index(killer_chosen))
    #            numbersw.pop(-1)
        print("Set two:")
        for q in range(3):
            list_chosen = choice(hard)
            killer_chosen = (list_chosen[choice(numbersw)])
            print(q+4, ":", killer_chosen)
            killerlist.append(killer_chosen)
    #            list_chosen.pop(list_chosen.index(killer_chosen))
    #            numbersw.pop(-1)
        print("Set three:")
        for q in range(3):
            list_chosen = choice(hard)
            killer_chosen = (list_chosen[choice(numbersw)])
            print(q+7,":",killer_chosen)
            killerlist.append(killer_chosen)
    #            list_chosen.pop(list_chosen.index(killer_chosen))
    #            numbersw.pop(-1)
        print("Set four:")
        for q in range(3):
            list_chosen = choice(hard)
            killer_chosen = (list_chosen[choice(numbersw)])
            print(q+10,":",killer_chosen)
            killerlist.append(killer_chosen)
    #            list_chosen.pop(list_chosen.index(killer_chosen))
    #            numbersw.pop(-1)
        suboutkiller = 0
        while suboutkiller == 0:
            replacementkiller = input("Need to replace anything? Enter the number!").lower().strip(" .,!?@()")
            replacementoptionspos = [1,2,3,4,5,6,7,8,9,10,11,12]
            replacementoptionsneg = ["no", "nope", "n", "none"]
            if replacementkiller in str(replacementoptionspos):
                killerlist.pop(int(replacementkiller)-1)
                killerlist.insert(int(replacementkiller)-1, choice(hard)[choice(numbersw)])
                for p in range(12):
                    if p == 0:
                        print("Set one:")
                    elif p == 3:
                        print("Set two:")
                    elif p == 6:
                        print("Set three:")
                    elif p == 9:
                        print("Set four:")
                    print(p+1, ":", killerlist[p])
            elif replacementkiller in replacementoptionsneg:
                print("Okay, get started!")
                suboutkiller = 1

    if typewchosen == "Pyramid" and challengew == "hard":
        pyramidlist = []
        print("Let's GO!")
        for q in range(12):
            list_chosen = choice(hard)
            pyramid_chosen = (list_chosen[choice(numbersw)])
            print(q+1,":",pyramid_chosen)
            pyramidlist.append(pyramid_chosen)
        suboutpyra = 0
        while suboutpyra == 0:
            replacementpyra = input("Need to replace anything? Enter the number!").lower().strip(" .,!?@()")
            replacementoptionspos = [1,2,3,4,5,6,7,8,9,10,11,12]
            replacementoptionsneg = ["no", "nope", "n", "none"]
            if replacementpyra in str(replacementoptionspos):
                pyramidlist.pop(int(replacementpyra)-1)
                pyramidlist.insert(int(replacementpyra)-1, choice(hard)[choice(numbersw)])
                for p in range(12):
                    print(p+1, ":", pyramidlist[p])
            elif replacementpyra in replacementoptionsneg:
                print("Okay, get started!")
                suboutpyra = 1
    if typewchosen == "Pyramid" and challengew == "moderate":
        pyramidlist = []
        print("Let's GO!")
        for q in range(12):
            list_chosen = choice(moderate)
            pyramid_chosen = (list_chosen[choice(numbersw)])
            print(q+1,":",pyramid_chosen)
            pyramidlist.append(pyramid_chosen)
        suboutpyra = 0
        while suboutpyra == 0:
            replacementpyra = input("Need to replace anything? Enter the number!").lower().strip(" .,!?@()")
            replacementoptionspos = [1,2,3,4,5,6,7,8,9,10,11,12]
            replacementoptionsneg = ["no", "nope", "n", "none"]
            if replacementpyra in str(replacementoptionspos):
                pyramidlist.pop(int(replacementpyra)-1)
                pyramidlist.insert(int(replacementpyra)-1, choice(moderate)[choice(numbersw)])
                for p in range(12):
                    print(p+1, ":", pyramidlist[p])
            elif replacementpyra in replacementoptionsneg:
                print("Okay, get started!")
                suboutpyra = 1
    if typewchosen == "Pyramid" and challengew == "easy":
        pyramidlist = []
        print("Let's GO!")
        for q in range(12):
            list_chosen = choice(easy)
            pyramid_chosen = (list_chosen[choice(numbersw)])
            print(q+1,":",pyramid_chosen)
            pyramidlist.append(pyramid_chosen)
        suboutpyra = 0
        while suboutpyra == 0:
            replacementpyra = input("Need to replace anything? Enter the number!").lower().strip(" .,!?@()")
            replacementoptionspos = [1,2,3,4,5,6,7,8,9,10,11,12]
            replacementoptionsneg = ["no", "nope", "n", "none"]
            if replacementpyra in str(replacementoptionspos):
                pyramidlist.pop(int(replacementpyra)-1)
                pyramidlist.insert(int(replacementpyra)-1, choice(easy)[choice(numbersw)])
                for p in range(12):
                    print(p+1, ":", pyramidlist[p])
            elif replacementpyra in replacementoptionsneg:
                print("Okay, get started!")
                suboutpyra = 1
def cocktails():
    print()
    print("Hey there! Answer a couple questions for me, and let's have a drink.")
    print('='*30)
    alcohols = ['vodka', 'gin', 'rum', 'whiskey', 'bourbon', 'tequila', 'triple sec', 'red wine', 'white wine', 'sweet vermouth', 'campari']
    mixers = ['soda water', 'lemon', 'lime', 'orange', 'berries', 'ginger beer', 'cranberry juice', 'bitters', 'sugar']

    answersc = []
    answersm = []
    for i in alcohols:
        print("Do you have", i, "?")
        answerc = input()
        answersc.append(answerc)
    for i in mixers:
        print("Do you have", i, "?")
        answerm = input()
        answersm.append(answerm)

    margarita = ['lime', 'tequila', 'triple sec']
    berrymargarita = ['lime', 'tequila', 'triple sec', 'berries']
    cosmo = ['vodka', 'cranberry juice', 'triple sec', 'lime']
    negroni = ['gin', 'sweet vermouth', 'campari']
    ginandtonic = ['gin', 'soda water', 'lime']
    manhattan = ['bourbon', 'sweet vermouth', 'bitters']
    daiquiri = ['rum', 'lime', 'sugar']

    cocktailoptions = margarita, berrymargarita, cosmo, negroni, ginandtonic, manhattan, daiquiri

    positive = ['yes', 'y', 'ya', 'yeah', 'si']

    for x in answersc:
        if x in positive:
            indexofx = answersc.index(x)
            answersc.pop(indexofx)
            answersc.insert(indexofx, alcohols[indexofx])
#        print(answersc)
    for x in answersm:
        if x in positive:
            indexofx = answersm.index(x)
            answersm.pop(indexofx)
            answersm.insert(indexofx, mixers[indexofx])
#        print(answersm)

    totalanswers = answersc + answersm
#    print(totalanswers)

    counting = 0
    answerstooptions = []
    for z in cocktailoptions:
#        print("this is z", z)
        for e in z:
#            print("this is e", e)
            if e in totalanswers:
                counting += 1
#                print("found", counting)
            if counting == len(z):
                answerstooptions.append(z)
        counting = 0
#    print(answerstooptions)

    finallistofcocktails = []
    for q in answerstooptions:
        if q == margarita:
            margaritafinal = ['margaritas!', margarita, '1:2:1']
            finallistofcocktails.append(margaritafinal)
        elif q == berrymargarita:
            berrymargaritafinal = ['berry margaritas!', berrymargarita, '1:2:1:1']
            finallistofcocktails.append(finallistofcocktails)
        elif q == cosmo:
            cosmofinal = ['cosmos!', cosmo, '4:2:2:1']
            finallistofcocktails.append(cosmofinal)
        elif q == negroni:
            negronifinal = ['negroni!', negroni, '1:1:1']
            finallistofcocktails.append(negronifinal)
        elif q == ginandtonic:
            ginandtonicfinal = ['gin & tonics!', ginandtonic, '1:1:1']
            finallistofcocktails.append(ginandtonicfinal)
        elif q == manhattan:
            manhattanfinal = ['manhattans!', manhattan, '2:1:dash']
            finallistofcocktails.append(manhattanfinal)
        elif q == daiquiri:
            daiquirifinal = ['daiquiris!', daiquiri, '2:1:1']
            finallistofcocktails.append(daiquirifinal)
    print()
    satisfied = 'no'
    while satisfied == 'no':
        chosenc = choice(finallistofcocktails)
        print("Great! We are having", chosenc[0], "Here's what you need:")
        usindcc3 = chosenc[2].strip(':')
        x=0
        for i in range(len(chosenc[1])):
            print(usindcc3[x], 'oz.', chosenc[1][i])
            x=x+2
        print()
        asksat = input("Everything look good?")
        asksatpos = ['all set', 'good', 'yes', 'y', 'oui', 'yep']
        if asksat in asksatpos:
            print('Great! Enjoy!')
            satisfied = 'yes'
        else:
            asksattwo = input("Oh no! Should we try again?")
            if asksattwo in asksatpos:
                satisfied = 'no'
            else:
                satisfied = 'yes'



def main():
    game_input = False
    while game_input == False:
        print("What would you like to do?")
        game_options = ['chopped', 'making it', 'great british bake off', 'workout', 'cocktails']
        print(game_options)
        game_choice = input().strip('!?.').lower()
        if game_choice == 'chopped':
            chopped()
            game_input = True
        elif game_choice == 'making it':
            making_it()
            game_input = True
        elif game_choice == 'great british bake off':
            bake_off()
            game_input = True
        elif game_choice == 'workout':
            workout()
            game_input = True
        elif game_choice == 'cocktails':
            cocktails()
            game_input = True
        else:
            print("I don't recognize that game...")
main()
