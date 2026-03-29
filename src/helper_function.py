from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def _save_figure_(FIG_DIR: Path, name: str):
    plt.savefig(FIG_DIR / f"{name}.png",
                dpi=300,
                bbox_inches='tight')


def _set_name_(feature: str, target: str) -> str:
    return f"{feature} distribution by {target}"


def plot_kde(df, feature, target='IS_DEFAULT', save_path=None):
    sns.kdeplot(x=feature, hue=target, data=df, fill=True)

    name = _set_name_(feature, target)

    plt.title(name)

    if save_path:
        _save_figure_(save_path, name)

    plt.show()


def plot_hist(df, feature, target='IS_DEFAULT', save_path=None, **kwargs):
    sns.histplot(x=feature, hue=target, data=df, **kwargs)
    name = _set_name_(feature, target)

    plt.title(name)

    if save_path:
        _save_figure_(save_path, name)

    plt.show()


def plot_count(df, feature: str, target='IS_DEFAULT', save_path=None, xtick_rotation=0):
    sns.countplot(x=feature, data=df, hue=target)

    plt.xticks(rotation= xtick_rotation)

    name = _set_name_(feature, target)

    plt.title(name)

    if save_path:
        _save_figure_(save_path, name)

    plt.show()


def plot_box(df, feature: str, target='IS_DEFAULT', save_path=None, xtick_rotation=0):
    sns.boxplot(
        x=target,
        y=feature,
        data=df
    )

    plt.xticks(rotation=xtick_rotation)

    plt.tight_layout()

    name = _set_name_(feature, target)

    plt.title(name)

    if save_path:
        _save_figure_(save_path, name)
    plt.show()


if __name__ == '__main__':
    name = _set_name_('SEX', 'IS_DEFAULT')
    print(name)
