from random import sample
from psychopy import visual, core, event
import csv

# Option 1: First show list of random words to recall, then ask them to free recall word

# Option 2: First show list of random words to recall, then show a list of words

# options 3: Show list of random words, then present words that may be related and ask them to say yes or no

#Option 4: combine recall and recognition

# Op3&4

# venv -> source ~/venv/psychopy/bin/activate

def instruct(win):
    start = visual.TextStim(win, text="Your task will be to remember a list of words. You will then be asked to recognize the previously shown words after. The experiment will autoproceed after 15 seconds.")
    start.autoDraw = True
    win.flip()
    # core.wait(1) ## testing value
    core.wait(15)
    start.autoDraw = False
    
def cross(win):
    default = visual.TextStim(win, text="+")
    default.autoDraw = True
    win.flip()
    core.wait(1)
    default.autoDraw = False

def initialList(win, listA, listB):
    
    final = listA + listB
    
    wordStim = sample(final, len(final))

    counter = 0
    
    for word in wordStim:
        stim = visual.TextStim(win, text=word)
        stim.autoDraw = True
        win.flip()
        #core.wait(0.01) ## testing val
        core.wait(1.5)
        stim.autoDraw = False

        win.flip()
        #core.wait(0.01) ## testing val
        core.wait(0.5)

def recog(win, listTotal, participant):
    recogInst = visual.TextStim(win, text="You will now be shown a list of words. Indicate with ~a~ if it is an old word, or indicate with ~l~ if it is a new word. The experiment will autoproceed after 30 seconds.")
    recogInst.autoDraw = True
    win.flip()
    #core.wait(0.1) ## testing val
    core.wait(30)
    recogInst.autoDraw = False

    newWords = ["monkey", "ankle", "table", "belt", "elephant", "pigeon", "peacock", "apple", "box", "book", "suit", "pencil"]

    falses = ["space", "planet", "comet", "stars"]

    newWords = newWords + falses

    finalWords = newWords + listTotal

    recogWords = sample(finalWords, len(finalWords))

    results = []
    perfect = []
    
    for word in recogWords:

        if word in newWords:
            perfect.append("NEW")
        else:
            perfect.append("OLD")
        
        rand = visual.TextStim(win, text=word)
        rand.autoDraw = True
        win.flip()
        
        keypress = event.waitKeys(keyList=["a", "l"])
        win.flip()

        if keypress[0] == "a":
            results.append("OLD")
        elif keypress[0] == "l":
            results.append("NEW")

        rand.autoDraw = False


    rightness = []
    falseList = []
    participantNumber = [participant] * 32

    for count, value in enumerate(results):
        if value == perfect[count]:
            rightness.append("0")
        else:
            rightness.append("1")

    for count, value in enumerate(recogWords):
        if value in falses:
            falseList.append("*")
        else:
            falseList.append(" ")
      
    
    filename = "%s.csv" % participant

    rowData = zip(recogWords, perfect, results, rightness, falseList, participantNumber)
    # change to columns
    with open(filename, "w", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(["Word", "OldNew", "SubjResponse", "Correct", "SpecWords" ,"Participant"])
        for row in rowData:
            writer.writerow(row)
        #writer.writerow(["row 1 = words", "row 2 = correct answers", "row 3 = participant results"])
        #writer.writerow(recogWords)
        #writer.writerow(perfect)
        #writer.writerow(results)
        #writer.writerow(rightness)
        f.close()
    
   # tofile = open(filename, "w")
   # tofile.write(strResult)
   # tofile.write(strWords)
   # tofile.write(strPerfect)
   # tofile.close()
    
    

def compiled():

    participant = input("Enter participant #: ")
    
    randomL = ["knight", "lotion", "phone", "yogurt", "ball", "laptop", "grapes", "spoon"]
    space = ["rocket", "asteroid", "meteor", "alien", "deep", "black", "vast", "discovery"]
    
    final = randomL + space
    
    win = visual.Window([720, 720])

    instruct(win)

    cross(win)

    initialList(win, randomL, space)

    recog(win, final, participant)   
    
    core.quit()

    
compiled()
    
    
