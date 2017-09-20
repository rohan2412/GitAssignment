from django.db import models
from datetime import datetime


class GitUser(models.Model):
    created_dt = models.DateTimeField(default=datetime.now())
    updated_dt = models.DateTimeField(default=datetime.now())
    login = models.CharField(max_length=200)
    git_id = models.IntegerField(unique=True)
    avatar_url = models.URLField()
    gravatar_id = models.CharField(max_length=200, blank=True)
    url = models.URLField()
    html_url = models.URLField()
    followers_url = models.URLField()
    following_url = models.URLField()
    gists_url = models.URLField()
    starred_url = models.URLField()
    subscriptions_url = models.URLField()
    organizations_url = models.URLField()
    repos_url = models.URLField()
    events_url = models.URLField()
    received_events_url = models.URLField()
    type = models.CharField(max_length=50, default='User')
    site_admin = models.BooleanField(default=False)
    score = models.FloatField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'user'
