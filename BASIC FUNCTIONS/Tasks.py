# TASK 00 Can you explain this piece of code?
def f ( x ) :
    return 2 * x + 1
def g () :
    return 7
y = f (2)
print ( y )
y = f (5) + g ()
print ( y )

# Cette fonction permet de faire des calculs. 

# TASK 01

# Using the following functions, display a lettuce-tomato-double ham sandwich in your terminal.

def bread () :
    print ( " <////////// > " )
def lettuce () :
    print ( " ~~~~~~~~~~~~ " )
def tomato () :
    print ( " O O O O O O " )
def ham () :
    print ( " ============ " )

print(bread(), lettuce(), tomato(), ham(), ham(), bread())

#TASK 02: Make 42 of those lettuce-tomato-double ham sandwiches.

for i in range (42):
    (bread(), lettuce(), tomato(), ham(), ham(), bread()),

# TASK 03: Write a function that takes the number of sandwiches to prepare as a parameter and displays as many sandwiches as requested.

option_vegan = (input("Voulez vous un burger végétal ? [yes/no] "))

if option_vegan == 'yes':
    nb_sand = int(input("Combien de sandwichs vegan voulez-vous?"))
    if nb_sand <= 0:
        print("I can't do that")
    for i in range (nb_sand):
        (bread(), lettuce(), lettuce(), tomato(), tomato(), bread())
        print()
elif option_vegan == "no":
    commande_sandwich = int(input("Combien de sandwichs à base de viande voulez-vous ? "))

    if commande_sandwich <= 0:
        print("I can't do that")
    else: 
        for i in range (commande_sandwich):
            (bread(), lettuce(), tomato(), ham(), ham(), bread())
            print()
else:
    print("I don't understand what you want")





