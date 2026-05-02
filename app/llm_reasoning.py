from openai import OpenAI

from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_reasoning(resume, job):

    prompt = f"""
    You are an AI hiring assistant.

    Resume:
    {resume}

    Job Description:
    {job['description']}

    Explain why this candidate is a strong fit.

    Include:
    - Relevant skills
    - Technical alignment
    - Project relevance

    Keep response professional.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content