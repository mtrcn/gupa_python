GUPA Python SDK
================

This repository contains the open source Python SDK that allows you to utilize the
above on your website. Except as otherwise noted, the GUPA Python SDK
is licensed under the Apache Licence, Version 2.0
(http://www.apache.org/licenses/LICENSE-2.0.html)


Usage
-----

To make [GUPA][GUPA] calls:

```python
consumer_key = 'XXXX'  
consumer_secret = 'XXXX'  
client = GUPAClient(consumer_key, consumer_secret)  
parameters = {'point': 'POINT(1000.0 1000.0)', 'distance': '121.26', 'azimuth': '168.3460'}  
response = client.access_resource(parameters, '/basic_calc/coord/')  
print response
```
			

[GUPA]: http://www.geomatikuygulamalar.com/gupa


Documentation
--------
Our [wiki] can help you develop your own application with it's rich content about GUPA APIs.

[wiki]: http://www.geomatikuygulamalar.com/wiki

Feedback
--------

File bugs or other issues [here][issues].

[issues]: http://github.com/mtrcn/gupa_python/issues