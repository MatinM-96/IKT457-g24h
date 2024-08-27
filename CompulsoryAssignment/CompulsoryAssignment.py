import random

# Define a simple Tsetlin Automaton
class TsetlinAutomaton:
    def __init__(self, n):
        # n is the number of states per action
        self.n = n
        # Start in the middle state (either n or n+1)
        self.state = random.choice([self.n, self.n + 1])

    # Method to handle a reward
    def reward(self):
        if self.state <= self.n and self.state > 1:
            self.state -= 1  # Move to a lower state if in the "Yes" zone
        elif self.state > self.n and self.state < 2 * self.n:
            self.state += 1  # Move to a higher state if in the "No" zone

    # Method to handle a penalty
    def penalize(self):
        if self.state <= self.n:
            self.state += 1  # Move to a higher state if in the "Yes" zone
        elif self.state > self.n:
            self.state -= 1  # Move to a lower state if in the "No" zone

    # Method to make a decision (Yes or No)
    def make_decision(self):
        if self.state <= self.n:
            return 1  # Action 1 ("Yes")
        else:
            return 2  # Action 2 ("No")




def runCompulsory():

    numberOfState = 5

    tsetlinAutomaton = []

    for _ in range(numberOfState):
        automaton = TsetlinAutomaton(numberOfState)
        tsetlinAutomaton.append(automaton)

    iteration = 100

    for _ in range(iteration):
        yes_count = 0;
        for automaton in tsetlinAutomaton:
            if automaton.make_decision() == 1:
                yes_count +=1

        if yes_count == 0:
            rewardProbability = 0.2 * 0
        elif yes_count == 1:
            rewardProbability = 1*0.2
        elif yes_count == 2:
            rewardProbability = 2*0.2
        elif yes_count == 3:
            rewardProbability = 3*0.2
        elif yes_count == 4:
            rewardProbability = 0.6 - (4-3)*0.2
        elif yes_count == 5:
            rewardProbability = 0.6 - (5-3)*0.2

        else:
            rewardProbability = 0


    countFinalYes = 0
    for automaton in tsetlinAutomaton:
        if automaton.make_decision() == 1:
            countFinalYes += 1

    final_state = []

    for automaton in tsetlinAutomaton:
        final_state.append(automaton.state)

    print("Final count of 'Yes' actions:", countFinalYes)
    print("Final states of the automata:", final_state)
