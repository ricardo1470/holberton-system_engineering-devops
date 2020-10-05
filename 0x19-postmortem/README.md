> # 0x19-postmortem
---
<center><a href="url"><img src="https://pbs.twimg.com/media/D71yyZAWkAAPRbb.jpg" width="480" height="360"></a></center>
---
The following is the incident report of the WEB infrastructure outage that occurred on `September 30, 2020`. We understand that this service issue has affected our valued developers and users, and we apologize to everyone who saw it. affected.

From `8:00 a.m. at 11:58 a.m. PCT`, the `website` entries resulted in `200 error response messages`. The services that depended on this website also showed an interruption in their services.
the user interface did not allow any action and only showed code errors, At its peak, `the problem affected 100% of the traffic to this infrastructure`.

## The following events took place September 30, 2020:

* Timeline (all hours, Pacific time)
  * 8:00 AM: Configuration insertion begins.
  * 8:16 AM: Interruption begins.
  * 8:26 AM: Pagers alerted teams.
  * 9:24 AM: Configuration change rollback failed.
  * 10:35 Am: successful rollback of configuration change.
  * 11:19 AM: Server restarts begin.
  * 11:58 AM: 100% of traffic is back online.

## Apparent reason

A badly installed update of the WEB server client was corrupting the data query that is sent to the DataBaseServer

## Root cause

At `8:00 AM PST`, a website update was inadvertently released with some new functionality which impacted the setup to our production environment without first being released to the test environment. The change specified an invalid address for the production authentication servers. this caused the internal monitoring systems to be permanently blocked. the configuration error caused all service threads to be quickly consumed. Traffic was permanently queued waiting for a posting thread to become available. The servers began to hang and restart repeatedly while trying to recover and, at 8:00 am. Pacific Time, the outage began.

## Resolution and recovery

At `8:26 a.m. PST`, the monitoring systems alerted our engineers, who investigated and quickly escalated the problem. At `9:40 am`, the incident response team identified that the update that did not go through the sandbox was causing the critical error.

At `9:24 am`, we tried to reverse the problematic configuration change. This rollback failed due to the complexity of the configuration system that caused our security checks to reject the rollback. These issues were fixed and successfully reversed at `10:35 am`.

Some services began to recover slowly and we determined that the overall recovery would be faster by restarting all the WEB infrastructure servers. To help with the recovery, we turned off some of our monitoring systems that were causing the error. At `11:19 am`, `25%` of the traffic was restored and `100%` of the traffic was routed to the WEB infrastructure at `11:58 am`.

## Corrective and preventive measures

In the last two days, we have conducted an internal review and analysis of the outage. The following are actions we are taking to address the underlying causes of the problem and help prevent recurrence and improve response times:

* Deactivate the release mechanism from the current configuration until more secure measures are implemented. (Finished.)
* Change the rollback process to be faster and more robust.
* Programmatically apply the staged releases of all configuration changes.
* Improve the process to audit all high-risk configuration options.

---
> ## contact 💬

| [twitter](https://twitter.com/RICARDO1470) | [linkedin](https://www.linkedin.com/in/ricardo-alfonso-camayo/) | [mail](1466@holbertonschool.com) | [github](https://github.com/ricardo1470/README/blob/master/README.md) |
|---|---|---|---|

---

## License
*`postmortem` is open source and therefore free to download and use without permission.*

<a href="url"><img src="https://www.holbertonschool.com/holberton-logo.png" align="middle" width="100" height="30"></a>

---