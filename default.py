import sys
import os
import xbmc
import xbmcgui
import xbmcaddon
import glob
import random

ADDON = xbmcaddon.Addon()
ADDON_VERSION = ADDON.getAddonInfo('version')
ADDON_LANGUAGE = ADDON.getLocalizedString
ADDON_PATH = ADDON.getAddonInfo('path').decode("utf-8")
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_DATA_PATH = os.path.join(xbmc.translatePath("special://profile/addon_data/%s" % ADDON_ID))
HOME = xbmcgui.Window(10000)

sys.path.append(xbmc.translatePath(os.path.join(ADDON_PATH, 'resources', 'lib')))
from random_art import *

randomart_breaker = 1

class CamView(xbmcgui.WindowDialog):

    def __init__(self):
        #set the initial image before the window is shown
        self.image001x = xbmcgui.ControlImage(0, 0, 256, 144, "")
        self.image002x = xbmcgui.ControlImage(256, 0, 256, 144, "")
        self.image003x = xbmcgui.ControlImage(512, 0, 256, 144, "")
        self.image004x = xbmcgui.ControlImage(768, 0, 256, 144, "")
        self.image005x = xbmcgui.ControlImage(1024, 0, 256, 144, "")

        self.image006x = xbmcgui.ControlImage(0, 144, 256, 144, "")
        self.image007x = xbmcgui.ControlImage(256, 144, 256, 144, "")
        self.image008x = xbmcgui.ControlImage(512, 144, 256, 144, "")
        self.image009x = xbmcgui.ControlImage(768, 144, 256, 144, "")
        self.image010x = xbmcgui.ControlImage(1024, 144, 256, 144, "")

        self.image011x = xbmcgui.ControlImage(0, 288, 256, 144, "")
        self.image012x = xbmcgui.ControlImage(256, 288, 256, 144, "")
        self.image013x = xbmcgui.ControlImage(512, 288, 256, 144, "")
        self.image014x = xbmcgui.ControlImage(768, 288, 256, 144, "")
        self.image015x = xbmcgui.ControlImage(1024, 288, 256, 144, "")

        self.image016x = xbmcgui.ControlImage(0, 432, 256, 144, "")
        self.image017x = xbmcgui.ControlImage(256, 432, 256, 144, "")
        self.image018x = xbmcgui.ControlImage(512, 432, 256, 144, "")
        self.image019x = xbmcgui.ControlImage(768, 432, 256, 144, "")
        self.image020x = xbmcgui.ControlImage(1024, 432, 256, 144, "")

        self.image021x = xbmcgui.ControlImage(0, 576, 256, 144, "")
        self.image022x = xbmcgui.ControlImage(256, 576, 256, 144, "")
        self.image023x = xbmcgui.ControlImage(512, 576, 256, 144, "")
        self.image024x = xbmcgui.ControlImage(768, 576, 256, 144, "")
        self.image025x = xbmcgui.ControlImage(1024, 576, 256, 144, "")

        self.image001 = xbmcgui.ControlImage(0, 0, 128, 72, "")
        self.image002 = xbmcgui.ControlImage(128, 0, 128, 72, "")
        self.image003 = xbmcgui.ControlImage(256, 0, 128, 72, "")
        self.image004 = xbmcgui.ControlImage(384, 0, 128, 72, "")
        self.image005 = xbmcgui.ControlImage(512, 0, 128, 72, "")
        self.image006 = xbmcgui.ControlImage(640, 0, 128, 72, "")
        self.image007 = xbmcgui.ControlImage(768, 0, 128, 72, "")
        self.image008 = xbmcgui.ControlImage(896, 0, 128, 72, "")
        self.image009 = xbmcgui.ControlImage(1024, 0, 128, 72, "")
        self.image010 = xbmcgui.ControlImage(1152, 0, 128, 72, "")

        self.image011 = xbmcgui.ControlImage(0, 72, 128, 72, "")
        self.image012 = xbmcgui.ControlImage(128, 72, 128, 72, "")
        self.image013 = xbmcgui.ControlImage(256, 72, 128, 72, "")
        self.image014 = xbmcgui.ControlImage(384, 72, 128, 72, "")
        self.image015 = xbmcgui.ControlImage(512, 72, 128, 72, "")
        self.image016 = xbmcgui.ControlImage(640, 72, 128, 72, "")
        self.image017 = xbmcgui.ControlImage(768, 72, 128, 72, "")
        self.image018 = xbmcgui.ControlImage(896, 72, 128, 72, "")
        self.image019 = xbmcgui.ControlImage(1024, 72, 128, 72, "")
        self.image020 = xbmcgui.ControlImage(1152, 72, 128, 72, "")

        self.image021 = xbmcgui.ControlImage(0, 144, 128, 72, "")
        self.image022 = xbmcgui.ControlImage(128, 144, 128, 72, "")
        self.image023 = xbmcgui.ControlImage(256, 144, 128, 72, "")
        self.image024 = xbmcgui.ControlImage(384, 144, 128, 72, "")
        self.image025 = xbmcgui.ControlImage(512, 144, 128, 72, "")
        self.image026 = xbmcgui.ControlImage(640, 144, 128, 72, "")
        self.image027 = xbmcgui.ControlImage(768, 144, 128, 72, "")
        self.image028 = xbmcgui.ControlImage(896, 144, 128, 72, "")
        self.image029 = xbmcgui.ControlImage(1024, 144, 128, 72, "")
        self.image030 = xbmcgui.ControlImage(1152, 144, 128, 72, "")

        self.image031 = xbmcgui.ControlImage(0, 216, 128, 72, "")
        self.image032 = xbmcgui.ControlImage(128, 216, 128, 72, "")
        self.image033 = xbmcgui.ControlImage(256, 216, 128, 72, "")
        self.image034 = xbmcgui.ControlImage(384, 216, 128, 72, "")
        self.image035 = xbmcgui.ControlImage(512, 216, 128, 72, "")
        self.image036 = xbmcgui.ControlImage(640, 216, 128, 72, "")
        self.image037 = xbmcgui.ControlImage(768, 216, 128, 72, "")
        self.image038 = xbmcgui.ControlImage(896, 216, 128, 72, "")
        self.image039 = xbmcgui.ControlImage(1024, 216, 128, 72, "")
        self.image040 = xbmcgui.ControlImage(1152, 216, 128, 72, "")

        self.image041 = xbmcgui.ControlImage(0, 288, 128, 72, "")
        self.image042 = xbmcgui.ControlImage(128, 288, 128, 72, "")
        self.image043 = xbmcgui.ControlImage(256, 288, 128, 72, "")
        self.image044 = xbmcgui.ControlImage(384, 288, 128, 72, "")
        self.image045 = xbmcgui.ControlImage(512, 288, 128, 72, "")
        self.image046 = xbmcgui.ControlImage(640, 288, 128, 72, "")
        self.image047 = xbmcgui.ControlImage(768, 288, 128, 72, "")
        self.image048 = xbmcgui.ControlImage(896, 288, 128, 72, "")
        self.image049 = xbmcgui.ControlImage(1024, 288, 128, 72, "")
        self.image050 = xbmcgui.ControlImage(1152, 288, 128, 72, "")

        self.image051 = xbmcgui.ControlImage(0, 360, 128, 72, "")
        self.image052 = xbmcgui.ControlImage(128, 360, 128, 72, "")
        self.image053 = xbmcgui.ControlImage(256, 360, 128, 72, "")
        self.image054 = xbmcgui.ControlImage(384, 360, 128, 72, "")
        self.image055 = xbmcgui.ControlImage(512, 360, 128, 72, "")
        self.image056 = xbmcgui.ControlImage(640, 360, 128, 72, "")
        self.image057 = xbmcgui.ControlImage(768, 360, 128, 72, "")
        self.image058 = xbmcgui.ControlImage(896, 360, 128, 72, "")
        self.image059 = xbmcgui.ControlImage(1024, 360, 128, 72, "")
        self.image060 = xbmcgui.ControlImage(1152, 360, 128, 72, "")

        self.image061 = xbmcgui.ControlImage(0, 432, 128, 72, "")
        self.image062 = xbmcgui.ControlImage(128, 432, 128, 72, "")
        self.image063 = xbmcgui.ControlImage(256, 432, 128, 72, "")
        self.image064 = xbmcgui.ControlImage(384, 432, 128, 72, "")
        self.image065 = xbmcgui.ControlImage(512, 432, 128, 72, "")
        self.image066 = xbmcgui.ControlImage(640, 432, 128, 72, "")
        self.image067 = xbmcgui.ControlImage(768, 432, 128, 72, "")
        self.image068 = xbmcgui.ControlImage(896, 432, 128, 72, "")
        self.image069 = xbmcgui.ControlImage(1024, 432, 128, 72, "")
        self.image070 = xbmcgui.ControlImage(1152, 432, 128, 72, "")

        self.image071 = xbmcgui.ControlImage(0, 504, 128, 72, "")
        self.image072 = xbmcgui.ControlImage(128, 504, 128, 72, "")
        self.image073 = xbmcgui.ControlImage(256, 504, 128, 72, "")
        self.image074 = xbmcgui.ControlImage(384, 504, 128, 72, "")
        self.image075 = xbmcgui.ControlImage(512, 504, 128, 72, "")
        self.image076 = xbmcgui.ControlImage(640, 504, 128, 72, "")
        self.image077 = xbmcgui.ControlImage(768, 504, 128, 72, "")
        self.image078 = xbmcgui.ControlImage(896, 504, 128, 72, "")
        self.image079 = xbmcgui.ControlImage(1024, 504, 128, 72, "")
        self.image080 = xbmcgui.ControlImage(1152, 504, 128, 72, "")

        self.image081 = xbmcgui.ControlImage(0, 576, 128, 72, "")
        self.image082 = xbmcgui.ControlImage(128, 576, 128, 72, "")
        self.image083 = xbmcgui.ControlImage(256, 576, 128, 72, "")
        self.image084 = xbmcgui.ControlImage(384, 576, 128, 72, "")
        self.image085 = xbmcgui.ControlImage(512, 576, 128, 72, "")
        self.image086 = xbmcgui.ControlImage(640, 576, 128, 72, "")
        self.image087 = xbmcgui.ControlImage(768, 576, 128, 72, "")
        self.image088 = xbmcgui.ControlImage(896, 576, 128, 72, "")
        self.image089 = xbmcgui.ControlImage(1024, 576, 128, 72, "")
        self.image090 = xbmcgui.ControlImage(1152, 576, 128, 72, "")

        self.image091 = xbmcgui.ControlImage(0, 648, 128, 72, "")
        self.image092 = xbmcgui.ControlImage(128, 648, 128, 72, "")
        self.image093 = xbmcgui.ControlImage(256, 648, 128, 72, "")
        self.image094 = xbmcgui.ControlImage(384, 648, 128, 72, "")
        self.image095 = xbmcgui.ControlImage(512, 648, 128, 72, "")
        self.image096 = xbmcgui.ControlImage(640, 648, 128, 72, "")
        self.image097 = xbmcgui.ControlImage(768, 648, 128, 72, "")
        self.image098 = xbmcgui.ControlImage(896, 648, 128, 72, "")
        self.image099 = xbmcgui.ControlImage(1024, 648, 128, 72, "")
        self.image100 = xbmcgui.ControlImage(1152, 648, 128, 72, "")


        self.addControl(self.image001)
        self.addControl(self.image002)
        self.addControl(self.image003)
        self.addControl(self.image004)
        self.addControl(self.image005)
        self.addControl(self.image006)
        self.addControl(self.image007)
        self.addControl(self.image008)
        self.addControl(self.image009)
        self.addControl(self.image010)

        self.addControl(self.image011)
        self.addControl(self.image012)
        self.addControl(self.image013)
        self.addControl(self.image014)
        self.addControl(self.image015)
        self.addControl(self.image016)
        self.addControl(self.image017)
        self.addControl(self.image018)
        self.addControl(self.image019)
        self.addControl(self.image020)

        self.addControl(self.image021)
        self.addControl(self.image022)
        self.addControl(self.image023)
        self.addControl(self.image024)
        self.addControl(self.image025)
        self.addControl(self.image026)
        self.addControl(self.image027)
        self.addControl(self.image028)
        self.addControl(self.image029)
        self.addControl(self.image030)

        self.addControl(self.image031)
        self.addControl(self.image032)
        self.addControl(self.image033)
        self.addControl(self.image034)
        self.addControl(self.image035)
        self.addControl(self.image036)
        self.addControl(self.image037)
        self.addControl(self.image038)
        self.addControl(self.image039)
        self.addControl(self.image040)

        self.addControl(self.image041)
        self.addControl(self.image042)
        self.addControl(self.image043)
        self.addControl(self.image044)
        self.addControl(self.image045)
        self.addControl(self.image046)
        self.addControl(self.image047)
        self.addControl(self.image048)
        self.addControl(self.image049)
        self.addControl(self.image050)

        self.addControl(self.image051)
        self.addControl(self.image052)
        self.addControl(self.image053)
        self.addControl(self.image054)
        self.addControl(self.image055)
        self.addControl(self.image056)
        self.addControl(self.image057)
        self.addControl(self.image058)
        self.addControl(self.image059)
        self.addControl(self.image060)

        self.addControl(self.image061)
        self.addControl(self.image062)
        self.addControl(self.image063)
        self.addControl(self.image064)
        self.addControl(self.image065)
        self.addControl(self.image066)
        self.addControl(self.image067)
        self.addControl(self.image068)
        self.addControl(self.image069)
        self.addControl(self.image070)

        self.addControl(self.image071)
        self.addControl(self.image072)
        self.addControl(self.image073)
        self.addControl(self.image074)
        self.addControl(self.image075)
        self.addControl(self.image076)
        self.addControl(self.image077)
        self.addControl(self.image078)
        self.addControl(self.image079)
        self.addControl(self.image080)

        self.addControl(self.image081)
        self.addControl(self.image082)
        self.addControl(self.image083)
        self.addControl(self.image084)
        self.addControl(self.image085)
        self.addControl(self.image086)
        self.addControl(self.image087)
        self.addControl(self.image088)
        self.addControl(self.image089)
        self.addControl(self.image090)

        self.addControl(self.image091)
        self.addControl(self.image092)
        self.addControl(self.image093)
        self.addControl(self.image094)
        self.addControl(self.image095)
        self.addControl(self.image096)
        self.addControl(self.image097)
        self.addControl(self.image098)
        self.addControl(self.image099)
        self.addControl(self.image100)

        self.addControl(self.image001x)
        self.addControl(self.image002x)
        self.addControl(self.image003x)
        self.addControl(self.image004x)
        self.addControl(self.image005x)
    
        self.addControl(self.image006x)
        self.addControl(self.image007x)
        self.addControl(self.image008x)
        self.addControl(self.image009x)
        self.addControl(self.image010x)
    
        self.addControl(self.image011x)
        self.addControl(self.image012x)
        self.addControl(self.image013x)
        self.addControl(self.image014x)
        self.addControl(self.image015x)
    
        self.addControl(self.image016x)
        self.addControl(self.image017x)
        self.addControl(self.image018x)
        self.addControl(self.image019x)
        self.addControl(self.image020x)
    
        self.addControl(self.image021x)
        self.addControl(self.image022x)
        self.addControl(self.image023x)
        self.addControl(self.image024x)
        self.addControl(self.image025x)
    
    def onScreensaverDeactivated(self):
        global randomart_breaker
        randomart_breaker = 0

    def onAction(self, action):
        global randomart_breaker
        randomart_breaker = 0

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
                image = Randomart_Color(self.prefix + "randomart_color")
                HOME.setProperty(self.prefix + "randomart_color", image)
            elif info == 'randomart_gray':
                image = Randomart_Gray(self.prefix + "randomart_gray")
                HOME.setProperty(self.prefix + "randomart_gray", image)
            elif info == 'randomart_eqn':
                image = Randomart_Eqn(self.prefix + "randomart_eqn")
                HOME.setProperty(self.prefix + "randomart_eqn", image)
            elif info == 'randomart_scrn':

                targetmask = os.path.join(xbmc.translatePath("special://profile"), self.path, self.mask)

                aeon_pics = glob.glob(targetmask)
                if len(aeon_pics) > 0:
                    while len(aeon_pics) < 100 and len(aeon_pics) > 0:
                        aeon_pics = aeon_pics + aeon_pics
                else:
                    return
                viewer = CamView()
                viewer.show()
                ran={}
                for x in range(1,101):
                    ran["r{0:03}".format(x)]=random.randint(0, 99)

                viewer.image001x.setAnimations([('conditional', "loop=true effect=slide start=-300,%04d end=2000,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])
                viewer.image002x.setAnimations([('conditional', "loop=true effect=slide start=2000,%04d end=-300,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])
                viewer.image003x.setAnimations([('conditional', "loop=true effect=slide start=%04d,-72 end=%04d,792 condition=true time=" % (random.randint(-1408,1408), random.randint(-1408,1408)) + str(random.randint(20000, 40000)),)])
                viewer.image004x.setAnimations([('conditional', "loop=true effect=slide start=%04d,792 end=%04d,-72 condition=true time=" % (random.randint(-1408,1408), random.randint(-1408,1408)) + str(random.randint(20000, 40000)),)])
                viewer.image005x.setAnimations([('conditional', "loop=true effect=slide start=-300,%04d end=2000,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])
                viewer.image006x.setAnimations([('conditional', "loop=true effect=slide start=2000,%04d end=-300,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])
                viewer.image007x.setAnimations([('conditional', "loop=true effect=slide start=%04d,-72 end=%04d,792 condition=true time=" % (random.randint(-1408,1408), random.randint(-1408,1408)) + str(random.randint(20000, 40000)),)])
                viewer.image008x.setAnimations([('conditional', "loop=true effect=slide start=%04d,792 end=%04d,-72 condition=true time=" % (random.randint(-1408,1408), random.randint(-1408,1408)) + str(random.randint(20000, 40000)),)])
                viewer.image009x.setAnimations([('conditional', "loop=true effect=slide start=-300,%04d end=2000,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])
                viewer.image010x.setAnimations([('conditional', "loop=true effect=slide start=2000,%04d end=-300,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])
                viewer.image011x.setAnimations([('conditional', "loop=true effect=slide start=%04d,-72 end=%04d,792 condition=true time=" % (random.randint(-1408,1408), random.randint(-1408,1408)) + str(random.randint(20000, 40000)),)])
                viewer.image012x.setAnimations([('conditional', "loop=true effect=slide start=%04d,792 end=%04d,-72 condition=true time=" % (random.randint(-1408,1408), random.randint(-1408,1408)) + str(random.randint(20000, 40000)),)])
                viewer.image013x.setAnimations([('conditional', "loop=true effect=slide start=-300,%04d end=2000,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])
                viewer.image014x.setAnimations([('conditional', "loop=true effect=slide start=2000,%04d end=-300,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])
                viewer.image015x.setAnimations([('conditional', "loop=true effect=slide start=%04d,-72 end=%04d,792 condition=true time=" % (random.randint(-1408,1408), random.randint(-1408,1408)) + str(random.randint(20000, 40000)),)])
                viewer.image016x.setAnimations([('conditional', "loop=true effect=slide start=%04d,792 end=%04d,-72 condition=true time=" % (random.randint(-1408,1408), random.randint(-1408,1408)) + str(random.randint(20000, 40000)),)])
                viewer.image017x.setAnimations([('conditional', "loop=true effect=slide start=-300,%04d end=2000,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])
                viewer.image018x.setAnimations([('conditional', "loop=true effect=slide start=2000,%04d end=-300,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])
                viewer.image019x.setAnimations([('conditional', "loop=true effect=slide start=%04d,-72 end=%04d,792 condition=true time=" % (random.randint(-1408,1408), random.randint(-1408,1408)) + str(random.randint(20000, 40000)),)])
                viewer.image020x.setAnimations([('conditional', "loop=true effect=slide start=%04d,792 end=%04d,-72 condition=true time=" % (random.randint(-1408,1408), random.randint(-1408,1408)) + str(random.randint(20000, 40000)),)])
                viewer.image021x.setAnimations([('conditional', "loop=true effect=slide start=-300,%04d end=2000,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])
                viewer.image022x.setAnimations([('conditional', "loop=true effect=slide start=2000,%04d end=-300,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])
                viewer.image023x.setAnimations([('conditional', "loop=true effect=slide start=%04d,-72 end=%04d,792 condition=true time=" % (random.randint(-1408,1408), random.randint(-1408,1408)) + str(random.randint(20000, 40000)),)])
                viewer.image024x.setAnimations([('conditional', "loop=true effect=slide start=%04d,792 end=%04d,-72 condition=true time=" % (random.randint(-1408,1408), random.randint(-1408,1408)) + str(random.randint(20000, 40000)),)])
                viewer.image025x.setAnimations([('conditional', "loop=true effect=slide start=-300,%04d end=2000,%04d condition=true time=" % (random.randint(-72,792), random.randint(-72,792)) + str(random.randint(20000, 40000)),)])

                while randomart_breaker:
                    ran["r{0:03}".format(random.randint(1, 100))]=random.randint(0, 99)

                    while 1:
                        if random.randint(1, 1000) > 960:
                            viewer.image001x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image001x.setImage("")
                        if random.randint(1, 1000) > 920:
                            viewer.image002x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image002x.setImage("")
                        if random.randint(1, 1000) > 880:
                            viewer.image003x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image003x.setImage("")
                        if random.randint(1, 1000) > 840:
                            viewer.image004x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image004x.setImage("")
                        if random.randint(1, 1000) > 800:
                            viewer.image005x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image005x.setImage("")

                        if random.randint(1, 1000) > 760:
                            viewer.image006x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image006x.setImage("")
                        if random.randint(1, 1000) > 720:
                            viewer.image007x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image007x.setImage("")
                        if random.randint(1, 1000) > 680:
                            viewer.image008x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image008x.setImage("")
                        if random.randint(1, 1000) > 640:
                            viewer.image009x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image009x.setImage("")
                        if random.randint(1, 1000) > 600:
                            viewer.image010x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image010x.setImage("")

                        if random.randint(1, 1000) > 560:
                            viewer.image011x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image011x.setImage("")
                        if random.randint(1, 1000) > 520:
                            viewer.image012x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image012x.setImage("")
                        if random.randint(1, 1000) > 480:
                            viewer.image013x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image013x.setImage("")
                        if random.randint(1, 1000) > 440:
                            viewer.image014x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image014x.setImage("")
                        if random.randint(1, 1000) > 400:
                            viewer.image015x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image015x.setImage("")

                        if random.randint(1, 1000) > 360:
                            viewer.image016x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image016x.setImage("")
                        if random.randint(1, 1000) > 320:
                            viewer.image017x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image017x.setImage("")
                        if random.randint(1, 1000) > 280:
                            viewer.image018x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image018x.setImage("")
                        if random.randint(1, 1000) > 240:
                            viewer.image019x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image019x.setImage("")
                        if random.randint(1, 1000) > 200:
                            viewer.image020x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image020x.setImage("")

                        if random.randint(1, 1000) > 160:
                            viewer.image021x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image021x.setImage("")
                        if random.randint(1, 1000) > 120:
                            viewer.image022x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image022x.setImage("")
                        if random.randint(1, 1000) > 80:
                            viewer.image023x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image023x.setImage("")
                        if random.randint(1, 1000) > 40:
                            viewer.image024x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
#                        else:
#                            viewer.image024x.setImage("")
                        if random.randint(1, 1000) < 40:
                            viewer.image025x.setImage(aeon_pics[ran["r{0:03}".format(random.randint(1, 100))]])
                            break
                        else:
                            viewer.image025x.setImage("")
                        break

                    xbmc.sleep(random.randint(200, 500))


                    viewer.image001.setImage(aeon_pics[ran["r001"]])
                    viewer.image002.setImage(aeon_pics[ran["r002"]])
                    viewer.image003.setImage(aeon_pics[ran["r003"]])
                    viewer.image004.setImage(aeon_pics[ran["r004"]])
                    viewer.image005.setImage(aeon_pics[ran["r005"]])
                    viewer.image006.setImage(aeon_pics[ran["r006"]])
                    viewer.image007.setImage(aeon_pics[ran["r007"]])
                    viewer.image008.setImage(aeon_pics[ran["r008"]])
                    viewer.image009.setImage(aeon_pics[ran["r009"]])
                    viewer.image010.setImage(aeon_pics[ran["r010"]])
                    viewer.image011.setImage(aeon_pics[ran["r011"]])
                    viewer.image012.setImage(aeon_pics[ran["r012"]])
                    viewer.image013.setImage(aeon_pics[ran["r013"]])
                    viewer.image014.setImage(aeon_pics[ran["r014"]])
                    viewer.image015.setImage(aeon_pics[ran["r015"]])
                    viewer.image016.setImage(aeon_pics[ran["r016"]])
                    viewer.image017.setImage(aeon_pics[ran["r017"]])
                    viewer.image018.setImage(aeon_pics[ran["r018"]])
                    viewer.image019.setImage(aeon_pics[ran["r019"]])
                    viewer.image020.setImage(aeon_pics[ran["r020"]])
                    viewer.image021.setImage(aeon_pics[ran["r021"]])
                    viewer.image022.setImage(aeon_pics[ran["r022"]])
                    viewer.image023.setImage(aeon_pics[ran["r023"]])
                    viewer.image024.setImage(aeon_pics[ran["r024"]])
                    viewer.image025.setImage(aeon_pics[ran["r025"]])
                    viewer.image026.setImage(aeon_pics[ran["r026"]])
                    viewer.image027.setImage(aeon_pics[ran["r027"]])
                    viewer.image028.setImage(aeon_pics[ran["r028"]])
                    viewer.image029.setImage(aeon_pics[ran["r029"]])
                    viewer.image030.setImage(aeon_pics[ran["r030"]])
                    viewer.image031.setImage(aeon_pics[ran["r031"]])
                    viewer.image032.setImage(aeon_pics[ran["r032"]])
                    viewer.image033.setImage(aeon_pics[ran["r033"]])
                    viewer.image034.setImage(aeon_pics[ran["r034"]])
                    viewer.image035.setImage(aeon_pics[ran["r035"]])
                    viewer.image036.setImage(aeon_pics[ran["r036"]])
                    viewer.image037.setImage(aeon_pics[ran["r037"]])
                    viewer.image038.setImage(aeon_pics[ran["r038"]])
                    viewer.image039.setImage(aeon_pics[ran["r039"]])
                    viewer.image040.setImage(aeon_pics[ran["r040"]])
                    viewer.image041.setImage(aeon_pics[ran["r041"]])
                    viewer.image042.setImage(aeon_pics[ran["r042"]])
                    viewer.image043.setImage(aeon_pics[ran["r043"]])
                    viewer.image044.setImage(aeon_pics[ran["r044"]])
                    viewer.image045.setImage(aeon_pics[ran["r045"]])
                    viewer.image046.setImage(aeon_pics[ran["r046"]])
                    viewer.image047.setImage(aeon_pics[ran["r047"]])
                    viewer.image048.setImage(aeon_pics[ran["r048"]])
                    viewer.image049.setImage(aeon_pics[ran["r049"]])
                    viewer.image050.setImage(aeon_pics[ran["r050"]])
                    viewer.image051.setImage(aeon_pics[ran["r051"]])
                    viewer.image052.setImage(aeon_pics[ran["r052"]])
                    viewer.image053.setImage(aeon_pics[ran["r053"]])
                    viewer.image054.setImage(aeon_pics[ran["r054"]])
                    viewer.image055.setImage(aeon_pics[ran["r055"]])
                    viewer.image056.setImage(aeon_pics[ran["r056"]])
                    viewer.image057.setImage(aeon_pics[ran["r057"]])
                    viewer.image058.setImage(aeon_pics[ran["r058"]])
                    viewer.image059.setImage(aeon_pics[ran["r059"]])
                    viewer.image060.setImage(aeon_pics[ran["r060"]])
                    viewer.image061.setImage(aeon_pics[ran["r061"]])
                    viewer.image062.setImage(aeon_pics[ran["r062"]])
                    viewer.image063.setImage(aeon_pics[ran["r063"]])
                    viewer.image064.setImage(aeon_pics[ran["r064"]])
                    viewer.image065.setImage(aeon_pics[ran["r065"]])
                    viewer.image066.setImage(aeon_pics[ran["r066"]])
                    viewer.image067.setImage(aeon_pics[ran["r067"]])
                    viewer.image068.setImage(aeon_pics[ran["r068"]])
                    viewer.image069.setImage(aeon_pics[ran["r069"]])
                    viewer.image070.setImage(aeon_pics[ran["r070"]])
                    viewer.image071.setImage(aeon_pics[ran["r071"]])
                    viewer.image072.setImage(aeon_pics[ran["r072"]])
                    viewer.image073.setImage(aeon_pics[ran["r073"]])
                    viewer.image074.setImage(aeon_pics[ran["r074"]])
                    viewer.image075.setImage(aeon_pics[ran["r075"]])
                    viewer.image076.setImage(aeon_pics[ran["r076"]])
                    viewer.image077.setImage(aeon_pics[ran["r077"]])
                    viewer.image078.setImage(aeon_pics[ran["r078"]])
                    viewer.image079.setImage(aeon_pics[ran["r079"]])
                    viewer.image080.setImage(aeon_pics[ran["r080"]])
                    viewer.image081.setImage(aeon_pics[ran["r081"]])
                    viewer.image082.setImage(aeon_pics[ran["r082"]])
                    viewer.image083.setImage(aeon_pics[ran["r083"]])
                    viewer.image084.setImage(aeon_pics[ran["r084"]])
                    viewer.image085.setImage(aeon_pics[ran["r085"]])
                    viewer.image086.setImage(aeon_pics[ran["r086"]])
                    viewer.image087.setImage(aeon_pics[ran["r087"]])
                    viewer.image088.setImage(aeon_pics[ran["r088"]])
                    viewer.image089.setImage(aeon_pics[ran["r089"]])
                    viewer.image090.setImage(aeon_pics[ran["r090"]])
                    viewer.image091.setImage(aeon_pics[ran["r091"]])
                    viewer.image092.setImage(aeon_pics[ran["r092"]])
                    viewer.image093.setImage(aeon_pics[ran["r093"]])
                    viewer.image094.setImage(aeon_pics[ran["r094"]])
                    viewer.image095.setImage(aeon_pics[ran["r095"]])
                    viewer.image096.setImage(aeon_pics[ran["r096"]])
                    viewer.image097.setImage(aeon_pics[ran["r097"]])
                    viewer.image098.setImage(aeon_pics[ran["r098"]])
                    viewer.image099.setImage(aeon_pics[ran["r099"]])
                    viewer.image100.setImage(aeon_pics[ran["r100"]])
                
                    xbmc.sleep(random.randint(200, 500))
                
                global randomart_breaker
                randomart_breaker = 1
                viewer.close()
                del viewer


    def _init_vars(self):
        self.window = xbmcgui.Window(10000)  # Home Window
        self.control = None
        self.infos = []
        self.id = ""
        self.prefix = ""
        self.path = ""
        self.mask = ""
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
            elif arg.startswith('path='):
                self.path = arg[5:]
            elif arg.startswith('mask='):
                self.mask = arg[5:]
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


if __name__ == "__main__":
    RandomartMain()
log('finished')
