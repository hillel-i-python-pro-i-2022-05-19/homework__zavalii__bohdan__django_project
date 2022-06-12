from django.http import HttpResponse

from user_generator.services import generator_of_users
from user_generator.utils import fake


def generate_users_view(request, users_count: int = 100) -> HttpResponse:
    output_response = ''.join(
        f"""<p>
        <i>{fake.first_name()}</i> - <u>{fake.ascii_email().lower()}</u>
        </p>"""
        for _ in generator_of_users(amount_of_users=users_count)
    )
    return HttpResponse(
        f"""<p>Number of users to generate: <i>{users_count}</i></p>
        <p>{output_response}</p>"""
    )
