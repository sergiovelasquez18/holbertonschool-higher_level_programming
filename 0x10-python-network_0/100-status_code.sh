#!/bin/bash
# script that sends a request to a URL passed as an argument
curl -sw "%{http_code}" 
