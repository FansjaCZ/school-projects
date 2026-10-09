from matplotlib import colors as mcolors
from matplotlib import pyplot as plt
from data import DataLoader, DataPath
from pathlib import Path

from utils import figure_utils

data_loader = DataLoader(Path(__file__).parent.parent / "data" / "main.json")

all_sports = data_loader.get_keys(DataPath(DataPath.Any, "sports", DataPath.Any))
all_sports = list(set(all_sports))

total_hours, total_labels = [], []
total_self_hours, total_self_labels = [], []
participation_hours, participation_labels = [], []
media_hours, media_labels = [], []

for sport in all_sports:
    both = sum(data_loader.get(DataPath(DataPath.Any, "sports", DataPath.Any, sport, "hours")))
    if both != 0:
        total_hours.append(both)
        total_labels.append(sport)

    media_valid_reason_filter = data_loader.filter_keys(
        lambda v, k: 
        "media" in v["sports"].keys() 
        and sport in v["sports"]["media"].keys()
        and v["sports"]["media"][sport]["valid_reason"]
    )
    participation_valid_reason_filter = data_loader.filter_keys(
        lambda v, k: 
        "participation" in v["sports"].keys() 
        and sport in v["sports"]["participation"].keys()
        and v["sports"]["participation"][sport]["valid_reason"]
    )
    both_self = sum(
        data_loader.get(DataPath(media_valid_reason_filter, "sports", "media", sport, "hours"))
        + data_loader.get(DataPath(participation_valid_reason_filter, "sports", "participation", sport, "hours"))
    )
    if both_self != 0:
        total_self_hours.append(both_self)
        total_self_labels.append(sport)

    participation = sum(data_loader.get(DataPath(DataPath.Any, "sports", "participation", sport, "hours")))
    if participation != 0:
        participation_hours.append(participation)
        participation_labels.append(sport)

    media = sum(data_loader.get(DataPath(DataPath.Any, "sports", "media", sport, "hours")))
    if media != 0:
        media_hours.append(media)
        media_labels.append(sport)


total_hours, total_labels = figure_utils.shrink(total_hours, total_labels, 5)
participation_hours, participation_labels = figure_utils.shrink(participation_hours, participation_labels, 5)
media_hours, media_labels = figure_utils.shrink(media_hours, media_labels, 5)
total_self_hours, total_self_labels = figure_utils.shrink(total_self_hours, total_self_labels, 5)

all_possible_labels = []
for v in (total_labels + media_labels + participation_labels + total_self_labels):
    if not v in all_possible_labels:
        all_possible_labels.append(v)

fig, axs = plt.subplots(2,2)
axs[0, 0].set_title("Totaal")
axs[0, 0].pie(x=total_hours, labels=total_labels, colors=figure_utils.palette(all_possible_labels, total_labels))
axs[1, 0].set_title("Participatie")
axs[1, 0].pie(x=participation_hours, labels=participation_labels, colors=figure_utils.palette(all_possible_labels, participation_labels))
axs[0, 1].set_title("Kijkcijfers")
axs[0, 1].pie(x=media_hours, labels=media_labels, colors=figure_utils.palette(all_possible_labels, media_labels))
axs[1, 1].set_title("Totaal met alleen 'geldige' redenen.")
axs[1, 1].pie(x=total_self_hours, labels=total_self_labels, colors=figure_utils.palette(all_possible_labels, total_self_labels))

plt.tight_layout()
plt.show()