# write a program to print multiplication table of a given humber using for loop
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")

# Write a program to greet all the person names storeg in a list ' and which starts with S.
l = ["Bunny", "Syed", "Saif", "Rafiiq"]

for name in l:
    if(name.startswith("S")):
        print(f"Assalam waleikum {name}")
                        
