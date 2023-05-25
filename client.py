import http.client
import json


class ChatGPTClient:
    def __init__(self, **kwargs):
        self.url = kwargs.get("url", "127.0.0.1")
        self.port = kwargs.get("port", 8080)
        self.endpoint = kwargs.get("endpoint", "/create/")
        self.connection = http.client.HTTPConnection(self.url, self.port)
        self.headers = kwargs.get("headers", {"Content-type": "application/json"})

    def create(self, **data):
        data = json.dumps(data).encode()
        self.connection.request("POST", self.endpoint, data, self.headers)

        response = self.connection.getresponse()

        if response.status == 200 and response.getheader("Transfer-Encoding") == "chunked":
            print("Receiving chunked data...")
            while True:
                chunk = response.read(1)
                if not chunk:
                    break
                print(chunk.decode(), end="")
        else:
            print(f"Unexpected status code: {response.status}")

        self.connection.close()


client = ChatGPTClient()
client.create(
              model="gpt-3.5-turbo",
              messages=[
                  {"role": "user", "content": "Say this is a test."},
              ],
              stream=True,)
