# Panini Montecarlo
# Compute the expected cost of filling the FIFA world cup album just by buying packs of cars

from datetime import datetime
from random import randint

def isComplete(collection):
    for i in range(len(collection)):
        if collection[i] == 0:
            return False
    return True

def countRepeated(collection):
    repeated = 0
    for i in range(len(collection)):
        if collection[i] > 1:
            repeated += collection[i] - 1
    return repeated

def montecarloIteration(total_cards, cards_per_pack, price_per_pack):
    collection = [0] * total_cards
    total_cost = 0
    packs_count = 0

    while not isComplete(collection):
        packs_count += 1
        total_cost += price_per_pack

        pack = [randint(1,total_cards) - 1 for _ in range(cards_per_pack)]

        for card in pack:
            collection[card] += 1

    repeated = countRepeated(collection)
    
    return packs_count, total_cost, repeated

def montecarlo(total_cards, cards_per_pack, price_per_pack, total_iterations):
    average_packs_count = 0
    average_total_cost = 0
    average_repeated = 0

    for i in range(total_iterations):
        expected_packs_count, expected_total_cost, expected_repeated = montecarloIteration(total_cards, cards_per_pack, price_per_pack)

        average_packs_count += expected_packs_count
        average_total_cost += expected_total_cost
        average_repeated += expected_repeated

    average_packs_count /= total_iterations
    average_total_cost /= total_iterations
    average_repeated /= total_iterations

    return average_packs_count, average_total_cost, average_repeated

if __name__=="__main__":
    total_cards = 980
    cards_per_pack = 7
    price_per_pack = 25
    montecarlo_iterations = 1000

    start = datetime.now()
    print(f"Perfect cost to fill: {total_cards / cards_per_pack * price_per_pack}")
    print()
    
    expected_packs_count, expected_total_cost, expected_repeated = montecarlo(total_cards, cards_per_pack, price_per_pack, montecarlo_iterations)
    print(f"Montecarlo results ({montecarlo_iterations} iterations):")
    print(f"Expected total cost: {expected_total_cost}")
    print(f"Expected pack count: {expected_packs_count}")
    print(f"Expected repeated cards: {expected_repeated}")
    end = datetime.now()

    elapsedTime = end - start
    print(f"\nElapsed time: {elapsedTime}")