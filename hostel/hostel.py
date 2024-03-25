import os

rooms = [
        ("Quarto 00", "INDIVIDUAL", "PRIVATIVA", 25),
        ("Quarto 01", "INDIVIDUAL", "PRIVATIVA", 25),
        ("Quarto 02", "ATÉ 2 PAX", "PRIVATIVA", 35),
        ("Quarto 03", "ATÉ 2 PAX", "PRIVATIVA", 35),
        ("Quarto 04", "ATÉ 5 PAX", "PRIVATIVA", 60),
        ("Quarto 05", "ATÉ 5 PAX", "PRIVATIVA", 60)
        ]

occupied = []


def show_available_rooms(rooms_list):
  for i, room in enumerate(rooms_list):
    print("[{}] {} | Tipologia {} | Casa-de-Banho {} - {}€ /noite.".format(i, room[0], room[1], room[2], room[3]))

show_available_rooms(rooms)

while True:
  os.system("cls")
  print("===============================")
  print("BEM-VINDO AO NOSSO HOSTEL!")
  print("===============================")
  print("")
  print("Selecione a ação pretendida")
  print("===========")
  print("0 - Mostrar quartos disponíveis | 1 - Alugar um quarto | 2 - Terminar estadia")
  option = int(input())

  os.system("cls")
  if option == 0:
    pass

  elif option == 1:
    pass

  elif option == 2:
    pass


  print("Selecione a ação pretendida")
  print("===========")
  print("0 para CONTINUAR | 1 para SAIR")
  if int(input()) == 1:
    break



