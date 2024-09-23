def dict_formatter(data: dict, values: dict) -> dict:
    """
    formats its string values using the values from 'values' dictionary.

    Args:
        param data: (dict) with string values that may contain placeholders.
        param values: (dict) with keys corresponding to placeholders in 'data'.
        :return: A new dictionary with formatted values.
    """
    return {k: v.format(**values) if isinstance(v, str) else v for k, v in data.items()}

