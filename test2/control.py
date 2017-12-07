part = []
sum_ipm = 0
with open ('freq.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
       line_list = line.split()
       if len(line_list) >= 5:
            if line_list[4] == 'перех':
                print(line)
    for line in lines:
        line_list = line.split()
        if line_list[2] == 'част':
            part.append(line_list[0])
            sum_ipm = sum_ipm + float(line_list[-1])
print(part)
print('Сумма ipm: ', sum_ipm)
