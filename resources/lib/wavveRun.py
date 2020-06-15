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
  self . WavveObj = iII111ii ( )
  if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
  if 31 - 31: OoO0O00 + II111iiii
  if 13 - 13: OOooOOo * oO0o * I1IiiI
 def addon_noti ( self , sting ) :
  try :
   oOOOO = xbmcgui . Dialog ( )
   if 45 - 45: I1Ii111 + Ii1I
   oOOOO . notification ( __addonname__ , sting )
  except :
   None
   if 17 - 17: o0oOOo0O0Ooo
   if 64 - 64: Ii1I % i1IIi % OoooooooOO
   if 3 - 3: iII111i + O0
 def addon_log ( self , string , isDebug = False ) :
  try :
   I1Ii = string . encode ( 'utf-8' , 'ignore' )
  except :
   I1Ii = 'addonException: addon_log'
  if isDebug : o0oOo0Ooo0O = xbmc . LOGDEBUG
  else : o0oOo0Ooo0O = xbmc . LOGNOTICE
  xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , I1Ii ) , level = o0oOo0Ooo0O )
  if 81 - 81: I1ii11iIi11i * IiII * I11i - iII111i - o0oOOo0O0Ooo
  if 90 - 90: II111iiii + oO0o / o0oOOo0O0Ooo % II111iiii - O0
  if 29 - 29: o0oOOo0O0Ooo / iIii1I11I1II1
  if 24 - 24: O0 % o0oOOo0O0Ooo + i1IIi + I1Ii111 + I1ii11iIi11i
 def get_keyboard_input ( self , title ) :
  OOoO000O0OO = None
  iiI1IiI = xbmc . Keyboard ( )
  iiI1IiI . setHeading ( title )
  xbmc . sleep ( 1000 )
  iiI1IiI . doModal ( )
  if ( iiI1IiI . isConfirmed ( ) ) :
   OOoO000O0OO = iiI1IiI . getText ( )
  return OOoO000O0OO
  if 13 - 13: Oo0Ooo . i11iIiiIii - iIii1I11I1II1 - OoOoOO00
  if 6 - 6: I1IiiI / Oo0Ooo % Ii1I
  if 84 - 84: i11iIiiIii . o0oOOo0O0Ooo
  if 100 - 100: Ii1I - Ii1I - I1Ii111
 def get_settings_login_info ( self ) :
  ii1 = __addon__ . getSetting ( 'id' )
  o0oO0o00oo = __addon__ . getSetting ( 'pw' )
  II1i1Ii11Ii11 = __addon__ . getSetting ( 'selected_profile' )
  return ( ii1 , o0oO0o00oo , II1i1Ii11Ii11 )
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
 def get_settings_direct_replay ( self ) :
  o00oOO0 = int ( __addon__ . getSetting ( 'direct_replay' ) )
  if o00oOO0 == 0 :
   return False
  else :
   return True
   if 95 - 95: OOooOOo / OoooooooOO
   if 18 - 18: i11iIiiIii
   if 46 - 46: i1IIi / I11i % OOooOOo + I1Ii111
 def get_settings_addinfo ( self ) :
  O0OOO00oo = __addon__ . getSetting ( 'add_infoyn' )
  if O0OOO00oo == 'false' :
   return False
  else :
   return True
   if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
   if 4 - 4: II111iiii / ooOoO0o . iII111i
   if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
   if 50 - 50: I1IiiI
 def get_settings_thumbnail_landyn ( self ) :
  Ii1i11IIii1I = int ( __addon__ . getSetting ( 'thumbnail_way' ) )
  if Ii1i11IIii1I == 0 :
   return True
  else :
   return False
   if 52 - 52: o0oOOo0O0Ooo - OoooooooOO + Ii1I + Ii1I - o0oOOo0O0Ooo / I1Ii111
   if 44 - 44: ooOoO0o . i1IIi - I1ii11iIi11i . O0 - ooOoO0o
   if 92 - 92: iII111i . I11i + o0oOOo0O0Ooo
   if 28 - 28: i1IIi * Oo0Ooo - o0oOOo0O0Ooo * IiII * Ii1I / OoO0O00
 def set_winCredential ( self , credential ) :
  OooO0OoOOOO = xbmcgui . Window ( 10000 )
  OooO0OoOOOO . setProperty ( 'WAVVE_M_CREDENTIAL' , credential )
  if 46 - 46: OOooOOo / I1ii11iIi11i
  OooO0OoOOOO . setProperty ( 'WAVVE_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
  if 24 - 24: I11i . iII111i % OOooOOo + ooOoO0o % OoOoOO00
 def get_winCredential ( self ) :
  OooO0OoOOOO = xbmcgui . Window ( 10000 )
  return OooO0OoOOOO . getProperty ( 'WAVVE_M_CREDENTIAL' )
  if 4 - 4: IiII - OoO0O00 * OoOoOO00 - I11i
 def set_winEpisodeOrderby ( self , orderby ) :
  OooO0OoOOOO = xbmcgui . Window ( 10000 )
  OooO0OoOOOO . setProperty ( 'WAVVE_M_ORDERBY' , orderby )
  if 41 - 41: OoOoOO00 . I1IiiI * oO0o % IiII
 def get_winEpisodeOrderby ( self ) :
  OooO0OoOOOO = xbmcgui . Window ( 10000 )
  return OooO0OoOOOO . getProperty ( 'WAVVE_M_ORDERBY' )
  if 86 - 86: I1IiiI + Ii1I % i11iIiiIii * oO0o . ooOoO0o * I11i
  if 44 - 44: oO0o
  if 88 - 88: I1Ii111 % Ii1I . II111iiii
  if 38 - 38: o0oOOo0O0Ooo
 def add_dir ( self , label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
  if 57 - 57: O0 / oO0o * I1Ii111 / OoOoOO00 . II111iiii
  i11iIIIIIi1 = '%s?%s' % ( self . _addon_url , urllib . urlencode ( params ) )
  if 20 - 20: i1IIi + I1ii11iIi11i - ooOoO0o
  if sublabel : IiI11iII1 = '%s < %s >' % ( label , sublabel )
  else : IiI11iII1 = label
  if not img : img = 'DefaultFolder.png'
  if 29 - 29: Oo0Ooo - oO0o - I11i % iII111i - oO0o
  if 91 - 91: OoO0O00 / I11i - II111iiii . I11i
  i1I11i1I = xbmcgui . ListItem ( IiI11iII1 )
  i1I11i1I . setArt ( { 'thumbnailImage' : img , 'icon' : img , 'poster' : img } )
  if 81 - 81: iIii1I11I1II1 + iIii1I11I1II1 * IiII * ooOoO0o % ooOoO0o
  if infoLabels : i1I11i1I . setInfo ( type = "video" , infoLabels = infoLabels )
  if not isFolder : i1I11i1I . setProperty ( 'IsPlayable' , 'true' )
  if 81 - 81: i11iIiiIii % OoOoOO00 - OOooOOo
  xbmcplugin . addDirectoryItem ( self . _addon_handle , i11iIIIIIi1 , i1I11i1I , isFolder )
  if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
  if 92 - 92: iII111i . I1Ii111
  if 31 - 31: I1Ii111 . OoOoOO00 / O0
  if 89 - 89: OoOoOO00
 def dp_Main_List ( self ) :
  if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + ooOoO0o
  for i11i1I1 in o0oO0 :
   IiI11iII1 = i11i1I1 . get ( 'title' )
   if 36 - 36: iIii1I11I1II1 / OoOoOO00 * OOooOOo
   if i11i1I1 . get ( 'uicode' ) == 'GENRE' :
    O0ii1ii1ii = { 'mode' : 'GENRE'
 , 'uicode' : i11i1I1 . get ( 'came' )
    , 'genre' : '-'
 , 'subgenre' : '-'
    , 'orderby' : i11i1I1 . get ( 'orderby' )
 , 'ordernm' : i11i1I1 . get ( 'ordernm' )
 }
   elif i11i1I1 . get ( 'uicode' ) == 'WATCH' :
    O0ii1ii1ii = { 'mode' : 'WATCH'
 , 'genre' : '-'
 }
   elif i11i1I1 . get ( 'uicode' ) == 'SEARCH' :
    O0ii1ii1ii = { 'mode' : 'SEARCH'
 , 'genre' : '-'
 }
   else :
    O0ii1ii1ii = { 'mode' : 'GNB_LIST'
 , 'uicode' : i11i1I1 . get ( 'uicode' )
 , 'came' : i11i1I1 . get ( 'came' )
 }
    if 91 - 91: IiII
   iiIii = True
   if 79 - 79: OoooooooOO / O0
   if i11i1I1 . get ( 'uicode' ) == 'XXX' :
    O0ii1ii1ii [ 'mode' ] = 'XXX'
    iiIii = False
    if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . I1Ii111
   self . add_dir ( IiI11iII1 , sublabel = '' , img = '' , infoLabels = None , isFolder = iiIii , params = O0ii1ii1ii )
  if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
 if 5 - 5: o0oOOo0O0Ooo * ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
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
 if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
 if 79 - 79: O0
 def login_main ( self ) :
  if 78 - 78: I1ii11iIi11i + OOooOOo - I1Ii111
  ( IIIIii1I , IiI1i , o0O ) = self . get_settings_login_info ( )
  if 90 - 90: OOooOOo . I1IiiI * I1IiiI
  if 7 - 7: IiII * I1Ii111 % Ii1I - o0oOOo0O0Ooo
  if not ( IIIIii1I and IiI1i ) :
   oOOOO = xbmcgui . Dialog ( )
   i1i = oOOOO . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
   if i1i == True :
    __addon__ . openSettings ( )
    sys . exit ( )
    if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  O00o0OO0 = datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' )
  if 35 - 35: oO0o % ooOoO0o / I1Ii111 + iIii1I11I1II1 . OoooooooOO . I1IiiI
  if 71 - 71: IiII * II111iiii * oO0o
  if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINWAIT' ) == 'TRUE' :
   oOOo0 = 0
   while True :
    oOOo0 += 1
    if 16 - 16: oO0o % I1ii11iIi11i * i11iIiiIii % i11iIiiIii
    time . sleep ( 0.05 )
    if 65 - 65: Ii1I - oO0o + oO0o + II111iiii
    if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINTIME' ) == O00o0OO0 : return
    if oOOo0 > 600 : return
  else :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'TRUE' )
   if 96 - 96: OOooOOo % O0 / O0
  if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINTIME' ) == O00o0OO0 :
   xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
   return
   if 44 - 44: oO0o / I11i / I11i
  if not self . WavveObj . GetCredential ( IIIIii1I , IiI1i , o0O ) :
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
   IiI11iII1 = O0OO . get ( 'title' )
   O0ii1ii1ii = { 'mode' : 'GN_LIST' if O0OO . get ( 'uicode' ) != 'CY1' else 'GN_MYVIEW'
   , 'uicode' : O0OO . get ( 'uicode' )
 , 'came' : args . get ( 'came' )
 , 'page' : '1'
 }
   if 6 - 6: iIii1I11I1II1 % i11iIiiIii % I1ii11iIi11i
   self . add_dir ( IiI11iII1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
  if len ( Oo0OO ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 93 - 93: IiII * OoooooooOO + ooOoO0o
  if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
  if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
  if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
 def dp_Myview_Group ( self , args ) :
  IiI11iII1 = 'VOD 시청내역'
  O0ii1ii1ii = { 'mode' : 'MYVIEW_LIST'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
  self . add_dir ( IiI11iII1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
  if 26 - 26: Ii1I % I1ii11iIi11i
  IiI11iII1 = '영화 시청내역'
  O0ii1ii1ii [ 'uicode' ] = 'movie'
  self . add_dir ( IiI11iII1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
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
  oOoO = int ( args . get ( 'page' ) )
  oOoO00O0 , OO = self . WavveObj . GetMyviewList ( IiI1iIiIIIii , oOoO , addinfoyn = oo0 )
  if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
  for II1IIIIiII1i in oOoO00O0 :
   IiI11iII1 = II1IIIIiII1i . get ( 'title' )
   i1II1 = II1IIIIiII1i . get ( 'subtitle' )
   i11i1 = II1IIIIiII1i . get ( 'thumbnail' )
   if 42 - 42: i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . i11iIiiIii % I11i
   i1iI = II1IIIIiII1i . get ( 'info' )
   if IiI1iIiIIIii == 'movie' and oo0 == True :
    IiI11iII1 = '%s (%s)' % ( IiI11iII1 , str ( i1iI . get ( 'year' ) ) )
   else :
    i1iI [ 'plot' ] = IiI11iII1
    if 29 - 29: I1IiiI % OOooOOo - I1IiiI / OOooOOo . i1IIi
   if IiI1iIiIIIii == 'vod' :
    O0ii1ii1ii = { 'mode' : 'DEEP_LIST'
 , 'contentid' : II1IIIIiII1i . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : IiI11iII1
    , 'subtitle' : i1II1
    , 'thumbnail' : i11i1
    , 'viewage' : II1IIIIiII1i . get ( 'viewage' )
 }
    iiIii = True
    if 31 - 31: I1Ii111
   else :
    O0ii1ii1ii = { 'mode' : 'MOVIE'
 , 'contentid' : II1IIIIiII1i . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : IiI11iII1
    , 'subtitle' : i1II1
    , 'thumbnail' : i11i1
    , 'viewage' : II1IIIIiII1i . get ( 'viewage' )
 }
    iiIii = False
    if 88 - 88: OoO0O00 - ooOoO0o + OOooOOo * I1IiiI % iIii1I11I1II1 + Oo0Ooo
   if II1IIIIiII1i . get ( 'viewage' ) == '21' : i1II1 += ' (%s)' % ( II1IIIIiII1i . get ( 'viewage' ) )
   if 76 - 76: I1IiiI * iII111i % I1Ii111
   self . add_dir ( IiI11iII1 , sublabel = i1II1 , img = i11i1 , infoLabels = i1iI , isFolder = iiIii , params = O0ii1ii1ii )
   if 57 - 57: iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * OoooooooOO % II111iiii
  if OO :
   if 68 - 68: OoooooooOO * I11i % OoOoOO00 - IiII
   O0ii1ii1ii [ 'mode' ] = 'MYVIEW_LIST'
   O0ii1ii1ii [ 'uicode' ] = IiI1iIiIIIii
   O0ii1ii1ii [ 'page' ] = str ( oOoO + 1 )
   IiI11iII1 = '[B]%s >>[/B]' % '다음 페이지'
   i1II1 = str ( oOoO + 1 )
   self . add_dir ( IiI11iII1 , sublabel = i1II1 , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if 34 - 34: I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / I1Ii111 / I1ii11iIi11i
  if len ( oOoO00O0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 78 - 78: Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
  if 10 - 10: iII111i + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / I1ii11iIi11i
  if 42 - 42: I1IiiI
  if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
  if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
 def dp_Genre_Group ( self , args ) :
  if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
  I1 = args . get ( 'mode' )
  OooooO0oOOOO = args . get ( 'uicode' )
  o0O00oOOoo = args . get ( 'genre' )
  i1I1iIi = args . get ( 'subgenre' )
  iIIiIi1 = args . get ( 'orderby' )
  IIii11Ii1i1I = args . get ( 'ordernm' )
  if 76 - 76: O0 + i1IIi . Oo0Ooo * I1IiiI * Ii1I
  if o0O00oOOoo == '-' :
   II1iI1I11I = self . WavveObj . GetGenreGroup ( OooooO0oOOOO , o0O00oOOoo , iIIiIi1 , IIii11Ii1i1I , exclusion21 = self . get_settings_exclusion21 ( ) )
  else :
   o0OO0 = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 , 'orderby' : iIIiIi1
 , 'ordernm' : IIii11Ii1i1I
 }
   if 44 - 44: O0 - Ii1I - O0 % I11i . oO0o
   II1iI1I11I = self . WavveObj . GetGenreGroup_sub ( o0OO0 )
   if 74 - 74: i11iIiiIii . I1IiiI
   if 36 - 36: OoooooooOO . OoO0O00
  for oO in II1iI1I11I :
   IiI11iII1 = oO . get ( 'title' ) + '  (' + IIii11Ii1i1I + ')'
   if 10 - 10: Oo0Ooo / Oo0Ooo / I1Ii111 . I1Ii111
   O0ii1ii1ii = { 'mode' : I1
 , 'uicode' : OooooO0oOOOO
   , 'genre' : oO . get ( 'genre' )
 , 'subgenre' : oO . get ( 'subgenre' )
 , 'adult' : oO . get ( 'adult' )
 , 'page' : '1'
 , 'broadcastid' : oO . get ( 'broadcastid' )
 , 'contenttype' : oO . get ( 'contenttype' )
 , 'uiparent' : oO . get ( 'uiparent' )
 , 'uirank' : oO . get ( 'uirank' )
 , 'uitype' : oO . get ( 'uitype' )
 , 'orderby' : iIIiIi1
 , 'ordernm' : IIii11Ii1i1I
 }
   if 98 - 98: Oo0Ooo / I1IiiI . O0 + OoO0O00
   if OooooO0oOOOO == 'moviegenre' or OooooO0oOOOO == 'moviegenre_svod' or OooooO0oOOOO == 'moviegenre_ppv' or oO . get ( 'subgenre' ) != '-' :
    O0ii1ii1ii [ 'mode' ] = 'GENRE_LIST'
    if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
   else :
    if 20 - 20: I1IiiI
    None
    if 95 - 95: iII111i - I1IiiI
   self . add_dir ( IiI11iII1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
  if len ( II1iI1I11I ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
  if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
  if 41 - 41: i1IIi - I11i - Ii1I
  if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
 def dp_Genre_List ( self , args ) :
  if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  oo0 = self . get_settings_addinfo ( )
  if 44 - 44: II111iiii
  OooooO0oOOOO = args . get ( 'uicode' )
  oOoO = int ( args . get ( 'page' ) )
  if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
  O0ii1ii1ii = { 'adult' : args . get ( 'adult' )
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
   O0ii1ii1ii [ 'subgenre' ] = 'all'
   if 35 - 35: iIii1I11I1II1
  II1iI1I11I , OO = self . WavveObj . GetGenreList ( OooooO0oOOOO , O0ii1ii1ii , oOoO , addinfoyn = oo0 )
  if 42 - 42: I1Ii111 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
  if 31 - 31: iII111i . OOooOOo - ooOoO0o . OoooooooOO / OoooooooOO
  if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
  for oO in II1iI1I11I :
   IiI11iII1 = oO . get ( 'title' )
   i11i1 = oO . get ( 'thumbnail' )
   if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
   i1iI = oO . get ( 'info' )
   if OooooO0oOOOO == 'moviegenre_svod' and oo0 == True :
    IiI11iII1 = '%s (%s)' % ( IiI11iII1 , str ( i1iI . get ( 'year' ) ) )
   else :
    i1iI [ 'plot' ] = IiI11iII1
    if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
   if OooooO0oOOOO == 'vodgenre' :
    oooooo0OO = { 'mode' : 'DEEP_LIST'
 , 'contentid' : oO . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : IiI11iII1
    , 'subtitle' : ''
    , 'thumbnail' : i11i1
    , 'viewage' : oO . get ( 'viewage' )
 }
    iiIii = True
    if 14 - 14: oO0o / oO0o % ooOoO0o
   else :
    oooooo0OO = { 'mode' : 'MOVIE'
 , 'contentid' : oO . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : IiI11iII1
    , 'subtitle' : ''
    , 'thumbnail' : i11i1
    , 'viewage' : oO . get ( 'viewage' )
 }
    if 56 - 56: I1IiiI . O0 + Oo0Ooo
    iiIii = False
    if 1 - 1: iII111i
   if oooooo0OO . get ( 'viewage' ) == '21' : IiI11iII1 += ' (%s)' % ( oooooo0OO . get ( 'viewage' ) )
   if 97 - 97: OOooOOo + iII111i + O0 + i11iIiiIii
   self . add_dir ( IiI11iII1 , sublabel = '' , img = i11i1 , infoLabels = i1iI , isFolder = iiIii , params = oooooo0OO )
   if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
  if OO :
   if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
   O0ii1ii1ii [ 'mode' ] = 'GENRE_LIST'
   O0ii1ii1ii [ 'uicode' ] = OooooO0oOOOO
   O0ii1ii1ii [ 'page' ] = str ( oOoO + 1 )
   IiI11iII1 = '[B]%s >>[/B]' % '다음 페이지'
   i1II1 = str ( oOoO + 1 )
   self . add_dir ( IiI11iII1 , sublabel = i1II1 , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
  if len ( II1iI1I11I ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
  if 17 - 17: i1IIi
  if 21 - 21: Oo0Ooo
  if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
 def dp_Deeplink_List ( self , args ) :
  if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  oo0 = self . get_settings_addinfo ( )
  if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
  OooooO0oOOOO = args . get ( 'uicode' )
  I1ii11 = args . get ( 'came' )
  oOoO = int ( args . get ( 'page' ) )
  if 74 - 74: Oo0Ooo - o0oOOo0O0Ooo . i1IIi
  if 43 - 43: iII111i / I1IiiI
  if 58 - 58: I1IiiI + i11iIiiIii % Ii1I . OoOoOO00
  Ii1i1iI , OO = self . WavveObj . GetDeeplinkList ( OooooO0oOOOO , I1ii11 , oOoO , addinfoyn = oo0 )
  if 16 - 16: OOooOOo / Oo0Ooo / OoooooooOO * I1IiiI + i1IIi % OOooOOo
  for ooo0o00 in Ii1i1iI :
   IiI11iII1 = ooo0o00 . get ( 'title' )
   i1II1 = ooo0o00 . get ( 'subtitle' )
   i11i1 = ooo0o00 . get ( 'thumbnail' )
   ooO = ooo0o00 . get ( 'uicode' )
   o0o00 = ooo0o00 . get ( 'channelepg' )
   if 14 - 14: o0oOOo0O0Ooo . OOooOOo . I11i + OoooooooOO - OOooOOo + IiII
   O0ii1ii1ii = { 'uicode' : ooO
   , 'came' : I1ii11
 , 'contentid' : ooo0o00 . get ( 'contentid' )
 , 'contentidType' : ooo0o00 . get ( 'contentidType' )
 , 'page' : '1'
 , 'title' : IiI11iII1
   , 'subtitle' : i1II1
   , 'thumbnail' : i11i1
   , 'viewage' : ooo0o00 . get ( 'viewage' )
 }
   if 9 - 9: Ii1I
   if ooO == 'channel' :
    O0ii1ii1ii [ 'mode' ] = 'LIVE'
   elif ooO == 'movie' :
    O0ii1ii1ii [ 'mode' ] = 'MOVIE'
   else :
    O0ii1ii1ii [ 'mode' ] = 'DEEP_LIST'
    if 59 - 59: I1IiiI * II111iiii . O0
    if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
   i1iI = ooo0o00 . get ( 'info' )
   if o0o00 :
    i1iI [ 'plot' ] = '%s\n\n%s' % ( IiI11iII1 , o0o00 )
   elif ooO == 'movie' and oo0 == True :
    IiI11iII1 = '%s (%s)' % ( IiI11iII1 , str ( i1iI . get ( 'year' ) ) )
   else :
    i1iI [ 'plot' ] = '%s\n\n%s' % ( IiI11iII1 , i1II1 )
    if 51 - 51: O0 / ooOoO0o * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
   if ooo0o00 . get ( 'viewage' ) == '21' : i1II1 += ' (%s)' % ( ooo0o00 . get ( 'viewage' ) )
   if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + ooOoO0o % i11iIiiIii % O0
   if ooO in [ 'channel' , 'movie' ] :
    iiIii = False
   elif O0ii1ii1ii [ 'contentidType' ] == 'direct' :
    iiIii = False
    O0ii1ii1ii [ 'mode' ] = 'VOD'
   else :
    iiIii = True
    if 27 - 27: O0
    if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
   self . add_dir ( IiI11iII1 , sublabel = i1II1 , img = i11i1 , infoLabels = i1iI , isFolder = iiIii , params = O0ii1ii1ii )
   if 28 - 28: i1IIi - iII111i
  if OO :
   if 54 - 54: iII111i - O0 % OOooOOo
   O0ii1ii1ii [ 'mode' ] = 'GN_LIST'
   O0ii1ii1ii [ 'uicode' ] = OooooO0oOOOO
   O0ii1ii1ii [ 'page' ] = str ( oOoO + 1 )
   IiI11iII1 = '[B]%s >>[/B]' % '다음 페이지'
   i1II1 = str ( oOoO + 1 )
   self . add_dir ( IiI11iII1 , sublabel = i1II1 , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
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
  oOoO = int ( args . get ( 'page' ) )
  if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
  OoOo , OO = self . WavveObj . GetEpisodeList ( OoO0ooO , IiI1iIiIIIii , O000 , oOoO , orderby = self . get_winEpisodeOrderby ( ) )
  if 35 - 35: ooOoO0o * OOooOOo . I11i * o0oOOo0O0Ooo . OoOoOO00 / O0
  for O00 in OoOo :
   IiI11iII1 = O00 . get ( 'title' )
   i1II1 = O00 . get ( 'subtitle' )
   i11i1 = O00 . get ( 'thumbnail' )
   O0ii1ii1ii = { 'mode' : 'VOD'
 , 'uicode' : O00 . get ( 'uicode' )
   , 'contentid' : O00 . get ( 'contentid' )
 , 'programid' : O00 . get ( 'programid' )
 , 'title' : IiI11iII1
   , 'subtitle' : i1II1
   , 'thumbnail' : i11i1
   , 'viewage' : O00 . get ( 'viewage' )
 }
   if 52 - 52: ooOoO0o + O0 . iII111i . I1ii11iIi11i . OoO0O00
   if O00 . get ( 'viewage' ) == '21' : i1II1 += ' (%s)' % ( O00 . get ( 'viewage' ) )
   if 97 - 97: I1IiiI / iII111i
   Oooo0 = O00 . get ( 'info' )
   Oooo0 [ 'plot' ] = O00 . get ( 'synopsis' )
   if 59 - 59: OoooooooOO
   if 47 - 47: ooOoO0o - I1IiiI / II111iiii
   if 12 - 12: OOooOOo
   if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
   self . add_dir ( IiI11iII1 , sublabel = i1II1 , img = i11i1 , infoLabels = Oooo0 , isFolder = False , params = O0ii1ii1ii )
   if 100 - 100: OoO0O00
  if oOoO == 1 :
   i1iI = { 'plot' : '정렬순서를 변경합니다.' }
   O0ii1ii1ii = { }
   O0ii1ii1ii [ 'mode' ] = 'ORDER_BY'
   if self . get_winEpisodeOrderby ( ) == 'desc' :
    IiI11iII1 = '정렬순서변경 : 최신화부터 -> 1회부터'
    O0ii1ii1ii [ 'orderby' ] = 'asc'
   else :
    IiI11iII1 = '정렬순서변경 : 1회부터 -> 최신화부터'
    O0ii1ii1ii [ 'orderby' ] = 'desc'
   self . add_dir ( IiI11iII1 , sublabel = '' , img = '' , infoLabels = i1iI , isFolder = False , params = O0ii1ii1ii )
   if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
  if OO :
   if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
   O0ii1ii1ii [ 'mode' ] = 'DEEP_LIST'
   O0ii1ii1ii [ 'uicode' ] = IiI1iIiIIIii
   O0ii1ii1ii [ 'contentid' ] = OoO0ooO
   O0ii1ii1ii [ 'contentidType' ] = O000
   O0ii1ii1ii [ 'page' ] = str ( oOoO + 1 )
   IiI11iII1 = '[B]%s >>[/B]' % '다음 페이지'
   i1II1 = str ( oOoO + 1 )
   self . add_dir ( IiI11iII1 , sublabel = i1II1 , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if 45 - 45: I1Ii111
  if len ( OoOo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 83 - 83: OoOoOO00 . OoooooooOO
  if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
  if 62 - 62: OoO0O00 / I1ii11iIi11i
 def play_VIDEO ( self , args ) :
  if 7 - 7: OoooooooOO . IiII
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
  OoO0ooO = args . get ( 'contentid' )
  IiI1iIiIIIii = args . get ( 'uicode' )
  Oooo00 = self . get_selQuality ( )
  if 6 - 6: Ii1I - ooOoO0o * OOooOOo . iII111i / O0 * ooOoO0o
  self . addon_log ( OoO0ooO + ' - ' + IiI1iIiIIIii , False )
  II11iI111i1 , Oo00OoOo , ii1ii111 , i11111I1I = self . WavveObj . GetStreamingURL ( OoO0ooO , IiI1iIiIIIii , Oooo00 )
  if 11 - 11: OoooooooOO . I1Ii111
  if 80 - 80: OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / I1IiiI / OOooOOo
  I1I11iI11iI1i = '%s|Cookie=%s' % ( II11iI111i1 , Oo00OoOo )
  self . addon_log ( I1I11iI11iI1i , False )
  if 75 - 75: OoooooooOO * IiII
  if II11iI111i1 == '' :
   self . addon_noti ( __language__ ( 30303 ) . encode ( 'utf8' ) )
   return
   if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  I1IIIiI1I1ii1 = xbmcgui . ListItem ( path = I1I11iI11iI1i )
  if 30 - 30: O0 * OoooooooOO
  if ii1ii111 :
   if 38 - 38: IiII - I1ii11iIi11i . OoOoOO00 - I1Ii111 . OoooooooOO
   if 89 - 89: iIii1I11I1II1
   i11iiiiI1i = ii1ii111 [ 'customdata' ]
   iIIii = ii1ii111 [ 'drmhost' ]
   if 18 - 18: iII111i . I1IiiI
   iiIi1IIiI = 'mpd'
   i1 = 'com.widevine.alpha'
   if 67 - 67: I1IiiI
   OO00OO0O0 = inputstreamhelper . Helper ( iiIi1IIiI , drm = i1 )
   if 48 - 48: I1Ii111
   if OO00OO0O0 . check_inputstream ( ) :
    if 72 - 72: iII111i * oO0o % Ii1I . OoooooooOO
    if IiI1iIiIIIii == 'movie' :
     OoO0O0O0o00 = 'https://www.wavve.com/player/movie?movieid=%s' % OoO0ooO
    else :
     OoO0O0O0o00 = 'https://www.wavve.com/player/vod?programid=%s&page=1' % OoO0ooO
     if 7 - 7: I1IiiI + OoOoOO00 / IiII
    OOOoO000 = { 'content-type' : 'application/octet-stream'
 , 'origin' : 'https://www.wavve.com'
 , 'pallycon-customdata' : i11iiiiI1i
 , 'referer' : OoO0O0O0o00
 , 'sec-fetch-dest' : 'empty'
    , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'

    , 'user-agent' : OOoO
 }
    oOOOOIi = iIIii + '|' + urllib . urlencode ( OOOoO000 ) + '|R{SSM}|'
    if 15 - 15: i11iIiiIii % I1IiiI * I11i / I1Ii111
    I1IIIiI1I1ii1 . setProperty ( 'inputstreamaddon' , OO00OO0O0 . inputstream_addon )
    I1IIIiI1I1ii1 . setProperty ( 'inputstream.adaptive.manifest_type' , iiIi1IIiI )
    I1IIIiI1I1ii1 . setProperty ( 'inputstream.adaptive.license_type' , i1 )
    if 90 - 90: iII111i
    I1IIIiI1I1ii1 . setProperty ( 'inputstream.adaptive.license_key' , oOOOOIi )
    I1IIIiI1I1ii1 . setProperty ( 'inputstream.adaptive.stream_headers' , 'Cookie=%s' % Oo00OoOo )
    if 31 - 31: OOooOOo + O0
  xbmcplugin . setResolvedUrl ( self . _addon_handle , True , I1IIIiI1I1ii1 )
  if 87 - 87: ooOoO0o
  if i11111I1I :
   self . addon_noti ( i11111I1I . encode ( 'utf-8' ) )
  else :
   if '/preview.' in urlparse . urlsplit ( II11iI111i1 ) . path : self . addon_noti ( __language__ ( 30401 ) . encode ( 'utf8' ) )
   if 45 - 45: OoO0O00 / OoooooooOO - iII111i / Ii1I % IiII
  try :
   if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) and args . get ( 'viewage' ) != '21' :
    O0ii1ii1ii = { 'code' : args . get ( 'programid' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'contentid' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 , 'subtitle' : args . get ( 'subtitle' )
 , 'videoid' : args . get ( 'contentid' )
    }
    self . Save_Watched_List ( args . get ( 'mode' ) . lower ( ) , O0ii1ii1ii )
  except :
   None
   if 83 - 83: I1IiiI . iIii1I11I1II1 - IiII * i11iIiiIii
   if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
   if 13 - 13: Oo0Ooo
   if 60 - 60: I1ii11iIi11i * I1IiiI
 def dp_Watch_List ( self , args ) :
  o0O00oOOoo = args . get ( 'genre' )
  o00oOO0 = self . get_settings_direct_replay ( )
  if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
  if o0O00oOOoo == '-' :
   IiI11iII1 = 'VOD 시청내역'
   O0ii1ii1ii = { 'mode' : 'WATCH'
 , 'genre' : 'vod'
 }
   self . add_dir ( IiI11iII1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if 41 - 41: Ii1I
   IiI11iII1 = '영화 시청내역'
   O0ii1ii1ii [ 'genre' ] = 'movie'
   self . add_dir ( IiI11iII1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if 77 - 77: I1Ii111
   xbmcplugin . endOfDirectory ( self . _addon_handle )
   if 65 - 65: II111iiii . I1IiiI % oO0o * OoO0O00
  else :
   iI11I = self . Load_Watched_List ( o0O00oOOoo )
   if 11 - 11: iII111i - oO0o + II111iiii - iIii1I11I1II1
   for I1i11ii11 in iI11I :
    OO00O0oOO = dict ( urlparse . parse_qsl ( I1i11ii11 ) )
    if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
    IiI11iII1 = OO00O0oOO . get ( 'title' ) . strip ( )
    i1II1 = OO00O0oOO . get ( 'subtitle' ) . strip ( )
    if i1II1 == 'None' : i1II1 = ''
    i11i1 = OO00O0oOO . get ( 'img' )
    Ooooo00o0OoO = OO00O0oOO . get ( 'videoid' )
    if 75 - 75: I1IiiI % II111iiii
    if 30 - 30: IiII + I1Ii111 - IiII . IiII - II111iiii + O0
    i1iI = { }
    if o0O00oOOoo == 'movie' and self . get_settings_addinfo ( ) == True :
     oOO0 = self . WavveObj . GetMovieInfoList ( [ OO00O0oOO . get ( 'code' ) ] )
     i1iI = oOO0 . get ( OO00O0oOO . get ( 'code' ) )
    else :
     i1iI [ 'plot' ] = '%s\n%s' % ( IiI11iII1 , i1II1 )
     if 46 - 46: Ii1I % OoOoOO00
    if o0O00oOOoo == 'vod' :
     if o00oOO0 == False or Ooooo00o0OoO == None :
      O0ii1ii1ii = { 'mode' : 'DEEP_LIST'
 , 'contentid' : OO00O0oOO . get ( 'code' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
      iiIii = True
     else :
      O0ii1ii1ii = { 'mode' : 'VOD'
 , 'contentid' : Ooooo00o0OoO
 , 'contentidType' : 'contentid'
 , 'programid' : OO00O0oOO . get ( 'code' )
 , 'uicode' : 'vod'
 , 'title' : IiI11iII1
 , 'subtitle' : i1II1
 , 'thumbnail' : i11i1
 }
      iiIii = False
    else :
     O0ii1ii1ii = { 'mode' : 'MOVIE'
 , 'contentid' : OO00O0oOO . get ( 'code' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'title' : IiI11iII1
 , 'thumbnail' : i11i1
 }
     iiIii = False
     if 64 - 64: i11iIiiIii - II111iiii
    self . add_dir ( IiI11iII1 , sublabel = i1II1 , img = i11i1 , infoLabels = i1iI , isFolder = iiIii , params = O0ii1ii1ii )
    if 77 - 77: OoOoOO00 % Ii1I
   i1iI = { 'plot' : '시청목록을 삭제합니다.' }
   IiI11iII1 = '*** 시청목록 삭제 ***'
   O0ii1ii1ii = { 'mode' : 'MYVIEW_REMOVE'
 , 'genre' : o0O00oOOoo
 }
   if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
   self . add_dir ( IiI11iII1 , sublabel = '' , img = '' , infoLabels = i1iI , isFolder = False , params = O0ii1ii1ii )
   if 2 - 2: OoooooooOO % OOooOOo
   xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
   if 63 - 63: I1IiiI % iIii1I11I1II1
   if 39 - 39: iII111i / II111iiii / I1ii11iIi11i % I1IiiI
   if 89 - 89: I1Ii111 + OoooooooOO + I1Ii111 * i1IIi + iIii1I11I1II1 % I11i
   if 59 - 59: OOooOOo + i11iIiiIii
   if 88 - 88: i11iIiiIii - ooOoO0o
 def dp_Search_Group ( self , args ) :
  IiI11iII1 = 'VOD 검색'
  O0ii1ii1ii = { 'mode' : 'SEARCH_LIST'
 , 'genre' : 'vod'
 , 'page' : '1'
 }
  self . add_dir ( IiI11iII1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
  if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
  IiI11iII1 = '영화 검색'
  O0ii1ii1ii [ 'genre' ] = 'movie'
  self . add_dir ( IiI11iII1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
  if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
  xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - I11i
  if 30 - 30: OoOoOO00
  if 21 - 21: i11iIiiIii / I1Ii111 % OOooOOo * O0 . I11i - iIii1I11I1II1
  if 26 - 26: II111iiii * OoOoOO00
 def dp_Search_List ( self , args ) :
  if 10 - 10: II111iiii . iII111i
  self . WavveObj . SaveCredential ( self . get_winCredential ( ) )
  oo0 = self . get_settings_addinfo ( )
  if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
  IiI1iIiIIIii = args . get ( 'genre' )
  oOoO = int ( args . get ( 'page' ) )
  if 88 - 88: iII111i
  if 'search_key' in args :
   iiI11I1i1i1iI = args . get ( 'search_key' )
  else :
   iiI11I1i1i1iI = self . get_keyboard_input ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
   if not iiI11I1i1i1iI : return
   if 60 - 60: OoooooooOO % Oo0Ooo + OOooOOo . ooOoO0o * iIii1I11I1II1
  oooo00 , OO = self . WavveObj . GetSearchList ( iiI11I1i1i1iI , IiI1iIiIIIii , oOoO , exclusion21 = self . get_settings_exclusion21 ( ) , addinfoyn = oo0 )
  if 77 - 77: ooOoO0o - I1IiiI % I11i - O0
  for o0O0O0 in oooo00 :
   IiI11iII1 = o0O0O0 . get ( 'title' )
   i11i1 = o0O0O0 . get ( 'thumbnail' )
   if 6 - 6: iII111i . IiII * OoOoOO00 . i1IIi
   i1iI = o0O0O0 . get ( 'info' )
   if IiI1iIiIIIii == 'movie' and oo0 == True :
    IiI11iII1 = '%s (%s)' % ( IiI11iII1 , str ( i1iI . get ( 'year' ) ) )
   else :
    i1iI [ 'plot' ] = IiI11iII1
    if 98 - 98: i1IIi
   if IiI1iIiIIIii == 'vod' :
    O0ii1ii1ii = { 'mode' : 'DEEP_LIST'
 , 'contentid' : o0O0O0 . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : IiI11iII1
    , 'subtitle' : ''
    , 'thumbnail' : i11i1
    , 'viewage' : o0O0O0 . get ( 'viewage' )
 }
    iiIii = True
    if 65 - 65: OoOoOO00 / OoO0O00 % IiII
   else :
    O0ii1ii1ii = { 'mode' : 'MOVIE'
 , 'contentid' : o0O0O0 . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : IiI11iII1
    , 'subtitle' : ''
    , 'thumbnail' : i11i1
    , 'viewage' : o0O0O0 . get ( 'viewage' )
 }
    if 45 - 45: OoOoOO00
    iiIii = False
    if 66 - 66: OoO0O00
   if O0ii1ii1ii . get ( 'viewage' ) == '21' : IiI11iII1 += ' (%s)' % ( O0ii1ii1ii . get ( 'viewage' ) )
   if 56 - 56: O0
   self . add_dir ( IiI11iII1 , sublabel = '' , img = i11i1 , infoLabels = i1iI , isFolder = iiIii , params = O0ii1ii1ii )
   if 61 - 61: o0oOOo0O0Ooo / OOooOOo / Oo0Ooo * O0
  if OO :
   if 23 - 23: oO0o - OOooOOo + I11i
   O0ii1ii1ii [ 'mode' ] = 'SEARCH_LIST'
   O0ii1ii1ii [ 'genre' ] = IiI1iIiIIIii
   O0ii1ii1ii [ 'page' ] = str ( oOoO + 1 )
   O0ii1ii1ii [ 'search_key' ] = iiI11I1i1i1iI
   IiI11iII1 = '[B]%s >>[/B]' % '다음 페이지'
   i1II1 = str ( oOoO + 1 )
   self . add_dir ( IiI11iII1 , sublabel = i1II1 , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if 12 - 12: I1IiiI / ooOoO0o % o0oOOo0O0Ooo / i11iIiiIii % OoooooooOO
  if len ( oooo00 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo0Ooo * Ii1I + I11i
  if 11 - 11: iII111i * Ii1I - OoOoOO00
  if 66 - 66: OoOoOO00 . i11iIiiIii - iII111i * o0oOOo0O0Ooo + OoooooooOO * I1ii11iIi11i
  if 74 - 74: Oo0Ooo
  if 61 - 61: Oo0Ooo - I1Ii111 * II111iiii % ooOoO0o * iIii1I11I1II1 + OoO0O00
 def Load_Watched_List ( self , genre ) :
  try :
   O0000 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   with open ( O0000 , 'r' ) as ooO00O0O0 :
    iII1I1 = ooO00O0O0 . readlines ( )
  except :
   iII1I1 = [ ]
   if 85 - 85: iII111i * o0oOOo0O0Ooo
  return iII1I1
  if 3 - 3: OOooOOo
  if 20 - 20: II111iiii . iII111i / II111iiii % i11iIiiIii % iII111i
  if 11 - 11: IiII % I1ii11iIi11i % Ii1I / II111iiii % I1Ii111 - Oo0Ooo
  if 96 - 96: I1ii11iIi11i / II111iiii . Ii1I - iII111i * I11i * oO0o
 def Save_Watched_List ( self , genre , in_params ) :
  try :
   O0000 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   O00oo0ooO = self . Load_Watched_List ( genre )
   if 38 - 38: iIii1I11I1II1 - II111iiii - I1IiiI
   with open ( O0000 , 'w' ) as ooO00O0O0 :
    ooo = urllib . urlencode ( in_params )
    ooo = ooo . encode ( 'utf-8' ) + '\n'
    ooO00O0O0 . write ( ooo )
    if 94 - 94: OoOoOO00 - Oo0Ooo - I1IiiI % i1IIi
    iIIiiiiI = 0
    for I111i1I1 in O00oo0ooO :
     O0o00OOo00O0O = dict ( urlparse . parse_qsl ( I111i1I1 ) )
     if 5 - 5: o0oOOo0O0Ooo / OoooooooOO * o0oOOo0O0Ooo * O0 . Ii1I % IiII
     i111I11i = in_params . get ( 'code' )
     ii1OoOO = O0o00OOo00O0O . get ( 'code' )
     if genre == 'vod' and self . get_settings_direct_replay ( ) == True :
      i111I11i = in_params . get ( 'videoid' )
      ii1OoOO = O0o00OOo00O0O . get ( 'videoid' ) if ii1OoOO != None else '-'
      if 44 - 44: OOooOOo
     if i111I11i != ii1OoOO :
      ooO00O0O0 . write ( I111i1I1 )
      iIIiiiiI += 1
      if iIIiiiiI >= 50 : break
  except :
   None
   if 54 - 54: Ii1I - I11i - I1Ii111 . iIii1I11I1II1
   if 79 - 79: Ii1I . OoO0O00
   if 40 - 40: o0oOOo0O0Ooo + Oo0Ooo . o0oOOo0O0Ooo % ooOoO0o
   if 15 - 15: Ii1I * Oo0Ooo % I1ii11iIi11i * iIii1I11I1II1 - i11iIiiIii
 def Delete_Watched_List ( self , genre ) :
  try :
   O0000 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
   with open ( O0000 , 'w' ) as ooO00O0O0 :
    ooO00O0O0 . write ( '' )
  except :
   None
   if 60 - 60: I1IiiI * I1Ii111 % OoO0O00 + oO0o
   if 52 - 52: i1IIi
   if 84 - 84: Ii1I / IiII
   if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / OOooOOo
 def dp_WatchList_Delete ( self , args ) :
  o0O00oOOoo = args . get ( 'genre' )
  if 11 - 11: I1IiiI * oO0o + I1ii11iIi11i / I1ii11iIi11i
  oOOOO = xbmcgui . Dialog ( )
  i1i = oOOOO . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if i1i == False : sys . exit ( )
  if 37 - 37: i11iIiiIii + i1IIi
  self . Delete_Watched_List ( o0O00oOOoo )
  if 23 - 23: iII111i + I11i . OoOoOO00 * I1IiiI + I1ii11iIi11i
  xbmc . executebuiltin ( "Container.Refresh" )
  if 18 - 18: IiII * o0oOOo0O0Ooo . IiII / O0
  if 8 - 8: o0oOOo0O0Ooo
  if 4 - 4: I1ii11iIi11i + I1ii11iIi11i * ooOoO0o - OoOoOO00
  if 78 - 78: Ii1I / II111iiii % OoOoOO00
  if 52 - 52: OOooOOo - iII111i * oO0o
  if 17 - 17: OoooooooOO + OOooOOo * I11i * OoOoOO00
  if 36 - 36: O0 + Oo0Ooo
  if 5 - 5: Oo0Ooo * OoOoOO00
  if 46 - 46: ooOoO0o
  if 33 - 33: iII111i - II111iiii * OoooooooOO - Oo0Ooo - OOooOOo
  if 84 - 84: I1Ii111 + Oo0Ooo - OoOoOO00 * OoOoOO00
 def wavve_main ( self ) :
  if 61 - 61: OoooooooOO . oO0o . OoooooooOO / Oo0Ooo
  I1 = self . main_params . get ( 'mode' , None )
  if 72 - 72: i1IIi
  self . login_main ( )
  if I1 is None :
   if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i . OoooooooOO
   self . dp_Main_List ( )
   if 63 - 63: I1ii11iIi11i
   if 6 - 6: ooOoO0o / I1ii11iIi11i
   if 57 - 57: I11i
   if 67 - 67: OoO0O00 . ooOoO0o
   if 87 - 87: oO0o % Ii1I
   if 83 - 83: II111iiii - I11i
   if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
   if 86 - 86: iIii1I11I1II1 + OoOoOO00 . i11iIiiIii - Ii1I
   if 51 - 51: OoOoOO00
  elif I1 == 'GNB_LIST' :
   self . dp_Gnb_List ( self . main_params )
   if 14 - 14: IiII % oO0o % Oo0Ooo - i11iIiiIii
  elif I1 == 'GN_LIST' :
   self . dp_Deeplink_List ( self . main_params )
   if 53 - 53: Ii1I % Oo0Ooo
  elif I1 == 'DEEP_LIST' :
   IiI1iIiIIIii = self . main_params . get ( 'uicode' , None )
   if 59 - 59: OOooOOo % iIii1I11I1II1 . i1IIi + II111iiii * IiII
   if IiI1iIiIIIii in [ 'quick' , 'vod' , 'program' , 'x' ] :
    self . dp_Episodelink_List ( self . main_params )
    if 41 - 41: Ii1I % I1ii11iIi11i
   else : None
   if 12 - 12: OOooOOo
  elif I1 in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
   self . play_VIDEO ( self . main_params )
   if 69 - 69: OoooooooOO + OOooOOo
   time . sleep ( 0.1 )
   if 26 - 26: Oo0Ooo + OOooOOo / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
  elif I1 == 'GN_MYVIEW' :
   self . dp_Myview_Group ( self . main_params )
   if 31 - 31: I11i % OOooOOo * I11i
  elif I1 == 'MYVIEW_LIST' :
   self . dp_Myview_List ( self . main_params )
   if 45 - 45: i1IIi . I1IiiI + OOooOOo - OoooooooOO % ooOoO0o
  elif I1 == 'GENRE' :
   self . dp_Genre_Group ( self . main_params )
   if 1 - 1: iIii1I11I1II1
  elif I1 == 'GENRE_LIST' :
   self . dp_Genre_List ( self . main_params )
   if 93 - 93: i1IIi . i11iIiiIii . Oo0Ooo
  elif I1 == 'WATCH' :
   self . dp_Watch_List ( self . main_params )
   if 99 - 99: I11i - I1Ii111 - oO0o % OoO0O00
  elif I1 == 'MYVIEW_REMOVE' :
   self . dp_WatchList_Delete ( self . main_params )
   if 21 - 21: II111iiii % I1ii11iIi11i . i1IIi - OoooooooOO
  elif I1 == 'SEARCH' :
   self . dp_Search_Group ( self . main_params )
   if 4 - 4: OoooooooOO . ooOoO0o
  elif I1 == 'SEARCH_LIST' :
   self . dp_Search_List ( self . main_params )
   if 78 - 78: I1ii11iIi11i + I11i - O0
  elif I1 == 'ORDER_BY' :
   self . dp_setEpOrderby ( self . main_params )
   if 10 - 10: I1Ii111 % I1IiiI
  else :
   None
   if 97 - 97: OoooooooOO - I1Ii111
   if 58 - 58: iIii1I11I1II1 + O0
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
