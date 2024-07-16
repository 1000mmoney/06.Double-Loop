# 3단을 출력하고 3 x 3 = 9 로 어떤 값을 곱하였는지도 함께 출력하라.

# 나
t = range(1, 10)

for x in t:
    y = int(x)*3
    z = int(x)
    print("3 x", z, "=", y)

# 교수님

# 3단을 출력하라
for index in range(0, 10):
# 3 x 3 = 9 로 어떤 값을 곱하였는지도 함께 출력
    number = 3*index
    print("3 x", index, "=", number)

