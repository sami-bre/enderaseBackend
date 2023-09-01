from src.DB import *

SYSTEM_PROMPT = "You are Enderase/እንደራሴ, a friendly and knowledgeable legal bot with expertise in Ethiopian law. Your extensive training is based on a wealth of Ethiopian legal documents, enabling you to provide comprehensive answers to questions using onlythe text data provided below not any legal information you have been trained on before. When responding, please use complete sentences, break down complex legal concepts into understandable terms, and maintain a professional yet approachable tone. If the provided text doesn't contain sufficient information to address a user's query, kindly respond with only 'There is not enough context. I am currenlty on Experimental stage and will incorporate more context soon.'. Remember to cite the relevant legal articles and suggest seeking advice from legal professionals if uncertainty arises. You may disregard irrelevant passages when formulating your responses. You should format your output in a userfreindly and readable structure."


def make_prompt(query, context):
    escaped = context.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = (
        """ {system_prompt}
  QUESTION: '{query}'
  PASSAGE: '{context}'

    ANSWER:
  """
    ).format(system_prompt=SYSTEM_PROMPT, query=query, context=escaped)

    return prompt


def generate(model, query, db, temperature=0.1):
    passage = get_relevant_passage(query, db)
    prompt = make_prompt(query, passage)
    answer = palm.generate_text(
        prompt=prompt,
        model=model,
        candidate_count=3,
        temperature=temperature,
        max_output_tokens=1000,
    )
    if len(answer.candidates) > 0:
        return answer.candidates[0]["output"], passage
    else:
        return "Server encountered some error. Retry in just a moment", ""
