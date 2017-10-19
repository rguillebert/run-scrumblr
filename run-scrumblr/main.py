import argparse

parser = argparse.ArgumentParser("Run different versions of Scrumblr in containers")
parser.add_argument("repository", help="Url of the git repository")
parser.add_argument("commit", help="Git commit of the version to be deployed")

def main():
    args = parser.parse_args()
    print args

if __name__ == "__main__":
    main()
