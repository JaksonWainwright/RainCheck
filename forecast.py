import requests, json
import secureconf, conf


class Forecast:
    def __init__(self):
        self.base_api_url = conf.base_api_url
        self.zip_codes = conf.zip_codes

    def send_get_request(self, uri):
        request = requests.get(f'{self.base_api_url}/{uri}&appid={secureconf.api_key}')
        return request.json()

    def get_current_weather(self):
        json_results = {}
        for city, zip_code in self.zip_codes.items():
            try:
                len(zip_code)
                for sub_zip in zip_code:
                    self.json_results[city] = self.send_get_request(f'weather?zip={str(sub_zip)}')
            except TypeError:
                self.json_results[city] = self.send_get_request(f'weather?zip={str(zip_code)}')
        self.json_results = json.dumps(self.json_results)
        return json.dumps(self.json_results)

    def get_weather_descriptions(self):
        self.get_current_weather()
        print(self.json_results)


#print(Forecast().get_current_weather())
#print(Forecast().send_get_request('weather?zip=84121'))
Forecast().get_weather_descriptions()