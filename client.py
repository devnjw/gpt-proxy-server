import http.client
import json

class ChatGPTClient:
    def __init__(self, **kwargs):
        self.url = kwargs.get("url", "127.0.0.1")
        self.port = kwargs.get("port", 5000)
        self.endpoint = kwargs.get("endpoint", "/create/")
        self.connection = http.client.HTTPConnection(self.url, self.port)
        self.headers = kwargs.get("headers", {"Content-type": "application/json"})

    # 데이터를 포함한 POST 요청을 보내는 함수
    def create(self, **data):
        # 데이터를 bytes 형식으로 변환
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

        # 연결 종료
        self.connection.close()

client = ChatGPTClient(
    url="127.0.0.1",
    port=8080,
    endpoint="/create/",
)

client.create(
              model="gpt-3.5-turbo",
              messages=[
                  {"role": "user", "content": "Say this is a test."},
              ],
              stream=True,)
