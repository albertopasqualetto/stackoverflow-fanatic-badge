#!/bin/bash
# bootstrap.sh
# for use with a remote docker container running selenium grid (arm version)

trap ' ' INT

echo starting Selenium...
docker run -d --name selenium_stackoverflow_fanatic_badge --rm -it -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g seleniarm/standalone-chromium:latest

# wait-for-grid.sh
sleep 2
while ! curl -sSL "localhost:4444/wd/hub/status" 2>&1 \
        | jq -r '.value.ready' 2>&1 | grep "true" >/dev/null; do
    echo 'Waiting for the Grid'
    sleep 1
done
>&2 echo "Selenium Grid is up - executing tests"

./venv/bin/python3 main.py

echo stopping Selenium...
docker stop selenium_stackoverflow_fanatic_badge
