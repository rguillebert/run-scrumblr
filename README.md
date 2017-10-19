# run_scrumblr

run_scrumblr can be used to run multiple versions on Scrumblr in parallel.

## Installation

As run_scrumblr is just a Python 2 package, the easiest way of using it is by installing it in a python virtualenv.

run_scrumblr can be installed by running `pip install .` in the repository's root directory, the `run_scrumblr` command should then be available in the virtualenv.

## Usage

`run_scrumblr -h` `run_scrumblr run -h` and `run_scrumblr stop -h` provide documentation on the 2 available commands.

run_scrumblr has only been tested with a docker daemon running on localhost.

Each instance of Scrumblr is running its own redis instance, this behaviour can be tested by checking that any modification made to the demo board of an instance is not reflected on other instances.

## Example

```
    » run_scrumblr run https://github.com/rguillebert/scrumblr 8ef6f38faf03d3ad18b117114b1a03522eb9c82f
    Deploying commit : 8ef6f38faf03d3ad18b117114b1a03522eb9c82f
    The container is now running and available at http://localhost:32783
    You can stop this container by running run_scrumblr stop 0e50fedb-3a33-4dbc-856f-b3040bd00274

    » run_scrumblr run https://github.com/rguillebert/scrumblr 8ef6f38faf03d3ad18b117114b1a03522eb9c82f
    Deploying commit : 8ef6f38faf03d3ad18b117114b1a03522eb9c82f
    The container is now running and available at http://localhost:32784
    You can stop this container by running run_scrumblr stop d77eb631-f960-4a83-a49b-cf9cef2976e8

    » run_scrumblr run https://github.com/rguillebert/scrumblr 6efa17b790b33e9f5d2e8c88c360941ded5d6125
    Deploying commit : 6efa17b790b33e9f5d2e8c88c360941ded5d6125
    The container is now running and available at http://localhost:32785
    You can stop this container by running run_scrumblr stop c422c386-96df-40da-b6fb-ab890ab3273d

    » run_scrumblr stop c422c386-96df-40da-b6fb-ab890ab3273d
    Stopping scrumblr container
    Scrumblr container stopped
    Stopping redis container
    Redis container stopped
```
