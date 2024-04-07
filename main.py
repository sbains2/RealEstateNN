import http.client 

conn = http.client.HTTPSConnection("api.gateway.attomdata.com") 

headers = { 
    'accept': "application/json", 
    'apikey': "54099c208364c2e344ba7c76bde63066", 
} 

# ZIPCODE QUERY
# Define query parameters
zipcode = "98391"  # Example zip code (replace with your desired zip code)
queryParams = f"?postal1={zipcode}"  # Filter properties by zip code
# Add query parameters to the endpoint URL
endpoint = f"/propertyapi/v1.0.0/property/address{queryParams}"


# API Call
conn.request("GET", endpoint, headers=headers)

res = conn.getresponse() 
data = res.read() 

print(data.decode("utf-8"))

