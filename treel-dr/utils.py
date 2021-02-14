from typing import Dict, List

def remove_none_from_dict(data: Dict):
    new_data = data.copy()
    for key in data:
        if data[key] == None:
            del new_data[key]
    return new_data

def remove_none_from_list(data: List):
    return [val for val in data if val is not None]

def clean_phone_number(number: str):
    cleaned_number = "".join([char for char in number if char.isnumeric()])
    if number[0] == "+":
        cleaned_number = "+" + cleaned_number
    return cleaned_number