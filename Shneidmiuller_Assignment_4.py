'''
Переведите содержимое файла purchase_log.txt в словарь purchases вида:
{'1840e0b9d4': 'Продукты', ...}
'''
purchases = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for lines in f:
        lines = lines.strip()
        parts = lines.split(maxsplit=1)

        if len(parts) == 2:
            user_id = parts[0]
            category = parts[1].strip('‘’')
            purchases[user_id] = category

for i, (user_id, category) in enumerate(purchases.items()):
    if i < 2:
        print(f"{user_id} '{category}'")
        
    else:
        break
