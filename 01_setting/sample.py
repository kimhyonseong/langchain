import json
import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "iphone8 출시일을 알려주세요"
        }
    ]
)

print(json.dumps(response, indent=2, ensure_ascii=False))