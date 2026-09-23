import time
import keyboard as keyb

spawned = False

boss = {
    "hp": 200,
    "speed": 30,
    "Damage": 20
}

Player = {
    "hp": 100,
    "speed": 20,
    "Damage": 5,
    "Inventory": []
}

Answer_question = ["Nope", "No", "Idi Nahui"]

question = input("Type <<Spawn Boss to Spawn Boss>>: ")
if question in Answer_question:
    print("You are not ready yet...")


def spawn_boss():
    if question == "Spawn Boss":
        global spawned
        timer = 3  # Сделали 3 секунды вместо 10 для скорости
        while timer > 0:
            print(f"\rBoss spawns in: {timer}...", end="", flush=True)
            time.sleep(0.5)
            timer -= 1
        print("\rBoss Has been spawned!        ")
        time.sleep(0.5)
        print("The fight Begins!!!")
        spawned = True


def attack():
    if spawned:
        print("\nPress [F] or [H] to attack!")

        # 1. Считывание клавиши И урон должны быть ВНУТРИ цикла
        while boss["hp"] > 0 and Player["hp"] > 0:
            event = keyb.read_event(suppress=True)

            if event.event_type == keyb.KEY_DOWN and event.name in ["f", "h"]:
                Player["hp"] -= boss["Damage"]
                boss["hp"] -= Player["Damage"]

                current_boss_hp = max(0, boss["hp"])
                current_player_hp = max(0, Player["hp"])

                print(f"Boss HP: {current_boss_hp} | Your HP: {current_player_hp}")

        # 2. Итог боя проверяется строго ПОСЛЕ окончания цикла (убран отступ)
        if boss["hp"] <= 0:
            print("\nXD Boss is defeated! | You just got Boss_Sword")
            Player["Inventory"].append("Boss_Sword")
            print(f"Inventory: {Player['Inventory']}")
        elif Player["hp"] <= 0:
            print("\nYOU DIED! The boss beat you...")


spawn_boss()
attack()
