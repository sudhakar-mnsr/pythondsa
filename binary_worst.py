# returns position in array where the card in query is found
# if the card is not found then return -1
# if the length of cards is 0 then return -1 as well
# for repititions just give first occurance and return
# def locate_card(cards, query):
#     position = 0
#     if len(cards) == 0:
#         return -1
#     while True:
#         if cards[position] == query:
#             return position
#         position += 1
#         if position == len(cards):
#             return -1
def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


tests = []
# 1. No cards present
test = {"input": {"cards": [], "query": 13}, "output": -1}
tests.append(test)
# 2. only one card present and that is in query
test = {"input": {"cards": [13], "query": 13}, "output": 0}
tests.append(test)
# 3. only one card and that is not in query
test = {"input": {"cards": [13], "query": 2}, "output": -1}
tests.append(test)
# 4. the card is first one
test = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 13}, "output": 0}
tests.append(test)
# 5. query card is last one
test = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 0}, "output": 7}
tests.append(test)
# 6. all cards are same and query matches
test = {"input": {"cards": [1, 1, 1, 1, 1, 1, 1, 1], "query": 1}, "output": 0}
tests.append(test)
# 7. all cards same and query card not present
test = {"input": {"cards": [1, 1, 1, 1, 1, 1, 1, 1], "query": 7}, "output": -1}
tests.append(test)
# 8. multiple repetitions of query card
test = {"input": {"cards": [13, 13, 10, 7, 7, 7, 1, 0], "query": 7}, "output": 3}
tests.append(test)
# 9. even number of cards
test = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7}, "output": 3}
tests.append(test)
# 10. odd number of cards
test = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1], "query": 7}, "output": 3}
tests.append(test)
# 11. The list cards doesnt contain the card
test = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 2}, "output": -1}
tests.append(test)
# locate_card(test[input][cards], test[input][query]
print(tests)

for i, test_case in enumerate(tests):
    print("Test case No. " + str(i))
    print(locate_card(**test_case["input"]) == test_case["output"])
# print(locate_card(test[input][cards], test[input][query]) == test['output'])
