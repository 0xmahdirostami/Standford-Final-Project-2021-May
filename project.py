
"""
graph of each country
and
an image of all countries (deaths ,confirmed ,recovered)
"""

# don't worry about this import! It just allows us to grab all the files in the Finalproject/ directory
import csv
import os
import matplotlib.pyplot as plt
from simpleimage import SimpleImage

# Dimensions of the final visualization. Change these if the
# image is too large for your screen
VISUALIZATION_WIDTH = 1920
VISUALIZATION_HEIGHT = 1080

MIN_LONGITUDE = -180
MAX_LONGITUDE = 180
MIN_LATITUDE = -90
MAX_LATITUDE = 90

# The folder in which all the country data can be found
COUNTRY_DIRECTORY = "finalproject"

def calculate_dict_confirm(filename):
    #create totall dictionary
    calculate_dict_confirmed={}
    with open(filename) as co:
        next(co)
        #creat id for every line
        id=0
        for line in co:
            #create a dictionary for each line
            calculate_line={}
            list_line=line.split(",")
            #since there is "," in the name of countries
            if len(list_line)==495:
                #print(list_line)
                if list_line[1]==""""Korea""":
                    list_line.pop(2)
                    list_line[1] = list_line[1] + " south"
                else:
                    list_line.pop(1)
            calculate_line["state"]=list_line[0]
            calculate_line["country"]=list_line[1]
            if len(list_line[2])==0:
                calculate_line["lat"] = 0
            else:
                if list_line[2][0]=="-":
                    calculate_line["lat"] =-1* float(list_line[2][1:])
                else:
                    calculate_line["lat"] = float(list_line[2])
            if len(list_line[3])==0:
                calculate_line["long"] = 0
            else:
                if list_line[3][0] == "-":
                    calculate_line["long"] = -1 * float(list_line[3][1:])
                else:
                    calculate_line["long"] = float(list_line[3])

            calculate_line["totall_confirmed"] = sum(map(float,list_line[4:]))
            calculate_line["3-22-2020_co"]=sum(map(float,list_line[4:64]))
            calculate_line["5-22-2020_co"] = sum(map(float, list_line[64:124]))
            calculate_line["7-22-2020_co"] = sum(map(float, list_line[124:184]))
            calculate_line["9-22-2020_co"] = sum(map(float, list_line[184:224]))
            calculate_line["11-22-2020_co"] = sum(map(float, list_line[224:304]))
            calculate_line["1-22-2021_co"] = sum(map(float, list_line[304:364]))
            calculate_line["3-22-2021_co"] = sum(map(float, list_line[364:424]))
            calculate_line["5-22-2021_co"] = sum(map(float, list_line[424:]))

            calculate_dict_confirmed[id]=calculate_line
            id += 1
    return calculate_dict_confirmed

def calculate_dict_death(filename):
    #create totall dictionary
    calculate_dict_death={}
    with open(filename) as de:
        next(de)
        #creat id for every line
        id=0
        for line in de:
            #create a dictionary for each line
            calculate_line={}
            list_line=line.split(",")
            #since there is "," in the name of countries
            if len(list_line)==495:
                #print(list_line)
                if list_line[1]==""""Korea""":
                    list_line.pop(2)
                    list_line[1] = list_line[1] + " south"
                else:
                    list_line.pop(1)
            calculate_line["state"]=list_line[0]
            calculate_line["country"]=list_line[1]
            if len(list_line[2])==0:
                calculate_line["lat"] = 0
            else:
                if list_line[2][0]=="-":
                    calculate_line["lat"] =-1* float(list_line[2][1:])
                else:
                    calculate_line["lat"] = float(list_line[2])
            if len(list_line[3])==0:
                calculate_line["long"] = 0
            else:
                if list_line[3][0] == "-":
                    calculate_line["long"] = -1 * float(list_line[3][1:])
                else:
                    calculate_line["long"] = float(list_line[3])

            calculate_line["totall_deaths"] = sum(map(float,list_line[4:]))
            calculate_line["3-22-2020_de"]=sum(map(float,list_line[4:64]))
            calculate_line["5-22-2020_de"] = sum(map(float, list_line[64:124]))
            calculate_line["7-22-2020_de"] = sum(map(float, list_line[124:184]))
            calculate_line["9-22-2020_de"] = sum(map(float, list_line[184:224]))
            calculate_line["11-22-2020_de"] = sum(map(float, list_line[224:304]))
            calculate_line["1-22-2021_de"] = sum(map(float, list_line[304:364]))
            calculate_line["3-22-2021_de"] = sum(map(float, list_line[364:424]))
            calculate_line["5-22-2021_de"] = sum(map(float, list_line[424:]))

            calculate_dict_death[id]=calculate_line
            id += 1

    return calculate_dict_death


def calculate_dict_recovered(filename):
    #create totall dictionary
    calculate_dict_recovered={}
    with open(filename) as re:
        next(re)
        #creat id for every line
        id=0
        for line in re:
            #create a dictionary for each line
            calculate_line={}
            list_line=line.split(",")
            #since there is "," in the name of countries
            if len(list_line)==495:
                #print(list_line)
                if list_line[1]==""""Korea""":
                    list_line.pop(2)
                    list_line[1] = list_line[1] + " south"
                else:
                    list_line.pop(1)
            calculate_line["state"]=list_line[0]
            calculate_line["country"]=list_line[1]
            if len(list_line[2])==0:
                calculate_line["lat"] = 0
            else:
                if list_line[2][0]=="-":
                    calculate_line["lat"] =-1* float(list_line[2][1:])
                else:
                    calculate_line["lat"] = float(list_line[2])
            if len(list_line[3])==0:
                calculate_line["long"] = 0
            else:
                if list_line[3][0] == "-":
                    calculate_line["long"] = -1 * float(list_line[3][1:])
                else:
                    calculate_line["long"] = float(list_line[3])

            calculate_line["totall_recovered"] = sum(map(float,list_line[4:]))
            calculate_line["3-22-2020_re"]=sum(map(float,list_line[4:64]))
            calculate_line["5-22-2020_re"] = sum(map(float, list_line[64:124]))
            calculate_line["7-22-2020_re"] = sum(map(float, list_line[124:184]))
            calculate_line["9-22-2020_re"] = sum(map(float, list_line[184:224]))
            calculate_line["11-22-2020_re"] = sum(map(float, list_line[224:304]))
            calculate_line["1-22-2021_re"] = sum(map(float, list_line[304:364]))
            calculate_line["3-22-2021_re"] = sum(map(float, list_line[364:424]))
            calculate_line["5-22-2021_re"] = sum(map(float, list_line[424:]))

            calculate_dict_recovered[id]=calculate_line
            id += 1
    return calculate_dict_recovered


def graph(num , country ,state):
    dict_death = calculate_dict_death(
        "COVID-19/csse_covid_19_data/csse_covid_19_time_series 22-1-2020 25-5-2021/time_series_covid19_deaths_global.csv")
    dict_recovered = calculate_dict_recovered(
        "COVID-19/csse_covid_19_data/csse_covid_19_time_series 22-1-2020 25-5-2021/time_series_covid19_recovered_global.csv")
    dict_confirm = calculate_dict_confirm(
        "COVID-19/csse_covid_19_data/csse_covid_19_time_series 22-1-2020 25-5-2021/time_series_covid19_confirmed_global.csv")

    x1 = [2,4,6,8,10,12,14,16]
    y1 = [
         dict_confirm[num]["3-22-2020_co"],dict_confirm[num]["5-22-2020_co"]
        ,dict_confirm[num]["7-22-2020_co"],dict_confirm[num]["9-22-2020_co"]
        ,dict_confirm[num]["11-22-2020_co"],dict_confirm[num]["1-22-2021_co"]
        ,dict_confirm[num]["3-22-2021_co"],dict_confirm[num]["5-22-2021_co"]]
    # plotting the line 1 points
    plt.plot(x1, y1, label="confirmed")

    # line 2 points
    x2 = [2,4,6,8,10,12,14,16]
    y2 = [
        dict_death[num]["3-22-2020_de"], dict_death[num]["5-22-2020_de"]
        , dict_death[num]["7-22-2020_de"], dict_death[num]["9-22-2020_de"]
        , dict_death[num]["11-22-2020_de"], dict_death[num]["1-22-2021_de"]
        , dict_death[num]["3-22-2021_de"], dict_death[num]["5-22-2021_de"]]
    # plotting the line 2 points
    plt.plot(x2, y2, label="death")
    # line 3 points
    x3 = [2,4,6,8,10,12,14,16]
    y3 = [
        dict_recovered[num]["3-22-2020_re"], dict_recovered[num]["5-22-2020_re"]
        , dict_recovered[num]["7-22-2020_re"], dict_recovered[num]["9-22-2020_re"]
        , dict_recovered[num]["11-22-2020_re"], dict_recovered[num]["1-22-2021_re"]
        , dict_recovered[num]["3-22-2021_re"], dict_recovered[num]["5-22-2021_re"]]
    # plotting the line 2 points
    plt.plot(x3, y3, label="recovered")
    # naming the x axis
    plt.xlabel('time(months')
    # naming the y axis
    plt.ylabel('reports(people')
    # giving a title to my graph
    plt.title('confirmed , death , recovered in '+ country +" (" +state+")")

    # show a legend on the plot
    plt.legend()

    #show
    plt.show()

def find_num(answer):
    with open("COVID-19/csse_covid_19_data/csse_covid_19_time_series 22-1-2020 25-5-2021/time_series_covid19_deaths_global.csv") as f:
        next(f)
        num = 0
        for line in f:
            # create a dictionary for each line
            list_line = line.split(",")
            # since there is "," in the name of countries
            if len(list_line) == 495:
                # print(list_line)
                if list_line[1] == """"Korea""":
                    list_line.pop(2)
                    list_line[1] = list_line[1] + " south"
                else:
                    list_line.pop(1)
            #print(list_line[1])
            if list_line[1]==answer:
                if list_line[0]=="":
                    return (num , list_line[1] , "")
                else:
                    state=input("which state:").title()
                    for line in f:
                        # create a dictionary for each line
                        list_line = line.split(",")
                        # since there is "," in the name of countries
                        if len(list_line) == 495:
                            # print(list_line)
                            if list_line[1] == """"Korea""":
                                list_line.pop(2)
                                list_line[1] = list_line[1] + " south"
                            else:
                                list_line.pop(1)
                        if state==list_line[0] and answer==list_line[1]:
                            return (num , list_line[1] ,list_line[0])

            else:
                num += 1

def creat_image():
    pass

def main():
    answer=input("do you want graph or an image :").title()
    if answer=="Image":
        which=input("which one :death ,recovered ,confirmed ").title()
        creat_image(which)
    elif answer=="Graph":
        answer=input("which country:").title()
        try:
            num , country , state=find_num(answer)
            graph(num , country ,state)
        except:
            print("please type correct country.")
    else:
        print("invalid input")
if __name__ == "__main__":
    main()