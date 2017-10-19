import argparse

from run_scrumblr.deploy import deploy_repository
from run_scrumblr.stop_container import stop_scrumblr_container

parser = argparse.ArgumentParser("Run different versions of Scrumblr in containers")
subparsers = parser.add_subparsers()

run_parser = subparsers.add_parser('run', help='Run a Scrumblr instance')
run_parser.add_argument("repository", help="Url of the git repository")
run_parser.add_argument("commit", help="Git commit of the version to be deployed")
run_parser.set_defaults(command="run")

stop_parser = subparsers.add_parser('stop', help='Stop a Scrumblr instance')
stop_parser.add_argument('container_name', help="Name of the Scrumblr instance that needs to stop")
stop_parser.set_defaults(command="stop")

def main():
    args = parser.parse_args()
    if args.command == "run":
        deploy_repository(args.repository, args.commit)
    else:
        stop_scrumblr_container(args.container_name)

if __name__ == "__main__":
    main()
