items = {'apples': 12, 'drinks':12, 'no':30, 'napkins':40}

def picnic_items(items, leftWidth, rightWidth):
    print('PICNIC_ITEMS'.center(leftWidth + rightWidth, '='))
    for k, v in items.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
        
picnic_items(items, 12, 5)

"""
===PICNIC_ITEMS==
apples......   12
drinks......   12
no..........   30
napkins.....   40
"""
