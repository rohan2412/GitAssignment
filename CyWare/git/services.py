from django.conf import settings
from CyWare.utils import process_GET_request, get_search_url
import json
from models import GitUser
from datetime import datetime


class GitService(object):

    @staticmethod
    def get_all_users():
        api_url = settings.GIT_USERS_GET_URL
        response = process_GET_request(api_url)
        return response

    @staticmethod
    def get_searched_users(search_params):
        """
        You can search users by filtering on username
        :param search_params: dictionary. Eg: {'q': 'rohanagarwal'}
        :return: api response
        """
        api_endpoint = settings.GIT_USERS_SEARCH_URL
        api_url = get_search_url(api_endpoint, search_params)
        response = process_GET_request(api_url)
        return response

    @staticmethod
    def get_users(request):
        query = request.GET.get('q', None)
        if query:
            response = GitService.get_searched_users({'q': query})
            users = json.loads(response.text)['items']
        else:
            response = GitService.get_all_users()
            users = json.loads(response.text)
        GitService.store_fetched_users(users)
        return users

    @staticmethod
    def store_fetched_users(users):
        bulk_create_list = []
        for user in users:
            try:
                obj = GitUser.objects.get(git_id=user['id'])
                for key, val in user.items():
                    if key in ['id']:
                        continue
                    setattr(obj, key, val)
                setattr(obj, 'updated_dt', datetime.now())
                obj.save()
            except GitUser.DoesNotExist:
                try:
                    user['git_id'] = user['id']
                    del user['id']
                    obj = GitUser(**user)
                    obj.full_clean()    # obj.save()
                    bulk_create_list.append(obj)
                except Exception as e:
                    print e
        GitUser.objects.bulk_create(bulk_create_list)
