while True:
        respuesta = input("¿Responde a Estímulos? (si/no): ").strip().lower()
        if respuesta == "si":
            print("Valorar la necesidad de llevarlo al hospital más cercano")
            break
        else:
            print("Abrir la vía Aérea")
            respuesta = input("¿Respira? (si/no): ").strip().lower()
            if respuesta == "si":
                print("Permitir posición de suficiente ventilación")
                break
            else:
                print("Administrar 5 Ventilaciones y llamar a Ambulancia")
                respuesta = input("¿Signos de Vida? (si/no): ").strip().lower()
                if respuesta == "si":
                    while True:
                        respuesta = input("¿Llegó la Ambulancia? (si/no): ").strip().lower()
                        if respuesta == "si":
                            break
                        else:
                            print("Reevaluar a la espera de la Ambulancia")
                else:
                    while True:
                        respuesta = input("¿Llegó la Ambulancia? (si/no): ").strip().lower()
                        if respuesta == "si":
                            break
                        else:
                            print("Administrar Compresiones Torácicas hasta que llegue ambulancia")