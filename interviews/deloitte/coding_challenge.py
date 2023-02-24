from django.http import HttpResponse, HttpResponseForbidden
import re


FIRST_NAME_VALIDATION_MESSAGE = (
    "First name should only contain characters and numbers without any "
    "spaces or special characters"
)
LAST_NAME_VALIDATION_MESSAGE = (
    "Last name should only contain characters and numbers "
    "without any spaces or special characters"
)
PHONE_VALIDATION_MESSAGE = "Phone number should only contain numbers and should have a maximum length of 10 digits"
EMAIL_VALIDATION_MESSAGE = (
    "Invalid email. Email should have the format: example@domain.com"
)


def verify_params(first_name, last_name, phone, email):
    errors = []

    if not first_name or not re.match("^[A-Za-z0-9]*$", first_name):
        errors.append(FIRST_NAME_VALIDATION_MESSAGE)

    if not last_name or not re.match("^[A-Za-z0-9]*$", last_name):
        errors.append(LAST_NAME_VALIDATION_MESSAGE)

    if not phone or len(phone) > 10 or not phone.isalnum():
        errors.append(PHONE_VALIDATION_MESSAGE)

    if not email or not re.fullmatch(
        r"\b[A-Za-z0-9_*&^%$#!~?]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,7}\b", email
    ):
        errors.append(EMAIL_VALIDATION_MESSAGE)

    return errors


def test_view(request):
    if request.method == "POST":
        data = dict(request.POST)

        first_name = str(data.get("first_name"))
        last_name = str(data.get("last_name"))
        phone = str(data.get("phone"))
        email = str(data.get("email"))
        errors = verify_params(first_name, last_name, phone, email)

        if errors:
            respone_error = "\n".join(errors)
            return HttpResponse(respone_error)

        return HttpResponse("Your data is valid")

    if request.method == "GET":
        return HttpResponse("This is a get Request")

    response = HttpResponse("")
    response.status_code = 405
    return response
