"""Helper functions that apply style and decoration to plots."""

###################################################################################################
###################################################################################################

def check_n_style(style_func, *args):
    """"Check is a style function has been passed, and apply if so.

    Parameters
    ----------
    style_func : callable or None
        Function to apply styling to a plot axis.
    *args
        Inputs to the style plot.
    """

    if style_func:
        style_func(*args)


def style_spectrum_plot(ax, log_freqs, log_powers):
    """Define to styling for a power spectrum plot.

    Parameters
    ----------
    ax : matplotlib.Axes
        Figure axes to apply styling to
    log_freqs : boolean
        Whether the frequency axis is plotted in log space.
    log_powers : boolean
        Whether the power axis is plotted in log space.
    """

    # Get labels, based on log status
    xlabel = 'Frequency' if not log_freqs else 'log(Frequency)'
    ylabel = 'Power' if not log_powers else 'log(Power)'

    # Aesthetics and axis labels
    ax.set_xlabel(xlabel, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.grid(True)

    # If labels were provided, add a legend
    if ax.get_legend_handles_labels()[0]:
        ax.legend(prop={'size': 16})
