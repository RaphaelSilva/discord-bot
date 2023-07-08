import discord
from typing import Any, Coroutine

class SendVideoToYoutubeCliente(discord.Client):
    async def on_reaction_add(reaction, user):
        pass
    
    async def on_message(self, message: discord.Message):
        print(f'{message.content}')
        if message.author == self.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
            

    async def on_error(self, event_method: str, /, *args: Any, **kwargs: Any) -> Coroutine[Any, Any, None]:
        print(f'@@@ Error on {event_method}')
        return await super().on_error(event_method, *args, **kwargs)