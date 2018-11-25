def health_calc(age, applesAte, cigsSmoked):
    answer = (100-age)+(applesAte * 3.5) - (cigsSmoked * 2)
    print(answer)


buckysData = [27, 20, 0]
#Normal passing of arguments
health_calc(buckysData[0], buckysData[1], buckysData[2])
#Unpacking arguments
health_calc(*buckysData)