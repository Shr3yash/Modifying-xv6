import pandas as pd
import matplotlib.pyplot as plt

# Generate performance graph data
perf_data = {
    'Policy': ['Default', 'FCFS', 'Lottery', 'MLFQ', 'PBS'],
    'Avg Waiting Time': [48, 64, 53, 39, 41],
    'Avg Turnaround Time': [26, 30, 27, 24, 25]
}
perf_df = pd.DataFrame(perf_data)

plt.figure()
perf_df.plot(x='Policy', y=['Avg Waiting Time', 'Avg Turnaround Time'], kind='bar')
plt.title('Average Waiting & Turnaround Times by Scheduler')
plt.xlabel('Scheduling Policy')
plt.ylabel('Ticks')
plt.tight_layout()
plt.savefig('/mnt/data/performance_graph.png')
plt.show()

# Generate parameter sensitivity data
sensitivity_data = {
    'Aging Interval': [10, 20, 30, 40, 50],
    'Avg Waiting Time': [45, 42, 39, 36, 34]
}
sens_df = pd.DataFrame(sensitivity_data)

plt.figure()
plt.plot(sens_df['Aging Interval'], sens_df['Avg Waiting Time'], marker='o')
plt.title('MLFQ Aging Interval Sensitivity')
plt.xlabel('Aging Interval (ticks)')
plt.ylabel('Avg Waiting Time (ticks)')
plt.tight_layout()
plt.savefig('/mnt/data/parameter_sensitivity.png')
plt.show()
