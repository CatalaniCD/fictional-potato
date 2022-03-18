import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # red balls - green balls
    balls = [1, 1, 1, -1, -1, -1]
    # all reds = 3, all greens = -3
    success = 0
    for i in range(numTrials):
        # shuffle the bag
        random.shuffle(balls)
        # pick 3 balls
        choice = balls[:3]
        # evaluate all red, all green
        if sum(choice) in [3, -3]:
            success += 1
    return success / numTrials


print(noReplacementSimulation(10000))
