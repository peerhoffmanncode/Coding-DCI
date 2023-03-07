from .models import NewStats

from django.db.models import F


class DemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.num_requests = 0
        self.num_exceptions = 0
        self.context_response = {"msg": {"warning": "No more ink in printer..."}}

    def stats(self, os_info):
        if "windows" in os_info.lower():
            NewStats.objects.all().update(win=F("win") + 1)
        elif "mac" in os_info.lower():
            NewStats.objects.all().update(mac=F("mac") + 1)
        elif "linux" in os_info.lower():
            NewStats.objects.all().update(linux=F("linux") + 1)
        else:
            NewStats.objects.all().update(other=F("other") + 1)

            pass

    def __call__(self, request):

        self.num_requests += 1
        # print(f"Requests {self.num_requests}")
        # print(request.path)
        # print(request.headers["Host"])
        # print(request.headers["Accept-Language"])
        # print(request.META["REQUEST_METHOD"])
        # print(request.META["HTTP_USER_AGENT"])

        if "admin" not in request.path:
            self.stats(request.META["HTTP_USER_AGENT"])

        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # logic executed before a view

        print(f"View: {view_func.__name__}")

    def process_exception(self, request, exception):
        self.num_exceptions += 1

        print(f"Exception: {self.num_exceptions}")

    def process_template_response(self, request, response):
        response.context_data["new_data"] = self.context_response
        return response

    # def
