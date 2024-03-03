dwarf = [int(input()) for _ in range(9)]  # 난쟁이 키 받기
total_height = sum(dwarf)  # 아홉 난쟁이 키의 합
fake = total_height - 100  # 초과하는 사이즈

while True:
    removed = False  # 두 명의 난쟁이가 제거되었는지 여부를 나타내는 플래그
    for i in range(9):
        for k in range(i+1, 9):  # i와 중복되지 않도록 범위 설정
            if dwarf[i] + dwarf[k] == fake:
                dwarf.pop(k)  # k번째 난쟁이를 제거
                dwarf.pop(i)  # i번째 난쟁이를 제거
                removed = True  # 제거되었음을 표시
                break
        if removed:  # 제거가 되었다면 외부 루프도 종료
            break

    if removed:  # 제거가 되었다면 루프를 종료
        break
dwarf.sort()
for ans in dwarf:
    print(ans)
