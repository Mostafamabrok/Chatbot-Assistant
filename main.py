from openai import OpenAI
client = OpenAI(api_key="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")

def send_to_gpt(sysprompt ,prompt):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
     messages=[
        {"role": "system", "content": sysprompt},
        {"role": "user", "content": prompt}
     ]
    )

    return completion.choices[0].message.content

print()