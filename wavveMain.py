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
 , { 'title' : '영화(Movie)' , 'uicode' : 'GN4' , 'came' : 'movie' }
 , { 'title' : '해외시리즈' , 'uicode' : 'GN12' , 'came' : 'global' }

, { 'title' : '분류별 탐색 --- 방송(VOD)' , 'uicode' : 'GENRE' , 'came' : 'vodgenre' }
 , { 'title' : '분류별 탐색 --- 영화(wavvie)' , 'uicode' : 'GENRE' , 'came' : 'moviegenre' }

, { 'title' : '검색' , 'uicode' : 'SEARCH' , 'came' : '-' }
 , { 'title' : 'Watched(시청목록)' , 'uicode' : 'WATCH' , 'came' : '-' }
 ]
oo00 = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
if 88 - 88: iII111i . oO0o % ooOoO0o
from wavveCore import *
if 66 - 66: iII111i
if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - oO0o
def ooO00oOoo ( sting ) :
 try :
  O0OOo = xbmcgui . Dialog ( )
  if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1 . IiII / IiII % IiII
  O0OOo . notification ( __addonname__ , sting )
 except :
  None
  if 22 - 22: Ii1I . IiII
  if 41 - 41: I1Ii111 . ooOoO0o * IiII % i11iIiiIii
  if 74 - 74: iII111i * IiII
def oo00o0Oo0oo ( string , isDebug = False ) :
 try :
  i1iII1I1i1i1 = string . encode ( 'utf-8' , 'ignore' )
 except :
  i1iII1I1i1i1 = 'addonException: addon_log'
 if isDebug : i1iIIII = xbmc . LOGDEBUG
 else : i1iIIII = xbmc . LOGNOTICE
 xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , i1iII1I1i1i1 ) , level = i1iIIII )
 if 26 - 26: I1Ii111 . I11i - OOooOOo % O0 + OOooOOo
 if 34 - 34: I11i * I1IiiI
 if 31 - 31: II111iiii + OoO0O00 . I1Ii111
 if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
def IiiIII111ii ( title ) :
 i1iIIi1 = None
 ii11iIi1I = xbmc . Keyboard ( )
 ii11iIi1I . setHeading ( title )
 xbmc . sleep ( 1000 )
 ii11iIi1I . doModal ( )
 if ( ii11iIi1I . isConfirmed ( ) ) :
  i1iIIi1 = ii11iIi1I . getText ( )
 return i1iIIi1
 if 6 - 6: OoOoOO00 * iII111i
 if 67 - 67: ooOoO0o - oO0o * o0oOOo0O0Ooo % o0oOOo0O0Ooo % I11i * OoOoOO00
 if 26 - 26: Ii1I - o0oOOo0O0Ooo
 if 63 - 63: II111iiii . II111iiii
def Ii1 ( ) :
 oOOoO0 = __addon__ . getSetting ( 'id' )
 O0OoO000O0OO = __addon__ . getSetting ( 'pw' )
 iiI1IiI = __addon__ . getSetting ( 'selected_profile' )
 return ( oOOoO0 , O0OoO000O0OO , iiI1IiI )
 if 13 - 13: Oo0Ooo . i11iIiiIii - iIii1I11I1II1 - OoOoOO00
 if 6 - 6: I1IiiI / Oo0Ooo % Ii1I
 if 84 - 84: i11iIiiIii . o0oOOo0O0Ooo
def o0O00oooo ( ) :
 O00o = __addon__ . getSetting ( 'exclusion21' )
 if O00o == 'false' :
  return False
 else :
  return True
  if 61 - 61: iII111i . iIii1I11I1II1 * I1IiiI . ooOoO0o % Oo0Ooo
  if 72 - 72: OOooOOo
  if 63 - 63: Ii1I
def O00 ( credential ) :
 iII11i = xbmcgui . Window ( 10000 )
 iII11i . setProperty ( 'WAVVE_M_CREDENTIAL' , credential )
 if 97 - 97: I11i % I11i + II111iiii * iII111i
 iII11i . setProperty ( 'WAVVE_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
 if 54 - 54: I11i + IiII / iII111i
def IIII ( ) :
 iII11i = xbmcgui . Window ( 10000 )
 return iII11i . getProperty ( 'WAVVE_M_CREDENTIAL' )
 if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
def III1ii1iII ( orderby ) :
 iII11i = xbmcgui . Window ( 10000 )
 iII11i . setProperty ( 'WAVVE_M_ORDERBY' , orderby )
 if 54 - 54: I1IiiI % II111iiii % II111iiii
def iI1 ( ) :
 iII11i = xbmcgui . Window ( 10000 )
 return iII11i . getProperty ( 'WAVVE_M_ORDERBY' )
 if 19 - 19: I11i + ooOoO0o
 if 53 - 53: OoooooooOO . i1IIi
 if 18 - 18: o0oOOo0O0Ooo
def I1i1I1II ( ) :
 i1 = urlparse . parse_qs ( sys . argv [ 2 ] [ 1 : ] )
 for IiIiiI in i1 . keys ( ) :
  i1 [ IiIiiI ] = i1 [ IiIiiI ] [ 0 ]
 return i1
 if 31 - 31: Ii1I . Ii1I - o0oOOo0O0Ooo / OoO0O00 + ooOoO0o * I1IiiI
 if 63 - 63: I1Ii111 % i1IIi / OoooooooOO - OoooooooOO
 if 8 - 8: OoOoOO00
def o00O ( label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
 if 69 - 69: oO0o % I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - O0 % OoooooooOO
 Iii111II = '%s?%s' % ( sys . argv [ 0 ] , urllib . urlencode ( params ) )
 if 9 - 9: OoO0O00
 if sublabel : i11 = '%s < %s >' % ( label , sublabel )
 else : i11 = label
 if not img : img = 'DefaultFolder.png'
 if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
 ii11i1 = xbmcgui . ListItem ( i11 , thumbnailImage = img )
 if infoLabels : ii11i1 . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder : ii11i1 . setProperty ( 'IsPlayable' , 'true' )
 if 29 - 29: I1ii11iIi11i % I1IiiI + ooOoO0o / o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
 xbmcplugin . addDirectoryItem ( i1I1iI , Iii111II , ii11i1 , isFolder )
 if 93 - 93: iIii1I11I1II1 % oO0o * i1IIi
 if 16 - 16: O0 - I1Ii111 * iIii1I11I1II1 + iII111i
 if 50 - 50: II111iiii - ooOoO0o * I1ii11iIi11i / I1Ii111 + o0oOOo0O0Ooo
def O0O0O ( ) :
 try :
  oO0Oo = [ 1080 , 720 , 480 , 360 ]
  if 54 - 54: o0oOOo0O0Ooo - I1IiiI + OoooooooOO
  O0o0 = int ( __addon__ . getSetting ( 'selected_quality' ) )
  return oO0Oo [ O0o0 ]
 except :
  None
  if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
 return 1080
 if 88 - 88: OoOoOO00 - OoO0O00 % OOooOOo
 if 16 - 16: I1IiiI * oO0o % IiII
 if 86 - 86: I1IiiI + Ii1I % i11iIiiIii * oO0o . ooOoO0o * I11i
def i1I11i1iI ( ) :
 if 15 - 15: Ii1I - O0 / oO0o * i1IIi
 for oooo000 in o0oO0 :
  i11 = oooo000 . get ( 'title' )
  if 16 - 16: I1ii11iIi11i + OoO0O00 - II111iiii
  if oooo000 . get ( 'uicode' ) == 'GENRE' :
   oOoOO0 = { 'mode' : 'GENRE'
 , 'uicode' : oooo000 . get ( 'came' )
   , 'genre' : '-'
 , 'subgenre' : '-'
   }
  elif oooo000 . get ( 'uicode' ) == 'WATCH' :
   oOoOO0 = { 'mode' : 'WATCH'
 , 'genre' : '-'
 }
  elif oooo000 . get ( 'uicode' ) == 'SEARCH' :
   oOoOO0 = { 'mode' : 'SEARCH'
 , 'genre' : '-'
 }
  else :
   oOoOO0 = { 'mode' : 'GNB_LIST'
 , 'uicode' : oooo000 . get ( 'uicode' )
 , 'came' : oooo000 . get ( 'came' )
 }
   if 30 - 30: II111iiii - OOooOOo - i11iIiiIii % OoOoOO00 - II111iiii * Ii1I
  oO00O0O0O = True
  if 31 - 31: I11i - II111iiii . I11i
  if oooo000 . get ( 'uicode' ) == 'XXX' :
   oOoOO0 [ 'mode' ] = 'XXX'
   oO00O0O0O = False
   if 18 - 18: o0oOOo0O0Ooo
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = oO00O0O0O , params = oOoOO0 )
 if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI )
 if 98 - 98: iII111i * iII111i / iII111i + I11i
 if 34 - 34: ooOoO0o
 if 15 - 15: I11i * ooOoO0o * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
 if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
def o0 ( ) :
 ( oo0oOo , o000O0o , iI1iII1 ) = Ii1 ( )
 if 86 - 86: OOooOOo
 if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
 if 25 - 25: I1ii11iIi11i
 if 7 - 7: i1IIi / I1IiiI * I1Ii111 . IiII . iIii1I11I1II1
 if 13 - 13: OOooOOo / i11iIiiIii
 if not ( oo0oOo and o000O0o ) :
  O0OOo = xbmcgui . Dialog ( )
  Iiii = O0OOo . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
  if Iiii == True :
   __addon__ . openSettings ( )
   sys . exit ( )
   if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . I1Ii111
   if 5 - 5: o0oOOo0O0Ooo * ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
 if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINWAIT' ) == 'TRUE' :
  oO = 0
  while True :
   oO += 1
   xbmc . sleep ( 250 )
   if xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINWAIT' ) == 'FALSE' or oO > 500 :
    break
    if 7 - 7: o0oOOo0O0Ooo - I1IiiI
 OOo00O0 = xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINTIME' )
 if 73 - 73: i1IIi + I1IiiI
 if OOo00O0 != '' :
  if 46 - 46: OoO0O00 . Oo0Ooo - OoooooooOO
  if OOo00O0 == datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) :
   if 93 - 93: iII111i
   if 10 - 10: I11i
   if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
   if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
   if 37 - 37: iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
   if 83 - 83: I11i / I1IiiI
   if 34 - 34: IiII
   if 57 - 57: oO0o . I11i . i1IIi
   if 42 - 42: I11i + I1ii11iIi11i % O0
   if 6 - 6: oO0o
   if 68 - 68: OoOoOO00 - OoO0O00
   return
   if 28 - 28: OoO0O00 . OOooOOo / OOooOOo + Oo0Ooo . I1ii11iIi11i
 xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'TRUE' )
 if 1 - 1: iIii1I11I1II1 / II111iiii
 if 33 - 33: I11i
 if not iI11i1ii11 . GetCredential ( oo0oOo , o000O0o , iI1iII1 ) :
  ooO00oOoo ( __language__ ( 30103 ) . encode ( 'utf8' ) )
  xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
  sys . exit ( )
  if 58 - 58: OoO0O00 % i11iIiiIii . iII111i / oO0o
  if 84 - 84: iII111i . I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / o0oOOo0O0Ooo
 O00 ( iI11i1ii11 . LoadCredential ( ) )
 III1ii1iII ( 'desc' )
 xbmcgui . Window ( 10000 ) . setProperty ( 'WAVVE_M_LOGINWAIT' , 'FALSE' )
 if 12 - 12: I1IiiI * iII111i % i1IIi % iIii1I11I1II1
 if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
 if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
 if 51 - 51: O0 + iII111i
def IIIII11I1IiI ( args ) :
 i1I = args . get ( 'orderby' )
 if 72 - 72: i1IIi / OoO0O00 + OoooooooOO - Oo0Ooo
 III1ii1iII ( i1I )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 29 - 29: I1ii11iIi11i + oO0o % O0
 if 10 - 10: I11i / I1Ii111 - I1IiiI * iIii1I11I1II1 - I1IiiI
 if 97 - 97: I1ii11iIi11i + I1IiiI * Ii1I + OOooOOo % iII111i
 if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
def i1I1iI1iIi111i ( args ) :
 if 44 - 44: i1IIi % II111iiii + I11i
 iI11i1ii11 . SaveCredential ( IIII ( ) )
 if 45 - 45: iII111i / iII111i + I1Ii111 + ooOoO0o
 iI111i = iI11i1ii11 . GetGnList ( args . get ( 'uicode' ) )
 if 26 - 26: I1ii11iIi11i * iII111i . II111iiii * Ii1I
 if 28 - 28: OoO0O00 . i1IIi * I1IiiI + O0 . i1IIi - ooOoO0o
 if 38 - 38: I1Ii111
 if 84 - 84: iIii1I11I1II1 % iII111i / iIii1I11I1II1 % I11i
 for ii in iI111i :
  i11 = ii . get ( 'title' )
  oOoOO0 = { 'mode' : 'GN_LIST' if ii . get ( 'uicode' ) != 'CY1' else 'GN_MYVIEW'
  , 'uicode' : ii . get ( 'uicode' )
 , 'came' : args . get ( 'came' )
 , 'page' : '1'
 }
  if 84 - 84: o0oOOo0O0Ooo % II111iiii . i11iIiiIii / OoO0O00
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if len ( iI111i ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 80 - 80: I1Ii111 . i11iIiiIii - o0oOOo0O0Ooo
 if 25 - 25: OoO0O00
 if 62 - 62: OOooOOo + O0
 if 98 - 98: o0oOOo0O0Ooo
def OOOO0oo0 ( args ) :
 i11 = 'VOD 시청내역'
 oOoOO0 = { 'mode' : 'MYVIEW_LIST'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
 o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
 i11 = '영화 시청내역'
 oOoOO0 [ 'uicode' ] = 'movie'
 o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if 47 - 47: iII111i - Ii1I . II111iiii + OoooooooOO . i11iIiiIii
 xbmcplugin . endOfDirectory ( i1I1iI )
 if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
 if 87 - 87: Oo0Ooo . IiII
 if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
 if 55 - 55: OOooOOo . I1IiiI
def oOo0O0o00o ( args ) :
 if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
 iI11i1ii11 . SaveCredential ( IIII ( ) )
 if 79 - 79: O0
 oOO00O = args . get ( 'uicode' )
 OOOoo0OO = int ( args . get ( 'page' ) )
 oO0o0 , iI1Ii11iIiI1 = iI11i1ii11 . GetMyviewList ( oOO00O , OOOoo0OO )
 if 86 - 86: oO0o * o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
 for oOOoo00O00o in oO0o0 :
  i11 = oOOoo00O00o . get ( 'title' )
  O0O00Oo = oOOoo00O00o . get ( 'subtitle' )
  oooooo0O000o = oOOoo00O00o . get ( 'thumbnail' )
  if 64 - 64: I1IiiI . o0oOOo0O0Ooo - I1Ii111 / OoooooooOO
  O0O0ooOOO = { }
  O0O0ooOOO [ 'plot' ] = i11
  if 77 - 77: OoOoOO00 - II111iiii - ooOoO0o
  if oOO00O == 'vod' :
   oOoOO0 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : oOOoo00O00o . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : O0O00Oo
   , 'thumbnail' : oooooo0O000o
   , 'viewage' : oOOoo00O00o . get ( 'viewage' )
 }
   oO00O0O0O = True
   if 49 - 49: II111iiii % O0 . OoOoOO00 + oO0o / I1IiiI
  else :
   oOoOO0 = { 'mode' : 'MOVIE'
 , 'contentid' : oOOoo00O00o . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : O0O00Oo
   , 'thumbnail' : oooooo0O000o
   , 'viewage' : oOOoo00O00o . get ( 'viewage' )
 }
   oO00O0O0O = False
   if 72 - 72: ooOoO0o * Oo0Ooo . I1IiiI - II111iiii + i1IIi
  if oOOoo00O00o . get ( 'viewage' ) == '21' : O0O00Oo += ' (%s)' % ( oOOoo00O00o . get ( 'viewage' ) )
  if 10 - 10: oO0o + i1IIi
  o00O ( i11 , sublabel = O0O00Oo , img = oooooo0O000o , infoLabels = O0O0ooOOO , isFolder = oO00O0O0O , params = oOoOO0 )
  if 87 - 87: I1IiiI
 if iI1Ii11iIiI1 :
  if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
  oOoOO0 [ 'mode' ] = 'MYVIEW_LIST'
  oOoOO0 [ 'uicode' ] = oOO00O
  oOoOO0 [ 'page' ] = str ( OOOoo0OO + 1 )
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  O0O00Oo = str ( OOOoo0OO + 1 )
  o00O ( i11 , sublabel = O0O00Oo , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 50 - 50: I1Ii111 . o0oOOo0O0Ooo
 if len ( oO0o0 ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 97 - 97: O0 + OoOoOO00
 if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
 if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
 if 77 - 77: OOooOOo * iIii1I11I1II1
 if 98 - 98: I1IiiI % Ii1I * OoooooooOO
def Oo ( args ) :
 if 34 - 34: oO0o + I1IiiI - oO0o
 iI11i1ii11 . SaveCredential ( IIII ( ) )
 if 17 - 17: II111iiii % iII111i + I11i - iII111i / OOooOOo + ooOoO0o
 O0oO000O0O = args . get ( 'mode' )
 I1i1i1iii = args . get ( 'uicode' )
 I1111i = args . get ( 'genre' )
 iIIii = args . get ( 'subgenre' )
 if 92 - 92: Ii1I + oO0o % OOooOOo
 if I1111i == '-' :
  oOo0 = iI11i1ii11 . GetGenreGroup ( I1i1i1iii , I1111i , exclusion21 = o0O00oooo ( ) )
 else :
  i1iI = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 }
  oOo0 = iI11i1ii11 . GetGenreGroup_sub ( i1iI )
  if 94 - 94: iIii1I11I1II1 / Oo0Ooo % iII111i * iII111i * II111iiii
  if 29 - 29: OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / OOooOOo * iIii1I11I1II1
 for O0OO in oOo0 :
  i11 = O0OO . get ( 'title' )
  if 6 - 6: iIii1I11I1II1 % i11iIiiIii % I1ii11iIi11i
  oOoOO0 = { 'mode' : O0oO000O0O
 , 'uicode' : I1i1i1iii
  , 'genre' : O0OO . get ( 'genre' )
 , 'subgenre' : O0OO . get ( 'subgenre' )
 , 'adult' : O0OO . get ( 'adult' )
 , 'page' : '1'
 , 'broadcastid' : O0OO . get ( 'broadcastid' )
 , 'contenttype' : O0OO . get ( 'contenttype' )
 , 'uiparent' : O0OO . get ( 'uiparent' )
 , 'uirank' : O0OO . get ( 'uirank' )
 , 'uitype' : O0OO . get ( 'uitype' )
 }
  if 93 - 93: IiII * OoooooooOO + ooOoO0o
  if I1i1i1iii == 'moviegenre' or O0OO . get ( 'subgenre' ) != '-' :
   oOoOO0 [ 'mode' ] = 'GENRE_LIST'
   if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
  else :
   if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
   None
   if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 26 - 26: Ii1I % I1ii11iIi11i
 if len ( oOo0 ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 76 - 76: IiII * iII111i
 if 52 - 52: OOooOOo
 if 19 - 19: I1IiiI
 if 25 - 25: Ii1I / ooOoO0o
def II ( args ) :
 if 70 - 70: iIii1I11I1II1
 iI11i1ii11 . SaveCredential ( IIII ( ) )
 if 31 - 31: IiII - I1IiiI % iIii1I11I1II1
 I1i1i1iii = args . get ( 'uicode' )
 OOOoo0OO = int ( args . get ( 'page' ) )
 if 92 - 92: i1IIi - iIii1I11I1II1
 oOoOO0 = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'subgenre' : args . get ( 'subgenre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 }
 if args . get ( 'genre' ) == args . get ( 'subgenre' ) :
  oOoOO0 [ 'subgenre' ] = 'all'
  if 16 - 16: OoO0O00 - OoOoOO00 - OOooOOo - i1IIi / Ii1I
 oOo0 , iI1Ii11iIiI1 = iI11i1ii11 . GetGenreList ( I1i1i1iii , oOoOO0 , OOOoo0OO )
 if 88 - 88: OoO0O00
 if 71 - 71: I1ii11iIi11i
 if 7 - 7: I1ii11iIi11i - I1IiiI . iIii1I11I1II1 - i1IIi
 for O0OO in oOo0 :
  i11 = O0OO . get ( 'title' )
  oooooo0O000o = O0OO . get ( 'thumbnail' )
  if 59 - 59: o0oOOo0O0Ooo
  O0O0ooOOO = { }
  O0O0ooOOO [ 'plot' ] = i11
  if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
  if I1i1i1iii == 'vodgenre' :
   o0OoOo00o0o = { 'mode' : 'DEEP_LIST'
 , 'contentid' : O0OO . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : ''
   , 'thumbnail' : oooooo0O000o
   , 'viewage' : O0OO . get ( 'viewage' )
 }
   oO00O0O0O = True
   if 41 - 41: ooOoO0o % OoO0O00 - Oo0Ooo * I1Ii111 * Oo0Ooo
  else :
   o0OoOo00o0o = { 'mode' : 'MOVIE'
 , 'contentid' : O0OO . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : ''
   , 'thumbnail' : oooooo0O000o
   , 'viewage' : O0OO . get ( 'viewage' )
 }
   if 69 - 69: OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
   oO00O0O0O = False
   if 23 - 23: i11iIiiIii
  if o0OoOo00o0o . get ( 'viewage' ) == '21' : i11 += ' (%s)' % ( o0OoOo00o0o . get ( 'viewage' ) )
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
  o00O ( i11 , sublabel = '' , img = oooooo0O000o , infoLabels = O0O0ooOOO , isFolder = oO00O0O0O , params = o0OoOo00o0o )
  if 81 - 81: IiII % i1IIi . iIii1I11I1II1
 if iI1Ii11iIiI1 :
  if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / IiII
  oOoOO0 [ 'mode' ] = 'GENRE_LIST'
  oOoOO0 [ 'uicode' ] = I1i1i1iii
  oOoOO0 [ 'page' ] = str ( OOOoo0OO + 1 )
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  O0O00Oo = str ( OOOoo0OO + 1 )
  o00O ( i11 , sublabel = O0O00Oo , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 6 - 6: iII111i / I1IiiI % OOooOOo - I1IiiI
 if len ( oOo0 ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 31 - 31: OOooOOo
 if 23 - 23: I1Ii111 . IiII
 if 92 - 92: OoOoOO00 + I1Ii111 * Ii1I % I1IiiI
 if 42 - 42: Oo0Ooo
def oo000O0OoooO ( args ) :
 if 93 - 93: I11i . II111iiii / oO0o % OoooooooOO * I11i % I1ii11iIi11i
 iI11i1ii11 . SaveCredential ( IIII ( ) )
 if 48 - 48: ooOoO0o / I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / i1IIi
 I1i1i1iii = args . get ( 'uicode' )
 OOOOoOOo0O0 = args . get ( 'came' )
 OOOoo0OO = int ( args . get ( 'page' ) )
 if 92 - 92: I1ii11iIi11i + iIii1I11I1II1 / II111iiii
 if 94 - 94: OoooooooOO + Oo0Ooo / OoOoOO00 * OOooOOo
 if 69 - 69: ooOoO0o % oO0o
 ii1I1IIii11 , iI1Ii11iIiI1 = iI11i1ii11 . GetDeeplinkList ( I1i1i1iii , OOOOoOOo0O0 , OOOoo0OO )
 if 67 - 67: iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
 for ooOoOo0 in ii1I1IIii11 :
  i11 = ooOoOo0 . get ( 'title' )
  O0O00Oo = ooOoOo0 . get ( 'subtitle' )
  oooooo0O000o = ooOoOo0 . get ( 'thumbnail' )
  I11iiiiI1i = ooOoOo0 . get ( 'uicode' )
  iI1i11 = ooOoOo0 . get ( 'channelepg' )
  if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / Ii1I + I1ii11iIi11i
  oOoOO0 = { 'uicode' : I11iiiiI1i
  , 'came' : OOOOoOOo0O0
 , 'contentid' : ooOoOo0 . get ( 'contentid' )
 , 'contentidType' : ooOoOo0 . get ( 'contentidType' )
 , 'page' : '1'
 , 'title' : i11
  , 'subtitle' : O0O00Oo
  , 'thumbnail' : oooooo0O000o
  , 'viewage' : ooOoOo0 . get ( 'viewage' )
 }
  if 86 - 86: o0oOOo0O0Ooo
  if I11iiiiI1i == 'channel' :
   oOoOO0 [ 'mode' ] = 'LIVE'
  elif I11iiiiI1i == 'movie' :
   oOoOO0 [ 'mode' ] = 'MOVIE'
  else :
   oOoOO0 [ 'mode' ] = 'DEEP_LIST'
   if 5 - 5: IiII * OoOoOO00
   if 5 - 5: I1Ii111
  O0O0ooOOO = { }
  if iI1i11 :
   O0O0ooOOO [ 'plot' ] = '%s\n\n%s' % ( i11 , iI1i11 )
  else :
   O0O0ooOOO [ 'plot' ] = '%s\n\n%s' % ( i11 , O0O00Oo )
   if 90 - 90: I1Ii111 . ooOoO0o / Ii1I - I11i
  if ooOoOo0 . get ( 'viewage' ) == '21' : O0O00Oo += ' (%s)' % ( ooOoOo0 . get ( 'viewage' ) )
  if 40 - 40: OoooooooOO
  if I11iiiiI1i in [ 'channel' , 'movie' ] :
   oO00O0O0O = False
  elif oOoOO0 [ 'contentidType' ] == 'direct' :
   oO00O0O0O = False
   oOoOO0 [ 'mode' ] = 'VOD'
  else :
   oO00O0O0O = True
   if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
   if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
  o00O ( i11 , sublabel = O0O00Oo , img = oooooo0O000o , infoLabels = O0O0ooOOO , isFolder = oO00O0O0O , params = oOoOO0 )
  if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
 if iI1Ii11iIiI1 :
  if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
  oOoOO0 [ 'mode' ] = 'GN_LIST'
  oOoOO0 [ 'uicode' ] = I1i1i1iii
  oOoOO0 [ 'page' ] = str ( OOOoo0OO + 1 )
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  O0O00Oo = str ( OOOoo0OO + 1 )
  o00O ( i11 , sublabel = O0O00Oo , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 19 - 19: OoO0O00 - Oo0Ooo . O0
 if len ( ii1I1IIii11 ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 60 - 60: II111iiii + Oo0Ooo
 if 9 - 9: ooOoO0o * OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoO0O00
 if 49 - 49: II111iiii
def Iiii1iI1i ( args ) :
 if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
 iI11i1ii11 . SaveCredential ( IIII ( ) )
 if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
 O0O0Oo00 = args . get ( 'contentid' )
 oOoO00o = args . get ( 'contentidType' )
 oOO00O = args . get ( 'uicode' )
 if 100 - 100: o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
 OOOoo0OO = int ( args . get ( 'page' ) )
 if 80 - 80: o0oOOo0O0Ooo * O0 - Ii1I
 oo00O00Oo , iI1Ii11iIiI1 = iI11i1ii11 . GetEpisodeList ( O0O0Oo00 , oOO00O , oOoO00o , OOOoo0OO , orderby = iI1 ( ) )
 if 26 - 26: I1ii11iIi11i - OoO0O00 - Ii1I + I1ii11iIi11i
 for oo in oo00O00Oo :
  i11 = oo . get ( 'title' )
  O0O00Oo = oo . get ( 'subtitle' )
  oooooo0O000o = oo . get ( 'thumbnail' )
  oOoOO0 = { 'mode' : 'VOD'
 , 'uicode' : oo . get ( 'uicode' )
  , 'contentid' : oo . get ( 'contentid' )
 , 'programid' : oo . get ( 'programid' )
 , 'title' : i11
  , 'subtitle' : O0O00Oo
  , 'thumbnail' : oooooo0O000o
  , 'viewage' : oo . get ( 'viewage' )
 }
  if 42 - 42: I1Ii111 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
  if oo . get ( 'viewage' ) == '21' : O0O00Oo += ' (%s)' % ( oo . get ( 'viewage' ) )
  if 31 - 31: iII111i . OOooOOo - ooOoO0o . OoooooooOO / OoooooooOO
  OOoO = { }
  OOoO [ 'plot' ] = oo . get ( 'synopsis' )
  if 44 - 44: oO0o
  if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
  o00O ( i11 , sublabel = O0O00Oo , img = oooooo0O000o , infoLabels = OOoO , isFolder = False , params = oOoOO0 )
  if 88 - 88: OoOoOO00 / II111iiii
 if OOOoo0OO == 1 :
  O0O0ooOOO = { 'plot' : '정렬순서를 변경합니다.' }
  oOoOO0 = { }
  oOoOO0 [ 'mode' ] = 'ORDER_BY'
  if iI1 ( ) == 'desc' :
   i11 = '정렬순서변경 : 최신화부터 -> 1회부터'
   oOoOO0 [ 'orderby' ] = 'asc'
  else :
   i11 = '정렬순서변경 : 1회부터 -> 최신화부터'
   oOoOO0 [ 'orderby' ] = 'desc'
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = O0O0ooOOO , isFolder = False , params = oOoOO0 )
  if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iII111i + oO0o
 if iI1Ii11iIiI1 :
  if 82 - 82: oO0o / iIii1I11I1II1 . I1IiiI . OOooOOo / o0oOOo0O0Ooo
  oOoOO0 [ 'mode' ] = 'DEEP_LIST'
  oOoOO0 [ 'uicode' ] = oOO00O
  oOoOO0 [ 'contentid' ] = O0O0Oo00
  oOoOO0 [ 'contentidType' ] = oOoO00o
  oOoOO0 [ 'page' ] = str ( OOOoo0OO + 1 )
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  O0O00Oo = str ( OOOoo0OO + 1 )
  o00O ( i11 , sublabel = O0O00Oo , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 42 - 42: Oo0Ooo
 if len ( oo00O00Oo ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
 if 46 - 46: Oo0Ooo
 if 1 - 1: iII111i
def O0O0Ooo ( args ) :
 if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
 iI11i1ii11 . SaveCredential ( IIII ( ) )
 if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
 O0O0Oo00 = args . get ( 'contentid' )
 oOO00O = args . get ( 'uicode' )
 Oo00o0OO0O00o = O0O0O ( )
 if 82 - 82: I11i + OoooooooOO - i1IIi . i1IIi
 oo00o0Oo0oo ( O0O0Oo00 + ' - ' + oOO00O , False )
 iIi1i , I1i11111i1i11 , OOoOOO0 , I1I1i = iI11i1ii11 . GetStreamingURL ( O0O0Oo00 , oOO00O , Oo00o0OO0O00o )
 if 1 - 1: I11i % OOooOOo + O0 + i1IIi - OoO0O00
 if 22 - 22: I1IiiI % I1ii11iIi11i
 o0oo0O = '%s|Cookie=%s' % ( iIi1i , I1i11111i1i11 )
 oo00o0Oo0oo ( o0oo0O , False )
 if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - II111iiii * OOooOOo
 if iIi1i == '' :
  ooO00oOoo ( __language__ ( 30303 ) . encode ( 'utf8' ) )
  return
  if 26 - 26: OoooooooOO * I1IiiI + OOooOOo
 IiIii1i111 = xbmcgui . ListItem ( path = o0oo0O )
 if 43 - 43: O0
 if OOoOOO0 :
  if 39 - 39: I1IiiI . iIii1I11I1II1 * Ii1I % ooOoO0o . iIii1I11I1II1
  if 54 - 54: OOooOOo
  IiI11ii1I = OOoOOO0 [ 'customdata' ]
  IiiiI = OOoOOO0 [ 'drmhost' ]
  if 61 - 61: OOooOOo % OOooOOo * o0oOOo0O0Ooo / o0oOOo0O0Ooo
  o0oOO = 'mpd'
  O0o0OO0000ooo = 'com.widevine.alpha'
  if 4 - 4: Ii1I
  OO0oOOoo = inputstreamhelper . Helper ( o0oOO , drm = O0o0OO0000ooo )
  if 52 - 52: o0oOOo0O0Ooo % Oo0Ooo
  if OO0oOOoo . check_inputstream ( ) :
   if 64 - 64: O0 % I11i % O0 * OoO0O00 . oO0o + I1IiiI
   if oOO00O == 'movie' :
    O00I11ii1i1 = 'https://www.wavve.com/player/movie?movieid=%s' % O0O0Oo00
   else :
    O00I11ii1i1 = 'https://www.wavve.com/player/vod?programid=%s&page=1' % O0O0Oo00
    if 78 - 78: iII111i
   iIiIIIIIii = { 'content-type' : 'application/octet-stream'
 , 'origin' : 'https://www.wavve.com'
 , 'pallycon-customdata' : IiI11ii1I
 , 'referer' : O00I11ii1i1
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'

   , 'user-agent' : oo00
 }
   OOo0 = IiiiI + '|' + urllib . urlencode ( iIiIIIIIii ) + '|R{SSM}|'
   if 25 - 25: OoooooooOO + IiII * I1ii11iIi11i
   IiIii1i111 . setProperty ( 'inputstreamaddon' , OO0oOOoo . inputstream_addon )
   IiIii1i111 . setProperty ( 'inputstream.adaptive.manifest_type' , o0oOO )
   IiIii1i111 . setProperty ( 'inputstream.adaptive.license_type' , O0o0OO0000ooo )
   if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + I1Ii111
   IiIii1i111 . setProperty ( 'inputstream.adaptive.license_key' , OOo0 )
   IiIii1i111 . setProperty ( 'inputstream.adaptive.stream_headers' , 'Cookie=%s' % I1i11111i1i11 )
   if 18 - 18: ooOoO0o * OoOoOO00 . iII111i / I1ii11iIi11i / i11iIiiIii
 xbmcplugin . setResolvedUrl ( i1I1iI , True , IiIii1i111 )
 if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
 if I1I1i :
  ooO00oOoo ( I1I1i . encode ( 'utf-8' ) )
 else :
  if '/preview.' in urlparse . urlsplit ( iIi1i ) . path : ooO00oOoo ( __language__ ( 30401 ) . encode ( 'utf8' ) )
  if 91 - 91: i11iIiiIii / i1IIi + iII111i + ooOoO0o * i11iIiiIii
 if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) and args . get ( 'viewage' ) != '21' :
  oOoOO0 = { 'code' : args . get ( 'programid' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'contentid' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 , 'subtitle' : args . get ( 'subtitle' )
 }
  OoOoOo00o0 ( args . get ( 'mode' ) . lower ( ) , oOoOO0 )
  if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iII111i
  if 8 - 8: ooOoO0o + II111iiii / iII111i / I11i
  if 74 - 74: O0 / i1IIi
  if 78 - 78: OoooooooOO . OoO0O00 + ooOoO0o - i1IIi
def ii1 ( args ) :
 I1111i = args . get ( 'genre' )
 if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
 if I1111i == '-' :
  i11 = 'VOD 시청내역'
  oOoOO0 = { 'mode' : 'WATCH'
 , 'genre' : 'vod'
 }
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 100 - 100: OoO0O00
  i11 = '영화 시청내역'
  oOoOO0 [ 'genre' ] = 'movie'
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
  xbmcplugin . endOfDirectory ( i1I1iI )
  if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
 else :
  i1iiIiI1Ii1i = i1iIi ( I1111i )
  if 30 - 30: O0 - iIii1I11I1II1 / OoooooooOO
  for O0000OOO0 in i1iiIiI1Ii1i :
   ooo0 = dict ( urlparse . parse_qsl ( O0000OOO0 ) )
   if 78 - 78: ooOoO0o
   i11 = ooo0 . get ( 'title' ) . strip ( )
   O0O00Oo = ooo0 . get ( 'subtitle' ) . strip ( )
   if O0O00Oo == 'None' : O0O00Oo = ''
   oooooo0O000o = ooo0 . get ( 'img' )
   if 53 - 53: ooOoO0o * OOooOOo . iII111i / O0 * ooOoO0o
   O0O0ooOOO = { }
   O0O0ooOOO [ 'plot' ] = '%s\n%s' % ( i11 , O0O00Oo )
   if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
   if I1111i == 'vod' :
    oOoOO0 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : ooo0 . get ( 'code' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
    oO00O0O0O = True
   else :
    oOoOO0 = { 'mode' : 'MOVIE'
 , 'contentid' : ooo0 . get ( 'code' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'title' : i11
 , 'thumbnail' : oooooo0O000o
 }
    oO00O0O0O = False
    if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
   o00O ( i11 , sublabel = O0O00Oo , img = oooooo0O000o , infoLabels = O0O0ooOOO , isFolder = oO00O0O0O , params = oOoOO0 )
   if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
  O0O0ooOOO = { 'plot' : '시청목록을 삭제합니다.' }
  i11 = '*** 시청목록 삭제 ***'
  oOoOO0 = { 'mode' : 'MYVIEW_REMOVE'
 , 'genre' : I1111i
 }
  if 92 - 92: I11i . I1Ii111
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = O0O0ooOOO , isFolder = False , params = oOoOO0 )
  if 85 - 85: I1ii11iIi11i . I1Ii111
  xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
  if 78 - 78: ooOoO0o * I1Ii111 + iIii1I11I1II1 + iIii1I11I1II1 / I1Ii111 . Ii1I
  if 97 - 97: ooOoO0o / I1Ii111 % i1IIi % I1ii11iIi11i
  if 18 - 18: iIii1I11I1II1 % I11i
  if 95 - 95: ooOoO0o + i11iIiiIii * I1Ii111 - i1IIi * I1Ii111 - iIii1I11I1II1
  if 75 - 75: OoooooooOO * IiII
def I1Iiiiiii ( args ) :
 i11 = 'VOD 검색'
 oOoOO0 = { 'mode' : 'SEARCH_LIST'
 , 'genre' : 'vod'
 , 'page' : '1'
 }
 o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
 i11 = '영화 검색'
 oOoOO0 [ 'genre' ] = 'movie'
 o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if 69 - 69: O0
 xbmcplugin . endOfDirectory ( i1I1iI )
 if 85 - 85: ooOoO0o / O0
 if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
 if 62 - 62: I1Ii111 . IiII . OoooooooOO
 if 11 - 11: OOooOOo / I11i
def oooO0 ( args ) :
 if 16 - 16: II111iiii + oO0o - OoooooooOO
 iI11i1ii11 . SaveCredential ( IIII ( ) )
 if 3 - 3: O0 / iII111i
 oOO00O = args . get ( 'genre' )
 OOOoo0OO = int ( args . get ( 'page' ) )
 if 31 - 31: OOooOOo + o0oOOo0O0Ooo . OoooooooOO
 if 'search_key' in args :
  ooOooo0 = args . get ( 'search_key' )
 else :
  ooOooo0 = IiiIII111ii ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
  if not ooOooo0 : return
  if 67 - 67: I1IiiI
 OO00OO0O0 , iI1Ii11iIiI1 = iI11i1ii11 . GetSearchList ( ooOooo0 , oOO00O , OOOoo0OO , exclusion21 = o0O00oooo ( ) )
 if 48 - 48: I1Ii111
 for O00Oo0o000oO in OO00OO0O0 :
  i11 = O00Oo0o000oO . get ( 'title' )
  oooooo0O000o = O00Oo0o000oO . get ( 'thumbnail' )
  if 99 - 99: oO0o * II111iiii * I1Ii111
  O0O0ooOOO = { }
  O0O0ooOOO [ 'plot' ] = i11
  if 92 - 92: Oo0Ooo
  if oOO00O == 'vod' :
   oOoOO0 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : O00Oo0o000oO . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : ''
   , 'thumbnail' : oooooo0O000o
   , 'viewage' : O00Oo0o000oO . get ( 'viewage' )
 }
   oO00O0O0O = True
   if 40 - 40: OoOoOO00 / IiII
  else :
   oOoOO0 = { 'mode' : 'MOVIE'
 , 'contentid' : O00Oo0o000oO . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : ''
   , 'thumbnail' : oooooo0O000o
   , 'viewage' : O00Oo0o000oO . get ( 'viewage' )
 }
   if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111
   oO00O0O0O = False
   if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
  if oOoOO0 . get ( 'viewage' ) == '21' : i11 += ' (%s)' % ( oOoOO0 . get ( 'viewage' ) )
  if 61 - 61: II111iiii
  o00O ( i11 , sublabel = '' , img = oooooo0O000o , infoLabels = O0O0ooOOO , isFolder = oO00O0O0O , params = oOoOO0 )
  if 15 - 15: i11iIiiIii % I1IiiI * I11i / I1Ii111
 if iI1Ii11iIiI1 :
  if 90 - 90: iII111i
  oOoOO0 [ 'mode' ] = 'SEARCH_LIST'
  oOoOO0 [ 'genre' ] = oOO00O
  oOoOO0 [ 'page' ] = str ( OOOoo0OO + 1 )
  oOoOO0 [ 'search_key' ] = ooOooo0
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  O0O00Oo = str ( OOOoo0OO + 1 )
  o00O ( i11 , sublabel = O0O00Oo , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 31 - 31: OOooOOo + O0
 if len ( OO00OO0O0 ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI )
 if 87 - 87: ooOoO0o
 if 45 - 45: OoO0O00 / OoooooooOO - iII111i / Ii1I % IiII
 if 83 - 83: I1IiiI . iIii1I11I1II1 - IiII * i11iIiiIii
 if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
 if 13 - 13: Oo0Ooo
def i1iIi ( genre ) :
 try :
  oOOo000oOoO0 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  with open ( oOOo000oOoO0 , 'r' ) as OoOo00o0OO :
   ii1IIIIiI11 = OoOo00o0OO . readlines ( )
 except :
  ii1IIIIiI11 = [ ]
  if 40 - 40: o0oOOo0O0Ooo
 return ii1IIIIiI11
 if 67 - 67: oO0o + II111iiii - O0 . oO0o * II111iiii * I11i
 if 90 - 90: Ii1I . IiII
 if 81 - 81: OOooOOo - I11i % ooOoO0o - OoO0O00 / Oo0Ooo
 if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
def OoOoOo00o0 ( genre , in_params ) :
 try :
  oOOo000oOoO0 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  Ooooo00o0OoO = i1iIi ( genre )
  if 75 - 75: I1IiiI % II111iiii
  with open ( oOOo000oOoO0 , 'w' ) as OoOo00o0OO :
   I1I1i1I = urllib . urlencode ( in_params )
   I1I1i1I = I1I1i1I . encode ( 'utf-8' ) + '\n'
   OoOo00o0OO . write ( I1I1i1I )
   if 87 - 87: O0 / iIii1I11I1II1 * i1IIi
   IIi11IIiIii1 = 0
   for I1iIII1 in Ooooo00o0OoO :
    iIii = dict ( urlparse . parse_qsl ( I1iIII1 ) )
    if in_params . get ( 'code' ) != iIii . get ( 'code' ) :
     OoOo00o0OO . write ( I1iIII1 )
     IIi11IIiIii1 += 1
     if IIi11IIiIii1 >= 50 : break
 except :
  None
  if 84 - 84: oO0o % i1IIi
  if 70 - 70: Oo0Ooo . OoooooooOO - iII111i
  if 30 - 30: I1ii11iIi11i % I1IiiI
  if 89 - 89: I1Ii111 + OoooooooOO + I1Ii111 * i1IIi + iIii1I11I1II1 % I11i
def oOo0oO ( genre ) :
 try :
  oOOo000oOoO0 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  with open ( oOOo000oOoO0 , 'w' ) as OoOo00o0OO :
   OoOo00o0OO . write ( '' )
 except :
  None
  if 5 - 5: OOooOOo - OOooOOo . Oo0Ooo + OoOoOO00 - OOooOOo . oO0o
  if 31 - 31: II111iiii - iIii1I11I1II1 - iIii1I11I1II1 % I11i
  if 12 - 12: iIii1I11I1II1
  if 20 - 20: o0oOOo0O0Ooo / i1IIi
def oOIi111 ( args ) :
 I1111i = args . get ( 'genre' )
 if 67 - 67: O0
 O0OOo = xbmcgui . Dialog ( )
 Iiii = O0OOo . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
 if Iiii == False : sys . exit ( )
 if 52 - 52: II111iiii . ooOoO0o / OoOoOO00 / OoooooooOO . i11iIiiIii
 oOo0oO ( I1111i )
 if 30 - 30: I11i / Ii1I . IiII . OoooooooOO - Oo0Ooo
 xbmc . executebuiltin ( "Container.Refresh" )
 if 44 - 44: O0 * OoooooooOO % ooOoO0o + II111iiii
 if 39 - 39: oO0o % iIii1I11I1II1 % O0 % OoooooooOO * I1ii11iIi11i + iII111i
 if 68 - 68: Oo0Ooo + i11iIiiIii
 if 69 - 69: iIii1I11I1II1 * iIii1I11I1II1 * i11iIiiIii + I1IiiI / OOooOOo % Ii1I
 if 58 - 58: OOooOOo * o0oOOo0O0Ooo + O0 % OOooOOo
 if 25 - 25: Oo0Ooo % I1ii11iIi11i * ooOoO0o
 if 6 - 6: iII111i . IiII * OoOoOO00 . i1IIi
 if 98 - 98: i1IIi
 if 65 - 65: OoOoOO00 / OoO0O00 % IiII
 if 45 - 45: OoOoOO00
 if 66 - 66: OoO0O00
iI11i1ii11 = iIi ( )
i1I1iI = int ( sys . argv [ 1 ] )
if 56 - 56: O0
if 61 - 61: o0oOOo0O0Ooo / OOooOOo / Oo0Ooo * O0
if 23 - 23: oO0o - OOooOOo + I11i
if 12 - 12: I1IiiI / ooOoO0o % o0oOOo0O0Ooo / i11iIiiIii % OoooooooOO
oOoOO0 = I1i1I1II ( )
O0oO000O0O = oOoOO0 . get ( 'mode' , None )
if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo0Ooo * Ii1I + I11i
o0 ( )
if O0oO000O0O is None :
 if 11 - 11: iII111i * Ii1I - OoOoOO00
 i1I11i1iI ( )
 if 66 - 66: OoOoOO00 . i11iIiiIii - iII111i * o0oOOo0O0Ooo + OoooooooOO * I1ii11iIi11i
 if 74 - 74: Oo0Ooo
 if 61 - 61: Oo0Ooo - I1Ii111 * II111iiii % ooOoO0o * iIii1I11I1II1 + OoO0O00
 if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
 if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
 if 58 - 58: I11i + II111iiii * iII111i * i11iIiiIii - iIii1I11I1II1
 if 68 - 68: OoooooooOO % II111iiii
 if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
 if 24 - 24: II111iiii % I1Ii111 - ooOoO0o + I1IiiI * I1ii11iIi11i
elif O0oO000O0O == 'GNB_LIST' :
 i1I1iI1iIi111i ( oOoOO0 )
 if 2 - 2: Ii1I - IiII
elif O0oO000O0O == 'GN_LIST' :
 oo000O0OoooO ( oOoOO0 )
 if 83 - 83: oO0o % o0oOOo0O0Ooo % Ii1I - II111iiii * OOooOOo / OoooooooOO
elif O0oO000O0O == 'DEEP_LIST' :
 oOO00O = oOoOO0 . get ( 'uicode' , None )
 if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
 if oOO00O in [ 'quick' , 'vod' , 'program' , 'x' ] :
  Iiii1iI1i ( oOoOO0 )
  if 71 - 71: OoooooooOO
 else : None
 if 33 - 33: I1Ii111
elif O0oO000O0O in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
 O0O0Ooo ( oOoOO0 )
 xbmc . sleep ( 200 )
 if 62 - 62: I1ii11iIi11i + Ii1I + i1IIi / OoooooooOO
elif O0oO000O0O == 'GN_MYVIEW' :
 OOOO0oo0 ( oOoOO0 )
 if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
elif O0oO000O0O == 'MYVIEW_LIST' :
 oOo0O0o00o ( oOoOO0 )
 if 22 - 22: ooOoO0o - ooOoO0o % OOooOOo . I1Ii111 + oO0o
elif O0oO000O0O == 'GENRE' :
 Oo ( oOoOO0 )
 if 63 - 63: I1IiiI % I1Ii111 * o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % iII111i
elif O0oO000O0O == 'GENRE_LIST' :
 II ( oOoOO0 )
 if 45 - 45: IiII
elif O0oO000O0O == 'WATCH' :
 ii1 ( oOoOO0 )
 if 20 - 20: OoooooooOO * o0oOOo0O0Ooo * O0 . OOooOOo
elif O0oO000O0O == 'MYVIEW_REMOVE' :
 oOIi111 ( oOoOO0 )
 if 78 - 78: iIii1I11I1II1 + I11i - Ii1I * I1Ii111 - OoooooooOO % OoOoOO00
elif O0oO000O0O == 'SEARCH' :
 I1Iiiiiii ( oOoOO0 )
 if 34 - 34: O0
elif O0oO000O0O == 'SEARCH_LIST' :
 oooO0 ( oOoOO0 )
 if 80 - 80: i1IIi - Oo0Ooo / OoO0O00 - i11iIiiIii
elif O0oO000O0O == 'ORDER_BY' :
 IIIII11I1IiI ( oOoOO0 )
 if 68 - 68: oO0o - I1ii11iIi11i % O0 % I1Ii111
else :
 None
 if 11 - 11: O0 / OoO0O00 % OOooOOo + o0oOOo0O0Ooo + iIii1I11I1II1
 if 40 - 40: ooOoO0o - OOooOOo . Ii1I * Oo0Ooo % I1Ii111
 if 56 - 56: i11iIiiIii . o0oOOo0O0Ooo - I1IiiI * I11i
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
