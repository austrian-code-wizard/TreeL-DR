from logging import Logger, getLogger
import re

import openai

from services.gpt3_examples import prompt_templates, email_examples
from utils import Timer


class GPT3Service:
    temperature = 0
    engine = "davinci"
    max_tokens = 300
    frequency_penalty = 0.3

    # answers_regex = r"((^|(\d\. )).+?(?=(\n\d\. )|$))"
    answers_regex = "\d\. "
    summary_max_len = 40
    max_chars_in_body = 3500

    prompt_template = prompt_templates[0]

    def __init__(self, logger: Logger = None):
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

        with Timer(self._logger, "Making open ai request"):
            response = openai.Completion.create(
                engine=self.engine, prompt=prompt, max_tokens=self.max_tokens, temperature=self.temperature, frequency_penalty=self.frequency_penalty
            )

        extraction = self._parse_response(response)
        
        return extraction

    def _validate_body(self, body):
        return body[:self.max_chars_in_body]

    def _fill_prompt(self, body):
        prompt = self.prompt_template.format(body=body)
        return prompt

    def _parse_response(self, response_object):
        res_text = response_object["choices"][0]["text"].strip()
        result = self._parse_response_text(res_text)
        return result

    def _parse_response_text(self, response_text):
        response_text = response_text.split("#####")[0].strip()
        answers = re.split(self.answers_regex, response_text)
        (
            tldr,
            category_text,
            action_needed_text,
            deadline_text,
            mentions_covid_text,
            sentiment_text,
            key_points,
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
        if len(key_points.split()) > self.summary_max_len:
            return tldr
        else:
            return key_points

    def _get_sentiment(self, sentiment_text):
        sentiment_text_low = sentiment_text.lower()
        pieces = sentiment_text_low.split("the sentiment of the email is ")
        if pieces == 1:
            return sentiment_text
        
        words = pieces[-1].split()
        return words[-1].replace(".", "")

    def _get_deadline(self, deadline_text):
        deadline_text_lower = deadline_text.lower()
        if " not" in deadline_text_lower or " no " in deadline_text_lower or "unknown" in deadline_text_lower:
            return ""
        else:
            return deadline_text

    def _get_action(self, action_text):
        if "No," in action_text:
            return ""
        else:
            return action_text.split('Yes, ')[-1]

    def _check_if_mentions_covid(self, mentions_covid_text):
        mentions_covid_text_lower = mentions_covid_text.lower()
        if "no," in mentions_covid_text_lower or "no." in mentions_covid_text_lower:
            return False

        else:
            return True

    def _get_category(self, category_text):
        category_text_low = category_text.lower()

        categories = [("event", "events"), ("job", "job_opportunities"), ("school", "school"), ("covid", "covid_updates")]

        for category in categories:
            category_term, category_name = category
            if category_term in category_text_low:
                return category_name

        return None

class TestGPT3Service:
    def __init__(self):
        self.gpt3_service = GPT3Service()

    def __call__(self):
        start_i = 2
        i = 0
        for email_name in email_examples:
            i += 1
            if i < start_i:
                continue
            
            body = email_examples[email_name]["body"]
            print(body)

            result = self.gpt3_service.get_email_attributes(body)
            print(result)
            print(f"analyzed {i}: {email_name}")
            input("continue? ")
