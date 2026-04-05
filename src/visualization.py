import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import src.constants as c

from typing import Optional

# Phong cach chung cho toan project
sns.set_theme(style= "whitegrid")
plt.rcParams['figure.dpi']= 100
plt.rcParams['savefig.dpi']= 300

def plot_distribution(
        df: pd.DataFrame,
        column: str,
        title: Optional[str]= None,
        ax: Optional[plt.Axes] = None,
        hue: Optional[str] = None,
        rotation: Optional[int] = 0,
) -> plt.Axes:
    """
    Ve bieu do pha phoi (Histogram + KDE) cho mot so cot
    """

    if ax is None:
        fig, ax= plt.subplots(figsize= (8, 5))

    sns.histplot(data= df, x= column, kde= True, ax= ax, color= 'skyblue', hue= hue)

    ax.set_title(title or f'Distribution of {column.upper()}', fontsize= 12, pad= 15)
    ax.set_xlabel(column.replace("_", " ").title())
    ax.set_xticklabels(ax.get_xticklabels(), rotation= rotation)
    ax.set_ylabel('Frequency')

    logging.info(f"Generated Distribution plot for: {column}")

    return ax

def plot_correlation_matrix(df: pd.DataFrame, title: str= "Correlation Heatmap"):
    """
    Ve ma tran tuong quan cho cac bien so
    """

    plt.figure(figsize= (12, 10))
    corr = df.select_dtypes(include= ['number']).corr()

    import numpy as np
    mask= np.triu(np.ones_like(corr, dtype= bool))

    sns.heatmap(corr, mask= mask, annot= False, fmt= '.2f', cmap= 'RdBu_r', center= 0)
    plt.title(title, fontsize= 15)
    plt.show()

def plot_catergorical(df: pd.DataFrame,
                      column: str,
                      ax: Optional[plt.Axes]= None,
                      hue: Optional[str]= None):
    
    """Bieu do cot dem so luong cho bien phan loai"""
    if ax is None:
        fig, ax= plt.subplots(figsize= (10, 6))

    # Ve bieu do va sap xep theo so luong giam dan
    sns.countplot(data= df, x= column, palette= 'viridis', ax= ax,
                  order= df[column].value_counts().index, hue= hue)

    ax.set_title(f"Distribution by {column.upper()}", fontsize= 12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation= 45)

    return ax

def box_group(df: pd.DataFrame, x: str, y: str, ax: Optional[plt.Axes]= None):
    """So sanh phan phoi cua nhom y dua tren nhom x"""

    if ax is None:
        fig, ax= plt.subplots(figsize= (12, 6))

    sns.boxplot(data= df, x= x, y= y, ax= ax, showfliers= False)
    sns.stripplot(data= df, x= x, y= y, ax= ax, color= ".3", size= 2, alpha= 0.3)

    ax.set_title(f"So sanh {y} theo {x}", fontsize= 12)

    return ax

def scatter_plot(df: pd.DataFrame,
                 x: str, y: str,
                 hue: Optional[str]= None,
                 ax: Optional[plt.Axes]= None):
    
    """Ve moi quan he giua cac bien so"""
    if ax is None:
        fig, ax = plt.subplots(figsize= (10, 7))

    sns.scatterplot(data= df, x= x, y= y, hue= hue, ax= ax, alpha= 0.6, edgecolor= None)

    ax.set_title(f"Moi lien he giua {x} va {y}", fontsize= 12)

    return ax

def save_plot(fig, file_name: str):
    """Tao thu muc va luu bieu do"""
    # Tro ra thu muc Finance/Visulization

    save_path = c.BASE_DIR / "src" / "Visualization"
    save_path.mkdir(parents= True, exist_ok= True)

    full_path = save_path/ f"{file_name}.png"
    fig.savefig(full_path, bbox_inches= 'tight')
    logging.info(f"Saved at: {full_path}")