#! /usr/bin/bash

# Requires curl && jq (obviously)

curl --silent --header "Accept: application/json" https://icanhazdadjoke.com/ | jq '.joke'
