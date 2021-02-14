from logging import Logger, getLogger
import re

import openai

from config import OPENAI_KEY
from data.gpt3_examples import prompt_templates, email_examples

class GPT3Service:
    temperature = 0
    engine = "davinci"
    max_tokens = 150
    frequency_penalty = 0.5

    answers_regex = r"\d\. "

    prompt_template = prompt_templates[0]

    def __init__(self, logger: Logger = None):
        openai.key = OPENAI_KEY
        if not logger:
            logger = getLogger("GPT3ServiceLogger")
        self._logger = logger

    def get_email_attributes(self, body):
        """Uses OpenAI API to analyze the email body.
        
        Args:
            body (str): body of the email to extract.

        Returns:
            dict: with the following properties:
                summary (str): summary of the email.
                category (str): category of the email.
                action_needed (str): the action that is requested from the receiver.
                sentiment (str): sentiment of the email.
                deadline (str): the deadline for the action if exists.
                mentions_covid (bool): 

        """
        body = self._validate_body(body)
        prompt = self._fill_prompt(body)

        response = openai.Completion.create(
            engine=self.engine, prompt=prompt, max_tokens=self.max_tokens, temperature=self.temperature
        )

        extraction = self._parse_response(response)
        
        return extraction

    def _validate_body(self, body):
        return body[:2500]

    def _fill_prompt(self, body):
        prompt = self.gpt3_prompt_template.format(body=body)
        return prompt

    def _parse_response(self, response_object):
        res_text = response_object["choices"][0]["text"].strip()
        result = self._parse_response_text(res_text)
        return result

    def _parse_response_text(self, response_text):
        response_text = response_text.split("#####")[0]
        answers = re.split(self.answers_regex, response_text)
        (
            tldr,
            key_points,
            category_text,
            action_needed_text,
            deadline_text,
            mentions_covid_text,
            sentiment_text,
        ) = [answer.replace("\n", "") for answer in answers]

        summary = self._get_summary(tldr, key_points)
        category = self._get_category(category_text)
        action_needed = self._get_action(action_needed_text)
        deadline = self._get_deadline(deadline_text)
        mentions_covid = self._check_if_mentions_covid(mentions_covid_text)
        sentiment = self._get_sentiment(sentiment_text)

        result = {
            "summary": summary,
            "category": category,
            "action_needed": action_needed,
            "sentiment": sentiment,
            "deadline": deadline,
            "mentions_covid": mentions_covid,
        }

        return result

    def _get_summary(self, tldr, key_points):
        if len(key_points.split()) > 40:
            return tldr
        else:
            return key_points

    def _get_sentiment(self, sentiment_text):
        return sentiment_text.split()[-1].replace(".", "")

    def _get_deadline(self, deadline_text):
        deadline_text_lower = deadline_text.lower()
        if "no," in deadline_text_lower:
            return ""

        else:
            return deadline_text_lower.split('yes, ')[-1]

    def _get_action(self, action_text):
        action_text_lower = action_text.lower()
        if "no," in action_text_lower:
            return ""

        else:
            return action_text_lower.split('yes, ')[-1]

    def _check_if_mentions_covid(self, mentions_covid_text):
        mentions_covid_text_lower = mentions_covid_text.lower()
        if "no," in mentions_covid_text_lower:
            return False

        else:
            return True

    def _get_category(self, category_text):
        category_text_low = category_text.lower()

        categories = [("event", "events"), ("job", "job_opportunities"), ("class", "school"), ("covid", "covid_updates")]

        for category in categories:
            category_term, category_name = category
            if category_term in category_text_low:
                return category_name

        return None

class TestGPT3Service:
    def __init__(self):
        self.gpt3_service = GPT3Service()

    def __call__(self):
        for email_name in email_examples:
            body = email_examples[email_name]["body"]
            result = self.gpt3_service.get_email_attributes(body)
            print(result)