DEFAULT_COLORS = ["red","orange","yellow","lime","green","cyan","blue","navy","purple","hotpink"]
BLUE_COLORS = ["royalblue","dodgerblue","deepskyblue","skyblue","lightblue","aliceblue"]
OTHER_LABEL = "Andere"

def shrink(values, labels, max=int):
    tuple_list = []
    for i, v in enumerate(labels):
        tuple_list.append((v, values[i]))
    tuple_list.sort(key=lambda v: v[1], reverse=True)
    out_values, out_labels = [], []
    for v in tuple_list:
        out_values.append(v[1])
        out_labels.append(v[0])

    if len(out_values) > max:
        other_cat_count = 0
        for i in range(len(out_values)-1, max-1, -1):
            other_cat_count += out_values[i]
            out_values.pop(i)
            out_labels.pop(i)
        
        out_values.append(other_cat_count)
        out_labels.append(OTHER_LABEL)

    return out_values, out_labels

def palette(all_labels, selected_labels):
    palette = []
    max_color_index = len(DEFAULT_COLORS)-1
    for i, v in enumerate(all_labels):
        color_i = i
        if i > max_color_index:
            color_i = (i % max_color_index)-1

        palette.append(DEFAULT_COLORS[color_i])

    colors = []
    palette_dict = dict(zip(all_labels, palette))
    for v in selected_labels:
        colors.append(palette_dict[v])

    return colors