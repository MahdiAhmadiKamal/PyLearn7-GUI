items = ['1','introduction','to','molecular','8','the','learning','module','5']

new_items = [item for item in items if not item.isdigit()]

print (new_items)