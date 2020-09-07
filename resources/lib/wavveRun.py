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
import base64
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
if 61 - 61: oO0o / OoOoOO00 / iII111i * OoO0O00 . II111iiii
__addon__ = xbmcaddon . Addon ( )
__language__ = __addon__ . getLocalizedString
__profile__ = xbmc . translatePath ( __addon__ . getAddonInfo ( 'profile' ) )
__version__ = __addon__ . getAddonInfo ( 'version' )
__addonid__ = __addon__ . getAddonInfo ( 'id' )
__addonname__ = __addon__ . getAddonInfo ( 'name' )
if 1 - 1: II111iiii - I1ii11iIi11i % i11iIiiIii + IiII . I1Ii111
if 55 - 55: iIii1I11I1II1 - I1IiiI . Ii1I * IiII * i1IIi / iIii1I11I1II1
OOo000 = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
O0I11i1i11i1I = xbmc . translatePath ( os . path . join ( __profile__ , 'wavve_cookies.json' ) )
if 31 - 31: i11iIiiIii / I1IiiI / ooOoO0o * oO0o / Oo0Ooo
if 99 - 99: iIii1I11I1II1 * OoooooooOO * II111iiii * iIii1I11I1II1
from wavveCore import *
if 44 - 44: oO0o / Oo0Ooo - II111iiii - i11iIiiIii % I1Ii111
if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
class iIiiI1 ( object ) :
 def __init__ ( self , in_addonurl , in_handle , in_params ) :
  if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
  if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
  if 3 - 3: iII111i + O0
  if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
  self . _addon_url = in_addonurl
  self . _addon_handle = in_handle
  self . main_params = in_params
  self . WavveObj = iII111ii ( )
  if 78 - 78: OoO0O00
  if 18 - 18: O0 - iII111i / iII111i + ooOoO0o % ooOoO0o - IiII
  if 62 - 62: iII111i - IiII - OoOoOO00 % i1IIi / oO0o
 def addon_noti ( self , sting ) :
  try :
   OoooooOoo = xbmcgui . Dialog ( )
   if 70 - 70: OoO0O00 . OoO0O00 - OoO0O00 / I1ii11iIi11i * OOooOOo
   OoooooOoo . notification ( __addonname__ , sting )
  except :
   None
   if 86 - 86: i11iIiiIii + Ii1I + ooOoO0o * I11i + o0oOOo0O0Ooo
   if 61 - 61: OoO0O00 / i11iIiiIii
   if 34 - 34: OoooooooOO + iIii1I11I1II1 + i11iIiiIii - I1ii11iIi11i + i11iIiiIii
 def addon_log ( self , string , isDebug = False ) :
  try :
   ooOoo0O = string . encode ( 'utf-8' , 'ignore' )
  except :
   ooOoo0O = 'addonException: addon_log'
  if isDebug : OooO0 = xbmc . LOGDEBUG
  else : OooO0 = xbmc . LOGNOTICE
  xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , ooOoo0O ) , level = OooO0 )
  if 35 - 35: OOooOOo % I1Ii111 % i11iIiiIii / OoooooooOO
  if 13 - 13: i1IIi - Ii1I % oO0o / iIii1I11I1II1 % iII111i
  if 97 - 97: i11iIiiIii
  if 32 - 32: Oo0Ooo * O0 % oO0o % Ii1I . IiII
 def get_keyboard_input ( self , title ) :
  o0OOOOO00o0O0 = None
  o0o0OOO0o0 = xbmc . Keyboard ( )
  o0o0OOO0o0 . setHeading ( title )
  xbmc . sleep ( 1000 )
  o0o0OOO0o0 . doModal ( )
  if ( o0o0OOO0o0 . isConfirmed ( ) ) :
   o0OOOOO00o0O0 = o0o0OOO0o0 . getText ( )
  return o0OOOOO00o0O0
  if 84 - 84: IiII
  if 25 - 25: Oo0Ooo - IiII . OoooooooOO
  if 22 - 22: IiII + II111iiii % I1Ii111 . I11i . OoOoOO00
  if 76 - 76: OoOoOO00 - O0 % OOooOOo / I1ii11iIi11i / OoOoOO00
 def get_settings_login_info ( self ) :
  oo0oooooO0 = __addon__ . getSetting ( 'id' )
  i11Iiii = __addon__ . getSetting ( 'pw' )
  iI = __addon__ . getSetting ( 'selected_profile' )
  return ( oo0oooooO0 , i11Iiii , iI )
  if 28 - 28: OOooOOo - IiII . IiII + OoOoOO00 - OoooooooOO + O0
  if 95 - 95: OoO0O00 % oO0o . O0
  if 15 - 15: ooOoO0o / Ii1I . Ii1I - i1IIi
 def get_selQuality ( self ) :
  try :
   o00oOO0 = [ 1080 , 720 , 480 , 360 ]
   if 95 - 95: OOooOOo / OoooooooOO
   iIo00O = int ( __addon__ . getSetting ( 'selected_quality' ) )
   return o00oOO0 [ iIo00O ]
  except :
   None
   if 69 - 69: oO0o % I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - O0 % OoooooooOO
  return 1080
  if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
  if 4 - 4: II111iiii / ooOoO0o . iII111i
  if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
 def get_settings_exclusion21 ( self ) :
  ii11i1 = __addon__ . getSetting ( 'exclusion21' )
  if ii11i1 == 'false' :
   return False
  else :
   return True
   if 29 - 29: I1ii11iIi11i % I1IiiI + ooOoO0o / o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
   if 42 - 42: Ii1I + oO0o
   if 76 - 76: I1Ii111 - OoO0O00
 def get_settings_direct_replay ( self ) :
  oOooOOo00Oo0O = int ( __addon__ . getSetting ( 'direct_replay' ) )
  if oOooOOo00Oo0O == 0 :
   return False
  else :
   return True
   if 72 - 72: iII111i / i1IIi * Oo0Ooo - I1Ii111
   if 51 - 51: II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % I1ii11iIi11i / ooOoO0o
   if 49 - 49: o0oOOo0O0Ooo
 def get_settings_addinfo ( self ) :
  IIii1Ii1 = __addon__ . getSetting ( 'add_infoyn' )
  if IIii1Ii1 == 'false' :
   return False
  else :
   return True
   if 5 - 5: iII111i % OOooOOo + ooOoO0o % i11iIiiIii + o0oOOo0O0Ooo
   if 60 - 60: OoO0O00 * OoOoOO00 - OoO0O00 % OoooooooOO - ooOoO0o + I1IiiI
   if 70 - 70: IiII * Oo0Ooo * I11i / Ii1I
   if 88 - 88: O0
 def get_settings_thumbnail_landyn ( self ) :
  O0OoO0O00o0oO = int ( __addon__ . getSetting ( 'thumbnail_way' ) )
  if O0OoO0O00o0oO == 0 :
   return True
  else :
   return False
   if 15 - 15: Ii1I - O0 / oO0o * i1IIi
   if 92 - 92: OoOoOO00
   if 26 - 26: iII111i . I1Ii111
   if 68 - 68: OoO0O00
 def set_winCredential ( self , credential ) :
  IIi1iIIiI = xbmcgui . Window ( 10000 )
  IIi1iIIiI . setProperty ( 'WAVVE_M_CREDENTIAL' , credential )
  if 58 - 58: ooOoO0o / II111iiii - OOooOOo - i11iIiiIii % OoOoOO00 - I1Ii111
  IIi1iIIiI . setProperty ( 'WAVVE_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
  if 29 - 29: Oo0Ooo - oO0o - I11i % iII111i - oO0o
 def get_winCredential ( self ) :
  IIi1iIIiI = xbmcgui . Window ( 10000 )
  return IIi1iIIiI . getProperty ( 'WAVVE_M_CREDENTIAL' )
  if 91 - 91: OoO0O00 / I11i - II111iiii . I11i
 def set_winEpisodeOrderby ( self , orderby ) :
  IIi1iIIiI = xbmcgui . Window ( 10000 )
  IIi1iIIiI . setProperty ( 'WAVVE_M_ORDERBY' , orderby )
  if 18 - 18: o0oOOo0O0Ooo
 def get_winEpisodeOrderby ( self ) :
  IIi1iIIiI = xbmcgui . Window ( 10000 )
  return IIi1iIIiI . getProperty ( 'WAVVE_M_ORDERBY' )
  if 98 - 98: iII111i * iII111i / iII111i + I11i
  if 34 - 34: ooOoO0o
  if 15 - 15: I11i * ooOoO0o * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
  if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
 def add_dir ( self , label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
  if 92 - 92: iII111i . I1Ii111
  i1i = '%s?%s' % ( self . _addon_url , urllib . urlencode ( params ) )
  if 50 - 50: IiII
  if sublabel : i11I1iIiII = '%s < %s >' % ( label , sublabel )
  else : i11I1iIiII = label
  if not img : img = 'DefaultFolder.png'
  if 96 - 96: Oo0Ooo
  if 45 - 45: O0 * o0oOOo0O0Ooo % Oo0Ooo * OoooooooOO + iII111i . OoOoOO00
  Oo0ooOo0o = xbmcgui . ListItem ( i11I1iIiII )
  Oo0ooOo0o . setArt ( { 'thumbnailImage' : img , 'icon' : img , 'poster' : img } )
  if 22 - 22: iIii1I11I1II1 / i11iIiiIii * iIii1I11I1II1 * II111iiii . OOooOOo / i11iIiiIii
  if infoLabels : Oo0ooOo0o . setInfo ( type = "video" , infoLabels = infoLabels )
  if not isFolder : Oo0ooOo0o . setProperty ( 'IsPlayable' , 'true' )
  if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
  xbmcplugin . addDirectoryItem ( self . _addon_handle , i1i , Oo0ooOo0o , isFolder )
  if 52 - 52: o0oOOo0O0Ooo
  if 95 - 95: Ii1I
  if 87 - 87: ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
  if 91 - 91: O0
 def dp_Main_List ( self ) :
  if 61 - 61: II111iiii
  for O0OOO in o0oO0 :
   i11I1iIiII = O0OOO . get ( 'title' )
   if 10 - 10: OOooOOo * I11i % OoOoOO00 / I1IiiI / OoOoOO00
   if O0OOO . get ( 'uicode' ) == 'GENRE' :
    iIIi1i1 = { 'mode' : 'GENRE'
 , 'uicode' : O0OOO . get ( 'came' )
    , 'genre' : '-'
 , 'subgenre' : '-'
    , 'orderby' : O0OOO . get ( 'orderby' )
 , 'ordernm' : O0OOO . get ( 'ordernm' )
 }
   elif O0OOO . get ( 'uicode' ) == 'WATCH' :
    iIIi1i1 = { 'mode' : 'WATCH'
 , 'genre' : '-'
 }
   elif O0OOO . get ( 'uicode' ) == 'SEARCH' :
    iIIi1i1 = { 'mode' : 'SEARCH'
 , 'genre' : '-'
 }
   else :
    iIIi1i1 = { 'mode' : 'GNB_LIST'
 , 'uicode' : O0OOO . get ( 'uicode' )
 , 'came' : O0OOO . get ( 'came' )
 }
    if 10 - 10: I11i
   OOooOO000 = True
   if 97 - 97: I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
   if O0OOO . get ( 'uicode' ) == 'XXX' :
    iIIi1i1 [ 'mode' ] = 'XXX'
    OOooOO000 = False
    if 37 - 37: iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = OOooOO000 , params = iIIi1i1 )
  if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 83 - 83: I11i / I1IiiI
  if 34 - 34: IiII
  if 57 - 57: oO0o . I11i . i1IIi
  if 42 - 42: I11i + I1ii11iIi11i % O0
 def login_main ( self ) :
  if 6 - 6: oO0o
  ( oOOo0oOo0 , II , ooooo ) = self . get_settings_login_info ( )
  if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iII111i * IiII . i11iIiiIii
  if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % iII111i
  if not ( oOOo0oOo0 and II ) :
   OoooooOoo = xbmcgui . Dialog ( )
   ooOOOoOooOoO = OoooooOoo . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
   if ooOOOoOooOoO == True :
    __addon__ . openSettings ( )
    sys . exit ( )
    if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
    if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
  if self . get_winEpisodeOrderby ( ) == '' :
   self . set_winEpisodeOrderby ( 'desc' )
   if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
   if 51 - 51: O0 + iII111i
  if self . cookiefile_check ( ) : return
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
  IIi1 = int ( datetime . datetime . now ( ) . strftime ( '%Y%m%d' ) )
  I1I1I = xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINTIME' )
  if I1I1I == None or I1I1I == '' : I1I1I = int ( '19000101' )
  if 95 - 95: II111iiii + o0oOOo0O0Ooo + iII111i * iIii1I11I1II1 % oO0o / IiII
  if 56 - 56: iII111i
  if 86 - 86: II111iiii % I1Ii111
  if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINWAIT' ) == 'TRUE' :
   iiIIiiIi1Ii11 = 0
   while True :
    iiIIiiIi1Ii11 += 1
    if 65 - 65: II111iiii . OOooOOo % I11i . i11iIiiIii + O0
    time . sleep ( 0.05 )
    if 26 - 26: I11i - iIii1I11I1II1 - I1IiiI / OoO0O00 . OoOoOO00 % iIii1I11I1II1
    if I1I1I >= IIi1 : return
    if iiIIiiIi1Ii11 > 600 : return
  else :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'TRUE' )
   if 91 - 91: o0oOOo0O0Ooo . iIii1I11I1II1 / oO0o + i1IIi
  if I1I1I >= IIi1 :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
   return
   if 42 - 42: ooOoO0o . o0oOOo0O0Ooo . ooOoO0o - I1ii11iIi11i
  if not self . WavveObj . GetCredential ( oOOo0oOo0 , II , ooooo ) :
   self . addon_noti ( __language__ ( 30103 ) . encode ( 'utf8' ) )
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
   sys . exit ( )
   if 40 - 40: ooOoO0o - i11iIiiIii / Ii1I
   if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
  self . set_winCredential ( self . WavveObj . LoadCredential ( ) )
  self . cookiefile_save ( )
  xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
  if 47 - 47: iII111i - Ii1I . II111iiii + OoooooooOO . i11iIiiIii
  if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
  if 87 - 87: Oo0Ooo . IiII
  if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
  if 55 - 55: OOooOOo . I1IiiI
  if 61 - 61: Oo0Ooo % IiII . Oo0Ooo
 def dp_setEpOrderby ( self , args ) :
  o0oOO000oO0oo = args . get ( 'orderby' )
  if 78 - 78: I1ii11iIi11i + OOooOOo - I1Ii111
  self . set_winEpisodeOrderby ( o0oOO000oO0oo )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
  if 57 - 57: OoO0O00 / ooOoO0o
  if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
  if 7 - 7: IiII * I1Ii111 % Ii1I - o0oOOo0O0Ooo
 def dp_Gnb_List ( self , args ) :
  if 13 - 13: Ii1I . i11iIiiIii
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  O00o0OO0 = self . WavveObj . GetGnList ( args . get ( 'uicode' ) )
  if 35 - 35: oO0o % ooOoO0o / I1Ii111 + iIii1I11I1II1 . OoooooooOO . I1IiiI
  if 71 - 71: IiII * II111iiii * oO0o
  if 56 - 56: I1IiiI
  if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
  for Oo in O00o0OO0 :
   i11I1iIiII = Oo . get ( 'title' )
   iIIi1i1 = { 'mode' : 'GN_LIST' if Oo . get ( 'uicode' ) != 'CY1' else 'GN_MYVIEW'
   , 'uicode' : Oo . get ( 'uicode' )
 , 'came' : args . get ( 'came' )
 , 'page' : '1'
 }
   if 65 - 65: Ii1I - oO0o + oO0o + II111iiii
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if len ( O00o0OO0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 96 - 96: OOooOOo % O0 / O0
  if 44 - 44: oO0o / I11i / I11i
  if 87 - 87: Oo0Ooo . I1IiiI - II111iiii + O0 / Oo0Ooo / oO0o
  if 25 - 25: I1IiiI . I1IiiI - OoOoOO00 % OoOoOO00 - i11iIiiIii / I1Ii111
 def dp_Myview_Group ( self , args ) :
  i11I1iIiII = 'VOD 시청내역'
  iIIi1i1 = { 'mode' : 'MYVIEW_LIST'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
  self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * IiII
  i11I1iIiII = '영화 시청내역'
  iIIi1i1 [ 'uicode' ] = 'movie'
  self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if 73 - 73: OoO0O00 + OoooooooOO - O0 - Ii1I - II111iiii
  xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 99 - 99: ooOoO0o . Ii1I + I1Ii111 + OoooooooOO % o0oOOo0O0Ooo
  if 51 - 51: iIii1I11I1II1
  if 34 - 34: oO0o + I1IiiI - oO0o
  if 17 - 17: II111iiii % iII111i + I11i - iII111i / OOooOOo + ooOoO0o
 def dp_Myview_List ( self , args ) :
  if 59 - 59: OOooOOo % OoOoOO00 . Ii1I * I1ii11iIi11i % I11i
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  oO0o0o0oo = self . get_settings_addinfo ( )
  if 32 - 32: OOooOOo
  I11iiiiIIii1I = args . get ( 'uicode' )
  II1IiiIi1i = int ( args . get ( 'page' ) )
  iiI11ii1I1 , Ooo0OOoOoO0 = self . WavveObj . GetMyviewList ( I11iiiiIIii1I , II1IiiIi1i , addinfoyn = oO0o0o0oo )
  if 70 - 70: oO0o
  for oOOoO0o0oO in iiI11ii1I1 :
   i11I1iIiII = oOOoO0o0oO . get ( 'title' )
   o0Oo0oO0oOO00 = oOOoO0o0oO . get ( 'subtitle' )
   oo00OO0000oO = oOOoO0o0oO . get ( 'thumbnail' )
   if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
   i1I1i111Ii = oOOoO0o0oO . get ( 'info' )
   if I11iiiiIIii1I == 'movie' and oO0o0o0oo == True :
    i11I1iIiII = '%s (%s)' % ( i11I1iIiII , str ( i1I1i111Ii . get ( 'year' ) ) )
   else :
    i1I1i111Ii [ 'plot' ] = i11I1iIiII
    if 67 - 67: I1IiiI . i1IIi
   if I11iiiiIIii1I == 'vod' :
    iIIi1i1 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : oOOoO0o0oO . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11I1iIiII
    , 'subtitle' : o0Oo0oO0oOO00
    , 'thumbnail' : oo00OO0000oO
    , 'viewage' : oOOoO0o0oO . get ( 'viewage' )
 }
    OOooOO000 = True
    if 27 - 27: ooOoO0o % I1IiiI
   else :
    iIIi1i1 = { 'mode' : 'MOVIE'
 , 'contentid' : oOOoO0o0oO . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11I1iIiII
    , 'subtitle' : o0Oo0oO0oOO00
    , 'thumbnail' : oo00OO0000oO
    , 'viewage' : oOOoO0o0oO . get ( 'viewage' )
 }
    OOooOO000 = False
    if 73 - 73: OOooOOo
   if oOOoO0o0oO . get ( 'viewage' ) == '21' : o0Oo0oO0oOO00 += ' (%s)' % ( oOOoO0o0oO . get ( 'viewage' ) )
   if 70 - 70: iIii1I11I1II1
   self . add_dir ( i11I1iIiII , sublabel = o0Oo0oO0oOO00 , img = oo00OO0000oO , infoLabels = i1I1i111Ii , isFolder = OOooOO000 , params = iIIi1i1 )
   if 31 - 31: IiII - I1IiiI % iIii1I11I1II1
  if Ooo0OOoOoO0 :
   if 92 - 92: i1IIi - iIii1I11I1II1
   iIIi1i1 [ 'mode' ] = 'MYVIEW_LIST'
   iIIi1i1 [ 'uicode' ] = I11iiiiIIii1I
   iIIi1i1 [ 'page' ] = str ( II1IiiIi1i + 1 )
   i11I1iIiII = '[B]%s >>[/B]' % '다음 페이지'
   o0Oo0oO0oOO00 = str ( II1IiiIi1i + 1 )
   self . add_dir ( i11I1iIiII , sublabel = o0Oo0oO0oOO00 , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 16 - 16: OoO0O00 - OoOoOO00 - OOooOOo - i1IIi / Ii1I
  if len ( iiI11ii1I1 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 88 - 88: OoO0O00
  if 71 - 71: I1ii11iIi11i
  if 7 - 7: I1ii11iIi11i - I1IiiI . iIii1I11I1II1 - i1IIi
  if 59 - 59: o0oOOo0O0Ooo
  if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
 def dp_Genre_Group ( self , args ) :
  if 73 - 73: I11i % i11iIiiIii - I1IiiI
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
  II1IIIIiII1i = args . get ( 'mode' )
  i1II1 = args . get ( 'uicode' )
  i11i1 = args . get ( 'genre' )
  IiiiiI1i1Iii = args . get ( 'subgenre' )
  o0oOO000oO0oo = args . get ( 'orderby' )
  oo00oO0o = args . get ( 'ordernm' )
  if 31 - 31: OOooOOo
  if i11i1 == '-' :
   i1 = self . WavveObj . GetGenreGroup ( i1II1 , i11i1 , o0oOO000oO0oo , oo00oO0o , exclusion21 = self . get_settings_exclusion21 ( ) )
  else :
   OOO0000oO = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 , 'orderby' : o0oOO000oO0oo
 , 'ordernm' : oo00oO0o
 }
   if 15 - 15: OoOoOO00 % I1IiiI * I11i
   i1 = self . WavveObj . GetGenreGroup_sub ( OOO0000oO )
   if 81 - 81: ooOoO0o - iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * I11i
   if 20 - 20: oO0o % IiII
  for III1i1i11i in i1 :
   i11I1iIiII = III1i1i11i . get ( 'title' ) + '  (' + oo00oO0o + ')'
   if 100 - 100: oO0o / I1Ii111 / I1ii11iIi11i
   iIIi1i1 = { 'mode' : II1IIIIiII1i
 , 'uicode' : i1II1
   , 'genre' : III1i1i11i . get ( 'genre' )
 , 'subgenre' : III1i1i11i . get ( 'subgenre' )
 , 'adult' : III1i1i11i . get ( 'adult' )
 , 'page' : '1'
 , 'broadcastid' : III1i1i11i . get ( 'broadcastid' )
 , 'contenttype' : III1i1i11i . get ( 'contenttype' )
 , 'uiparent' : III1i1i11i . get ( 'uiparent' )
 , 'uirank' : III1i1i11i . get ( 'uirank' )
 , 'uitype' : III1i1i11i . get ( 'uitype' )
 , 'orderby' : o0oOO000oO0oo
 , 'ordernm' : oo00oO0o
 }
   if 78 - 78: Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
   if i1II1 == 'moviegenre' or i1II1 == 'moviegenre_svod' or i1II1 == 'moviegenre_ppv' or III1i1i11i . get ( 'subgenre' ) != '-' :
    iIIi1i1 [ 'mode' ] = 'GENRE_LIST'
    if 10 - 10: iII111i + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / I1ii11iIi11i
   else :
    if 42 - 42: I1IiiI
    None
    if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
  if len ( i1 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
  if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
  if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
  if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
 def dp_Genre_List ( self , args ) :
  if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  oO0o0o0oo = self . get_settings_addinfo ( )
  if 79 - 79: O0 * i11iIiiIii - IiII / IiII
  i1II1 = args . get ( 'uicode' )
  II1IiiIi1i = int ( args . get ( 'page' ) )
  if 48 - 48: O0
  iIIi1i1 = { 'adult' : args . get ( 'adult' )
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
   iIIi1i1 [ 'subgenre' ] = 'all'
   if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
  i1 , Ooo0OOoOoO0 = self . WavveObj . GetGenreList ( i1II1 , iIIi1i1 , II1IiiIi1i , addinfoyn = oO0o0o0oo )
  if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
  if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
  if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
  for III1i1i11i in i1 :
   i11I1iIiII = III1i1i11i . get ( 'title' )
   oo00OO0000oO = III1i1i11i . get ( 'thumbnail' )
   if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
   i1I1i111Ii = III1i1i11i . get ( 'info' )
   if i1II1 == 'moviegenre_svod' and oO0o0o0oo == True :
    i11I1iIiII = '%s (%s)' % ( i11I1iIiII , str ( i1I1i111Ii . get ( 'year' ) ) )
   else :
    i1I1i111Ii [ 'plot' ] = i11I1iIiII
    if 19 - 19: OoO0O00 - Oo0Ooo . O0
   if i1II1 == 'vodgenre' :
    ooOo00 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : III1i1i11i . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11I1iIiII
    , 'subtitle' : ''
    , 'thumbnail' : oo00OO0000oO
    , 'viewage' : III1i1i11i . get ( 'viewage' )
 }
    OOooOO000 = True
    if 98 - 98: Oo0Ooo / I1IiiI . O0 + OoO0O00
   else :
    ooOo00 = { 'mode' : 'MOVIE'
 , 'contentid' : III1i1i11i . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11I1iIiII
    , 'subtitle' : ''
    , 'thumbnail' : oo00OO0000oO
    , 'viewage' : III1i1i11i . get ( 'viewage' )
 }
    if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
    OOooOO000 = False
    if 20 - 20: I1IiiI
   if ooOo00 . get ( 'viewage' ) == '21' : i11I1iIiII += ' (%s)' % ( ooOo00 . get ( 'viewage' ) )
   if 95 - 95: iII111i - I1IiiI
   self . add_dir ( i11I1iIiII , sublabel = '' , img = oo00OO0000oO , infoLabels = i1I1i111Ii , isFolder = OOooOO000 , params = ooOo00 )
   if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
  if Ooo0OOoOoO0 :
   if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
   iIIi1i1 [ 'mode' ] = 'GENRE_LIST'
   iIIi1i1 [ 'uicode' ] = i1II1
   iIIi1i1 [ 'page' ] = str ( II1IiiIi1i + 1 )
   i11I1iIiII = '[B]%s >>[/B]' % '다음 페이지'
   o0Oo0oO0oOO00 = str ( II1IiiIi1i + 1 )
   self . add_dir ( i11I1iIiII , sublabel = o0Oo0oO0oOO00 , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
  if len ( i1 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 41 - 41: i1IIi - I11i - Ii1I
  if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
  if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
  if 44 - 44: II111iiii
 def dp_Deeplink_List ( self , args ) :
  if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  oO0o0o0oo = self . get_settings_addinfo ( )
  if 35 - 35: iIii1I11I1II1
  i1II1 = args . get ( 'uicode' )
  I1i = args . get ( 'came' )
  II1IiiIi1i = int ( args . get ( 'page' ) )
  if 32 - 32: OoOoOO00 / OoO0O00 + OOooOOo
  if 32 - 32: iIii1I11I1II1 % iII111i
  if 65 - 65: ooOoO0o . OoooooooOO / I1ii11iIi11i . i1IIi * OoO0O00
  IiIiII1 , Ooo0OOoOoO0 = self . WavveObj . GetDeeplinkList ( i1II1 , I1i , II1IiiIi1i , addinfoyn = oO0o0o0oo )
  if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
  for OOOO0O00o in IiIiII1 :
   i11I1iIiII = OOOO0O00o . get ( 'title' )
   o0Oo0oO0oOO00 = OOOO0O00o . get ( 'subtitle' )
   oo00OO0000oO = OOOO0O00o . get ( 'thumbnail' )
   ooo = OOOO0O00o . get ( 'uicode' )
   IIiIiI1I = OOOO0O00o . get ( 'channelepg' )
   if 100 - 100: iIii1I11I1II1 + OoOoOO00 / Oo0Ooo . i11iIiiIii
   iIIi1i1 = { 'uicode' : ooo
   , 'came' : I1i
 , 'contentid' : OOOO0O00o . get ( 'contentid' )
 , 'contentidType' : OOOO0O00o . get ( 'contentidType' )
 , 'page' : '1'
 , 'title' : i11I1iIiII
   , 'subtitle' : o0Oo0oO0oOO00
   , 'thumbnail' : oo00OO0000oO
   , 'viewage' : OOOO0O00o . get ( 'viewage' )
 }
   if 14 - 14: o0oOOo0O0Ooo * OOooOOo + iII111i + O0 + i11iIiiIii
   if ooo == 'channel' :
    iIIi1i1 [ 'mode' ] = 'LIVE'
   elif ooo == 'movie' :
    iIIi1i1 [ 'mode' ] = 'MOVIE'
   else :
    iIIi1i1 [ 'mode' ] = 'DEEP_LIST'
    if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
    if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
   i1I1i111Ii = OOOO0O00o . get ( 'info' )
   if IIiIiI1I :
    i1I1i111Ii [ 'plot' ] = '%s\n\n%s' % ( i11I1iIiII , IIiIiI1I )
   elif ooo == 'movie' and oO0o0o0oo == True :
    i11I1iIiII = '%s (%s)' % ( i11I1iIiII , str ( i1I1i111Ii . get ( 'year' ) ) )
   else :
    i1I1i111Ii [ 'plot' ] = '%s\n\n%s' % ( i11I1iIiII , o0Oo0oO0oOO00 )
    if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
   if OOOO0O00o . get ( 'viewage' ) == '21' : o0Oo0oO0oOO00 += ' (%s)' % ( OOOO0O00o . get ( 'viewage' ) )
   if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
   if ooo in [ 'channel' , 'movie' ] :
    OOooOO000 = False
   elif iIIi1i1 [ 'contentidType' ] == 'direct' :
    OOooOO000 = False
    iIIi1i1 [ 'mode' ] = 'VOD'
   else :
    OOooOO000 = True
    if 17 - 17: i1IIi
    if 21 - 21: Oo0Ooo
   self . add_dir ( i11I1iIiII , sublabel = o0Oo0oO0oOO00 , img = oo00OO0000oO , infoLabels = i1I1i111Ii , isFolder = OOooOO000 , params = iIIi1i1 )
   if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
  if Ooo0OOoOoO0 :
   if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
   iIIi1i1 [ 'mode' ] = 'GN_LIST'
   iIIi1i1 [ 'uicode' ] = i1II1
   iIIi1i1 [ 'page' ] = str ( II1IiiIi1i + 1 )
   i11I1iIiII = '[B]%s >>[/B]' % '다음 페이지'
   o0Oo0oO0oOO00 = str ( II1IiiIi1i + 1 )
   self . add_dir ( i11I1iIiII , sublabel = o0Oo0oO0oOO00 , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
  if len ( IiIiII1 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
  if 54 - 54: i1IIi + II111iiii
  if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
  if 5 - 5: Ii1I
 def dp_Episodelink_List ( self , args ) :
  if 46 - 46: IiII
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 45 - 45: ooOoO0o
  IIi = args . get ( 'contentid' )
  ooO0oOo0o = args . get ( 'contentidType' )
  I11iiiiIIii1I = args . get ( 'uicode' )
  if 66 - 66: OoOoOO00 . i1IIi . i11iIiiIii % iII111i % ooOoO0o
  II1IiiIi1i = int ( args . get ( 'page' ) )
  if 43 - 43: O0
  Ii1 , Ooo0OOoOoO0 = self . WavveObj . GetEpisodeList ( IIi , I11iiiiIIii1I , ooO0oOo0o , II1IiiIi1i , orderby = self . get_winEpisodeOrderby ( ) )
  if 14 - 14: iIii1I11I1II1 % iIii1I11I1II1 * i11iIiiIii - OoO0O00 - I11i
  for o00oo0 in Ii1 :
   i11I1iIiII = o00oo0 . get ( 'title' )
   o0Oo0oO0oOO00 = o00oo0 . get ( 'subtitle' )
   oo00OO0000oO = o00oo0 . get ( 'thumbnail' )
   iIIi1i1 = { 'mode' : 'VOD'
 , 'uicode' : o00oo0 . get ( 'uicode' )
   , 'contentid' : o00oo0 . get ( 'contentid' )
 , 'programid' : o00oo0 . get ( 'programid' )
 , 'title' : i11I1iIiII
   , 'subtitle' : o0Oo0oO0oOO00
   , 'thumbnail' : oo00OO0000oO
   , 'viewage' : o00oo0 . get ( 'viewage' )
 }
   if 59 - 59: I1IiiI * II111iiii . O0
   if o00oo0 . get ( 'viewage' ) == '21' : o0Oo0oO0oOO00 += ' (%s)' % ( o00oo0 . get ( 'viewage' ) )
   if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
   Oo00O = o00oo0 . get ( 'info' )
   Oo00O [ 'plot' ] = o00oo0 . get ( 'synopsis' )
   if 12 - 12: o0oOOo0O0Ooo - ooOoO0o * I1Ii111
   if 14 - 14: Oo0Ooo - Ii1I % Ii1I * O0 . i11iIiiIii / O0
   if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
   if 28 - 28: i1IIi - iII111i
   self . add_dir ( i11I1iIiII , sublabel = o0Oo0oO0oOO00 , img = oo00OO0000oO , infoLabels = Oo00O , isFolder = False , params = iIIi1i1 )
   if 54 - 54: iII111i - O0 % OOooOOo
  if II1IiiIi1i == 1 :
   i1I1i111Ii = { 'plot' : '정렬순서를 변경합니다.' }
   iIIi1i1 = { }
   iIIi1i1 [ 'mode' ] = 'ORDER_BY'
   if self . get_winEpisodeOrderby ( ) == 'desc' :
    i11I1iIiII = '정렬순서변경 : 최신화부터 -> 1회부터'
    iIIi1i1 [ 'orderby' ] = 'asc'
   else :
    i11I1iIiII = '정렬순서변경 : 1회부터 -> 최신화부터'
    iIIi1i1 [ 'orderby' ] = 'desc'
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = i1I1i111Ii , isFolder = False , params = iIIi1i1 )
   if 73 - 73: O0 . OoOoOO00 + I1IiiI - I11i % I11i . I11i
  if Ooo0OOoOoO0 :
   if 17 - 17: Ii1I - OoooooooOO % Ii1I . IiII / i11iIiiIii % iII111i
   iIIi1i1 [ 'mode' ] = 'DEEP_LIST'
   iIIi1i1 [ 'uicode' ] = I11iiiiIIii1I
   iIIi1i1 [ 'contentid' ] = IIi
   iIIi1i1 [ 'contentidType' ] = ooO0oOo0o
   iIIi1i1 [ 'page' ] = str ( II1IiiIi1i + 1 )
   i11I1iIiII = '[B]%s >>[/B]' % '다음 페이지'
   o0Oo0oO0oOO00 = str ( II1IiiIi1i + 1 )
   self . add_dir ( i11I1iIiII , sublabel = o0Oo0oO0oOO00 , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 28 - 28: I11i
   if 58 - 58: OoOoOO00
  if len ( Ii1 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = True )
  if 37 - 37: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i
  if 73 - 73: i11iIiiIii - IiII
  if 25 - 25: OoooooooOO + IiII * I1ii11iIi11i
 def play_VIDEO ( self , args ) :
  if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + I1Ii111
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 18 - 18: ooOoO0o * OoOoOO00 . iII111i / I1ii11iIi11i / i11iIiiIii
  IIi = args . get ( 'contentid' )
  I11iiiiIIii1I = args . get ( 'uicode' )
  IIIII = self . get_selQuality ( )
  if 78 - 78: Ii1I * i1IIi
  self . addon_log ( IIi + ' - ' + I11iiiiIIii1I , False )
  iI11 , o00oOoOo0 , o0O0O0ooo0oOO , oo000 = self . WavveObj . GetStreamingURL ( IIi , I11iiiiIIii1I , IIIII )
  if 32 - 32: i1IIi . Ii1I
  if 59 - 59: OoooooooOO
  i1iiiii1 = '%s|Cookie=%s' % ( iI11 , o00oOoOo0 )
  self . addon_log ( i1iiiii1 , False )
  if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
  if iI11 == '' :
   self . addon_noti ( __language__ ( 30303 ) . encode ( 'utf8' ) )
   return
   if 100 - 100: OoO0O00
  II1i = xbmcgui . ListItem ( path = i1iiiii1 )
  if 2 - 2: iIii1I11I1II1 * Oo0Ooo % oO0o - II111iiii - iII111i
  if o0O0O0ooo0oOO :
   if 3 - 3: I1Ii111
   if 45 - 45: I1Ii111
   oO = o0O0O0ooo0oOO [ 'customdata' ]
   IIi1iiii1iI = o0O0O0ooo0oOO [ 'drmhost' ]
   if 25 - 25: I1ii11iIi11i + O0
   i1II = 'mpd'
   O0OOO0OOooo00 = 'com.widevine.alpha'
   if 6 - 6: Ii1I - ooOoO0o * OOooOOo . iII111i / O0 * ooOoO0o
   II11iI111i1 = inputstreamhelper . Helper ( i1II , drm = O0OOO0OOooo00 )
   if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
   if II11iI111i1 . check_inputstream ( ) :
    if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
    if I11iiiiIIii1I == 'movie' :
     o00 = 'https://www.wavve.com/player/movie?movieid=%s' % IIi
    else :
     o00 = 'https://www.wavve.com/player/vod?programid=%s&page=1' % IIi
     if 85 - 85: I1ii11iIi11i . I1Ii111
    O0O0Ooooo000 = { 'content-type' : 'application/octet-stream'
 , 'origin' : 'https://www.wavve.com'
 , 'pallycon-customdata' : oO
 , 'referer' : o00
 , 'sec-fetch-dest' : 'empty'
    , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'

    , 'user-agent' : OOo000
 }
    o000oOoo0o000 = IIi1iiii1iI + '|' + urllib . urlencode ( O0O0Ooooo000 ) + '|R{SSM}|'
    if 40 - 40: i11iIiiIii * I1Ii111 - i1IIi * I1Ii111 - I11i . i1IIi
    II1i . setProperty ( 'inputstreamaddon' , II11iI111i1 . inputstream_addon )
    II1i . setProperty ( 'inputstream.adaptive.manifest_type' , i1II )
    II1i . setProperty ( 'inputstream.adaptive.license_type' , O0OOO0OOooo00 )
    if 99 - 99: O0 * I11i
    II1i . setProperty ( 'inputstream.adaptive.license_key' , o000oOoo0o000 )
    II1i . setProperty ( 'inputstream.adaptive.stream_headers' , 'Cookie=%s' % o00oOoOo0 )
    if 64 - 64: II111iiii + O0 / iIii1I11I1II1 / Oo0Ooo . ooOoO0o % IiII
  xbmcplugin . setResolvedUrl ( self . _addon_handle , True , II1i )
  if 50 - 50: iIii1I11I1II1 - IiII + OOooOOo
  if oo000 :
   self . addon_noti ( oo000 . encode ( 'utf-8' ) )
  else :
   if '/preview.' in urlparse . urlsplit ( iI11 ) . path : self . addon_noti ( __language__ ( 30401 ) . encode ( 'utf8' ) )
   if 69 - 69: O0
  try :
   if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) and args . get ( 'viewage' ) != '21' :
    iIIi1i1 = { 'code' : args . get ( 'programid' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'contentid' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 , 'subtitle' : args . get ( 'subtitle' )
 , 'videoid' : args . get ( 'contentid' )
    }
    self . Save_Watched_List ( args . get ( 'mode' ) . lower ( ) , iIIi1i1 )
  except :
   None
   if 85 - 85: ooOoO0o / O0
   if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
   if 62 - 62: I1Ii111 . IiII . OoooooooOO
   if 11 - 11: OOooOOo / I11i
 def dp_Watch_List ( self , args ) :
  i11i1 = args . get ( 'genre' )
  oOooOOo00Oo0O = self . get_settings_direct_replay ( )
  if 73 - 73: i1IIi / i11iIiiIii
  if i11i1 == '-' :
   i11I1iIiII = 'VOD 시청내역'
   iIIi1i1 = { 'mode' : 'WATCH'
 , 'genre' : 'vod'
 }
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
   i11I1iIiII = '영화 시청내역'
   iIIi1i1 [ 'genre' ] = 'movie'
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 85 - 85: OoOoOO00 + OOooOOo
   xbmcplugin . endOfDirectory ( self . _addon_handle )
   if 10 - 10: IiII / OoO0O00 + OoOoOO00 / i1IIi
  else :
   i1iII1II11I = self . Load_Watched_List ( i11i1 )
   if 54 - 54: IiII + O0 + I11i * I1Ii111 - OOooOOo % oO0o
   for I111 in i1iII1II11I :
    iI1I1i11iIIii = dict ( urlparse . parse_qsl ( I111 ) )
    if 46 - 46: oO0o % OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111 * I1ii11iIi11i
    i11I1iIiII = iI1I1i11iIIii . get ( 'title' ) . strip ( )
    o0Oo0oO0oOO00 = iI1I1i11iIIii . get ( 'subtitle' ) . strip ( )
    if o0Oo0oO0oOO00 == 'None' : o0Oo0oO0oOO00 = ''
    oo00OO0000oO = iI1I1i11iIIii . get ( 'img' )
    iIIIIIii = iI1I1i11iIIii . get ( 'videoid' )
    if 15 - 15: i11iIiiIii % I1IiiI * I11i / I1Ii111
    if 90 - 90: iII111i
    i1I1i111Ii = { }
    if i11i1 == 'movie' and self . get_settings_addinfo ( ) == True :
     i1i1i1I = self . WavveObj . GetMovieInfoList ( [ iI1I1i11iIIii . get ( 'code' ) ] )
     i1I1i111Ii = i1i1i1I . get ( iI1I1i11iIIii . get ( 'code' ) )
    else :
     i1I1i111Ii [ 'plot' ] = '%s\n%s' % ( i11I1iIiII , o0Oo0oO0oOO00 )
     if 83 - 83: oO0o + OoooooooOO
    if i11i1 == 'vod' :
     if oOooOOo00Oo0O == False or iIIIIIii == None :
      iIIi1i1 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : iI1I1i11iIIii . get ( 'code' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
      OOooOO000 = True
     else :
      iIIi1i1 = { 'mode' : 'VOD'
 , 'contentid' : iIIIIIii
 , 'contentidType' : 'contentid'
 , 'programid' : iI1I1i11iIIii . get ( 'code' )
 , 'uicode' : 'vod'
 , 'title' : i11I1iIiII
 , 'subtitle' : o0Oo0oO0oOO00
 , 'thumbnail' : oo00OO0000oO
 }
      OOooOO000 = False
    else :
     iIIi1i1 = { 'mode' : 'MOVIE'
 , 'contentid' : iI1I1i11iIIii . get ( 'code' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'title' : i11I1iIiII
 , 'thumbnail' : oo00OO0000oO
 }
     OOooOO000 = False
     if 22 - 22: Ii1I % iII111i * OoooooooOO - o0oOOo0O0Ooo / iIii1I11I1II1
    self . add_dir ( i11I1iIiII , sublabel = o0Oo0oO0oOO00 , img = oo00OO0000oO , infoLabels = i1I1i111Ii , isFolder = OOooOO000 , params = iIIi1i1 )
    if 86 - 86: OoooooooOO . iII111i % OoOoOO00 / I11i * iII111i / o0oOOo0O0Ooo
   i1I1i111Ii = { 'plot' : '시청목록을 삭제합니다.' }
   i11I1iIiII = '*** 시청목록 삭제 ***'
   iIIi1i1 = { 'mode' : 'MYVIEW_REMOVE'
 , 'genre' : i11i1
 }
   if 64 - 64: i11iIiiIii
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = i1I1i111Ii , isFolder = False , params = iIIi1i1 )
   if 38 - 38: IiII / I1IiiI - IiII . I11i
   xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
   if 69 - 69: OoooooooOO + I1ii11iIi11i
   if 97 - 97: OOooOOo - OoO0O00 / Ii1I . i11iIiiIii % oO0o * oO0o
   if 1 - 1: I1IiiI % ooOoO0o
   if 65 - 65: I1IiiI + OoOoOO00 / OOooOOo
   if 83 - 83: o0oOOo0O0Ooo . iII111i - Oo0Ooo
 def dp_Search_Group ( self , args ) :
  i11I1iIiII = 'VOD 검색'
  iIIi1i1 = { 'mode' : 'SEARCH_LIST'
 , 'genre' : 'vod'
 , 'page' : '1'
 }
  self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if 65 - 65: iIii1I11I1II1 / ooOoO0o . IiII - II111iiii
  i11I1iIiII = '영화 검색'
  iIIi1i1 [ 'genre' ] = 'movie'
  self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if 72 - 72: iIii1I11I1II1 / IiII % iII111i % OOooOOo - I11i % OOooOOo
  xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 100 - 100: Oo0Ooo + i11iIiiIii
  if 71 - 71: I11i / o0oOOo0O0Ooo / I1Ii111 % OOooOOo
  if 51 - 51: IiII * O0 / II111iiii . Ii1I % OOooOOo / I1IiiI
  if 9 - 9: I1IiiI % I1IiiI % II111iiii
 def dp_Search_List ( self , args ) :
  if 30 - 30: IiII + I1Ii111 - IiII . IiII - II111iiii + O0
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  oO0o0o0oo = self . get_settings_addinfo ( )
  if 86 - 86: i1IIi
  I11iiiiIIii1I = args . get ( 'genre' )
  II1IiiIi1i = int ( args . get ( 'page' ) )
  if 41 - 41: OoOoOO00 * I11i / OoOoOO00 % oO0o
  if 'search_key' in args :
   Ii = args . get ( 'search_key' )
  else :
   Ii = self . get_keyboard_input ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
   if not Ii : return
   if 77 - 77: OoOoOO00 % Ii1I
  II1IiiIii , Ooo0OOoOoO0 = self . WavveObj . GetSearchList ( Ii , I11iiiiIIii1I , II1IiiIi1i , exclusion21 = self . get_settings_exclusion21 ( ) , addinfoyn = oO0o0o0oo )
  if 84 - 84: oO0o % i1IIi
  for oOO in II1IiiIii :
   i11I1iIiII = oOO . get ( 'title' )
   oo00OO0000oO = oOO . get ( 'thumbnail' )
   if 17 - 17: II111iiii / I1ii11iIi11i % IiII + I1IiiI * I1Ii111
   i1I1i111Ii = oOO . get ( 'info' )
   if I11iiiiIIii1I == 'movie' and oO0o0o0oo == True :
    i11I1iIiII = '%s (%s)' % ( i11I1iIiII , str ( i1I1i111Ii . get ( 'year' ) ) )
   else :
    i1I1i111Ii [ 'plot' ] = i11I1iIiII
    if 36 - 36: I1Ii111 * OoO0O00
   if I11iiiiIIii1I == 'vod' :
    iIIi1i1 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : oOO . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11I1iIiII
    , 'subtitle' : ''
    , 'thumbnail' : oo00OO0000oO
    , 'viewage' : oOO . get ( 'viewage' )
 }
    OOooOO000 = True
    if 23 - 23: I11i . OoooooooOO - OOooOOo + IiII . II111iiii
   else :
    iIIi1i1 = { 'mode' : 'MOVIE'
 , 'contentid' : oOO . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11I1iIiII
    , 'subtitle' : ''
    , 'thumbnail' : oo00OO0000oO
    , 'viewage' : oOO . get ( 'viewage' )
 }
    if 54 - 54: ooOoO0o
    OOooOO000 = False
    if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
   if iIIi1i1 . get ( 'viewage' ) == '21' : i11I1iIiII += ' (%s)' % ( iIIi1i1 . get ( 'viewage' ) )
   if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
   self . add_dir ( i11I1iIiII , sublabel = '' , img = oo00OO0000oO , infoLabels = i1I1i111Ii , isFolder = OOooOO000 , params = iIIi1i1 )
   if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - I11i
  if Ooo0OOoOoO0 :
   if 30 - 30: OoOoOO00
   iIIi1i1 [ 'mode' ] = 'SEARCH_LIST'
   iIIi1i1 [ 'genre' ] = I11iiiiIIii1I
   iIIi1i1 [ 'page' ] = str ( II1IiiIi1i + 1 )
   iIIi1i1 [ 'search_key' ] = Ii
   i11I1iIiII = '[B]%s >>[/B]' % '다음 페이지'
   o0Oo0oO0oOO00 = str ( II1IiiIi1i + 1 )
   self . add_dir ( i11I1iIiII , sublabel = o0Oo0oO0oOO00 , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 21 - 21: i11iIiiIii / I1Ii111 % OOooOOo * O0 . I11i - iIii1I11I1II1
  if len ( II1IiiIii ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 26 - 26: II111iiii * OoOoOO00
  if 10 - 10: II111iiii . iII111i
  if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
  if 88 - 88: iII111i
  if 19 - 19: II111iiii * IiII + Ii1I
 def Load_Watched_List ( self , genre ) :
  try :
   O0o = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   with open ( O0o , 'r' ) as oO00oO :
    i11i1iIiii = oO00oO . readlines ( )
  except :
   i11i1iIiii = [ ]
   if 71 - 71: I1ii11iIi11i % ooOoO0o - I1IiiI % I11i - O0
  return i11i1iIiii
  if 67 - 67: OOooOOo + Oo0Ooo
  if 84 - 84: O0 * OoooooooOO - IiII * IiII
  if 8 - 8: ooOoO0o / i1IIi . oO0o
  if 41 - 41: iII111i + OoO0O00
 def Save_Watched_List ( self , genre , in_params ) :
  try :
   O0o = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   oOOiiiIIiIi = self . Load_Watched_List ( genre )
   if 68 - 68: O0 + OoOoOO00 / oO0o - OOooOOo + iIii1I11I1II1 % Ii1I
   with open ( O0o , 'w' ) as oO00oO :
    i1iI1iii11i = urllib . urlencode ( in_params )
    i1iI1iii11i = i1iI1iii11i . encode ( 'utf-8' ) + '\n'
    oO00oO . write ( i1iI1iii11i )
    if 62 - 62: Oo0Ooo * OoOoOO00
    OO0 = 0
    for OOO0oOOo00O in oOOiiiIIiIi :
     OO0o = dict ( urlparse . parse_qsl ( OOO0oOOo00O ) )
     if 39 - 39: o0oOOo0O0Ooo * ooOoO0o + Ii1I * II111iiii
     OoO00o0 = in_params . get ( 'code' )
     OOoOoO00O0O0o = OO0o . get ( 'code' )
     if genre == 'vod' and self . get_settings_direct_replay ( ) == True :
      OoO00o0 = in_params . get ( 'videoid' )
      OOoOoO00O0O0o = OO0o . get ( 'videoid' ) if OOoOoO00O0O0o != None else '-'
      if 12 - 12: I1ii11iIi11i + OoO0O00 % I11i
     if OoO00o0 != OOoOoO00O0O0o :
      oO00oO . write ( OOO0oOOo00O )
      OO0 += 1
      if OO0 >= 50 : break
  except :
   None
   if 85 - 85: iII111i * o0oOOo0O0Ooo
   if 3 - 3: OOooOOo
   if 20 - 20: II111iiii . iII111i / II111iiii % i11iIiiIii % iII111i
   if 11 - 11: IiII % I1ii11iIi11i % Ii1I / II111iiii % I1Ii111 - Oo0Ooo
 def Delete_Watched_List ( self , genre ) :
  try :
   O0o = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   with open ( O0o , 'w' ) as oO00oO :
    oO00oO . write ( '' )
  except :
   None
   if 96 - 96: I1ii11iIi11i / II111iiii . Ii1I - iII111i * I11i * oO0o
   if 76 - 76: Ii1I - II111iiii * OOooOOo / OoooooooOO
   if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
   if 71 - 71: OoooooooOO
 def dp_WatchList_Delete ( self , args ) :
  i11i1 = args . get ( 'genre' )
  if 33 - 33: I1Ii111
  OoooooOoo = xbmcgui . Dialog ( )
  ooOOOoOooOoO = OoooooOoo . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if ooOOOoOooOoO == False : sys . exit ( )
  if 62 - 62: I1ii11iIi11i + Ii1I + i1IIi / OoooooooOO
  self . Delete_Watched_List ( i11i1 )
  if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
  xbmc . executebuiltin ( "Container.Refresh" )
  if 22 - 22: ooOoO0o - ooOoO0o % OOooOOo . I1Ii111 + oO0o
  if 63 - 63: I1IiiI % I1Ii111 * o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % iII111i
  if 45 - 45: IiII
  if 20 - 20: OoooooooOO * o0oOOo0O0Ooo * O0 . OOooOOo
 def logout ( self ) :
  OoooooOoo = xbmcgui . Dialog ( )
  ooOOOoOooOoO = OoooooOoo . yesno ( __language__ ( 30910 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if ooOOOoOooOoO == False : sys . exit ( )
  if 78 - 78: iIii1I11I1II1 + I11i - Ii1I * I1Ii111 - OoooooooOO % OoOoOO00
  self . wininfo_clear ( )
  if 34 - 34: O0
  if 80 - 80: i1IIi - Oo0Ooo / OoO0O00 - i11iIiiIii
  if os . path . isfile ( O0I11i1i11i1I ) : os . remove ( O0I11i1i11i1I )
  if 68 - 68: oO0o - I1ii11iIi11i % O0 % I1Ii111
  self . addon_noti ( __language__ ( 30909 ) . encode ( 'utf-8' ) )
  if 11 - 11: O0 / OoO0O00 % OOooOOo + o0oOOo0O0Ooo + iIii1I11I1II1
  if 40 - 40: ooOoO0o - OOooOOo . Ii1I * Oo0Ooo % I1Ii111
  if 56 - 56: i11iIiiIii . o0oOOo0O0Ooo - I1IiiI * I11i
  if 91 - 91: oO0o + OoooooooOO - i1IIi
 def wininfo_clear ( self ) :
  if 84 - 84: Ii1I / IiII
  IIi1iIIiI = xbmcgui . Window ( 10000 )
  IIi1iIIiI . setProperty ( 'WAVVE_M_CREDENTIAL' , '' )
  IIi1iIIiI . setProperty ( 'WAVVE_M_LOGINTIME' , '' )
  if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / OOooOOo
  if 11 - 11: I1IiiI * oO0o + I1ii11iIi11i / I1ii11iIi11i
  if 37 - 37: i11iIiiIii + i1IIi
  if 23 - 23: iII111i + I11i . OoOoOO00 * I1IiiI + I1ii11iIi11i
 def cookiefile_save ( self ) :
  I1iIi1iiiIiI = datetime . datetime . now ( )
  III1I1Ii11iI = I1iIi1iiiIiI + datetime . timedelta ( days = int ( __addon__ . getSetting ( 'cache_ttl' ) ) )
  if 52 - 52: OOooOOo - iII111i * oO0o
  IIi1iIIiI = xbmcgui . Window ( 10000 )
  Ii1I11I = { 'wavve_token' : IIi1iIIiI . getProperty ( 'WAVVE_M_CREDENTIAL' )
 , 'wavve_id' : base64 . standard_b64encode ( __addon__ . getSetting ( 'id' ) . encode ( ) ) . decode ( 'utf-8' )
 , 'wavve_pw' : base64 . standard_b64encode ( __addon__ . getSetting ( 'pw' ) . encode ( ) ) . decode ( 'utf-8' )
 , 'wavve_profile' : __addon__ . getSetting ( 'selected_profile' )
 , 'wavve_limitdate' : III1I1Ii11iI . strftime ( '%Y-%m-%d' )
 }
  if 36 - 36: O0 + Oo0Ooo
  try :
   with open ( O0I11i1i11i1I , 'w' ) as oO00oO :
    json . dump ( Ii1I11I , oO00oO )
  except Exception as iIIIi1i1I11i :
   print ( iIIIi1i1I11i )
   if 55 - 55: Oo0Ooo - OOooOOo
   if 84 - 84: I1Ii111 + Oo0Ooo - OoOoOO00 * OoOoOO00
   if 61 - 61: OoooooooOO . oO0o . OoooooooOO / Oo0Ooo
   if 72 - 72: i1IIi
 def cookiefile_check ( self ) :
  if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i . OoooooooOO
  if 63 - 63: I1ii11iIi11i
  Ii1I11I = { }
  try :
   with open ( O0I11i1i11i1I , 'r' ) as oO00oO :
    Ii1I11I = json . load ( oO00oO )
  except Exception as iIIIi1i1I11i :
   self . wininfo_clear ( )
   return False
   if 6 - 6: ooOoO0o / I1ii11iIi11i
   if 57 - 57: I11i
   if 67 - 67: OoO0O00 . ooOoO0o
  oOOo0oOo0 = __addon__ . getSetting ( 'id' )
  II = __addon__ . getSetting ( 'pw' )
  oO00oOo0OOO = __addon__ . getSetting ( 'selected_profile' )
  Ii1I11I [ 'wavve_id' ] = base64 . standard_b64decode ( Ii1I11I [ 'wavve_id' ] ) . decode ( 'utf-8' )
  Ii1I11I [ 'wavve_pw' ] = base64 . standard_b64decode ( Ii1I11I [ 'wavve_pw' ] ) . decode ( 'utf-8' )
  if oOOo0oOo0 != Ii1I11I [ 'wavve_id' ] or II != Ii1I11I [ 'wavve_pw' ] or oO00oOo0OOO != Ii1I11I [ 'wavve_profile' ] :
   self . wininfo_clear ( )
   return False
   if 23 - 23: i1IIi . o0oOOo0O0Ooo * OoO0O00
   if 15 - 15: OoOoOO00
   if 62 - 62: Ii1I
   if 51 - 51: OoOoOO00
   if 14 - 14: IiII % oO0o % Oo0Ooo - i11iIiiIii
   if 53 - 53: Ii1I % Oo0Ooo
   if 59 - 59: OOooOOo % iIii1I11I1II1 . i1IIi + II111iiii * IiII
   if 41 - 41: Ii1I % I1ii11iIi11i
   if 12 - 12: OOooOOo
   if 69 - 69: OoooooooOO + OOooOOo
  IIi1 = int ( datetime . datetime . now ( ) . strftime ( '%Y%m%d' ) )
  IIi11I1 = Ii1I11I [ 'wavve_limitdate' ]
  I1I1I = int ( re . sub ( '-' , '' , IIi11I1 ) )
  if 49 - 49: II111iiii - I1IiiI / I11i
  if 74 - 74: I11i - OOooOOo + i1IIi . I1IiiI + OOooOOo - I11i
  if I1I1I < IIi1 :
   self . wininfo_clear ( )
   return False
   if 17 - 17: O0 . I1Ii111 . O0 + O0 / Oo0Ooo . ooOoO0o
   if 62 - 62: I1ii11iIi11i % iII111i * OoO0O00 - i1IIi
  IIi1iIIiI = xbmcgui . Window ( 10000 )
  IIi1iIIiI . setProperty ( 'WAVVE_M_CREDENTIAL' , Ii1I11I [ 'wavve_token' ] )
  IIi1iIIiI . setProperty ( 'WAVVE_M_LOGINTIME' , IIi11I1 )
  if 66 - 66: i11iIiiIii / o0oOOo0O0Ooo - OoooooooOO / i1IIi . i11iIiiIii
  return True
  if 16 - 16: Oo0Ooo % I1ii11iIi11i + I11i - O0 . iII111i / I1Ii111
  if 35 - 35: oO0o / I1Ii111 / II111iiii - iIii1I11I1II1 + II111iiii . I1Ii111
  if 81 - 81: iII111i * OOooOOo - I1ii11iIi11i * Ii1I % OoOoOO00 * OoOoOO00
  if 59 - 59: iIii1I11I1II1
 def wavve_main ( self ) :
  if 7 - 7: OOooOOo * I1IiiI / o0oOOo0O0Ooo * i11iIiiIii
  II1IIIIiII1i = self . main_params . get ( 'mode' , None )
  if 84 - 84: OOooOOo . iII111i
  self . login_main ( )
  if II1IIIIiII1i is None :
   if 8 - 8: Oo0Ooo + II111iiii * OOooOOo * OoOoOO00 * I11i / IiII
   self . dp_Main_List ( )
   if 21 - 21: oO0o / OoooooooOO
   if 11 - 11: OOooOOo % Ii1I - i11iIiiIii - oO0o + ooOoO0o + IiII
   if 87 - 87: I1Ii111 * i1IIi / I1ii11iIi11i
   if 6 - 6: o0oOOo0O0Ooo + Oo0Ooo - OoooooooOO % OOooOOo * OoOoOO00
   if 69 - 69: i1IIi
   if 59 - 59: II111iiii - o0oOOo0O0Ooo
   if 24 - 24: Oo0Ooo - i1IIi + I11i
   if 38 - 38: OoooooooOO / I1ii11iIi11i . O0 / i1IIi / Oo0Ooo + iIii1I11I1II1
   if 96 - 96: iII111i
  elif II1IIIIiII1i == 'GNB_LIST' :
   self . dp_Gnb_List ( self . main_params )
   if 18 - 18: iII111i * I11i - Ii1I
  elif II1IIIIiII1i == 'GN_LIST' :
   self . dp_Deeplink_List ( self . main_params )
   if 31 - 31: Oo0Ooo - O0 % OoOoOO00 % oO0o
  elif II1IIIIiII1i == 'DEEP_LIST' :
   I11iiiiIIii1I = self . main_params . get ( 'uicode' , None )
   if 45 - 45: I1ii11iIi11i + II111iiii * i11iIiiIii
   if I11iiiiIIii1I in [ 'quick' , 'vod' , 'program' , 'x' ] :
    self . dp_Episodelink_List ( self . main_params )
    if 13 - 13: OoooooooOO * oO0o - Ii1I / OOooOOo + I11i + IiII
   else : None
   if 39 - 39: iIii1I11I1II1 - OoooooooOO
  elif II1IIIIiII1i in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
   self . play_VIDEO ( self . main_params )
   if 81 - 81: I1ii11iIi11i - O0 * OoooooooOO
   time . sleep ( 0.1 )
   if 23 - 23: II111iiii / oO0o
  elif II1IIIIiII1i == 'GN_MYVIEW' :
   self . dp_Myview_Group ( self . main_params )
   if 28 - 28: Oo0Ooo * ooOoO0o - OoO0O00
  elif II1IIIIiII1i == 'MYVIEW_LIST' :
   self . dp_Myview_List ( self . main_params )
   if 19 - 19: I11i
  elif II1IIIIiII1i == 'GENRE' :
   self . dp_Genre_Group ( self . main_params )
   if 67 - 67: O0 % iIii1I11I1II1 / IiII . i11iIiiIii - Ii1I + O0
  elif II1IIIIiII1i == 'GENRE_LIST' :
   self . dp_Genre_List ( self . main_params )
   if 27 - 27: OOooOOo
  elif II1IIIIiII1i == 'WATCH' :
   self . dp_Watch_List ( self . main_params )
   if 89 - 89: II111iiii / oO0o
  elif II1IIIIiII1i == 'MYVIEW_REMOVE' :
   self . dp_WatchList_Delete ( self . main_params )
   if 14 - 14: OOooOOo . I1IiiI * ooOoO0o + II111iiii - ooOoO0o + OOooOOo
  elif II1IIIIiII1i == 'SEARCH' :
   self . dp_Search_Group ( self . main_params )
   if 18 - 18: oO0o - o0oOOo0O0Ooo - I1IiiI - I1IiiI
  elif II1IIIIiII1i == 'SEARCH_LIST' :
   self . dp_Search_List ( self . main_params )
   if 54 - 54: Oo0Ooo + I1IiiI / iII111i . I1IiiI * OoOoOO00
  elif II1IIIIiII1i == 'ORDER_BY' :
   self . dp_setEpOrderby ( self . main_params )
   if 1 - 1: OoOoOO00 * OoO0O00 . i1IIi / Oo0Ooo . I1ii11iIi11i + Oo0Ooo
  elif II1IIIIiII1i == 'LOGOUT' :
   self . logout ( )
   if 17 - 17: Oo0Ooo + OoO0O00 / Ii1I / iII111i * OOooOOo
   if 29 - 29: OoO0O00 % OoooooooOO * oO0o / II111iiii - oO0o
   if 19 - 19: i11iIiiIii
   if 54 - 54: II111iiii . I11i
   if 73 - 73: OoOoOO00 . I1IiiI
   if 32 - 32: OoOoOO00 * I1IiiI % ooOoO0o * Ii1I . O0
  else :
   None
   if 48 - 48: iII111i * iII111i
   if 13 - 13: Ii1I / I11i + OoOoOO00 . o0oOOo0O0Ooo % ooOoO0o
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
