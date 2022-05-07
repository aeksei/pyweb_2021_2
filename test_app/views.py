from datetime import datetime

from django.views import View
from django.http import HttpRequest, HttpResponse


class DatetimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = datetime.now()

        return HttpResponse(now)
