from __future__ import print_function
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)

from xvfbwrapper import Xvfb


@magics_class
class XvfbMagics(Magics):
    def __init__(self, shell, **xvfb_kwargs):
        """
        Initialize the XvfbMagics object

        Parameters
        ----------
        shell : IPython instance

        xvfb_kwargs : dict
            Keyword arguments to initialize xfvbwrapper.Xvfb
            Defaultst to: width=800, height=680, colordepth=24.
        """
        super(XvfbMagics, self).__init__(shell)
        self.xvfb_kwargs = xvfb_kwargs

    @line_cell_magic
    def xvfb(self, line, cell=None):
        display = Xvfb(**self.xvfb_kwargs)
        display.start()
        if cell is None:
            self.shell.ex(line)
        else:
            self.shell.ex(cell)
        display.stop()

_loaded = False
def load_ipython_extension(ip, **kwargs):
    """Load the extension in IPython."""
    global _loaded
    if not _loaded:
        ip.register_magics(XvfbMagics(ip, **kwargs))
        _loaded = True

def unload_ipython_extension(ip):
    global _loaded
    if _loaded:
        magic = ip.magics_manager.registry.pop('XvfbMagics')
        _loaded = False
