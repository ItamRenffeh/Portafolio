# DHCP Lab

TL;DR
Packet Tracer DHCP lab that demonstrates configuring a DHCP pool on a Cisco router, verifying bindings and client leases, and configuring DHCP relay when needed.

Summary
This lab includes a Packet Tracer project, screenshots of verification commands, and a short answer file. It demonstrates how to configure DHCP pools, exclusions, reservations, and how to verify DHCP operation from both the router and a client host.

Difficulty: Beginner–Intermediate
Estimated time: 30–60 minutes
Skills demonstrated: DHCP pool configuration, DHCP bindings verification, DHCP relay, Packet Tracer usage
Tags: DHCP, services, Packet Tracer, CCNA

Files included
- `DHCPproyect.pkt` — Packet Tracer project file.
- `Clase-M5C6-DHCP-Practica-Real-Routers.pdf` — Activity description and steps.
- `Respuesta.txt` — Short textual answers to lab questions.
- `Pc0DHCP.png`, `Router1ShowIpBinding.png` — screenshots showing client and router verification outputs.

How to open
1. Download `DHCPproyect.pkt` to your machine and open it with Cisco Packet Tracer.
2. Follow the activity PDF to understand the tasks.

Verification commands
- `show ip dhcp binding` — lists active DHCP leases on the router.
- `show running-config | section dhcp` — shows DHCP pool configuration.
- On the client: check IP assignment and default gateway.

Solution (spoiler)
A suggested solution is provided in `solutions/solution.txt` (marked as SPOILER).

What I learned
- DHCP server configuration basics on Cisco IOS.
- How to verify DHCP operation and troubleshoot common issues (missing exclusions, incorrect gateway).

Next challenges
- Add a DHCP reservation for a specific MAC address.
- Configure DHCP relay (ip helper-address) on a different subnet.

