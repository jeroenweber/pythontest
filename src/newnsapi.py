import http.client, urllib.parse, urllib.error, credentials

user = 'jeroen.weber@hu.nl'
filename = 'stations4.dct'
headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': credentials.getcredentials(user),
}
params = urllib.parse.urlencode({
})

def writetofile(response,filename):
    bestand = open(filename, 'w')
    bestand.write(str(response))
    bestand.close()

try:
    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request("GET", "/reisinformatie-api/api/v2/stations?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    nsdata = data.decode("utf-8")
    print(nsdata)
    writetofile(nsdata, filename)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


