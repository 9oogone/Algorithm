switch = int(input())  # 스위치의 개수
arr = list(map(int, input().split()))  # 스위치 처음 상태
students = int(input())  # 학생 수

for _ in range(students):
    gender, num = map(int, input().split())  # gender = 성별 num = 받은 스위치 넘버

    if gender == 1:  # 남학생이면
        for i in range(num - 1, switch, num):
            arr[i] = 1 if arr[i] == 0 else 0  # 색깔 바꾸기
    elif gender == 2:  # 여학생이면
        num -= 1  # 인덱스 이용할 것이므로 -1
        arr[num] = 1 if arr[num] == 0 else 0  # 일단 누른 스위치는 바꿔줌
        for j in range(1, switch // 2):
            if num - j < 0 or num + j >= switch or arr[num - j] != arr[num + j]:
                break
            arr[num - j] = 1 if arr[num - j] == 0 else 0
            arr[num + j] = 1 if arr[num + j] == 0 else 0

for i in range(0, switch, 20):
    print(*arr[i:i + 20])
