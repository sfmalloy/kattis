num_ingredients, num_recipes = map(int, input().split())
ingredients = list(map(int, input().split()))

total_money = 0
for _ in range(num_recipes):
    line = list(map(int, input().split()))
    recipe_ingredients = line[:-1]
    price = line[-1]
    can_make = 100001
    for ing_curr, ing_total in zip(recipe_ingredients, ingredients):
        if ing_curr > 0:
            can_make = min(can_make, ing_total // ing_curr)
    total_money = max(total_money, can_make * price)
print(total_money)
