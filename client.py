from openai import OpenAI

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
    {"role": "system", "content": "you are poetic assistant, skilled in explaining complex programming concepts with creative flair."},
     {"role": "user", "content": "compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)