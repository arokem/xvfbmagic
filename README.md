## xvfbmagic for IPython

Run lines/cells under a virtual frame buffer.

### Install:

    %install_ext https://raw.github.com/arokem/xvfbmagic/master/xvfbmagic.py

### Use:

Once you have installed the extension, you will need to load it using:

    %load_ext xvfbmagic

To use it as a cell magic, use:

    %%xvfb
    # Additional code displaying visualizations that require Xvfb
    # Can be several lines

To use it as a line magic use:

    %xvfb #additional code that requires xvfb (just that line)
