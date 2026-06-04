# hybrid-security-lab

Overview
A hybrid on-premise and cloud security lab built on a physical ESXi server connected to an AWS cloud environment. Designed to simulate real-world attack scenarios and detect them using a centralized Wazuh SIEM with custom detection rules mapped to MITRE ATT&CK techniques, automated IP blocking via AWS Lambda, and real-time email/SMS alerts via AWS SNS. 

Architecture
ESXi Host — bare metal hypervisor running all on-prem VMs
Ubuntu Server — attack target running SSH and Apache
Wazuh SIEM — central detection brain ingesting logs from both on-prem and cloud
Kali Linux — attacker machine generating real attacks against both environments
AWS EC2 — cloud attack target with Wazuh agent reporting back to on-prem SIEM
AWS Lambda — automatically blocks attacking IPs at the security group level
AWS SNS — sends real-time SMS alert to phone when attack is detected

Tools & Technologies
Wazuh SIEM
VMware ESXi
Kali Linux
Nmap, Nikto, John the Ripper, Metasploit
AWS (EC2, VPC, Lambda, CloudWatch, SNS)
MITRE ATT&CK Framework

Repository Structure
hybrid-security-lab/
├── README.md
├── architecture/
├── phase1-onprem/
├── phase2-cloud/
├── detection-rules/
├── attack-scenarios/
└── lambda/

Muhsin Abbamacha | CS/Cybersecurity, UMBC
Cybersecurity Intern, MELE Associates Inc
