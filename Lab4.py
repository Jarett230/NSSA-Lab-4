import numpy as np
import matplotlib.pyplot as plt

fileNames = [
	"metrics/APM1_metrics.csv",
	"metrics/APM2_metrics.csv",
	"metrics/APM3_metrics.csv",
	"metrics/APM4_metrics.csv",
	"metrics/APM5_metrics.csv",
	"metrics/APM6_metrics.csv",
	"metrics/system_metrics.csv"
	]

colors = ["blue", "black", "red", "green", "yellow", "cyan"]

labels = ["APM1", "APM2", "APM3", "APM4", "APM5", "APM6"]

for i in range(0, len(fileNames)-1):
	CPU = np.genfromtxt(fileNames[i], delimiter=",", names=["x", "y", "z"])
	plt.plot(CPU['x'], CPU['y'], color=colors[i], label=labels[i])

plt.xlabel('Time(seconds)')
plt.ylabel('CPU(%)')
plt.title('CPU Utilization over Time')
plt.legend(loc = 'upper right')
plt.savefig("cpu.png")

plt.figure()

for i in range(0, len(fileNames)-1):
	Memory = np.genfromtxt(fileNames[i], delimiter=",", names=["x", "y", "z"])
	plt.plot(Memory['x'], Memory['z'], color=colors[i], label=labels[i])

plt.xlabel('Time(seconds)')
plt.ylabel('Memory(%)')
plt.title('Memory Utilization over Time')
plt.legend(loc = 'upper right')
plt.savefig("memory.png")

plt.figure()

system = np.genfromtxt(fileNames[6], delimiter=",", names=["Time", "RX_Data_Rate", "TX_Data_Rate", "Disk_Writes", "Disk_Capacity"])

plt.plot(system['Time'], system['RX_Data_Rate'], color="blue", label="RX_Data_Rate")
plt.plot(system['Time'], system['TX_Data_Rate'], color="green", label="TX_Data_Rate")
plt.xlabel('Time(seconds)')
plt.ylabel('Data Rate (kb/sec)')
plt.title('Network Bandwidth Utilization over Time')
plt.legend(loc = 'upper right')
plt.savefig("bandwidth.png")

plt.figure()

plt.plot(system['Time'], system['Disk_Writes'], color="blue", label="Disk_Writes")
plt.xlabel('Time(seconds)')
plt.ylabel('Disk Writes (kb/sec)')
plt.title('Hard Disk Access Rates over Time')
plt.legend(loc = 'upper right')
plt.savefig("disk_access.png")

plt.figure()

plt.plot(system['Time'], system['Disk_Capacity'], color="blue", label="Disk_Capacity")
plt.xlabel('Time(seconds)')
plt.ylabel('Disk Capacity (MB)')
plt.title('Hard Disk Utilization over Time')
plt.legend(loc = 'upper right')
plt.savefig("disk_util.png")

