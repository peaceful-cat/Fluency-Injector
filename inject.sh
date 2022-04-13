#!/bin/sh

echo ">-----------Fluency-Injector-----------<"
echo Install mitmproxy
echo Trustruct certificate from ~/.mitmproxy
echo Setup HTTP/HTTPS proxy to 127.0.0.1:8080
echo Click around until prompt appears
echo Chose how much time to add
echo ">--------------------------------------<"

mitmdump -q -s ./mitm.py
