from fastapi import FastAPI, Request, Body
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from chatgpt import ChatGPT

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return "GPT Proxy Server is running..."


@app.post("/create/")
async def create(request: Request, data: dict = Body(...)):
    try:
        gpt = ChatGPT()
        if 'model' in data:
            gpt.model = data['model']
        if 'temperature' in data:
            gpt.temperature = data['temperature']
        if 'top_p' in data:
            gpt.top_p = data['top_p']
        if 'max_tokens' in data:
            gpt.max_tokens = data['max_tokens']
        if 'stream' in data:
            gpt.stream = data['stream']

        return StreamingResponse(gpt.create(messages=data['messages'], only_content=data.get('only_content', False)))
    except Exception as e:
        raise e


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
