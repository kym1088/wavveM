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
 def get_settings_exclusion21 ( self ) :
  iI = __addon__ . getSetting ( 'exclusion21' )
  if iI == 'false' :
   return False
  else :
   return True
   if 28 - 28: OOooOOo - IiII . IiII + OoOoOO00 - OoooooooOO + O0
   if 95 - 95: OoO0O00 % oO0o . O0
   if 15 - 15: ooOoO0o / Ii1I . Ii1I - i1IIi
 def get_settings_thumbnail_landyn ( self ) :
  o00oOO0 = int ( __addon__ . getSetting ( 'thumbnail_way' ) )
  if o00oOO0 == 0 :
   return True
  else :
   return False
   if 95 - 95: OOooOOo / OoooooooOO
   if 18 - 18: i11iIiiIii
   if 46 - 46: i1IIi / I11i % OOooOOo + I1Ii111
   if 79 - 79: I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - iII111i
 def set_winCredential ( self , credential ) :
  i1Iii = xbmcgui . Window ( 10000 )
  i1Iii . setProperty ( 'WAVVE_M_CREDENTIAL' , credential )
  if 69 - 69: o0oOOo0O0Ooo * O0 + OoO0O00 . II111iiii / O0
  i1Iii . setProperty ( 'WAVVE_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
  if 97 - 97: ooOoO0o - OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - OoooooooOO
 def get_winCredential ( self ) :
  i1Iii = xbmcgui . Window ( 10000 )
  return i1Iii . getProperty ( 'WAVVE_M_CREDENTIAL' )
  if 59 - 59: O0 + I1IiiI + IiII % I1IiiI
 def set_winEpisodeOrderby ( self , orderby ) :
  i1Iii = xbmcgui . Window ( 10000 )
  i1Iii . setProperty ( 'WAVVE_M_ORDERBY' , orderby )
  if 70 - 70: iII111i * I1ii11iIi11i
 def get_winEpisodeOrderby ( self ) :
  i1Iii = xbmcgui . Window ( 10000 )
  return i1Iii . getProperty ( 'WAVVE_M_ORDERBY' )
  if 46 - 46: ooOoO0o / OoO0O00
  if 52 - 52: o0oOOo0O0Ooo - OoooooooOO + Ii1I + Ii1I - o0oOOo0O0Ooo / I1Ii111
  if 44 - 44: ooOoO0o . i1IIi - I1ii11iIi11i . O0 - ooOoO0o
  if 92 - 92: iII111i . I11i + o0oOOo0O0Ooo
 def add_dir ( self , label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
  if 28 - 28: i1IIi * Oo0Ooo - o0oOOo0O0Ooo * IiII * Ii1I / OoO0O00
  OooO0OoOOOO = '%s?%s' % ( self . _addon_url , urllib . urlencode ( params ) )
  if 46 - 46: OOooOOo / I1ii11iIi11i
  if sublabel : I1 = '%s < %s >' % ( label , sublabel )
  else : I1 = label
  if not img : img = 'DefaultFolder.png'
  if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
  oO0OOoO0 = xbmcgui . ListItem ( I1 , thumbnailImage = img )
  if infoLabels : oO0OOoO0 . setInfo ( type = "Video" , infoLabels = infoLabels )
  if not isFolder : oO0OOoO0 . setProperty ( 'IsPlayable' , 'true' )
  if 34 - 34: IiII - IiII * I1IiiI + Ii1I % IiII
  xbmcplugin . addDirectoryItem ( self . _addon_handle , OooO0OoOOOO , oO0OOoO0 , isFolder )
  if 4 - 4: oO0o
  if 93 - 93: OoO0O00 % oO0o . OoO0O00 * I1Ii111 % Ii1I . II111iiii
  if 38 - 38: o0oOOo0O0Ooo
  if 57 - 57: O0 / oO0o * I1Ii111 / OoOoOO00 . II111iiii
 def dp_Main_List ( self ) :
  if 26 - 26: iII111i
  for OOO in o0oO0 :
   I1 = OOO . get ( 'title' )
   if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
   if OOO . get ( 'uicode' ) == 'GENRE' :
    Oo0OoO00oOO0o = { 'mode' : 'GENRE'
 , 'uicode' : OOO . get ( 'came' )
    , 'genre' : '-'
 , 'subgenre' : '-'
    , 'orderby' : OOO . get ( 'orderby' )
 , 'ordernm' : OOO . get ( 'ordernm' )
 }
   elif OOO . get ( 'uicode' ) == 'WATCH' :
    Oo0OoO00oOO0o = { 'mode' : 'WATCH'
 , 'genre' : '-'
 }
   elif OOO . get ( 'uicode' ) == 'SEARCH' :
    Oo0OoO00oOO0o = { 'mode' : 'SEARCH'
 , 'genre' : '-'
 }
   else :
    Oo0OoO00oOO0o = { 'mode' : 'GNB_LIST'
 , 'uicode' : OOO . get ( 'uicode' )
 , 'came' : OOO . get ( 'came' )
 }
    if 80 - 80: oO0o + OOooOOo - OOooOOo % iII111i
   OoOO0oo0o = True
   if 14 - 14: o0oOOo0O0Ooo * iII111i * iII111i / OoOoOO00
   if OOO . get ( 'uicode' ) == 'XXX' :
    Oo0OoO00oOO0o [ 'mode' ] = 'XXX'
    OoOO0oo0o = False
    if 81 - 81: iIii1I11I1II1 + iIii1I11I1II1 * IiII * ooOoO0o % ooOoO0o
   self . add_dir ( I1 , sublabel = '' , img = '' , infoLabels = None , isFolder = OoOO0oo0o , params = Oo0OoO00oOO0o )
  if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
 if 81 - 81: i11iIiiIii % OoOoOO00 - OOooOOo
 if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
 if 92 - 92: iII111i . I1Ii111
 if 31 - 31: I1Ii111 . OoOoOO00 / O0
 if 89 - 89: OoOoOO00
 if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + ooOoO0o
 if 4 - 4: ooOoO0o + O0 * OOooOOo
 if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
 if 25 - 25: I1ii11iIi11i
 if 7 - 7: i1IIi / I1IiiI * I1Ii111 . IiII . iIii1I11I1II1
 if 13 - 13: OOooOOo / i11iIiiIii
 if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
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
 def login_main ( self ) :
  ( oOo0oO , OOOO0oo0 , I11iiI1i1 ) = self . get_settings_login_info ( )
  if 47 - 47: iII111i - Ii1I . II111iiii + OoooooooOO . i11iIiiIii
  if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
  if not ( oOo0oO and OOOO0oo0 ) :
   IIIiI11ii = xbmcgui . Dialog ( )
   oO0 = IIIiI11ii . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
   if oO0 == True :
    __addon__ . openSettings ( )
    sys . exit ( )
    if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
  oO = datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' )
  if 31 - 31: OOooOOo + i11iIiiIii + Oo0Ooo * ooOoO0o
  if 28 - 28: O0 * Oo0Ooo - OOooOOo % iIii1I11I1II1 * Ii1I - i11iIiiIii
  if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINWAIT' ) == 'TRUE' :
   IIII11 = 0
   while True :
    IIII11 += 1
    if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
    time . sleep ( 0.05 )
    if 57 - 57: OoO0O00 / ooOoO0o
    if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINTIME' ) == oO : return
    if IIII11 > 600 : return
  else :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'TRUE' )
   if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
  if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINTIME' ) == oO :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
   return
   if 7 - 7: IiII * I1Ii111 % Ii1I - o0oOOo0O0Ooo
  if not self . WavveObj . GetCredential ( oOo0oO , OOOO0oo0 , I11iiI1i1 ) :
   self . addon_noti ( __language__ ( 30103 ) . encode ( 'utf8' ) )
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
   sys . exit ( )
   if 13 - 13: Ii1I . i11iIiiIii
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  self . set_winCredential ( self . WavveObj . LoadCredential ( ) )
  self . set_winEpisodeOrderby ( 'desc' )
  xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
  if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
  if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
  if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
  if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
 def dp_setEpOrderby ( self , args ) :
  Oo = args . get ( 'orderby' )
  if 65 - 65: Ii1I - oO0o + oO0o + II111iiii
  self . set_winEpisodeOrderby ( Oo )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 96 - 96: OOooOOo % O0 / O0
  if 44 - 44: oO0o / I11i / I11i
  if 87 - 87: Oo0Ooo . I1IiiI - II111iiii + O0 / Oo0Ooo / oO0o
  if 25 - 25: I1IiiI . I1IiiI - OoOoOO00 % OoOoOO00 - i11iIiiIii / I1Ii111
 def dp_Gnb_List ( self , args ) :
  if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * IiII
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 73 - 73: OoO0O00 + OoooooooOO - O0 - Ii1I - II111iiii
  O0O = self . WavveObj . GetGnList ( args . get ( 'uicode' ) )
  if 80 - 80: Ii1I * o0oOOo0O0Ooo / o0oOOo0O0Ooo
  if 5 - 5: I1IiiI
  if 48 - 48: o0oOOo0O0Ooo - oO0o / OoooooooOO
  if 100 - 100: I1IiiI / o0oOOo0O0Ooo % II111iiii % Oo0Ooo % OOooOOo
  for O00oO000O0O in O0O :
   I1 = O00oO000O0O . get ( 'title' )
   Oo0OoO00oOO0o = { 'mode' : 'GN_LIST' if O00oO000O0O . get ( 'uicode' ) != 'CY1' else 'GN_MYVIEW'
   , 'uicode' : O00oO000O0O . get ( 'uicode' )
 , 'came' : args . get ( 'came' )
 , 'page' : '1'
 }
   if 18 - 18: iII111i - OOooOOo . I1Ii111 . iIii1I11I1II1
   self . add_dir ( I1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
  if len ( O0O ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 2 - 2: OOooOOo . OoO0O00
  if 78 - 78: I11i * iIii1I11I1II1 . I1IiiI / o0oOOo0O0Ooo - OoooooooOO / I1Ii111
  if 35 - 35: I11i % OOooOOo - oO0o
  if 20 - 20: i1IIi - ooOoO0o
 def dp_Myview_Group ( self , args ) :
  I1 = 'VOD 시청내역'
  Oo0OoO00oOO0o = { 'mode' : 'MYVIEW_LIST'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
  self . add_dir ( I1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
  if 30 - 30: I11i / I1IiiI
  I1 = '영화 시청내역'
  Oo0OoO00oOO0o [ 'uicode' ] = 'movie'
  self . add_dir ( I1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
  if 35 - 35: II111iiii % OOooOOo . ooOoO0o + ooOoO0o % II111iiii % II111iiii
  xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 72 - 72: II111iiii + i1IIi + o0oOOo0O0Ooo
  if 94 - 94: oO0o . i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
  if 72 - 72: Ii1I
  if 1 - 1: OoO0O00 * IiII * OoooooooOO + ooOoO0o
 def dp_Myview_List ( self , args ) :
  if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
  I1II1 = args . get ( 'uicode' )
  oooO = int ( args . get ( 'page' ) )
  i1I1i111Ii , ooo = self . WavveObj . GetMyviewList ( I1II1 , oooO )
  if 27 - 27: ooOoO0o % I1IiiI
  for o0oooOO00 in i1I1i111Ii :
   I1 = o0oooOO00 . get ( 'title' )
   iiIiii1IIIII = o0oooOO00 . get ( 'subtitle' )
   o00o = o0oooOO00 . get ( 'thumbnail' )
   if 45 - 45: I1ii11iIi11i . o0oOOo0O0Ooo . I1ii11iIi11i - I1IiiI . o0oOOo0O0Ooo
   iiI1IIIi = { }
   iiI1IIIi [ 'plot' ] = I1
   if 47 - 47: Oo0Ooo % I11i % i11iIiiIii - O0 + ooOoO0o
   if I1II1 == 'vod' :
    Oo0OoO00oOO0o = { 'mode' : 'DEEP_LIST'
 , 'contentid' : o0oooOO00 . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : I1
    , 'subtitle' : iiIiii1IIIII
    , 'thumbnail' : o00o
    , 'viewage' : o0oooOO00 . get ( 'viewage' )
 }
    OoOO0oo0o = True
    if 94 - 94: I1Ii111
   else :
    Oo0OoO00oOO0o = { 'mode' : 'MOVIE'
 , 'contentid' : o0oooOO00 . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : I1
    , 'subtitle' : iiIiii1IIIII
    , 'thumbnail' : o00o
    , 'viewage' : o0oooOO00 . get ( 'viewage' )
 }
    OoOO0oo0o = False
    if 4 - 4: Ii1I % oO0o * OoO0O00
   if o0oooOO00 . get ( 'viewage' ) == '21' : iiIiii1IIIII += ' (%s)' % ( o0oooOO00 . get ( 'viewage' ) )
   if 100 - 100: I1Ii111 * OOooOOo + OOooOOo
   self . add_dir ( I1 , sublabel = iiIiii1IIIII , img = o00o , infoLabels = iiI1IIIi , isFolder = OoOO0oo0o , params = Oo0OoO00oOO0o )
   if 54 - 54: OoooooooOO + o0oOOo0O0Ooo - i1IIi % i11iIiiIii
  if ooo :
   if 3 - 3: o0oOOo0O0Ooo % o0oOOo0O0Ooo
   Oo0OoO00oOO0o [ 'mode' ] = 'MYVIEW_LIST'
   Oo0OoO00oOO0o [ 'uicode' ] = I1II1
   Oo0OoO00oOO0o [ 'page' ] = str ( oooO + 1 )
   I1 = '[B]%s >>[/B]' % '다음 페이지'
   iiIiii1IIIII = str ( oooO + 1 )
   self . add_dir ( I1 , sublabel = iiIiii1IIIII , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
   if 83 - 83: II111iiii + I1Ii111
  if len ( i1I1i111Ii ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 73 - 73: iII111i
  if 42 - 42: i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . i11iIiiIii % I11i
  if 41 - 41: IiII / O0
  if 51 - 51: I11i % I1IiiI
  if 60 - 60: I1IiiI / OOooOOo . I1IiiI / I1Ii111 . IiII
 def dp_Genre_Group ( self , args ) :
  if 92 - 92: OoOoOO00 + I1Ii111 * Ii1I % I1IiiI
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 42 - 42: Oo0Ooo
  oo000O0OoooO = args . get ( 'mode' )
  O0o = args . get ( 'uicode' )
  I1i11II1i = args . get ( 'genre' )
  o0o0OoOo0O0OO = args . get ( 'subgenre' )
  Oo = args . get ( 'orderby' )
  iIi1I11I = args . get ( 'ordernm' )
  if 42 - 42: iIii1I11I1II1 / I1Ii111 / OoO0O00 - OoooooooOO
  if I1i11II1i == '-' :
   iII1i11IIi1i = self . WavveObj . GetGenreGroup ( O0o , I1i11II1i , Oo , iIi1I11I , exclusion21 = self . get_settings_exclusion21 ( ) )
  else :
   oOOoo0000O0o0 = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 , 'orderby' : Oo
 , 'ordernm' : iIi1I11I
 }
   if 1 - 1: oO0o + oO0o % OoOoOO00 + i11iIiiIii
   iII1i11IIi1i = self . WavveObj . GetGenreGroup_sub ( oOOoo0000O0o0 )
   if 56 - 56: o0oOOo0O0Ooo
   if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
  for iII1i1 in iII1i11IIi1i :
   I1 = iII1i1 . get ( 'title' ) + '  (' + iIi1I11I + ')'
   if 85 - 85: Ii1I * Oo0Ooo . O0 - i11iIiiIii
   Oo0OoO00oOO0o = { 'mode' : oo000O0OoooO
 , 'uicode' : O0o
   , 'genre' : iII1i1 . get ( 'genre' )
 , 'subgenre' : iII1i1 . get ( 'subgenre' )
 , 'adult' : iII1i1 . get ( 'adult' )
 , 'page' : '1'
 , 'broadcastid' : iII1i1 . get ( 'broadcastid' )
 , 'contenttype' : iII1i1 . get ( 'contenttype' )
 , 'uiparent' : iII1i1 . get ( 'uiparent' )
 , 'uirank' : iII1i1 . get ( 'uirank' )
 , 'uitype' : iII1i1 . get ( 'uitype' )
 , 'orderby' : Oo
 , 'ordernm' : iIi1I11I
 }
   if 18 - 18: Ii1I + IiII - O0
   if O0o == 'moviegenre' or O0o == 'moviegenre_svod' or O0o == 'moviegenre_ppv' or iII1i1 . get ( 'subgenre' ) != '-' :
    Oo0OoO00oOO0o [ 'mode' ] = 'GENRE_LIST'
    if 53 - 53: i1IIi
   else :
    if 87 - 87: i11iIiiIii + I1Ii111 . I1ii11iIi11i * I1Ii111 . ooOoO0o / I1ii11iIi11i
    None
    if 76 - 76: O0 + i1IIi . Oo0Ooo * I1IiiI * Ii1I
   self . add_dir ( I1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
   if 14 - 14: o0oOOo0O0Ooo % O0 * iII111i + Ii1I + Oo0Ooo * Ii1I
  if len ( iII1i11IIi1i ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 3 - 3: OoOoOO00 * Oo0Ooo
  if 95 - 95: OOooOOo % oO0o . Ii1I
  if 72 - 72: OoooooooOO
  if 72 - 72: I1IiiI % i11iIiiIii . Oo0Ooo / II111iiii
 def dp_Genre_List ( self , args ) :
  if 14 - 14: I1ii11iIi11i + OoO0O00
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 3 - 3: I1ii11iIi11i . Oo0Ooo / II111iiii
  O0o = args . get ( 'uicode' )
  oooO = int ( args . get ( 'page' ) )
  if 39 - 39: I1Ii111
  Oo0OoO00oOO0o = { 'adult' : args . get ( 'adult' )
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
   Oo0OoO00oOO0o [ 'subgenre' ] = 'all'
   if 91 - 91: OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoOoOO00 + O0
  iII1i11IIi1i , ooo = self . WavveObj . GetGenreList ( O0o , Oo0OoO00oOO0o , oooO )
  if 26 - 26: I1ii11iIi11i - OoooooooOO
  if 11 - 11: I1IiiI * oO0o
  if 81 - 81: iII111i + IiII
  for iII1i1 in iII1i11IIi1i :
   I1 = iII1i1 . get ( 'title' )
   o00o = iII1i1 . get ( 'thumbnail' )
   if 98 - 98: I1IiiI
   iiI1IIIi = { }
   iiI1IIIi [ 'plot' ] = I1
   if 95 - 95: ooOoO0o / ooOoO0o
   if O0o == 'vodgenre' :
    IIiI1Ii = { 'mode' : 'DEEP_LIST'
 , 'contentid' : iII1i1 . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : I1
    , 'subtitle' : ''
    , 'thumbnail' : o00o
    , 'viewage' : iII1i1 . get ( 'viewage' )
 }
    OoOO0oo0o = True
    if 57 - 57: OOooOOo - ooOoO0o - I11i + OoO0O00
   else :
    IIiI1Ii = { 'mode' : 'MOVIE'
 , 'contentid' : iII1i1 . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : I1
    , 'subtitle' : ''
    , 'thumbnail' : o00o
    , 'viewage' : iII1i1 . get ( 'viewage' )
 }
    if 30 - 30: Ii1I % OoOoOO00 + i1IIi - I11i - Ii1I
    OoOO0oo0o = False
    if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
   if IIiI1Ii . get ( 'viewage' ) == '21' : I1 += ' (%s)' % ( IIiI1Ii . get ( 'viewage' ) )
   if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
   self . add_dir ( I1 , sublabel = '' , img = o00o , infoLabels = iiI1IIIi , isFolder = OoOO0oo0o , params = IIiI1Ii )
   if 44 - 44: II111iiii
  if ooo :
   if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
   Oo0OoO00oOO0o [ 'mode' ] = 'GENRE_LIST'
   Oo0OoO00oOO0o [ 'uicode' ] = O0o
   Oo0OoO00oOO0o [ 'page' ] = str ( oooO + 1 )
   I1 = '[B]%s >>[/B]' % '다음 페이지'
   iiIiii1IIIII = str ( oooO + 1 )
   self . add_dir ( I1 , sublabel = iiIiii1IIIII , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
   if 35 - 35: iIii1I11I1II1
  if len ( iII1i11IIi1i ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 42 - 42: I1Ii111 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
  if 31 - 31: iII111i . OOooOOo - ooOoO0o . OoooooooOO / OoooooooOO
  if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
  if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
 def dp_Deeplink_List ( self , args ) :
  if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 71 - 71: O0 - iIii1I11I1II1
  O0o = args . get ( 'uicode' )
  i1II = args . get ( 'came' )
  oooO = int ( args . get ( 'page' ) )
  if 14 - 14: oO0o / oO0o % ooOoO0o
  if 56 - 56: I1IiiI . O0 + Oo0Ooo
  if 1 - 1: iII111i
  O0O0Ooo , ooo = self . WavveObj . GetDeeplinkList ( O0o , i1II , oooO )
  if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
  for IIii11I1i1I in O0O0Ooo :
   I1 = IIii11I1i1I . get ( 'title' )
   iiIiii1IIIII = IIii11I1i1I . get ( 'subtitle' )
   o00o = IIii11I1i1I . get ( 'thumbnail' )
   o0o0OO0O00o = IIii11I1i1I . get ( 'uicode' )
   O0Oooo = IIii11I1i1I . get ( 'channelepg' )
   if 21 - 21: Oo0Ooo
   Oo0OoO00oOO0o = { 'uicode' : o0o0OO0O00o
   , 'came' : i1II
 , 'contentid' : IIii11I1i1I . get ( 'contentid' )
 , 'contentidType' : IIii11I1i1I . get ( 'contentidType' )
 , 'page' : '1'
 , 'title' : I1
   , 'subtitle' : iiIiii1IIIII
   , 'thumbnail' : o00o
   , 'viewage' : IIii11I1i1I . get ( 'viewage' )
 }
   if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
   if o0o0OO0O00o == 'channel' :
    Oo0OoO00oOO0o [ 'mode' ] = 'LIVE'
   elif o0o0OO0O00o == 'movie' :
    Oo0OoO00oOO0o [ 'mode' ] = 'MOVIE'
   else :
    Oo0OoO00oOO0o [ 'mode' ] = 'DEEP_LIST'
    if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
    if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
   iiI1IIIi = { }
   if O0Oooo :
    iiI1IIIi [ 'plot' ] = '%s\n\n%s' % ( I1 , O0Oooo )
   else :
    iiI1IIIi [ 'plot' ] = '%s\n\n%s' % ( I1 , iiIiii1IIIII )
    if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
   if IIii11I1i1I . get ( 'viewage' ) == '21' : iiIiii1IIIII += ' (%s)' % ( IIii11I1i1I . get ( 'viewage' ) )
   if 54 - 54: i1IIi + II111iiii
   if o0o0OO0O00o in [ 'channel' , 'movie' ] :
    OoOO0oo0o = False
   elif Oo0OoO00oOO0o [ 'contentidType' ] == 'direct' :
    OoOO0oo0o = False
    Oo0OoO00oOO0o [ 'mode' ] = 'VOD'
   else :
    OoOO0oo0o = True
    if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
    if 5 - 5: Ii1I
   self . add_dir ( I1 , sublabel = iiIiii1IIIII , img = o00o , infoLabels = iiI1IIIi , isFolder = OoOO0oo0o , params = Oo0OoO00oOO0o )
   if 46 - 46: IiII
  if ooo :
   if 45 - 45: ooOoO0o
   Oo0OoO00oOO0o [ 'mode' ] = 'GN_LIST'
   Oo0OoO00oOO0o [ 'uicode' ] = O0o
   Oo0OoO00oOO0o [ 'page' ] = str ( oooO + 1 )
   I1 = '[B]%s >>[/B]' % '다음 페이지'
   iiIiii1IIIII = str ( oooO + 1 )
   self . add_dir ( I1 , sublabel = iiIiii1IIIII , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
   if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
  if len ( O0O0Ooo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 17 - 17: OOooOOo / OOooOOo / I11i
  if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
  if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % IiII / Ii1I . Ii1I
  if 14 - 14: o0oOOo0O0Ooo . OOooOOo . I11i + OoooooooOO - OOooOOo + IiII
 def dp_Episodelink_List ( self , args ) :
  if 9 - 9: Ii1I
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 59 - 59: I1IiiI * II111iiii . O0
  O000OoOO0 = args . get ( 'contentid' )
  i1IiIII111i1 = args . get ( 'contentidType' )
  I1II1 = args . get ( 'uicode' )
  if 57 - 57: Ii1I % Ii1I * i11iIiiIii
  oooO = int ( args . get ( 'page' ) )
  if 7 - 7: O0 . Ii1I
  OO0oOOoo , ooo = self . WavveObj . GetEpisodeList ( O000OoOO0 , I1II1 , i1IiIII111i1 , oooO , orderby = self . get_winEpisodeOrderby ( ) )
  if 52 - 52: o0oOOo0O0Ooo % Oo0Ooo
  for Oo000ooOOO in OO0oOOoo :
   I1 = Oo000ooOOO . get ( 'title' )
   iiIiii1IIIII = Oo000ooOOO . get ( 'subtitle' )
   o00o = Oo000ooOOO . get ( 'thumbnail' )
   Oo0OoO00oOO0o = { 'mode' : 'VOD'
 , 'uicode' : Oo000ooOOO . get ( 'uicode' )
   , 'contentid' : Oo000ooOOO . get ( 'contentid' )
 , 'programid' : Oo000ooOOO . get ( 'programid' )
 , 'title' : I1
   , 'subtitle' : iiIiii1IIIII
   , 'thumbnail' : o00o
   , 'viewage' : Oo000ooOOO . get ( 'viewage' )
 }
   if 31 - 31: iIii1I11I1II1 % I11i % ooOoO0o . Ii1I - I11i
   if Oo000ooOOO . get ( 'viewage' ) == '21' : iiIiii1IIIII += ' (%s)' % ( Oo000ooOOO . get ( 'viewage' ) )
   if 17 - 17: Ii1I
   Ii1ii1IiIII = { }
   Ii1ii1IiIII [ 'plot' ] = Oo000ooOOO . get ( 'synopsis' )
   if 57 - 57: iIii1I11I1II1 / I11i - i1IIi
   if 51 - 51: IiII
   self . add_dir ( I1 , sublabel = iiIiii1IIIII , img = o00o , infoLabels = Ii1ii1IiIII , isFolder = False , params = Oo0OoO00oOO0o )
   if 25 - 25: OoooooooOO + IiII * I1ii11iIi11i
  if oooO == 1 :
   iiI1IIIi = { 'plot' : '정렬순서를 변경합니다.' }
   Oo0OoO00oOO0o = { }
   Oo0OoO00oOO0o [ 'mode' ] = 'ORDER_BY'
   if self . get_winEpisodeOrderby ( ) == 'desc' :
    I1 = '정렬순서변경 : 최신화부터 -> 1회부터'
    Oo0OoO00oOO0o [ 'orderby' ] = 'asc'
   else :
    I1 = '정렬순서변경 : 1회부터 -> 최신화부터'
    Oo0OoO00oOO0o [ 'orderby' ] = 'desc'
   self . add_dir ( I1 , sublabel = '' , img = '' , infoLabels = iiI1IIIi , isFolder = False , params = Oo0OoO00oOO0o )
   if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + I1Ii111
  if ooo :
   if 18 - 18: ooOoO0o * OoOoOO00 . iII111i / I1ii11iIi11i / i11iIiiIii
   Oo0OoO00oOO0o [ 'mode' ] = 'DEEP_LIST'
   Oo0OoO00oOO0o [ 'uicode' ] = I1II1
   Oo0OoO00oOO0o [ 'contentid' ] = O000OoOO0
   Oo0OoO00oOO0o [ 'contentidType' ] = i1IiIII111i1
   Oo0OoO00oOO0o [ 'page' ] = str ( oooO + 1 )
   I1 = '[B]%s >>[/B]' % '다음 페이지'
   iiIiii1IIIII = str ( oooO + 1 )
   self . add_dir ( I1 , sublabel = iiIiii1IIIII , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
   if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
  if len ( OO0oOOoo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 91 - 91: i11iIiiIii / i1IIi + iII111i + ooOoO0o * i11iIiiIii
  if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * I1Ii111 . IiII
  if 52 - 52: ooOoO0o + O0 . iII111i . I1ii11iIi11i . OoO0O00
 def play_VIDEO ( self , args ) :
  if 97 - 97: I1IiiI / iII111i
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 71 - 71: II111iiii / i1IIi . I1ii11iIi11i % OoooooooOO . OoOoOO00
  O000OoOO0 = args . get ( 'contentid' )
  I1II1 = args . get ( 'uicode' )
  Iiiiii111i1ii = self . get_selQuality ( )
  if 25 - 25: OOooOOo - ooOoO0o / i11iIiiIii
  self . addon_log ( O000OoOO0 + ' - ' + I1II1 , False )
  iiI1ii11i1 , IIi1ii1Ii , OoOoO , o0 = self . WavveObj . GetStreamingURL ( O000OoOO0 , I1II1 , Iiiiii111i1ii )
  if 18 - 18: II111iiii / IiII
  if 4 - 4: II111iiii / I1ii11iIi11i + II111iiii . iIii1I11I1II1
  II1111II = '%s|Cookie=%s' % ( iiI1ii11i1 , IIi1ii1Ii )
  self . addon_log ( II1111II , False )
  if 49 - 49: Oo0Ooo - I1IiiI / IiII / O0 % o0oOOo0O0Ooo * Ii1I
  if iiI1ii11i1 == '' :
   self . addon_noti ( __language__ ( 30303 ) . encode ( 'utf8' ) )
   return
   if 100 - 100: OOooOOo . iII111i / O0 * i1IIi * Ii1I * Oo0Ooo
  OO00 = xbmcgui . ListItem ( path = II1111II )
  if 92 - 92: I11i
  if OoOoO :
   if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
   if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
   o00 = OoOoO [ 'customdata' ]
   oOO00O0Ooooo00 = OoOoO [ 'drmhost' ]
   if 97 - 97: ooOoO0o / I1Ii111 % i1IIi % I1ii11iIi11i
   ii111I11iI = 'mpd'
   OO0o = 'com.widevine.alpha'
   if 75 - 75: OoooooooOO * IiII
   I1Iiiiiii = inputstreamhelper . Helper ( ii111I11iI , drm = OO0o )
   if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
   if I1Iiiiiii . check_inputstream ( ) :
    if 69 - 69: O0
    if I1II1 == 'movie' :
     o0ooO = 'https://www.wavve.com/player/movie?movieid=%s' % O000OoOO0
    else :
     o0ooO = 'https://www.wavve.com/player/vod?programid=%s&page=1' % O000OoOO0
     if 74 - 74: O0 * oO0o - i11iIiiIii + I1Ii111
    Iii = { 'content-type' : 'application/octet-stream'
 , 'origin' : 'https://www.wavve.com'
 , 'pallycon-customdata' : o00
 , 'referer' : o0ooO
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'

    , 'user-agent' : OOoO
 }
    I1iiiiI1iI = oOO00O0Ooooo00 + '|' + urllib . urlencode ( Iii ) + '|R{SSM}|'
    if 43 - 43: oO0o - OoooooooOO
    OO00 . setProperty ( 'inputstreamaddon' , I1Iiiiiii . inputstream_addon )
    OO00 . setProperty ( 'inputstream.adaptive.manifest_type' , ii111I11iI )
    OO00 . setProperty ( 'inputstream.adaptive.license_type' , OO0o )
    if 3 - 3: O0 / iII111i
    OO00 . setProperty ( 'inputstream.adaptive.license_key' , I1iiiiI1iI )
    OO00 . setProperty ( 'inputstream.adaptive.stream_headers' , 'Cookie=%s' % IIi1ii1Ii )
    if 31 - 31: OOooOOo + o0oOOo0O0Ooo . OoooooooOO
  xbmcplugin . setResolvedUrl ( self . _addon_handle , True , OO00 )
  if 89 - 89: II111iiii + i1IIi + II111iiii
  if o0 :
   self . addon_noti ( o0 . encode ( 'utf-8' ) )
  else :
   if '/preview.' in urlparse . urlsplit ( iiI1ii11i1 ) . path : self . addon_noti ( __language__ ( 30401 ) . encode ( 'utf8' ) )
   if 7 - 7: O0 % o0oOOo0O0Ooo + I1ii11iIi11i * iII111i - iII111i
  try :
   if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) and args . get ( 'viewage' ) != '21' :
    Oo0OoO00oOO0o = { 'code' : args . get ( 'programid' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'contentid' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 , 'subtitle' : args . get ( 'subtitle' )
 }
    self . Save_Watched_List ( args . get ( 'mode' ) . lower ( ) , Oo0OoO00oOO0o )
  except :
   None
   if 42 - 42: OoOoOO00 * OoOoOO00 * I1Ii111 . I11i
   if 51 - 51: OOooOOo % iIii1I11I1II1 - OoooooooOO % ooOoO0o * iIii1I11I1II1 % OoO0O00
   if 99 - 99: oO0o * II111iiii * I1Ii111
   if 92 - 92: Oo0Ooo
 def dp_Watch_List ( self , args ) :
  I1i11II1i = args . get ( 'genre' )
  if 40 - 40: OoOoOO00 / IiII
  if I1i11II1i == '-' :
   I1 = 'VOD 시청내역'
   Oo0OoO00oOO0o = { 'mode' : 'WATCH'
 , 'genre' : 'vod'
 }
   self . add_dir ( I1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
   if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111
   I1 = '영화 시청내역'
   Oo0OoO00oOO0o [ 'genre' ] = 'movie'
   self . add_dir ( I1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
   if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
   xbmcplugin . endOfDirectory ( self . _addon_handle )
   if 61 - 61: II111iiii
  else :
   Ii1ii111i1 = self . Load_Watched_List ( I1i11II1i )
   if 31 - 31: OOooOOo + O0
   for oO0oOOoo00000 in Ii1ii111i1 :
    oOo00 = dict ( urlparse . parse_qsl ( oO0oOOoo00000 ) )
    if 3 - 3: iII111i % i1IIi
    I1 = oOo00 . get ( 'title' ) . strip ( )
    iiIiii1IIIII = oOo00 . get ( 'subtitle' ) . strip ( )
    if iiIiii1IIIII == 'None' : iiIiii1IIIII = ''
    o00o = oOo00 . get ( 'img' )
    if 46 - 46: II111iiii % o0oOOo0O0Ooo % iIii1I11I1II1 - Oo0Ooo . OoooooooOO - IiII
    iiI1IIIi = { }
    iiI1IIIi [ 'plot' ] = '%s\n%s' % ( I1 , iiIiii1IIIII )
    if 59 - 59: IiII . OOooOOo % II111iiii
    if I1i11II1i == 'vod' :
     Oo0OoO00oOO0o = { 'mode' : 'DEEP_LIST'
 , 'contentid' : oOo00 . get ( 'code' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
     OoOO0oo0o = True
    else :
     Oo0OoO00oOO0o = { 'mode' : 'MOVIE'
 , 'contentid' : oOo00 . get ( 'code' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'title' : I1
 , 'thumbnail' : o00o
 }
     OoOO0oo0o = False
     if 39 - 39: I1ii11iIi11i
    self . add_dir ( I1 , sublabel = iiIiii1IIIII , img = o00o , infoLabels = iiI1IIIi , isFolder = OoOO0oo0o , params = Oo0OoO00oOO0o )
    if 97 - 97: OOooOOo - OoO0O00 / Ii1I . i11iIiiIii % oO0o * oO0o
   iiI1IIIi = { 'plot' : '시청목록을 삭제합니다.' }
   I1 = '*** 시청목록 삭제 ***'
   Oo0OoO00oOO0o = { 'mode' : 'MYVIEW_REMOVE'
 , 'genre' : I1i11II1i
 }
   if 1 - 1: I1IiiI % ooOoO0o
   self . add_dir ( I1 , sublabel = '' , img = '' , infoLabels = iiI1IIIi , isFolder = False , params = Oo0OoO00oOO0o )
   if 65 - 65: I1IiiI + OoOoOO00 / OOooOOo
   xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
   if 83 - 83: o0oOOo0O0Ooo . iII111i - Oo0Ooo
   if 65 - 65: iIii1I11I1II1 / ooOoO0o . IiII - II111iiii
   if 72 - 72: iIii1I11I1II1 / IiII % iII111i % OOooOOo - I11i % OOooOOo
   if 100 - 100: Oo0Ooo + i11iIiiIii
   if 71 - 71: I11i / o0oOOo0O0Ooo / I1Ii111 % OOooOOo
 def dp_Search_Group ( self , args ) :
  I1 = 'VOD 검색'
  Oo0OoO00oOO0o = { 'mode' : 'SEARCH_LIST'
 , 'genre' : 'vod'
 , 'page' : '1'
 }
  self . add_dir ( I1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
  if 51 - 51: IiII * O0 / II111iiii . Ii1I % OOooOOo / I1IiiI
  I1 = '영화 검색'
  Oo0OoO00oOO0o [ 'genre' ] = 'movie'
  self . add_dir ( I1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
  if 9 - 9: I1IiiI % I1IiiI % II111iiii
  xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 30 - 30: IiII + I1Ii111 - IiII . IiII - II111iiii + O0
  if 86 - 86: i1IIi
  if 41 - 41: OoOoOO00 * I11i / OoOoOO00 % oO0o
  if 18 - 18: II111iiii . OoooooooOO % OoOoOO00 % Ii1I
 def dp_Search_List ( self , args ) :
  if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 2 - 2: OoooooooOO % OOooOOo
  I1II1 = args . get ( 'genre' )
  oooO = int ( args . get ( 'page' ) )
  if 63 - 63: I1IiiI % iIii1I11I1II1
  if 'search_key' in args :
   I1ii = args . get ( 'search_key' )
  else :
   I1ii = self . get_keyboard_input ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
   if not I1ii : return
   if 73 - 73: IiII + I1IiiI * Oo0Ooo * OoooooooOO
  Oo0o0O , ooo = self . WavveObj . GetSearchList ( I1ii , I1II1 , oooO , exclusion21 = self . get_settings_exclusion21 ( ) )
  if 17 - 17: i11iIiiIii - II111iiii * o0oOOo0O0Ooo
  for IIi1IIIIi in Oo0o0O :
   I1 = IIi1IIIIi . get ( 'title' )
   o00o = IIi1IIIIi . get ( 'thumbnail' )
   if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
   iiI1IIIi = { }
   iiI1IIIi [ 'plot' ] = I1
   if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - I11i
   if I1II1 == 'vod' :
    Oo0OoO00oOO0o = { 'mode' : 'DEEP_LIST'
 , 'contentid' : IIi1IIIIi . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : I1
    , 'subtitle' : ''
    , 'thumbnail' : o00o
    , 'viewage' : IIi1IIIIi . get ( 'viewage' )
 }
    OoOO0oo0o = True
    if 30 - 30: OoOoOO00
   else :
    Oo0OoO00oOO0o = { 'mode' : 'MOVIE'
 , 'contentid' : IIi1IIIIi . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : I1
    , 'subtitle' : ''
    , 'thumbnail' : o00o
    , 'viewage' : IIi1IIIIi . get ( 'viewage' )
 }
    if 21 - 21: i11iIiiIii / I1Ii111 % OOooOOo * O0 . I11i - iIii1I11I1II1
    OoOO0oo0o = False
    if 26 - 26: II111iiii * OoOoOO00
   if Oo0OoO00oOO0o . get ( 'viewage' ) == '21' : I1 += ' (%s)' % ( Oo0OoO00oOO0o . get ( 'viewage' ) )
   if 10 - 10: II111iiii . iII111i
   self . add_dir ( I1 , sublabel = '' , img = o00o , infoLabels = iiI1IIIi , isFolder = OoOO0oo0o , params = Oo0OoO00oOO0o )
   if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
  if ooo :
   if 88 - 88: iII111i
   Oo0OoO00oOO0o [ 'mode' ] = 'SEARCH_LIST'
   Oo0OoO00oOO0o [ 'genre' ] = I1II1
   Oo0OoO00oOO0o [ 'page' ] = str ( oooO + 1 )
   Oo0OoO00oOO0o [ 'search_key' ] = I1ii
   I1 = '[B]%s >>[/B]' % '다음 페이지'
   iiIiii1IIIII = str ( oooO + 1 )
   self . add_dir ( I1 , sublabel = iiIiii1IIIII , img = '' , infoLabels = None , isFolder = True , params = Oo0OoO00oOO0o )
   if 19 - 19: II111iiii * IiII + Ii1I
  if len ( Oo0o0O ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 65 - 65: OOooOOo . I1Ii111 . OoO0O00 . iII111i - OOooOOo
  if 19 - 19: i11iIiiIii + iII111i % ooOoO0o
  if 14 - 14: OoO0O00 . II111iiii . I11i / Ii1I % I1ii11iIi11i - ooOoO0o
  if 67 - 67: I11i - OOooOOo . i1IIi
  if 35 - 35: iII111i + ooOoO0o - oO0o . iII111i . IiII
 def Load_Watched_List ( self , genre ) :
  try :
   oo0ooOO = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   with open ( oo0ooOO , 'r' ) as iI1IiIIiIIi :
    IiIi11Iii = iI1IiIIiIIi . readlines ( )
  except :
   IiIi11Iii = [ ]
   if 46 - 46: OoOoOO00 - I11i - Ii1I . i1IIi
  return IiIi11Iii
  if 35 - 35: II111iiii * I11i - OoooooooOO . I11i . I11i
  if 11 - 11: I1Ii111 / OoOoOO00 + I11i % iIii1I11I1II1
  if 42 - 42: I1ii11iIi11i * OoOoOO00 % ooOoO0o - OoOoOO00 . i11iIiiIii - I1Ii111
  if 84 - 84: I1Ii111 - I1ii11iIi11i / I11i
 def Save_Watched_List ( self , genre , in_params ) :
  try :
   oo0ooOO = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   i1II111i1 = self . Load_Watched_List ( genre )
   if 98 - 98: OoO0O00 . I11i % II111iiii
   with open ( oo0ooOO , 'w' ) as iI1IiIIiIIi :
    O0OoOoO00O = urllib . urlencode ( in_params )
    O0OoOoO00O = O0OoOoO00O . encode ( 'utf-8' ) + '\n'
    iI1IiIIiIIi . write ( O0OoOoO00O )
    if 96 - 96: I1IiiI % Oo0Ooo . I1ii11iIi11i + OOooOOo
    Ii11Iii1i1ii = 0
    for Ii1i1i1111 in i1II111i1 :
     o0oO0O00oOo = dict ( urlparse . parse_qsl ( Ii1i1i1111 ) )
     if in_params . get ( 'code' ) != o0oO0O00oOo . get ( 'code' ) :
      iI1IiIIiIIi . write ( Ii1i1i1111 )
      Ii11Iii1i1ii += 1
      if Ii11Iii1i1ii >= 50 : break
  except :
   None
   if 26 - 26: IiII % I1Ii111 % oO0o % Ii1I
   if 55 - 55: ooOoO0o % OoooooooOO / OoooooooOO % OoooooooOO
   if 52 - 52: I1ii11iIi11i + I1ii11iIi11i . II111iiii
   if 34 - 34: OoooooooOO . O0 / oO0o * OoOoOO00 - I1ii11iIi11i
 def Delete_Watched_List ( self , genre ) :
  try :
   oo0ooOO = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   with open ( oo0ooOO , 'w' ) as iI1IiIIiIIi :
    iI1IiIIiIIi . write ( '' )
  except :
   None
   if 36 - 36: i1IIi / O0 / OoO0O00 - O0 - i1IIi
   if 22 - 22: i1IIi + Ii1I
   if 54 - 54: ooOoO0o % OOooOOo . I1Ii111 + oO0o - OOooOOo * I1IiiI
   if 92 - 92: o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % OoO0O00 % IiII . OoooooooOO
 def dp_WatchList_Delete ( self , args ) :
  I1i11II1i = args . get ( 'genre' )
  if 52 - 52: ooOoO0o / i11iIiiIii - OOooOOo . IiII % iIii1I11I1II1 + o0oOOo0O0Ooo
  IIIiI11ii = xbmcgui . Dialog ( )
  oO0 = IIIiI11ii . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if oO0 == False : sys . exit ( )
  if 71 - 71: oO0o % I11i * OoOoOO00 . O0 / Ii1I . I1ii11iIi11i
  self . Delete_Watched_List ( I1i11II1i )
  if 58 - 58: Oo0Ooo / oO0o
  xbmc . executebuiltin ( "Container.Refresh" )
  if 44 - 44: OOooOOo
  if 54 - 54: Ii1I - I11i - I1Ii111 . iIii1I11I1II1
  if 79 - 79: Ii1I . OoO0O00
  if 40 - 40: o0oOOo0O0Ooo + Oo0Ooo . o0oOOo0O0Ooo % ooOoO0o
  if 15 - 15: Ii1I * Oo0Ooo % I1ii11iIi11i * iIii1I11I1II1 - i11iIiiIii
  if 60 - 60: I1IiiI * I1Ii111 % OoO0O00 + oO0o
  if 52 - 52: i1IIi
  if 84 - 84: Ii1I / IiII
  if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / OOooOOo
  if 11 - 11: I1IiiI * oO0o + I1ii11iIi11i / I1ii11iIi11i
  if 37 - 37: i11iIiiIii + i1IIi
 def wavve_main ( self ) :
  if 23 - 23: iII111i + I11i . OoOoOO00 * I1IiiI + I1ii11iIi11i
  oo000O0OoooO = self . main_params . get ( 'mode' , None )
  if 18 - 18: IiII * o0oOOo0O0Ooo . IiII / O0
  self . login_main ( )
  if oo000O0OoooO is None :
   if 8 - 8: o0oOOo0O0Ooo
   self . dp_Main_List ( )
   if 4 - 4: I1ii11iIi11i + I1ii11iIi11i * ooOoO0o - OoOoOO00
   if 78 - 78: Ii1I / II111iiii % OoOoOO00
   if 52 - 52: OOooOOo - iII111i * oO0o
   if 17 - 17: OoooooooOO + OOooOOo * I11i * OoOoOO00
   if 36 - 36: O0 + Oo0Ooo
   if 5 - 5: Oo0Ooo * OoOoOO00
   if 46 - 46: ooOoO0o
   if 33 - 33: iII111i - II111iiii * OoooooooOO - Oo0Ooo - OOooOOo
   if 84 - 84: I1Ii111 + Oo0Ooo - OoOoOO00 * OoOoOO00
  elif oo000O0OoooO == 'GNB_LIST' :
   self . dp_Gnb_List ( self . main_params )
   if 61 - 61: OoooooooOO . oO0o . OoooooooOO / Oo0Ooo
  elif oo000O0OoooO == 'GN_LIST' :
   self . dp_Deeplink_List ( self . main_params )
   if 72 - 72: i1IIi
  elif oo000O0OoooO == 'DEEP_LIST' :
   I1II1 = self . main_params . get ( 'uicode' , None )
   if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i . OoooooooOO
   if I1II1 in [ 'quick' , 'vod' , 'program' , 'x' ] :
    self . dp_Episodelink_List ( self . main_params )
    if 63 - 63: I1ii11iIi11i
   else : None
   if 6 - 6: ooOoO0o / I1ii11iIi11i
  elif oo000O0OoooO in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
   self . play_VIDEO ( self . main_params )
   if 57 - 57: I11i
   time . sleep ( 0.1 )
   if 67 - 67: OoO0O00 . ooOoO0o
  elif oo000O0OoooO == 'GN_MYVIEW' :
   self . dp_Myview_Group ( self . main_params )
   if 87 - 87: oO0o % Ii1I
  elif oo000O0OoooO == 'MYVIEW_LIST' :
   self . dp_Myview_List ( self . main_params )
   if 83 - 83: II111iiii - I11i
  elif oo000O0OoooO == 'GENRE' :
   self . dp_Genre_Group ( self . main_params )
   if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
  elif oo000O0OoooO == 'GENRE_LIST' :
   self . dp_Genre_List ( self . main_params )
   if 86 - 86: iIii1I11I1II1 + OoOoOO00 . i11iIiiIii - Ii1I
  elif oo000O0OoooO == 'WATCH' :
   self . dp_Watch_List ( self . main_params )
   if 51 - 51: OoOoOO00
  elif oo000O0OoooO == 'MYVIEW_REMOVE' :
   self . dp_WatchList_Delete ( self . main_params )
   if 14 - 14: IiII % oO0o % Oo0Ooo - i11iIiiIii
  elif oo000O0OoooO == 'SEARCH' :
   self . dp_Search_Group ( self . main_params )
   if 53 - 53: Ii1I % Oo0Ooo
  elif oo000O0OoooO == 'SEARCH_LIST' :
   self . dp_Search_List ( self . main_params )
   if 59 - 59: OOooOOo % iIii1I11I1II1 . i1IIi + II111iiii * IiII
  elif oo000O0OoooO == 'ORDER_BY' :
   self . dp_setEpOrderby ( self . main_params )
   if 41 - 41: Ii1I % I1ii11iIi11i
  else :
   None
   if 12 - 12: OOooOOo
   if 69 - 69: OoooooooOO + OOooOOo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
