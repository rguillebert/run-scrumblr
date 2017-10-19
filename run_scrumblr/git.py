import sh

def clone_and_checkout(repository, destination, commit):
    "Clone a given git repository to destination and checkout the specified commit"
    sh.git.clone(repository, destination)
    sh.git("-C", destination, "checkout", commit)
