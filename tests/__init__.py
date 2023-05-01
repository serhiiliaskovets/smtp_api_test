from cerberus import Validator


class BaseTest:

    # as we don't have API doc, we validate each field as required
    @staticmethod
    def validate_member_object(member_obj: dict) -> None:
        """
        Validates the fields and field value types of an object.

        Args:
            member_obj: dict, the object to validate.

        Raises:
            AssertionError: if any fields are missing or have the wrong value type.
        """
        schema = {
            "position": {"type": "string", "required": True},
            "level": {"type": "string", "required": True},
            "first_name": {"type": "string", "required": True},
            "last_name": {"type": "string", "required": True},
            "day_birth": {"type": "integer", "required": True},
            "hr_department": {"type": "string", "required": True},
            "email": {"type": "string", "required": True},
            "mobile": {"type": "integer", "required": True},
            "probation_period": {"type": "integer", "required": True},
            "ID": {"type": "string", "required": True},
        }

        v = Validator(schema)
        if not v.validate(member_obj):
            errors = v.errors
            error_msg = f"Validation of member data is failed: {errors}"
            raise AssertionError(error_msg)
