import requests

api_keys = ["ccaf284e2c7322650b4d22edc05ff7b4", "423878ba73d398385d87b8559c20e1c6", "cb433c0cde9836c90855b92accd64610", "68dc4fe85dbc39ec214f7aedc31d7f2a"]

#years = list(range(2018,2023)
years = [2018]
#months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
months = ["05", "06"]
days = ["01", "11", "21"]
#days = ["21"]


counter = 0
i = 0

for year in years:
    for month in months:
        for day in days:
            date_fields = [str(year), month, day]
            date_string = "-".join(date_fields)
            counter += 1
            i += 1
            api_key = api_keys[i%4]
            url = "https://firms.modaps.eosdis.nasa.gov/api/area/csv/{key}/MODIS_SP/world/10/{date}".format(key=api_key, date=date_string)
            print("Making request for date: ", date_string)
            response = requests.get(url)
            if(response.text=="Exceeding allowed transaction limit."):
                counter -= 1
                print("Request for:{date} failed with error message:{error}".format(date=date_string, error=response.text))
            else:
                f = open(date_string+".csv", "w")
                f.write(response.text)

print("Total requests: ", counter)

# response = requests.get(url)
# print(response.text)