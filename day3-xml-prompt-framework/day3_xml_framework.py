import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# System instruction
system_instruction = """
You are a resume parser.
Extract the resume information and return it in XML format.

Include:
- Name
- Mail
- Skills
Mobile Number
"""

# Sample resume content
sample_resume_text = """
Name :Pacchikolla Ravi Kiran
Mobile Number: +91 9876543210 
Mail: ravi@mail.com

Experience: GenAI Engineer Intern at Crafttechco (2026).
Built automated data validation microservices using regular expressions.

Skills: Python, JavaScript, Java.
"""


def extract_structured_payload(raw_text):

    try:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {
                    "role": "system",
                    "content": system_instruction
                },
                {
                    "role": "user",
                    "content": f"Parse this resume content:\n\n{raw_text}"
                }
            ],
            max_tokens=1000,
            temperature=0
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Operational Engine Error: {str(e)}"


if __name__ == "__main__":

    print("=== Executing Day 3 XML Extraction Framework ===")

    compiled_output = extract_structured_payload(
        sample_resume_text
    )

    print("\n=== XML Structured Output ===")
    print(compiled_output)