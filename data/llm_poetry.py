"""Extract poems from LLMs with API from OpenRouter"""

from openai import OpenAI


FAMOUS_POETS = [
    "William Shakespeare",      # 1564–1616
    "Emily Dickinson",          # 1830–1886
    "John Keats",               # 1795–1821
    "William Wordsworth",       # 1770–1850
    "Robert Frost",             # 1874–1963
    "Langston Hughes",          # 1902–1967
    "Sylvia Plath",             # 1932–1963
    "T.S. Eliot",               # 1888–1965
    "W.B. Yeats",               # 1865–1939
    "Pablo Neruda",             # 1904–1973
]


def get_poem(
    api_key: str,
    llm: str,
    user_prompt: str,
    system_prompt: str = "",
    temperature: float = 0.95,
) -> str:
    """Creates poem from openrouter api with given model and prompt"""
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    completion = client.chat.completions.create(
        model=llm,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=temperature,
    )
    return completion.choices[0].message.content
