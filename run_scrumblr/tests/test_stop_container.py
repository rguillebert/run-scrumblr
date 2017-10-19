import json

import sh

from run_scrumblr.deploy import deploy_repository
from run_scrumblr.docker import object_exists
from run_scrumblr.stop_container import stop_scrumblr_container


def is_container_running(container_name):
    container_info = json.loads(str(sh.docker.inspect(container_name)))
    return container_info[0]["State"]["Running"]


def test_deploy_repository():
    scrumblr_repository = "https://github.com/rguillebert/scrumblr"
    scrumblr_commit = "6efa17b790b33e9f5d2e8c88c360941ded5d6125"

    container_name, port = deploy_repository(scrumblr_repository, scrumblr_commit)

    assert is_container_running(container_name)

    stop_scrumblr_container(container_name)

    assert not is_container_running(container_name)
