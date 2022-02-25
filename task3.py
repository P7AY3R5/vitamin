import requests
city = "Moscow,RU"
appid= "af26cab34da466167c09c522a1a54965"
res=requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data=res.json()
print("Погода на текущее день:")
print ("\t",data['weather'][0]['description'],". Скорость ветра: ",data['wind']['speed'],"м/с")
res=requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data["list"]:
    print (i["dt_txt"])
    print ("\t","Видимость: ", i["visibility"]," м ; Скорость ветра: ",
    i['wind']['speed'],"м/с\n")
