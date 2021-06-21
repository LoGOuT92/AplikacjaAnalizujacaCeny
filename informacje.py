import profit
class Informacje:
    def info(self,tablica,wartosc):

        Clay = []
        Gravel = []
        Limestone = []
        Coal = []
        Iron_ore = []
        Crude_oil = []
        Quartz_sand = []
        Chalcopyrite = []
        Bauxite = []
        Lithium_ore = []
        Ilmenite = []
        Silver_ore = []
        Gold_ore = []
        Rough_diamonds = []
        # ========================================================
        Bricks = []
        Concrete = []
        Steel = []
        Fossil_fuel = []
        Copper = []
        Aluminium = []
        Plastics = []
        Lithium = []
        Batteries = []
        Silicon = []
        Electronics = []
        Titanium = []
        Silver = []
        Gold = []
        # =============================================
        Glass = []
        Weapons = []
        Medical_technology = []
        Jewellery = []
        Scan_drones = []
        tablice = [Clay, Gravel, Limestone, Coal, Iron_ore, Crude_oil, Quartz_sand, Chalcopyrite, Bauxite, Lithium_ore,
                   Ilmenite, Silver_ore, Gold_ore, Rough_diamonds,
                   Bricks, Concrete, Steel, Fossil_fuel, Copper, Aluminium, Plastics, Lithium, Batteries, Silicon,
                   Electronics, Titanium, Silver, Gold, Glass, Weapons, Medical_technology, Jewellery, Scan_drones]
        for i in range(len(wartosc)):
            tablice[i].append(wartosc[i][0])


        pobor_gliny=tablica[0][0][1]+tablica[9][0][1]
        cena_glina=pobor_gliny*Clay[0]

        pobor_zwiru=tablica[1][0][1]
        cena_zwiru=pobor_zwiru*Gravel[0]

        pobor_wapna=tablica[1][0][2]+tablica[14][0][1]
        cena_wapna=pobor_wapna*Limestone[0]

        pobor_wegla=tablica[2][0][1]
        cena_wegla=pobor_wegla*Coal[0]

        pobor_ironOre=tablica[2][0][2]
        cena_ironOre=pobor_ironOre*Iron_ore[0]

        pobor_ropy=tablica[3][0][1]+tablica[6][0][1]
        cena_ropy=pobor_ropy*Crude_oil[0]

        pobor_piasku=tablica[14][0][3]+tablica[9][0][3]
        cena_piasku=pobor_piasku*Quartz_sand[0]

        pobor_chalkopirytu=tablica[4][0][1]
        cena_chalkopirytu=pobor_chalkopirytu*Chalcopyrite[0]

        pobor_boxytu=tablica[5][0][1]
        cena_boxytu=pobor_boxytu*Bauxite[0]

        pobor_rudyLitu=tablica[7][0][1]
        cena_rudyLitu=pobor_rudyLitu*Lithium_ore[0]

        pobor_rudyTytanu=tablica[11][0][1]
        cena_rudyTytanu=pobor_rudyTytanu*Ilmenite[0]

        pobor_rudySrebra=tablica[12][0][1]
        cena_rudySrebra=pobor_rudySrebra*Silver_ore[0]

        pobor_rudyZloa=tablica[13][0][1]
        cena_rudyZlota=pobor_rudyZloa*Gold_ore[0]

        pobor_diamentow=tablica[17][0][3]
        cena_diamentow=pobor_diamentow*Rough_diamonds[0]

        print("pobor Gliny wynosi:",pobor_gliny,"placisz za to:",cena_glina)
        print("pobor Zwiru wynosi:",pobor_zwiru,"placisz za to:",cena_zwiru)
        print("pobor wapna wynosi:",pobor_wapna,"placisz za to:",cena_wapna)
        print("pobor wegla wynosi:",pobor_wegla,"placisz za to:",cena_wegla)
        print("pobor rudyRzelaza wynosi:",pobor_ironOre,"placisz za to:",cena_ironOre)
        print("pobor ropy wynosi:",pobor_ropy,"placisz za to:",cena_ropy)
        print("pobor piasku wynosi:",pobor_piasku,"placisz za to:",cena_piasku)
        print("pobor chalkopirytu  wynosi:",pobor_chalkopirytu,"placisz za to:",cena_chalkopirytu)
        print("pobor boxytu  wynosi:",pobor_boxytu,"placisz za to:",cena_boxytu)
        print("pobor rudy litu  wynosi:",pobor_rudyLitu,"placisz za to:",cena_rudyLitu)
        print("pobor rudy tytanu  wynosi:",pobor_rudyTytanu,"placisz za to:",cena_rudyTytanu)
        print("pobor rudy srebra  wynosi:",pobor_rudySrebra,"placisz za to:",cena_rudySrebra)
        print("pobor rudy zlota  wynosi:",pobor_rudyZloa,"placisz za to:",cena_rudyZlota)
        print("pobor diamentow  wynosi:",pobor_diamentow,"placisz za to:",cena_diamentow)

        pobor_stali=tablica[15][0][1]
        produkcja_stalii=tablica[2][0][3]
        suma_stalii=produkcja_stalii-pobor_stali
        cena_stalii=suma_stalii*Steel[0]

        pobor_paliwa=tablica[14][0][2]+tablica[9][0][2]
        produkcja_paliwa=tablica[3][0][2]
        suma_paliiwa=produkcja_paliwa-produkcja_paliwa
        cena_paliwa=suma_paliiwa*Fossil_fuel[0]

        pobor_miedzi=tablica[10][0][1]
        produkcja_miedzi=tablica[4][0][2]
        suma_miedzi=produkcja_miedzi-pobor_miedzi
        cena_miedzi=suma_miedzi*Copper[0]

        pobor_aluminium=tablica[8][0][1]+tablica[15][0][2]
        producja_aluminium=tablica[5][0][2]
        suma_aluminium=producja_aluminium-pobor_aluminium
        cena_aluminium=suma_aluminium*Aluminium[0]

        pobor_plastiku=tablica[8][0][2]+tablica[10][0][2]+tablica[16][0][2]
        produkcja_plastiku=tablica[6][0][2]
        suma_plastiku=produkcja_plastiku-pobor_plastiku
        cena_plastiku=suma_plastiku*Plastics[0]

        pobor_litu=tablica[8][0][3]
        produkcja_litu=tablica[7][0][2]
        suma_litu=produkcja_litu-pobor_litu
        cena_litu=suma_litu*Lithium[0]

        pobor_baterii=tablica[15][0][3]+tablica[18][0][3]
        produkcja_baterii=tablica[8][0][4]
        suma_baterii=produkcja_baterii-pobor_baterii
        cena_baterii=suma_baterii*Batteries[0]

        pobor_krzem=tablica[10][0][3]
        produkcja_krzem=tablica[9][0][4]
        suma_krzem=produkcja_krzem-pobor_krzem
        cena_krzem=suma_krzem*Silicon[0]

        pobor_elektronika=tablica[16][0][3]+tablica[18][0][2]
        produkcja_elektronika=tablica[10][0][4]
        suma_elektronika=produkcja_elektronika-pobor_elektronika
        cena_elektroniki=suma_elektronika*Electronics[0]

        pobor_tytan=tablica[16][0][1]+tablica[18][0][1]
        produkcja_tytan=tablica[11][0][2]
        suma_tytan=produkcja_tytan-pobor_tytan
        cena_tytan=suma_tytan*Titanium[0]

        pobor_srebro=tablica[17][0][1]
        produkcja_srebro=tablica[12][0][2]
        suma_srebro=produkcja_srebro-pobor_srebro
        cena_srebra=suma_srebro*Silver[0]

        pobor_zloto=tablica[17][0][2]
        produkcja_zloto=tablica[13][0][2]
        suma_zloto=produkcja_zloto-pobor_zloto
        cena_zloto=suma_zloto*Gold[0]

        produkcja_cegly=tablica[0][0][2]
        cena_cegly=produkcja_cegly*Bricks[0]
        produkcja_beton=tablica[1][0][3]
        cena_beton=produkcja_beton*Concrete[0]
        produkcja_szklo=tablica[14][0][4]
        cena_szklo=produkcja_szklo*Glass[0]
        produkcja_bron=tablica[15][0][4]
        cena_bron=produkcja_bron*Weapons[0]
        produkcja_medyczne=tablica[16][0][4]
        cena_medyczne=produkcja_medyczne*Medical_technology[0]
        produkcja_bizuteria=tablica[17][0][4]
        cena_bizuteria=produkcja_bizuteria*Jewellery[0]
        produkcja_dron=tablica[18][0][4]
        cena_dron=produkcja_dron*Scan_drones[0]

        print()
        print("pobor stali wynosi:",pobor_stali,"produkcja stali wynosi:",produkcja_stalii,"laczna produkcja:",suma_stalii,"profit=",cena_stalii)
        print("pobor paliwa wynosi:",pobor_paliwa,"produkcja paliwia wynosi:",produkcja_paliwa,"laczna produkcja",suma_paliiwa,"profit=",cena_paliwa)
        print("pobor miedzi wynosi:",pobor_miedzi,"produkcja miedzi wynosi:",produkcja_miedzi,"laczna produkcja:",suma_miedzi,"profit:",cena_miedzi)
        print("pobor aluminium wynosi:",pobor_aluminium,"produkcja aluminium",producja_aluminium,"laczna produkcja:",suma_aluminium,"profit:",cena_aluminium)
        print("pobor plastiku wynosi:", pobor_plastiku, "produkcja plastiku", produkcja_plastiku, "laczna produkcja:",suma_plastiku, "profit:",cena_plastiku)
        print("pobor litu wynosi:",pobor_litu,"produkcja litu",produkcja_litu,"laczna produkcja:",suma_litu,"profit:",suma_litu*Lithium[0])
        print("pobor baterii wynosi:",pobor_baterii,"produkcja baterii",produkcja_baterii,"laczna produkcja:",suma_baterii,"profit:",cena_baterii)
        print("pobor krzemu wynosi:",pobor_krzem,"produkcja krzemu",produkcja_krzem,"laczna produkcja:",suma_krzem,"profit:",cena_krzem)
        print("pobor elektroniki wynosi:",pobor_elektronika,"produkcja elektroniki",produkcja_elektronika,"laczna produkcja:",suma_elektronika,"profit:",cena_elektroniki)
        print("pobor tytanu wynosi:",pobor_tytan,"produkcja tytanu",produkcja_tytan,"laczna produkcja:",suma_tytan,"profit:",cena_tytan)
        print("pobor srebra wynosi:",pobor_srebro,"produkcja srebra",produkcja_srebro,"laczna produkcja:",suma_srebro,"profit:",cena_srebra)
        print("pobor zlota wynosi:",pobor_zloto,"produkcja zlota",produkcja_zloto,"laczna produkcja:",suma_zloto,"profit:",cena_zloto)
        print()
        print("produkcja cegiel",produkcja_cegly,"profit:",cena_cegly)
        print("produkcja betonu",produkcja_beton,"profit:",cena_beton)
        print("produkcja szkla",produkcja_szklo,"profit:",cena_szklo)
        print("produkcja bronii",produkcja_bron,"profit:",cena_bron)
        print("produkcja medycznych",produkcja_medyczne,"profit:",cena_medyczne)
        print("produkcja bizuterii",produkcja_bizuteria,"profit:",cena_bizuteria)
        print("produkcja drownow",produkcja_dron,"profit:",cena_dron)

        debet=cena_glina+cena_zwiru+cena_wapna+cena_wegla+cena_ironOre+cena_ropy+cena_piasku+cena_chalkopirytu+cena_boxytu+cena_rudyLitu+cena_rudyTytanu
        profit=cena_stalii+cena_paliwa+cena_miedzi+cena_aluminium+cena_plastiku+cena_litu+cena_baterii+cena_krzem+cena_elektroniki+cena_tytan+cena_cegly+cena_beton+cena_szklo+cena_bron+cena_medyczne+cena_dron
        print("SUMA=",profit-debet)
        print(debet,profit)

