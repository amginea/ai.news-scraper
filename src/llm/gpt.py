import os

from langchain_core.prompts import ChatPromptTemplate


def load_prompt_from_file(name: str) -> str:
    prompt_path = os.path.join(os.path.dirname(__file__),"prompts/", f"{name}.txt")
    if not os.path.exists(prompt_path):
        raise ValueError(f"Prompt file {prompt_path} not found")
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_text = f.read().strip()
    return prompt_text


def load_prompt(name: str) -> list:
    import json
    with open(os.path.join(os.path.dirname(__file__), 'prompts_config.json'), 'r', encoding='utf-8') as f:
        prompts = json.load(f)

    for prompt in prompts:
        if prompt['name'] == name:
            prompt_template = ChatPromptTemplate.from_messages([
                ("system", load_prompt_from_file(prompt['system_prompt_file_name'])), 
                ("user", load_prompt_from_file(prompt['user_prompt_file_name']))
            ])
            return prompt_template

    raise ValueError(f"Prompt with name {name} not found")

def semantic_search_prompt():
    return load_prompt("semantic_search")