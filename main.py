import urllib

import requests

import Zoom_API

if __name__ == "__main__":
    call = Zoom_API.call

    call("/videosdk/sessions")

    sessionID = "oYQwb5s/Ty+MHomQZlBFaw=="
    cmd = f"/videosdk/sessions/{sessionID}/users"
    print(cmd)
    call(cmd)