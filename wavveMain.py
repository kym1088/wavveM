# -*- coding: utf-8 -*-
__author__ = "NightRain"
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
import os
import xbmcplugin , xbmcgui , xbmcaddon
import sys
import urlparse
import inputstreamhelper
import datetime
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
__addon__ = xbmcaddon . Addon ( )
__language__ = __addon__ . getLocalizedString
__profile__ = xbmc . translatePath ( __addon__ . getAddonInfo ( 'profile' ) )
__version__ = __addon__ . getAddonInfo ( 'version' )
__addonid__ = __addon__ . getAddonInfo ( 'id' )
__addonname__ = __addon__ . getAddonInfo ( 'name' )
__cwd__ = xbmc . translatePath ( __addon__ . getAddonInfo ( 'path' ) )
__lib__ = os . path . join ( __cwd__ , 'resources' , 'lib' )
__data__ = os . path . join ( __cwd__ , 'resources' , 'data' )
sys . path . append ( __lib__ )
sys . path . append ( __data__ )
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
from wavveCore import *
if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1 . IiII / IiII % IiII
if 22 - 22: Ii1I . IiII
def I11 ( sting ) :
 try :
  Oo0o0000o0o0 = xbmcgui . Dialog ( )
  if 86 - 86: OoOoOO00 % I1IiiI
  Oo0o0000o0o0 . notification ( __addonname__ , sting )
 except :
  None
  if 80 - 80: OoooooooOO . I1IiiI
  if 87 - 87: oO0o / ooOoO0o + I1Ii111 - ooOoO0o . ooOoO0o / II111iiii
  if 11 - 11: I1IiiI % o0oOOo0O0Ooo - Oo0Ooo
def oo0O000OoO ( string , isDebug = False ) :
 try :
  i1iiIIiiI111 = string . encode ( 'utf-8' , 'ignore' )
 except :
  i1iiIIiiI111 = 'addonException: addon_log'
 if isDebug : oooOOOOO = xbmc . LOGDEBUG
 else : oooOOOOO = xbmc . LOGNOTICE
 xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , i1iiIIiiI111 ) , level = oooOOOOO )
 if 22 - 22: Ii1I * O0 / o0oOOo0O0Ooo
 if 64 - 64: Ii1I % i1IIi % OoooooooOO
 if 3 - 3: iII111i + O0
 if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
def oo0Ooo0 ( title ) :
 I1I11I1I1I = None
 OooO0OO = xbmc . Keyboard ( )
 OooO0OO . setHeading ( title )
 xbmc . sleep ( 1000 )
 OooO0OO . doModal ( )
 if ( OooO0OO . isConfirmed ( ) ) :
  I1I11I1I1I = OooO0OO . getText ( )
 return I1I11I1I1I
 if 28 - 28: II111iiii
 if 28 - 28: iIii1I11I1II1 - i1IIi
 if 70 - 70: OoO0O00 . OoO0O00 - OoO0O00 / I1ii11iIi11i * OOooOOo
 if 86 - 86: i11iIiiIii + Ii1I + ooOoO0o * I11i + o0oOOo0O0Ooo
def oOoO ( ) :
 oOo = __addon__ . getSetting ( 'id' )
 oOoOoO = __addon__ . getSetting ( 'pw' )
 ii1I = __addon__ . getSetting ( 'selected_profile' )
 return ( oOo , oOoOoO , ii1I )
 if 76 - 76: O0 / o0oOOo0O0Ooo . I1IiiI * Ii1I - OOooOOo
 if 76 - 76: i11iIiiIii / iIii1I11I1II1 . I1ii11iIi11i % OOooOOo / OoooooooOO % oO0o
 if 75 - 75: iII111i
def oo ( ) :
 try :
  O0o0Oo = [ 1080 , 720 , 480 , 360 ]
  if 78 - 78: iIii1I11I1II1 - Ii1I * OoO0O00 + o0oOOo0O0Ooo + iII111i + iII111i
  I11I11i1I = int ( __addon__ . getSetting ( 'selected_quality' ) )
  return O0o0Oo [ I11I11i1I ]
 except :
  None
  if 49 - 49: II111iiii % iII111i * O0
 return 1080
 if 89 - 89: oO0o + Oo0Ooo
 if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
 if 49 - 49: oO0o % Ii1I + i1IIi . I1IiiI % I1ii11iIi11i
def I1i1iii ( ) :
 i1iiI11I = __addon__ . getSetting ( 'exclusion21' )
 if i1iiI11I == 'false' :
  return False
 else :
  return True
  if 29 - 29: OoooooooOO
  if 23 - 23: o0oOOo0O0Ooo . II111iiii
  if 98 - 98: iIii1I11I1II1 % OoOoOO00 * I1ii11iIi11i * OoOoOO00
def i1 ( ) :
 IiIiiI = int ( __addon__ . getSetting ( 'thumbnail_way' ) )
 if IiIiiI == 0 :
  return True
 else :
  return False
  if 31 - 31: Ii1I . Ii1I - o0oOOo0O0Ooo / OoO0O00 + ooOoO0o * I1IiiI
  if 63 - 63: I1Ii111 % i1IIi / OoooooooOO - OoooooooOO
  if 8 - 8: OoOoOO00
  if 60 - 60: I11i / I11i
def I1II1III11iii ( credential ) :
 Oo000 = xbmcgui . Window ( 10000 )
 Oo000 . setProperty ( 'WAVVE_M_CREDENTIAL' , credential )
 if 51 - 51: i11iIiiIii . I1IiiI + II111iiii
 Oo000 . setProperty ( 'WAVVE_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
 if 10 - 10: I1ii11iIi11i * ooOoO0o * II111iiii % Ii1I . OOooOOo + I1Ii111
def IIiIi11i1 ( ) :
 Oo000 = xbmcgui . Window ( 10000 )
 return Oo000 . getProperty ( 'WAVVE_M_CREDENTIAL' )
 if 29 - 29: I1ii11iIi11i % I1IiiI + ooOoO0o / o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
def i1I1iI ( orderby ) :
 Oo000 = xbmcgui . Window ( 10000 )
 Oo000 . setProperty ( 'WAVVE_M_ORDERBY' , orderby )
 if 93 - 93: iIii1I11I1II1 % oO0o * i1IIi
def Ii11Ii1I ( ) :
 Oo000 = xbmcgui . Window ( 10000 )
 return Oo000 . getProperty ( 'WAVVE_M_ORDERBY' )
 if 72 - 72: iII111i / i1IIi * Oo0Ooo - I1Ii111
 if 51 - 51: II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % I1ii11iIi11i / ooOoO0o
 if 49 - 49: o0oOOo0O0Ooo
def IIii1Ii1 ( ) :
 I1II11IiII = urlparse . parse_qs ( sys . argv [ 2 ] [ 1 : ] )
 for OOO0OOo in I1II11IiII . keys ( ) :
  I1II11IiII [ OOO0OOo ] = I1II11IiII [ OOO0OOo ] [ 0 ]
 return I1II11IiII
 if 47 - 47: OOooOOo + IiII - IiII * I1IiiI + Ii1I % IiII
 if 4 - 4: oO0o
 if 93 - 93: OoO0O00 % oO0o . OoO0O00 * I1Ii111 % Ii1I . II111iiii
def iI1ii1Ii ( label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
 if 92 - 92: OoOoOO00
 i1OOO = '%s?%s' % ( sys . argv [ 0 ] , urllib . urlencode ( params ) )
 if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
 if sublabel : Oo0OoO00oOO0o = '%s < %s >' % ( label , sublabel )
 else : Oo0OoO00oOO0o = label
 if not img : img = 'DefaultFolder.png'
 if 80 - 80: oO0o + OOooOOo - OOooOOo % iII111i
 OoOO0oo0o = xbmcgui . ListItem ( Oo0OoO00oOO0o , thumbnailImage = img )
 if infoLabels : OoOO0oo0o . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder : OoOO0oo0o . setProperty ( 'IsPlayable' , 'true' )
 if 14 - 14: o0oOOo0O0Ooo * iII111i * iII111i / OoOoOO00
 xbmcplugin . addDirectoryItem ( Oo0o00 , i1OOO , OoOO0oo0o , isFolder )
 if 73 - 73: iII111i * Ii1I + o0oOOo0O0Ooo . OOooOOo + I1ii11iIi11i % iII111i
 if 95 - 95: i1IIi
 if 3 - 3: I1Ii111 - O0 / I1Ii111 % OoO0O00 / I1Ii111 . I1IiiI
 if 50 - 50: IiII
def i11I1iIiII ( ) :
 if 96 - 96: Oo0Ooo
 for Ii1I1IIii1II in o0oO0 :
  Oo0OoO00oOO0o = Ii1I1IIii1II . get ( 'title' )
  if 65 - 65: Ii1I . iIii1I11I1II1 / O0 - Ii1I
  if Ii1I1IIii1II . get ( 'uicode' ) == 'GENRE' :
   iii1i1iiiiIi = { 'mode' : 'GENRE'
 , 'uicode' : Ii1I1IIii1II . get ( 'came' )
   , 'genre' : '-'
 , 'subgenre' : '-'
   , 'orderby' : Ii1I1IIii1II . get ( 'orderby' )
 , 'ordernm' : Ii1I1IIii1II . get ( 'ordernm' )
 }
  elif Ii1I1IIii1II . get ( 'uicode' ) == 'WATCH' :
   iii1i1iiiiIi = { 'mode' : 'WATCH'
 , 'genre' : '-'
 }
  elif Ii1I1IIii1II . get ( 'uicode' ) == 'SEARCH' :
   iii1i1iiiiIi = { 'mode' : 'SEARCH'
 , 'genre' : '-'
 }
  else :
   iii1i1iiiiIi = { 'mode' : 'GNB_LIST'
 , 'uicode' : Ii1I1IIii1II . get ( 'uicode' )
 , 'came' : Ii1I1IIii1II . get ( 'came' )
 }
   if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
  o0o00OO0 = True
  if 7 - 7: OOooOOo + I1Ii111 + O0
  if Ii1I1IIii1II . get ( 'uicode' ) == 'XXX' :
   iii1i1iiiiIi [ 'mode' ] = 'XXX'
   o0o00OO0 = False
   if 9 - 9: II111iiii . o0oOOo0O0Ooo - ooOoO0o / o0oOOo0O0Ooo
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = o0o00OO0 , params = iii1i1iiiiIi )
 if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 )
 if 46 - 46: I11i . OOooOOo * I11i % i1IIi
 if 46 - 46: OoOoOO00 + OoO0O00
 if 10 - 10: Oo0Ooo - I1Ii111 . O0
 if 84 - 84: O0
def OOOooOO0 ( ) :
 ( OOOOoOoo0O0O0 , OOOo00oo0oO , IIiIi1iI ) = oOoO ( )
 if 35 - 35: Ii1I % O0 - O0
 if 16 - 16: II111iiii % OoOoOO00 - II111iiii + Ii1I
 if 12 - 12: OOooOOo / OOooOOo + i11iIiiIii
 if 40 - 40: I1IiiI . iIii1I11I1II1 / I1IiiI / i11iIiiIii
 if 75 - 75: I11i + o0oOOo0O0Ooo
 if not ( OOOOoOoo0O0O0 and OOOo00oo0oO ) :
  Oo0o0000o0o0 = xbmcgui . Dialog ( )
  O0i1II1Iiii1I11 = Oo0o0000o0o0 . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
  if O0i1II1Iiii1I11 == True :
   __addon__ . openSettings ( )
   sys . exit ( )
   if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
   if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
 if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINWAIT' ) == 'TRUE' :
  IIi1I11I1II = 0
  while True :
   IIi1I11I1II += 1
   xbmc . sleep ( 250 )
   if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINWAIT' ) == 'FALSE' or IIi1I11I1II > 500 :
    break
    if 63 - 63: OoooooooOO - OoO0O00 . II111iiii / o0oOOo0O0Ooo . OoOoOO00 / O0
 o0OOOO00O0Oo = xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINTIME' )
 if 48 - 48: O0
 if o0OOOO00O0Oo != '' :
  if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
  if o0OOOO00O0Oo == datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) :
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
   return
   if 77 - 77: iIii1I11I1II1 * OoO0O00
 xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'TRUE' )
 if 95 - 95: I1IiiI + i11iIiiIii
 if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
 if not o00o0 . GetCredential ( OOOOoOoo0O0O0 , OOOo00oo0oO , IIiIi1iI ) :
  I11 ( __language__ ( 30103 ) . encode ( 'utf8' ) )
  xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
  sys . exit ( )
  if 45 - 45: O0
  if 26 - 26: I11i - iIii1I11I1II1 - I1IiiI / OoO0O00 . OoOoOO00 % iIii1I11I1II1
 I1II1III11iii ( o00o0 . LoadCredential ( ) )
 i1I1iI ( 'desc' )
 xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
 if 91 - 91: o0oOOo0O0Ooo . iIii1I11I1II1 / oO0o + i1IIi
 if 42 - 42: ooOoO0o . o0oOOo0O0Ooo . ooOoO0o - I1ii11iIi11i
 if 40 - 40: ooOoO0o - i11iIiiIii / Ii1I
 if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
def I1i1Iiiii ( args ) :
 OOo0oO00ooO00 = args . get ( 'orderby' )
 if 90 - 90: OoOoOO00 * I1Ii111 + o0oOOo0O0Ooo
 i1I1iI ( OOo0oO00ooO00 )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 81 - 81: oO0o . o0oOOo0O0Ooo % O0 / I1IiiI - oO0o
 if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * I1Ii111 * O0
 if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
 if 79 - 79: O0
def oOO00O ( args ) :
 if 77 - 77: Oo0Ooo - i1IIi - I11i . OoOoOO00
 o00o0 . SaveCredential ( IIiIi11i1 ( ) )
 if 39 - 39: II111iiii / ooOoO0o + I1Ii111 / OoOoOO00
 I1Ii11i = o00o0 . GetGnList ( args . get ( 'uicode' ) )
 if 35 - 35: o0oOOo0O0Ooo
 if 90 - 90: I1Ii111 % Ii1I - iIii1I11I1II1 - iIii1I11I1II1 / i11iIiiIii % I1ii11iIi11i
 if 37 - 37: oO0o - I1IiiI . I11i * Ii1I - iII111i
 if 8 - 8: OoO0O00 - I1IiiI % Ii1I * OoooooooOO - OoO0O00 * I1Ii111
 for iii in I1Ii11i :
  Oo0OoO00oOO0o = iii . get ( 'title' )
  iii1i1iiiiIi = { 'mode' : 'GN_LIST' if iii . get ( 'uicode' ) != 'CY1' else 'GN_MYVIEW'
  , 'uicode' : iii . get ( 'uicode' )
 , 'came' : args . get ( 'came' )
 , 'page' : '1'
 }
  if 71 - 71: IiII * II111iiii * oO0o
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
 if len ( I1Ii11i ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 , cacheToDisc = False )
 if 56 - 56: I1IiiI
 if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
 if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
 if 63 - 63: OoOoOO00 * iII111i
def ooiIi1 ( args ) :
 Oo0OoO00oOO0o = 'VOD 시청내역'
 iii1i1iiiiIi = { 'mode' : 'MYVIEW_LIST'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
 iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
 if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
 Oo0OoO00oOO0o = '영화 시청내역'
 iii1i1iiiiIi [ 'uicode' ] = 'movie'
 iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
 if 62 - 62: OoooooooOO * I1IiiI
 xbmcplugin . endOfDirectory ( Oo0o00 )
 if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
 if 50 - 50: I1Ii111 . o0oOOo0O0Ooo
 if 97 - 97: O0 + OoOoOO00
 if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
def iiIiI1i1 ( args ) :
 if 69 - 69: ooOoO0o
 o00o0 . SaveCredential ( IIiIi11i1 ( ) )
 if 40 - 40: I1Ii111 + OoooooooOO % o0oOOo0O0Ooo - iIii1I11I1II1 . I1IiiI
 iIiIi11iI = args . get ( 'uicode' )
 Oo0O00O000 = int ( args . get ( 'page' ) )
 i11I1IiII1i1i , ooI1111i = o00o0 . GetMyviewList ( iIiIi11iI , Oo0O00O000 )
 if 14 - 14: OOooOOo / o0oOOo0O0Ooo
 for iII11I1IiiIi in i11I1IiII1i1i :
  Oo0OoO00oOO0o = iII11I1IiiIi . get ( 'title' )
  oo0oO = iII11I1IiiIi . get ( 'subtitle' )
  Oo0O0 = iII11I1IiiIi . get ( 'thumbnail' )
  if 82 - 82: II111iiii % I11i / OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / I1Ii111
  oOo0OOoO0 = { }
  oOo0OOoO0 [ 'plot' ] = Oo0OoO00oOO0o
  if 11 - 11: I1ii11iIi11i . OoO0O00 * IiII * OoooooooOO + ooOoO0o
  if iIiIi11iI == 'vod' :
   iii1i1iiiiIi = { 'mode' : 'DEEP_LIST'
 , 'contentid' : iII11I1IiiIi . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : Oo0OoO00oOO0o
   , 'subtitle' : oo0oO
   , 'thumbnail' : Oo0O0
   , 'viewage' : iII11I1IiiIi . get ( 'viewage' )
 }
   o0o00OO0 = True
   if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
  else :
   iii1i1iiiiIi = { 'mode' : 'MOVIE'
 , 'contentid' : iII11I1IiiIi . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : Oo0OoO00oOO0o
   , 'subtitle' : oo0oO
   , 'thumbnail' : Oo0O0
   , 'viewage' : iII11I1IiiIi . get ( 'viewage' )
 }
   o0o00OO0 = False
   if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
  if iII11I1IiiIi . get ( 'viewage' ) == '21' : oo0oO += ' (%s)' % ( iII11I1IiiIi . get ( 'viewage' ) )
  if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = oo0oO , img = Oo0O0 , infoLabels = oOo0OOoO0 , isFolder = o0o00OO0 , params = iii1i1iiiiIi )
  if 26 - 26: Ii1I % I1ii11iIi11i
 if ooI1111i :
  if 76 - 76: IiII * iII111i
  iii1i1iiiiIi [ 'mode' ] = 'MYVIEW_LIST'
  iii1i1iiiiIi [ 'uicode' ] = iIiIi11iI
  iii1i1iiiiIi [ 'page' ] = str ( Oo0O00O000 + 1 )
  Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
  oo0oO = str ( Oo0O00O000 + 1 )
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = oo0oO , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
  if 52 - 52: OOooOOo
 if len ( i11I1IiII1i1i ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 , cacheToDisc = False )
 if 19 - 19: I1IiiI
 if 25 - 25: Ii1I / ooOoO0o
 if 31 - 31: OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + IiII
 if 71 - 71: I1Ii111 . II111iiii
 if 62 - 62: OoooooooOO . I11i
def oOOOoo00 ( args ) :
 if 9 - 9: O0 % O0 - o0oOOo0O0Ooo
 o00o0 . SaveCredential ( IIiIi11i1 ( ) )
 if 51 - 51: I1IiiI . iIii1I11I1II1 - I1ii11iIi11i / O0
 OOOoO00 = args . get ( 'mode' )
 IIiIi11i1i = args . get ( 'uicode' )
 I1II1I11I1I = args . get ( 'genre' )
 OoOO0o = args . get ( 'subgenre' )
 OOo0oO00ooO00 = args . get ( 'orderby' )
 i1II1 = args . get ( 'ordernm' )
 if 25 - 25: I1Ii111 / iIii1I11I1II1 % iII111i
 if I1II1I11I1I == '-' :
  IiiiiI1i1Iii = o00o0 . GetGenreGroup ( IIiIi11i1i , I1II1I11I1I , OOo0oO00ooO00 , i1II1 , exclusion21 = I1i1iii ( ) )
 else :
  oo00oO0o = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 , 'orderby' : OOo0oO00ooO00
 , 'ordernm' : i1II1
 }
  if 31 - 31: OOooOOo
  IiiiiI1i1Iii = o00o0 . GetGenreGroup_sub ( oo00oO0o )
  if 23 - 23: I1Ii111 . IiII
  if 92 - 92: OoOoOO00 + I1Ii111 * Ii1I % I1IiiI
 for i1I1i1 in IiiiiI1i1Iii :
  Oo0OoO00oOO0o = i1I1i1 . get ( 'title' ) + '  (' + i1II1 + ')'
  if 81 - 81: ooOoO0o - iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * I11i
  iii1i1iiiiIi = { 'mode' : OOOoO00
 , 'uicode' : IIiIi11i1i
  , 'genre' : i1I1i1 . get ( 'genre' )
 , 'subgenre' : i1I1i1 . get ( 'subgenre' )
 , 'adult' : i1I1i1 . get ( 'adult' )
 , 'page' : '1'
 , 'broadcastid' : i1I1i1 . get ( 'broadcastid' )
 , 'contenttype' : i1I1i1 . get ( 'contenttype' )
 , 'uiparent' : i1I1i1 . get ( 'uiparent' )
 , 'uirank' : i1I1i1 . get ( 'uirank' )
 , 'uitype' : i1I1i1 . get ( 'uitype' )
 , 'orderby' : OOo0oO00ooO00
 , 'ordernm' : i1II1
 }
  if 20 - 20: oO0o % IiII
  if IIiIi11i1i == 'moviegenre' or IIiIi11i1i == 'moviegenre_svod' or IIiIi11i1i == 'moviegenre_ppv' or i1I1i1 . get ( 'subgenre' ) != '-' :
   iii1i1iiiiIi [ 'mode' ] = 'GENRE_LIST'
   if 19 - 19: I1ii11iIi11i % IiII + ooOoO0o / I1Ii111 . ooOoO0o
  else :
   if 12 - 12: i1IIi + i1IIi - I1ii11iIi11i * Oo0Ooo % Oo0Ooo - II111iiii
   None
   if 52 - 52: ooOoO0o . iII111i + I1Ii111
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
  if 38 - 38: i1IIi - II111iiii . I1Ii111
 if len ( IiiiiI1i1Iii ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 , cacheToDisc = False )
 if 58 - 58: I1IiiI . iII111i + OoOoOO00
 if 66 - 66: iII111i / oO0o * OoooooooOO + OoooooooOO % I11i
 if 49 - 49: oO0o - i11iIiiIii . I1Ii111 * Ii1I % iII111i + i1IIi
 if 71 - 71: o0oOOo0O0Ooo
def IIIIiIiIi1 ( args ) :
 if 2 - 2: iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
 o00o0 . SaveCredential ( IIiIi11i1 ( ) )
 if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
 IIiIi11i1i = args . get ( 'uicode' )
 Oo0O00O000 = int ( args . get ( 'page' ) )
 if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
 iii1i1iiiiIi = { 'adult' : args . get ( 'adult' )
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
  iii1i1iiiiIi [ 'subgenre' ] = 'all'
  if 79 - 79: O0 * i11iIiiIii - IiII / IiII
 IiiiiI1i1Iii , ooI1111i = o00o0 . GetGenreList ( IIiIi11i1i , iii1i1iiiiIi , Oo0O00O000 )
 if 48 - 48: O0
 if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
 if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
 for i1I1i1 in IiiiiI1i1Iii :
  Oo0OoO00oOO0o = i1I1i1 . get ( 'title' )
  Oo0O0 = i1I1i1 . get ( 'thumbnail' )
  if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
  oOo0OOoO0 = { }
  oOo0OOoO0 [ 'plot' ] = Oo0OoO00oOO0o
  if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
  if IIiIi11i1i == 'vodgenre' :
   I1iiiiIii = { 'mode' : 'DEEP_LIST'
 , 'contentid' : i1I1i1 . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : Oo0OoO00oOO0o
   , 'subtitle' : ''
   , 'thumbnail' : Oo0O0
   , 'viewage' : i1I1i1 . get ( 'viewage' )
 }
   o0o00OO0 = True
   if 19 - 19: OoO0O00 - Oo0Ooo . O0
  else :
   I1iiiiIii = { 'mode' : 'MOVIE'
 , 'contentid' : i1I1i1 . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : Oo0OoO00oOO0o
   , 'subtitle' : ''
   , 'thumbnail' : Oo0O0
   , 'viewage' : i1I1i1 . get ( 'viewage' )
 }
   if 60 - 60: II111iiii + Oo0Ooo
   o0o00OO0 = False
   if 9 - 9: ooOoO0o * OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoO0O00
  if I1iiiiIii . get ( 'viewage' ) == '21' : Oo0OoO00oOO0o += ' (%s)' % ( I1iiiiIii . get ( 'viewage' ) )
  if 49 - 49: II111iiii
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = Oo0O0 , infoLabels = oOo0OOoO0 , isFolder = o0o00OO0 , params = I1iiiiIii )
  if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
 if ooI1111i :
  if 81 - 81: iII111i + IiII
  iii1i1iiiiIi [ 'mode' ] = 'GENRE_LIST'
  iii1i1iiiiIi [ 'uicode' ] = IIiIi11i1i
  iii1i1iiiiIi [ 'page' ] = str ( Oo0O00O000 + 1 )
  Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
  oo0oO = str ( Oo0O00O000 + 1 )
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = oo0oO , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
  if 98 - 98: I1IiiI
 if len ( IiiiiI1i1Iii ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 , cacheToDisc = False )
 if 95 - 95: ooOoO0o / ooOoO0o
 if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
 if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
 if 41 - 41: i1IIi - I11i - Ii1I
def III11I1 ( args ) :
 if 36 - 36: oO0o - Ii1I . Oo0Ooo - i11iIiiIii - OOooOOo * Oo0Ooo
 o00o0 . SaveCredential ( IIiIi11i1 ( ) )
 if 76 - 76: i11iIiiIii + o0oOOo0O0Ooo / I1ii11iIi11i - OoO0O00 - Ii1I + I1ii11iIi11i
 IIiIi11i1i = args . get ( 'uicode' )
 ooI1i = args . get ( 'came' )
 Oo0O00O000 = int ( args . get ( 'page' ) )
 if 32 - 32: OoOoOO00 / OoO0O00 + OOooOOo
 if 32 - 32: iIii1I11I1II1 % iII111i
 if 65 - 65: ooOoO0o . OoooooooOO / I1ii11iIi11i . i1IIi * OoO0O00
 IiIiII1 , ooI1111i = o00o0 . GetDeeplinkList ( IIiIi11i1i , ooI1i , Oo0O00O000 )
 if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
 for OOOO0O00o in IiIiII1 :
  Oo0OoO00oOO0o = OOOO0O00o . get ( 'title' )
  oo0oO = OOOO0O00o . get ( 'subtitle' )
  Oo0O0 = OOOO0O00o . get ( 'thumbnail' )
  ooo = OOOO0O00o . get ( 'uicode' )
  IIiIiI1I = OOOO0O00o . get ( 'channelepg' )
  if 100 - 100: iIii1I11I1II1 + OoOoOO00 / Oo0Ooo . i11iIiiIii
  iii1i1iiiiIi = { 'uicode' : ooo
  , 'came' : ooI1i
 , 'contentid' : OOOO0O00o . get ( 'contentid' )
 , 'contentidType' : OOOO0O00o . get ( 'contentidType' )
 , 'page' : '1'
 , 'title' : Oo0OoO00oOO0o
  , 'subtitle' : oo0oO
  , 'thumbnail' : Oo0O0
  , 'viewage' : OOOO0O00o . get ( 'viewage' )
 }
  if 14 - 14: o0oOOo0O0Ooo * OOooOOo + iII111i + O0 + i11iIiiIii
  if ooo == 'channel' :
   iii1i1iiiiIi [ 'mode' ] = 'LIVE'
  elif ooo == 'movie' :
   iii1i1iiiiIi [ 'mode' ] = 'MOVIE'
  else :
   iii1i1iiiiIi [ 'mode' ] = 'DEEP_LIST'
   if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
   if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
  oOo0OOoO0 = { }
  if IIiIiI1I :
   oOo0OOoO0 [ 'plot' ] = '%s\n\n%s' % ( Oo0OoO00oOO0o , IIiIiI1I )
  else :
   oOo0OOoO0 [ 'plot' ] = '%s\n\n%s' % ( Oo0OoO00oOO0o , oo0oO )
   if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
  if OOOO0O00o . get ( 'viewage' ) == '21' : oo0oO += ' (%s)' % ( OOOO0O00o . get ( 'viewage' ) )
  if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
  if ooo in [ 'channel' , 'movie' ] :
   o0o00OO0 = False
  elif iii1i1iiiiIi [ 'contentidType' ] == 'direct' :
   o0o00OO0 = False
   iii1i1iiiiIi [ 'mode' ] = 'VOD'
  else :
   o0o00OO0 = True
   if 17 - 17: i1IIi
   if 21 - 21: Oo0Ooo
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = oo0oO , img = Oo0O0 , infoLabels = oOo0OOoO0 , isFolder = o0o00OO0 , params = iii1i1iiiiIi )
  if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
 if ooI1111i :
  if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
  iii1i1iiiiIi [ 'mode' ] = 'GN_LIST'
  iii1i1iiiiIi [ 'uicode' ] = IIiIi11i1i
  iii1i1iiiiIi [ 'page' ] = str ( Oo0O00O000 + 1 )
  Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
  oo0oO = str ( Oo0O00O000 + 1 )
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = oo0oO , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
  if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
 if len ( IiIiII1 ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 , cacheToDisc = False )
 if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
 if 54 - 54: i1IIi + II111iiii
 if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
def iIi1Ii1i1iI ( args ) :
 if 16 - 16: OOooOOo / Oo0Ooo / OoooooooOO * I1IiiI + i1IIi % OOooOOo
 o00o0 . SaveCredential ( IIiIi11i1 ( ) )
 if 71 - 71: OoOoOO00
 ii111IiiI1 = args . get ( 'contentid' )
 ii11i1iIiII1 = args . get ( 'contentidType' )
 iIiIi11iI = args . get ( 'uicode' )
 if 63 - 63: OoO0O00
 Oo0O00O000 = int ( args . get ( 'page' ) )
 if 69 - 69: iIii1I11I1II1 . I1ii11iIi11i % ooOoO0o + iIii1I11I1II1 / O0 / I1ii11iIi11i
 O00OoOO0oo0 , ooI1111i = o00o0 . GetEpisodeList ( ii111IiiI1 , iIiIi11iI , ii11i1iIiII1 , Oo0O00O000 , orderby = Ii11Ii1I ( ) )
 if 96 - 96: OoOoOO00 . o0oOOo0O0Ooo - ooOoO0o
 for O0O in O00OoOO0oo0 :
  Oo0OoO00oOO0o = O0O . get ( 'title' )
  oo0oO = O0O . get ( 'subtitle' )
  Oo0O0 = O0O . get ( 'thumbnail' )
  iii1i1iiiiIi = { 'mode' : 'VOD'
 , 'uicode' : O0O . get ( 'uicode' )
  , 'contentid' : O0O . get ( 'contentid' )
 , 'programid' : O0O . get ( 'programid' )
 , 'title' : Oo0OoO00oOO0o
  , 'subtitle' : oo0oO
  , 'thumbnail' : Oo0O0
  , 'viewage' : O0O . get ( 'viewage' )
 }
  if 37 - 37: ooOoO0o % i11iIiiIii % II111iiii . O0 . Ii1I
  if O0O . get ( 'viewage' ) == '21' : oo0oO += ' (%s)' % ( O0O . get ( 'viewage' ) )
  if 51 - 51: OoO0O00 - O0 % oO0o - II111iiii
  I1II = { }
  I1II [ 'plot' ] = O0O . get ( 'synopsis' )
  if 64 - 64: O0 % I11i % O0 * OoO0O00 . oO0o + I1IiiI
  if 75 - 75: I11i . OoooooooOO % o0oOOo0O0Ooo * I11i % OoooooooOO
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = oo0oO , img = Oo0O0 , infoLabels = I1II , isFolder = False , params = iii1i1iiiiIi )
  if 13 - 13: IiII / i11iIiiIii % II111iiii % I11i . I1ii11iIi11i
 if Oo0O00O000 == 1 :
  oOo0OOoO0 = { 'plot' : '정렬순서를 변경합니다.' }
  iii1i1iiiiIi = { }
  iii1i1iiiiIi [ 'mode' ] = 'ORDER_BY'
  if Ii11Ii1I ( ) == 'desc' :
   Oo0OoO00oOO0o = '정렬순서변경 : 최신화부터 -> 1회부터'
   iii1i1iiiiIi [ 'orderby' ] = 'asc'
  else :
   Oo0OoO00oOO0o = '정렬순서변경 : 1회부터 -> 최신화부터'
   iii1i1iiiiIi [ 'orderby' ] = 'desc'
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = oOo0OOoO0 , isFolder = False , params = iii1i1iiiiIi )
  if 8 - 8: OoOoOO00 + Oo0Ooo - II111iiii
 if ooI1111i :
  if 11 - 11: i1IIi % i11iIiiIii - i1IIi * OoOoOO00
  iii1i1iiiiIi [ 'mode' ] = 'DEEP_LIST'
  iii1i1iiiiIi [ 'uicode' ] = iIiIi11iI
  iii1i1iiiiIi [ 'contentid' ] = ii111IiiI1
  iii1i1iiiiIi [ 'contentidType' ] = ii11i1iIiII1
  iii1i1iiiiIi [ 'page' ] = str ( Oo0O00O000 + 1 )
  Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
  oo0oO = str ( Oo0O00O000 + 1 )
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = oo0oO , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
  if 39 - 39: I1Ii111
 if len ( O00OoOO0oo0 ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 , cacheToDisc = False )
 if 86 - 86: I11i * I1IiiI + I11i + II111iiii
 if 8 - 8: I1Ii111 - iII111i / ooOoO0o
 if 96 - 96: OoOoOO00
def IIiiI ( args ) :
 if 31 - 31: I1ii11iIi11i + Ii1I + I1Ii111 / Ii1I
 o00o0 . SaveCredential ( IIiIi11i1 ( ) )
 if 25 - 25: OoO0O00
 ii111IiiI1 = args . get ( 'contentid' )
 iIiIi11iI = args . get ( 'uicode' )
 i11iI11iIiIi = oo ( )
 if 100 - 100: I1Ii111 . o0oOOo0O0Ooo * Oo0Ooo % O0 * O0
 oo0O000OoO ( ii111IiiI1 + ' - ' + iIiIi11iI , False )
 II , Iii1 , Oooo0 , oOO = o00o0 . GetStreamingURL ( ii111IiiI1 , iIiIi11iI , i11iI11iIiIi )
 if 54 - 54: I1IiiI / iIii1I11I1II1 / OOooOOo . OOooOOo % iII111i . I1IiiI
 if 10 - 10: o0oOOo0O0Ooo + OOooOOo
 IIII1i = '%s|Cookie=%s' % ( II , Iii1 )
 oo0O000OoO ( IIII1i , False )
 if 2 - 2: iIii1I11I1II1 * Oo0Ooo % oO0o - II111iiii - iII111i
 if II == '' :
  I11 ( __language__ ( 30303 ) . encode ( 'utf8' ) )
  return
  if 3 - 3: I1Ii111
 i1iiIiI1Ii1i = xbmcgui . ListItem ( path = IIII1i )
 if 22 - 22: IiII / i11iIiiIii
 if Oooo0 :
  if 62 - 62: OoO0O00 / I1ii11iIi11i
  if 7 - 7: OoooooooOO . IiII
  O000OOO0OOo = Oooo0 [ 'customdata' ]
  i1i1I111iIi1 = Oooo0 [ 'drmhost' ]
  if 92 - 92: ooOoO0o
  II11iI111i1 = 'mpd'
  Oo00OoOo = 'com.widevine.alpha'
  if 24 - 24: i11iIiiIii - I1Ii111
  i11iiI1111 = inputstreamhelper . Helper ( II11iI111i1 , drm = Oo00OoOo )
  if 97 - 97: Oo0Ooo * I1IiiI . iIii1I11I1II1
  if i11iiI1111 . check_inputstream ( ) :
   if 16 - 16: ooOoO0o % OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / OoooooooOO
   if iIiIi11iI == 'movie' :
    I11o0oO00oO0o0o0 = 'https://www.wavve.com/player/movie?movieid=%s' % ii111IiiI1
   else :
    I11o0oO00oO0o0o0 = 'https://www.wavve.com/player/vod?programid=%s&page=1' % ii111IiiI1
    if 17 - 17: I11i . IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
   I1IIIiI1I1ii1 = { 'content-type' : 'application/octet-stream'
 , 'origin' : 'https://www.wavve.com'
 , 'pallycon-customdata' : O000OOO0OOo
 , 'referer' : I11o0oO00oO0o0o0
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'

   , 'user-agent' : OOoO
 }
   iiiI1I1iIIIi1 = i1i1I111iIi1 + '|' + urllib . urlencode ( I1IIIiI1I1ii1 ) + '|R{SSM}|'
   if 17 - 17: iIii1I11I1II1 . OoooooooOO / I11i % II111iiii % i1IIi / i11iIiiIii
   i1iiIiI1Ii1i . setProperty ( 'inputstreamaddon' , i11iiI1111 . inputstream_addon )
   i1iiIiI1Ii1i . setProperty ( 'inputstream.adaptive.manifest_type' , II11iI111i1 )
   i1iiIiI1Ii1i . setProperty ( 'inputstream.adaptive.license_type' , Oo00OoOo )
   if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
   i1iiIiI1Ii1i . setProperty ( 'inputstream.adaptive.license_key' , iiiI1I1iIIIi1 )
   i1iiIiI1Ii1i . setProperty ( 'inputstream.adaptive.stream_headers' , 'Cookie=%s' % Iii1 )
   if 85 - 85: OoOoOO00 + OOooOOo
 xbmcplugin . setResolvedUrl ( Oo0o00 , True , i1iiIiI1Ii1i )
 if 10 - 10: IiII / OoO0O00 + OoOoOO00 / i1IIi
 if oOO :
  I11 ( oOO . encode ( 'utf-8' ) )
 else :
  if '/preview.' in urlparse . urlsplit ( II ) . path : I11 ( __language__ ( 30401 ) . encode ( 'utf8' ) )
  if 27 - 27: Ii1I
 if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) and args . get ( 'viewage' ) != '21' :
  iii1i1iiiiIi = { 'code' : args . get ( 'programid' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'contentid' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 , 'subtitle' : args . get ( 'subtitle' )
 }
  oO0OO0 ( args . get ( 'mode' ) . lower ( ) , iii1i1iiiiIi )
  if 82 - 82: IiII - IiII + OoOoOO00
  if 8 - 8: o0oOOo0O0Ooo % iII111i * oO0o % Ii1I . ooOoO0o / ooOoO0o
  if 81 - 81: OoO0O00
  if 99 - 99: oO0o * II111iiii * I1Ii111
def oOooO0 ( args ) :
 I1II1I11I1I = args . get ( 'genre' )
 if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111
 if I1II1I11I1I == '-' :
  Oo0OoO00oOO0o = 'VOD 시청내역'
  iii1i1iiiiIi = { 'mode' : 'WATCH'
 , 'genre' : 'vod'
 }
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
  if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
  Oo0OoO00oOO0o = '영화 시청내역'
  iii1i1iiiiIi [ 'genre' ] = 'movie'
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
  if 61 - 61: II111iiii
  xbmcplugin . endOfDirectory ( Oo0o00 )
  if 15 - 15: i11iIiiIii % I1IiiI * I11i / I1Ii111
 else :
  oooO0o0o0O0 = iii11111I ( I1II1I11I1I )
  if 16 - 16: iIii1I11I1II1 - IiII
  for o00o in oooO0o0o0O0 :
   Ii1IIiiIIi = dict ( urlparse . parse_qsl ( o00o ) )
   if 88 - 88: OoooooooOO + I11i * II111iiii % Oo0Ooo
   Oo0OoO00oOO0o = Ii1IIiiIIi . get ( 'title' ) . strip ( )
   oo0oO = Ii1IIiiIIi . get ( 'subtitle' ) . strip ( )
   if oo0oO == 'None' : oo0oO = ''
   Oo0O0 = Ii1IIiiIIi . get ( 'img' )
   if 17 - 17: IiII * OOooOOo - OoO0O00 / i11iIiiIii
   oOo0OOoO0 = { }
   oOo0OOoO0 [ 'plot' ] = '%s\n%s' % ( Oo0OoO00oOO0o , oo0oO )
   if 79 - 79: I1Ii111 . oO0o - II111iiii . I1IiiI % ooOoO0o
   if I1II1I11I1I == 'vod' :
    iii1i1iiiiIi = { 'mode' : 'DEEP_LIST'
 , 'contentid' : Ii1IIiiIIi . get ( 'code' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
    o0o00OO0 = True
   else :
    iii1i1iiiiIi = { 'mode' : 'MOVIE'
 , 'contentid' : Ii1IIiiIIi . get ( 'code' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'title' : Oo0OoO00oOO0o
 , 'thumbnail' : Oo0O0
 }
    o0o00OO0 = False
    if 65 - 65: I1IiiI + OoOoOO00 / OOooOOo
   iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = oo0oO , img = Oo0O0 , infoLabels = oOo0OOoO0 , isFolder = o0o00OO0 , params = iii1i1iiiiIi )
   if 83 - 83: o0oOOo0O0Ooo . iII111i - Oo0Ooo
  oOo0OOoO0 = { 'plot' : '시청목록을 삭제합니다.' }
  Oo0OoO00oOO0o = '*** 시청목록 삭제 ***'
  iii1i1iiiiIi = { 'mode' : 'MYVIEW_REMOVE'
 , 'genre' : I1II1I11I1I
 }
  if 65 - 65: iIii1I11I1II1 / ooOoO0o . IiII - II111iiii
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = oOo0OOoO0 , isFolder = False , params = iii1i1iiiiIi )
  if 72 - 72: iIii1I11I1II1 / IiII % iII111i % OOooOOo - I11i % OOooOOo
  xbmcplugin . endOfDirectory ( Oo0o00 , cacheToDisc = False )
  if 100 - 100: Oo0Ooo + i11iIiiIii
  if 71 - 71: I11i / o0oOOo0O0Ooo / I1Ii111 % OOooOOo
  if 51 - 51: IiII * O0 / II111iiii . Ii1I % OOooOOo / I1IiiI
  if 9 - 9: I1IiiI % I1IiiI % II111iiii
  if 30 - 30: IiII + I1Ii111 - IiII . IiII - II111iiii + O0
def oOO0 ( args ) :
 Oo0OoO00oOO0o = 'VOD 검색'
 iii1i1iiiiIi = { 'mode' : 'SEARCH_LIST'
 , 'genre' : 'vod'
 , 'page' : '1'
 }
 iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
 if 46 - 46: Ii1I % OoOoOO00
 Oo0OoO00oOO0o = '영화 검색'
 iii1i1iiiiIi [ 'genre' ] = 'movie'
 iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
 if 64 - 64: i11iIiiIii - II111iiii
 xbmcplugin . endOfDirectory ( Oo0o00 )
 if 77 - 77: OoOoOO00 % Ii1I
 if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
 if 2 - 2: OoooooooOO % OOooOOo
 if 63 - 63: I1IiiI % iIii1I11I1II1
def I1ii ( args ) :
 if 73 - 73: IiII + I1IiiI * Oo0Ooo * OoooooooOO
 o00o0 . SaveCredential ( IIiIi11i1 ( ) )
 if 95 - 95: i1IIi + iIii1I11I1II1 % I1ii11iIi11i % Oo0Ooo / i11iIiiIii - IiII
 iIiIi11iI = args . get ( 'genre' )
 Oo0O00O000 = int ( args . get ( 'page' ) )
 if 26 - 26: ooOoO0o . OOooOOo - OOooOOo . OoO0O00
 if 'search_key' in args :
  Ii1IiII = args . get ( 'search_key' )
 else :
  Ii1IiII = oo0Ooo0 ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
  if not Ii1IiII : return
  if 27 - 27: iII111i . I11i . iIii1I11I1II1 . iIii1I11I1II1
 iIi1i , ooI1111i = o00o0 . GetSearchList ( Ii1IiII , iIiIi11iI , Oo0O00O000 , exclusion21 = I1i1iii ( ) )
 if 4 - 4: I1Ii111 / i11iIiiIii / OOooOOo
 for OooO0ooo0o in iIi1i :
  Oo0OoO00oOO0o = OooO0ooo0o . get ( 'title' )
  Oo0O0 = OooO0ooo0o . get ( 'thumbnail' )
  if 47 - 47: OoooooooOO
  oOo0OOoO0 = { }
  oOo0OOoO0 [ 'plot' ] = Oo0OoO00oOO0o
  if 4 - 4: I1IiiI % I11i
  if iIiIi11iI == 'vod' :
   iii1i1iiiiIi = { 'mode' : 'DEEP_LIST'
 , 'contentid' : OooO0ooo0o . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : Oo0OoO00oOO0o
   , 'subtitle' : ''
   , 'thumbnail' : Oo0O0
   , 'viewage' : OooO0ooo0o . get ( 'viewage' )
 }
   o0o00OO0 = True
   if 10 - 10: IiII . OoooooooOO - OoO0O00 + IiII - O0
  else :
   iii1i1iiiiIi = { 'mode' : 'MOVIE'
 , 'contentid' : OooO0ooo0o . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : Oo0OoO00oOO0o
   , 'subtitle' : ''
   , 'thumbnail' : Oo0O0
   , 'viewage' : OooO0ooo0o . get ( 'viewage' )
 }
   if 82 - 82: ooOoO0o + II111iiii
   o0o00OO0 = False
   if 39 - 39: oO0o % iIii1I11I1II1 % O0 % OoooooooOO * I1ii11iIi11i + iII111i
  if iii1i1iiiiIi . get ( 'viewage' ) == '21' : Oo0OoO00oOO0o += ' (%s)' % ( iii1i1iiiiIi . get ( 'viewage' ) )
  if 68 - 68: Oo0Ooo + i11iIiiIii
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = '' , img = Oo0O0 , infoLabels = oOo0OOoO0 , isFolder = o0o00OO0 , params = iii1i1iiiiIi )
  if 69 - 69: iIii1I11I1II1 * iIii1I11I1II1 * i11iIiiIii + I1IiiI / OOooOOo % Ii1I
 if ooI1111i :
  if 58 - 58: OOooOOo * o0oOOo0O0Ooo + O0 % OOooOOo
  iii1i1iiiiIi [ 'mode' ] = 'SEARCH_LIST'
  iii1i1iiiiIi [ 'genre' ] = iIiIi11iI
  iii1i1iiiiIi [ 'page' ] = str ( Oo0O00O000 + 1 )
  iii1i1iiiiIi [ 'search_key' ] = Ii1IiII
  Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
  oo0oO = str ( Oo0O00O000 + 1 )
  iI1ii1Ii ( Oo0OoO00oOO0o , sublabel = oo0oO , img = '' , infoLabels = None , isFolder = True , params = iii1i1iiiiIi )
  if 25 - 25: Oo0Ooo % I1ii11iIi11i * ooOoO0o
 if len ( iIi1i ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 )
 if 6 - 6: iII111i . IiII * OoOoOO00 . i1IIi
 if 98 - 98: i1IIi
 if 65 - 65: OoOoOO00 / OoO0O00 % IiII
 if 45 - 45: OoOoOO00
 if 66 - 66: OoO0O00
def iii11111I ( genre ) :
 try :
  oOOI11I = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  with open ( oOOI11I , 'r' ) as iIIII1i :
   o00oO0 = iIIII1i . readlines ( )
 except :
  o00oO0 = [ ]
  if 5 - 5: iIii1I11I1II1
 return o00oO0
 if 72 - 72: oO0o . I1Ii111 / OoOoOO00 + I11i % iIii1I11I1II1
 if 42 - 42: I1ii11iIi11i * OoOoOO00 % ooOoO0o - OoOoOO00 . i11iIiiIii - I1Ii111
 if 84 - 84: I1Ii111 - I1ii11iIi11i / I11i
 if 13 - 13: IiII - Oo0Ooo - ooOoO0o
def oO0OO0 ( genre , in_params ) :
 try :
  oOOI11I = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  O00Oo = iii11111I ( genre )
  if 42 - 42: II111iiii % IiII % I1Ii111 % i1IIi - oO0o
  with open ( oOOI11I , 'w' ) as iIIII1i :
   i1I1I1iiII = urllib . urlencode ( in_params )
   i1I1I1iiII = i1I1I1iiII . encode ( 'utf-8' ) + '\n'
   iIIII1i . write ( i1I1I1iiII )
   if 58 - 58: I11i + II111iiii * iII111i * i11iIiiIii - iIii1I11I1II1
   oooo00o0o0o = 0
   for O0Oo00oO0O00 in O00Oo :
    Ii = dict ( urlparse . parse_qsl ( O0Oo00oO0O00 ) )
    if in_params . get ( 'code' ) != Ii . get ( 'code' ) :
     iIIII1i . write ( O0Oo00oO0O00 )
     oooo00o0o0o += 1
     if oooo00o0o0o >= 50 : break
 except :
  None
  if 63 - 63: iII111i * I11i * Ii1I - oO0o - Ii1I
  if 97 - 97: OOooOOo / OoooooooOO
  if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
  if 71 - 71: OoooooooOO
def iIIIII1iiiiII ( genre ) :
 try :
  oOOI11I = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  with open ( oOOI11I , 'w' ) as iIIII1i :
   iIIII1i . write ( '' )
 except :
  None
  if 54 - 54: i1IIi
  if 22 - 22: i1IIi + Ii1I
  if 54 - 54: ooOoO0o % OOooOOo . I1Ii111 + oO0o - OOooOOo * I1IiiI
  if 92 - 92: o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % OoO0O00 % IiII . OoooooooOO
def O0Oo ( args ) :
 I1II1I11I1I = args . get ( 'genre' )
 if 7 - 7: IiII % iIii1I11I1II1 + I11i - Ii1I * oO0o
 Oo0o0000o0o0 = xbmcgui . Dialog ( )
 O0i1II1Iiii1I11 = Oo0o0000o0o0 . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
 if O0i1II1Iiii1I11 == False : sys . exit ( )
 if 94 - 94: OoOoOO00 . O0 / Ii1I . I1ii11iIi11i - i1IIi
 iIIIII1iiiiII ( I1II1I11I1I )
 if 26 - 26: OoO0O00 - OOooOOo . o0oOOo0O0Ooo
 xbmc . executebuiltin ( "Container.Refresh" )
 if 65 - 65: I1ii11iIi11i % O0 % iIii1I11I1II1 * Ii1I
 if 31 - 31: Ii1I
 if 44 - 44: OoOoOO00 - iIii1I11I1II1 - Oo0Ooo
 if 80 - 80: iIii1I11I1II1 * I1Ii111 % I11i % Oo0Ooo
 if 95 - 95: iIii1I11I1II1 - I1ii11iIi11i . I1Ii111 - I1IiiI
 if 75 - 75: OoO0O00 + o0oOOo0O0Ooo - i1IIi . OoooooooOO * Ii1I / IiII
 if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / OOooOOo
 if 11 - 11: I1IiiI * oO0o + I1ii11iIi11i / I1ii11iIi11i
 if 37 - 37: i11iIiiIii + i1IIi
 if 23 - 23: iII111i + I11i . OoOoOO00 * I1IiiI + I1ii11iIi11i
 if 18 - 18: IiII * o0oOOo0O0Ooo . IiII / O0
o00o0 = O0OoOoo00o ( )
Oo0o00 = int ( sys . argv [ 1 ] )
if 8 - 8: o0oOOo0O0Ooo
if 4 - 4: I1ii11iIi11i + I1ii11iIi11i * ooOoO0o - OoOoOO00
if 78 - 78: Ii1I / II111iiii % OoOoOO00
if 52 - 52: OOooOOo - iII111i * oO0o
iii1i1iiiiIi = IIii1Ii1 ( )
OOOoO00 = iii1i1iiiiIi . get ( 'mode' , None )
if 17 - 17: OoooooooOO + OOooOOo * I11i * OoOoOO00
OOOooOO0 ( )
if OOOoO00 is None :
 if 36 - 36: O0 + Oo0Ooo
 i11I1iIiII ( )
 if 5 - 5: Oo0Ooo * OoOoOO00
 if 46 - 46: ooOoO0o
 if 33 - 33: iII111i - II111iiii * OoooooooOO - Oo0Ooo - OOooOOo
 if 84 - 84: I1Ii111 + Oo0Ooo - OoOoOO00 * OoOoOO00
 if 61 - 61: OoooooooOO . oO0o . OoooooooOO / Oo0Ooo
 if 72 - 72: i1IIi
 if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i . OoooooooOO
 if 63 - 63: I1ii11iIi11i
 if 6 - 6: ooOoO0o / I1ii11iIi11i
elif OOOoO00 == 'GNB_LIST' :
 oOO00O ( iii1i1iiiiIi )
 if 57 - 57: I11i
elif OOOoO00 == 'GN_LIST' :
 III11I1 ( iii1i1iiiiIi )
 if 67 - 67: OoO0O00 . ooOoO0o
elif OOOoO00 == 'DEEP_LIST' :
 iIiIi11iI = iii1i1iiiiIi . get ( 'uicode' , None )
 if 87 - 87: oO0o % Ii1I
 if iIiIi11iI in [ 'quick' , 'vod' , 'program' , 'x' ] :
  iIi1Ii1i1iI ( iii1i1iiiiIi )
  if 83 - 83: II111iiii - I11i
 else : None
 if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
elif OOOoO00 in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
 IIiiI ( iii1i1iiiiIi )
 xbmc . sleep ( 200 )
 if 86 - 86: iIii1I11I1II1 + OoOoOO00 . i11iIiiIii - Ii1I
elif OOOoO00 == 'GN_MYVIEW' :
 ooiIi1 ( iii1i1iiiiIi )
 if 51 - 51: OoOoOO00
elif OOOoO00 == 'MYVIEW_LIST' :
 iiIiI1i1 ( iii1i1iiiiIi )
 if 14 - 14: IiII % oO0o % Oo0Ooo - i11iIiiIii
elif OOOoO00 == 'GENRE' :
 oOOOoo00 ( iii1i1iiiiIi )
 if 53 - 53: Ii1I % Oo0Ooo
elif OOOoO00 == 'GENRE_LIST' :
 IIIIiIiIi1 ( iii1i1iiiiIi )
 if 59 - 59: OOooOOo % iIii1I11I1II1 . i1IIi + II111iiii * IiII
elif OOOoO00 == 'WATCH' :
 oOooO0 ( iii1i1iiiiIi )
 if 41 - 41: Ii1I % I1ii11iIi11i
elif OOOoO00 == 'MYVIEW_REMOVE' :
 O0Oo ( iii1i1iiiiIi )
 if 12 - 12: OOooOOo
elif OOOoO00 == 'SEARCH' :
 oOO0 ( iii1i1iiiiIi )
 if 69 - 69: OoooooooOO + OOooOOo
elif OOOoO00 == 'SEARCH_LIST' :
 I1ii ( iii1i1iiiiIi )
 if 26 - 26: Oo0Ooo + OOooOOo / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
elif OOOoO00 == 'ORDER_BY' :
 I1i1Iiiii ( iii1i1iiiiIi )
 if 31 - 31: I11i % OOooOOo * I11i
else :
 None
 if 45 - 45: i1IIi . I1IiiI + OOooOOo - OoooooooOO % ooOoO0o
 if 1 - 1: iIii1I11I1II1
 if 93 - 93: i1IIi . i11iIiiIii . Oo0Ooo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
