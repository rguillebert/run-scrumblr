import tempfile
import uuid

from run_scrumblr import docker, git

def deploy_repository(repository, commit):
    """
    This is the entrypoint, start a docker container running the version of
    Scrumblr specified by the arguments
    """
    print("Deploying commit : {}".format(commit))

    repo_directory = tempfile.mkdtemp()

    docker_tag = "scrumblr:{}".format(commit)

    if not docker.object_exists(docker_tag):
        git.clone_and_checkout(repository, repo_directory, commit)
        docker.build_image(repo_directory, docker_tag)

    scrumblr_container_name = str(uuid.uuid4())

    redis_container_name = docker.run_redis_for_container(scrumblr_container_name)
    port = docker.run_scrumblr_container(docker_tag, scrumblr_container_name, redis_container_name)

    print("The container is now running and available at http://localhost:{}".format(port))

    return port
