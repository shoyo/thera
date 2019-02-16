import requests,json


#Change IP address,get IP address and get geolocation
response = requests.get("https://moocher-io-ip-geolocation-v1.p.rapidapi.com/192.119.168.96",
  headers={
    "X-RapidAPI-Key": "85a5d7a39emsh30bfd214eaadf58p15822fjsn42e2f79f9778"
  }
)
location = response.json()
latitude = float(location['ip']['latitude'])
longitude = float(location['ip']['longitude'])
print(latitude,longitude)
loc = 'location=' + str(latitude) + '%2C' + str(longitude)
api_key = 'a549447491dbb332ce44a9a9a4a1098a' #LOCAL FILE
query = 'https://api.betterdoctor.com/2016-03-01/practices?'+loc+'%2C100&user_location='+str(latitude)+'%2C'+str(longitude)+'&skip=0&limit=3&user_key='+api_key
find_doc = requests.get(query) #GET ALL INFORMATION ABOUT DOCTORS
result = find_doc.json()
#Parse json
for pos in range(len(result['data'])):
    if result['data'][pos]['total_doctors'] == 0:
        print('No doctor')
        pass
    else:
        name =result['data'][pos]['doctors'][0]['profile']['first_name'] + result['data'][pos]['doctors'][0]['profile']['last_name']
        url_img = result['data'][pos]['doctors'][0]['profile']['image_url']
        specialty = result['data'][pos]['doctors'][0]['specialties'][0]['description']
        city = result['data'][pos]['visit_address']['city']
        state = result['data'][pos]['visit_address']['state']
        print(name,url_img,specialty,state,'-',city)



