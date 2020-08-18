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
  i1Iii1i1I = datetime . datetime . now ( ) . date ( )
  OOoO00 = xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINTIME' )
  if OOoO00 == None or OOoO00 == '' : OOoO00 = '1900-01-01'
  try :
   OOoO00 = datetime . datetime . strptime ( OOoO00 , '%Y-%m-%d' ) . date ( )
  except TypeError :
   OOoO00 = datetime . datetime ( * ( time . strptime ( OOoO00 , '%Y-%m-%d' ) [ 0 : 6 ] ) ) . date ( )
   if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
   if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
   if 23 - 23: O0
  if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINWAIT' ) == 'TRUE' :
   o00oO0oOo00 = 0
   while True :
    o00oO0oOo00 += 1
    if 81 - 81: OoO0O00
    time . sleep ( 0.05 )
    if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iII111i / OoOoOO00
    if 84 - 84: ooOoO0o * II111iiii + Oo0Ooo
    if OOoO00 >= i1Iii1i1I : return
    if o00oO0oOo00 > 600 : return
  else :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'TRUE' )
   if 53 - 53: iII111i % II111iiii . IiII - iIii1I11I1II1 - IiII * II111iiii
   if 77 - 77: iIii1I11I1II1 * OoO0O00
  if OOoO00 >= i1Iii1i1I :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
   return
   if 95 - 95: I1IiiI + i11iIiiIii
  if not self . WavveObj . GetCredential ( oOOo0oOo0 , II , ooooo ) :
   self . addon_noti ( __language__ ( 30103 ) . encode ( 'utf8' ) )
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
   sys . exit ( )
   if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
   if 80 - 80: II111iiii
  self . set_winCredential ( self . WavveObj . LoadCredential ( ) )
  if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
  self . cookiefile_save ( )
  xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
  if 53 - 53: II111iiii
  if 31 - 31: OoO0O00
  if 80 - 80: I1Ii111 . i11iIiiIii - o0oOOo0O0Ooo
  if 25 - 25: OoO0O00
  if 62 - 62: OOooOOo + O0
  if 98 - 98: o0oOOo0O0Ooo
 def dp_setEpOrderby ( self , args ) :
  OOOO0oo0 = args . get ( 'orderby' )
  if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
  self . set_winEpisodeOrderby ( OOOO0oo0 )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 47 - 47: iII111i - Ii1I . II111iiii + OoooooooOO . i11iIiiIii
  if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
  if 87 - 87: Oo0Ooo . IiII
  if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
 def dp_Gnb_List ( self , args ) :
  if 55 - 55: OOooOOo . I1IiiI
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 61 - 61: Oo0Ooo % IiII . Oo0Ooo
  o0oOO000oO0oo = self . WavveObj . GetGnList ( args . get ( 'uicode' ) )
  if 78 - 78: I1ii11iIi11i + OOooOOo - I1Ii111
  if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
  if 57 - 57: OoO0O00 / ooOoO0o
  if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
  for I111I1Iiii1i in o0oOO000oO0oo :
   i11I1iIiII = I111I1Iiii1i . get ( 'title' )
   iIIi1i1 = { 'mode' : 'GN_LIST' if I111I1Iiii1i . get ( 'uicode' ) != 'CY1' else 'GN_MYVIEW'
   , 'uicode' : I111I1Iiii1i . get ( 'uicode' )
 , 'came' : args . get ( 'came' )
 , 'page' : '1'
 }
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if len ( o0oOO000oO0oo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
  if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
  if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
  if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
 def dp_Myview_Group ( self , args ) :
  i11I1iIiII = 'VOD 시청내역'
  iIIi1i1 = { 'mode' : 'MYVIEW_LIST'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
  self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
  i11I1iIiII = '영화 시청내역'
  iIIi1i1 [ 'uicode' ] = 'movie'
  self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if 63 - 63: OoOoOO00 * iII111i
  xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 69 - 69: O0 . OoO0O00
  if 49 - 49: I1IiiI - I11i
  if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
  if 62 - 62: OoooooooOO * I1IiiI
 def dp_Myview_List ( self , args ) :
  if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  i1 = self . get_settings_addinfo ( )
  if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * IiII
  OOOoOo = args . get ( 'uicode' )
  O00o0 = int ( args . get ( 'page' ) )
  I11iII , iIIII = self . WavveObj . GetMyviewList ( OOOoOo , O00o0 , addinfoyn = i1 )
  if 33 - 33: ooOoO0o . II111iiii % iII111i + o0oOOo0O0Ooo
  for oO00O000oO0 in I11iII :
   i11I1iIiII = oO00O000oO0 . get ( 'title' )
   O0OoOO0o = oO00O000oO0 . get ( 'subtitle' )
   ooooo0O0000oo = oO00O000oO0 . get ( 'thumbnail' )
   if 21 - 21: o0oOOo0O0Ooo - I1IiiI
   II11I1 = oO00O000oO0 . get ( 'info' )
   if OOOoOo == 'movie' and i1 == True :
    i11I1iIiII = '%s (%s)' % ( i11I1iIiII , str ( II11I1 . get ( 'year' ) ) )
   else :
    II11I1 [ 'plot' ] = i11I1iIiII
    if 62 - 62: I1ii11iIi11i / i1IIi
   if OOOoOo == 'vod' :
    iIIi1i1 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : oO00O000oO0 . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11I1iIiII
    , 'subtitle' : O0OoOO0o
    , 'thumbnail' : ooooo0O0000oo
    , 'viewage' : oO00O000oO0 . get ( 'viewage' )
 }
    OOooOO000 = True
    if 98 - 98: i1IIi / I11i
   else :
    iIIi1i1 = { 'mode' : 'MOVIE'
 , 'contentid' : oO00O000oO0 . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11I1iIiII
    , 'subtitle' : O0OoOO0o
    , 'thumbnail' : ooooo0O0000oo
    , 'viewage' : oO00O000oO0 . get ( 'viewage' )
 }
    OOooOO000 = False
    if 32 - 32: Ii1I * iIii1I11I1II1 / OOooOOo
   if oO00O000oO0 . get ( 'viewage' ) == '21' : O0OoOO0o += ' (%s)' % ( oO00O000oO0 . get ( 'viewage' ) )
   if 38 - 38: ooOoO0o % II111iiii % I11i / OoO0O00 + OoOoOO00 / i1IIi
   self . add_dir ( i11I1iIiII , sublabel = O0OoOO0o , img = ooooo0O0000oo , infoLabels = II11I1 , isFolder = OOooOO000 , params = iIIi1i1 )
   if 54 - 54: iIii1I11I1II1 % I1ii11iIi11i - OOooOOo / oO0o - OoO0O00 . I11i
  if iIIII :
   if 11 - 11: I1ii11iIi11i . OoO0O00 * IiII * OoooooooOO + ooOoO0o
   iIIi1i1 [ 'mode' ] = 'MYVIEW_LIST'
   iIIi1i1 [ 'uicode' ] = OOOoOo
   iIIi1i1 [ 'page' ] = str ( O00o0 + 1 )
   i11I1iIiII = '[B]%s >>[/B]' % '다음 페이지'
   O0OoOO0o = str ( O00o0 + 1 )
   self . add_dir ( i11I1iIiII , sublabel = O0OoOO0o , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
  if len ( I11iII ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
  if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
  if 26 - 26: Ii1I % I1ii11iIi11i
  if 76 - 76: IiII * iII111i
  if 52 - 52: OOooOOo
 def dp_Genre_Group ( self , args ) :
  if 19 - 19: I1IiiI
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 25 - 25: Ii1I / ooOoO0o
  IIooO = args . get ( 'mode' )
  Ooo0oOooo0 = args . get ( 'uicode' )
  oOOOoo00 = args . get ( 'genre' )
  iiIiIIIiiI = args . get ( 'subgenre' )
  OOOO0oo0 = args . get ( 'orderby' )
  iiI1IIIi = args . get ( 'ordernm' )
  if 47 - 47: Oo0Ooo % I11i % i11iIiiIii - O0 + ooOoO0o
  if oOOOoo00 == '-' :
   ooO000OO0O00O = self . WavveObj . GetGenreGroup ( Ooo0oOooo0 , oOOOoo00 , OOOO0oo0 , iiI1IIIi , exclusion21 = self . get_settings_exclusion21 ( ) )
  else :
   OOOoOO0o = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 , 'orderby' : OOOO0oo0
 , 'ordernm' : iiI1IIIi
 }
   if 1 - 1: II111iiii
   ooO000OO0O00O = self . WavveObj . GetGenreGroup_sub ( OOOoOO0o )
   if 68 - 68: iII111i - I1IiiI / I1Ii111 / I11i
   if 12 - 12: Ii1I + i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . I11i
  for Iii1iI in ooO000OO0O00O :
   i11I1iIiII = Iii1iI . get ( 'title' ) + '  (' + iiI1IIIi + ')'
   if 29 - 29: I1IiiI % OOooOOo - I1IiiI / OOooOOo . i1IIi
   iIIi1i1 = { 'mode' : IIooO
 , 'uicode' : Ooo0oOooo0
   , 'genre' : Iii1iI . get ( 'genre' )
 , 'subgenre' : Iii1iI . get ( 'subgenre' )
 , 'adult' : Iii1iI . get ( 'adult' )
 , 'page' : '1'
 , 'broadcastid' : Iii1iI . get ( 'broadcastid' )
 , 'contenttype' : Iii1iI . get ( 'contenttype' )
 , 'uiparent' : Iii1iI . get ( 'uiparent' )
 , 'uirank' : Iii1iI . get ( 'uirank' )
 , 'uitype' : Iii1iI . get ( 'uitype' )
 , 'orderby' : OOOO0oo0
 , 'ordernm' : iiI1IIIi
 }
   if 31 - 31: I1Ii111
   if Ooo0oOooo0 == 'moviegenre' or Ooo0oOooo0 == 'moviegenre_svod' or Ooo0oOooo0 == 'moviegenre_ppv' or Iii1iI . get ( 'subgenre' ) != '-' :
    iIIi1i1 [ 'mode' ] = 'GENRE_LIST'
    if 88 - 88: OoO0O00 - ooOoO0o + OOooOOo * I1IiiI % iIii1I11I1II1 + Oo0Ooo
   else :
    if 76 - 76: I1IiiI * iII111i % I1Ii111
    None
    if 57 - 57: iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * OoooooooOO % II111iiii
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 68 - 68: OoooooooOO * I11i % OoOoOO00 - IiII
  if len ( ooO000OO0O00O ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 34 - 34: I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / I1Ii111 / I1ii11iIi11i
  if 78 - 78: Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
  if 10 - 10: iII111i + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / I1ii11iIi11i
  if 42 - 42: I1IiiI
 def dp_Genre_List ( self , args ) :
  if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  i1 = self . get_settings_addinfo ( )
  if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
  Ooo0oOooo0 = args . get ( 'uicode' )
  O00o0 = int ( args . get ( 'page' ) )
  if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
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
   if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
  ooO000OO0O00O , iIIII = self . WavveObj . GetGenreList ( Ooo0oOooo0 , iIIi1i1 , O00o0 , addinfoyn = i1 )
  if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
  if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
  if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
  for Iii1iI in ooO000OO0O00O :
   i11I1iIiII = Iii1iI . get ( 'title' )
   ooooo0O0000oo = Iii1iI . get ( 'thumbnail' )
   if 79 - 79: O0 * i11iIiiIii - IiII / IiII
   II11I1 = Iii1iI . get ( 'info' )
   if Ooo0oOooo0 == 'moviegenre_svod' and i1 == True :
    i11I1iIiII = '%s (%s)' % ( i11I1iIiII , str ( II11I1 . get ( 'year' ) ) )
   else :
    II11I1 [ 'plot' ] = i11I1iIiII
    if 48 - 48: O0
   if Ooo0oOooo0 == 'vodgenre' :
    Oo0o0O00 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : Iii1iI . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11I1iIiII
    , 'subtitle' : ''
    , 'thumbnail' : ooooo0O0000oo
    , 'viewage' : Iii1iI . get ( 'viewage' )
 }
    OOooOO000 = True
    if 40 - 40: OoooooooOO
   else :
    Oo0o0O00 = { 'mode' : 'MOVIE'
 , 'contentid' : Iii1iI . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11I1iIiII
    , 'subtitle' : ''
    , 'thumbnail' : ooooo0O0000oo
    , 'viewage' : Iii1iI . get ( 'viewage' )
 }
    if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
    OOooOO000 = False
    if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
   if Oo0o0O00 . get ( 'viewage' ) == '21' : i11I1iIiII += ' (%s)' % ( Oo0o0O00 . get ( 'viewage' ) )
   if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
   self . add_dir ( i11I1iIiII , sublabel = '' , img = ooooo0O0000oo , infoLabels = II11I1 , isFolder = OOooOO000 , params = Oo0o0O00 )
   if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
  if iIIII :
   if 19 - 19: OoO0O00 - Oo0Ooo . O0
   iIIi1i1 [ 'mode' ] = 'GENRE_LIST'
   iIIi1i1 [ 'uicode' ] = Ooo0oOooo0
   iIIi1i1 [ 'page' ] = str ( O00o0 + 1 )
   i11I1iIiII = '[B]%s >>[/B]' % '다음 페이지'
   O0OoOO0o = str ( O00o0 + 1 )
   self . add_dir ( i11I1iIiII , sublabel = O0OoOO0o , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 60 - 60: II111iiii + Oo0Ooo
  if len ( ooO000OO0O00O ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 9 - 9: ooOoO0o * OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoO0O00
  if 49 - 49: II111iiii
  if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
  if 81 - 81: iII111i + IiII
 def dp_Deeplink_List ( self , args ) :
  if 98 - 98: I1IiiI
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  i1 = self . get_settings_addinfo ( )
  if 95 - 95: ooOoO0o / ooOoO0o
  Ooo0oOooo0 = args . get ( 'uicode' )
  IIiI1Ii = args . get ( 'came' )
  O00o0 = int ( args . get ( 'page' ) )
  if 57 - 57: OOooOOo - ooOoO0o - I11i + OoO0O00
  if 30 - 30: Ii1I % OoOoOO00 + i1IIi - I11i - Ii1I
  if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
  IIIi11I11 , iIIII = self . WavveObj . GetDeeplinkList ( Ooo0oOooo0 , IIiI1Ii , O00o0 , addinfoyn = i1 )
  if 44 - 44: II111iiii
  for OOOO0OOO in IIIi11I11 :
   i11I1iIiII = OOOO0OOO . get ( 'title' )
   O0OoOO0o = OOOO0OOO . get ( 'subtitle' )
   ooooo0O0000oo = OOOO0OOO . get ( 'thumbnail' )
   i1i1ii = OOOO0OOO . get ( 'uicode' )
   iII1ii1 = OOOO0OOO . get ( 'channelepg' )
   if 12 - 12: OOooOOo - ooOoO0o . OoooooooOO / I1ii11iIi11i . i1IIi * OoO0O00
   iIIi1i1 = { 'uicode' : i1i1ii
   , 'came' : IIiI1Ii
 , 'contentid' : OOOO0OOO . get ( 'contentid' )
 , 'contentidType' : OOOO0OOO . get ( 'contentidType' )
 , 'page' : '1'
 , 'title' : i11I1iIiII
   , 'subtitle' : O0OoOO0o
   , 'thumbnail' : ooooo0O0000oo
   , 'viewage' : OOOO0OOO . get ( 'viewage' )
 }
   if 19 - 19: i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
   if i1i1ii == 'channel' :
    iIIi1i1 [ 'mode' ] = 'LIVE'
   elif i1i1ii == 'movie' :
    iIIi1i1 [ 'mode' ] = 'MOVIE'
   else :
    iIIi1i1 [ 'mode' ] = 'DEEP_LIST'
    if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
    if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
   II11I1 = OOOO0OOO . get ( 'info' )
   if iII1ii1 :
    II11I1 [ 'plot' ] = '%s\n\n%s' % ( i11I1iIiII , iII1ii1 )
   elif i1i1ii == 'movie' and i1 == True :
    i11I1iIiII = '%s (%s)' % ( i11I1iIiII , str ( II11I1 . get ( 'year' ) ) )
   else :
    II11I1 [ 'plot' ] = '%s\n\n%s' % ( i11I1iIiII , O0OoOO0o )
    if 71 - 71: O0 - iIii1I11I1II1
   if OOOO0OOO . get ( 'viewage' ) == '21' : O0OoOO0o += ' (%s)' % ( OOOO0OOO . get ( 'viewage' ) )
   if 12 - 12: OOooOOo / o0oOOo0O0Ooo
   if i1i1ii in [ 'channel' , 'movie' ] :
    OOooOO000 = False
   elif iIIi1i1 [ 'contentidType' ] == 'direct' :
    OOooOO000 = False
    iIIi1i1 [ 'mode' ] = 'VOD'
   else :
    OOooOO000 = True
    if 42 - 42: Oo0Ooo
    if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
   self . add_dir ( i11I1iIiII , sublabel = O0OoOO0o , img = ooooo0O0000oo , infoLabels = II11I1 , isFolder = OOooOO000 , params = iIIi1i1 )
   if 46 - 46: Oo0Ooo
  if iIIII :
   if 1 - 1: iII111i
   iIIi1i1 [ 'mode' ] = 'GN_LIST'
   iIIi1i1 [ 'uicode' ] = Ooo0oOooo0
   iIIi1i1 [ 'page' ] = str ( O00o0 + 1 )
   i11I1iIiII = '[B]%s >>[/B]' % '다음 페이지'
   O0OoOO0o = str ( O00o0 + 1 )
   self . add_dir ( i11I1iIiII , sublabel = O0OoOO0o , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 97 - 97: OOooOOo + iII111i + O0 + i11iIiiIii
  if len ( IIIi11I11 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
  if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
  if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
  if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
 def dp_Episodelink_List ( self , args ) :
  if 17 - 17: i1IIi
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 21 - 21: Oo0Ooo
  I1ii1 = args . get ( 'contentid' )
  O00 = args . get ( 'contentidType' )
  OOOoOo = args . get ( 'uicode' )
  if 92 - 92: iIii1I11I1II1 * i1IIi * iII111i % OOooOOo % I1ii11iIi11i + II111iiii
  O00o0 = int ( args . get ( 'page' ) )
  if 42 - 42: IiII - o0oOOo0O0Ooo . II111iiii
  ooo000OOOoOoO , iIIII = self . WavveObj . GetEpisodeList ( I1ii1 , OOOoOo , O00 , O00o0 , orderby = self . get_winEpisodeOrderby ( ) )
  if 22 - 22: I1IiiI % I1ii11iIi11i
  for o0oo0O in ooo000OOOoOoO :
   i11I1iIiII = o0oo0O . get ( 'title' )
   O0OoOO0o = o0oo0O . get ( 'subtitle' )
   ooooo0O0000oo = o0oo0O . get ( 'thumbnail' )
   iIIi1i1 = { 'mode' : 'VOD'
 , 'uicode' : o0oo0O . get ( 'uicode' )
   , 'contentid' : o0oo0O . get ( 'contentid' )
 , 'programid' : o0oo0O . get ( 'programid' )
 , 'title' : i11I1iIiII
   , 'subtitle' : O0OoOO0o
   , 'thumbnail' : ooooo0O0000oo
   , 'viewage' : o0oo0O . get ( 'viewage' )
 }
   if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - II111iiii * OOooOOo
   if o0oo0O . get ( 'viewage' ) == '21' : O0OoOO0o += ' (%s)' % ( o0oo0O . get ( 'viewage' ) )
   if 26 - 26: OoooooooOO * I1IiiI + OOooOOo
   IiIii1i111 = o0oo0O . get ( 'info' )
   IiIii1i111 [ 'plot' ] = o0oo0O . get ( 'synopsis' )
   if 43 - 43: O0
   if 39 - 39: I1IiiI . iIii1I11I1II1 * Ii1I % ooOoO0o . iIii1I11I1II1
   if 54 - 54: OOooOOo
   if 45 - 45: OoooooooOO - OOooOOo + O0 * Ii1I . I1ii11iIi11i
   self . add_dir ( i11I1iIiII , sublabel = O0OoOO0o , img = ooooo0O0000oo , infoLabels = IiIii1i111 , isFolder = False , params = iIIi1i1 )
   if 39 - 39: iIii1I11I1II1 / O0 / oO0o - Ii1I - iII111i % OOooOOo
  if O00o0 == 1 :
   II11I1 = { 'plot' : '정렬순서를 변경합니다.' }
   iIIi1i1 = { }
   iIIi1i1 [ 'mode' ] = 'ORDER_BY'
   if self . get_winEpisodeOrderby ( ) == 'desc' :
    i11I1iIiII = '정렬순서변경 : 최신화부터 -> 1회부터'
    iIIi1i1 [ 'orderby' ] = 'asc'
   else :
    i11I1iIiII = '정렬순서변경 : 1회부터 -> 최신화부터'
    iIIi1i1 [ 'orderby' ] = 'desc'
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = II11I1 , isFolder = False , params = iIIi1i1 )
   if 31 - 31: I11i - O0 / ooOoO0o * OoOoOO00
  if iIIII :
   if 12 - 12: o0oOOo0O0Ooo - ooOoO0o * I1Ii111
   iIIi1i1 [ 'mode' ] = 'DEEP_LIST'
   iIIi1i1 [ 'uicode' ] = OOOoOo
   iIIi1i1 [ 'contentid' ] = I1ii1
   iIIi1i1 [ 'contentidType' ] = O00
   iIIi1i1 [ 'page' ] = str ( O00o0 + 1 )
   i11I1iIiII = '[B]%s >>[/B]' % '다음 페이지'
   O0OoOO0o = str ( O00o0 + 1 )
   self . add_dir ( i11I1iIiII , sublabel = O0OoOO0o , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 14 - 14: Oo0Ooo - Ii1I % Ii1I * O0 . i11iIiiIii / O0
   if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
  if len ( ooo000OOOoOoO ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = True )
  if 28 - 28: i1IIi - iII111i
  if 54 - 54: iII111i - O0 % OOooOOo
  if 73 - 73: O0 . OoOoOO00 + I1IiiI - I11i % I11i . I11i
 def play_VIDEO ( self , args ) :
  if 17 - 17: Ii1I - OoooooooOO % Ii1I . IiII / i11iIiiIii % iII111i
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 28 - 28: I11i
  I1ii1 = args . get ( 'contentid' )
  OOOoOo = args . get ( 'uicode' )
  oOOOOoo = self . get_selQuality ( )
  if 58 - 58: o0oOOo0O0Ooo / IiII . OoOoOO00 / OoooooooOO + I1Ii111
  self . addon_log ( I1ii1 + ' - ' + OOOoOo , False )
  O0OoO0ooOO0o , OoOo0oOooOoOO , oo00ooOoO00 , o00oOoOo0 = self . WavveObj . GetStreamingURL ( I1ii1 , OOOoOo , oOOOOoo )
  if 72 - 72: I1Ii111
  if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iII111i
  I1iii11 = '%s|Cookie=%s' % ( O0OoO0ooOO0o , OoOo0oOooOoOO )
  self . addon_log ( I1iii11 , False )
  if 74 - 74: O0 / i1IIi
  if O0OoO0ooOO0o == '' :
   self . addon_noti ( __language__ ( 30303 ) . encode ( 'utf8' ) )
   return
   if 78 - 78: OoooooooOO . OoO0O00 + ooOoO0o - i1IIi
  ii1 = xbmcgui . ListItem ( path = I1iii11 )
  if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
  if oo00ooOoO00 :
   if 100 - 100: OoO0O00
   if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
   IIi1ii1Ii = oo00ooOoO00 [ 'customdata' ]
   OoOoO = oo00ooOoO00 [ 'drmhost' ]
   if 83 - 83: OOooOOo . i1IIi / OoooooooOO
   IIiIiiii = 'mpd'
   O0000OOO0 = 'com.widevine.alpha'
   if 51 - 51: I1IiiI / IiII / Ii1I
   I111iIi1 = inputstreamhelper . Helper ( IIiIiiii , drm = O0000OOO0 )
   if 92 - 92: ooOoO0o
   if I111iIi1 . check_inputstream ( ) :
    if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
    if OOOoOo == 'movie' :
     Oo00OoOo = 'https://www.wavve.com/player/movie?movieid=%s' % I1ii1
    else :
     Oo00OoOo = 'https://www.wavve.com/player/vod?programid=%s&page=1' % I1ii1
     if 24 - 24: i11iIiiIii - I1Ii111
    i11iiI1111 = { 'content-type' : 'application/octet-stream'
 , 'origin' : 'https://www.wavve.com'
 , 'pallycon-customdata' : IIi1ii1Ii
 , 'referer' : Oo00OoOo
 , 'sec-fetch-dest' : 'empty'
    , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'

    , 'user-agent' : OOo000
 }
    oOoooo000Oo00 = OoOoO + '|' + urllib . urlencode ( i11iiI1111 ) + '|R{SSM}|'
    if 93 - 93: I1ii11iIi11i / I1IiiI / iIii1I11I1II1 % I1Ii111 % I1Ii111
    ii1 . setProperty ( 'inputstreamaddon' , I111iIi1 . inputstream_addon )
    ii1 . setProperty ( 'inputstream.adaptive.manifest_type' , IIiIiiii )
    ii1 . setProperty ( 'inputstream.adaptive.license_type' , O0000OOO0 )
    if 40 - 40: i11iIiiIii * I1Ii111 - i1IIi * I1Ii111 - I11i . i1IIi
    ii1 . setProperty ( 'inputstream.adaptive.license_key' , oOoooo000Oo00 )
    ii1 . setProperty ( 'inputstream.adaptive.stream_headers' , 'Cookie=%s' % OoOo0oOooOoOO )
    if 99 - 99: O0 * I11i
  xbmcplugin . setResolvedUrl ( self . _addon_handle , True , ii1 )
  if 64 - 64: II111iiii + O0 / iIii1I11I1II1 / Oo0Ooo . ooOoO0o % IiII
  if o00oOoOo0 :
   self . addon_noti ( o00oOoOo0 . encode ( 'utf-8' ) )
  else :
   if '/preview.' in urlparse . urlsplit ( O0OoO0ooOO0o ) . path : self . addon_noti ( __language__ ( 30401 ) . encode ( 'utf8' ) )
   if 50 - 50: iIii1I11I1II1 - IiII + OOooOOo
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
   if 69 - 69: O0
   if 85 - 85: ooOoO0o / O0
   if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
   if 62 - 62: I1Ii111 . IiII . OoooooooOO
 def dp_Watch_List ( self , args ) :
  oOOOoo00 = args . get ( 'genre' )
  oOooOOo00Oo0O = self . get_settings_direct_replay ( )
  if 11 - 11: OOooOOo / I11i
  if oOOOoo00 == '-' :
   i11I1iIiII = 'VOD 시청내역'
   iIIi1i1 = { 'mode' : 'WATCH'
 , 'genre' : 'vod'
 }
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 73 - 73: i1IIi / i11iIiiIii
   i11I1iIiII = '영화 시청내역'
   iIIi1i1 [ 'genre' ] = 'movie'
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
   xbmcplugin . endOfDirectory ( self . _addon_handle )
   if 85 - 85: OoOoOO00 + OOooOOo
  else :
   I1II = self . Load_Watched_List ( oOOOoo00 )
   if 27 - 27: II111iiii / Ii1I . OOooOOo
   for i1II11II in I1II :
    oOo00O000Oo0 = dict ( urlparse . parse_qsl ( i1II11II ) )
    if 18 - 18: iII111i * OoO0O00 . OoO0O00 * oO0o * II111iiii * I1Ii111
    i11I1iIiII = oOo00O000Oo0 . get ( 'title' ) . strip ( )
    O0OoOO0o = oOo00O000Oo0 . get ( 'subtitle' ) . strip ( )
    if O0OoOO0o == 'None' : O0OoOO0o = ''
    ooooo0O0000oo = oOo00O000Oo0 . get ( 'img' )
    oOooO0 = oOo00O000Oo0 . get ( 'videoid' )
    if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111
    if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
    II11I1 = { }
    if oOOOoo00 == 'movie' and self . get_settings_addinfo ( ) == True :
     ooO0o = self . WavveObj . GetMovieInfoList ( [ oOo00O000Oo0 . get ( 'code' ) ] )
     II11I1 = ooO0o . get ( oOo00O000Oo0 . get ( 'code' ) )
    else :
     II11I1 [ 'plot' ] = '%s\n%s' % ( i11I1iIiII , O0OoOO0o )
     if 89 - 89: I11i / I1Ii111
    if oOOOoo00 == 'vod' :
     if oOooOOo00Oo0O == False or oOooO0 == None :
      iIIi1i1 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : oOo00O000Oo0 . get ( 'code' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
      OOooOO000 = True
     else :
      iIIi1i1 = { 'mode' : 'VOD'
 , 'contentid' : oOooO0
 , 'contentidType' : 'contentid'
 , 'programid' : oOo00O000Oo0 . get ( 'code' )
 , 'uicode' : 'vod'
 , 'title' : i11I1iIiII
 , 'subtitle' : O0OoOO0o
 , 'thumbnail' : ooooo0O0000oo
 }
      OOooOO000 = False
    else :
     iIIi1i1 = { 'mode' : 'MOVIE'
 , 'contentid' : oOo00O000Oo0 . get ( 'code' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'title' : i11I1iIiII
 , 'thumbnail' : ooooo0O0000oo
 }
     OOooOO000 = False
     if 90 - 90: iII111i
    self . add_dir ( i11I1iIiII , sublabel = O0OoOO0o , img = ooooo0O0000oo , infoLabels = II11I1 , isFolder = OOooOO000 , params = iIIi1i1 )
    if 31 - 31: OOooOOo + O0
   II11I1 = { 'plot' : '시청목록을 삭제합니다.' }
   i11I1iIiII = '*** 시청목록 삭제 ***'
   iIIi1i1 = { 'mode' : 'MYVIEW_REMOVE'
 , 'genre' : oOOOoo00
 }
   if 87 - 87: ooOoO0o
   self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = II11I1 , isFolder = False , params = iIIi1i1 )
   if 45 - 45: OoO0O00 / OoooooooOO - iII111i / Ii1I % IiII
   xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
   if 83 - 83: I1IiiI . iIii1I11I1II1 - IiII * i11iIiiIii
   if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
   if 13 - 13: Oo0Ooo
   if 60 - 60: I1ii11iIi11i * I1IiiI
   if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
 def dp_Search_Group ( self , args ) :
  i11I1iIiII = 'VOD 검색'
  iIIi1i1 = { 'mode' : 'SEARCH_LIST'
 , 'genre' : 'vod'
 , 'page' : '1'
 }
  self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if 41 - 41: Ii1I
  i11I1iIiII = '영화 검색'
  iIIi1i1 [ 'genre' ] = 'movie'
  self . add_dir ( i11I1iIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if 77 - 77: I1Ii111
  xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 65 - 65: II111iiii . I1IiiI % oO0o * OoO0O00
  if 38 - 38: OoOoOO00 / iII111i % Oo0Ooo
  if 11 - 11: iII111i - oO0o + II111iiii - iIii1I11I1II1
  if 7 - 7: IiII - I11i / II111iiii * Ii1I . iII111i * iII111i
 def dp_Search_List ( self , args ) :
  if 61 - 61: I11i % ooOoO0o - OoO0O00 / Oo0Ooo
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  i1 = self . get_settings_addinfo ( )
  if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
  OOOoOo = args . get ( 'genre' )
  O00o0 = int ( args . get ( 'page' ) )
  if 85 - 85: OoooooooOO * iIii1I11I1II1 . iII111i / OoooooooOO % I1IiiI % O0
  if 'search_key' in args :
   I1iii = args . get ( 'search_key' )
  else :
   I1iii = self . get_keyboard_input ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
   if not I1iii : return
   if 86 - 86: I1ii11iIi11i * O0 * IiII
  Ooo0oo , iIIII = self . WavveObj . GetSearchList ( I1iii , OOOoOo , O00o0 , exclusion21 = self . get_settings_exclusion21 ( ) , addinfoyn = i1 )
  if 41 - 41: OoOoOO00 * I11i / OoOoOO00 % oO0o
  for Ii in Ooo0oo :
   i11I1iIiII = Ii . get ( 'title' )
   ooooo0O0000oo = Ii . get ( 'thumbnail' )
   if 77 - 77: OoOoOO00 % Ii1I
   II11I1 = Ii . get ( 'info' )
   if OOOoOo == 'movie' and i1 == True :
    i11I1iIiII = '%s (%s)' % ( i11I1iIiII , str ( II11I1 . get ( 'year' ) ) )
   else :
    II11I1 [ 'plot' ] = i11I1iIiII
    if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
   if OOOoOo == 'vod' :
    iIIi1i1 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : Ii . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11I1iIiII
    , 'subtitle' : ''
    , 'thumbnail' : ooooo0O0000oo
    , 'viewage' : Ii . get ( 'viewage' )
 }
    OOooOO000 = True
    if 2 - 2: OoooooooOO % OOooOOo
   else :
    iIIi1i1 = { 'mode' : 'MOVIE'
 , 'contentid' : Ii . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11I1iIiII
    , 'subtitle' : ''
    , 'thumbnail' : ooooo0O0000oo
    , 'viewage' : Ii . get ( 'viewage' )
 }
    if 63 - 63: I1IiiI % iIii1I11I1II1
    OOooOO000 = False
    if 39 - 39: iII111i / II111iiii / I1ii11iIi11i % I1IiiI
   if iIIi1i1 . get ( 'viewage' ) == '21' : i11I1iIiII += ' (%s)' % ( iIIi1i1 . get ( 'viewage' ) )
   if 89 - 89: I1Ii111 + OoooooooOO + I1Ii111 * i1IIi + iIii1I11I1II1 % I11i
   self . add_dir ( i11I1iIiII , sublabel = '' , img = ooooo0O0000oo , infoLabels = II11I1 , isFolder = OOooOO000 , params = iIIi1i1 )
   if 59 - 59: OOooOOo + i11iIiiIii
  if iIIII :
   if 88 - 88: i11iIiiIii - ooOoO0o
   iIIi1i1 [ 'mode' ] = 'SEARCH_LIST'
   iIIi1i1 [ 'genre' ] = OOOoOo
   iIIi1i1 [ 'page' ] = str ( O00o0 + 1 )
   iIIi1i1 [ 'search_key' ] = I1iii
   i11I1iIiII = '[B]%s >>[/B]' % '다음 페이지'
   O0OoOO0o = str ( O00o0 + 1 )
   self . add_dir ( i11I1iIiII , sublabel = O0OoOO0o , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
  if len ( Ooo0oo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
  if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - I11i
  if 30 - 30: OoOoOO00
  if 21 - 21: i11iIiiIii / I1Ii111 % OOooOOo * O0 . I11i - iIii1I11I1II1
  if 26 - 26: II111iiii * OoOoOO00
 def Load_Watched_List ( self , genre ) :
  try :
   ii = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   with open ( ii , 'r' ) as oo0o0OoOOO :
    ooO0oO00O0o = oo0o0OoOOO . readlines ( )
  except :
   ooO0oO00O0o = [ ]
   if 70 - 70: I1Ii111
  return ooO0oO00O0o
  if 16 - 16: iII111i - OoooooooOO % Oo0Ooo
  if 36 - 36: OOooOOo
  if 84 - 84: I1Ii111 . OoO0O00 . II111iiii . I11i / Ii1I % I1ii11iIi11i
  if 57 - 57: I1IiiI % I11i - OOooOOo . I1IiiI / Oo0Ooo % iII111i
 def Save_Watched_List ( self , genre , in_params ) :
  try :
   ii = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   OO = self . Load_Watched_List ( genre )
   if 16 - 16: IiII * OoOoOO00 . ooOoO0o / i1IIi . OoO0O00 - i1IIi
   with open ( ii , 'w' ) as oo0o0OoOOO :
    I1IiIIi = urllib . urlencode ( in_params )
    I1IiIIi = I1IiIIi . encode ( 'utf-8' ) + '\n'
    oo0o0OoOOO . write ( I1IiIIi )
    if 42 - 42: O0 . oO0o - o0oOOo0O0Ooo / i1IIi
    OooOOO = 0
    for Ii1iI11iI1 in OO :
     i11 = dict ( urlparse . parse_qsl ( Ii1iI11iI1 ) )
     if 11 - 11: I1Ii111 / OoOoOO00 + I11i % iIii1I11I1II1
     II1II1iIIi11 = in_params . get ( 'code' )
     IiI1iII1II111 = i11 . get ( 'code' )
     if genre == 'vod' and self . get_settings_direct_replay ( ) == True :
      II1II1iIIi11 = in_params . get ( 'videoid' )
      IiI1iII1II111 = i11 . get ( 'videoid' ) if IiI1iII1II111 != None else '-'
      if 28 - 28: OoOoOO00 * OoO0O00 . I11i % I11i / I11i * I1Ii111
     if II1II1iIIi11 != IiI1iII1II111 :
      oo0o0OoOOO . write ( Ii1iI11iI1 )
      OooOOO += 1
      if OooOOO >= 50 : break
  except :
   None
   if 64 - 64: II111iiii - I1IiiI
   if 68 - 68: ooOoO0o - OOooOOo - iIii1I11I1II1 / OoOoOO00 + OOooOOo - OoO0O00
   if 75 - 75: iII111i / o0oOOo0O0Ooo % iIii1I11I1II1 . OoooooooOO % OoooooooOO % II111iiii
   if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
 def Delete_Watched_List ( self , genre ) :
  try :
   ii = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   with open ( ii , 'w' ) as oo0o0OoOOO :
    oo0o0OoOOO . write ( '' )
  except :
   None
   if 24 - 24: II111iiii % I1Ii111 - ooOoO0o + I1IiiI * I1ii11iIi11i
   if 2 - 2: Ii1I - IiII
   if 83 - 83: oO0o % o0oOOo0O0Ooo % Ii1I - II111iiii * OOooOOo / OoooooooOO
   if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
 def dp_WatchList_Delete ( self , args ) :
  oOOOoo00 = args . get ( 'genre' )
  if 71 - 71: OoooooooOO
  OoooooOoo = xbmcgui . Dialog ( )
  ooOOOoOooOoO = OoooooOoo . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if ooOOOoOooOoO == False : sys . exit ( )
  if 33 - 33: I1Ii111
  self . Delete_Watched_List ( oOOOoo00 )
  if 62 - 62: I1ii11iIi11i + Ii1I + i1IIi / OoooooooOO
  xbmc . executebuiltin ( "Container.Refresh" )
  if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
  if 22 - 22: ooOoO0o - ooOoO0o % OOooOOo . I1Ii111 + oO0o
  if 63 - 63: I1IiiI % I1Ii111 * o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % iII111i
  if 45 - 45: IiII
 def logout ( self ) :
  OoooooOoo = xbmcgui . Dialog ( )
  ooOOOoOooOoO = OoooooOoo . yesno ( __language__ ( 30910 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if ooOOOoOooOoO == False : sys . exit ( )
  if 20 - 20: OoooooooOO * o0oOOo0O0Ooo * O0 . OOooOOo
  self . wininfo_clear ( )
  if 78 - 78: iIii1I11I1II1 + I11i - Ii1I * I1Ii111 - OoooooooOO % OoOoOO00
  if 34 - 34: O0
  if os . path . isfile ( O0I11i1i11i1I ) : os . remove ( O0I11i1i11i1I )
  if 80 - 80: i1IIi - Oo0Ooo / OoO0O00 - i11iIiiIii
  self . addon_noti ( __language__ ( 30909 ) . encode ( 'utf-8' ) )
  if 68 - 68: oO0o - I1ii11iIi11i % O0 % I1Ii111
  if 11 - 11: O0 / OoO0O00 % OOooOOo + o0oOOo0O0Ooo + iIii1I11I1II1
  if 40 - 40: ooOoO0o - OOooOOo . Ii1I * Oo0Ooo % I1Ii111
  if 56 - 56: i11iIiiIii . o0oOOo0O0Ooo - I1IiiI * I11i
 def wininfo_clear ( self ) :
  if 91 - 91: oO0o + OoooooooOO - i1IIi
  IIi1iIIiI = xbmcgui . Window ( 10000 )
  IIi1iIIiI . setProperty ( 'WAVVE_M_CREDENTIAL' , '' )
  IIi1iIIiI . setProperty ( 'WAVVE_M_LOGINTIME' , '' )
  if 84 - 84: Ii1I / IiII
  if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / OOooOOo
  if 11 - 11: I1IiiI * oO0o + I1ii11iIi11i / I1ii11iIi11i
  if 37 - 37: i11iIiiIii + i1IIi
 def cookiefile_save ( self ) :
  I1i11II = datetime . datetime . now ( )
  II11 = I1i11II + datetime . timedelta ( days = int ( __addon__ . getSetting ( 'cache_ttl' ) ) )
  if 15 - 15: IiII / O0 . o0oOOo0O0Ooo . i11iIiiIii
  IIi1iIIiI = xbmcgui . Window ( 10000 )
  o0OO0O0Oo = { 'wavve_token' : IIi1iIIiI . getProperty ( 'WAVVE_M_CREDENTIAL' )
 , 'wavve_id' : base64 . standard_b64encode ( __addon__ . getSetting ( 'id' ) . encode ( ) ) . decode ( 'utf-8' )
 , 'wavve_pw' : base64 . standard_b64encode ( __addon__ . getSetting ( 'pw' ) . encode ( ) ) . decode ( 'utf-8' )
 , 'wavve_profile' : __addon__ . getSetting ( 'selected_profile' )
 , 'wavve_limitdate' : II11 . strftime ( '%Y-%m-%d' )
 }
  if 78 - 78: OoOoOO00 / Oo0Ooo - OOooOOo - iII111i * oO0o
  try :
   with open ( O0I11i1i11i1I , 'w' ) as oo0o0OoOOO :
    json . dump ( o0OO0O0Oo , oo0o0OoOOO )
  except Exception as Ii1I11I :
   print ( Ii1I11I )
   if 36 - 36: O0 + Oo0Ooo
   if 5 - 5: Oo0Ooo * OoOoOO00
   if 46 - 46: ooOoO0o
   if 33 - 33: iII111i - II111iiii * OoooooooOO - Oo0Ooo - OOooOOo
 def cookiefile_check ( self ) :
  if 84 - 84: I1Ii111 + Oo0Ooo - OoOoOO00 * OoOoOO00
  if 61 - 61: OoooooooOO . oO0o . OoooooooOO / Oo0Ooo
  o0OO0O0Oo = { }
  try :
   with open ( O0I11i1i11i1I , 'r' ) as oo0o0OoOOO :
    o0OO0O0Oo = json . load ( oo0o0OoOOO )
  except Exception as Ii1I11I :
   self . wininfo_clear ( )
   return False
   if 72 - 72: i1IIi
   if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i . OoooooooOO
   if 63 - 63: I1ii11iIi11i
  oOOo0oOo0 = __addon__ . getSetting ( 'id' )
  II = __addon__ . getSetting ( 'pw' )
  i1II = __addon__ . getSetting ( 'selected_profile' )
  o0OO0O0Oo [ 'wavve_id' ] = base64 . standard_b64decode ( o0OO0O0Oo [ 'wavve_id' ] ) . decode ( 'utf-8' )
  o0OO0O0Oo [ 'wavve_pw' ] = base64 . standard_b64decode ( o0OO0O0Oo [ 'wavve_pw' ] ) . decode ( 'utf-8' )
  if oOOo0oOo0 != o0OO0O0Oo [ 'wavve_id' ] or II != o0OO0O0Oo [ 'wavve_pw' ] or i1II != o0OO0O0Oo [ 'wavve_profile' ] :
   self . wininfo_clear ( )
   return False
   if 2 - 2: II111iiii - OoO0O00 . IiII * iII111i / oO0o
   if 80 - 80: OOooOOo / I11i / OoOoOO00 + i1IIi - Oo0Ooo
  i1Iii1i1I = datetime . datetime . now ( ) . date ( )
  iIIiiIIi1IiI = o0OO0O0Oo [ 'wavve_limitdate' ]
  try :
   OOoO00 = datetime . datetime . strptime ( iIIiiIIi1IiI , '%Y-%m-%d' ) . date ( )
  except TypeError :
   OOoO00 = datetime . datetime ( * ( time . strptime ( iIIiiIIi1IiI , '%Y-%m-%d' ) [ 0 : 6 ] ) ) . date ( )
   if 14 - 14: IiII % oO0o % Oo0Ooo - i11iIiiIii
  if OOoO00 < i1Iii1i1I :
   self . wininfo_clear ( )
   return False
   if 53 - 53: Ii1I % Oo0Ooo
   if 59 - 59: OOooOOo % iIii1I11I1II1 . i1IIi + II111iiii * IiII
  IIi1iIIiI = xbmcgui . Window ( 10000 )
  IIi1iIIiI . setProperty ( 'WAVVE_M_CREDENTIAL' , o0OO0O0Oo [ 'wavve_token' ] )
  IIi1iIIiI . setProperty ( 'WAVVE_M_LOGINTIME' , iIIiiIIi1IiI )
  if 41 - 41: Ii1I % I1ii11iIi11i
  return True
  if 12 - 12: OOooOOo
  if 69 - 69: OoooooooOO + OOooOOo
  if 26 - 26: Oo0Ooo + OOooOOo / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
  if 31 - 31: I11i % OOooOOo * I11i
 def wavve_main ( self ) :
  if 45 - 45: i1IIi . I1IiiI + OOooOOo - OoooooooOO % ooOoO0o
  IIooO = self . main_params . get ( 'mode' , None )
  if 1 - 1: iIii1I11I1II1
  self . login_main ( )
  if IIooO is None :
   if 93 - 93: i1IIi . i11iIiiIii . Oo0Ooo
   self . dp_Main_List ( )
   if 99 - 99: I11i - I1Ii111 - oO0o % OoO0O00
   if 21 - 21: II111iiii % I1ii11iIi11i . i1IIi - OoooooooOO
   if 4 - 4: OoooooooOO . ooOoO0o
   if 78 - 78: I1ii11iIi11i + I11i - O0
   if 10 - 10: I1Ii111 % I1IiiI
   if 97 - 97: OoooooooOO - I1Ii111
   if 58 - 58: iIii1I11I1II1 + O0
   if 30 - 30: ooOoO0o % iII111i * OOooOOo - I1ii11iIi11i * Ii1I % ooOoO0o
   if 46 - 46: i11iIiiIii - O0 . oO0o
  elif IIooO == 'GNB_LIST' :
   self . dp_Gnb_List ( self . main_params )
   if 100 - 100: I1IiiI / o0oOOo0O0Ooo * iII111i . O0 / OOooOOo
  elif IIooO == 'GN_LIST' :
   self . dp_Deeplink_List ( self . main_params )
   if 83 - 83: I1Ii111
  elif IIooO == 'DEEP_LIST' :
   OOOoOo = self . main_params . get ( 'uicode' , None )
   if 48 - 48: II111iiii * OOooOOo * I1Ii111
   if OOOoOo in [ 'quick' , 'vod' , 'program' , 'x' ] :
    self . dp_Episodelink_List ( self . main_params )
    if 50 - 50: IiII % i1IIi
   else : None
   if 21 - 21: OoooooooOO - iIii1I11I1II1
  elif IIooO in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
   self . play_VIDEO ( self . main_params )
   if 93 - 93: oO0o - o0oOOo0O0Ooo % OoOoOO00 . OoOoOO00 - ooOoO0o
   time . sleep ( 0.1 )
   if 90 - 90: ooOoO0o + II111iiii * I1ii11iIi11i / Ii1I . o0oOOo0O0Ooo + o0oOOo0O0Ooo
  elif IIooO == 'GN_MYVIEW' :
   self . dp_Myview_Group ( self . main_params )
   if 40 - 40: ooOoO0o / OoOoOO00 % i11iIiiIii % I1ii11iIi11i / I1IiiI
  elif IIooO == 'MYVIEW_LIST' :
   self . dp_Myview_List ( self . main_params )
   if 62 - 62: i1IIi - OoOoOO00
  elif IIooO == 'GENRE' :
   self . dp_Genre_Group ( self . main_params )
   if 62 - 62: i1IIi + Oo0Ooo % IiII
  elif IIooO == 'GENRE_LIST' :
   self . dp_Genre_List ( self . main_params )
   if 28 - 28: I1ii11iIi11i . i1IIi
  elif IIooO == 'WATCH' :
   self . dp_Watch_List ( self . main_params )
   if 10 - 10: OoO0O00 / Oo0Ooo
  elif IIooO == 'MYVIEW_REMOVE' :
   self . dp_WatchList_Delete ( self . main_params )
   if 15 - 15: iII111i . OoOoOO00 / iII111i * I11i - I1IiiI % I1ii11iIi11i
  elif IIooO == 'SEARCH' :
   self . dp_Search_Group ( self . main_params )
   if 57 - 57: O0 % OoOoOO00 % oO0o
  elif IIooO == 'SEARCH_LIST' :
   self . dp_Search_List ( self . main_params )
   if 45 - 45: I1ii11iIi11i + II111iiii * i11iIiiIii
  elif IIooO == 'ORDER_BY' :
   self . dp_setEpOrderby ( self . main_params )
   if 13 - 13: OoooooooOO * oO0o - Ii1I / OOooOOo + I11i + IiII
  elif IIooO == 'LOGOUT' :
   self . logout ( )
   if 39 - 39: iIii1I11I1II1 - OoooooooOO
   if 81 - 81: I1ii11iIi11i - O0 * OoooooooOO
   if 23 - 23: II111iiii / oO0o
   if 28 - 28: Oo0Ooo * ooOoO0o - OoO0O00
   if 19 - 19: I11i
   if 67 - 67: O0 % iIii1I11I1II1 / IiII . i11iIiiIii - Ii1I + O0
  else :
   None
   if 27 - 27: OOooOOo
   if 89 - 89: II111iiii / oO0o
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
