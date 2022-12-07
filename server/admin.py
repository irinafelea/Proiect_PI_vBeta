from pymongo import MongoClient
import random

client = MongoClient("mongodb://localhost:27017")
db = client["proiect"]
coll_user = db["utilizator"]
coll_ong = db["ong"]

admin = 1
while admin:
    print("1.Logare\n2.Iesire")

    optiune = 0
    while int(optiune) < 1 or int(optiune) > 2:
        print("Selecteaza optiunea: ")
        optiune = int(input())

    if optiune == 1:
        print("--- LOGARE ---\n")

        log = 1

        email = input("E-mail: ", )
        parola = input("Parola: ", )

        result_email = coll_user.find_one({'e-mail': email})
        result_pass = coll_user.find_one({'password': parola})

        if result_email is None:
            print("E-mail inexistent\n")
            log = 0
        else:
            if result_pass is None:
                print("Parola gresita\n")
                log = 0
            else:
                for x in coll_user.find():
                    if x['e-mail'] == email:
                        if x["isAdmin"] is not True:
                            print("Nu esti admin!\n")
                            log = 0

        if log == 1:
            print("Te-ai logat cu succes!\n")

        while log:
            print("1.Adauga un admin\n2.Actualizeaza lista de nevoi\n3.Iesire")

            opt_admin = 0
            while int(opt_admin) < 1 or int(opt_admin) > 3:
                print("Selecteaza optiunea: ")
                opt_admin = int(input())

            if opt_admin == 1:
                print("--- ADAUGA ADMIN NOU ---\n")

                id = random.randint(1000, 9999)
                while coll_user.find_one({'id': id}) is not None:
                    id = random.randint(1000, 9999)

                nume = input("Nume: ", )
                prenume = input("Prenume: ", )
                email_nou = input("Email: ", )
                while coll_user.find_one({'e-mail': email_nou}) is not None:
                    print("Acest admin exista deja!")
                    email_nou = input("Email: ", )
                parola_noua = input("Parola: ", )

                coll_user.insert_one({"id": id, "firstName": nume, "lastName": prenume, "e-mail": email_nou, "password": parola_noua, "isAdmin": True})

            if opt_admin == 2:
                print("--- ACTUALIZEAZA LISTA DE NEVOI ---\n")

                denumire = input("Scrie denumirea ONG-ului: ", )

                result_denumire = coll_ong.find_one({'Denumire': denumire})

                for x in coll_ong.find():
                    if x['Denumire'] == str(denumire):
                        nevoi = x['lista de nevoi']

                        nev = 1
                        while nev:
                            print("1.Adauga o nevoie \n2.Sterge o nevoie \n3.Iesire")
                            opt_nevoi = 0
                            while int(opt_nevoi) < 1 or int(opt_nevoi) > 3:
                                print("Selecteaza optiunea: ")
                                opt_nevoi = int(input())

                            if opt_nevoi == 1:
                                nevoi_noi = input("Introduceti o nevoie noua: ", )
                                nevoi.append(str(nevoi_noi))
                                coll_ong.update_one({"Denumire": denumire}, {"$set": {"lista de nevoi": nevoi}})

                            if opt_nevoi == 2:
                                print(nevoi)
                                sterge = input("Introduceti o nevoie pe care doriti sa o stergeti: ", )
                                nevoi.remove(str(sterge))
                                coll_ong.update_one({"Denumire": denumire}, {"$set": {"lista de nevoi": nevoi}})

                            if opt_nevoi == 3:
                                nev = 0

            if opt_admin == 3:
                log = 0

    if optiune == 2:
        admin = 0
