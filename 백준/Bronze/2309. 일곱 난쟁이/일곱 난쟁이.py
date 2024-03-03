dwarf = [int(input()) for _ in range(9)]  # 난쟁이 키 받기
total_height = sum(dwarf)  # 아홉 난쟁이 키의 합
fake = total_height - 100  # 초과하는 사이즈


for i in range(9):
    for k in range(i+1, 9):  # i와 중복되지 않도록 범위 설정
        if dwarf[i] + dwarf[k] == fake:
            dwarf.pop(k)  # k번째 난쟁이를 제거
            dwarf.pop(i)  # i번째 난쟁이를 제거
            break
    if len(dwarf) == 7:
        break
                
dwarf.sort()
for ans in dwarf:
    print(ans)
