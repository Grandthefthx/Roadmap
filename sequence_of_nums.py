# Найти максимальную длинну последовательности 1 в списке
ar = [0,1,1,0,1,1,0,1,1,1,0]
cur_count = 0
max_count = 0
for i in ar:
    if i == 1:
        cur_count += 1
        max_count = max(cur_count,max_count)
    else:
        cur_count = 0

print(max_count)
# RDY
