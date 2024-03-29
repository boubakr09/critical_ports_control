## Control if ports are open to all internet on AWS

Many times peoples make mistakes leaving ports (like ssh, rdp, mysql, oracle, ...) open to all internet, which is critical especially in production environment.
To prevent this happening in your infrastructure, you can put in place a python script to control and notify your admins so that the can take action and rectify the mistake.

## Running the script

Use the [critical_port_control.py](https://github.com/boubakr09/critical_ports_control/blob/master/critical_ports_control.py) script to test it in your environment.

Run the bellow command:

```
python3 critical_ports_control.py
```

PS: Assign value to the variable 'endpoint' into this [file](https://github.com/boubakr09/critical_ports_control/blob/master/critical_ports_control.py) before running the script. The value must be an email address of the subscriber to the SNS topic.

