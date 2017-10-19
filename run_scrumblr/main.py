import argparse

from run_scrumblr.deploy import deploy_repository

parser = argparse.ArgumentParser("Run different versions of Scrumblr in containers")
parser.add_argument("repository", help="Url of the git repository")
parser.add_argument("commit", help="Git commit of the version to be deployed")

def main():
    args = parser.parse_args()
    deploy_repository(args.repository, args.commit)

if __name__ == "__main__":
    main()
