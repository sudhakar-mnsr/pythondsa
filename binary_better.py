import math
# return position if the card is found
# return -1 if card not found
# cards empty return -1
# repetition return any correct position

# start with position len(cards)/2 (it can be fraction) (will this work if one card?)
# start = 0 end = len(cards) position = (start + end) / 2
# if card[position] < query make index start = (start + end) / 2 + 1

position = 0


def locate_card(cards, query):
    print(str(len(cards)))
    start = 0
    end = len(cards) - 1
    while start <= end:
        position = (start + end) // 2
        if cards[position] == query:
            print("Hurray!! found it at: " + str(position))
            return position
        elif cards[position] < query:
            end = position - 1
        else:
            start = position + 1
    return -1


tests = []
# 0. No cards present
test = {"input": {"cards": [], "query": 13}, "output": -1}
tests.append(test)
# 1. only one card present and that is in query
test = {"input": {"cards": [13], "query": 13}, "output": 0}
tests.append(test)
# 2. only one card and that is not in query
test = {"input": {"cards": [13], "query": 2}, "output": -1}
tests.append(test)
# 3. the card is first one
test = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 13}, "output": 0}
tests.append(test)
# 4. query card is last one
test = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 0}, "output": 7}
tests.append(test)
# 5. all cards are same and query matches
test = {"input": {"cards": [1, 1, 1, 1, 1, 1, 1, 1], "query": 1}, "output": 0}
tests.append(test)
# 6. all cards same and query card not present
test = {"input": {"cards": [1, 1, 1, 1, 1, 1, 1, 1], "query": 7}, "output": -1}
tests.append(test)
# 7. multiple repetitions of query card
test = {"input": {"cards": [13, 13, 10, 7, 7, 7, 1, 0], "query": 7}, "output": 3}
tests.append(test)
# 8. even number of cards
test = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7}, "output": 3}
tests.append(test)
# 9. odd number of cards
test = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1], "query": 7}, "output": 3}
tests.append(test)
# 10. The list cards doesnt contain the card
test = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 2}, "output": -1}
tests.append(test)
# 11. the card is first one
test = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 0}, "output": 7}
tests.append(test)
# 12. the card is first one
test = {"input": {"cards": [13, 11], "query": 11}, "output": 1}
tests.append(test)
# 13. the card is first one
test = {"input": {"cards": [13, 11], "query": 12}, "output": -1}
tests.append(test)
# locate_card(test[input][cards], test[input][query]
print(tests)

for i, test_case in enumerate(tests):
    print("Test case No. " + str(i))
    print(str(position) + str(test_case["output"]))
    print(locate_card(**test_case["input"]) == test_case["output"])
# print(locate_card(test[input][cards], test[input][query]) == test['output'])
