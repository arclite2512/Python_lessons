import json

with open('file7.txt', 'r', encoding='utf-8') as f:
    companies_profit = {}
    average_profit = {}
    all_profit = 0
    profit_count = 0
    for line in f.readlines():
        data = line.rstrip().split()
        profit = float(data[2]) - float(data[3])
        companies_profit.update({data[0]: profit})
        if profit > 0:
            profit_count += 1
            all_profit += profit
average_profit.update({"average_profit": all_profit / profit_count})

with open('file7_2.json', 'w+', encoding='utf-8') as f:
    json.dump([companies_profit, average_profit], f)
    f.seek(0)
    print(f.read())
