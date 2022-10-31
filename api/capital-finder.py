from http.server import BaseHTTPRequestHandler
from urllib import parse 
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        '''
        A function that send response to vercel "Serverless computing":
        it takes query even its country or its capital 
        and send request to "REST Countries API" to get a response and send it to user as response of her/his query 
        '''

        s=self.path
        url_components=parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary=dict(query_string_list)

        if 'country' in dictionary:
            country=dictionary['country']
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + country)
            data = r.json()
            capital=str(data[0]['capital'][0])
            result=f'The capital of {country} is {capital}.' 


        elif 'capital' in dictionary:
            capital=dictionary['capital']
            url = 'https://restcountries.com/v3.1/capital/'
            r = requests.get(url + capital)
            data = r.json()
            country=str(data[0]['name']['common'])
            result=f'{capital} is the capital of {country}.'   

    
        else :
            result="please provide me with a country name or its capital"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
     
        self.wfile.write(result.encode())
        return