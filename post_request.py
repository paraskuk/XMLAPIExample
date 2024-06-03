import requests

# URL of the FastAPI endpoint
url = "http://127.0.0.1:8000/consume-xml"

# Path to the XML file
xml_file_path = "data/data.xml"

# Read the XML file
with open(xml_file_path, "r") as file:
    xml_data = file.read()

# Set the headers for the request
headers = {
    "Content-Type": "application/xml"
}

# Make the POST request
response = requests.post(url, data=xml_data, headers=headers)

# Print the response from the server
print("Status Code:", response.status_code)
print("Response Content:", response.json())
