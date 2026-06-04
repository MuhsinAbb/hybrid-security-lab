# Hybrid Security Operations Lab

## Overview
A hybrid on-premise and cloud security lab built on a physical ESXi server connected to an AWS cloud environment. Designed to simulate real-world attack scenarios and detect them using a centralized Wazuh SIEM with custom detection rules mapped to MITRE ATT&CK techniques, automated IP blocking via AWS Lambda, and real-time SMS alerts via AWS SNS.

Built during a cybersecurity internship at Mele Associates.

---

## Architecture
| Component | Role |
|---|---|
| ESXi Host | Bare metal hypervisor running all on-prem VMs |
| Ubuntu Server | Attack target running SSH and Apache |
| Wazuh SIEM | Central detection brain ingesting logs from both environments |
| Kali Linux | Attacker machine generating real attacks |
| AWS EC2 | Cloud attack target with Wazuh agent reporting to on-prem SIEM |
| AWS Lambda | Automatically blocks attacking IPs at the security group level |
| AWS SNS | Sends real-time SMS alert to phone when attack is detected |

---

## Tools & Technologies
- **SIEM:** Wazuh
- **Hypervisor:** VMware ESXi
- **Attacker:** Kali Linux
- **Attack Tools:** Nmap, Nikto, John the Ripper, Metasploit
- **Cloud:** AWS (EC2, VPC, Lambda, CloudWatch, SNS)
- **Framework:** MITRE ATT&CK

---

## Attack Scenarios
| Attack | Tool | MITRE Technique |
|---|---|---|
| Port scan | Nmap | T1046 |
| SSH brute force | Hydra | T1110.001 |
| Credential dumping | John the Ripper | T1003 |
| Web enumeration | Nikto | T1595 |
| Exploitation | Metasploit | T1210 |
| Privilege escalation | Manual | T1548.003 |
| Backdoor user creation | Manual | T1136.001 |

---

## Project Status
| Milestone | Status |
|---|---|
| Ubuntu Target VM | Complete |
| Wazuh SIEM | Complete |
| Kali Linux | In Progress |
| Wazuh agent on Ubuntu target | In Progress |
| AWS cloud environment | Phase 2 |
| Lambda + SNS alerts | Phase 2 |

---

## Repository Structure
