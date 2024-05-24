# 다음과 같이 두 개의 숫자 N, M이 주어질 때, N의 M 거듭제곱 값을 구하는 프로그램을 재귀호출을 이용하여 구현해 보아라.

# 2 5 = 2 X 2 X 2 X 2 X 2 = 32

# 3 6 = 3 X 3 X 3 X 3 X 3 X 3 = 729

# [제약 사항]
# java: import java.util.Scanner;
# c/c++: #include
# 를 제외한 나머지 라이브러리 사용을 금한다.

# 총 10개의 테스트 케이스가 주어진다.

# 결과 값은 Integer 범위를 넘어가지 않는다.
 
# [입력]

# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 두 개의 숫자가 주어진다.

# [출력]

# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

def rec(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        half_power = rec(a, b // 2)
        if b % 2 == 0:
            return half_power * half_power
        else:
            return half_power * half_power * a

# 테스트 케이스의 수는 10으로 고정
for i in range(1, 11):
    n = int(input())  # 테스트 케이스 번호
    a, b = map(int, input().split())

    result = rec(a, b)
    print(f"#{i} {result}")