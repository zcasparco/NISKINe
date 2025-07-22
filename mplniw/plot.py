import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

def plot_uv(ds,V,fig,ax,cmap = 'coolwarm', vmax=0.4,**kwargs):
    """
    Wrapper to plot 2D variables (Depth, Time)
    ds : xarray, Dataset
    V : Variable to be plotted
    fig,ax: figure and ax to use to plot the variable
    
    """
    ds[V].plot(ax=ax, yincrease=False,vmax=vmax,cmap=cmap, **kwargs)
    return fig,ax

def plot_event2D(ds,v,mld,ti,tf,months,**kwargs):
    fig,axs = plt.subplots(1,len(ti),figsize=(5*len(ti),6))
    for i in range(len(ti)):
        ds.sel(time=slice(ti[i],tf[i]))[v].plot(ax=axs[i],zorder=-1,y='z',yincrease=False,**kwargs)
        mld.sel(time=slice(ti[i],tf[i])).plot(ax=axs[i],x='time',c='c',zorder=1)
        #axs[i].plot(mld.sel(time=slice(ti[i],tf[i])),c='c',lw=2,zorder=1)
        axs[i].set_title('Month %s'%months[i])
    return fig,axs

def get_hist(ds,bins):
    """ get histograms times value to compare plot with Savage et al, 2025 (not published yet)
    ----------------------------------------------------
    Parameters:
    ds: xr.Dataset, contains variable to use for histogram
    bins:int, number of bins for histogram
    ----------------------------------------------------
    Returns:
    pdf_times_values:array, pdf x values
    bin_centers:array, histogram bins center for plot
    """
    # Flatten the 2D array to 1D
    flattened_data = ds.values.ravel()
    valid_data = flattened_data[~np.isnan(flattened_data)]
    # Compute histogram
    counts, bin_edges = np.histogram(valid_data, bins=bins, density=True)
    # Compute bin centers
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    # Compute PDF × value
    pdf_times_value = counts * np.abs(bin_centers)
    return pdf_times_value,bin_centers

def plot_hist(pi,ow,bins=50, plot=True):
    """ plot histograms times value to compare plot with Savage et al, 2025 (not published yet)
    ----------------------------------------------------
    Parameters:
    pi: xr.Dataset, contains energy transfer estimates to use for histogram
    ow: xr.Dataset, contains Okubo-Weiss parameter estimates to use for histogram plot
    bins:int, number of bins for histogram
    ----------------------------------------------------
    Returns:
    [hist_pos,hist_neg]: list of array, histograms for positive OW parameter
    [hist_pos_neg,hist_neg_neg]: list of array, histograms for negative OW parameter
    [bin_pos,bin_neg]: list of array, bins for positive OW parameter
    [bin_pos_neg,bin_neg_neg]: list of array, bins for negative OW parameter
    bin_centers:array, histogram bins center for plot
    """
    P_pos=pi.where((ow>0)&(pi>0))
    P_neg=pi.where((ow>0)&(pi<0))
    
    hist_pos,bin_pos = get_hist(P_pos,bins=bins)
    hist_neg,bin_neg = get_hist(P_neg,bins=bins)

    if plot:
    # Plot
        fig,axs=plt.subplots(1,2,figsize=(10,4),sharey=True)
        ax=axs[0]
        ax.plot(bin_pos, hist_pos, drawstyle='steps-mid', color='r', linewidth=2)
        ax.plot(-1*bin_neg, hist_neg, drawstyle='steps-mid', color='b', linewidth=2)
        ax.set_ylabel(r'PDf $\times$ $\Pi_\omega$ [m$^2$ s$^{-3}$]')
        ax.set_xlabel(r'$\Pi_\omega$ [m$^2$ s$^{-3}$]');ax.set_title(r'OW>0')
        ax.set_xlim(0,4e-6);#ax.set_ylim(0,None)
        ax.grid(True)
    
        P_pos=pi.where((ow<0)&(pi>0))
        P_neg=pi.where((ow<0)&(pi<0))
        
        hist_pos,bin_pos = get_hist(P_pos,bins=bins)
        hist_neg,bin_neg = get_hist(P_neg,bins=bins)
        
        # Plot
        ax=axs[1]
        ax.plot(bin_pos, hist_pos, drawstyle='steps-mid', color='r', linewidth=2,label=r'$\Pi_\omega>0$')
        ax.plot(-1*bin_neg, hist_neg, drawstyle='steps-mid', color='b', linewidth=2,label=r'$\Pi_\omega<0$')
        ax.set_ylabel(r'PDf $\times$ $\Pi_\omega$ [m$^2$ s$^{-3}$]')
        ax.set_xlabel(r'$\Pi_\omega$ [m$^2$ s$^{-3}$]');ax.set_title(r'OW<0')
        ax.set_xlim(0,4e-6);ax.set_ylim(0,0.4)
        ax.grid(True);ax.legend()
        return fig,axs
    else:
        P_pos_neg=pi.where((ow<0)&(pi>0))
        P_neg_neg=pi.where((ow<0)&(pi<0))
        
        hist_pos_neg,bin_pos_neg = get_hist(P_pos_neg,bins=bins)
        hist_neg_neg,bin_neg_neg = get_hist(P_neg_neg,bins=bins)
        return [hist_pos,hist_neg], [hist_pos_neg,hist_neg_neg], [bin_pos,bin_neg], [bin_pos_neg,bin_neg_neg]