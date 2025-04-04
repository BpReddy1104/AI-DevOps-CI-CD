import openai
import os

openai.api_key = os.getenv("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")

def review_code(file_path):
    with open("C:\\Users\\bpred\\AI-DevOps-CI-CD\\AI-DevOps-CI-CD\\app.py", "r") as file:

        code = file.read()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Review this code and suggest improvements:"},
                  {"role": "user", "content": code}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print(review_code("app.py"))
