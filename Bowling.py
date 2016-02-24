#  File: Bowling.py
#  Description: Calculates the score of a bowling match
#  Student's Name: Minh-Tri Ho
#  Student's UT EID: mh47723
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 01/29/16
#  Date Last Modified: 02/02/16

#Shows the upper part of the scoring
def printHeader():
    print("  1   2   3   4   5   6   7   8   9    10")
    print("+---+---+---+---+---+---+---+---+---+-----+")

#Shows the middle part of the scoring with the detailed scores
def printScore(score):
    #Initialize the string that will contain the detailed scores
    res = "|"

    #Rewrite score to add a " " list cell after X
    i = 0
    while(i < len(score)):
        if(score[i] == "X" and i < 18):
            score.insert(i + 1, " ")
            i += 1
        i += 1

    if(len(score) == 20):
        score += " "
        
    for i in range(len(score)):
        res += str(score[i])
        if(i%2 == 0 and i <= 19):
            res += " "
        elif(i%2 == 1 and i <= 18):
            res += "|"
        elif(i%2 == 1 and i == 19):
            res += " "
    res += "|"
    print(res)

#Shows the middle part of the scoring with the accumulated scores
def printScoreTotal(score):
    #Initialize the string that will contain the accumulated scores
    res = "|"

    #Make a copy of the score we imported
    scoreNum = score[:]
    
    #Transform symbols in numbers
    for i in range(len(score)):
        if(score[i] == "X"):
            scoreNum[i] = 10
        elif(score[i] == "-"):
            scoreNum[i] = 0
        elif(score[i] == " "):
            scoreNum[i] = 0
        elif(score[i] == "/"):
            scoreNum[i] = 10 - (int)(scoreNum[i-1])
        else:
            scoreNum[i] = (int)(scoreNum[i])

    #Calculate the score per frame
    scoreTt = []
    scoreTtCum = []
    for i in range(0, len(score)-2, 2):
        if(score[i] == "X"):
            if(i <= 14 and score[i+2] == "X"):
                scoreTt.append(scoreNum[i]+scoreNum[i+2]+scoreNum[i+4])
            elif(i == 16 and score[i+2] == "X"):
                scoreTt.append(scoreNum[i]+scoreNum[i+2]+scoreNum[i+3])
            elif(i == 18):
                scoreTt.append(scoreNum[i]+scoreNum[i+1]+scoreNum[i+2])
            else:
                scoreTt.append(scoreNum[i]+scoreNum[i+2]+scoreNum[i+3])
        elif(score[i+1] == "/"):
            scoreTt.append(scoreNum[i]+scoreNum[i+1]+scoreNum[i+2])
        else:
            scoreTt.append(scoreNum[i]+scoreNum[i+1])

        #Add that score to the last accumulated score, if it exists
        if(i == 0):
            scoreTtCum.append(scoreTt[0])
        else:
            scoreTtCum.append((scoreTtCum[(int)(i/2)-1]) + scoreTt[(int)(i/2)])

    #Add the aggregated scores to the result (with correct formatage)
    for i in range(len(scoreTtCum)):
        if(scoreTtCum[i] < 10):
            if(i == 9):
                res += "  " + str(scoreTtCum[i]) + "  |"
            else:
                res += " " + str(scoreTtCum[i]) + " |"
        elif(scoreTtCum[i] < 100):
            if(i == 9):
                res += "  " + str(scoreTtCum[i]) + " |"
            else:
                res += " " + str(scoreTtCum[i]) + "|"
        else:
            if(i == 9):
                res += " " + str(scoreTtCum[i]) + " |"
            else:
                res += str(scoreTtCum[i]) + "|"

    #Display the result
    print(res)

#Shows the lower part of the scoring
def printFooter():
    print("+---+---+---+---+---+---+---+---+---+-----+\n")

def main():
    file_name = "scores.txt"

    in_file = open(file_name, 'r')
    for line in in_file:
        printHeader()
        score_raw = line.rstrip("\n")
        score = score_raw.split()
        printScore(score)
        printScoreTotal(score)
        printFooter()
        


main()
