from run_scrumblr import docker

def stop_scrumblr_container(container_name):
    """Stop the scrumblr container along with its associated redis instance"""
    print("Stopping scrumblr container")
    docker.stop_scrumblr_container(container_name)
    print("Scrumblr container stopped")
    print("Stopping redis container")
    docker.stop_redis_container(container_name)
    print("Redis container stopped")
