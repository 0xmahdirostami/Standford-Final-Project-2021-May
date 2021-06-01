
"""
graph of each country
and
an image of all countries (deaths ,confirmed ,recovered)
"""

# don't worry about this import! It just allows us to grab all the files in the Finalproject/ directory
import csv
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



def calculate_dict_confirm():
    #create totall dictionary
    calculate_dict_confirmed={}
    with open("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv") as co:
        next(co)
        #creat id for every line
        id=0
        for line in co:
            #create a dictionary for each line
            calculate_line={}
            list_line=line.split(",")
            #since there is "," in the name of countries
            if len(list_line)==501:
                list_line.pop(1)
            if list_line[1][0]==" ":
                list_line[1]="Korea South"
            calculate_line["state"]=list_line[0]
            calculate_line["country"]=list_line[1]
            # see there is lat and long or not and convert string to float
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
            # create a totall and 2 moth -2month values
            calculate_line["totall_confirmed"] = sum(map(float,list_line[4:]))
            #print(len(list_line))

            calculate_line["3-22-2020_co"]=sum(map(float,list_line[4:66]))
            calculate_line["5-22-2020_co"] = sum(map(float, list_line[66:126]))
            calculate_line["7-22-2020_co"] = sum(map(float, list_line[126:186]))
            calculate_line["9-22-2020_co"] = sum(map(float, list_line[184:246]))
            calculate_line["11-22-2020_co"] = sum(map(float, list_line[246:306]))
            calculate_line["1-22-2021_co"] = sum(map(float, list_line[306:366]))
            calculate_line["3-22-2021_co"] = sum(map(float, list_line[366:426]))
            calculate_line["5-22-2021_co"] = sum(map(float, list_line[426:]))

            print(calculate_line["state"],calculate_line["country"])
            calculate_dict_confirmed[id]=calculate_line
            id += 1
    return calculate_dict_confirmed

def calculate_dict_death():
    #create totall dictionary
    calculate_dict_death={}
    with open("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv") as de:
        next(de)
        #creat id for every line
        id=0
        for line in de:
            #create a dictionary for each line
            calculate_line={}
            list_line=line.split(",")
            #since there is "," in the name of countries
            if len(list_line) == 501:
                list_line.pop(1)
            if list_line[1][0] == " ":
                list_line[1] = "Korea South"
            calculate_line["state"]=list_line[0]
            calculate_line["country"]=list_line[1]
            # see there is lat and long or not and convert string to float
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
            #create a totall and 2 moth -2month values
            calculate_line["totall_deaths"] = sum(map(float,list_line[4:]))
            # len list_line =494
            # len days=494-3=491
            # len 2 moths= 491//8==60
            calculate_line["3-22-2020_de"]=sum(map(float,list_line[4:66]))
            calculate_line["5-22-2020_de"] = sum(map(float, list_line[66:126]))
            calculate_line["7-22-2020_de"] = sum(map(float, list_line[126:186]))
            calculate_line["9-22-2020_de"] = sum(map(float, list_line[186:226]))
            calculate_line["11-22-2020_de"] = sum(map(float, list_line[226:306]))
            calculate_line["1-22-2021_de"] = sum(map(float, list_line[306:366]))
            calculate_line["3-22-2021_de"] = sum(map(float, list_line[366:426]))
            calculate_line["5-22-2021_de"] = sum(map(float, list_line[426:]))

            calculate_dict_death[id]=calculate_line
            id += 1
    return calculate_dict_death


def calculate_dict_recovered():
    #create totall dictionary
    calculate_dict_recovered={}
    with open("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv") as re:
        next(re)
        #creat id for every line
        id=0
        for line in re:
            #create a dictionary for each line
            calculate_line={}
            list_line=line.split(",")
            #since there is "," in the name of countries
            if len(list_line) == 501:
                list_line.pop(1)
            if list_line[1][0] == " ":
                list_line[1] = "Korea South"
            calculate_line["state"]=list_line[0]
            calculate_line["country"]=list_line[1]
            # see there is lat and long or not and convert string to float
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
            # create a totall and 2 moth -2month values
            calculate_line["totall_recovered"] = sum(map(float,list_line[4:]))
            # len list_line =494
            # len days=494-3=491
            # len 2 moths= 491//8==60
            calculate_line["3-22-2020_re"]=sum(map(float,list_line[4:66]))
            calculate_line["5-22-2020_re"] = sum(map(float, list_line[66:126]))
            calculate_line["7-22-2020_re"] = sum(map(float, list_line[126:186]))
            calculate_line["9-22-2020_re"] = sum(map(float, list_line[186:246]))
            calculate_line["11-22-2020_re"] = sum(map(float, list_line[246:306]))
            calculate_line["1-22-2021_re"] = sum(map(float, list_line[306:366]))
            calculate_line["3-22-2021_re"] = sum(map(float, list_line[366:426]))
            calculate_line["5-22-2021_re"] = sum(map(float, list_line[426:]))

            calculate_dict_recovered[id]=calculate_line
            id += 1
    return calculate_dict_recovered

#creat graph for each counrty or state
def graph(num , country ,state):

    dict_death = calculate_dict_death()
    dict_recovered = calculate_dict_recovered()
    dict_confirm = calculate_dict_confirm()
    #in recovered dict there is one canada ,in death and confirmed there is 15 states
    #num 39 is canada
    if num==39:
        one1 ,two1 ,three1 ,four1 ,five1 ,six1 ,seven1 ,eight1 = 0,0,0,0,0,0,0,0
        for num in range(39,55):
            one1 += dict_confirm[num]["3-22-2020_co"]
            two1 += dict_confirm[num]["5-22-2020_co"]
            three1+=dict_confirm[num]["7-22-2020_co"]
            four1+= dict_confirm[num]["9-22-2020_co"]
            five1+= dict_confirm[num]["11-22-2020_co"]
            six1 += dict_confirm[num]["1-22-2021_co"]
            seven1+=dict_confirm[num]["3-22-2021_co"]
            eight1+=dict_confirm[num]["5-22-2021_co"]

        x1 = [2, 4, 6, 8, 10, 12, 14, 16]
        y1 = [one1,two1,three1,four1,five1,six1,seven1,eight1]
        # plotting the line 1 points
        plt.plot(x1, y1, label="confirmed")

        one, two, three, four, five, six, seven, eight = 0,0,0,0,0,0,0,0
        for num in range(39, 55):
            one += dict_death[num]["3-22-2020_de"]
            two += dict_death[num]["5-22-2020_de"]
            three += dict_death[num]["7-22-2020_de"]
            four += dict_death[num]["9-22-2020_de"]
            five += dict_death[num]["11-22-2020_de"]
            six += dict_death[num]["1-22-2021_de"]
            seven += dict_death[num]["3-22-2021_de"]
            eight += dict_death[num]["5-22-2021_de"]
        # line 2 points
        x2 = [2, 4, 6, 8, 10, 12, 14, 16]
        y2 = [one,two,three,four,five,six,seven,eight]
        # plotting the line 2 points
        plt.plot(x2, y2, label="death")
        # line 3 points
        x3 = [2, 4, 6, 8, 10, 12, 14, 16]
        y3 = [one1-one-10000,two1-two-20000,three1-three-30000,four1-four-4000000,five1-five-5000000
            ,six1-six-6000000,seven1-seven-7000000,eight1-eight-10000000]

        # plotting the line 2 points
        plt.plot(x3, y3, label="recovered")
        # naming the x axis
        plt.xlabel('time(months)')
        # naming the y axis
        plt.ylabel('reports(people)')
        # giving a title to my graph
        plt.title(country + " " + state + " between 1/22/2020 - 5/25/2021")

        # show a legend on the plot
        plt.legend()

        # show
        plt.show()
    else:
        num = change(num)
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
        if num>54:
            num=num-15
        x3 = [2,4,6,8,10,12,14,16]
        y3 = [
            dict_recovered[num]["3-22-2020_re"], dict_recovered[num]["5-22-2020_re"]
            , dict_recovered[num]["7-22-2020_re"], dict_recovered[num]["9-22-2020_re"]
            , dict_recovered[num]["11-22-2020_re"], dict_recovered[num]["1-22-2021_re"]
            , dict_recovered[num]["3-22-2021_re"], dict_recovered[num]["5-22-2021_re"]]
        # plotting the line 2 points
        plt.plot(x3, y3, label="recovered")
        # naming the x axis
        plt.xlabel('time(months)')
        # naming the y axis
        plt.ylabel('reports(people)')
        # giving a title to my graph
        plt.title(country +" "+state +" between 1/22/2020 - 5/31/2021")

        # show a legend on the plot
        plt.legend()

        #show
        plt.show()
def change(num):
    if num>39:
        num=num+15
        return num
    else:
        return num


#find a number of countries list
def find_num(answer):
    dict=calculate_dict_recovered()
    for num in range(260):
        if dict[num]["country"]==answer:
            if dict[num]["state"]=="":
                return (num ,answer ,"" )
            else:
                state=input("which state please type a name that first letter is uppercase::").title()
                if state==dict[num]["state"]:
                    return (num , answer ,state)
                else:
                    for num in range(260):
                        if state==dict[num]["state"] and dict[num]["country"]==answer:
                            return (num, answer, state)



"""creat image"""

def plot_pixel(visualization, x, y ,dict,average,totall,which):
    """
    Set a pixel at a particular coordinate to be blue. Pixels start off as
    white, so all three color components have a value of 255. Setting the red
    and green components to 0 makes the pixel appear blue.

    Note that we don't return anything in this function because the Pixel is
    'mutated' in place

    Parameters:
        - `visualization` is the SimpleImage that will eventually be
          shown to the user
        - `x` is the x coordinate of the pixel that we are turning blue
        - `y` is the y coordinate of the pixel that we are turning blue
    """

    rang=int(totall*10//average)
    #print(rang)
    if rang>=15:
        rang=15
    elif rang<1:
        rang=1
    if which == "Death":
        for i in range(-rang,+rang):
            pixel = visualization.get_pixel(x+i, y+i)
            pixel.blue =0
            pixel.green =0
            pixel = visualization.get_pixel(x - i, y + i)
            pixel.blue = 0
            pixel.green =0
            pixel = visualization.get_pixel(x + i, y - i)
            pixel.blue = 0
            pixel.green = 0
    elif which=="Confirmed":
        for i in range(-rang,+rang):
            pixel = visualization.get_pixel(x+i, y+i)
            pixel.red =0
            pixel.blue =0
            pixel.green =0
            pixel = visualization.get_pixel(x - i, y + i)
            pixel.red = 0
            pixel.blue =0
            pixel.green = 0
            pixel = visualization.get_pixel(x + i, y - i)
            pixel.red = 0
            pixel.blue = 0
            pixel.green = 0

    elif which == "Recovered":
        for i in range(-rang,+rang):
            pixel = visualization.get_pixel(x+i, y+i)
            pixel.red =0
            pixel.green =0
            pixel = visualization.get_pixel(x - i, y + i)
            pixel.red = 0
            pixel.green =0
            pixel = visualization.get_pixel(x + i, y - i)
            pixel.red = 0
            pixel.green = 0


def longitude_to_x(longitude):
    """
    Scales a longitude coordinate to a coordinate in the visualization email
    """
    return VISUALIZATION_WIDTH * (longitude - MIN_LONGITUDE) / (MAX_LONGITUDE - MIN_LONGITUDE)


def latitude_to_y(latitude):
    """
    Scales a latitude coordinate to a coordinate in the visualization email
    """
    return VISUALIZATION_HEIGHT * (1.0 - (latitude - MIN_LATITUDE) / (MAX_LATITUDE - MIN_LATITUDE))


def plot(which):
    # create a blank image on which we'll plot cities
    visualization = SimpleImage.blank(
        VISUALIZATION_WIDTH, VISUALIZATION_HEIGHT
    )
    if which=="Death":
        dict=calculate_dict_death()
        #calculate average
        sum = 0
        for i in range(275):
            sum += dict[i]["totall_deaths"]
        average=sum/275
        for i in range(275):
            y=latitude_to_y(dict[i]['lat'])
            x=longitude_to_x(dict[i]['long'])
            totall = dict[i]["totall_deaths"]
            if 0 < x < visualization.width and 0 < y < visualization.height:
                plot_pixel(visualization, x, y ,dict,average,totall,which)

    elif which=="Recovered":
        dict=calculate_dict_recovered()
        # calculate average
        sum = 0
        # the length of recovered dictionary is less than the others
        for i in range(260):
            sum += dict[i]["totall_recovered"]
        average = sum / 260
        # the length of recovered dictionary is less than the others
        for i in range(260):
            y=latitude_to_y(dict[i]['lat'])
            x=longitude_to_x(dict[i]['long'])
            totall = dict[i]["totall_recovered"]
            if 0 < x < visualization.width and 0 < y < visualization.height:
                plot_pixel(visualization, x, y, dict, average, totall, which)

    elif which=="Confirmed":
        dict=calculate_dict_confirm()
        sum=0
        for i in range(275):
            sum += dict[i]["totall_confirmed"]
        average=sum/275
        for i in range(275):
            y=latitude_to_y(dict[i]['lat'])
            x=longitude_to_x(dict[i]['long'])
            totall=dict[i]["totall_confirmed"]
            if 0 < x < visualization.width and 0 < y < visualization.height:
                plot_pixel(visualization, x, y ,dict,average,totall,which)
    else:
        print("invalid input")
    visualization.show()



def main():
    answer=input("do you want a graph or an image :").title()
    if answer=="Image":
        which=input("which one :death ,recovered ,confirmed ").title()
        try:
            plot(which)
        except:
            print("invalid input")
    elif answer=="Graph":
        answer=input("which country please type a name that first letter is uppercase:").title()
        try:
            num , country , state=find_num(answer)
            graph(num , country ,state)
        except:
            print("please type correct country.")
    else:
        print("invalid input")
if __name__ == "__main__":
    main()
