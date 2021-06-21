class Ceny:
    def ceny(self,tablica):
        pomoc = [['Clay'], ['Gravel'], ['Limestone'],['Coal'],['Iron ore'],['Crude oil'],['Quartz sand'],['Chalcopyrite'],['Bauxite'],['Lithium ore'],['Ilmenite'],['Silver ore'],['Gold ore'],['Rough diamonds'],['Bricks'],['Concrete'],['Steel'],['Fossil fuel'],['Copper'],['Aluminium'],['Plastics'],['Lithium'],['Batteries'],['Silicon'],['Electronics'],['Titanium'],['Silver'],['Gold'],['Glass'],['Weapons'],['Medical technology'],['Jewellery'],['Scan drones']]
        Clay=[]
        Gravel=[]
        Limestone=[]
        Coal=[]
        Iron_ore=[]
        Crude_oil=[]
        Quartz_sand=[]
        Chalcopyrite=[]
        Bauxite=[]
        Lithium_ore=[]
        Ilmenite=[]
        Silver_ore=[]
        Gold_ore=[]
        Rough_diamonds=[]
#========================================================
        Bricks=[]
        Concrete=[]
        Steel=[]
        Fossil_fuel=[]
        Copper=[]
        Aluminium=[]
        Plastics=[]
        Lithium=[]
        Batteries=[]
        Silicon=[]
        Electronics=[]
        Titanium=[]
        Silver=[]
        Gold=[]

        Glass=[]
        Weapons=[]
        Medical_technology=[]
        Jewellery=[]
        Scan_drones=[]

        tablice = [Clay, Gravel, Limestone, Coal, Iron_ore, Crude_oil, Quartz_sand, Chalcopyrite,Bauxite,Lithium_ore,Ilmenite,Silver_ore,Gold_ore,Rough_diamonds,
Bricks,Concrete,Steel,Fossil_fuel,Copper,Aluminium,Plastics,Lithium,Batteries,Silicon,Electronics,Titanium,Silver,Gold,Glass,Weapons,Medical_technology,Jewellery,Scan_drones]

        for t in range(len(pomoc)):
           for i in range(len(tablica)):
               if tablica[i] == pomoc[t][0]:
                   if tablica[i+2] == '0':
                       tablice[t].append(int(tablica[i + 1]))
                   else:
                       tablice[t].append(int(tablica[i + 2]))
        return tablice
#========================================================================================================================






