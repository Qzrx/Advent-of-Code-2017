# Day 6 - Memory Reallocation-1

test_banks = [0, 2, 7, 0]
fancy_banks = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3,  6]


def reallocate(memory, iterations=None, states=None):
    if iterations is None:
        iterations = 1
    if states is None:
        states = set()
    largest_bank_value = 0
    largest_bank_idx = 0
    bank_redistribution_value = 0
    L = len(memory)
    # loop through banks to find the largest value
    for bank in xrange(0, L):
        if memory[bank] > largest_bank_value:
            largest_bank_idx = bank
            largest_bank_value = memory[bank]
    # pop + store largest value
    bank_redistribution_value = memory[largest_bank_idx]
    memory[largest_bank_idx] = 0
    while bank_redistribution_value > 0:
        # print(str(bank_redistribution_value) + ':' + str(memory))
        largest_bank_idx = largest_bank_idx + 1
        memory[largest_bank_idx % L] = memory[largest_bank_idx % L] + 1
        bank_redistribution_value = bank_redistribution_value - 1
        if str(memory) in states:
            print('Found a duplicated memory state: ' + str(memory))
            print('Required ' + str(iterations) + ' iterations')
            return(None)
        states.add(str(memory))
    iterations = iterations + 1
    # print(str(iterations))
    # print(str(memory))
    reallocate(memory, iterations, states)

reallocate(test_banks)
reallocate(fancy_banks)
