from pprint import pprint

with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {} 
    for row in f:
        dish_comp = []
        if not row.strip().isdigit() and ' | ' not in row:
            dish_title = row.strip()
        elif ' | ' in row:
            ingredient_name, quantity, measure = row.strip().split(' | ')
            list_wth_int = [ingredient_name, int(quantity), measure]
            name_comp = 'ingredient_name', 'quantity', 'measure'
            dish_comp.append(dict(zip(name_comp, (list_wth_int))))
            cook_book.setdefault(dish_title,[])  
            cook_book[dish_title] += dish_comp


def get_shop_list_by_dishes(list_, quantity):
    comp_list = {}
    for ttl in list_:
        for dish_ttl in cook_book:
            for comp_ in cook_book[dish_ttl]:
                if ttl == dish_ttl:
                    if comp_['ingredient_name'] not in comp_list.keys():
                        comp_list.setdefault(comp_.pop('ingredient_name'), comp_)
                        comp_['quantity'] *= quantity  
                    else:
                        comp_list[comp_['ingredient_name']]['quantity'] += comp_['quantity']*quantity
    return comp_list

list_ = ['Фахитос', 'Омлет']
quantity = 2
pprint(get_shop_list_by_dishes(list_, quantity))

print('-'*25)
pprint(cook_book)


    
