from matplotlib import pyplot as plt
from data import DataLoader, DataPath
from pathlib import Path

data_loader = DataLoader(Path(__file__).parent.parent / "data" / "main.json")

# Grafieken:
# twee stack diagrammen per reden, geldig en ongeldig. Leeftijd?
# een pie diagram per reden of geldig en ongeldig?
# 3 pie-diagrammen per sport participatie, kijkcijfers en totaal. Daarnaast zonder 'ongeldige' redenen?

all_sports = data_loader.get_keys(DataPath(DataPath.Any, "sports", DataPath.Any))
all_sports = list(set(all_sports))

total_hours = []
total_labels = []
participation_hours = []
participation_labels = []
media_hours = []
media_labels = []

for sport in all_sports:
    both = sum(data_loader.get(DataPath(DataPath.Any, "sports", DataPath.Any, sport, "hours")))
    if both != 0:
        total_hours.append(both)
        total_labels.append(sport)

    participation = sum(data_loader.get(DataPath(DataPath.Any, "sports", "participation", sport, "hours")))
    if participation != 0:
        participation_hours.append(participation)
        participation_labels.append(sport)

    media = sum(data_loader.get(DataPath(DataPath.Any, "sports", "media", sport, "hours")))
    if media != 0:
        media_hours.append(media)
        media_labels.append(sport)


fig, axs = plt.subplots(1,3)
axs[0].set_title("Totaal")
axs[0].pie(x=total_hours, labels=total_labels)
axs[1].set_title("Participatie")
axs[1].pie(x=participation_hours, labels=participation_labels)
axs[2].set_title("Kijkcijfers")
axs[2].pie(x=media_hours, labels=media_labels)

plt.tight_layout()
plt.show()