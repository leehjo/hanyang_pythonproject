###########################################################################################
#
# Title : Python Project - 뉴스 클러스터링
# 학번 : 2017053136
# 이름 : 이형조
#
############################################################################################
class lower:
    def __init__(self, a):
        self.a = a
    def low(self):
        result = self.a.lower()
        return result

def solution(str1, str2):

    # class 사용!! 문제에서 대소문자를 구분하지 않는다라고 제시
    str1 = lower(str1)
    str2 = lower(str2)

    str1 = str1.low()
    str2 = str2.low()

    list1 = []
    # 문자열 두 글자씩 끊어서 다중 집합 만들기
    # 기타 공백, 숫자, 특수문자 제거를 위해 isalpha 사용
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            list1.append(str1[i:i+2])

    list2 = []
    # 문자열 두 글자씩 끊어서 다중 집합 만들기
    # 기타 공백, 숫자, 특수문자 제거를 위해 isalpha 사용
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            list2.append(str2[i:i+2])

    # 교집합
    intersection = 0
    # 합집합
    union = 0

    # list1, list2의 중복값을 제거하기 위해 set 사용
    for s in set(list1+list2):
        union += max(list1.count(s), list2.count(s))
        intersection += min(list1.count(s), list2.count(s))

    # list1과 list2가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 1 * 65536 로 정의한다.
    if intersection == 0:
        return 65536
    else:
        # 유사도 값은 0에서 1 사이의 실수이므로, 다루기 쉽게 65536 곱한 후 정수 출력 위한 int
        answer = int(intersection / union * 65536)
        return answer

    if __name__ == "__main__" :
        print(' str1', '    str2',' answer')
        print('FRANCE', '  french',    solution('FRANCE', 'french'))
        print('handshake', '  shake hands',    solution('handshake', 'shake hands'))
        print('aa1+aa2', '  AAAA12',    solution('aa1+aa2', 'AAAA12'))
        print('E=M*C^2', '  e=m*c^2',    solution('E=M*C^2', 'e=m*c^2'))