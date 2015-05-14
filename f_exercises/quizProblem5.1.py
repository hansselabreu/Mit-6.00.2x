import random
import pylab

def sampleQuizzes():
    #two midterm quizzes and a final exam
    #25% each midterm and 50% the final
    #midterm 1: 50 <= grade <= 80
    #midterm 2: 60 <= grade <= 90
    #final exam: 55 <= grade <= 95
    TRIALS = range(10000)
    midterm1 = 0
    midterm2 = 0
    total = 0
    cont = 0
    #calculte probability of a studing having
    #a final score >= 70 and <= 75.
    for n in TRIALS:
        m1 = random.randint(50, 80)
        m2 = random.randint(60, 90)
        f = random.randint(55, 95)
        final_grade = (m1*0.25) + (m2*0.25) + (f*0.50)
        if final_grade >= 70 and final_grade <= 75:
            total += final_grade
            cont +=1
    return cont/10000.0

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    trials = range(numTrials)
    scores = []
    for n in trials:
        m1 = random.randint(50, 80)
        m2 = random.randint(60, 90)
        f = random.randint(55, 95)
        final_grade = (m1*0.25) + (m2*0.25) + (f*0.50)
        scores.append(final_grade)
    return scores


def plotQuizzes():
    scores = generateScores(10000)
    pylab.hist(scores, bins=7)
    pylab.title("Distribution of Scores")
    pylab.xlabel("Final Score")
    pylab.ylabel("Number of Trials")
    pylab.show()
