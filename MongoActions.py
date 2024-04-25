from pymongo import MongoClient
from pprint import pprint

class MongoActions:
    def __init__(self, uri, db_name, collName):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collName]

    def __call__(self):
        while True:
            print("\nMenú de Gestión de Restaurantes")
            print("1. Afegir un restaurant")
            print("2. Cercar un restaurant")
            print("3. Esborrar un restaurant")
            print("4. Actualitzar la puntuació d'un restaurant")
            print("5. Sortir")

            choice = input("Introdueix una opció (1-5): ")

            if choice == '1':
                self.afegir_restaurant()
            elif choice == '2':
                self.cercar_restaurant()
            elif choice == '3':
                self.esborrar_restaurant()
            elif choice == '4':
                self.actualitzar_puntuacio()
            elif choice == '5':
                print("Sortint...")
                break
            else:
                print("\nOpció invàlida, si us plau, intenta de nou.")

    def afegir_restaurant(self):
        restaurant = {
            'url': input("Introdueix URL del restaurant: ").strip(),
            'address': input("Introdueix l'adreça del restaurant: ").strip(),
            'address_line': input("Introdueix la línia adicional de l'adreça: ").strip(),
            'name': input("Introdueix el nom del restaurant: ").strip(),
            'outcode': input("Introdueix el codi exterior: ").strip(),
            'postcode': input("Introdueix el codi postal: ").strip(),
            'rating': None,  # Inicializamos el campo de valoración
            'type_of_food': None  # Inicializamos el campo de tipo de comida
        }

        # Solicitar y validar la valoración
        while True:
            rating_input = input("Introdueix la valoració del restaurant (0.0 a 10): ").strip()
            if rating_input:  # Verificar si se ha introducido algo
                try:
                    rating = float(rating_input)
                    if 0.0 <= rating <= 10:
                        restaurant['rating'] = rating
                        break
                    else:
                        print("La valoració ha de ser un número entre 0.0 i 10. Torna a intentar-ho.")
                except ValueError:
                    print("Has d'introduir un número válid. Torna a intentar-ho.")
            else:
                break

        # Solicitar el tipo de comida después de la valoración
        restaurant['type_of_food'] = input("Introdueix el tipus de menjar: ").strip()

        if any(restaurant.values()):
            self.collection.insert_one(restaurant)
            print("\nRestaurant afegit correctament.")
        else:
            print("\nNo es pot afegir el restaurant. Almenys un camp ha de tenir contingut.")




    def cercar_restaurant(self):
        query = {}
        name = input("Introdueix el nom del restaurant a cercar o deixa en blanc: ")
        if name: query['name'] = name
        
        postcode = input("Introdueix el codi postal a cercar o deixa en blanc: ")
        if postcode: query['postcode'] = postcode
        
        type_of_food = input("Introdueix el tipus de menjar a cercar o deixa en blanc: ")
        if type_of_food: query['type_of_food'] = type_of_food
        

        if query:
            results = list(self.collection.find(query))
            if results:
                for r in results:
                    print("------------------------------------------------------------------------")
                    pprint(r)
                    print("------------------------------------------------------------------------")
            else:
                print("\nNo s'han trobat restaurants.")
        else:
            print('\nTots els camps per a cercar, estan buits')
            

    def esborrar_restaurant(self):
        name = input("Introdueix el nom del restaurant a esborrar: ")
        existe = self.collection.find_one({'name': name})
        if existe:
            self.collection.delete_one({'name': name})
            print('\n Restaurant eliminat correctament')
        else:
            print('\nNo s\'ha trobat cap restaurant amb aquest nom!')

    def actualitzar_puntuacio(self):
        name = input("Introdueix el nom del restaurant a actualitzar: ").strip()
        existe = self.collection.find_one({'name': name})
        if existe:
            # Solicitar y validar la valoración
            while True:
                rating_input = input("Introdueix la valoració del restaurant (0.0 a 10): ").strip()
                if rating_input:  # Verificar si se ha introducido algo
                    try:
                        rating = float(rating_input)
                        if 0.0 <= rating <= 10:
                            self.collection.update_one({'name': name}, {'$set': {'rating': rating}})
                            print("\nValoració actualitzada correctament.")
                            break
                        else:
                            print("\nLa valoració ha de ser un número entre 0.0 i 10. Torna a intentar-ho.")
                    except ValueError:
                        print("\nHas d'introduir un número vàlid. Torna a intentar-ho.")
                else:
                    print("\nLa valoració no pot estar buida.")
        else:
            print('\nNo s\'ha trobat cap restaurant amb aquest nom!')


        