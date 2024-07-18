# # 8. 다음 이중 리스트의 평균값을 아래 출력 결과와 같이 각각 구하여라.
my_list = [[100, 200], [400, 800], [1000, 1400]]

# for i in my_list:
#     y = int(i[0]+i[1])/2
#     print(int(y))
# for i in my_list:
#     for k in i:
#         y = k
#         x = int(k)+int(y)/2
#         print(int(x))

# 교수님

# for i in my_list:
#     var = 0
#     for j in i:
#         var = var + j
#     result = var/2
#     print(int(result))
# m = [1, 2, 3, 4, 5, 6]


for i in my_list:
    var = 0
    for k in i:
        var = var + k
    print(int(var / len(i)))

