from openai import OpenAI
import config
key = config.OPENAI_KEY

client = OpenAI(api_key=key)

res = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "こんにちは"},
    {"role": "user", "content": "おはよう"}
  ]
)

print(res.choices[0].message.content)