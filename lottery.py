 from random import randint


def generate_numbers(n):
    # 무작위로 1~45사이의 서로 다른 숫자 6개를 뽑아 리스트에 넣고 그 리스트를 리턴.
    numbers = []
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers

#print(generate_numbers(6))



def draw_winning_numbers():
    # [당첨숫자 6개 + 보너스 숫자 1개]의 리스트 리턴. 당첨숫자는 정렬.
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]




def count_matching_numbers(list_1, list_2):
    # 두 리스트 사이에 겹치는 숫자갯수를 리턴
    count = 0
    
    for num in list_1:
        if num in list_2:
            count += 1
    return numbers


count = count_matching_numbers(numbers, winning_numbers[:6])
bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

if count == 6:
    return 1000000000
elif count == 5 and bonus_count == 1:
    return 50000000
elif count == 5:
    return 1000000
elif count == 4:
    return 50000
elif count == 3:
    return 5000
else:
    return 0
