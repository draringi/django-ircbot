from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Network(models.Model):
    server = models.CharField(max_length = 255)
    port = PositiveSmallIntegerField()
    def __unicode__(self):
        return self.server + ":" + str(self.port)

class Bot(models.Model):
    nick = models.CharField(max_length = 30, unique = True)
    nick_pass = models.CharField(blank = True)
    username = models.CharField(default = nick, max_length = 30)
    server = models.ForeignKey(Network)
    def __unicode__(self):
        return self.nick + "@" + self.server.server

class Channel(models.Model):
    name = models.CharField(max_length = 30)
    bot = models.ForeignKey(Bot)
    def __unicode__(self):
        return bot.nick + " on " + self.name

class ChannelLogEntry(models.Model):
    channel = models.ForeignKey(Channel)
    def bot(self):
        return self.channel.bot
    time = models.DateTimeField(auto_now_add=True)

class Quote(models.Model):
    submitter = models.ForeignKey(User)
    quote = models.TextField()
    submitted = models.DateTimeField(auto_now_add=True)
