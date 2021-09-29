Holberton School - 0x15. Web stack debugging #3
## Description

The focus of this project is to learn how to debug a website that runs on wordpress. The webserver is running, but traffic receives a 500 server error.


Note: Solution 2, Using strace is less specific when trying to pinpoint the error. Solution 2, setting php to report errors helps locate the issue much more easily.


## Solution 1
1. get PID of apache2 (or child process if one exists)
   
		ps auxf

2. start an strace for the target PID

   		 strace -p <PID>

3. in another terminal, request localhost

         curl 127.0.0.1


4.  in first terminal, search for errors. In this case, strace reported missing files:


 	* /var/www/html/wp-includes/lamguages
           - class-wp-locale.phpp <------- This is the problem. typo with extra 'p'

	*  /var/www/html/
		   - .htaccess
		   - index.html
		   - index.cgi
		   - index.pl
		   - .maintenance

     * /var/www/html/wp-content/
	        - languages
			- db.php
			- object-cache.php

## Solution 2
1. Turn on php error reporting in /etc/php5/apache2/php.ini by setting:

   		 display_errors = On
		 display_start_up_errors = On

	* Make sure to turn these off afterwards if using a production server.


3. request localhost

		 curl 127.0.0.1

4. output will specify where the issue is

      Warning:  require_once(/var/www/html/wp-includes/class-wp-locale.phpp): failed to open stream: No such file or directory in /var/www/html/wp-settings.php on line 137

   	  Fatal error:  require_once(): Failed opening required '/var/www/html/wp-includes/class-wp-locale.phpp' (include_path='.:/usr/share/php:/usr/share/pear') in /var/www/html/wp-settings.php on line 137
   		 

The bug was patched using puppet resource 'file_line' *If this isn't installed, you can get it with

          puppet module install puppetlabs-stdlib --version 4.19.0

or use the 'exec' rescource to run 'sed'.


## File Descriptions
- `0-strace_is_your_friend.pp`: contains puppet code used to deploy the fix on multiple machines
- `strace.txt`: output of strace in step 2 above
---
## Author
* **Bassem Yahia** - [Github profile](https://github.com/tennin12) - [Linkedin profile](https://tn.linkedin.com/in/bassem-ben-yahia)

## License
Public Domain, no copyright protection