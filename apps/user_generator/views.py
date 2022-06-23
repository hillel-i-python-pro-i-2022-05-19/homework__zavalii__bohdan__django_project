from django.http import HttpResponse

from apps.user_generator.services import generator_of_users


def generate_users_view(request, users_count: int = 100) -> HttpResponse:
    output_response = ''.join(
        f"""<p>
        {user.name} - {user.unique_email_address}</p>"""
        for user in generator_of_users(amount_of_users=users_count)
    )
    return HttpResponse(
        f"""<p>Number of users to generate: {users_count}</p>
        <p>{output_response}</p>"""
    )
