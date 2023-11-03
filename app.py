from modules.biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input
                       ("1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - peržiūrėti įrašus\n4 - balansas\n0 - išeiti iš programos\n"))
    match pasirinkimas:
        case 1:
            biudzetas.prideti_pajamas()
        case 2:
            biudzetas.prideti_islaidas()
        case 3:
            biudzetas.parodyti_ataskaita()
        case 4:
            print(biudzetas.gauti_balansa())
        case 0:
            print("Viso gero")
            break
        case _:
            print("Įrašėte netinkamą pasirinkimą")
