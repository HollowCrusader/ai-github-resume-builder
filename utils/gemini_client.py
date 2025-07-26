import os
import yaml
from typing import Any, Dict
from dotenv import load_dotenv
from google import genai

class ResumeGenerator:
    """
    1. Loads GEMINI_API_KEY
    2. Reads YAML input
    3. Builds a detailed prompt
    4. Calls Gemini to generate résumé text
    """
    PROMPT_TEMPLATE = """
        You are an expert résumé writer following Harvard University style guidelines:
        - Concise header with name & contact
        - 2–3‑sentence professional summary
        - Education & certifications (if present)
        - Technical skills bullet list
        - Professional experience (company, role, dates, notes)
        - Up to five key projects (name, desc, URL, ⭐, forks)

        Keep line width ≤80 characters. Use clear headings.

        YAML input:
        ```yaml
        {yaml_content}
        ```

        Please output just the résumé in plain text."""


    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    @staticmethod
    def read_yaml(path: str) -> Dict[str, Any]:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def build_prompt(self, data: Dict[str, Any]) -> str:
        yaml_str = yaml.dump(data, sort_keys=False)
        return self.PROMPT_TEMPLATE.format(yaml_content=yaml_str)

    def generate_resume(self, yaml_path: str) -> str:
        data = self.read_yaml(yaml_path)
        prompt = self.build_prompt(data)
        response = self.client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )
        return response.text.strip()


def create_generator_from_env() -> ResumeGenerator:
    load_dotenv()
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY missing in .env")
    return ResumeGenerator(key)
