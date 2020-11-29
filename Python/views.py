from django.shortcuts import render
from django.http import HttpResponse
import wbdata as w


# Create your views here.
def index(request):
    # return HttpResponse('Hey!!')
    return render(request, "index.html")


def home(request):
    if request.method == "POST":
        def coal(c1):
            amount = 0.015 * c1
            return amount

        def lpg(lg):
            amount = 0.0803 * lg
            return amount

        def redmeat(rm):  # (per day)
            amount = 2.58 * rm  # metric tons of co2 per year
            return amount

        def clothes(cl):  # cl should be in dollars(per month)
            amount = 0.005 * cl
            return amount

        def furniture(fr):  # fr should be in dollars
            amount = 0.001 * fr
            return amount

        def laundry(ld):  # ld is number of times(per week)
            amount = 0.1 * ld
            return amount

        def treadmill(tm):  # tm must be in hrs(per week)
            amount = 0.0467 * tm
            return amount

        def vehicle(hrs):
            amount = 0.0444 * hrs
            return amount

        def papers(number):
            amount = 0.0152 * number
            return amount

        a = request.POST['heat']
        b = request.POST['hrsofheat']
        he = float(b)
        if a == 'coal':
            res1 = coal(he)
        elif a == 'LPG':
            res1 = lpg(he)

        c = request.POST['transportation']
        res2 = 0
        d = request.POST['hrs']
        hr = float(d)
        print(vehicle(hr))
        res3 = vehicle(hr)
        e = request.POST['meat']
        mt = float(e)
        print(redmeat(mt))
        res4 = redmeat(mt)
        f = request.POST['clothes']
        cl = float(f)
        print(clothes(cl))
        res5 = clothes(cl)
        g = request.POST['ac']
        print(g)
        res6 = 0
        h = request.POST['furniture']
        ft = float(h)
        print(furniture(ft))
        res7 = furniture(ft)
        i = request.POST['laundary']
        ld = float(i)
        print(laundry(ld))
        res7 = laundry(ld)
        j = request.POST['treadmill']
        td = float(j)
        print(treadmill(td))
        res8 = treadmill(td)
        k = request.POST['papers']
        p = int(k)
        print(papers(p))
        res9 = papers(p)

        code = request.POST['crcode']
        print(code)
        emission_per_capita = w.get_data("EN.ATM.CO2E.EG.ZS", country=code.upper())/3.667
        for i in emission_per_capita:
            if i['value'] != None:
                emission_per_capita_value = i['value']
                break
        # print(value)

        # country_code = input("Country code : ")
        GDP = w.get_data("NY.GDP.MKTP.CD", country=code.upper())
        GDP_val = GDP[1]['value']
        # print(GDP[1]['value'])

        # country_code = input("Country code : ")
        energy_intensity = w.get_data("EG.EGY.PRIM.PP.KD", country=code.upper())
        # print(energy_intensity)
        for i in energy_intensity:
            if i['value'] != None:
                energy_intensity_val = i['value']
                break
        # print(val)
        # print(emission_per_capita_value)
        # print(GDP_val)
        # print(energy_intensity_val)
        # print()
        kaya_value = (emission_per_capita_value * GDP_val * energy_intensity_val * 0.001) / 41.868
        result = res1 + res2 + res3 + res4 + res5 + res6 + res7 + res8
        print(result)
        print(kaya_value)

    return render(request, "home.html", {'getvalue': result, 'countrycode': kaya_value})


def recommendations(request):
    if request.method == "POST":
        a1 = request.POST['Jogging']
        if a1 == 'Treadmill':
            rec1 = "Prefer running, walking or jogging and enjoy the fresh air"
        else:
            rec1 = ""
        b1 = request.POST['LED']
        if b1 == 'Bulb':
            rec2 = "Use LED and light your years ahead"
        else:
            rec2 = ""
        c1 = request.POST['Solar']
        if c1 == 'No':
            rec3 = "Use Solar panel and save your electricity bill"
        else:
            rec3 = ""
        d1 = request.POST['transport']
        if d1 == 'Private':
            rec4 = "Use public transport and make new friends"
        else:
            rec4 = ""
        e1 = request.POST['diet']
        if e1 == "Vegetarian" or e1 == "Non-Vegetarian":
            rec5 = "Eat vegan and reduce your carbon footprint of food to half"
        else:
            rec5 = ""
        f1 = request.POST['ac']
        if f1 == 'Yes':
            rec6 = "Do not place lamps or TV sets near your air conditioner as it cause ACs to run longer"
        else:
            rec6 = ""
        g1 = request.POST['bags']
        if g1 == 'Polythene bags':
            rec7 = "Make jute bags your best friend as it is the new trend"
        else:
            rec7 = ""
        h1 = request.POST['shop']
        if h1 == "Yes":
            rec8 = "The garment industry is one of the biggest source of CO2 emissions, so shop less and save your money"
        else:
            rec8 = ""
        i1 = request.POST['Laptop']
        if i1 == "Desktop":
            rec9 = "It's time to buy a new laptop as Desktop uses more energy for its operation"
        else:
            rec9 = ""
        j1 = request.POST['car']
        if j1 == "No":
            rec10 = "Keep your car's full efficiency in check and send it for regular maintenance"
        else:
            rec10 = ""
        k1 = request.POST['flights']
        if k1 == "Yes":
            rec11 = "Prefer car,bus or train and save your money"
        else:
            rec11 = ""

    return render(request, "last page.html",
                  {'recommendations': [rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8, rec9, rec10, rec11]})


def questions(request):
    return render(request, "questions.html")

def save(request):
    return render(request, "save.html")
