
from cloudify import ctx
import json
from cloudify.decorators import operation
from cloudify.exceptions import NonRecoverableError
import mec_platform_client as mec_platform_client


@operation
def redirect_by_name(**kwargs):
    command = ctx.node.properties['command']
    registrar_host = ctx.node.properties['registrar_host']
    registrar_port = ctx.node.properties['registrar_port']
    registrar_service_catalogue_url = ctx.node.properties['registrar_service_catalogue_url']

    mec_platform_client.registrar_host = registrar_host
    mec_platform_client.registrar_port = registrar_port
    mec_platform_client.registrar_service_catalogue_url = registrar_service_catalogue_url
    msg = "Creating redirect by name"
    ctx.logger.info(msg)

    msg = 'REST request Host = "' + registrar_host + '"' \
                                                     ' Port = "' + registrar_port + '"' + \
          ' Url = "' + registrar_service_catalogue_url + '"' + \
          ' Command = "' + command + '"'
    ctx.logger.info(msg)
    try:
        response_str = mec_platform_client.redirect_by_name(command)

    except Exception as e:
        if str(e) == '[Errno 110] Connection timed out':
            msg = "Server " + mec_platform_client.registrar_host + \
                  " port " + str(mec_platform_client.registrar_port) + \
                  " connection timeout"
            ctx.logger.info(msg)
            msg = 'Waiting avaibility of server Host = "' + registrar_host + \
                  ' Port = "' + registrar_port
            return ctx.operation.retry(message=msg)
        else:
            raise NonRecoverableError(str(e))

    response_dict = json.loads(response_str)
    response = response_dict['RESPONSE']

    ctx.logger.info("Server response full = " + str(response))

    msg = 'Server response' \
          ' description = "' + response['description'] + '"' \
                                                         ' result = "' + str(response['result']) + '"'
    ctx.logger.info(msg)

    if response['result'] != 200:
        raise NonRecoverableError("Server returned code not 200")
    if response['description'] != 'Redirection URL added successfully':
        raise NonRecoverableError("Server returned incorrect description")


@operation
def delete_redirect_by_name(**kwargs):
    command = ctx.node.properties['command']
    registrar_host = ctx.node.properties['registrar_host']
    registrar_port = ctx.node.properties['registrar_port']
    registrar_service_catalogue_url = ctx.node.properties['registrar_service_catalogue_url']

    mec_platform_client.registrar_host = registrar_host
    mec_platform_client.registrar_port = registrar_port
    mec_platform_client.registrar_service_catalogue_url = registrar_service_catalogue_url

    msg = "Deleteing redirect by name"
    ctx.logger.info(msg)

    msg = 'REST request Host = "' + registrar_host + '"' \
                                                     ' Port = "' + registrar_port + '"' + \
          ' Url = "' + registrar_service_catalogue_url + '"' + \
          ' Command = "' + command + '"'
    ctx.logger.info(msg)
    try:
        response_str = mec_platform_client.delete_redirect_by_name(command)

    except Exception as e:
        if str(e) == '[Errno 110] Connection timed out':
            msg = "Server " + mec_platform_client.registrar_host + \
                  " port " + str(mec_platform_client.registrar_port) + \
                  " connection timeout"
            return ctx.operation.retry(message=msg)
        else:
            raise NonRecoverableError(str(e))

    response_dict = json.loads(response_str)
    response = response_dict['RESPONSE']

    ctx.logger.info("Server response full = " + str(response))

    msg = 'Server response' \
          ' description = "' + response['description'] + '"' \
                                                         ' result = "' + str(response['result']) + '"'
    ctx.logger.info(msg)

    if response['result'] != 200:
        raise NonRecoverableError("Server returned code not 200")
    if response['description'] != 'Redirection URL deleted successfully':
        raise NonRecoverableError("Server returned incorrect description")


@operation
def redirect_by_traffic(**kwargs):
    command = ctx.node.properties['command']
    registrar_host = ctx.node.properties['registrar_host']
    registrar_port = ctx.node.properties['registrar_port']
    registrar_service_catalogue_url = ctx.node.properties['registrar_service_catalogue_url']

    mec_platform_client.registrar_host = registrar_host
    mec_platform_client.registrar_port = registrar_port
    mec_platform_client.registrar_service_catalogue_url = registrar_service_catalogue_url

    msg = "Creating redirect by traffic"
    ctx.logger.info(msg)

    msg = 'REST request Host = "' + registrar_host + '"' \
                                                     ' Port = "' + registrar_port + '"' + \
          ' Url = "' + registrar_service_catalogue_url + '"' + \
          ' Command = "' + command + '"'
    ctx.logger.info(msg)
    try:
        response_str = mec_platform_client.redirect_by_traffic_type(command)

    except Exception as e:
        if (str(e) == '[Errno 110] Connection timed out'):
            msg = "Server " + mec_platform_client.registrar_host + \
                  " port " + str(mec_platform_client.registrar_port) + \
                  " connection timeout"
            return ctx.operation.retry(message=msg)
        else:
            raise NonRecoverableError(str(e))

    response_dict = json.loads(response_str)
    response = response_dict['RESPONSE']

    ctx.logger.info("Server response full = " + str(response))

    msg = 'Server response' \
          ' description = "' + response['description'] + '"' \
                                                         ' result = "' + str(response['result']) + '"'
    ctx.logger.info(msg)

    if response['result'] != 200:
        raise NonRecoverableError("Server returned code not 200")
    if response['description'] != 'Added IMSI list':
        raise NonRecoverableError("Server returned incorrect description")


@operation
def delete_redirect_by_traffic(**kwargs):
    command = ctx.node.properties['command']
    registrar_host = ctx.node.properties['registrar_host']
    registrar_port = ctx.node.properties['registrar_port']
    registrar_service_catalogue_url = ctx.node.properties['registrar_service_catalogue_url']

    mec_platform_client.registrar_host = registrar_host
    mec_platform_client.registrar_port = registrar_port
    mec_platform_client.registrar_service_catalogue_url = registrar_service_catalogue_url

    msg = "Deleteing redirect by traffic"
    ctx.logger.info(msg)

    msg = 'REST request Host = "' + registrar_host + '"' \
                                                     ' Port = "' + registrar_port + '"' + \
          ' Url = "' + registrar_service_catalogue_url + '"' + \
          ' Command = "' + command + '"'
    ctx.logger.info(msg)
    try:
        response_str = mec_platform_client.delete_redirect_by_traffic_type(command)

    except Exception as e:
        if str(e) == '[Errno 110] Connection timed out':
            msg = "Server " + mec_platform_client.registrar_host + \
                  " port " + str(mec_platform_client.registrar_port) + \
                  " connection timeout"
            return ctx.operation.retry(message=msg)
        else:
            raise NonRecoverableError(str(e))

    response_dict = json.loads(response_str)
    response = response_dict['RESPONSE']

    ctx.logger.info("Server response full = " + str(response))

    msg = 'Server response' \
          ' description = "' + response['description'] + '"' \
          ' result = "' + str(response['result']) + '"'
    ctx.logger.info(msg)

    if response['result'] != 200:
        raise NonRecoverableError("Server returned code not 200")
    if response['description'] != 'Removed redirection by service type':
        raise NonRecoverableError("Server returned incorrect description")
