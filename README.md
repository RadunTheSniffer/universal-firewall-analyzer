Hello there and welcome to my project. 

Main topic of this project is to create and test a firewall log analyzer. The API will be used to direct user after supplementing an input log. The purpose of the analyzer is to digest universal log data and find malicious activities and movements. 

We will use free tools and programs like fastapi and uvicorn.


The process will be to parse through firewall logs and match the logs with said regex, in which we will then tabulate into a visual structure for easy data viewing. 

The starting code is like this

'''python
import re
logs = [
    "2025-01-01 12:00:00 ACCEPT src=192.168.0.1 dst=10.0.0.1 proto=TCP sport=12345 dport=80",
    "01-Jan-2025 12:00:00 DROP source=192.168.0.2 destination=10.0.0.2 protocol=UDP src_port=54321 dest_port=53",
    "[2025-01-01T12:00:00Z] ALLOW 192.168.0.3 -> 10.0.0.3 [TCP] 11111 -> 22"
]

patterns = {
    "timestamp": r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}|\[\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\]",
    "action": r"ACCEPT|DROP|ALLOW|DENY",
    "source_ip": r"src(?:=|| )([\d\.]+)|source(?:=|| )([\d\.]+)|([\d\.]+) ->",
    "dest_ip": r"dst(?:=|| )([\d\.]+)|destination(?:=|| )([\d\.]+)|-> ([\d\.]+)",
    "protocol": r"proto(?:=|| )(\w+)|protocol(?:=|| )(\w+)|\[(\w+)\]",
    "source_port": r"sport(?:=|| )(\d+)|src_port(?:=|| )(\d+)|([\d]+) ->",
    "dest_port": r"dport(?:=|| )(\d+)|dest_port(?:=|| )(\d+)|-> (\d+)"
}

parsed_logs = []
for log in logs:
  parsed_data ={}
  for key, pattern in patterns.items():
    match = re.search(pattern, log)
    if match:
      parsed_data[key] = next((g for g in match.groups() if g), None)
  parsed_logs.append(parsed_data)
  print(parsed_data)
#print(parsed_logs)
'''
