import requests


class TuringBot:

    url = "http://openapi.tuling123.com/openapi/api/v2"

    signal_thread = "0e4dc4f3608b4da38dbbac4c746b6428"
    not_robot_key = "7714085bddd24e7aa77b071d8eaec5db"

    @classmethod
    def automatic_reply(cls, text):

        parameter_json = {
                            "reqType": 0,
                            "perception": {
                                "inputText": {
                                    "text": text
                                }
                            },
                            "userInfo": {
                                "apiKey": cls.not_robot_key,
                                "userId": "single"
                            }
                        }

        response = requests.post(cls.url, json=parameter_json)
        return response.json()["results"][0]["values"]["text"]
