# Hybrid Security Operations Lab

## Overview
A hybrid on-premise and cloud security lab built on a physical ESXi server connected to an AWS cloud environment. Designed to simulate real-world attack scenarios and detect them using a centralized Wazuh SIEM with custom detection rules mapped to MITRE ATT&CK techniques, automated email alerts via AWS Lambda and SNS, and real attack simulation using Kali Linux.

Built during a federal cybersecurity internship at Mele Associates (May–Aug 2026).

---

## Architecture

| Component | Role |
|---|---|
| ESXi Host | Bare metal hypervisor running all on-prem VMs |
| Ubuntu Server | Attack target running SSH and Apache |
| Wazuh SIEM | Central detection brain ingesting logs from both environments |
| Kali Linux | Attacker machine generating real attacks against both environments |
| AWS EC2 | Cloud attack target with Wazuh agent reporting to on-prem SIEM |
| AWS Lambda | Receives Wazuh webhooks and publishes alerts to SNS |
| AWS SNS | Sends real-time email alerts when attacks are detected |
| Ngrok | TCP tunnel connecting EC2 Wazuh agent to on-prem Wazuh manager |

---

## Tools & Technologies

- **SIEM:** Wazuh 4.7.5
- **Hypervisor:** VMware ESXi
- **Attacker OS:** Kali Linux 2026.1
- **Attack Tools:** Nmap, Hydra, Nikto, Wireshark, Metasploit
- **Cloud:** AWS (EC2, VPC, Lambda, CloudWatch, SNS)
- **Framework:** MITRE ATT&CK

---

## Attack Scenarios

| Attack | Tool | MITRE Technique | Phase |
|---|---|---|---|
| Port scan | Nmap | T1046 | 1 and 2 |
| SSH brute force | Hydra | T1110.001 | 1 |
| Packet capture | Wireshark | T1040 | 1 |
| Web enumeration | Nikto | T1595 | 1 and 2 |
| Privilege escalation | Manual | T1548.003 | 1 |
| Backdoor user creation | Manual | T1136.001 | 1 |
| Exploitation simulation | Metasploit | T1210 | 2 |

---

## Project Status

| Milestone | Status |
|---|---|
| Ubuntu Target VM | ✅ Complete |
| Wazuh SIEM | ✅ Complete |
| Kali Linux | ✅ Complete |
| Wazuh agent on Ubuntu target | ✅ Complete |
| Custom detection rules | ✅ Complete |
| SSH brute force attack | ✅ Complete |
| Nikto web scan | ✅ Complete |
| Wireshark packet capture | ✅ Complete |
| Privilege escalation simulation | ✅ Complete |
| Backdoor user creation | ✅ Complete |
| AWS VPC and EC2 | ✅ Complete |
| EC2 Wazuh agent connected | ✅ Complete |
| Both agents active simultaneously | ✅ Complete |
| Lambda and SNS email alerts | ✅ Complete |
| Metasploit exploitation simulation | ✅ Complete |

---

## Repository Structure

- `README.md` — Project overview and status
- `attack-scenarios/` — All attack commands, tools, and MITRE mappings
- `architecture/` — Architecture diagram
- `detection-rules/` — Custom Wazuh rules and explanations
- `phase1-onprem/` — On-premise setup guide and screenshots
- `phase2-cloud/` — AWS setup guide and screenshots
- `lambda/` — Lambda function code for automated alerting

## Author
**Muhsin Abbamacha** — CS/Cybersecurity, UMBC Rising Junior
Federal Cybersecurity Intern, Mele Associates
