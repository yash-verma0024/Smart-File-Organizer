import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from database.analytics import *

def file_count_graph():
    """
    Graph for number of files vs extension
    """
    info = get_file_count_by_extension()

    # Setting data and values 
    data = info.index
    values = info.values

    colors = sns.color_palette("pastel")
    plt.figure(figsize=(6,6))
    plt.pie(values,
            labels=data,
            colors=colors,
            autopct='%.1f%%',       # Formats and displays percentage numbers on slices
            startangle=140          
            )
    plt.title("Extension vs number of files")
    plt.show()


def storage_graph():
    """
    Graph for number of extension vs storage
    """
    info = get_storage_by_extension()

    # Settings data and values
    data = info.index
    values = info.values

    colors = sns.color_palette("muted")
    plt.figure(figsize=(5,5))
    plt.pie(values,
            labels=data,
            colors=colors,
            autopct='%.1f%%',
            startangle=140
            )

    plt.title("Extension vs storage")
    plt.show()


def largest_files_graph():
    """
    Graph for files having most max size
    """
    info = get_largest_files()

    # Setting data and values
    data = info["file_size"]
    values = info["file_name"]

    color = sns.color_palette("dark")
    plt.figure(figsize=(6,6))
    plt.pie(data,
            labels=values,
            colors=color,
            autopct='%.1f%%',
            startangle=140
            )
    plt.title("Top 10 Files")
    plt.show()
