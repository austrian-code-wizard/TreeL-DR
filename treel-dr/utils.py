def remove_none_from_dict(data: dict):
    new_data = data.copy()
    for key in data:
        if data[key] == None:
            del new_data[key]
    return new_data