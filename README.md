# wise-old-man-updater

A utility to update [Wise Old Man](https://www.wiseoldman.net/) group competitions.


## About
Requires `docker-compose`. All other dependencies are encapsulated as everything runs in a container.


### Run the application
`./bin/run.sh` or `docker-compose run --rm updater`.

### Run tests
`./bin/test.sh` or `docker-compose run --rm test`.

### Update dependencies
Python dependencies are managed with `pip-tools` to ensure builds are reproducible.
Do not manually modify `requirements.txt`. Set logical dependencies in `requirements.in`.

Generate `requirements.txt` with `./bin/generate-dependencies.sh` or `docker-compose run --rm generate-dependencies`.
