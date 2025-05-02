
with open("foobar.txt", "r") as file1, open("foobar.txt", "r") as file2:
    c1 = file1.read(1)
    c2 = file2.read(1)

    # Imprime el caracter leido de file1 y file2 por separado
    print(f"c1={c1} c2 = {c2}")



