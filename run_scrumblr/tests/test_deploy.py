from run_scrumblr.deploy import deploy_repository

def test_deploy_repository():
    scrumblr_repository = "https://github.com/rguillebert/scrumblr"
    scrumblr_commit = "6efa17b790b33e9f5d2e8c88c360941ded5d6125"

    port = deploy_repository(scrumblr_repository, scrumblr_commit)

    assert int(port)
