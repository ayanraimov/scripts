from datetime import date

def get_villain_name(birthdate): 
    first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    # your code here
    birthdate = birthdate.split("-")
    month = int(birthdate[1])
    day = int(birthdate[2])
    villain_name = f"{first[month-1]} {last[day-1]}"
    return villain_name