import json
import requests
import os
'''
do pip install ntfy and obtain APIKey from https://market.mashape.com/navii/daily-fuel-price-india/overview
'''
def notification(response):
	json_res = json.loads(response)
	title = "Petrol Price Update"
	msg = "Todays price is  Rs.{0}/- for {1} ".format(json_res["price"],json_res["state"])
	print msg
	cmd = "ntfy -t \"{0}\" send \"{1}\" ".format(title,msg)
	os.system(cmd)


print "ap = Andhra Pradesh\nan = Andaman and Nicobar Islands\nar = Arunachal Pradesh\nas = Assam\nbr = Bihar\ncg = Chhattisgarh\nch = Chandigarh\ndl = Delhi\nga = Goa\ngj = Gujarat\nhr = Haryana\nhp = Himachal Pradesh\njk = Jammu & Kashmir\njh = Jharkhand\nka = Karnataka\nkl = Kerala\nmp = Madhya Pradesh\nmh = Maharashtra\nmn = Manipur\nml = Meghalaya\nmz = Mizoram\nnl = Nagaland\nor = Orissa\npb = Punjab\npy = Pondicherry\nrj = Rajasthan\nsk = Sikkim\ntn = Tamil Nadu\ntr = Tripura\nts = Telangana\nup = Uttar Pradesh\nuk = Uttarakhand\nwb = West Bengal"
code = raw_input("Enter the state code: ")
api_key = "<Your_API_Key>"
end_point = "https://fuelprice.p.mashape.com/"
headers = {"Content-Type":"application/json","Accept":"application/json","X-Mashape-Key":api_key}
params = {"fuel":"p","state":code}
response = requests.post(end_point,json=params,headers=headers)
json_res = json.loads(response.text)
notification(response.text)

