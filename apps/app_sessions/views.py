from typing import ClassVar, Any

from django.views.generic import TemplateView


class SessionView(TemplateView):
    template_name = "app_sessions/index.html"

    # LAST_VISIT = datetime.datetime.now().strftime("%Y-%m-%d: %H:%M")
    COUNT_OF_VISITS: ClassVar[str] = "count_of_visits"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        session = self.request.session

        count_of_visits = session.get(self.COUNT_OF_VISITS, 0)
        count_of_visits += 1
        session[self.COUNT_OF_VISITS] = count_of_visits

        kwargs[self.COUNT_OF_VISITS] = count_of_visits
        kwargs["session_id"] = session.session_key
        return kwargs
