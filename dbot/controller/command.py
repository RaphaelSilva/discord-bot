
from discord.ext import commands


@commands.command()
async def upload(context: commands.Context):
    '''
    TODO: send menssage to queue by context.message.id
    When the message is edited this command is not trigged
    Here we can use Celery to send a command to Queue Redis
    '''    
    print(f'''
        context.message.content={context.message.content} 
        context.message.attachments={context.message.attachments}
        context.message.channel={context.message.channel}
        context.message.position={context.message.position}
        context.message.id={context.message.id} 
    ''')