fog
===

A droplet health checking script.

In order to run this script, you must have an API token from DigitalOcean. You
can get one from logging in and to the API section where you will generate a
new personal access token.

From there you will need to define an environment variable in your shell like
this:
    ```export DO_TOKEN=[YOUR GENERATED KEY]```

After these steps have been completed, just fire off python fog.py.

It relies on requests for the HTTPS API request and termcolor for nice colored
output in the terminal. You can install them with:
    ```pip install requests termcolor```
