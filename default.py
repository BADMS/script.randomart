import sys
import os
import xbmc
import xbmcgui
import xbmcaddon

ADDON = xbmcaddon.Addon()
ADDON_VERSION = ADDON.getAddonInfo('version')
ADDON_LANGUAGE = ADDON.getLocalizedString
ADDON_PATH = ADDON.getAddonInfo('path').decode("utf-8")
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_DATA_PATH = os.path.join(xbmc.translatePath("special://profile/addon_data/%s" % ADDON_ID))
HOME = xbmcgui.Window(10000)
sys.path.append(xbmc.translatePath(os.path.join(ADDON_PATH, 'resources', 'lib')))

from random_art import *


class RandomartMain:

    def __init__(self):
        log("version %s started" % ADDON_VERSION)
        self._init_vars()
        self._parse_argv()
        if not xbmcvfs.exists(ADDON_DATA_PATH):
            # addon data path does not exist...create it
            xbmcvfs.mkdir(ADDON_DATA_PATH)
        if self.infos:
            self._StartInfoActions()
        if self.control == "plugin":
            xbmcplugin.endOfDirectory(self.handle)

    def _StartInfoActions(self):
        for info in self.infos:
            if info == 'randomart_color':
                image = Randomart_Color(self.prefix)
                HOME.setProperty(self.prefix + "randomart_color", image)
            elif info == 'randomart_gray':
                image = Randomart_Gray(self.prefix)
                HOME.setProperty(self.prefix + "randomart_gray", image)
            elif info == 'randomart_eqn':
                image = Randomart_Eqn(self.prefix)
                HOME.setProperty(self.prefix + "randomart_gray", image)

    def _init_vars(self):
        self.window = xbmcgui.Window(10000)  # Home Window
        self.control = None
        self.infos = []
        self.id = ""
        self.prefix = ""
        self.daemon = False
        self.autoclose = ""

    def _parse_argv(self):
        args = sys.argv
        for arg in args:
            arg = arg.replace("'\"", "").replace("\"'", "")
            if arg == 'script.randomart':
                continue
            elif arg.startswith('info='):
                self.infos.append(arg[5:])
            elif arg.startswith('id='):
                self.id = RemoveQuotes(arg[3:])
            elif arg.startswith('prefix='):
                self.prefix = arg[7:]
                if not self.prefix.endswith("."):
                    self.prefix = self.prefix + "."
            elif arg.startswith('container='):
                self.container = RemoveQuotes(arg[10:])

class RandomartMonitor(xbmc.Monitor):

    def __init__(self, *args, **kwargs):
        xbmc.Monitor.__init__(self)

    def onPlayBackStarted(self):
        pass
        # HOME.clearProperty(self.prefix + 'ImageFilter')
        # Notify("test", "test")
        # image, imagecolor = Filter_Image(self.id, self.radius)
        # HOME.setProperty(self.prefix + 'ImageFilter', image)
        # HOME.setProperty(self.prefix + "ImageColor", imagecolor)


if __name__ == "__main__":
    RandomartMain()
log('finished')
