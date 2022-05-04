from django.db import models

class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, 
        db_index=True, default= 'Anonymous'
    )
    body = models.CharField(
        'body', blank=True, null=True, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        "Created DateTime", blank=True, auto_now_add=True
    )

    class Tweet(models.Model):
        # id = models.AutoField(primary_key=True)
        content = models.TextField(blank=True, null=True)
        image = models.FileField(upload_to='images/' , blank=True, null=True)
        