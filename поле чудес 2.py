import random

byk = ["политика", "качество", "время", "словарь", "мебель", "аннотация", "композиция"]
word = random.choice(byk)
a = ["*"] * len(word)
score1 = 0
score2 = 0
count1 = 3
count2 = 3
player = 1
print("Добро пожаловать в игру 'Поле чудес'!")
print("Слово:", " ".join(a))

while "*" in a and (count1 > 0 or count2 > 0):

    if (player == 1 and count1 <= 0) or (player == 2 and count2 <= 0):
        player = 2 if player == 1 else 1
        continue
    
    print(f'\nИгрок {player}:')
    print("Слово:", " ".join(a))
    print(f'Очки: игрок 1 - {score1}, игрок 2 - {score2}')
    print(f'Попытки: игрок 1 - {count1}, игрок 2 - {count2}')
    
    c = input("Слово или буква? ").lower()
    
    if len(c) == 1:  # Буква
        if c in word and c not in a:
            print(f'Есть буква "{c}"!')
            count = word.count(c)
            for i in range(len(word)):
                if word[i] == c:
                    a[i] = c
            
            if player == 1:
                score1 += count * 100
            else:
                score2 += count * 100
        else:
            print("Такой буквы нет или она уже была")
            if player == 1:
                count1 -= 1
            else:
                count2 -= 1
            

            player = 2 if player == 1 else 1
    else:  # Слово целиком
        if c == word:
            print(f"Игрок {player} угадал слово!")
            if player == 1:
                score1 += 1000
            else:
                score2 += 1000
            a = list(word)
            break
        else:
            print("Не угадал!")
            if player == 1:
                count1 -= 1
            else:
                count2 -= 1
           
            player = 2 if player == 1 else 1

print(f"\nСлово было: {word}")
print(f"Итог: Игрок 1 = {score1}, Игрок 2 = {score2}")

if score1 > score2:
    print("Победил Игрок 1!")
elif score2 > score1:
    print("Победил Игрок 2!")
else:
    print("Ничья!")