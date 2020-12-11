import wbdata as w

country_code = input("Country code : ")

emission_per_capita = w.get_data("EN.ATM.CO2E.EG.ZS", country=country_code.upper())
energy_intensity = w.get_data("EG.EGY.PRIM.PP.KD", country=country_code.upper())
data = w.get_data("SP.POP.TOTL", country=country_code.upper())
GDP = w.get_data("NY.GDP.MKTP.CD", country=country_code.upper())

for i,j,k,l in zip(emission_per_capita, energy_intensity, data, GDP) :
    if(i['value']!=None and j['value']!=None and k['value']!=None and l['value']!=None and i['date']==j['date']==k['date']==l['date']) :
#         print(i['date'],j['date'],k['date'],l['date'])
#         print(i['value'])
#         print()
#         print(j['value'])
#         print()
#         print(k['value'])
#         print()
#         print(l['value'])
        population = k['value']
        emission_per_capita_value = i['value']
        GDP_val = l['value']
        energy_intensity_val = j['value']
        break
kaya_value = (population*emission_per_capita_value * GDP_val * energy_intensity_val*0.001)/41.868
print(kaya_value,"metric tonne")
print(i['date'])
