import uuid

import sh

import run_scrumblr.docker
import run_scrumblr.git

def test_build_image(tmpdir):
    scrumblr_commit = "6efa17b790b33e9f5d2e8c88c360941ded5d6125"

    tag = "scrumblr:{}".format(str(uuid.uuid4()))
    assert not run_scrumblr.docker.object_exists(tag)

    run_scrumblr.git.clone_and_checkout("https://github.com/rguillebert/scrumblr", tmpdir, scrumblr_commit)
    run_scrumblr.docker.build_image(tmpdir, tag)

    assert run_scrumblr.docker.object_exists(tag)
