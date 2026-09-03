Inter-VLAN / Static Routing & Trunks Lab
TL;DR Packet Tracer lab to configure inter-VLAN routing (SVIs or router-on-a-stick), trunking (802.1Q) and static routes to connect VLANs/subnets.

Summary This lab demonstrates VLAN creation, SVI configuration on an L3 switch (or router-on-a-stick), trunk configuration on switch ports, and static routing for inter-subnet communication. It includes the Packet Tracer project, screenshots, and a solutions file with configuration snippets and verification outputs.

Difficulty: Intermediate Estimated time: 45–90 minutes Skills demonstrated: VLANs, SVIs, 802.1Q trunking, switchport configuration, static routing, Packet Tracer Tags: inter-vlan, trunking, static-routing, Packet Tracer, CCNA

Files included

Packet Tracer project file (move to this folder and rename to intervlan_project.pkt).
Activity PDF (rename to class_intervlan_practice.pdf).
solutions/solution.txt — configuration snippets and verification outputs.
images/ (topology and command screenshots)
How to open

Download intervlan_project.pkt and open with Cisco Packet Tracer.
Follow the activity PDF to configure VLANs, trunks and static routing.
Verification commands

On switches:
show vlan brief
show interfaces trunk
show running-config interface <interface>
On L3 device / router-on-a-stick:
show ip route
show ip interface brief
show running-config | section interface vlan
From hosts: ping across VLAN boundaries to verify inter‑VLAN routing.
Solution (spoiler) See solutions/solution.txt for suggested configuration and expected outputs.

What I learned

How to design and configure SVIs and trunking for multi-VLAN networks.
How static routes can be used to interconnect isolated segments when full dynamic routing is not required.
Next challenges

Replace static routes with a dynamic routing protocol (OSPF) and compare convergence.
