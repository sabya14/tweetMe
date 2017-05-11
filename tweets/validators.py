from django.core.exceptions import ValidationError


def validate_content(value):
    if value == "*****":
        raise ValidationError("Cannot be 5 stars")
    return value
