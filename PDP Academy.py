# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 21:51:07 2023
PDP academiy misollari --
@author: Ergashov Sherzod
"""
# # 1-masala
# bir = int(input('1-son '))
# ikki = int(input('2-son '))
# uch = int(input('3-son '))
# arifmetik = (bir+ikki+uch)/3
# print('3 ta sonning o\'rta arifmetigi', arifmetik)

# # 2-masala   kvadratning peremetirini topish
# tomon = float(input('a = '))
# p = 4*tomon
# print('Kvadratning Peremetiri ', p)

# # 3-masala   To’g’ri to’rtburchakning tomonlari a va b berilgan. Uning yuzasi S = a*b orqali va P=2*(a+b) orqali aniqlansin.
# tomon1 = float(input('a = '))
# tomon2 = float(input('a = '))
# s = tomon1*tomon2
# p = 2*(tomon1+tomon2)
# print(f"Yuzasi {s},  Peremetri {p} ga teng")

# # 4-masala   Kubning yon tomoni a berilgan. Uning hajmini V=a*a*a va to’la sirti S=6*a*a aniqlansin.
# tomon = float(input('a = '))
# V = tomon**3
# St = (tomon**2)*6
# print(f"Hajm {V},  To'la sirti {St}")

# # 5-masala   A, B va C sonlar berilgan. A ni qiymati B ga, B ni qiymati C ga va C ni
# # qiymati A ga almashtirilsin. A, B va C ning yangi qiymati ekranga
# # chiqarilsin.
# tomon1 = float(input('a = '))
# tomon2 = float(input('b = '))
# tomon3 = float(input('c = '))
# print(f"a = {tomon2}, b = {tomon3}, c = {tomon1}")

# # 6-masala  . Foydalanuvchi tomonidan kiritilgan sonning kvadratini ekranga chiqaruvchi dastur tuzing.
# son = int(input('a = '))
# kvadrat = son**2
# print(f"{son} ning kvadrati {kvadrat}")

# # 7-masala    1 dollar 11200 so’m. Mijoz necha so’m puli borligini kiritsa unga shu puliga to’g’ri keladigan valyuta miqdorini aniqlovchi dastur tuzing.
# print("Pulingizni dollorga o'tkazib beraman.")
# pul = float(input("Pulingiz necha pul (so'mda) -->  "))
# dollor = pul/11200
# print(f"Pulingiz {dollor} dollor ekan")

# # 8-masala   4 xonali son berilgan. Soning o’nlar va minglar xonasidagi raqamlar ko’paytmasini aniqlovchi dastur tuzing.
# raqam = float(input('4 xonali son kiriting --> '))
# onlik = raqam%1000%100//10
# minglik = raqam//1000
# kopayt = minglik*onlik
# print(f"4 xonali sonni minglik va o'nlik raqamlarini ko'paytmasi {kopayt}")

# # 10-masala   a haqiqiy son berilgan bo‘lsin. Faqat ko‘paytirish amalidan foydalanib: a7 darajasini 4 ta amal bilan hisoblaydigan dastur tuzing.
# haqiqiy = int(input('n = '))
# print(haqiqiy**7)
# m = haqiqiy*haqiqiy**2*haqiqiy**3*haqiqiy
# print(m)

# # 11-masala   . Uzunlik L santimerda berilgan. Uni metrga o’tkazuvchi dastur tuzilsin.
# uzunlik= float(input('Uzunligi (sm) -- '))
# metr=uzunlik/100
# print("Uzunligi ", metr ,'m')

# # 12-masala   Uch xonali son berilgan. Uning yuzlar xonasidagi raqamni aniqlovchi programma tuzilsin.
# son = int(input("3 xonali son kiriting = "))
# if son<1000:
#     son//=100
#     print(f"3 xonali son natijasi {son}")
# else:
#     print('Siz 3 xonali son kiritmadingiz !')

# # 13-masala   Uch xonali son berilgan. Uni chapdan birinchi raqamni o’chirib, o’n tarafiga yozishdan hosil bo’lgan sonni aniqlovchi programma tuzilsin.
# son = int(input("3 xonali son kiriting = "))
# if son<1000:
#     sonn= son%100
#     sons = son//100
#     print(f"{sonn}{sons}")
# else:
#     print("Siz 3 xonali son kiritmadingiz.")

# # 14-masala  Uch xonali son berilgan. Uning raqamlarini teskari tartibda yozilishidan hosil bo’lgan sonni chiqaruvchi dastur tuzilsin.
# son = int(input("3 xonali son kiriting = "))
# if son<1000:
#     birlik= son%100%10
#     onlik = son%100//10
#     yuzlik = son//100
#     print(f"{birlik}{onlik}{yuzlik}")
# else:
#     print("Siz 3 xonali son kiritmadingiz.")

# # 15-masala   To’rt xonali son berilgan. Uning raqamlari ko’paytmasini hisoblovchi dastur tuzilsin.
# son = int(input("4 xonali son kiriting = "))
# if son>1000 and son<10000:
#     birlik = son%1000%100%10
#     onlik = son%1000%100//10
#     yuzlik = son%1000//100
#     minglik = son//1000
#     print(f"4 xonali sonning ko'paytmasi {birlik*onlik*yuzlik*minglik}")
# else:
#     print("Siz 4 xonali son kiritmadingiz.")

# # 16-masala  Uch xonali son berilgan. Uning raqamlari yig’indisi hisoblovchi dastur tuzilsin
# son = int(input("3 xonali son kiriting = "))
# if son<1000:
#     birlik = son%100%10
#     onlik = son%100//10
#     yuzlik = son//100
#     print(f"3 xonali sonni raqamlar yig'indisi {birlik+onlik+yuzlik}")
# else:
#     print("Siz 3 xonali son kiritmadingiz.")

# # 17-masala   Faylning hajmi baytlarda berilgan. Fayl hajmini to’liq kilobaytlarda ifodalovchi programma tuzilsin.
# bayt = int(input("Fayl hajmini kiriting (bayt) - "))
# Kbayt = bayt/1024
# print(f"Fayl hajmi {Kbayt} Kbayt")

# # 18-masala   Berilgan n sekund necha soat va minutdan iboratligini aniqlaydigan dastur tuzing.
# sekund = int(input('Sekundni kiriting -> '))
# minut = sekund//60%60
# soat = sekund//3600
# print(f"{sekund} sekund {soat} soat-u {minut} minutga teng")
# print(minut)

# # 19-masala   Qo’shimcha o’zgaruvchidan foydalanmasdan a va b o’zgaruvchilar qiymatini almashtirib ekranga chiqaruvchi dastur tuzing.
# bir = int(input('a = '))
# ikki = int(input('b = '))
# print(f"a = {ikki}, b = {bir}")

# # 20-masala   999 dan katta son berilgan. Uni yuzliklar xonasidagi raqamni aniqlovchi programma tuzilsin.
# sonlar = int(input("4 xonali son kiriting - "))
# if sonlar>999:
#     yuzlik = sonlar%1000//100
#     print(f"{yuzlik}")
# else:
#     print("Siz 4 xonali son kiritmadingiz.")

# # 21-masala   Uch xonali son berilgan. Uni o’ngdan birinchi raqamni o’chirib, chap tarafiga yozishdan hosil bo’lgan sonni aniqlovchi programma tuzilsin.
# son = int(input("3 xonali son kiriting = "))
# if son<1000:
#     sonn= son%100%10
#     sons = son//10
#     print(f"{sonn}{sons}")
# else:
#     print("Siz 3 xonali son kiritmadingiz.")

# # 22-masala   a sutka va b soat berilgan, ikkalasi jami necha minut bo’lishini aniqlovchi dastur tuzing
# sutka = int(input("Sutkani kiriting (kun) - "))
# soat = int(input("Soatni kiriting - "))
# a = sutka*24*60  # soatga kopaytrib minutga bolinadi
# b = soat*60
# print(f"{sutka} va {soat} jami {a+b} minutga teng.")

# # 23-masala   . Ikki shahar o’rtasidagi masofa berilgan. Masofa S km. Agar inson 1 soatda 7 km tezlik bilan yura olsa u, bu shaharlar orasidagi masofani necha soatda bosib o’tishini aniqlovchi dastur tuzing.
# masofa = int(input("Masofani kiriting (km) - "))
# tezlik = 7  # (km/soat)
# vaqt = tezlik/masofa
# print(f"{masofa} kmni {vaqt} soatda bosib o'tadi.")

# # 24-masala   a hafta bilan b sutka berilgan, bular jami necha soat bo’lishini aniqlovchi dastur tuzing.
# hafta = int(input("Haftani kiriting = "))
# sutka = int(input("Sutkani kiriting = "))
# soat = hafta*7*24
# soat2 = sutka*24
# print(f"{hafta} va {sutka} ning jami {soat+soat2} soat bo'ladi.")

# # 25-masala     Agar internet tezligi 750 kbayt/sekund bo'lsa 1.8 GBayt axborotni necha sekundda uzatish mumkinligini aniqlaydigan dastur tuzing.
# intrnet = 1.8*1024*1024/750
# print(f"Intrnet {intrnet} sekuntda 1.8 Gbayt axborot yuklanadi.")

# # 26-masala   Berilgan sekundni soatga o’tkazadigan dastur tuzing. 1 soat = 3600 s
# sekunt = int(input("Sekundni kiriting = "))
# soat = sekunt/3600
# print(soat, 'soat')

# # 27-masala   N sekund vaqt berilgan. Bu N sekund necha kun, soat, minut va sekunddan iborat ekanligini aniqlovchi programma tuzilsin.
# sekund = int(input("Sekundni kiriting = "))

# # 28-masala    Berigan 3xonali sonning raqamlari ko’paymasini toping
# sonlar = int(input("3 xonali son kiriting - "))
# birlik = sonlar%100%10
# onlik = sonlar%100//10
# yuzlik = sonlar//100
# print(f"3 xonali sonni raqamlar ko'paytmasi {birlik*onlik*yuzlik}")

# # 29-masala   Aylananing R radiusi berilgan. Uning uzunligini aniqlaydigan dastur tuzing.
# radius=int(input("R = "))
# pi=3.14; L=2*pi*radius; print(f"Aylanani uzunligi {L} ga teng")

# # 30-masala    Bitta belgi kompyuter xotirasidan 2 bayt joy oladi deb biling. Faylning hajmi foydalanuvchi tomonidan KBaytda kiritilsa unda nechta belgi borligini aniqlovchi dastur tuzing.
# fayl = int(input("Fayl necha Kbaytligini kiriting = "))
# bayt=fayl*1024/2; print(f"Faylda {bayt} ta belgi bor ekan")

# # 31-masla    Uch xonali son berilgan. Uni o’ngliklar xonasidagi raqam bilan yuzliklar xonasidagi raqamni almashtirishdan hosil bo’lgan sonni aniqlovchi programma tuzilsin.
# son=int(input("Ixtiyoriy son kiriting -> "))
# birlik=son%100%10
# onlik=son%100//10
# yuzlik=son//100; print(f"{onlik}{yuzlik}{birlik}")

# # 32-masala   Berilgan 4 xonali sonda 3 raqami ishtirik etgan yoki etmaganligini anqlang.
# son = int(input("4 xonali son kiriting -> "))
# if son<10000:
#     birlik=son%1000%100%10
#     onlik=son%1000%100//10
#     yuzlik=son%1000//100%10
#     minglik=son//1000
#     if birlik==3 or onlik==3 or yuzlik==3 or minglik==3:
#         print(True)
#     else:
#         print(False)
# else:
#     print("Siz 4 xonali son kiritmagansiz !")

# 33-masala    5 ta butun son berilgan. Shu sonlar orasida nechta musbat va nechta manfiy, nechta nol raqami borligini aniqlovchi dastur tuzing.

# # 34. Foydalanuvchi tomonidan oyning raqami kiritilsa u qaysi faslga kirishini aniqlovchi dastur tuzing.
# fasl = int(input("Oyni kiriting -> "))
# if fasl==1 and fasl==2 and fasl==12:
#     print("Qish faslli")
# elif fasl>=3 and fasl<=5:
#     print("Bahor faslli")
# elif fasl>=6 and fasl<=8:
#     print("Yoz faslli")
# elif fasl>=9 and fasl<=11:
#     print("Kuz faslli")

# # 35. Imtihondan olingan ball kiritilsa uning bahosini aniqlovchi dastur tuzing.
# baho = int(input("Imtihondan olgan ballingizni kiriting -> "))
# if baho>0 and baho<=54:
#     print("Sizning bahoingiz 2")
# elif baho>=55 and baho<=70:
#     print('Sizning bahoingiz 3')
# elif baho>=71 and baho<=84:
#     print('Sizning bahoingiz 4')
# else:
#     print('Sizning bahoingiz 5')

# # 36. Berilgan 3 ta sondan bir xil bo’lmaganini ekranga chiqaradigan dastur tuzing. Agar barcha sonlar bir xil bo’lsa ‘=’ belgisi chiqsin.
# son1 = float(input("A = ")); son2 = float(input('B = ')); son3 = float(input('C = '))
# if son1==son2 and son1==son3 and son2==son3:    print('Bu sonlar teng')
# elif son1==son2:    print(son3)
# elif son1==son3:    print(son2)
# elif son2==son3:    print(son1)

# # 37. 2 ta a va b butun sonlar berilgan. Ularning yig’indisi 10...19 oraliqda bo’lsa, ekranga 20 chiqaring, aks holda yig’indini o’zini chiqaradigan dastur tuzilsin.
# son1 = float(input("A = ")); son2 = float(input('B = '));
# if 10<son1+son2<19:     print(20)
# else:   print(son1+son2)

# # 38. Berilgan 4 xonali sonda minglar yoki birlar xonasida 3 raqami ishtirok etgan yoki etmaganligini aniqlaydigan dastur tuzing.
# son=int(input("4 xonali son kiriting - "))
# if 1000<son<10000:
#     if 3==son//1000 or son%1000%100%10==3:
#         print('Ishtirok etgan')
#     else: print('Ishtirok ertmagan')
# else: print('4 xonali son kiritmadingiz.')

# # 39. Butun son berilgan. Agar son musbat bo’lsa 15 martaga oshiring, manfiy bo’lsa absolut qiymatini (ya’ni modulini), aks holda berilgan sonning o’zini ekranga chiqaruvchi dastur tuzing.
# son=int(input('Ixtiyoriy son kiriting - '))
# if son>0:
#     print(son*15)
# elif son<0:
#     print(abs(son))
# else:
#     print(son)

# # 40. A son berilgan. Agar A musbat bo’lsa 1 qo’shilgan, manfiy bo’lsa absolyut qiymatiga (moduliga) 2 qo’shilgan, aks holda 100 ga bo’lingan qiymatini chiqaruvchi dastur tuzilsin.
# son=int(input('Ixtiyoriy son kiriting - '))
# if son>0:
#     print(son+1)
# elif son<0:
#     print(abs(son)+2)
# else:
#     print(son/100)

# # 41. 3 ta a, b, c sonlar berilgan. Agar shu sonlardan ixtiyoriy biri ikkinchisidan 10 taga yoki undan ko’proqqa farq qilsa, ekranga true, aks holda false chiqaradigan dastur tuzing
# son1 = float(input("A = ")); son2 = float(input('B = ')); son3 = float(input("C = "));
# if son1<10<son2 or son2<10<son3 or son1>10>son3 or son2>10>son3:
#     print(True)
# else:
#     print(False)

# # 42 masala Ikkita butun a va b sonlar berilgan. Jumlani rostlikka tekshiring: a soni 2 dan katta va b soni 3 dan kichik yoki teng.
# son = float(input("Ixtiypriy son kiriting --> "))
# if son>=2 and son <=3:
#     print(True)
# else:
#     print(False)

# # 43 masala  .Uchta butun a, b, c sonlar berilgan. Jumlani rostlikka tekshiring: a, b, c sonlarning faqat ikkitasi musbat son.
# a = int(input('A = '))
# b = int(input('B = '))
# c = int(input('C = '))
# if a and b > 0:
#     print(True)
# else:
#     print(False)

# # 44 masala   Jumlani rostlikka tekshiring: Berilgan uch xonali sonning raqamlari ketma ket o’suvchi bo’lib joylashgan
# a = int(input('A = '))
# b = int(input('B = '))
# c = int(input('C = '))
# sonlar = [a,b,c]
# sonlar.sort()
# print(sonlar)

# # 45 masala   .Jumlani rostlikka tekshiring: Berilgan uch xonali sonning raqamlari ketma ket o’suvchi yoki kamayuvchi bo’lib joylashgan
# a = int(input('A = '))
# b = int(input('B = '))
# c = int(input('C = '))
# sonlar = [a,b,c]
# number = [a,b,c]
# sonlar.sort()
# number.reverse()
# print(sonlar);  print(number)

# # 46 masala   Uch xonali a sonni berilgan. Shu sondagi eng katta raqamni aniqlovchi dastur tuzing
# sonlar = int(input('3 xonali son kiriting --> '))
# if sonlar<1000:
#     bir = sonlar%100%10
#     on = sonlar%100//10
#     yuz = sonlar//100
#     if bir>on and bir>yuz:
#         print(bir)
#     elif yuz<on and on>bir:
#         print(on)
#     else:
#         print(yuz)
# else:
#     print('Siz 3 xonali son kiritmadingiz !')
