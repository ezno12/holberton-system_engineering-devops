Holberton School - 0x17. Web stack debugging #4
## Description

In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it's not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed

The goal is to fix our stack so that we get to 0 failed requests. 



## File Descriptions
- `0-the_sky_is_the_limit_not.pp`: puppet file used to deploy the bug fix
---
## Author
* **Bassem Yahia** - [Github profile](https://github.com/tennin12) - [Linkedin profile](https://tn.linkedin.com/in/bassem-ben-yahia)

## License
Public Domain, no copyright protection
