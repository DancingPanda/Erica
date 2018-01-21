from discord.ext import commands
import logging
import random

logger = logging.getLogger(__name__)


class Basic():
    """
    This Category contains Erica's basic functionality.
    """

    ASK_ANSWERS = {
        "1": "Yes! Definitely",
        "2": "I think so, but I'm not completely sure. You better ask my brother!",
        "3": "I don't think so. You better ask Lucas!",
        "4": "Shut your mouth, nerd!",
        "5": "Nope!"
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def repeat(self, times, *message):
        """Repeats a message by speaking out loudly
        :param times: the number of times the message needs to be repeated.
        :param the message: the message to be repeated.
        """
        try:
            times = int(times)
            times = min(times, 20)  # repeat at maximum 20 times

            for i in range(int(times)):
                await self.bot.say(" ".join(message), tts=True)
        except ValueError:
            logger.info("Time in repeat command must be integer")

    @commands.command()
    async def ask(self, *question):
        """Try Erica Magic 8 Ball
        :param question: the question asked.
        """

        if "?" not in " ".join(question):
            await self.bot.say("That's not a question, fella!")
        answer = self.ASK_ANSWERS.get(str(random.randint(1, len(self.ASK_ANSWERS))))
        await self.bot.say(answer)


def setup(bot):
    """
    This method is needed for this extension to be loaded properly.
    """
    bot.add_cog(Basic(bot))