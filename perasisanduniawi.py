#Tipe data
#Boolean

# A = True
# B = False
# print(type(A and B))

# String
# a = 10
C = "INI STRING"
D = 'rrrrrrrr10 ini angka JUGA   '
# print(type(a))
# print(type(C and D))
# print(C)

# Fungsi String
# C = C.lower()
# D = D.capitalize()
# print(C)
# print(D)

# print(len(C))
# print(len(D))

# D = D.strip()
# print(D)

# C = C.replace("INI", "itu")
# print(C)

# D = D.replace('juga','termasuk')
# print(D)

# D = D.replace('JUGA','TERMASUK')
# print(D)

# print(C)
# split1 = C.split()
# split2 = C.split('i')
# split3 = C.split('i', 1)
# print(split1)
# print(split2)
# print(split3)


# # Integer
# x = 5
# y = 100000
# print(type(x and y))


# # Float 
# X = 2.0
# Y = 80.59
# print(type(X and Y))


# # Complex
# E = 8j 
# F = 8j + 3
# print(type(E and F ))

# a = (-1)**0.5
# print(a)


# List Data
listA=["a","b","c"]
listB=[1,"Apel",50.6,True]
# print(type(listA))
# print(listA,listB)

# #Fungsi List
# print (listA[2])
# print (listB[0:2])

# listB.append('Pisang')
# print(listB)

# listB.insert(1,"Nanas")
# print(listB)

# listA.extend(listB)
# print(listA)
# print(listB)

# listA.remove("a")
# print(listA)

# listB.pop(2)
# print(listB)

# del listB[0]
# print(listB)

# listB.clear()
# print(listB)

# Tuple Data
# tupleA=("a","b","c")
# tupleB=(1,3.2,"4")
# print(tupleA,tupleB)
# print(type(tupleA))

# #Set Data
# setA={"ini","Pakai","Set","Coba","print","hasilnya"}
# print(type(setA))
# print(setA)

#DIctionary Data
# dictA={"Ini adalah key":"Dan ini value","Mobil":"Avanza"}
# # print(type(dictA))
# # print(dictA)

# # Fungsi Dictionary
# mobil={"Mitsubishi":"Pajero","Suzuki":"Ertiga","Honda":"Civic"}
# # mengakses value dictionary
# print(mobil["Mitsubishi"])
# #mengupdate value dictionary
# mobil["Mitsubishi"]= "Xpander"
# print(mobil["Mitsubishi"])
# #Menghapus item dictionary terakhir
# mobil.popitem()
# print(mobil)
# # #menghapus item berdasarkan keys
# del mobil["Suzuki"]
# print(mobil)
# # #menambahkan item dictionary
# mobil["Ford"]="Mustang"
# print (mobil)
# #mendapatkan list keys semua dictionary
# print(mobil.keys())
# #mendapatkan list values semua dictionary
# print(mobil.values())
# # #mendapatkan list keys dan values dictionary
# print(mobil.items())
# mendapatkan data keys dan values dictionary
# for itemkeys, itemvalues in mobil.items():
#     print (itemkeys,":",itemvalues)


#     KONVERSI DATA
# string to integer or Float
# variabelA="5"
# print(type(variabelA))
# variabelB=int(variabelA)
# print(type(variabelB))
# print(type(int(variabelA)))
# variabelC=float(variabelA)
# print(variabelC)
# print(type(variabelC))
# #integer or float to string
# variabel1=50000
# variabel2=str(variabel1)
# print(variabel2)
# print(type(variabel2))

#Variabel Global dan Lokal



# def lokal():
#     a = 8
#     print(a)
# print(a)
# lokal()



#     OPERATOR MATEMATIKA
# Variabel awal
varA=10
varB=20
# #Penjumlahan
# hasil=varA + varB
# print(hasil)
# #pengurangan
# hasil=varA-varB
# print(hasil)
# #perkalian
# hasil=varA*varB
# print(hasil)
# #pembagian
# hasil=varA/varB
# print(hasil)
# #Modulus
# hasil=varA%varB
# print(hasil)
# #perpangkatan
# hasil=varA**2
# # print(hasil)

    #OPERATOR PENYERAHAN
# varA+=5
# print(varA)
# varA = varA + 5
# print(varA)

#     #OPERATOR IDENTITAS
# varC=10
# varD=12
# print(varD is varC)
# print(varC is not varD)

#     #OPERATOR MEMBERSHIP
# listAsisten=["Reza","Try","Addis","Arief"]
# nama = "Rahmat"
# print("Rahmat" in listAsisten)
# print("Rahmat" not in listAsisten)

    # STRUKTUR KONTROL SEDERHANA
# nilai = 70
# if nilai > 90 :
#     print("Lulus")
# print("Terimakasih")

    # STRUKTUR KONTROL BERTINGKAT (IF ELSE)
# nilai = 90
# if nilai > 70:
#     print("Lulus")
# else:
#     print("Gagal")

    # STRUKTUR KONTROL BERTINGKAT (IF ELIF ELSE)
# nilai = 100
# if nilai<100 and nilai>90:
#     print("Nilai Anda A")
# elif nilai<90 and nilai>80:
#     print("Nilai Anda B+")
# elif nilai<=80 and nilai>70:
#     print("Nilai anda B") 
# elif nilai>=100 or nilai<0:
#     print("Nilai Tidak Valid")
# else:
#     print("Nilai belum memenuhi")

#     STRUKTUR  PENGULANGAN FOR
# dengan parameter range
# satusampespeuluh = []

# for i in range(2,10+1):
#     print(i)

# print(*satusampespeuluh)


#dengan parameter list
# fruits = ["Apel","Pisang","Durian","Kentang"]
# for i in fruits:
#     print(i)

    #STRUKTUR PENGULANGAN WHILE
# index=1
# # while index<=10:
# #     print("Selamat Belajar")
# #     index+=1

# while index <=20:
#     if index == 15:
#         index+=1
#         continue
#     if index == 17:
#         break
#     if index == 20:
#         pass
#     print("Ini adalah index ke",index)
#     index+=1

def penjumlahan(a,b):
    c = a+b
    return c

penjumlahan(4,6)
