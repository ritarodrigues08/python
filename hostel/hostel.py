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


def show_rooms(rooms_list):
  for i, room in enumerate(rooms_list):
    print("[{}] {} | Tipologia {} | Casa-de-Banho {} - {}€ /noite.".format(i, room[0], room[1], room[2], room[3]))


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
    show_rooms(rooms)

  elif option == 1:
    show_rooms(rooms)
    print("")
    print("===========")
    print("Escolha o código do quarto")
    cod_room = int(input())
    print("Número de noites")
    nights = int(input())
    os.system("cls")

    print("A sua escolha: {} | Tipologia {} | Casa-de-banho {}\nValor total da estadia: {}€".format(rooms[cod_room][0], rooms[cod_room][1], rooms[cod_room][2], nights * rooms[cod_room][3]))

    print("")
    print("Pretende confirmar a sua escolha?")
    print("===========")
    print("0 - SIM | 1 - NÃO")
    confirmation = int(input())
    os.system("cls")
    if confirmation == 0:
      print("Reserva CONFIRMADA. Agradecemos a sua preferência e desejamos-lhe uma boa estadia.")
      print("===========")
      print("Quarto reservado: {}\nNúmero de noites: {}\nValor a pagar: {}".format(rooms[cod_room][0], nights, nights * rooms[cod_room][3]))
      print("===========")
      occupied.append(rooms.pop(cod_room))

  elif option == 2:
    if len(occupied) == 0:
      print("Todos os quartos estão disponíveis")
    else:
      print("Quartos reservados")
      show_rooms(occupied)
      print("")
      print("Selecione a reserva que pertende terminar")
      print("===========")
      cod_end = int(input())
      os.system("cls")
      if confirmation == 0:
        print("Reserva TERMINADA. Agradecemos a sua preferência.\nReserva terminada: {}".format(occupied[cod_end][0]))
        rooms.append(occupied.pop(cod_end))


  print("")
  print("Selecione a ação pretendida")
  print("===========")
  print("0 para CONTINUAR | 1 para SAIR")
  if int(input()) == 1:
    break



