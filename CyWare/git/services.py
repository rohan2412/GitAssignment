from django.conf import settings
from CyWare.utils import process_GET_request, get_search_url
import json
from models import GitUser
from datetime import datetime
from django.core.exceptions import ValidationError
from django.db import IntegrityError
import logging


logger = logging.getLogger('Logging')


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
                try:
                    obj = GitUser.objects.get(git_id=user['id'])
                    git_id = user.pop('id')
                    for key, val in user.items():
                        setattr(obj, key, val)
                    user['id'] = git_id
                    setattr(obj, 'updated_dt', datetime.now())
                    try:
                        obj.save()
                    except IntegrityError as e:
                        logger.error('Failed to load into database|User|%s|Error|%s'
                                     % (user['login'], e))
                except GitUser.DoesNotExist:
                    # logger.info('New User|%s' % user['login'])

                    user['git_id'] = user.pop('id')
                    obj = GitUser(**user)
                    user['id'] = user.pop('git_id')
                    try:
                        obj.full_clean()
                        bulk_create_list.append(obj)
                    except ValidationError as e:
                        logger.error('Failed to load into database|User|%s|Error|%s'
                                     % (user['login'], e))
            except KeyError as e:
                logger.critical('Missing Fields|User|%s' % e)
        GitUser.objects.bulk_create(bulk_create_list)
