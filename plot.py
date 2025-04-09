import matplotlib.pyplot as plt
import sys
import json

plt.rcParams['font.family'] = ['Roboto Mono', 'sans-serif']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 14

data = json.loads(sys.stdin.read())

labels = ['Computing Layer Groups',  'app (everything else)', 'node (node binary) ', 'node_modules (symlinks)', 'pkg_store_1p (1st party code)', 'pkg_store_3p (npm)' ]
colors = ['#0069d6', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#00d64e']

fig, ax = plt.subplots(figsize=(10, 6))
bottom = [0] * len(data)
for i, label in enumerate(labels):
    values = [data[cat][i] for cat in data]
    ax.bar(data.keys(), values, bottom=bottom, label=label, width=0.3, color=colors[i], edgecolor='black', )
    bottom = [b + v for b, v in zip(bottom, values)]

ax.set_ylabel('Time (seconds)')
ax.set_title('Cold Build (200K files / 1GB total size)')
ax.legend()
plt.savefig(sys.argv[1], dpi=300, bbox_inches='tight')
plt.close()