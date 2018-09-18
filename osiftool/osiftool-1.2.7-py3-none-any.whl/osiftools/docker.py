import docker
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

##########################################################################################

def fn_build() :

    image = client.images.build(dockerfile="Dockerfile.rpi", tag="osif/iotweek-demo-button:rpi", path=".")
    print(image)

