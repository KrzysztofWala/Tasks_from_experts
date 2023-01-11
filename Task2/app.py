import os
import logging
import sys
import time

def main():
    """Main function of module."""
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    log = logging.getLogger('my_first_docker_app')
    while True:
        log.info('It works, it will go to the next iteration in 5s.')
        for k,v in os.environ.items():
            print(k,v)
        time.sleep(5)


if __name__ == "__main__":
    sys.exit(main())
    