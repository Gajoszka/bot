import statistics

import requests


def weatherURL():
    api_url = 'http://api.openweathermap.org/data/2.5/weather?appid=73041764461c75168f67f580c696f3a4&q='
    name_City = input('City Name :')
    url = api_url + name_City

    json_data = requests.get(url).json()
    Latitude_data = json_data['coord']['lat']
    Longitude_data = json_data['coord']['lon']

    url_part1 = 'https://api.darksky.net/forecast/8a775ab50744d50f8b565f3ae94dcd67/'
    url_part2 = ','
    url_part3 = ','
    url_part5 = 'T'
    url_part4 = '-'
    url_part6 = '?exclude=currently,flags'
    currentYear = int(input('enterdate ([YYYY]): '))
    yr1prev = currentYear - 1
    yr2prev = currentYear - 2
    yr3prev = currentYear - 3

    monthDay = input('enterdate ([MM]-[DD]): ')

    time = input('[HH]:[MM]:[SS]): ')

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    urlYear1 = url_part1 + str(Latitude_data) + url_part2 + str(Longitude_data) + url_part3 + str(
        yr1prev) + url_part4 + monthDay + url_part5 + time + url_part6

    json_data = requests.get(urlYear1).json()

    temp1 = json_data['hourly']['data'][0]['temperature']
    wind_speed1 = json_data['hourly']['data'][0]['windSpeed']
    humidity1 = json_data['hourly']['data'][0]['humidity']
    # rain_prob1 = json_data['hourly']['data'][0]['precipProbability']
    # weather_info1 = json_data['hourly']['data'][0]['icon']
    description1 = json_data['hourly']['summary']

    Fahrenheit_to_Celsius1 = (temp1 - 32) * (5 / 9)
    temp_in_celsius1 = round(Fahrenheit_to_Celsius1, 2)

    humidity_in_percentage1 = humidity1 * 100
    # rain_prob1_percentage = rain_prob1 * 100

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    urlYear2 = url_part1 + str(Latitude_data) + url_part2 + str(Longitude_data) + url_part3 + str(
        yr2prev) + url_part4 + monthDay + url_part5 + time + url_part6

    json_data = requests.get(urlYear2).json()

    temp2 = json_data['hourly']['data'][0]['temperature']
    wind_speed2 = json_data['hourly']['data'][0]['windSpeed']
    humidity2 = json_data['hourly']['data'][0]['humidity']
    # rain_prob2 = json_data['hourly']['data'][0]['precipProbability']
    # weather_info = json_data['hourly']['data'][0]['icon']
    description = json_data['hourly']['summary']

    Fahrenheit_to_Celsius2 = (temp2 - 32) * (5 / 9)
    temp_in_celsius2 = round(Fahrenheit_to_Celsius2, 2)

    humidity_in_percentage2 = humidity2 * 100
    # rain_prob2_percentage = rain_prob2 * 100

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    urlYear3 = url_part1 + str(Latitude_data) + url_part2 + str(Longitude_data) + url_part3 + str(
        yr3prev) + url_part4 + monthDay + url_part5 + time + url_part6

    json_data = requests.get(urlYear3).json()

    temp3 = json_data['hourly']['data'][0]['temperature']
    wind_speed3 = json_data['hourly']['data'][0]['windSpeed']
    humidity3 = json_data['hourly']['data'][0]['humidity']
    # rain_prob3 = json_data['hourly']['data'][0]['precipProbability']
    # weather_info = json_data['hourly']['data'][0]['icon']
    description = json_data['hourly']['summary']

    Fahrenheit_to_Celsius3 = (temp3 - 32) * (5 / 9)
    temp_in_celsius3 = round(Fahrenheit_to_Celsius3, 2)

    humidity_in_percentage3 = humidity3 * 100
    # rain_prob3_percentage = rain_prob3 * 100

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    listofTemp = [temp_in_celsius1, temp_in_celsius2, temp_in_celsius3]
    averageTemp = round(statistics.mean(listofTemp), 2)

    listWindspeed = [wind_speed1, wind_speed2, wind_speed3]
    averageWindspeed = round(statistics.mean(listWindspeed), 2)

    listHumidities = [humidity_in_percentage1, humidity_in_percentage2, humidity_in_percentage3]
    averageHumidity = round(statistics.mean(listHumidities), 2)

    # listRainProb = [rain_prob1_percentage, rain_prob2_percentage, rain_prob3_percentage]
    # averageRainProb = round(statistics.mean(listRainProb), 2)

    # -----------------------------------------------------------------------------------------------------------------------------------------------
    print('')
    print('')
    # print ('Weather at given time: {} '.format(weather_info1))
    print('General weather on this day: {} '.format(description1))
    print('Temperature : {} degree celsius. '.format(averageTemp))
    print('Wind Speed : {} m/s. '.format(averageWindspeed))
    print('Humidity : {} %. '.format(averageHumidity))
    # print('Probability of Rain: {} %. '.format(averageRainProb))
    print('Description : {}'.format(description1))
