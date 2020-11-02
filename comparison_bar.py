import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

my_dict = {
    'REB': [7, 47],
    'OREB': [10, 13],
}

#fig, ax = plt.subplots(nrows=2, ncols=len(my_dict), sharex=True)


def create_subplot(stat_name, col, stat_pair, color1, color2):
    team1_list = stat_pair[0:1]
    print(team1_list)
    team2_list = stat_pair[1:]
    print(team2_list)
    x_size = np.arange(len(team1_list))

    graph1 = ax[0][col].bar(x_size, team1_list, align = 'center', color='red')
    graph2 = ax[1][col].bar(x_size, team2_list, align='center', color='black')
    ax[1][col].invert_yaxis()
    ax[0][col].set(xticks=x_size, xticklabels=[stat_name])
    ax[1][col].xaxis.tick_top()
    ax[0][col].yaxis.set_visible(False)
    ax[1][col].yaxis.set_visible(False)
    #delete_border(col)
    annotate(graph1, graph2, col)


def delete_border(col):
    ax[0][col].spines['top'].set_visible(False)
    ax[0][col].spines['right'].set_visible(False)
    ax[0][col].spines['bottom'].set_visible(False)
    ax[0][col].spines['left'].set_visible(False)
    ax[1][col].spines['top'].set_visible(False)
    ax[1][col].spines['right'].set_visible(False)
    ax[1][col].spines['bottom'].set_visible(False)
    ax[1][col].spines['left'].set_visible(False)

#attaches text label above each bar displaying height
def annotate(bars1, bars2, col):
    height = bars1[0].get_height()
    height2 = bars2[0].get_height()
    ax[0][col].text(bars1[0].get_x() + bars1[0].get_width()/2, height*1.05, '%d' % int(height), ha='center', va='bottom')
    ax[1][col].text(bars2[0].get_x() + bars2[0].get_width()/2, height2 * 1.14, '%d' % int(height2), ha='center', va='bottom')
"""
col = 0
for stat in my_dict:
    create_subplot(stat, col, my_dict[stat], "red", "black")
    col = col + 1
"""
x = ['REB']
y = [5]
y2 = [47]

x_size = np.arange(len(y))
print(x_size)

fig, ax = plt.subplots(nrows=2)
#fig = plt.figure(frameon=False)
rects = ax[1].bar(x_size, y2, align= 'center', color='black')
rects2 = ax[0].bar(x_size, y, align = 'center', color='red')
ax[1].invert_yaxis()
ax[0].set(xticks = x_size, xticklabels = x)
#ax[1].xaxis.tick_top()
ax[0].xaxis.set_ticks_position('none')
ax[1].axis('off')
print(ax[1].get_ylim())
ax[0].set_ylim(0, ax[1].get_ylim()[0])

plt.subplots_adjust(wspace = 0, hspace = 0.2)

#fig.subplots_adjust(wspace=0.09)
plt.show()