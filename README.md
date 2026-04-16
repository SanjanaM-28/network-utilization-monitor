# Network Utilization Monitor using SDN (Mininet + POX)
# Author: Sanjana Medarametla - PES1UG24CS908

## Problem Statement

The aim of this project is to monitor network bandwidth utilization in a Software Defined Network (SDN) environment using Mininet and the POX controller. The controller collects flow statistics from OpenFlow switches and calculates network utilization dynamically.

---

## Objectives

* Collect byte counters from OpenFlow switches
* Estimate bandwidth usage
* Display network utilization
* Update statistics periodically

---

## Tools and Technologies Used

* Mininet
* POX Controller
* OpenFlow
* Python

---

## System Architecture

The system consists of:

* Hosts generating traffic
* OpenFlow switch forwarding packets
* POX controller monitoring flow statistics

### Workflow

1. Hosts generate traffic using ping or iperf
2. Switch forwards packets
3. Controller requests flow statistics every 5 seconds
4. Bandwidth utilization is calculated and displayed

---

## Setup and Execution Steps

### Clone POX

```bash
git clone https://github.com/noxrepo/pox.git
cd pox
```

### Create the Monitor File

Place `monitor.py` inside:

```bash
pox/ext/
```

### Run the Controller

```bash
python3 pox.py forwarding.l2_learning monitor
```

### Start Mininet

Open a new terminal and run:

```bash
sudo mn --topo single,3 --controller remote,ip=127.0.0.1,port=6633
```

---

## Test Scenarios

### Scenario 1: Low Traffic

Command:

```bash
h1 ping h2
```

Observation:

* Low utilization values were observed
* Values remained small and stable

### Scenario 2: High Traffic

Command:

```bash
iperf h1 h2
```

Observation:

* High utilization values were observed
* Large spikes occurred because iperf generates heavy traffic

---

## Bandwidth Calculation

The controller calculates utilization using:

```text
Bandwidth = (Current Bytes - Previous Bytes) / Time Interval
```

The time interval used is 5 seconds.

---

## Sample Output

### Low Traffic

```text
INFO:monitor:Port 2 -> Dest 72:ab:2f:0d:55:8b | Utilization: 89.60 Bytes/sec
INFO:monitor:Port 1 -> Dest 4a:08:bc:dc:36:0c | Utilization: 187.60 Bytes/sec
```

### High Traffic

```text
INFO:monitor:Port 1 -> Dest 5a:67:d6:e4:37:38 | Utilization: 5579890142.00 Bytes/sec
INFO:monitor:Port 2 -> Dest 7e:ee:72:67:75:11 | Utilization: 4477733.20 Bytes/sec
```

---

## Screenshots

The following screenshots are included in the screenshots/ folder:

* Mininet topology
* Low traffic output
* High traffic output

---

## Results

* Successfully monitored network utilization
* Observed lower utilization for ping traffic
* Observed significantly higher utilization for iperf traffic
* Periodic monitoring worked correctly

---

## Conclusion

This project demonstrates how SDN can be used to monitor network bandwidth dynamically. The POX controller successfully collected flow statistics and calculated utilization for different traffic conditions.

---

## References

* POX Documentation
* Mininet Documentation
* OpenFlow Documentation
