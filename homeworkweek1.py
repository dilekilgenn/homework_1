countries_list= ["turkey","germany","italy", "canada", "brazil" , "egypt"]
#listenin eleman sayısını bulmak için
len(countries_list)
print(len(countries_list))

for i in countries_list:
    print(i)

if "turkey" in countries_list:
        print("turkey listede var.")
else :
        print("turkey listede yok.")


if "japan" in countries_list:
    print("japan listede var.")
else:
    print("japan listede yok.")

def elemanları_say(input_string):
    eleman_list={}

    for eleman in input_string:
        if eleman in eleman_list:
            eleman_list[eleman] += 1
        else:
            eleman_list[eleman] = 1
    return  eleman_list

input_str = "ada lovelace akademi"
sonuç= elemanları_say(input_str)
print(sonuç)






