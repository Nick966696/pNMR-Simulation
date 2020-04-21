import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm as mcolors

from units import *

def plot_RF_pulse_3D(data, savepath=None):
    fig = plt.figure(figsize=(16,12))

    ax = fig.add_subplot(221)
    ax.set_title(r"$x \approx y \approx z \approx 0$")
    ax.plot(data[:,0]/us, data[:,4], label="$M_x$")
    ax.plot(data[:,0]/us, data[:,6], label="$M_z$")
    ax.plot(data[:,0]/us, data[:,5], label="$M_y$", color="k")
    ax.legend(loc=3)
    ax.grid()
    ax.set_xlim(0,14)
    ax.set_ylim(-1,1)
    ax.set_xlabel("time / $\mu$s")
    ax.set_ylabel(r"$M(\sim0,\sim0,\sim0)$")
    axins = inset_axes(ax, width="50%",  height="30%", loc=1)
    axins.plot(data[:,0]/us, data[:,4])
    axins.plot(data[:,0]/us, data[:,6])
    axins.plot(data[:,0]/us, data[:,5], color="k")
    axins.set_xlim(0.5,0.7)
    axins.set_ylim(-0.25,0.25)
    axins.yaxis.get_major_locator().set_params(nbins=7)
    axins.xaxis.get_major_locator().set_params(nbins=7)
    plt.yticks(visible=False)
    #mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

    ax = fig.add_subplot(222)
    ax.set_title("averaged over volume")
    ax.plot(data[:,0]/us, data[:,1], label="$M_x$")
    ax.plot(data[:,0]/us, data[:,3], label="$M_z$")
    ax.plot(data[:,0]/us, data[:,2], label="$M_y$", color="k")
    ax.legend(loc=3)
    ax.grid()
    ax.set_xlim(0,14)
    ax.set_ylim(-1,1)
    ax.set_xlabel("time / $\mu$s")
    ax.set_ylabel(r"$\langle M_i \rangle$")
    axins = inset_axes(ax, width="50%",  height="30%", loc=1)
    axins.plot(data[:,0]/us, data[:,1])
    axins.plot(data[:,0]/us, data[:,3])
    axins.plot(data[:,0]/us, data[:,2], color="k")
    axins.set_xlim(0.5,0.7)
    axins.set_ylim(-0.25,0.25)
    axins.yaxis.get_major_locator().set_params(nbins=7)
    axins.xaxis.get_major_locator().set_params(nbins=7)
    plt.yticks(visible=False)
    #mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

    step = -10
    ax = fig.add_subplot(223, projection='3d')
    sc = ax.scatter(data[::step,4], data[::step,6], data[::step,5], c=data[::step,0]/us,
                    marker="o", cmap="jet", vmin=data[0,0]/us, vmax=data[-1,0]/us)
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    ax.set_xlabel("Mx")
    ax.set_ylabel("Mz")
    ax.set_zlabel("My")

    ax.xaxis.get_major_locator().set_params(nbins=5)
    ax.yaxis.get_major_locator().set_params(nbins=5)
    ax.zaxis.get_major_locator().set_params(nbins=5)
    plt.colorbar(sc, ax=ax).set_label("time / $\mu$s")


    ax = fig.add_subplot(224, projection='3d')
    sc = ax.scatter(data[::step,1], data[::step,3], data[::step,2], c=data[::step,0]/us,
                    #sc = ax.scatter(data[:,1], data[:,3], -data[:,2], c=data[::-1,0]/us,
                    marker="o", cmap="jet", vmin=data[0,0]/us, vmax=data[-1,0]/us)
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    ax.set_xlabel("Mx")
    ax.set_ylabel("Mz")
    ax.set_zlabel("My")

    ax.xaxis.get_major_locator().set_params(nbins=5)
    ax.yaxis.get_major_locator().set_params(nbins=5)
    ax.zaxis.get_major_locator().set_params(nbins=5)
    plt.colorbar(sc, ax=ax).set_label("time / $\mu$s")

    if savepath is not None:
        fig.savefig(savepath.replace("png", "pdf"), bbox_inches="tight")
        fig.savefig(savepath.replace("pdf", "png"), dpi=200)
