https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3

#1차 코드

 def solution(phone_book):
     #phone_book -> 리스트
     phone_book.sort(key=len)
     for i in range(len(phone_book)-1):
         #타깃의 길이
         targetLen = len(phone_book[i])
         target= phone_book[i]
         for j in range(i+1,len(phone_book)):
             targetB = phone_book[j]
             if target == targetB[:targetLen]:
                 return False
     return True

접두사를 찾기 위해 -> 리스트 길이 순서대로 정렬 후, 해당 리스트의 앞에서부터 뒤에서까지 있는지 완전탐색

##2차 코드
def solution(phone_book):
    phone_set = set(phone_book)

    for number in phone_book:
        for i in range(1, len(number) + 1):
            # print(number[:i])
            if number[:i] in phone_set and number[:i] != number:
                return False
    return True


세트로 변경
꼭 길이 순서대로 정렬하지 않아도 됨 왜냐면 다른 곳에 [11, 1] 이런식으로 존재한다면 어짜피 접두사에 존재하게 됨
그러니까 하나씩 뜯어서 생각하는 걸러 

number[:i]는 항상 number의 접두사이기 때문에 number보다 긴 숫자가 올 수는 없습니다.

코드 분석
python


for i in range(1, len(number) + 1):
    if number[:i] in phone_set and number[:i] != number:
        return False
for i in range(1, len(number) + 1)::

i는 1부터 len(number)까지의 값을 가집니다. 즉, i는 number의 길이와 같거나 그보다 작습니다.
이 루프는 number의 길이에 따라 반복되므로, i의 최대값은 len(number)입니다.
number[:i]:

number[:i]는 number의 첫 i글자를 잘라서 접두사를 생성합니다.
예를 들어, number가 "12345"라면, number[:1]은 "1", number[:2]는 "12", ..., number[:5]는 "12345"가 됩니다.
따라서 number[:i]는 항상 number의 길이보다 짧거나 같고, 절대 길이가 더 길어질 수는 없습니다.
조건문:

if number[:i] in phone_set and number[:i] != number:에서 number[:i]는 number의 접두사이므로, number와 같지 않은 경우에만 True가 됩니다.
즉, number와 같은 경우는 i가 len(number)일 때만 발생하며, 이 경우는 조건문에서 number[:i] != number가 False가 되어 해당 조건을 통과하지 않습니다.

