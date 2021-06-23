#  Holberton School - 0x05. Processes and signals
## Description

The focus of this project is to illustrate:
* what a PID is
* what a process is
* how to find a process PID
* how to kill a process
* what a signal is
* what the 2 signals that cannot be ignored are

## Environment
* Ubuntu 14.04 LTS
* zsh 5.0.2 (x86_64-pc-linux-gnu)

## New commands / functions used:


## Helpful Links
* Linux PID:
 http://www.linfo.org/pid.html
* Linux process:
  http://www.thegeekstuff.com/2012/03/linux-processes-environment/
* Linux signal:
  http://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/

## File Descriptions
- ``0-what-is-my-pid``: displays the scripts PID
- ``1-list_your_processes``: displays a list of currently running processes
- ``2-show_your_bash_pid``: displays lines containing `bash`, making it easy to get the PID of your Bash process
- ``3-show_your_bash_pid_made_easy``: displays PID and process name of processes that contain `bash`
- ``4-to_infinity_and_beyond``: displays To infinity and beyond indefinitely with `sleep 2` between each iteration
- ``5-kill_me_now``: kills `4-to_infinity_and_beyond process` using `kill`
- ``6-kill_me_now_made_easy``: kills 4-to_infinity_and_beyond process without using `kill` or `killall`
- ``7-highlander``: displays:

		  - "To inifinity and beyond" indefinitely
		  - with `sleep 2` inbetween each iteration
		  - "I am inviincible!!!" when recieving a SIGTERM signal

- ``8-beheaded_process``: kills the process,  "7-highlander"
- ``9-process_and_pid_file``: bash script that:

			    - creates the file /var/run/holbertonscript.pid containing its PID
			    - displays 'To infinity and beyond' indefinitely
			    - displays 'I hate the kill command' when receiving a SIGTERM signal
			    - displays 'Y U no love me?!' when receiving a SIGINT signal
			    - deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
- ``10-manage_my_process``: bash ínit script that manages the `manage_my_process` script. Takes the arguments:

			   - `start`: executes the `manage_my_process`script and writes it's PID to a file
			   - `stop`: kills the `manage_my_process` script and deletes the file containing it's PID
			   - `restart`: executes `start` and `stop` effectively replacing the PID
- ``manage_my_process``: indefinitely writes 'I am alive!' to the file /tmp/my_process
- ``11-zombie.c``: creates 5 zombie processes


## Author
Bassem Ben Yahia

linkdin: https://www.linkedin.com/in/bassem-ben-yahia/

## License
Public Domain, no copyright protection
