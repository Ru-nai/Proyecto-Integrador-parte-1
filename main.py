import keyboard

continuar = True
while continuar:
    keyboard.read_key() != keyboard.KEY_UP
    print(keyboard.read_key())
    if keyboard.is_pressed(keyboard.KEY_UP):
        continuar == False
        break
