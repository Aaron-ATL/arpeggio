from .models import Lesson


class LessonsInViews:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # sourcery skip: inline-immediately-returned-variable
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.is_authenticated:
            request.lessons = Lesson.objects.all().order_by('number')

        response = self.get_response(request)

        return response