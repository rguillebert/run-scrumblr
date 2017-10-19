import sh

from run_scrumblr import git

def test_clone_and_checkout(tmpdir):
    scrumblr_commit = "6efa17b790b33e9f5d2e8c88c360941ded5d6125"
    git.clone_and_checkout("https://github.com/rguillebert/scrumblr", tmpdir, scrumblr_commit)
    assert str(sh.git("-C", tmpdir, "rev-parse", "HEAD")).strip() == scrumblr_commit
