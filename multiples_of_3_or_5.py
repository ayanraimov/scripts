# Finally well done

def solution(number):
    list_numbers_to_reach_the_last = list(range(1, number, 1))
    list_multiples = list()
    for i in list_numbers_to_reach_the_last:
        if i in list_multiples:
            continue
        elif i % 3 == 0:
            list_multiples.append(i)
        elif i % 5 == 0:
            list_multiples.append(i)
        else:
            continue
    print(list_multiples)
    total = 0
    for x in list_multiples:
        total += x
    print(total)

solution(15)
solution(3)