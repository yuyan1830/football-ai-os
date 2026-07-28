
from .validation_result import ValidationResult


def validate_schema(data, schema):

    result = ValidationResult(
        target="schema_validation"
    )


    for field, rule in schema.items():

        if rule.get("required"):

            if field not in data:

                result.add_error(
                    "Missing field: " + field
                )


    return result

