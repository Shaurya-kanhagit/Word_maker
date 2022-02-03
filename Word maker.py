import random
print("Hello this word adventure game is designed by shaurya hope you will like it 0_0")
a = 0
p = 0
aa = input("Entre your name -->")
print("welcome", aa)


while a <= 10:
    a = a+1
    
    dit = ["a", "abandon", "abandoned", "ability", "able", "about", "above", "abroad", "absence", "absent", "absolute",
           "absorb", "abuse", "academic", "accent", "accept", "acceptable", "access", "accident", "accidental",
           "accompany", "according", "to", "account", "accurate", "accuse", "achieve", "achievement", "acid",
           "acknowledge", "acquire", "across", "act", "action", "active", "activist", "activity", "actor", "actress",
           "actual", "actually", "ad", "adapt", "add", "addition", "additional", "address", "add", "up", "adequate",
           "adjust", "administration", "admiration", "admire", "admit", "adopt", "adult", "advance", "advanced",
           "advantage", "adventure", "advertise", "advertisement", "advertising", "advice", "advise", "affair",
           "affect", "affection", "afford", "afraid", "after", "afternoon", "afterward", "again", "against", "age",
           "aged", "agency", "agenda", "agent", "aggressive", "ago", "agree", "agreement", "ahead", "aid", "aim", "air",
           "aircraft", "airport", "alarm", "alarmed", "alarming", "alcohol", "alcoholic", "alive", "all", "allied",
           "allow", "of", "ally", "almost", "alone", "along", "alongside", "aloud", "alphabet", "alphabetical",
           "already", "also", "alter", "alternative", "alternatively", "although", "altogether", "always", "a.m.",
           "amaze", "amazed", "amazing", "ambition", "ambulance", "among", "amount", "amuse", "amused", "amusing",
           "an", "analysis", "analyze", "ancient", "and", "anger", "angle", "angry", "animal", "ankle", "anniversary",
           "announce", "announcement", "annoy", "annoyed", "annoying", "annual", "annually", "another", "answer",
           "anti-", "anticipate", "anxiety", "anxious", "any", "anymore", "anyone", "anything", "anyway", "anywhere",
           "apart", "apart", "from", "apartment", "apologize", "apparently", "appeal", "appear", "appearance", "apple",
           "application", "apply", "appoint", "appointment", "appreciate", "approach", "appropriate", "approval",
           "approve", "approving", "approximate", "approximately", "April", "area", "argue", "argument", "arise", "arm",
           "armed", "arms", "army", "around", "arrange", "arrangement", "arrest", "arrival", "arrive", "arrow", "art",
           "article", "artificial", "artist", "artistic", "as", "ashamed", "aside", "aside from", "ask", "asleep",
           "aspect", "assist", "assistance", "assistant", "associate", "association", "assume", "assure", "at",
           "atmosphere", "atom", "attach", "attached", "attack", "attempt", "attempted", "attend", "attention",
           "attitude", "attorney", "attract", "attraction", "attractive", "audience", "August", "aunt", "author",
           "authority", "automatic", "available", "average", "avoid", "awake", "award", "aware", "away", "awful",
           "awkward", "baby", "back", "background", "backward", "bacteria", "bad", "badly", "bag", "baggage", "bake",
           "balance", "ball", "ban", "band", "bandage", "bank", "bar", "barely", "bargain", "barrier", "base",
           "baseball", "basic", "basically", "basis", "basketball", "bath", "bathroom", "battery", "battle", "bay",
           "be", "beach", "beak", "bear", "beard", "beat", "beautiful", "beautifully", "beauty", "because", "become",
           "bed", "bedroom", "beef", "beer", "before", "begin", "beginning", "behalf", "behave", "behavior", "behind",
           "belief", "believe", "bell", "belong", "below", "l", "label", "labor", "laboratory", "lack", "lacking",
           "lady", "lake", "lamp", "land", "landscape", "lane", "language", "large", "largely", "last", "1", "late",
           "lately", "later", "latest", "latter", "laugh", "launch", "laundry", "law", "lawyer", "lay", "layer", "lazy",
           "lead", "1", "leader", "leading", "1", "leaf", "league", "lean", "learn", "least", "leather", "leave",
           "lecture", "left", "leg", "legal", "lemon", "lend", "length", "less", "lessen", "let", "letter", "level",
           "liberal", "library", "license", "lid", "lie", "1", "life", "lift", "light", "lightly", "like", "likely",
           "limit", "limited", "line", "link", "lip", "liquid", "list", "listen", "liter", "literature", "little",
           "live", "1", "live", "2", "lively", "living", "load", "loan", "local", "locate", "location", "lock", "lock",
           "up", "logic", "logical", "lonely", "long", "look", "loose", "loosely", "lord", "lose", "loss", "lost",
           "lot", "loud", "love", "lover", "low"]
    dic = ['bear']
    a1 = random.choice(dic)
    len(a1)
    a2 = list(a1)
    if len(a1) == 2:
        a3 = random.choice(a2)
        a4 = random.choice(a2)
        if a3 == a4:
            a3 = random.choice(a2)
        elif a4 == a3:
            a4 = random.choice(a2)
        else:
            pass

        print("You have to find an the word from -_->", a3, a4)
        print("Thinking-Thinking")
        a15 = input("Entre the 1st Word here-->")
        a16 = input("Entre the 2nd Word here-->")
        b1 = a15 + a16
        print(b1)
        if b1 == a1:
            print("Great you have successfully formed that word congratulations", aa)
            p = p+1
            print('---------------------------------------------------------------------------------------------------')
        elif b1 != a1:
            print("Sorry you failed!!!", aa)
            print('you have formed O_O--? ', b1)
            print('You have to form this word O_O-> ', a1)
            print('--------------------------------------------------------------------------------------------------')
        else:
            print("Sorry you failed!!!")
            print('--------------------------------------------------------------------------------------------------')
    
    elif len(a1) == 3:
        a3 = random.choice(a2)
        a4 = random.choice(a2)
        a5 = random.choice(a2)
        if a3 == a4 or a3 == a5:
            a3 = random.choice(a2)
        elif a4 == a3 or a4 == a5:
            a3 = random.choice(a2)
        elif a5 == a3 or a5 == a4:
            a5 = random.choice(a2)
        else:
            pass
        print("You have to find and the word from -_->", a3, a4, a5)
        print("Thinking-Thinking")
        a15 = input("Entre the 1st Word here-->")
        a16 = input("Entre the 2nd Word here-->")
        a17 = input("Entre the 3rd Word here-->")
        b1 = a15 + a16 + a17 
        print(b1)
        if b1 == a1:
            print("Great you have formed that word congratulations", aa)
            p = p+1

            print('---------------------------------------------------------------------------------------------------')
        elif b1 != a1:
            print("Sorry you failed!!!", aa)
            print('you have formed O_O--? ', b1)
            print('You have to form this word O_O-> ', a1)
            print('---------------------------------------------------------------------------------------------------')
        else:
            print("Sorry you failed!!!")
            print('---------------------------------------------------------------------------------------------------')

    elif len(a1) == 4:
        a3 = random.choice(a2)
        a4 = random.choice(a2)
        a5 = random.choice(a2)
        a6 = random.choice(a2)
        if a3 == a4 or a3 == a5 or a3 == a6:
            a3 = random.choice(a2)
            continue
        elif a4 == a3 or a4 == a5 or a4 == a6:
            a4 = random.choice(a2)
            continue
        elif a5 == a4 or a5 == a3 or a5 == a6:
            a5 = random.choice(a2)
            continue
        elif a6 == a4 or a6 == a3 or a6 == a5:
            a6 = random.choice(a2)
            continue
        else:
            pass
        print("You have to find and the word from -_->", a3, a4, a5, a6)
        print("Thinking-Thinking")
        a15 = input("Entre the 1st Word here-->")
        a16 = input("Entre the 2nd Word here-->")
        a17 = input("Entre the 3rd Word here-->")
        a18 = input("Entre the 4rth Word here-->")
        b1 = a15 + a16 + a17 + a18 
        print(b1)
        if b1 == a1:
            print("Great you have formed that word congratulations", aa)
            p = p+1
        elif b1 != a1:
            print("Sorry you failed!!!", aa)
            print('you have formed O_O--? ', b1)
            print('You have to form this word O_O-> ', a1)
            print('---------------------------------------------------------------------------------------------------')
        else:
            print("Sorry you failed!!!")
            print('---------------------------------------------------------------------------------------------------')

    elif len(a1) == '5':
        a3 = random.choice(a2)
        a4 = random.choice(a2)
        a5 = random.choice(a2)
        a6 = random.choice(a2)
        a7 = random.choice(a2)
        if a3 == a4 or a3 == a5 or a3 == 6 or a3 == a7:
            a3 = random.choice(a2)
        elif a4 == a3 or a4 == a5 or a4 == a6 or a4 == a7:
            a4 = random.choice(a2)
        elif a5 == a4 or a5 == a3 or a5 == a6 or a5 == a7:
            a5 = random.choice(a2)
        elif a6 == a4 or a6 == a3 or a6 == a5 or a6 == a7:
            a6 = random.choice(a2)
        elif a7 == a3 or a7 == a4 or a7 == a5 or a7 == a6:
            a7 = random.choice(a2)
        else:
            pass

        print("You have to find and the word from -_->", a3, a4, a5, a6, a7)
        print("Thinking-Thinking")
        a15 = input("Entre the 1st Word here-->")
        a16 = input("Entre the 2nd Word here-->")
        a17 = input("Entre the 3rd Word here-->")
        a18 = input("Entre the 4rth Word here-->")
        a19 = input("Entre the 5th Word here-->")
        b1 = a15 + a16 + a17 + a18 + a19
        print(b1)
        if b1 == a1:
            print("Great you have formed that word congratulations", aa)
            p = p+1
            print('---------------------------------------------------------------------------------------------------')
        elif b1 != a1:
            print("Sorry you failed!!!", aa)
            print('you have formed O_O--? ', b1)
            print('You have to form this word O_O-> ', a1)
            print('---------------------------------------------------------------------------------------------------')
        else:
            print("Sorry you failed!!!")
            print('---------------------------------------------------------------------------------------------------')
    elif len(a1) == '6':
        a3 = random.choice(a2)
        a4 = random.choice(a2)
        a5 = random.choice(a2)
        a6 = random.choice(a2)
        a7 = random.choice(a2)
        a8 = random.choice(a2)
        if a3 == a4 or a3 == a5 or a3 == 6 or a3 == a7 or a3 == a8:
            a3 = random.choice(a2)
        elif a4 == a3 or a4 == a5 or a4 == a6 or a4 == a7 or a4 == a8:
            a4 = random.choice(a2)
        elif a5 == a4 or a5 == a3 or a5 == a6 or a5 == a7 or a5 == a8:
            a5 = random.choice(a2)
        elif a6 == a4 or a6 == a3 or a6 == a5 or a6 == a7 or a6 == a8:
            a6 = random.choice(a2)
        elif a7 == a3 or a7 == a4 or a7 == a5 or a7 == a6 or a7 == a8:
            a7 = random.choice(a2)
        elif a8 == a3 or a8 == a4 or a8 == a5 or a8 == a6 or a8 == a7:
            a8 = random.choice(a2)
        else:
            pass
        print("You have to find and the word from -_->", a3, a4, a5, a6, a7, a8)
        print("Thinking-Thinking")
        a15 = input("Entre the 1st Word here-->")
        a16 = input("Entre the 2nd Word here-->")
        a17 = input("Entre the 3rd Word here-->")
        a18 = input("Entre the 4rth Word here-->")
        a19 = input("Entre the 5th Word here-->")
        a20 = input("Entre the 6th Word here-->")
        b1 = a15 + a16 + a17 + a18 + a19 + a20 
        print(b1)
        if b1 == a1:
            print("Great you have formed that word congratulations", aa)
            p = p+1
            print('---------------------------------------------------------------------------------------------------')
        elif b1 != a1:
            print("Sorry you failed!!!", aa)
            print('you have formed O_O--? ', b1)
            print('You have to form this word O_O-> ', a1)
            print('---------------------------------------------------------------------------------------------------')
        else:
            print("Sorry you failed!!!")
            print('---------------------------------------------------------------------------------------------------')

    elif len(a1) == '7':
        a3 = random.choice(a2)
        a4 = random.choice(a2) 
        a5 = random.choice(a2)
        a6 = random.choice(a2)
        a7 = random.choice(a2)
        a8 = random.choice(a2)
        a9 = random.choice(a2)
        if a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a3 == a9:
            a3 = random.choice(a2)
        elif a4 == a3 or a4 == a5 or a4 == a6 or a4 == a7 or a4 == a8 or a4 == a9:
            a4 = random.choice(a2)
        elif a5 == a3 or a5 == a4 or a5 == a6 or a5 == a7 or a5 == a8 or a5 == a9:
            a5 = random.choice(a2)
        elif a6 == a3 or a6 == a4 or a6 == a5 or a6 == a7 or a6 == a8 or a6 == a9:
            a6 = random.choice(a2)
        elif a7 == a3 or a7 == a4 or a7 == a5 or a7 == a6 or a7 == a8 or a7 == a9:
            a7 = random.choice(a2)
        elif a8 == a3 or a8 == a4 or a8 == a5 or a8 == a6 or a8 == a7 or a8 == a9:
            a8 = random.choice(a2)
        elif a9 == a3 or a9 == a4 or a9 == a5 or a9 == a6 or a9 == a7 or a9 == a8:
            a9 = random.choice(a2)
        else:
            pass
        print("You have to find and the word from -_->", a3, a4, a5, a6, a7, a8, a9)
        print("Thinking-Thinking")
        a15 = input("Entre the 1st Word here-->")
        a16 = input("Entre the 2nd Word here-->")
        a17 = input("Entre the 3rd Word here-->")
        a18 = input("Entre the 4rth Word here-->")
        a19 = input("Entre the 5th Word here-->")
        a20 = input("Entre the 6th Word here-->")
        a21 = input("Entre the 7th Word here-->")
        b1 = a15 + a16 + a17 + a18 + a19 + a20 + a21 
        print(b1)
        if b1 == a1:
            print("Great you have formed that word congratulations", aa)
            print('---------------------------------------------------------------------------------------------------')
            p = p+1
        elif b1 != a1:
            print("Sorry you failed!!!", aa)
            print('you have formed O_O--? ', b1)
            print('You have to form this word O_O-> ', a1)
            print('---------------------------------------------------------------------------------------------------')
        else:
            print("Sorry you failed!!!")
            print('---------------------------------------------------------------------------------------------------')

    elif len(a1) == '8':
        a3 = random.choice(a2)
        a4 = random.choice(a2)
        a5 = random.choice(a2)
        a6 = random.choice(a2)
        a7 = random.choice(a2)
        a8 = random.choice(a2)
        a9 = random.choice(a2)
        a10 = random.choice(a2)
        if a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a3 == a9 or a3 == a10:
            a3 = random.choice(a2)
        elif a4 == a3 or a4 == a5 or a4 == a6 or a4 == a7 or a4 == a8 or a4 == a9 or a4 == a10:
            a4 = random.choice(a2)
        elif a5 == a3 or a5 == a4 or a5 == a6 or a5 == a7 or a5 == a8 or a5 == a9 or a5 == a10:
            a5 = random.choice(a2)
        elif a6 == a3 or a6 == a4 or a6 == a5 or a6 == a7 or a6 == a8 or a6 == a9 or a6 == a10:
            a6 = random.choice(a2)
        elif a7 == a3 or a7 == a4 or a7 == a5 or a7 == a6 or a7 == a8 or a7 == a9 or a7 == a10:
            a7 = random.choice(a2)
        elif a8 == a3 or a8 == a4 or a8 == a5 or a8 == a6 or a8 == a7 or a8 == a9 or a8 == a10:
            a8 = random.choice(a2)
        elif a9 == a3 or a9 == a4 or a9 == a5 or a9 == a6 or a9 == a7 or a9 == a8 or a9 == a10:
            a9 = random.choice(a2)
        elif a10 == a3 or a10 == a4 or a10 == a5 or a10 == a6 or a10 == a7 or a10 == a8 or a10 == a9:
            a10 = random.choice(a2)
        else:
            pass
        print("You have to find and the word from -_->", a3, a4, a5, a6, a7, a8, a9, a10)
        print("Thinking-Thinking")
        a15 = input("Entre the 1st Word here-->")
        a16 = input("Entre the 2nd Word here-->")
        a17 = input("Entre the 3rd Word here-->")
        a18 = input("Entre the 4rth Word here-->")
        a19 = input("Entre the 5th Word here-->")
        a20 = input("Entre the 6th Word here-->")
        a21 = input("Entre the 7th Word here-->")
        a22 = input("Entre the 8th Word here-->")
        b1 = a15 + a16 + a17 + a18 + a19 + a20 + a21 + a22
        print(b1)
        if b1 == a1:
            print("Great you have formed that word congratulations", aa)
            print('---------------------------------------------------------------------------------------------------')
            p = p+1
        elif b1 != a1:
            print("Sorry you failed!!!", aa)
            print('you have formed O_O--? ', b1)
            print('You have to form this word O_O-> ', a1)
            print('---------------------------------------------------------------------------------------------------')
        else:
            print("Sorry you failed!!!")
            print('---------------------------------------------------------------------------------------------------')

    elif len(a1) == '9':
        a3 = random.choice(a2)
        a4 = random.choice(a2)
        a5 = random.choice(a2)
        a6 = random.choice(a2)
        a7 = random.choice(a2)
        a8 = random.choice(a2)
        a9 = random.choice(a2)
        a10 = random.choice(a2)
        a11 = random.choice(a2)
        if a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a3 == a9 or a3 == a10 or a3 == a11:
            a3 = random.choice(a2)
        elif a4 == a3 or a4 == a5 or a4 == a6 or a4 == a7 or a4 == a8 or a4 == a9 or a4 == a10 or a4 == a11:
            a4 = random.choice(a2)
        elif a5 == a3 or a5 == a4 or a5 == a6 or a5 == a7 or a5 == a8 or a5 == a9 or a5 == a10 or a5 == a11:
            a5 = random.choice(a2)
        elif a6 == a3 or a6 == a4 or a6 == a5 or a6 == a7 or a6 == a8 or a6 == a9 or a6 == a10 or a6 == a11:
            a6 = random.choice(a2)
        elif a7 == a3 or a7 == a4 or a7 == a5 or a7 == a6 or a7 == a8 or a7 == a9 or a7 == a10 or a7 == a11:
            a7 = random.choice(a2)
        elif a8 == a3 or a8 == a4 or a8 == a5 or a8 == a6 or a8 == a7 or a8 == a9 or a8 == a10 or a8 == a11:
            a8 = random.choice(a2)
        elif a9 == a3 or a9 == a4 or a9 == a5 or a9 == a6 or a9 == a7 or a9 == a8 or a9 == a10 or a9 == a11:
            a9 = random.choice(a2)
        elif a10 == a3 or a10 == a4 or a10 == a5 or a10 == a6 or a10 == a7 or a10 == a8 or a10 == a9 or a10 == a11:
            a10 = random.choice(a2)
        elif a11 == a3 or a11 == a4 or a11 == a5 or a11 == a6 or a11 == a7 or a11 == a8 or a11 == a9 or a11 == a10:
            a11 = random.choice(a2)
        else:
            pass
        print("You have to find and the word from -_->", a3, a4, a5, a6, a7, a8, a9, a10, a11)
        print("Thinking-Thinking")
        a15 = input("Entre the 1st Word here-->")
        a16 = input("Entre the 2nd Word here-->")
        a17 = input("Entre the 3rd Word here-->")
        a18 = input("Entre the 4rth Word here-->")
        a19 = input("Entre the 5th Word here-->")
        a20 = input("Entre the 6th Word here-->")
        a21 = input("Entre the 7th Word here-->")
        a22 = input("Entre the 8th Word here-->")
        a23 = input("Entre the 9th Word here-->")
        b1 = a15 + a16 + a17 + a18 + a19 + a20 + a21 + a22 + a23 
        print(b1)
        if b1 == a1:
            print("Great you have formed that word congratulations", aa)
            print('---------------------------------------------------------------------------------------------------')
            p = p+1
        elif b1 != a1:
            print("Sorry you failed!!!", aa)
            print('you have formed O_O--? ', b1)
            print('You have to form this word O_O-> ', a1)
            print('---------------------------------------------------------------------------------------------------')
        else:
            print("Sorry you failed!!!")
            print('---------------------------------------------------------------------------------------------------')

    elif len(a1) == '10':
        a3 = random.choice(a2)
        a4 = random.choice(a2)
        a5 = random.choice(a2)
        a6 = random.choice(a2)
        a7 = random.choice(a2)
        a8 = random.choice(a2)
        a9 = random.choice(a2)
        a10 = random.choice(a2)
        a11 = random.choice(a2)
        a12 = random.choice(a2)
        if a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a3 == a9 or a3 == a10 or a3 == a11 or a3 == a12:
            a3 = random.choice(a2)
        elif a4 == a3 or a4 == a5 or a4 == a6 or a4 == a7 or a4 == a8 or a4 == a9 or a4 == a10 or a4 == a11 or\
                a4 == a12:
            a4 = random.choice(a2)
        elif a5 == a3 or a5 == a4 or a5 == a6 or a5 == a7 or a5 == a8 or a5 == a9 or a5 == a10 or a5 == a11 or\
                a5 == a12:
            a5 = random.choice(a2)
        elif a6 == a3 or a6 == a4 or a6 == a5 or a6 == a7 or a6 == a8 or a6 == a9 or a6 == a10 or a6 == a11 or\
                a6 == a12:
            a6 = random.choice(a2)
        elif a7 == a3 or a7 == a4 or a7 == a5 or a7 == a6 or a7 == a8 or a7 == a9 or a7 == a10 or a7 == a11 or\
                a7 == a12:
            a7 = random.choice(a2)
        elif a8 == a3 or a8 == a4 or a8 == a5 or a8 == a6 or a8 == a7 or a8 == a9 or a8 == a10 or a8 == a11 or\
                a8 == a12:
            a8 = random.choice(a2)
        elif a9 == a3 or a9 == a4 or a9 == a5 or a9 == a6 or a9 == a7 or a9 == a8 or a9 == a10 or a9 == a11 or\
                a9 == a12:
            a9 = random.choice(a2)
        elif a10 == a3 or a10 == a4 or a10 == a5 or a10 == a6 or a10 == a7 or a10 == a8 or a10 == a9 or a10 == a11 or\
                a10 == a12:
            a10 = random.choice(a2)
        elif a11 == a3 or a11 == a4 or a11 == a5 or a11 == a6 or a11 == a7 or a11 == a8 or a11 == a9 or a11 == a10 or\
                a11 == a12:
            a11 = random.choice(a2)
        elif a12 == a3 or a12 == a4 or a12 == a5 or a12 == a6 or a12 == a7 or a12 == a8 or a12 == a9 or a12 == a10 or\
                a12 == a11:
            a12 = random.choice(a2)
        else:
            pass
        print("You have to find and the word from -_->", a3, a4, a5, a6, a7, a8, a9, a10, a11, a12)
        print("Thinking-Thinking")
        a15 = input("Entre the 1st Word here-->")
        a16 = input("Entre the 2nd Word here-->")
        a17 = input("Entre the 3rd Word here-->")
        a18 = input("Entre the 4rth Word here-->")
        a19 = input("Entre the 5th Word here-->")
        a20 = input("Entre the 6th Word here-->")
        a21 = input("Entre the 7th Word here-->")
        a22 = input("Entre the 8th Word here-->")
        a23 = input("Entre the 9th Word here-->")
        a24 = input("Entre the 10th Word here-->")

        b1 = a15 + a16 + a17 + a18 + a19 + a20 + a21 + a22 + a23 + a24 
        print(b1)
        if b1 == a1:
            print("Great you have formed that word congratulations", aa)
            print('---------------------------------------------------------------------------------------------------')
            p = p+1
        elif b1 != a1:
            print("Sorry you failed!!!", aa)
            print('you have formed O_O--? ', b1)
            print('You have to form this word O_O-> ', a1)
            print('---------------------------------------------------------------------------------------------------')
        else:
            print("Sorry you failed!!!")
            print('---------------------------------------------------------------------------------------------------')

    elif len(a1) == '11':
        a3 = random.choice(a2)
        a4 = random.choice(a2)
        a5 = random.choice(a2)
        a6 = random.choice(a2)
        a7 = random.choice(a2)
        a8 = random.choice(a2)
        a9 = random.choice(a2)
        a10 = random.choice(a2)
        a11 = random.choice(a2)
        a12 = random.choice(a2)
        a13 = random.choice(a2)
        if a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a3 == a9 or a3 == a10 or a3 == a11 or a3 == a12 \
                or a3 == a13:
            a3 = random.choice(a2)
        elif a4 == a3 or a4 == a5 or a4 == a6 or a4 == a7 or a4 == a8 or a4 == a9 or a4 == a10 or a4 == a11 or a4 == \
                a12 or a4 == a13:
            a4 = random.choice(a2)
        elif a5 == a3 or a5 == a4 or a5 == a6 or a5 == a7 or a5 == a8 or a5 == a9 or a5 == a10 or a5 == a11 or a5 == \
                a12 or a5 == a13:
            a5 = random.choice(a2)
        elif a6 == a3 or a6 == a4 or a6 == a5 or a6 == a7 or a6 == a8 or a6 == a9 or a6 == a10 or a6 == a11 or a6 == \
                a12 or a6 == a13:
            a6 = random.choice(a2)
        elif a7 == a3 or a7 == a4 or a7 == a5 or a7 == a6 or a7 == a8 or a7 == a9 or a7 == a10 or a7 == a11 or a7 == \
                a12 or a7 == a13:
            a7 = random.choice(a2)
        elif a8 == a3 or a8 == a4 or a8 == a5 or a8 == a6 or a8 == a7 or a8 == a9 or a8 == a10 or a8 == a11 or a8 == \
                a12 or a8 == a13:
            a8 = random.choice(a2)
        elif a9 == a3 or a9 == a4 or a9 == a5 or a9 == a6 or a9 == a7 or a9 == a8 or a9 == a10 or a9 == a11 or a9 == \
                a12 or a9 == a13:
            a9 = random.choice(a2)
        elif a10 == a3 or a10 == a4 or a10 == a5 or a10 == a6 or a10 == a7 or a10 == a8 or a10 == a9 or a10 == a11 or \
                a10 == a12 or a10 == a13:
            a10 = random.choice(a2)
        elif a11 == a3 or a11 == a4 or a11 == a5 or a11 == a6 or a11 == a7 or a11 == a8 or a11 == a9 or a11 == a10 or \
                a11 == a12 or a11 == a13:
            a11 = random.choice(a2)
        elif a12 == a3 or a12 == a4 or a12 == a5 or a12 == a6 or a12 == a7 or a12 == a8 or a12 == a9 or a12 == a10 or \
                a12 == a11 or a12 == a13:
            a12 = random.choice(a2)
        elif a13 == a3 or a13 == a4 or a13 == a5 or a13 == a6 or a13 == a7 or a13 == a8 or a13 == a9 or a13 == a10 or \
                a13 == a11 or a13 == a12:
            a13 = random.choice(a2)
        else:
            pass
            a13 = random.choice(a2)
        print("You have to find and the word from -_->", a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13)
        print("Thinking-Thinking")
        a15 = input("Entre the 1st Word here-->")
        a16 = input("Entre the 2nd Word here-->")
        a17 = input("Entre the 3rd Word here-->")
        a18 = input("Entre the 4rth Word here-->")
        a19 = input("Entre the 5th Word here-->")
        a20 = input("Entre the 6th Word here-->")
        a21 = input("Entre the 7th Word here-->")
        a22 = input("Entre the 8th Word here-->")
        a23 = input("Entre the 9th Word here-->")
        a24 = input("Entre the 10th Word here-->")
        a25 = input("Entre the 11th Word here-->")
        b1 = a15 + a16 + a17 + a18 + a19 + a20 + a21 + a22 + a23 + a24 + a25
        print(b1)
        if b1 == a1:
            print("Great you have formed that word congratulations", aa)
            print('---------------------------------------------------------------------------------------------------')
            p = p+1
        elif b1 != a1:
            print("Sorry you failed!!!", aa)
            print('you have formed O_O--? ', b1)
            print('You have to form this word O_O-> ', a1)
            print('---------------------------------------------------------------------------------------------------')
        else:
            print("Sorry you failed!!!")
            print('---------------------------------------------------------------------------------------------------')

    elif len(a1) == '12':
        a3 = random.choice(a2)
        a4 = random.choice(a2)
        a5 = random.choice(a2)
        a6 = random.choice(a2)
        a7 = random.choice(a2)
        a8 = random.choice(a2)
        a9 = random.choice(a2)
        a10 = random.choice(a2)
        a11 = random.choice(a2)
        a12 = random.choice(a2)
        a13 = random.choice(a2)
        a14 = random.choice(a2)
        if a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a3 == a9 or a3 == a10 or a3 == a11 or\
                a3 == a12 or a3 == a13 or a3 == a14:
            a3 = random.choice(a2)
        elif a4 == a3 or a4 == a5 or a4 == a6 or a4 == a7 or a4 == a8 or a4 == a9 or a4 == a10 or a4 == a11 or\
                a4 == a12 or a4 == a13 or a4 == a14:
            a4 = random.choice(a2)
        elif a5 == a3 or a5 == a4 or a5 == a6 or a5 == a7 or a5 == a8 or a5 == a9 or a5 == a10 or a5 == a11 or\
                a5 == a12 or a5 == a13 or a5 == a14:
            a5 = random.choice(a2)
        elif a6 == a3 or a6 == a5 or a6 == a4 or a6 == a7 or a6 == a8 or a6 == a9 or a6 == a10 or a6 == a11 or\
                a6 == a12 or a6 == a13 or a6 == a14:
            a6 = random.choice(a2)
        elif a7 == a3 or a7 == a5 or a7 == a4 or a7 == a6 or a7 == a8 or a7 == a9 or a7 == a10 or a7 == a11 or\
                a7 == a12 or a7 == a13 or a7 == a14:
            a7 = random.choice(a2)
        elif a8 == a3 or a8 == a5 or a8 == a4 or a8 == a6 or a8 == a7 or a8 == a9 or a8 == a10 or a8 == a11 or\
                a8 == a12 or a8 == a13 or a8 == a14:
            a8 = random.choice(a2)
        elif a9 == a3 or a9 == a5 or a9 == a4 or a9 == a6 or a9 == a7 or a9 == a8 or a9 == a10 or a9 == a11 or\
                a9 == a12 or a9 == a13 or a9 == a14:
            a9 = random.choice(a2)
        elif a10 == a3 or a10 == a5 or a10 == a4 or a10 == a6 or a10 == a7 or a10 == a8 or a10 == a9 or a10 == a11 or\
                a10 == a12 or a10 == a13 or a10 == a14:
            a10 = random.choice(a2)
        elif a11 == a3 or a11 == a5 or a11 == a4 or a11 == a6 or a11 == a7 or a11 == a8 or a11 == a9 or a11 == a10 or\
                a11 == a12 or a11 == a13 or a11 == a14:
            a11 = random.choice(a2)
        elif a12 == a3 or a12 == a5 or a12 == a4 or a12 == a6 or a12 == a7 or a12 == a8 or a12 == a9 or a12 == a10 or\
                a12 == a11 or a12 == a13 or a12 == a14:
            a12 = random.choice(a2)
        elif a13 == a3 or a13 == a4 or a13 == a5 or a13 == a6 or a13 == a7 or a13 == a8 or a13 == a9 or a13 == a10 or\
                a13 == a11 or a13 == a12 or a13 == a14:
            a13 = random.choice(a2)
        elif a14 == a3 or a14 == a4 or a14 == a5 or a14 == a6 or a14 == a7 or a14 == a8 or a14 == a9 or a14 == a10 or\
                a14 == a11 or a14 == a12 or a14 == a13:
            a14 = random.choice(a2)
        else:
            pass

        print("You have to find and the word from -_->", a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14)
        print("Thinking-Thinking")
        a15 = input("Entre the 1st Word here-->")
        a16 = input("Entre the 2nd Word here-->")
        a17 = input("Entre the 3rd Word here-->")
        a18 = input("Entre the 4rth Word here-->")
        a19 = input("Entre the 5th Word here-->")
        a20 = input("Entre the 6th Word here-->")
        a21 = input("Entre the 7th Word here-->")
        a22 = input("Entre the 8th Word here-->")
        a23 = input("Entre the 9th Word here-->")
        a24 = input("Entre the 10th Word here-->")
        a25 = input("Entre the 11th Word here-->")
        a26 = input("Entre the 12th Word here-->")
        b1 = a15 + a16 + a17 + a18 + a19 + a20 + a21 + a22 + a23 + a24 + a25 + a26
        print(b1)
        if b1 == a1:
            print("Great you have formed that word congratulations", aa)
            print('---------------------------------------------------------------------------------------------------')
            p = p+1
            print('---------------------------------------------------------------------------------------------------')
        elif b1 != a1:
            print("Sorry you failed!!!", aa)
            print('you have formed O_O--? ', b1)
            print('You have to form this word O_O-> ', a1)
            print('---------------------------------------------------------------------------------------------------')
        else:
            print("Sorry you failed!!!")
            print('---------------------------------------------------------------------------------------------------')

    elif len(a1) == '13':
        a3 = random.choice(a2)
        a4 = random.choice(a2)
        a5 = random.choice(a2)
        a6 = random.choice(a2)
        a7 = random.choice(a2)
        a8 = random.choice(a2)
        a9 = random.choice(a2)
        a10 = random.choice(a2)
        a11 = random.choice(a2)
        a12 = random.choice(a2)
        a13 = random.choice(a2)
        a14 = random.choice(a2)
        a111 = random.choice(a2)
        if a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a3 == a9 or a3 == a10 or a3 == a11 or a3 == a12 \
                or a3 == a13 or a3 == a14 or a3 == a111:
            a3 = random.choice(a2)
        elif a4 == a3 or a4 == a5 or a4 == a6 or a4 == a7 or a4 == a8 or a4 == a9 or a4 == a10 or a4 == a11 or\
                a4 == a12 or a4 == a13 or a4 == a14 or a4 == a111:
            a4 = random.choice(a2)
        elif a5 == a3 or a5 == a4 or a5 == a6 or a5 == a7 or a5 == a8 or a5 == a9 or a5 == a10 or a5 == a11 or\
                a5 == a12 or a5 == a13 or a5 == a14 or a5 == a111:
            a5 = random.choice(a2)
        elif a6 == a3 or a6 == a5 or a6 == a4 or a6 == a7 or a6 == a8 or a6 == a9 or a6 == a10 or a6 == a11 or\
                a6 == a12 or a6 == a13 or a6 == a14 or a6 == a111:
            a6 = random.choice(a2)
        elif a7 == a3 or a7 == a5 or a7 == a4 or a7 == a6 or a7 == a8 or a7 == a9 or a7 == a10 or a7 == a11 or\
                a7 == a12 or a7 == a13 or a7 == a14 or a7 == a111:
            a7 = random.choice(a2)
        elif a8 == a3 or a8 == a5 or a8 == a4 or a8 == a6 or a8 == a7 or a8 == a9 or a8 == a10 or a8 == a11 or\
                a8 == a12 or a8 == a13 or a8 == a14 or a8 == a111:
            a8 = random.choice(a2)
        elif a9 == a3 or a9 == a5 or a9 == a4 or a9 == a6 or a9 == a7 or a9 == a8 or a9 == a10 or a9 == a11 or\
                a9 == a12 or a9 == a13 or a9 == a14 or a9 == a111:
            a9 = random.choice(a2)
        elif a10 == a3 or a10 == a5 or a10 == a4 or a10 == a6 or a10 == a7 or a10 == a8 or a10 == a9 or a10 == a11 or\
                a10 == a12 or a10 == a13 or a10 == a14 or a10 == a111:
            a10 = random.choice(a2)
        elif a11 == a3 or a11 == a5 or a11 == a4 or a11 == a6 or a11 == a7 or a11 == a8 or a11 == a9 or a11 == a10 or\
                a11 == a12 or a11 == a13 or a11 == a14 or a11 == a111:
            a11 = random.choice(a2)
        elif a12 == a3 or a12 == a5 or a12 == a4 or a12 == a6 or a12 == a7 or a12 == a8 or a12 == a9 or a12 == a10 or\
                a12 == a11 or a12 == a13 or a12 == a14 or a12 == a111:
            a12 = random.choice(a2)
        elif a13 == a3 or a13 == a4 or a13 == a5 or a13 == a6 or a13 == a7 or a13 == a8 or a13 == a9 or a13 == a10 or\
                a13 == a11 or a13 == a12 or a13 == a14 or a13 == a111:
            a13 = random.choice(a2)
        elif a14 == a3 or a14 == a4 or a14 == a5 or a14 == a6 or a14 == a7 or a14 == a8 or a14 == a9 or a14 == a10 or\
                a14 == a11 or a14 == a12 or a14 == a13 or a14 == a111:
            a14 = random.choice(a2)
        elif a111 == a3 or a111 == a4 or a111 == a5 or a111 == a6 or a111 == a7 or a111 == a8 or a111 == a9 or\
                a111 == a10 or a111 == a11 or a111 == a12 or a111 == a13 or a111 == a14:
            a111 = random.choice(a2)
        else:
            pass
        print("You have to find and the word from -_->", a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a111)
        print("Thinking-Thinking")
        a15 = input("Entre the 1st Word here-->")
        a16 = input("Entre the 2nd Word here-->")
        a17 = input("Entre the 3rd Word here-->")
        a18 = input("Entre the 4rth Word here-->")
        a19 = input("Entre the 5th Word here-->")
        a20 = input("Entre the 6th Word here-->")
        a21 = input("Entre the 7th Word here-->")
        a22 = input("Entre the 8th Word here-->")
        a23 = input("Entre the 9th Word here-->")
        a24 = input("Entre the 10th Word here-->")
        a25 = input("Entre the 11th Word here-->")
        a26 = input("Entre the 12th Word here-->")
        a27 = input("Entre the 13th Word here-->")
        b1 = a15 + a16 + a17 + a18 + a19 + a20 + a21 + a22 + a23 + a24 + a25 + a26 + a27

        print(b1)
        if b1 == a1:
            print("Great you have successFULLY formed that word congratulations", aa)
            p = p+1
            print('---------------------------------------------------------------------------------------------------')
        elif b1 != a1:
            print("Sorry you failed!!!", aa)
            print('you have formed O_O--? ', b1)
            print('You have to form this word O_O-> ', a1)
            print('---------------------------------------------------------------------------------------------------')
        else:
            print("Sorry you failed!!!")
            print('---------------------------------------------------------------------------------------------------')
        
while a < 11:
    print("So", aa, "your score is -_0 ", p, "/10")

    a121 = input("Do you want to play again Y or N")
    if a121 == 'Y' or 'y':
        print("Okay restarting the again")
        continue
    elif a121 == 'N' or 'n':
        print("okay finishing  ~thank you~ !-_0!")
        exit()

    
