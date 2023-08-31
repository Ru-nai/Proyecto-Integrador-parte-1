
import curses

jugador_nick = input() #Solicita el nombre del jugador

print(f'¡Bienvenido, {jugador_nick}!') #Imprime mensaje de bienvenida + el nickname


arrow_key = curses.initscr().getch()
if arrow_key == curses.KEY_UP:
  print("Up")
elif arrow_key == curses.KEY_DOWN:
  print("Down")
elif arrow_key == curses.KEY_RIGHT:
  print("Right")
elif arrow_key == curses.KEY_LEFT:
  print("Left")
else:
  print("Not an arrow key")