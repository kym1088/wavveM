# -*- coding: utf-8 -*-
__author__ = "NightRain"
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
import os
import xbmcplugin , xbmcgui , xbmcaddon , xbmc
import sys
import urlparse
import inputstreamhelper
import datetime
import time
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
if 94 - 94: i1IIi % Oo0Ooo
o0oO0 = [
 { 'title' : '홈' , 'uicode' : 'GN1' , 'came' : 'home' }
 , { 'title' : 'LIVE 채널' , 'uicode' : 'GN3' , 'came' : 'live' }
 , { 'title' : 'VOD 방송' , 'uicode' : 'GN2' , 'came' : 'broadcast' }

, { 'title' : '영화(Movie)' , 'uicode' : 'GN17' , 'came' : 'movie' }
 , { 'title' : '해외시리즈' , 'uicode' : 'GN12' , 'came' : 'global' }

# i1IIi . I1Ii111 / IiII * OoooooooOO + I11i * oO0o
# i11iIiiIii - II111iiii % I1Ii111 - iIii1I11I1II1 . I1ii11iIi11i . II111iiii
, { 'title' : '분류별 - 방송(VOD) - 인기순' , 'uicode' : 'GENRE' , 'came' : 'vodgenre' , 'orderby' : 'viewtime' , 'ordernm' : '인기순' }
 , { 'title' : '분류별 - 방송(VOD) - 최신순' , 'uicode' : 'GENRE' , 'came' : 'vodgenre' , 'orderby' : 'new' , 'ordernm' : '최신순' }
 , { 'title' : '분류별 - 영화(Movie) - 인기순' , 'uicode' : 'GENRE' , 'came' : 'moviegenre_svod' , 'orderby' : 'paid' , 'ordernm' : '인기순' }
 , { 'title' : '분류별 - 영화(Movie) - 업데이트순' , 'uicode' : 'GENRE' , 'came' : 'moviegenre_svod' , 'orderby' : 'displaystart' , 'ordernm' : '업데이트순' }

, { 'title' : '검색' , 'uicode' : 'SEARCH' , 'came' : '-' }
 , { 'title' : 'Watched(시청목록)' , 'uicode' : 'WATCH' , 'came' : '-' }
 ]
OOoO = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
if 91 - 91: OoO0O00 . i11iIiiIii / oO0o % I11i / OoO0O00 - i11iIiiIii
__addon__ = xbmcaddon . Addon ( )
__language__ = __addon__ . getLocalizedString
__profile__ = xbmc . translatePath ( __addon__ . getAddonInfo ( 'profile' ) )
__version__ = __addon__ . getAddonInfo ( 'version' )
__addonid__ = __addon__ . getAddonInfo ( 'id' )
__addonname__ = __addon__ . getAddonInfo ( 'name' )
if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1 . IiII / IiII % IiII
from wavveCore import *
if 22 - 22: Ii1I . IiII
if 41 - 41: I1Ii111 . ooOoO0o * IiII % i11iIiiIii
class o000o0o00o0Oo ( object ) :
 def __init__ ( self , in_addonurl , in_handle , in_params ) :
  if 80 - 80: OoooooooOO . I1IiiI
  if 87 - 87: oO0o / ooOoO0o + I1Ii111 - ooOoO0o . ooOoO0o / II111iiii
  if 11 - 11: I1IiiI % o0oOOo0O0Ooo - Oo0Ooo
  if 58 - 58: i11iIiiIii % I1Ii111
  self . _addon_url = in_addonurl
  self . _addon_handle = in_handle
  self . main_params = in_params
  self . WavveObj = O0OoOoo00o ( )
  if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
  if 31 - 31: OoO0O00 + II111iiii
  if 13 - 13: OOooOOo * oO0o * I1IiiI
  if 55 - 55: II111iiii
 def addon_noti ( self , sting ) :
  try :
   IIIiI11ii = xbmcgui . Dialog ( )
   if 52 - 52: iII111i + OOooOOo % OoooooooOO / i11iIiiIii
   IIIiI11ii . notification ( __addonname__ , sting )
  except :
   None
   if 25 - 25: O0 * oO0o + OoooooooOO
   if 70 - 70: OOooOOo / Ii1I . Ii1I
   if 11 - 11: ooOoO0o / O0 - i1IIi
 def addon_log ( self , string , isDebug = False ) :
  try :
   o00O00O0O0O = string . encode ( 'utf-8' , 'ignore' )
  except :
   o00O00O0O0O = 'addonException: addon_log'
  if isDebug : OooO0OO = xbmc . LOGDEBUG
  else : OooO0OO = xbmc . LOGNOTICE
  xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , o00O00O0O0O ) , level = OooO0OO )
  if 28 - 28: II111iiii
  if 28 - 28: iIii1I11I1II1 - i1IIi
  if 70 - 70: OoO0O00 . OoO0O00 - OoO0O00 / I1ii11iIi11i * OOooOOo
  if 86 - 86: i11iIiiIii + Ii1I + ooOoO0o * I11i + o0oOOo0O0Ooo
 def get_keyboard_input ( self , title ) :
  oOoO = None
  oOo = xbmc . Keyboard ( )
  oOo . setHeading ( title )
  xbmc . sleep ( 1000 )
  oOo . doModal ( )
  if ( oOo . isConfirmed ( ) ) :
   oOoO = oOo . getText ( )
  return oOoO
  if 63 - 63: Oo0Ooo
  if 57 - 57: oO0o
  if 14 - 14: Oo0Ooo . I1IiiI / Ii1I
  if 38 - 38: II111iiii % i11iIiiIii . ooOoO0o - OOooOOo + Ii1I
 def get_settings_login_info ( self ) :
  Ooooo0Oo00oO0 = __addon__ . getSetting ( 'id' )
  Iiii11I1i1Ii1 = __addon__ . getSetting ( 'pw' )
  O00 = __addon__ . getSetting ( 'selected_profile' )
  return ( Ooooo0Oo00oO0 , Iiii11I1i1Ii1 , O00 )
  if 35 - 35: o0oOOo0O0Ooo + iII111i + iII111i
  if 11 - 11: iII111i - OoO0O00 % ooOoO0o % iII111i / OoOoOO00 - OoO0O00
  if 74 - 74: iII111i * O0
 def get_selQuality ( self ) :
  try :
   oOOo0oo = [ 1080 , 720 , 480 , 360 ]
   if 80 - 80: I11i * i11iIiiIii / I1Ii111
   I11II1i = int ( __addon__ . getSetting ( 'selected_quality' ) )
   return oOOo0oo [ I11II1i ]
  except :
   None
   if 23 - 23: I1ii11iIi11i / o0oOOo0O0Ooo + I11i + I11i / II111iiii
  return 1080
  if 26 - 26: OoooooooOO
  if 12 - 12: OoooooooOO % OoOoOO00 / ooOoO0o % o0oOOo0O0Ooo
  if 29 - 29: OoooooooOO
  if 23 - 23: o0oOOo0O0Ooo . II111iiii
 def get_settings_exclusion21 ( self ) :
  Oo0O0OOOoo = __addon__ . getSetting ( 'exclusion21' )
  if Oo0O0OOOoo == 'false' :
   return False
  else :
   return True
   if 95 - 95: OoO0O00 % oO0o . O0
   if 15 - 15: ooOoO0o / Ii1I . Ii1I - i1IIi
   if 53 - 53: IiII + I1IiiI * oO0o
   if 61 - 61: i1IIi * OOooOOo / OoooooooOO . i11iIiiIii . OoOoOO00
 def get_settings_addinfo ( self ) :
  o00O = __addon__ . getSetting ( 'add_infoyn' )
  if o00O == 'false' :
   return False
  else :
   return True
   if 69 - 69: oO0o % I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - O0 % OoooooooOO
   if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
   if 4 - 4: II111iiii / ooOoO0o . iII111i
   if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
 def get_settings_thumbnail_landyn ( self ) :
  ii11i1 = int ( __addon__ . getSetting ( 'thumbnail_way' ) )
  if ii11i1 == 0 :
   return True
  else :
   return False
   if 29 - 29: I1ii11iIi11i % I1IiiI + ooOoO0o / o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
   if 42 - 42: Ii1I + oO0o
   if 76 - 76: I1Ii111 - OoO0O00
   if 70 - 70: ooOoO0o
 def set_winCredential ( self , credential ) :
  oOO = xbmcgui . Window ( 10000 )
  oOO . setProperty ( 'WAVVE_M_CREDENTIAL' , credential )
  if 10 - 10: OoOoOO00 * iII111i . I11i + II111iiii - ooOoO0o * i1IIi
  oOO . setProperty ( 'WAVVE_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
  if 56 - 56: o0oOOo0O0Ooo * IiII * II111iiii
 def get_winCredential ( self ) :
  oOO = xbmcgui . Window ( 10000 )
  return oOO . getProperty ( 'WAVVE_M_CREDENTIAL' )
  if 80 - 80: o0oOOo0O0Ooo * II111iiii % II111iiii
 def set_winEpisodeOrderby ( self , orderby ) :
  oOO = xbmcgui . Window ( 10000 )
  oOO . setProperty ( 'WAVVE_M_ORDERBY' , orderby )
  if 59 - 59: iIii1I11I1II1 + I1IiiI - o0oOOo0O0Ooo - I1IiiI + OOooOOo / I1ii11iIi11i
 def get_winEpisodeOrderby ( self ) :
  oOO = xbmcgui . Window ( 10000 )
  return oOO . getProperty ( 'WAVVE_M_ORDERBY' )
  if 24 - 24: I11i . iII111i % OOooOOo + ooOoO0o % OoOoOO00
  if 4 - 4: IiII - OoO0O00 * OoOoOO00 - I11i
  if 41 - 41: OoOoOO00 . I1IiiI * oO0o % IiII
  if 86 - 86: I1IiiI + Ii1I % i11iIiiIii * oO0o . ooOoO0o * I11i
 def add_dir ( self , label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
  if 44 - 44: oO0o
  o0o0oOoOO0 = '%s?%s' % ( self . _addon_url , urllib . urlencode ( params ) )
  if 17 - 17: IiII
  if sublabel : ooOooo000oOO = '%s < %s >' % ( label , sublabel )
  else : ooOooo000oOO = label
  if not img : img = 'DefaultFolder.png'
  if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
  if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
  oO0o0OOOO = xbmcgui . ListItem ( ooOooo000oOO )
  oO0o0OOOO . setArt ( { 'thumbnailImage' : img , 'icon' : img , 'poster' : img } )
  if 68 - 68: iII111i - I1Ii111 - I1IiiI - I1ii11iIi11i + I11i
  if infoLabels : oO0o0OOOO . setInfo ( type = "video" , infoLabels = infoLabels )
  if not isFolder : oO0o0OOOO . setProperty ( 'IsPlayable' , 'true' )
  if 10 - 10: OoooooooOO % iIii1I11I1II1
  xbmcplugin . addDirectoryItem ( self . _addon_handle , o0o0oOoOO0 , oO0o0OOOO , isFolder )
  if 54 - 54: I1Ii111 - II111iiii % OoOoOO00 % I11i % iIii1I11I1II1 + ooOoO0o
  if 15 - 15: I11i * ooOoO0o * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
  if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
  if 92 - 92: iII111i . I1Ii111
 def dp_Main_List ( self ) :
  if 31 - 31: I1Ii111 . OoOoOO00 / O0
  for o000O0o in o0oO0 :
   ooOooo000oOO = o000O0o . get ( 'title' )
   if 42 - 42: OoOoOO00
   if o000O0o . get ( 'uicode' ) == 'GENRE' :
    II = { 'mode' : 'GENRE'
 , 'uicode' : o000O0o . get ( 'came' )
    , 'genre' : '-'
 , 'subgenre' : '-'
    , 'orderby' : o000O0o . get ( 'orderby' )
 , 'ordernm' : o000O0o . get ( 'ordernm' )
 }
   elif o000O0o . get ( 'uicode' ) == 'WATCH' :
    II = { 'mode' : 'WATCH'
 , 'genre' : '-'
 }
   elif o000O0o . get ( 'uicode' ) == 'SEARCH' :
    II = { 'mode' : 'SEARCH'
 , 'genre' : '-'
 }
   else :
    II = { 'mode' : 'GNB_LIST'
 , 'uicode' : o000O0o . get ( 'uicode' )
 , 'came' : o000O0o . get ( 'came' )
 }
    if 45 - 45: O0 * o0oOOo0O0Ooo % Oo0Ooo * OoooooooOO + iII111i . OoOoOO00
   Oo0ooOo0o = True
   if 22 - 22: iIii1I11I1II1 / i11iIiiIii * iIii1I11I1II1 * II111iiii . OOooOOo / i11iIiiIii
   if o000O0o . get ( 'uicode' ) == 'XXX' :
    II [ 'mode' ] = 'XXX'
    Oo0ooOo0o = False
    if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
   self . add_dir ( ooOooo000oOO , sublabel = '' , img = '' , infoLabels = None , isFolder = Oo0ooOo0o , params = II )
  if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
 if 52 - 52: o0oOOo0O0Ooo
 if 95 - 95: Ii1I
 if 87 - 87: ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
 if 91 - 91: O0
 if 61 - 61: II111iiii
 if 64 - 64: ooOoO0o / OoOoOO00 - O0 - I11i
 if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
 if 42 - 42: OoO0O00
 if 67 - 67: I1Ii111 . iII111i . O0
 if 10 - 10: I1ii11iIi11i % I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
 if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
 if 37 - 37: iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
 if 83 - 83: I11i / I1IiiI
 if 34 - 34: IiII
 if 57 - 57: oO0o . I11i . i1IIi
 if 42 - 42: I11i + I1ii11iIi11i % O0
 if 6 - 6: oO0o
 if 68 - 68: OoOoOO00 - OoO0O00
 if 28 - 28: OoO0O00 . OOooOOo / OOooOOo + Oo0Ooo . I1ii11iIi11i
 if 1 - 1: iIii1I11I1II1 / II111iiii
 if 33 - 33: I11i
 if 18 - 18: o0oOOo0O0Ooo % iII111i * O0
 if 87 - 87: i11iIiiIii
 if 93 - 93: I1ii11iIi11i - OoO0O00 % i11iIiiIii . iII111i / iII111i - I1Ii111
 if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
 if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
 if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
 if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
 if 51 - 51: O0 + iII111i
 if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
 if 48 - 48: O0
 if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
 if 41 - 41: Ii1I - O0 - O0
 if 68 - 68: OOooOOo % I1Ii111
 if 88 - 88: iIii1I11I1II1 - ooOoO0o + OOooOOo
 if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
 if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
 if 23 - 23: O0
 if 85 - 85: Ii1I
 if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
 if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iII111i / OoOoOO00
 if 84 - 84: ooOoO0o * II111iiii + Oo0Ooo
 if 53 - 53: iII111i % II111iiii . IiII - iIii1I11I1II1 - IiII * II111iiii
 if 77 - 77: iIii1I11I1II1 * OoO0O00
 if 95 - 95: I1IiiI + i11iIiiIii
 if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
 if 80 - 80: II111iiii
 if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
 if 53 - 53: II111iiii
 if 31 - 31: OoO0O00
 if 80 - 80: I1Ii111 . i11iIiiIii - o0oOOo0O0Ooo
 if 25 - 25: OoO0O00
 if 62 - 62: OOooOOo + O0
 if 98 - 98: o0oOOo0O0Ooo
 if 51 - 51: Oo0Ooo - oO0o + II111iiii * Ii1I . I11i + oO0o
 if 78 - 78: i11iIiiIii / iII111i - Ii1I / OOooOOo + oO0o
 if 82 - 82: Ii1I
 if 46 - 46: OoooooooOO . i11iIiiIii
 if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
 if 87 - 87: Oo0Ooo . IiII
 if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
 if 55 - 55: OOooOOo . I1IiiI
 if 61 - 61: Oo0Ooo % IiII . Oo0Ooo
 if 100 - 100: I1Ii111 * O0
 def login_main ( self ) :
  if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
  ( o0 , iI11I1II , Ii1IIiI1i ) = self . get_settings_login_info ( )
  if 92 - 92: IiII . IiII + OoO0O00
  if 9 - 9: I1IiiI * O0 + IiII - I11i * I1Ii111
  if not ( o0 and iI11I1II ) :
   IIIiI11ii = xbmcgui . Dialog ( )
   Oooo0oOO = IIIiI11ii . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
   if Oooo0oOO == True :
    __addon__ . openSettings ( )
    sys . exit ( )
    if 81 - 81: O0 - ooOoO0o / o0oOOo0O0Ooo % Ii1I
  oOO0O00Oo0O0o = datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' )
  if 13 - 13: OoooooooOO
  if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
  if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINWAIT' ) == 'TRUE' :
   O0oO = 0
   while True :
    O0oO += 1
    if 73 - 73: I1ii11iIi11i * i11iIiiIii % oO0o . I1ii11iIi11i
    time . sleep ( 0.05 )
    if 66 - 66: oO0o + oO0o + ooOoO0o / iII111i + OOooOOo
    if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINTIME' ) == oOO0O00Oo0O0o : return
    if O0oO > 600 : return
  else :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'TRUE' )
   if 30 - 30: O0
  if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINTIME' ) == oOO0O00Oo0O0o :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
   return
   if 44 - 44: oO0o / I11i / I11i
  if not self . WavveObj . GetCredential ( o0 , iI11I1II , Ii1IIiI1i ) :
   self . addon_noti ( __language__ ( 30103 ) . encode ( 'utf8' ) )
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
   sys . exit ( )
   if 87 - 87: Oo0Ooo . I1IiiI - II111iiii + O0 / Oo0Ooo / oO0o
   if 25 - 25: I1IiiI . I1IiiI - OoOoOO00 % OoOoOO00 - i11iIiiIii / I1Ii111
  self . set_winCredential ( self . WavveObj . LoadCredential ( ) )
  self . set_winEpisodeOrderby ( 'desc' )
  xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
  if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * IiII
  if 73 - 73: OoO0O00 + OoooooooOO - O0 - Ii1I - II111iiii
  if 99 - 99: ooOoO0o . Ii1I + I1Ii111 + OoooooooOO % o0oOOo0O0Ooo
  if 51 - 51: iIii1I11I1II1
 def dp_setEpOrderby ( self , args ) :
  iIIiIi1 = args . get ( 'orderby' )
  if 74 - 74: iII111i + o0oOOo0O0Ooo
  self . set_winEpisodeOrderby ( iIIiIi1 )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 71 - 71: Oo0Ooo % OOooOOo
  if 98 - 98: I11i % i11iIiiIii % ooOoO0o + Ii1I
  if 78 - 78: I1ii11iIi11i % oO0o / iII111i - iIii1I11I1II1
  if 69 - 69: I1Ii111
 def dp_Gnb_List ( self , args ) :
  if 11 - 11: I1IiiI
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 16 - 16: Ii1I + IiII * O0 % i1IIi . I1IiiI
  Oo0OO = self . WavveObj . GetGnList ( args . get ( 'uicode' ) )
  if 78 - 78: OOooOOo - OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii
  if 29 - 29: I1IiiI % I1IiiI
  if 94 - 94: iIii1I11I1II1 / Oo0Ooo % iII111i * iII111i * II111iiii
  if 29 - 29: OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / OOooOOo * iIii1I11I1II1
  for O0OO in Oo0OO :
   ooOooo000oOO = O0OO . get ( 'title' )
   II = { 'mode' : 'GN_LIST' if O0OO . get ( 'uicode' ) != 'CY1' else 'GN_MYVIEW'
   , 'uicode' : O0OO . get ( 'uicode' )
 , 'came' : args . get ( 'came' )
 , 'page' : '1'
 }
   if 6 - 6: iIii1I11I1II1 % i11iIiiIii % I1ii11iIi11i
   self . add_dir ( ooOooo000oOO , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = II )
  if len ( Oo0OO ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 93 - 93: IiII * OoooooooOO + ooOoO0o
  if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
  if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
  if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
 def dp_Myview_Group ( self , args ) :
  ooOooo000oOO = 'VOD 시청내역'
  II = { 'mode' : 'MYVIEW_LIST'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
  self . add_dir ( ooOooo000oOO , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = II )
  if 26 - 26: Ii1I % I1ii11iIi11i
  ooOooo000oOO = '영화 시청내역'
  II [ 'uicode' ] = 'movie'
  self . add_dir ( ooOooo000oOO , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = II )
  if 76 - 76: IiII * iII111i
  xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 52 - 52: OOooOOo
  if 19 - 19: I1IiiI
  if 25 - 25: Ii1I / ooOoO0o
  if 31 - 31: OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + IiII
 def dp_Myview_List ( self , args ) :
  if 71 - 71: I1Ii111 . II111iiii
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  oo0 = self . get_settings_addinfo ( )
  if 61 - 61: OoOoOO00 - OOooOOo - i1IIi
  IiI1iIiIIIii = args . get ( 'uicode' )
  oOoOoOoO00O0 = int ( args . get ( 'page' ) )
  OO , Ii1iI111II1I1 = self . WavveObj . GetMyviewList ( IiI1iIiIIIii , oOoOoOoO00O0 , addinfoyn = oo0 )
  if 91 - 91: OOooOOo % OOooOOo - I1IiiI
  for I1iiii1I in OO :
   ooOooo000oOO = I1iiii1I . get ( 'title' )
   OOo0 = I1iiii1I . get ( 'subtitle' )
   oO00ooooO0o = I1iiii1I . get ( 'thumbnail' )
   if 75 - 75: i1IIi / O0 * o0oOOo0O0Ooo
   IiI1iiiIii = I1iiii1I . get ( 'info' )
   if IiI1iIiIIIii == 'movie' and oo0 == True :
    ooOooo000oOO = '%s (%s)' % ( ooOooo000oOO , str ( IiI1iiiIii . get ( 'year' ) ) )
   else :
    IiI1iiiIii [ 'plot' ] = ooOooo000oOO
    if 7 - 7: I1Ii111 * OoO0O00 - ooOoO0o + OOooOOo * I1IiiI % OoO0O00
   if IiI1iIiIIIii == 'vod' :
    II = { 'mode' : 'DEEP_LIST'
 , 'contentid' : I1iiii1I . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : ooOooo000oOO
    , 'subtitle' : OOo0
    , 'thumbnail' : oO00ooooO0o
    , 'viewage' : I1iiii1I . get ( 'viewage' )
 }
    Oo0ooOo0o = True
    if 15 - 15: OoOoOO00 % I1IiiI * I11i
   else :
    II = { 'mode' : 'MOVIE'
 , 'contentid' : I1iiii1I . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : ooOooo000oOO
    , 'subtitle' : OOo0
    , 'thumbnail' : oO00ooooO0o
    , 'viewage' : I1iiii1I . get ( 'viewage' )
 }
    Oo0ooOo0o = False
    if 81 - 81: ooOoO0o - iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * I11i
   if I1iiii1I . get ( 'viewage' ) == '21' : OOo0 += ' (%s)' % ( I1iiii1I . get ( 'viewage' ) )
   if 20 - 20: oO0o % IiII
   self . add_dir ( ooOooo000oOO , sublabel = OOo0 , img = oO00ooooO0o , infoLabels = IiI1iiiIii , isFolder = Oo0ooOo0o , params = II )
   if 19 - 19: I1ii11iIi11i % IiII + ooOoO0o / I1Ii111 . ooOoO0o
  if Ii1iI111II1I1 :
   if 12 - 12: i1IIi + i1IIi - I1ii11iIi11i * Oo0Ooo % Oo0Ooo - II111iiii
   II [ 'mode' ] = 'MYVIEW_LIST'
   II [ 'uicode' ] = IiI1iIiIIIii
   II [ 'page' ] = str ( oOoOoOoO00O0 + 1 )
   ooOooo000oOO = '[B]%s >>[/B]' % '다음 페이지'
   OOo0 = str ( oOoOoOoO00O0 + 1 )
   self . add_dir ( ooOooo000oOO , sublabel = OOo0 , img = '' , infoLabels = None , isFolder = True , params = II )
   if 52 - 52: ooOoO0o . iII111i + I1Ii111
  if len ( OO ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 38 - 38: i1IIi - II111iiii . I1Ii111
  if 58 - 58: I1IiiI . iII111i + OoOoOO00
  if 66 - 66: iII111i / oO0o * OoooooooOO + OoooooooOO % I11i
  if 49 - 49: oO0o - i11iIiiIii . I1Ii111 * Ii1I % iII111i + i1IIi
  if 71 - 71: o0oOOo0O0Ooo
 def dp_Genre_Group ( self , args ) :
  if 38 - 38: oO0o % OoOoOO00 + I1ii11iIi11i . i11iIiiIii
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 53 - 53: i11iIiiIii * iII111i
  OooooO0oOOOO = args . get ( 'mode' )
  o0O00oOOoo = args . get ( 'uicode' )
  i1I1iIi = args . get ( 'genre' )
  IIii11Ii1i1I = args . get ( 'subgenre' )
  iIIiIi1 = args . get ( 'orderby' )
  Oooo0O = args . get ( 'ordernm' )
  if 90 - 90: iIii1I11I1II1 % ooOoO0o
  if i1I1iIi == '-' :
   OoO0O00O0oo0O = self . WavveObj . GetGenreGroup ( o0O00oOOoo , i1I1iIi , iIIiIi1 , Oooo0O , exclusion21 = self . get_settings_exclusion21 ( ) )
  else :
   I1IiI11 = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 , 'orderby' : iIIiIi1
 , 'ordernm' : Oooo0O
 }
   if 9 - 9: I11i
   OoO0O00O0oo0O = self . WavveObj . GetGenreGroup_sub ( I1IiI11 )
   if 64 - 64: iIii1I11I1II1 / I1IiiI . II111iiii + OoooooooOO . OoO0O00
   if 56 - 56: Oo0Ooo . I1ii11iIi11i . I1IiiI
  for ii111I in OoO0O00O0oo0O :
   ooOooo000oOO = ii111I . get ( 'title' ) + '  (' + Oooo0O + ')'
   if 17 - 17: I1IiiI . O0 + OoO0O00
   II = { 'mode' : OooooO0oOOOO
 , 'uicode' : o0O00oOOoo
   , 'genre' : ii111I . get ( 'genre' )
 , 'subgenre' : ii111I . get ( 'subgenre' )
 , 'adult' : ii111I . get ( 'adult' )
 , 'page' : '1'
 , 'broadcastid' : ii111I . get ( 'broadcastid' )
 , 'contenttype' : ii111I . get ( 'contenttype' )
 , 'uiparent' : ii111I . get ( 'uiparent' )
 , 'uirank' : ii111I . get ( 'uirank' )
 , 'uitype' : ii111I . get ( 'uitype' )
 , 'orderby' : iIIiIi1
 , 'ordernm' : Oooo0O
 }
   if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
   if o0O00oOOoo == 'moviegenre' or o0O00oOOoo == 'moviegenre_svod' or o0O00oOOoo == 'moviegenre_ppv' or ii111I . get ( 'subgenre' ) != '-' :
    II [ 'mode' ] = 'GENRE_LIST'
    if 20 - 20: I1IiiI
   else :
    if 95 - 95: iII111i - I1IiiI
    None
    if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
   self . add_dir ( ooOooo000oOO , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = II )
   if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
  if len ( OoO0O00O0oo0O ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
  if 41 - 41: i1IIi - I11i - Ii1I
  if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
  if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
 def dp_Genre_List ( self , args ) :
  if 44 - 44: II111iiii
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  oo0 = self . get_settings_addinfo ( )
  if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
  o0O00oOOoo = args . get ( 'uicode' )
  oOoOoOoO00O0 = int ( args . get ( 'page' ) )
  if 35 - 35: iIii1I11I1II1
  II = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'subgenre' : args . get ( 'subgenre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 , 'orderby' : args . get ( 'orderby' )
 }
  if args . get ( 'genre' ) == args . get ( 'subgenre' ) :
   II [ 'subgenre' ] = 'all'
   if 42 - 42: I1Ii111 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
  OoO0O00O0oo0O , Ii1iI111II1I1 = self . WavveObj . GetGenreList ( o0O00oOOoo , II , oOoOoOoO00O0 , addinfoyn = oo0 )
  if 31 - 31: iII111i . OOooOOo - ooOoO0o . OoooooooOO / OoooooooOO
  if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
  if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
  for ii111I in OoO0O00O0oo0O :
   ooOooo000oOO = ii111I . get ( 'title' )
   oO00ooooO0o = ii111I . get ( 'thumbnail' )
   if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
   IiI1iiiIii = ii111I . get ( 'info' )
   if o0O00oOOoo == 'moviegenre_svod' and oo0 == True :
    ooOooo000oOO = '%s (%s)' % ( ooOooo000oOO , str ( IiI1iiiIii . get ( 'year' ) ) )
   else :
    IiI1iiiIii [ 'plot' ] = ooOooo000oOO
    if 71 - 71: O0 - iIii1I11I1II1
   if o0O00oOOoo == 'vodgenre' :
    i1II = { 'mode' : 'DEEP_LIST'
 , 'contentid' : ii111I . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : ooOooo000oOO
    , 'subtitle' : ''
    , 'thumbnail' : oO00ooooO0o
    , 'viewage' : ii111I . get ( 'viewage' )
 }
    Oo0ooOo0o = True
    if 14 - 14: oO0o / oO0o % ooOoO0o
   else :
    i1II = { 'mode' : 'MOVIE'
 , 'contentid' : ii111I . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : ooOooo000oOO
    , 'subtitle' : ''
    , 'thumbnail' : oO00ooooO0o
    , 'viewage' : ii111I . get ( 'viewage' )
 }
    if 56 - 56: I1IiiI . O0 + Oo0Ooo
    Oo0ooOo0o = False
    if 1 - 1: iII111i
   if i1II . get ( 'viewage' ) == '21' : ooOooo000oOO += ' (%s)' % ( i1II . get ( 'viewage' ) )
   if 97 - 97: OOooOOo + iII111i + O0 + i11iIiiIii
   self . add_dir ( ooOooo000oOO , sublabel = '' , img = oO00ooooO0o , infoLabels = IiI1iiiIii , isFolder = Oo0ooOo0o , params = i1II )
   if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
  if Ii1iI111II1I1 :
   if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
   II [ 'mode' ] = 'GENRE_LIST'
   II [ 'uicode' ] = o0O00oOOoo
   II [ 'page' ] = str ( oOoOoOoO00O0 + 1 )
   ooOooo000oOO = '[B]%s >>[/B]' % '다음 페이지'
   OOo0 = str ( oOoOoOoO00O0 + 1 )
   self . add_dir ( ooOooo000oOO , sublabel = OOo0 , img = '' , infoLabels = None , isFolder = True , params = II )
   if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
  if len ( OoO0O00O0oo0O ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
  if 17 - 17: i1IIi
  if 21 - 21: Oo0Ooo
  if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
 def dp_Deeplink_List ( self , args ) :
  if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  oo0 = self . get_settings_addinfo ( )
  if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
  o0O00oOOoo = args . get ( 'uicode' )
  I1ii11 = args . get ( 'came' )
  oOoOoOoO00O0 = int ( args . get ( 'page' ) )
  if 74 - 74: Oo0Ooo - o0oOOo0O0Ooo . i1IIi
  if 43 - 43: iII111i / I1IiiI
  if 58 - 58: I1IiiI + i11iIiiIii % Ii1I . OoOoOO00
  Ii1i1iI , Ii1iI111II1I1 = self . WavveObj . GetDeeplinkList ( o0O00oOOoo , I1ii11 , oOoOoOoO00O0 , addinfoyn = oo0 )
  if 16 - 16: OOooOOo / Oo0Ooo / OoooooooOO * I1IiiI + i1IIi % OOooOOo
  for ooo0o00 in Ii1i1iI :
   ooOooo000oOO = ooo0o00 . get ( 'title' )
   OOo0 = ooo0o00 . get ( 'subtitle' )
   oO00ooooO0o = ooo0o00 . get ( 'thumbnail' )
   ooO = ooo0o00 . get ( 'uicode' )
   o0o00 = ooo0o00 . get ( 'channelepg' )
   if 14 - 14: o0oOOo0O0Ooo . OOooOOo . I11i + OoooooooOO - OOooOOo + IiII
   II = { 'uicode' : ooO
   , 'came' : I1ii11
 , 'contentid' : ooo0o00 . get ( 'contentid' )
 , 'contentidType' : ooo0o00 . get ( 'contentidType' )
 , 'page' : '1'
 , 'title' : ooOooo000oOO
   , 'subtitle' : OOo0
   , 'thumbnail' : oO00ooooO0o
   , 'viewage' : ooo0o00 . get ( 'viewage' )
 }
   if 9 - 9: Ii1I
   if ooO == 'channel' :
    II [ 'mode' ] = 'LIVE'
   elif ooO == 'movie' :
    II [ 'mode' ] = 'MOVIE'
   else :
    II [ 'mode' ] = 'DEEP_LIST'
    if 59 - 59: I1IiiI * II111iiii . O0
    if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
   IiI1iiiIii = ooo0o00 . get ( 'info' )
   if o0o00 :
    IiI1iiiIii [ 'plot' ] = '%s\n\n%s' % ( ooOooo000oOO , o0o00 )
   elif ooO == 'movie' and oo0 == True :
    ooOooo000oOO = '%s (%s)' % ( ooOooo000oOO , str ( IiI1iiiIii . get ( 'year' ) ) )
   else :
    IiI1iiiIii [ 'plot' ] = '%s\n\n%s' % ( ooOooo000oOO , OOo0 )
    if 51 - 51: O0 / ooOoO0o * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
   if ooo0o00 . get ( 'viewage' ) == '21' : OOo0 += ' (%s)' % ( ooo0o00 . get ( 'viewage' ) )
   if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + ooOoO0o % i11iIiiIii % O0
   if ooO in [ 'channel' , 'movie' ] :
    Oo0ooOo0o = False
   elif II [ 'contentidType' ] == 'direct' :
    Oo0ooOo0o = False
    II [ 'mode' ] = 'VOD'
   else :
    Oo0ooOo0o = True
    if 27 - 27: O0
    if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
   self . add_dir ( ooOooo000oOO , sublabel = OOo0 , img = oO00ooooO0o , infoLabels = IiI1iiiIii , isFolder = Oo0ooOo0o , params = II )
   if 28 - 28: i1IIi - iII111i
  if Ii1iI111II1I1 :
   if 54 - 54: iII111i - O0 % OOooOOo
   II [ 'mode' ] = 'GN_LIST'
   II [ 'uicode' ] = o0O00oOOoo
   II [ 'page' ] = str ( oOoOoOoO00O0 + 1 )
   ooOooo000oOO = '[B]%s >>[/B]' % '다음 페이지'
   OOo0 = str ( oOoOoOoO00O0 + 1 )
   self . add_dir ( ooOooo000oOO , sublabel = OOo0 , img = '' , infoLabels = None , isFolder = True , params = II )
   if 73 - 73: O0 . OoOoOO00 + I1IiiI - I11i % I11i . I11i
  if len ( Ii1i1iI ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 17 - 17: Ii1I - OoooooooOO % Ii1I . IiII / i11iIiiIii % iII111i
  if 28 - 28: I11i
  if 58 - 58: OoOoOO00
  if 37 - 37: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i
 def dp_Episodelink_List ( self , args ) :
  if 73 - 73: i11iIiiIii - IiII
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 25 - 25: OoooooooOO + IiII * I1ii11iIi11i
  OoO0ooO = args . get ( 'contentid' )
  O000 = args . get ( 'contentidType' )
  IiI1iIiIIIii = args . get ( 'uicode' )
  if 7 - 7: iII111i / I1ii11iIi11i / i11iIiiIii
  oOoOoOoO00O0 = int ( args . get ( 'page' ) )
  if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
  OoOo , Ii1iI111II1I1 = self . WavveObj . GetEpisodeList ( OoO0ooO , IiI1iIiIIIii , O000 , oOoOoOoO00O0 , orderby = self . get_winEpisodeOrderby ( ) )
  if 35 - 35: ooOoO0o * OOooOOo . I11i * o0oOOo0O0Ooo . OoOoOO00 / O0
  for O00O0ooo0 in OoOo :
   ooOooo000oOO = O00O0ooo0 . get ( 'title' )
   OOo0 = O00O0ooo0 . get ( 'subtitle' )
   oO00ooooO0o = O00O0ooo0 . get ( 'thumbnail' )
   II = { 'mode' : 'VOD'
 , 'uicode' : O00O0ooo0 . get ( 'uicode' )
   , 'contentid' : O00O0ooo0 . get ( 'contentid' )
 , 'programid' : O00O0ooo0 . get ( 'programid' )
 , 'title' : ooOooo000oOO
   , 'subtitle' : OOo0
   , 'thumbnail' : oO00ooooO0o
   , 'viewage' : O00O0ooo0 . get ( 'viewage' )
 }
   if 8 - 8: ooOoO0o + II111iiii / iII111i / I11i
   if O00O0ooo0 . get ( 'viewage' ) == '21' : OOo0 += ' (%s)' % ( O00O0ooo0 . get ( 'viewage' ) )
   if 74 - 74: O0 / i1IIi
   OoO = O00O0ooo0 . get ( 'info' )
   OoO [ 'plot' ] = O00O0ooo0 . get ( 'synopsis' )
   if 41 - 41: i1IIi * II111iiii / OoooooooOO . OOooOOo
   if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
   if 100 - 100: OoO0O00
   if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
   self . add_dir ( ooOooo000oOO , sublabel = OOo0 , img = oO00ooooO0o , infoLabels = OoO , isFolder = False , params = II )
   if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
  if oOoOoOoO00O0 == 1 :
   IiI1iiiIii = { 'plot' : '정렬순서를 변경합니다.' }
   II = { }
   II [ 'mode' ] = 'ORDER_BY'
   if self . get_winEpisodeOrderby ( ) == 'desc' :
    ooOooo000oOO = '정렬순서변경 : 최신화부터 -> 1회부터'
    II [ 'orderby' ] = 'asc'
   else :
    ooOooo000oOO = '정렬순서변경 : 1회부터 -> 최신화부터'
    II [ 'orderby' ] = 'desc'
   self . add_dir ( ooOooo000oOO , sublabel = '' , img = '' , infoLabels = IiI1iiiIii , isFolder = False , params = II )
   if 45 - 45: I1Ii111
  if Ii1iI111II1I1 :
   if 83 - 83: OoOoOO00 . OoooooooOO
   II [ 'mode' ] = 'DEEP_LIST'
   II [ 'uicode' ] = IiI1iIiIIIii
   II [ 'contentid' ] = OoO0ooO
   II [ 'contentidType' ] = O000
   II [ 'page' ] = str ( oOoOoOoO00O0 + 1 )
   ooOooo000oOO = '[B]%s >>[/B]' % '다음 페이지'
   OOo0 = str ( oOoOoOoO00O0 + 1 )
   self . add_dir ( ooOooo000oOO , sublabel = OOo0 , img = '' , infoLabels = None , isFolder = True , params = II )
   if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
  if len ( OoOo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 62 - 62: OoO0O00 / I1ii11iIi11i
  if 7 - 7: OoooooooOO . IiII
  if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
 def play_VIDEO ( self , args ) :
  if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
  OoO0ooO = args . get ( 'contentid' )
  IiI1iIiIIIii = args . get ( 'uicode' )
  oo00O00oO000o = self . get_selQuality ( )
  if 71 - 71: I1ii11iIi11i - ooOoO0o / OoOoOO00 * OoOoOO00 / i1IIi . i1IIi
  self . addon_log ( OoO0ooO + ' - ' + IiI1iIiIIIii , False )
  ooo000ooO0000 , oOoooo000Oo00 , OOoo , o00O00oO00 = self . WavveObj . GetStreamingURL ( OoO0ooO , IiI1iIiIIIii , oo00O00oO000o )
  if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * IiII
  if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  I1IIIiI1I1ii1 = '%s|Cookie=%s' % ( ooo000ooO0000 , oOoooo000Oo00 )
  self . addon_log ( I1IIIiI1I1ii1 , False )
  if 30 - 30: O0 * OoooooooOO
  if ooo000ooO0000 == '' :
   self . addon_noti ( __language__ ( 30303 ) . encode ( 'utf8' ) )
   return
   if 38 - 38: IiII - I1ii11iIi11i . OoOoOO00 - I1Ii111 . OoooooooOO
  ooo = xbmcgui . ListItem ( path = I1IIIiI1I1ii1 )
  if 70 - 70: II111iiii % i1IIi / I1ii11iIi11i . OoooooooOO * Oo0Ooo
  if OOoo :
   if 43 - 43: oO0o - OoooooooOO
   if 3 - 3: O0 / iII111i
   iIiIi1I = OOoo [ 'customdata' ]
   iiii11i = OOoo [ 'drmhost' ]
   if 35 - 35: I1ii11iIi11i * iII111i - OoO0O00 % o0oOOo0O0Ooo
   oOo00O000Oo0 = 'mpd'
   I1iI1I1I1i11i = 'com.widevine.alpha'
   if 39 - 39: II111iiii / IiII + Ii1I
   OOoO000 = inputstreamhelper . Helper ( oOo00O000Oo0 , drm = I1iI1I1I1i11i )
   if 57 - 57: II111iiii
   if OOoO000 . check_inputstream ( ) :
    if 54 - 54: Oo0Ooo + oO0o + i11iIiiIii
    if IiI1iIiIIIii == 'movie' :
     i1i1ii111 = 'https://www.wavve.com/player/movie?movieid=%s' % OoO0ooO
    else :
     i1i1ii111 = 'https://www.wavve.com/player/vod?programid=%s&page=1' % OoO0ooO
     if 3 - 3: II111iiii / OOooOOo + IiII . ooOoO0o . OoO0O00
    oOoo000 = { 'content-type' : 'application/octet-stream'
 , 'origin' : 'https://www.wavve.com'
 , 'pallycon-customdata' : iIiIi1I
 , 'referer' : i1i1ii111
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'

    , 'user-agent' : OOoO
 }
    OooOo00o = iiii11i + '|' + urllib . urlencode ( oOoo000 ) + '|R{SSM}|'
    if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
    ooo . setProperty ( 'inputstreamaddon' , OOoO000 . inputstream_addon )
    ooo . setProperty ( 'inputstream.adaptive.manifest_type' , oOo00O000Oo0 )
    ooo . setProperty ( 'inputstream.adaptive.license_type' , I1iI1I1I1i11i )
    if 13 - 13: Oo0Ooo
    ooo . setProperty ( 'inputstream.adaptive.license_key' , OooOo00o )
    ooo . setProperty ( 'inputstream.adaptive.stream_headers' , 'Cookie=%s' % oOoooo000Oo00 )
    if 60 - 60: I1ii11iIi11i * I1IiiI
  xbmcplugin . setResolvedUrl ( self . _addon_handle , True , ooo )
  if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
  if o00O00oO00 :
   self . addon_noti ( o00O00oO00 . encode ( 'utf-8' ) )
  else :
   if '/preview.' in urlparse . urlsplit ( ooo000ooO0000 ) . path : self . addon_noti ( __language__ ( 30401 ) . encode ( 'utf8' ) )
   if 41 - 41: Ii1I
  try :
   if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) and args . get ( 'viewage' ) != '21' :
    II = { 'code' : args . get ( 'programid' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'contentid' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 , 'subtitle' : args . get ( 'subtitle' )
 }
    self . Save_Watched_List ( args . get ( 'mode' ) . lower ( ) , II )
  except :
   None
   if 77 - 77: I1Ii111
   if 65 - 65: II111iiii . I1IiiI % oO0o * OoO0O00
   if 38 - 38: OoOoOO00 / iII111i % Oo0Ooo
   if 11 - 11: iII111i - oO0o + II111iiii - iIii1I11I1II1
 def dp_Watch_List ( self , args ) :
  i1I1iIi = args . get ( 'genre' )
  if 7 - 7: IiII - I11i / II111iiii * Ii1I . iII111i * iII111i
  if i1I1iIi == '-' :
   ooOooo000oOO = 'VOD 시청내역'
   II = { 'mode' : 'WATCH'
 , 'genre' : 'vod'
 }
   self . add_dir ( ooOooo000oOO , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = II )
   if 61 - 61: I11i % ooOoO0o - OoO0O00 / Oo0Ooo
   ooOooo000oOO = '영화 시청내역'
   II [ 'genre' ] = 'movie'
   self . add_dir ( ooOooo000oOO , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = II )
   if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
   xbmcplugin . endOfDirectory ( self . _addon_handle )
   if 85 - 85: OoooooooOO * iIii1I11I1II1 . iII111i / OoooooooOO % I1IiiI % O0
  else :
   I1iii = self . Load_Watched_List ( i1I1iIi )
   if 86 - 86: I1ii11iIi11i * O0 * IiII
   for Ooo0oo in I1iii :
    IIi11IIiIii1 = dict ( urlparse . parse_qsl ( Ooo0oo ) )
    if 17 - 17: Ii1I + oO0o . OoO0O00 - Oo0Ooo * i11iIiiIii
    ooOooo000oOO = IIi11IIiIii1 . get ( 'title' ) . strip ( )
    OOo0 = IIi11IIiIii1 . get ( 'subtitle' ) . strip ( )
    if OOo0 == 'None' : OOo0 = ''
    oO00ooooO0o = IIi11IIiIii1 . get ( 'img' )
    if 20 - 20: I1IiiI . OoooooooOO % OOooOOo
    if 63 - 63: I1IiiI % iIii1I11I1II1
    IiI1iiiIii = { }
    if i1I1iIi == 'movie' and self . get_settings_addinfo ( ) == True :
     I1ii = self . WavveObj . GetMovieInfoList ( [ IIi11IIiIii1 . get ( 'code' ) ] )
     IiI1iiiIii = I1ii . get ( IIi11IIiIii1 . get ( 'code' ) )
    else :
     IiI1iiiIii [ 'plot' ] = '%s\n%s' % ( ooOooo000oOO , OOo0 )
     if 73 - 73: IiII + I1IiiI * Oo0Ooo * OoooooooOO
    if i1I1iIi == 'vod' :
     II = { 'mode' : 'DEEP_LIST'
 , 'contentid' : IIi11IIiIii1 . get ( 'code' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
     Oo0ooOo0o = True
    else :
     II = { 'mode' : 'MOVIE'
 , 'contentid' : IIi11IIiIii1 . get ( 'code' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'title' : ooOooo000oOO
 , 'thumbnail' : oO00ooooO0o
 }
     Oo0ooOo0o = False
     if 95 - 95: i1IIi + iIii1I11I1II1 % I1ii11iIi11i % Oo0Ooo / i11iIiiIii - IiII
    self . add_dir ( ooOooo000oOO , sublabel = OOo0 , img = oO00ooooO0o , infoLabels = IiI1iiiIii , isFolder = Oo0ooOo0o , params = II )
    if 26 - 26: ooOoO0o . OOooOOo - OOooOOo . OoO0O00
   IiI1iiiIii = { 'plot' : '시청목록을 삭제합니다.' }
   ooOooo000oOO = '*** 시청목록 삭제 ***'
   II = { 'mode' : 'MYVIEW_REMOVE'
 , 'genre' : i1I1iIi
 }
   if 39 - 39: OoooooooOO + oO0o % OOooOOo / OOooOOo
   self . add_dir ( ooOooo000oOO , sublabel = '' , img = '' , infoLabels = IiI1iiiIii , isFolder = False , params = II )
   if 27 - 27: iII111i . I11i . iIii1I11I1II1 . iIii1I11I1II1
   xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
   if 20 - 20: o0oOOo0O0Ooo / i1IIi
   if 71 - 71: OoOoOO00 . i1IIi
   if 94 - 94: OOooOOo . I1Ii111
   if 84 - 84: O0 . I11i - II111iiii . ooOoO0o / II111iiii
   if 47 - 47: OoooooooOO
 def dp_Search_Group ( self , args ) :
  ooOooo000oOO = 'VOD 검색'
  II = { 'mode' : 'SEARCH_LIST'
 , 'genre' : 'vod'
 , 'page' : '1'
 }
  self . add_dir ( ooOooo000oOO , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = II )
  if 4 - 4: I1IiiI % I11i
  ooOooo000oOO = '영화 검색'
  II [ 'genre' ] = 'movie'
  self . add_dir ( ooOooo000oOO , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = II )
  if 10 - 10: IiII . OoooooooOO - OoO0O00 + IiII - O0
  xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 82 - 82: ooOoO0o + II111iiii
  if 39 - 39: oO0o % iIii1I11I1II1 % O0 % OoooooooOO * I1ii11iIi11i + iII111i
  if 68 - 68: Oo0Ooo + i11iIiiIii
  if 69 - 69: iIii1I11I1II1 * iIii1I11I1II1 * i11iIiiIii + I1IiiI / OOooOOo % Ii1I
 def dp_Search_List ( self , args ) :
  if 58 - 58: OOooOOo * o0oOOo0O0Ooo + O0 % OOooOOo
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  oo0 = self . get_settings_addinfo ( )
  if 25 - 25: Oo0Ooo % I1ii11iIi11i * ooOoO0o
  IiI1iIiIIIii = args . get ( 'genre' )
  oOoOoOoO00O0 = int ( args . get ( 'page' ) )
  if 6 - 6: iII111i . IiII * OoOoOO00 . i1IIi
  if 'search_key' in args :
   oOOo = args . get ( 'search_key' )
  else :
   oOOo = self . get_keyboard_input ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
   if not oOOo : return
   if 46 - 46: IiII + iIii1I11I1II1 + OOooOOo + OoO0O00 . I1ii11iIi11i
  iIiIi11Ii , Ii1iI111II1I1 = self . WavveObj . GetSearchList ( oOOo , IiI1iIiIIIii , oOoOoOoO00O0 , exclusion21 = self . get_settings_exclusion21 ( ) , addinfoyn = oo0 )
  if 23 - 23: oO0o - OOooOOo + I11i
  for II11 in iIiIi11Ii :
   ooOooo000oOO = II11 . get ( 'title' )
   oO00ooooO0o = II11 . get ( 'thumbnail' )
   if 30 - 30: i11iIiiIii % iIii1I11I1II1 . I11i % iIii1I11I1II1
   IiI1iiiIii = II11 . get ( 'info' )
   if IiI1iIiIIIii == 'movie' and oo0 == True :
    ooOooo000oOO = '%s (%s)' % ( ooOooo000oOO , str ( IiI1iiiIii . get ( 'year' ) ) )
   else :
    IiI1iiiIii [ 'plot' ] = ooOooo000oOO
    if 62 - 62: Oo0Ooo * OoOoOO00
   if IiI1iIiIIIii == 'vod' :
    II = { 'mode' : 'DEEP_LIST'
 , 'contentid' : II11 . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : ooOooo000oOO
    , 'subtitle' : ''
    , 'thumbnail' : oO00ooooO0o
    , 'viewage' : II11 . get ( 'viewage' )
 }
    Oo0ooOo0o = True
    if 79 - 79: OoO0O00 . iII111i * Ii1I - OOooOOo + ooOoO0o
   else :
    II = { 'mode' : 'MOVIE'
 , 'contentid' : II11 . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : ooOooo000oOO
    , 'subtitle' : ''
    , 'thumbnail' : oO00ooooO0o
    , 'viewage' : II11 . get ( 'viewage' )
 }
    if 14 - 14: i11iIiiIii - iII111i * OoOoOO00
    Oo0ooOo0o = False
    if 51 - 51: I1ii11iIi11i / iIii1I11I1II1 % oO0o + o0oOOo0O0Ooo * ooOoO0o + I1Ii111
   if II . get ( 'viewage' ) == '21' : ooOooo000oOO += ' (%s)' % ( II . get ( 'viewage' ) )
   if 77 - 77: ooOoO0o * OoOoOO00
   self . add_dir ( ooOooo000oOO , sublabel = '' , img = oO00ooooO0o , infoLabels = IiI1iiiIii , isFolder = Oo0ooOo0o , params = II )
   if 14 - 14: I11i % I11i / IiII
  if Ii1iI111II1I1 :
   if 72 - 72: i1IIi - II111iiii - OOooOOo + OOooOOo * o0oOOo0O0Ooo * OOooOOo
   II [ 'mode' ] = 'SEARCH_LIST'
   II [ 'genre' ] = IiI1iIiIIIii
   II [ 'page' ] = str ( oOoOoOoO00O0 + 1 )
   II [ 'search_key' ] = oOOo
   ooOooo000oOO = '[B]%s >>[/B]' % '다음 페이지'
   OOo0 = str ( oOoOoOoO00O0 + 1 )
   self . add_dir ( ooOooo000oOO , sublabel = OOo0 , img = '' , infoLabels = None , isFolder = True , params = II )
   if 33 - 33: Oo0Ooo
  if len ( iIiIi11Ii ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 49 - 49: OoO0O00 % iII111i % iII111i / iII111i
  if 53 - 53: iIii1I11I1II1
  if 68 - 68: OoooooooOO % II111iiii
  if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
  if 24 - 24: II111iiii % I1Ii111 - ooOoO0o + I1IiiI * I1ii11iIi11i
 def Load_Watched_List ( self , genre ) :
  try :
   i11111I1I = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   with open ( i11111I1I , 'r' ) as Ooo0ooOOOOoOo :
    Iii = Ooo0ooOOOOoOo . readlines ( )
  except :
   Iii = [ ]
   if 6 - 6: OOooOOo - I1ii11iIi11i + Ii1I + i1IIi / O0 / o0oOOo0O0Ooo
  return Iii
  if 42 - 42: i1IIi . I1IiiI / i1IIi + Ii1I
  if 54 - 54: ooOoO0o % OOooOOo . I1Ii111 + oO0o - OOooOOo * I1IiiI
  if 92 - 92: o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % OoO0O00 % IiII . OoooooooOO
  if 52 - 52: ooOoO0o / i11iIiiIii - OOooOOo . IiII % iIii1I11I1II1 + o0oOOo0O0Ooo
 def Save_Watched_List ( self , genre , in_params ) :
  try :
   i11111I1I = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   OO00oOooo0O = self . Load_Watched_List ( genre )
   if 58 - 58: Oo0Ooo / oO0o
   with open ( i11111I1I , 'w' ) as Ooo0ooOOOOoOo :
    iIII1I1i1i = urllib . urlencode ( in_params )
    iIII1I1i1i = iIII1I1i1i . encode ( 'utf-8' ) + '\n'
    Ooo0ooOOOOoOo . write ( iIII1I1i1i )
    if 79 - 79: Ii1I . OoO0O00
    IIiI1I1 = 0
    for I11I1IIiiII1 in OO00oOooo0O :
     IIIIIii1ii11 = dict ( urlparse . parse_qsl ( I11I1IIiiII1 ) )
     if in_params . get ( 'code' ) != IIIIIii1ii11 . get ( 'code' ) :
      Ooo0ooOOOOoOo . write ( I11I1IIiiII1 )
      IIiI1I1 += 1
      if IIiI1I1 >= 50 : break
  except :
   None
   if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / OOooOOo
   if 11 - 11: I1IiiI * oO0o + I1ii11iIi11i / I1ii11iIi11i
   if 37 - 37: i11iIiiIii + i1IIi
   if 23 - 23: iII111i + I11i . OoOoOO00 * I1IiiI + I1ii11iIi11i
 def Delete_Watched_List ( self , genre ) :
  try :
   i11111I1I = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   with open ( i11111I1I , 'w' ) as Ooo0ooOOOOoOo :
    Ooo0ooOOOOoOo . write ( '' )
  except :
   None
   if 18 - 18: IiII * o0oOOo0O0Ooo . IiII / O0
   if 8 - 8: o0oOOo0O0Ooo
   if 4 - 4: I1ii11iIi11i + I1ii11iIi11i * ooOoO0o - OoOoOO00
   if 78 - 78: Ii1I / II111iiii % OoOoOO00
 def dp_WatchList_Delete ( self , args ) :
  i1I1iIi = args . get ( 'genre' )
  if 52 - 52: OOooOOo - iII111i * oO0o
  IIIiI11ii = xbmcgui . Dialog ( )
  Oooo0oOO = IIIiI11ii . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if Oooo0oOO == False : sys . exit ( )
  if 17 - 17: OoooooooOO + OOooOOo * I11i * OoOoOO00
  self . Delete_Watched_List ( i1I1iIi )
  if 36 - 36: O0 + Oo0Ooo
  xbmc . executebuiltin ( "Container.Refresh" )
  if 5 - 5: Oo0Ooo * OoOoOO00
  if 46 - 46: ooOoO0o
  if 33 - 33: iII111i - II111iiii * OoooooooOO - Oo0Ooo - OOooOOo
  if 84 - 84: I1Ii111 + Oo0Ooo - OoOoOO00 * OoOoOO00
  if 61 - 61: OoooooooOO . oO0o . OoooooooOO / Oo0Ooo
  if 72 - 72: i1IIi
  if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i . OoooooooOO
  if 63 - 63: I1ii11iIi11i
  if 6 - 6: ooOoO0o / I1ii11iIi11i
  if 57 - 57: I11i
  if 67 - 67: OoO0O00 . ooOoO0o
 def wavve_main ( self ) :
  if 87 - 87: oO0o % Ii1I
  OooooO0oOOOO = self . main_params . get ( 'mode' , None )
  if 83 - 83: II111iiii - I11i
  self . login_main ( )
  if OooooO0oOOOO is None :
   if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
   self . dp_Main_List ( )
   if 86 - 86: iIii1I11I1II1 + OoOoOO00 . i11iIiiIii - Ii1I
   if 51 - 51: OoOoOO00
   if 14 - 14: IiII % oO0o % Oo0Ooo - i11iIiiIii
   if 53 - 53: Ii1I % Oo0Ooo
   if 59 - 59: OOooOOo % iIii1I11I1II1 . i1IIi + II111iiii * IiII
   if 41 - 41: Ii1I % I1ii11iIi11i
   if 12 - 12: OOooOOo
   if 69 - 69: OoooooooOO + OOooOOo
   if 26 - 26: Oo0Ooo + OOooOOo / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
  elif OooooO0oOOOO == 'GNB_LIST' :
   self . dp_Gnb_List ( self . main_params )
   if 31 - 31: I11i % OOooOOo * I11i
  elif OooooO0oOOOO == 'GN_LIST' :
   self . dp_Deeplink_List ( self . main_params )
   if 45 - 45: i1IIi . I1IiiI + OOooOOo - OoooooooOO % ooOoO0o
  elif OooooO0oOOOO == 'DEEP_LIST' :
   IiI1iIiIIIii = self . main_params . get ( 'uicode' , None )
   if 1 - 1: iIii1I11I1II1
   if IiI1iIiIIIii in [ 'quick' , 'vod' , 'program' , 'x' ] :
    self . dp_Episodelink_List ( self . main_params )
    if 93 - 93: i1IIi . i11iIiiIii . Oo0Ooo
   else : None
   if 99 - 99: I11i - I1Ii111 - oO0o % OoO0O00
  elif OooooO0oOOOO in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
   self . play_VIDEO ( self . main_params )
   if 21 - 21: II111iiii % I1ii11iIi11i . i1IIi - OoooooooOO
   time . sleep ( 0.1 )
   if 4 - 4: OoooooooOO . ooOoO0o
  elif OooooO0oOOOO == 'GN_MYVIEW' :
   self . dp_Myview_Group ( self . main_params )
   if 78 - 78: I1ii11iIi11i + I11i - O0
  elif OooooO0oOOOO == 'MYVIEW_LIST' :
   self . dp_Myview_List ( self . main_params )
   if 10 - 10: I1Ii111 % I1IiiI
  elif OooooO0oOOOO == 'GENRE' :
   self . dp_Genre_Group ( self . main_params )
   if 97 - 97: OoooooooOO - I1Ii111
  elif OooooO0oOOOO == 'GENRE_LIST' :
   self . dp_Genre_List ( self . main_params )
   if 58 - 58: iIii1I11I1II1 + O0
  elif OooooO0oOOOO == 'WATCH' :
   self . dp_Watch_List ( self . main_params )
   if 30 - 30: ooOoO0o % iII111i * OOooOOo - I1ii11iIi11i * Ii1I % ooOoO0o
  elif OooooO0oOOOO == 'MYVIEW_REMOVE' :
   self . dp_WatchList_Delete ( self . main_params )
   if 46 - 46: i11iIiiIii - O0 . oO0o
  elif OooooO0oOOOO == 'SEARCH' :
   self . dp_Search_Group ( self . main_params )
   if 100 - 100: I1IiiI / o0oOOo0O0Ooo * iII111i . O0 / OOooOOo
  elif OooooO0oOOOO == 'SEARCH_LIST' :
   self . dp_Search_List ( self . main_params )
   if 83 - 83: I1Ii111
  elif OooooO0oOOOO == 'ORDER_BY' :
   self . dp_setEpOrderby ( self . main_params )
   if 48 - 48: II111iiii * OOooOOo * I1Ii111
  else :
   None
   if 50 - 50: IiII % i1IIi
   if 21 - 21: OoooooooOO - iIii1I11I1II1
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
