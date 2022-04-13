#!/usr/bin/env python3

from mitmproxy import http
import json


def request(flow: http.HTTPFlow):
    if flow.request.method != "POST":
        return
    if flow.request.url == "https://gaia-server.rosettastone.com/graphql":
        j = json.loads(flow.request.content.decode("ascii"))
        if j["operationName"] != "AddProgress":
            return

        i = float(input("time in hour >> "))
        j["variables"]["messages"][0]["durationMs"] = 1000*60*60*i
        flow.request.content = json.dumps(j, indent=2).encode("ascii")
        print(f"adding {i}h")
