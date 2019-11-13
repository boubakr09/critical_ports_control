## Control if ports are open to all internet on AWS

Many times peoples make mistakes leaving ports (like ssh, rdp, mysql, oracle, ...) open to all internet, which is critical especially in production environment.
To prevent this happening in your infrastructure, you can put in place a python script to control to notify your admins so that the can take action and rectify the mistake.

## Running the script

Use the [critical_port_control.py]() script to test it in your environment.

