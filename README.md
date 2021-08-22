# Service_scan

Obtain a list of `IPs` from a LAN what have some service port opened, with `async`architecture



- Click cli
- Async architecture


## Example

Default timeout to 3 seconds.

```
(venv) ➜  service_scan git:(master) ✗ time ./cli.py 
Scanning network 192.168.2.0/24 for services on port 3389
[IPv4Address('192.168.2.148')]
./cli.py  0,13s user 0,00s system 4% cpu 3,117 total
(venv) ➜  service_scan git:(master) ✗ 
 
``
