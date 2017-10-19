import sh


def object_exists(object_id):
    try:
        sh.docker.inspect(object_id)
        return True
    except sh.ErrorReturnCode_1:
        return False


def build_image(directory, tag):
    """Build the Dockerfile in "directory" and tag it with the specified tag"""
    sh.docker.build('-t', tag, directory)


def pull_image(image):
    """Pull the specified image from Docker Hub"""
    sh.docker.pull(image)


def run_redis_for_container(container_name):
    """Start the redis container for the (not yet running) container 'container_name'"""
    pull_image("redis:latest")

    redis_container_name = container_name + "_redis"
    result = sh.docker.run("-d", "--name", redis_container_name, "redis:latest")
    return str(result).strip()
