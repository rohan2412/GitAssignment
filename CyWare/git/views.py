from django.views.generic import TemplateView
from django.template.response import TemplateResponse

from services import GitService


class UsersView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = {}
        git_users = GitService.get_users(request)
        context['users'] = git_users
        return TemplateResponse(request=request,
                                template=self.template_name,
                                context=context)
