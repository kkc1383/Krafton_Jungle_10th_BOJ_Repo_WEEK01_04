import sys

point_num = int(sys.stdin.readline().strip())
point_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(point_num)]

# 신발끈 공식 (Shoelace Formula)
area = 0
for i in range(point_num):
    # 현재 점과 다음 점 (마지막 점은 첫 점과 연결)
    x1, y1 = point_list[i]
    x2, y2 = point_list[(i + 1) % point_num]

    area += x1 * y2 - x2 * y1

# 절댓값을 취하고 2로 나눔
area = abs(area) / 2

# 소수점 첫째 자리까지 출력
print(round(area, 1))