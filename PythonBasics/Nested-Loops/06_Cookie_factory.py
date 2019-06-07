n = int(input())

for batch in range(1, n + 1):
    flour = False
    sugar = False
    eggs = False

    while True:
        products = input()

        if products == "Bake!":
            if eggs and flour and sugar:
                print(f"Baking batch number {batch}...")
                break
            else:
                print("The batter should contain flour, eggs and sugar!")

        if products == "flour":
            flour = True
        elif products == "sugar":
            sugar = True
        elif products == "eggs":
            eggs = True
