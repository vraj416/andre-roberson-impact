import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.patches as mpatches

my_dict_base = {
    'REB': [44, 47],
    'OREB': [10, 13],
    'DREB': [34, 34],
    'AST': [12, 18],
    'STL': [11, 8],
    'BLK': [9, 3],
    'TOV': [9, 15],
}

base_values = {'DEF_RATING': 90,
               'OPP_FG3_PCT': 0.30,
               'OPP_FG_PCT': 0.40}

my_dict = {'DEF_RATING': [95.9, 112.92261538461538],
           'OPP_FG3_PCT': [0.339, 0.3989969230769231],
           'OPP_FG_PCT': [0.446, 0.48382923076923073]}

fig, ax = plt.subplots(nrows=2, ncols=len(my_dict))

def find_bigger(col):
    print(ax[0][col].get_ylim()[1])
    print(ax[1][col].get_ylim()[0])
    x = ax[0][col].get_ylim()[1] > ax[1][col].get_ylim()[0]
    print(x)
    if(ax[1][col].get_ylim()[0] >= ax[0][col].get_ylim()[1]):
        return 1
        #return ax[1][col].get_ylim()[0]
    else:
        return 1
        #return ax[0][col].get_ylim()[1]

def create_stat_pair(stats, stat_name):
    stat_pair = stats
    sum = stat_pair[0] - 2*base_values[stat_name] + stat_pair[1]
    if(stat_pair[0] == stat_pair[1]):
        print("1")
        return [stat_pair[0]/sum, stat_pair[1]/sum]
    elif(stat_pair[0] == 0):
        print("2")
        stat_pair[0] = stat_pair[1]/5
    elif (stat_pair[1] == 0):
        print("3")
        stat_pair[1] = stat_pair[0]/5
    return [(stat_pair[0] - base_values[stat_name])/sum, (stat_pair[1] - base_values[stat_name])/sum]

def delete_border(col):
    ax[0][col].spines['top'].set_visible(False)
    ax[0][col].spines['right'].set_visible(False)
    ax[0][col].spines['bottom'].set_visible(False)
    ax[0][col].spines['left'].set_visible(False)
    ax[1][col].spines['top'].set_visible(False)
    ax[1][col].spines['right'].set_visible(False)
    ax[1][col].spines['bottom'].set_visible(False)
    ax[1][col].spines['left'].set_visible(False)

def create_subplot(stat_name, col, stats_orig, color1, color2):
    stat_pair = create_stat_pair(stats_orig, stat_name)
    #print(stat_pair)
    team1_list = stat_pair[0:1]
    team2_list = stat_pair[1:]
    x_size = np.arange(len(team1_list))
    graph1 = ax[0][col].bar(x_size, team1_list, align = 'center', color='orange')
    graph2 = ax[1][col].bar(x_size, team2_list, align='center', color='blue')
    ax[1][col].invert_yaxis()
    ax[0][col].set(xticks=x_size, xticklabels=[stat_name])
    ax[1][col].xaxis.tick_top()
    ax[0][col].yaxis.set_visible(False)
    ax[1][col].yaxis.set_visible(False)
    ax[1][col].xaxis.set_visible(False)
    ax[0][col].xaxis.set_ticks_position('none')
    #ax[1][col].axis('off')
    lim = find_bigger(col)
    print("lim: " + str(lim))
    ax[0][col].set_ylim(0, lim)
    ax[1][col].set_ylim(lim, 0)
    delete_border(col)
    annotate(graph1, graph2, col, stats_orig)

def annotate(bars1, bars2, col, stats_orig):
    height = bars1[0].get_height()
    height2 = bars2[0].get_height()
    ax[0][col].text(bars1[0].get_x() + bars1[0].get_width()/2, height + 0.03, '%f' % float(stats_orig[0]), ha='center', va='bottom', fontname='Sans', color='grey')
    ax[1][col].text(bars2[0].get_x() + bars2[0].get_width()/2, height2 + 0.1, '%f' % float(stats_orig[1]), ha='center', va='bottom', fontname='Sans', color='red')

col = 0
for stat in my_dict:
    print(stat)
    create_subplot(stat, col, my_dict[stat], "red", "blue")
    col = col + 1

orange_patch = mpatches.Patch(color='orange', label="Big 4 with Roberson")
blue_patch = mpatches.Patch(color='blue', label="Big 4 without Roberson")
plt.legend(handles=[orange_patch, blue_patch])
plt.subplots_adjust(wspace = 0.2, hspace = 0.2)
plt.show()