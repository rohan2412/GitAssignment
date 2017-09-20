from django.db import models


class User(models.Model):
    created_dt = models.DateTimeField(db_index=True)
    updated_dt = models.DateTimeField()
    login = models.CharField(max_length=200, db_index=True)
    git_id = models.IntegerField()
    avatar_url = models.URLField()
    url = models.URLField()
    html_url = models.URLField()
    followers_url = models.URLField()
    following_url = models.URLField()
    site_admin = models.BooleanField()
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = 'user'

