import json
profit = {}
pr = {}
pro = 0
pavg = 0
i = 0
with open('7.txt', 'r') as file:
    for line in file:
        name, firm, earning, costs = line.split()
        profit[name] = int(earning) - int(costs)
        if profit.setdefault(name) >= 0:
            pro = pro + profit.setdefault(name)
            i += 1
    if i != 0:
        pavg = pro / i
        print(f'average_profit - {pavg:.2f}')
    else:
        print(f'no profit')
    pr = {'average_profit': round(pavg)}
    profit.update(pr)
    print(f'company profit - {profit}')

with open('7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'total: \n '
          f' {js_str}')