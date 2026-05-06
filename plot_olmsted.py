import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

df = pd.read_csv('wastewater_flu_a.csv')
df = df[df['county_fips'].astype(str).str.contains('27109')]
df['sample_collect_date'] = pd.to_datetime(df['sample_collect_date'])
df['pcr_target_avg_conc'] = pd.to_numeric(df['pcr_target_avg_conc'], errors='coerce')

# Split by source/matrix since units differ
raw = df[df['sample_matrix'] == 'raw wastewater'].copy()
sludge = df[df['sample_matrix'] == 'post grit removal'].copy()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

ax1.plot(raw['sample_collect_date'], raw['pcr_target_avg_conc'], 'o-', color='steelblue')
ax1.set_ylabel('copies/L wastewater')
ax1.set_title('Influenza A — Olmsted County Wastewater (Raw)')
ax1.grid(True, alpha=0.3)

ax2.plot(sludge['sample_collect_date'], sludge['pcr_target_avg_conc'], 'o-', color='darkorange')
ax2.set_ylabel('copies/g dry sludge')
ax2.set_title('Influenza A — Olmsted County Wastewater (Sludge)')
ax2.grid(True, alpha=0.3)
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
fig.autofmt_xdate()

fig.text(0.5, 0.01, f'CDC NWSS | Generated {datetime.utcnow().strftime("%Y-%m-%d")}',
         ha='center', fontsize=8, color='gray')

plt.tight_layout()
plt.savefig('olmsted_flu_a.png', dpi=150, bbox_inches='tight')
print("Plot saved.")
