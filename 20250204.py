# def solution(phone_book):
#     #phone_book -> 리스트
#     phone_book.sort(key=len)
#     for i in range(len(phone_book)-1):
#         #타깃의 길이
#         targetLen = len(phone_book[i])
#         target= phone_book[i]
#         for j in range(i+1,len(phone_book)):
#             targetB = phone_book[j]
#             if target == targetB[:targetLen]:
#                 return False
#     return True


def solution(phone_book):
    phone_set = set(phone_book)

    for number in phone_book:
        for i in range(1, len(number) + 1):
            # print(number[:i])
            if number[:i] in phone_set and number[:i] != number:
                return False
    return True