# 0x09. Web infrastructure design
## General
This project white on a whiteboard to explain basics for web infrastructure, explain how website working indeepth from web server, application server, codebase, database, and balance loader.
## Helpful Links
* <a href="https://searchdatamanagement.techtarget.com/definition/database">What is a database</a>
* <a href="https://www.youtube.com/watch?v=S97eKyv2b9M">What’s the difference between a web server and an app server?</a>
* <a href="https://pressable.com/2019/10/11/what-are-dns-records-types-explained-2/">DNS record types</a>
* <a href="https://en.wikipedia.org/wiki/Single_point_of_failure">Single point of failure</a>
* <a href="https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header">How to avoid downtime when deploying new code</a>
* <a href="https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA714">High availability cluster (active-active/active-passive)</a>
* <a href="https://www.instantssl.com/http-vs-https">What is HTTPS</a>
* <a href="https://www.webopedia.com/definitions/firewall/">What is firewall</a>
## File Descriptions
- ``0-simple_web_stack``: a one server web infrastructure that hosts the website that is reachable via www.foobar.com. explaining the user access to website.
- ``1-distributed_web_infrastructure``: a three server web infrastructure that hosts the website www.foobar.com. explaining some specifics about this infrastructure.
- ``2-secured_and_monitored_web_infrastructure``: a three server web infrastructure that hosts the website www.foobar.com. a secured, serve encrypted traffic, and be monitored.
- ``3-scale_up``: scale up - Application server vs web server. load-balancer (HAproxy) configured as cluster.

