import json
import openai



response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "냉면의 원재료를 알려줘"
        }
    ],
    max_tokens=100,
    temperature=1,
    n=2,
)

print(json.dumps(response, indent=2, ensure_ascii=False))