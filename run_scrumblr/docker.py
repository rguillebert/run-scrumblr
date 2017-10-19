import json

import sh


def object_exists(object_id):
    try:
        sh.docker.inspect(object_id)
        return True
    except sh.ErrorReturnCode_1:
        return False


def inspect(object_id):
    return json.loads(str(sh.docker.inspect(object_id)))[0]


def build_image(directory, tag):
    """Build the Dockerfile in "directory" and tag it with the specified tag"""
    sh.docker.build('-t', tag, directory)


def pull_image(image):
    """Pull the specified image from Docker Hub"""
    sh.docker.pull(image)


def stop_container(container_name):
    """Stops a running docker container"""
    sh.docker.stop(container_name)


def run_redis_for_container(container_name):
    """Start the redis container for the (not yet running) container
    'container_name' and return the container_id"""
    pull_image("redis:latest")

    redis_container_name = container_name + "_redis"
    result = sh.docker.run("-d", "--name", redis_container_name, "redis:latest")
    return str(result).strip()


def run_scrumblr_container(tag, container_name, redis_container_name):
    """Start the scrumblr container specified by tag, link it with redis, and
    return the port on which the host can reach the server"""
    result = sh.docker.run(
        "-d", "-P",
        "--link", "{}:redis".format(redis_container_name),
        "--name", container_name,
        tag
    )

    container_id = str(result).strip()

    container_info = inspect(container_id)
    return container_info['NetworkSettings']['Ports']['80/tcp'][0]['HostPort']


def stop_scrumblr_container(scrumblr_container_name):
    """Stop a running scrumblr container"""
    stop_container(scrumblr_container_name)


def stop_redis_container(scrumblr_container_name):
    """Stop a running redis container associated with a scrumblr one"""
    container_name = scrumblr_container_name + "_redis"
    stop_container(container_name)
