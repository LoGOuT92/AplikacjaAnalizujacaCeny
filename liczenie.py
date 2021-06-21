import fabryki as f
class liczenie:
    def ceny(self,wartosc):
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

        Cegielnia = []#0
        Cegielnia.append(f.Fabryki.fabryka1(0, Clay[0], Bricks[0], 1200, 800, 150, 4000))

        Cementowania = []#1
        Cementowania.append(f.Fabryki.fabryka2(0, Gravel[0], Limestone[0], Concrete[0], 450, 300, 2100, 70, 3000))

        Huta = []#2
        Huta.append(f.Fabryki.fabryka2(0, Coal[0], Iron_ore[0], Steel[0], 4500, 3150, 450, 9, 157500))

        Rafineria = []#3
        Rafineria.append(f.Fabryki.fabryka1(0, Crude_oil[0], Fossil_fuel[0], 640, 640, 26, 24000))

        HutaMiedzi = []#4
        HutaMiedzi.append(f.Fabryki.fabryka1(0, Chalcopyrite[0], Copper[0], 810, 270, 19, 225000))

        FabrykaAluminium = []#5
        FabrykaAluminium.append(f.Fabryki.fabryka1(0, Bauxite[0], Aluminium[0], 1920, 320, 17, 400000))

        FabrykaTworzywSztucznych = []#6
        FabrykaTworzywSztucznych.append(f.Fabryki.fabryka1(0, Crude_oil[0], Plastics[0], 180, 1800, 5, 72000))

        HutaLitu = []#7
        HutaLitu.append(f.Fabryki.fabryka1(0, Lithium_ore[0], Lithium[0], 17250, 750, 7, 750000))

        FabrykaBaterii = []#8
        FabrykaBaterii.append(
            f.Fabryki.fabryka3(0, Aluminium[0], Plastics[0], Lithium[0], Batteries[0], 600, 2400, 1200, 600, 2,
                               4500000))

        WytworniaKrzemu = []#9
        WytworniaKrzemu.append(
            f.Fabryki.fabryka3(0, Clay[0], Fossil_fuel[0], Quartz_sand[0], Silicon[0], 60, 300, 1200, 120, 6, 2970000))

        FabrykaElektroniki = []#10
        FabrykaElektroniki.append(
            f.Fabryki.fabryka3(0, Copper[0], Plastics[0], Silicon[0], Electronics[0], 180, 240, 60, 480, 12, 300000))

        HutaTytanu = []#11
        HutaTytanu.append(f.Fabryki.fabryka1(0, Ilmenite[0], Titanium[0], 640, 320, 6, 800000))

        HutaSrebra = []#12
        HutaSrebra.append(f.Fabryki.fabryka1(0, Silver_ore[0], Silver[0], 480, 3000, 1, 600000))

        HutaZlota = []#13
        HutaZlota.append(f.Fabryki.fabryka1(0, Gold_ore[0], Gold[0], 1600, 240, 1, 1600000))

        HutaSzkla = []#14
        HutaSzkla.append(
            f.Fabryki.fabryka3(0, Limestone[0], Fossil_fuel[0], Quartz_sand[0], Glass[0], 320, 640, 480, 640, 23,
                               240000))

        ZakladZbroieniowy = []#15
        ZakladZbroieniowy.append(
            f.Fabryki.fabryka3(0, Steel[0], Aluminium[0], Batteries[0], Weapons[0], 5, 5, 5, 125, 8, 1250000))

        FabrykaUrzadzenMedycznych = []#16
        FabrykaUrzadzenMedycznych.append(
            f.Fabryki.fabryka3(0, Titanium[0], Plastics[0], Electronics[0], Medical_technology[0], 160, 80, 80, 400, 11,
                               3600000))

        Zlotnik = []#17
        Zlotnik.append(
            f.Fabryki.fabryka3(0, Silver[0], Gold[0], Rough_diamonds[0], Jewellery[0], 50, 50, 50000, 100, 3, 2500000))

        WytworniaDronow = []#18
        WytworniaDronow.append(
            f.Fabryki.fabryka3(0, Titanium[0], Electronics[0], Batteries[0], Scan_drones[0], 50, 25, 250, 1, 1,
                               25000000))
        return Cegielnia,Cementowania,Huta,Rafineria,HutaMiedzi,FabrykaAluminium,FabrykaTworzywSztucznych,HutaLitu,FabrykaBaterii,WytworniaKrzemu,FabrykaElektroniki,HutaTytanu,HutaSrebra,HutaZlota,HutaSzkla,ZakladZbroieniowy,FabrykaUrzadzenMedycznych,Zlotnik,WytworniaDronow
