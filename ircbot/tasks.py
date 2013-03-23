from celery import task
from irc import client
from ircbot.models import Bot

@task(track_started = True)
def ircbot(bot):
    bot = Bot.objects.get(nick = bot)
    clnt = client.IRC()
    serv = clnt.server()
    set_commands(
    serv.connect(bot.server.server, bot.server.port, bot.nick)
    if bot.nick_pass:
        serv.privmsg("nickserv", "identify "+bot.nick_pass)
    for chan in bot.channel_set.all():
        serv.join(chan.name)
    clnt.process_forever()
