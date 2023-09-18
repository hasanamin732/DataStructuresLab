spicy_foods = [
{
"name": "Green Curry",
"cuisine": "Thai",
"heat_level": 9,
},
{
"name": "Buffalo Wings",
"cuisine": "American",
"heat_level": 3,
},
{
"name": "Mapo Tofu",
"cuisine": "Sichuan",
"heat_level": 6,
},
]

def get_names(spicy_foods):
    names = [i["name"] for i in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    foods=[i for i in spicy_foods if i["heat_level"]>5]
    return foods

def print_spicy_foods(spicy_foods):
    spice='\U0001F336'
    for i in spicy_foods:
        print(f"{i['name']} ({i['cuisine']}) | Heat Level: {spice*i['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_food={i["cuisine"]==cuisine for i in spicy_foods}
    return spicy_food

def print_spiciest_foods(spicy_foods):
    spiciest=get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    heat_levels=[i["heat_level"] for i in spicy_foods]
    return sum(heat_levels)/len(heat_levels)

def create_spicy_food(spicy_foods):
    new={
        "name":str(input("Enter name for yor spicy food: ")),
        "cuisine":str(input("Enter cuisine for yor spicy food: ")),
        "heat_level":int(input("Enter heat_level for yor spicy food: "))
    }
    spicy_foods.append(new)
    return spicy_foods

def main(spicy_foods):
    print("Names--------")
    print(get_names(spicy_foods))
    print("Spiciest food list--------")
    print(get_spiciest_foods(spicy_foods))
    print("Spicy foods print--------")
    print_spicy_foods(spicy_foods)
    print("spicy foods by cuisine--------")
    print(get_spicy_food_by_cuisine(spicy_foods,"Sichuan"))
    print("Printing spiciest foods--------")
    print_spiciest_foods(spicy_foods)
    print("Average heat levels--------")
    print(get_average_heat_level(spicy_foods))
    print("Add a new spicy food--------")
    print(create_spicy_food(spicy_foods))

main(spicy_foods)