# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# не (Х или Y или Z) = не X или не Y или не Z


for X in range(0, 2):
    for Y in range(0, 2):
        for Z in range(0, 2):
            if not (X or Y or Z) == (not X) or (not Y) or (not Z):
                print(True) 