# OSPF Packet Tracer Lab

TL;DR
A Packet Tracer lab that exercises OSPF configuration, verification and troubleshooting in a small multi-area network.

Summary
This mini-project contains the Packet Tracer file, the lab instructions (PDF), screenshots of verification outputs, and a short text response file. The goal is to demonstrate OSPF neighborship, correct area assignment, route propagation, and basic troubleshooting steps.

Objectives
- Configure OSPF on multiple routers.
- Verify OSPF neighbor relationships and routing tables.
- Troubleshoot common OSPF issues (misconfigured area, passive interfaces, wrong network statements).

Prerequisites
- Cisco Packet Tracer (recommended version compatible with the provided .pkt file).
- Basic knowledge of Cisco IOS and OSPF concepts (areas, networks, router IDs).

Files included
- `Ospf proyecto redes.pkt` — Packet Tracer project file.
- `Clase-M5C5-OSPF-Practica-PacketTracer.pdf` — Activity description and steps.
- `Respuesta.txt` — Short textual answers to lab questions.
- `Router1Tables.png` and `Screenshot 2026-08-25 181700.png` — screenshots showing command outputs and topology.

How to open
1. Download `Ospf proyecto redes.pkt` to your machine.
2. Open it with Cisco Packet Tracer.
3. Start simulation or real-time mode to interact with devices.
4. If devices appear shut down, power them on in the Packet Tracer GUI.

Suggested lab steps (high level)
1. Read the PDF `Clase-M5C5-OSPF-Practica-PacketTracer.pdf` to understand the tasks and the expected verification steps.
2. Open the .pkt file and inspect the topology and interface addressing.
3. On each router, enter configuration mode and add OSPF process and network statements matching the topology.
   - Example:
     - configure terminal
     - router ospf 1
     - network 10.0.0.0 0.0.0.255 area 0
4. Verify OSPF neighbor relationships and routing tables with the following commands:
   - `show ip ospf neighbor`
   - `show ip route ospf`
   - `show ip protocols`
   - `show ip route`
5. Troubleshoot any missing routes by checking interface statuses, OSPF area misassignments, and passive interfaces.

Expected verification commands and typical outputs
- `show ip ospf neighbor` — lists OSPF neighbors and states (FULL means adjacency established).
- `show ip route` — OSPF learned routes appear with an `O` prefix.
- `ping` between end hosts to validate end-to-end connectivity.

Screenshots and evidence
- `Router1Tables.png` contains examples of `show` outputs from Router1.
- `Screenshot 2026-08-25 181700.png` shows topology or additional verification evidence.

Notes on content and privacy
- The provided files appear to be classroom lab materials. Ensure you do not upload or publish real customer data or credentials. This repository keeps the original filenames; if you need me to anonymize content inside configs, I can help.

License
This lab content is provided for learning purposes. Licensed under MIT — see LICENSE in the repository (if present).

Contact / Author
If you are the author and want changes to the README or to the project structure (move to different folder, rename files, add a branch), tell me and I will update it.
