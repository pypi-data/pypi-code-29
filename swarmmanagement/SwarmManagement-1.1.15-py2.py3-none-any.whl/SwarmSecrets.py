from SwarmManagement import SwarmTools
from DockerBuildSystem import DockerSwarmTools
import sys


def GetInfoMsg():
    infoMsg = "Secrets is configured by adding a 'secrets' property to the .yaml file.\r\n"
    infoMsg += "The 'secrets' property is a dictionary of secrets.\r\n"
    infoMsg += "Each key in the secret dictionary is the secret name with a value containing the path to the secret file, as such: \r\n"
    infoMsg += "<secret_name>: <secret_file>\r\n"
    infoMsg += "Example: \r\n"
    infoMsg += "secrets: <secret_name>: <secret_file>\r\n"
    infoMsg += "Create or remove a secret by adding '-secret -c/-create <secret_name>' or 'secret -r/-remove <secret_name>' to the arguments\r\n"
    infoMsg += "Create or remove all secrets by adding '-secret -c/-create --all' or 'secret -r/-remove --all' to the arguments\r\n"
    return infoMsg


def GetSecrets(arguments):
    return SwarmTools.GetProperties(arguments, 'secrets', GetInfoMsg())


def CreateSecrets(secretsToCreate, secrets):
    for secretToCreate in secretsToCreate:
        if secretToCreate == '--all':
            for secret in secrets:
                CreateSecret(secret, secrets[secret])
        else:
            if secretToCreate in secrets:
                CreateSecret(secretToCreate, secrets[secretToCreate])


def CreateSecret(secretName, secretFile):
    DockerSwarmTools.CreateSwarmSecret(
        secretFile, secretName)


def RemoveSecrets(secretsToRemove, secrets):
    for secretToRemove in secretsToRemove:
        if secretToRemove == '--all':
            for secret in secrets:
                RemoveSecret(secret)
        else:
            if secretToRemove in secrets:
                RemoveSecret(secretToRemove)


def RemoveSecret(secretName):
    DockerSwarmTools.RemoveSwarmSecret(secretName)


def HandleSecrets(arguments):
    if len(arguments) == 0:
        return
    if not('-secret' in arguments):
        return

    if '-help' in arguments:
        print(GetInfoMsg())
        return

    secretsToCreate = SwarmTools.GetArgumentValues(arguments, '-create')
    secretsToCreate += SwarmTools.GetArgumentValues(arguments, '-c')

    secretsToRemove = SwarmTools.GetArgumentValues(arguments, '-remove')
    secretsToRemove += SwarmTools.GetArgumentValues(arguments, '-r')

    secrets = GetSecrets(arguments)

    CreateSecrets(secretsToCreate, secrets)
    RemoveSecrets(secretsToRemove, secrets)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    HandleSecrets(arguments)
