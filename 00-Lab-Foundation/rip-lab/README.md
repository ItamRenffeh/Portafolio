# RIPv2 Lab

TL;DR
Packet Tracer lab to practice RIPv2 configuration and verification in a small multi-router network.

Summary
This lab includes the Packet Tracer file, the activity PDF, screenshots, and a solutions file. The goal is to configure RIPv2 on routers, verify route exchange and convergence, and troubleshoot common RIPv2 issues.

Difficulty: Beginner–Intermediate
Estimated time: 30–60 minutes
Skills demonstrated: RIPv2 configuration, route verification, basic troubleshooting, Packet Tracer usage
Tags: RIPv2, routing, Packet Tracer, CCNA

Files included
- `PracticoRip.pkt` — Packet Tracer project file.
- `Clase-M5C4-RIP-Practica-PacketTracer.pdf` — Activity description and steps.
- `Repuesta.txt` — Short textual answers to lab questions.
- `Pc1-pingPc3.png`, `Router1Table.png` — screenshots showing verification outputs.

How to open
1. Download `PracticoRip.pkt` and open it with Cisco Packet Tracer.
2. Follow the activity PDF for the tasks.

Verification commands
- `show ip route` — verify RIP learned routes (look for `R` prefix).
- `show ip protocols` — check the active routing protocols and networks advertised.
- `debug ip rip` (use cautiously) — observe RIP updates during convergence.

Solution (spoiler)
A suggested solution is provided in `solutions/solution.txt` (marked as SPOILER).

What I learned
- How RIPv2 advertises networks and the significance of hop count.
- Limitations of distance-vector protocols and scenarios where link-state (OSPF) is preferred.

Next challenges
- Introduce a route filter or passive-interface to observe changes in propagation.

License
MIT

Contact / Author
If you want changes to this README or the solution, tell me and I will update it.
