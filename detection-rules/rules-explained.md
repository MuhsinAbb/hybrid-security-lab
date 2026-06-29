# Custom Detection Rules

## Overview
Four custom detection rules were written and deployed to the Wazuh manager at /var/ossec/etc/rules/local_rules.xml. Each rule maps to a specific MITRE ATT&CK technique and builds on top of Wazuh's built-in ruleset using composite rule logic.

---

## Rule 100001 — SSH Brute Force (T1110.001)

xml
<group name="linux,authentication_failed,">
  <rule id="100001" level="12" frequency="5" timeframe="120">
    <if_matched_sid>5760</if_matched_sid>
    <description>SSH brute force attack detected</description>
    <mitre><id>T1110.001</id></mitre>
  </rule>
</group>


**What it does:** Watches for Wazuh's built-in rule 5760 (SSH authentication failure) to fire 5 times within 120 seconds from the same source IP. When the threshold is met the rule fires at level 12 — high severity.

**Why level 12:** Level 12 is high severity in Wazuh. One failed SSH login is normal. Five in two minutes is an attack. The frequency and timeframe thresholds filter out false positives while catching real brute force attempts.

**MITRE mapping:** T1110.001 — Brute Force: Password Guessing. Attackers use automated tools like Hydra to try thousands of passwords against SSH services.

**Confirmed working:** Rule fired during Hydra brute force attack generating 253 alerts.

---

## Rule 100002 — Port Scan / Web Enumeration (T1046)

xml
<group name="linux,network,scan,">
  <rule id="100002" level="10" frequency="10" timeframe="60">
    <if_matched_sid>31101</if_matched_sid>
    <same_source_ip/>
    <description>Port scan detected - possible reconnaissance</description>
    <mitre><id>T1046</id></mitre>
  </rule>
</group>


**What it does:** Watches for rule 31101 (web server 400 error) to fire 10 times within 60 seconds from the same source IP. The same_source_ip tag ensures the hits are counted per attacker IP rather than globally.

**Why 31101:** Originally designed to watch for rule 40101 (Snort/Suricata network scan detection) but was updated to use 31101 since Suricata was not installed. Rule 31101 fires when web server enumeration tools like Nmap and Nikto generate 400 errors against Apache.

**MITRE mapping:** T1046 — Network Service Discovery. Attackers scan for open ports and services before launching targeted attacks.

**Confirmed working:** Rule fired during Nikto web scan. Tagged T1046 Discovery in the Wazuh dashboard.

---

## Rule 100003 — Privilege Escalation (T1548.003)

xml
<group name="linux,privilege_escalation,">
  <rule id="100003" level="10" frequency="3" timeframe="60">
    <if_matched_sid>5402</if_matched_sid>
    <description>Multiple sudo failures - possible privilege escalation</description>
    <mitre><id>T1548.003</id></mitre>
  </rule>
</group>


**What it does:** Watches for rule 5402 (sudo command execution) to fire 3 times within 60 seconds. Designed to catch attackers repeatedly attempting to escalate privileges using sudo after gaining initial access.

**Note:** Rule 5402 also fires on successful sudo execution. In testing the built-in rule 5402 caught privilege escalation activity and tagged it T1548.003 directly. The custom rule adds an additional composite layer for rapid repeated attempts.

**MITRE mapping:** T1548.003 — Abuse Elevation Control Mechanism: Sudo and Sudo Caching. Attackers attempt to gain root access by exploiting sudo configurations.

---

## Rule 100004 — New User Created (T1136.001)

xml
<group name="linux,persistence,">
  <rule id="100004" level="8">
    <if_sid>5901</if_sid>
    <description>New user account created - possible persistence</description>
    <mitre><id>T1136.001</id></mitre>
  </rule>
</group>


**What it does:** Fires immediately when rule 5901 (new user account created) triggers on any monitored system. No frequency threshold needed — any new user creation is suspicious in a production environment and warrants investigation.

**Why level 8:** Medium-high severity. New user creation is not always malicious but is a common persistence technique attackers use to maintain access even after their initial entry point is closed.

**MITRE mapping:** T1136.001 — Create Account: Local Account. Attackers create new user accounts to maintain persistent access to compromised systems.

**Confirmed working:** Rule fired immediately when backdoor user was created using useradd. Tagged T1136.001 Persistence in the Wazuh dashboard.

---

## Deployment

Rules are stored at:
/var/ossec/etc/rules/local_rules.xml

To deploy after editing:
sudo systemctl restart wazuh-manager

To verify syntax:
sudo /var/ossec/bin/ossec-logtest

---

## Rule ID Reference

| Rule ID | Description | Parent Rule | MITRE | Level |
|---|---|---|---|---|
| 100001 | SSH Brute Force | 5760 | T1110.001 | 12 |
| 100002 | Port Scan | 31101 | T1046 | 10 |
| 100003 | Privilege Escalation | 5402 | T1548.003 | 10 |
| 100004 | New User Created | 5901 | T1136.001 | 8 |
