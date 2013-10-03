from django.db import models
from django.contrib.auth.models import User

class Forum(models.Model):
    title = models.CharField(max_length=60)
    def __unicode__(self):
        return self.title
    def threads(self):
        return self.thread_set.all()
class Thread(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum = models.ForeignKey(Forum, related_name='threads')

    def __unicode__(self):
        return unicode(self.creator) + " - " + self.title
    def posts(self):
        return self.post_set.all()
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    thread = models.ForeignKey(Thread, related_name='posts')
    body = models.TextField(max_length=10000)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.creator, self.thread, self.title)

    def short(self):
        return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))
    short.allow_tags = True
