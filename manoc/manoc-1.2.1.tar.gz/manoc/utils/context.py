from manoc.utils.config import get_config


def fill_context(ctx):
    config = get_config()

    if 'common' in config.sections():
        if 'current_env' in config['common']:
            current_env = config['common']['current_env']
            if ('access_token' in config[current_env]) & ('expires_at' in config[current_env]):
                ctx.base_url = current_env
                ctx.access_token = config[current_env]['access_token']
                ctx.expires_at = config[current_env]['expires_at']
                if 'tenant' in config[current_env]:
                    ctx.tenant = config[current_env]['tenant']

