#!/usr/bin/env python3
import json
import sys


def main():
    with open(sys.argv[1], "r") as f:
        dataJ = json.load(f)
        with open(sys.argv[2], "w") as t:
            t.write("id;name;lat;long;community;status"+"\n")
            # clients;community;id;lat;long;name;status;
        with open(sys.argv[2], "a") as t:
            for entry in dataJ["allTheRouters"]:
                ID = str(entry["id"])
                Name = entry["name"]
                Lat = str(entry["lat"])
                Long = str(entry["long"])
                Community = entry["community"]
                Status = entry["status"]
                t.write(ID+";"+Name+";"+Lat+";"+Long+";"+Community+";"+Status+"\n")


if __name__ == '__main__':
    main()
