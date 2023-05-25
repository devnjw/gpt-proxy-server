import openai
import os
from dotenv import load_dotenv
import json

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")


class ChatGPT:
    def __init__(self, **kwargs):
        openai.api_key = OPENAI_API_KEY
        self.model = kwargs.get("model", "gpt-3.5-turbo-0301")
        self.temperature = kwargs.get("temperature", 1.0)
        self.top_p = kwargs.get("top_p", 0.9)
        self.max_tokens = kwargs.get("max_tokens", 512)
        self.stream = kwargs.get("stream", False)
        self.system_prompt = ""

    def create(self, **kwargs):
        response = openai.ChatCompletion.create(
            model=kwargs.get("model", self.model),
            temperature=kwargs.get("temperature", self.temperature),
            top_p=kwargs.get("top_p", self.top_p),
            max_tokens=kwargs.get("max_tokens", self.max_tokens),
            stream=kwargs.get("stream", self.stream),
            messages=kwargs.get("messages"),
        )

        

        if not kwargs.get("stream", self.stream):
            content = response['choices'][0]['message']['content']
            yield content + "\n"
        
        else:
            full_content = ''
            for chunk in response:
                full_content += chunk['choices'][0]['delta']['content'] if 'content' in chunk['choices'][0]['delta'] else ''

                if not kwargs.get("only_content", False):
                    yield f'data: {json.dumps(chunk)}' + "\n\n"

                else:
                    content = chunk['choices'][0]['delta']['content'] if 'content' in chunk['choices'][0]['delta'] else ''
                    yield {"data": content + "\n"}
              
                if chunk['choices'][0]['finish_reason'] == 'stop':
                    yield f'data: [DONE]' + "\n\n"

            # print('full_content', full_content)
