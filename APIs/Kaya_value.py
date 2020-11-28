import wbdata as w

country_code = input("Country code : ")
emission_per_capita = w.get_data("EN.ATM.CO2E.EG.ZS", country=country_code.upper())
for i in emission_per_capita:
    if i['value'] != None :
        emission_per_capita_value = i['value']
        break
#print(value)

# country_code = input("Country code : ")
GDP = w.get_data("NY.GDP.MKTP.CD", country=country_code.upper())
GDP_val =  GDP[1]['value']
# print(GDP[1]['value'])

# country_code = input("Country code : ")
energy_intensity = w.get_data("EG.EGY.PRIM.PP.KD", country=country_code.upper())
#pprint(energy_intensity)
for i in energy_intensity:
    if i['value'] != None :
        energy_intensity_val = i['value']
        break
#print(val)
# print(emission_per_capita_value)
# print(GDP_val)
# print(energy_intensity_val)
# print()
kaya_value = emission_per_capita_value * GDP_val * energy_intensity_val
print((kaya_value*0.001)/41.868,"metric tonne")
