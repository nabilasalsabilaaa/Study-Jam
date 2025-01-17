import random

def GameBatuGuntingKertas():
    pilihan = ["batu", "gunting", "kertas"]
    for i in pilihan:
        print(i)
    
    nyawaUser = 3  
    nyawaCompt = 3   
    
    while nyawaUser > 0 and nyawaCompt > 0 :
        user = input("Masukkan pilihan anda: ").lower()
        compt = random.choice(["batu", "gunting", "kertas"]).lower()
        
        hasil = ""
        if (user == "batu" and compt == "gunting") or (user == "gunting" and compt == "kertas") or (user == "kertas" and compt == "batu"):
            hasil = "menang"
        elif (user == "batu" and compt == "kertas") or (user == "gunting" and compt == "batu") or (user == "kertas" and compt == "gunting"):
            hasil = "kalah"
        else:
            hasil = "seri"
        print(hasil)
        print(f"pilihan anda {user} pilihan lawan {compt}")

        if hasil == "menang":
            nyawaCompt -= 1
        elif hasil == "kalah":
            nyawaUser -= 1
        print("Nyawa kamu | Nyawa lawan")
        print(f"    {nyawaUser}      |     {nyawaCompt}")
            
    if nyawaUser == 0:
        print("Kamu kalah yhahahahhaha")
    elif nyawaCompt == 0:
        print("Kamu menang telak")
        
GameBatuGuntingKertas()