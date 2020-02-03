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
  O0OOo . notification ( __name__ , sting )
 except :
  None
  if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1 . IiII / IiII % IiII
  if 22 - 22: Ii1I . IiII
  if 41 - 41: I1Ii111 . ooOoO0o * IiII % i11iIiiIii
def o000o0o00o0Oo ( string , isDebug = False ) :
 try :
  oo = string . encode ( 'utf-8' , 'ignore' )
 except :
  oo = 'addonException: addon_log'
 if isDebug : IiII1I1i1i1ii = xbmc . LOGDEBUG
 else : IiII1I1i1i1ii = xbmc . LOGNOTICE
 xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , oo ) , level = IiII1I1i1i1ii )
 if 44 - 44: oO0o / Oo0Ooo - II111iiii - i11iIiiIii % I1Ii111
 if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
 if 31 - 31: OoO0O00 + II111iiii
 if 13 - 13: OOooOOo * oO0o * I1IiiI
def oOOOO ( title ) :
 i11iiII = None
 I1iiiiI1iII = xbmc . Keyboard ( )
 I1iiiiI1iII . setHeading ( title )
 xbmc . sleep ( 1000 )
 I1iiiiI1iII . doModal ( )
 if ( I1iiiiI1iII . isConfirmed ( ) ) :
  i11iiII = I1iiiiI1iII . getText ( )
 return i11iiII
 if 20 - 20: i1IIi + i11iIiiIii - Ii1I % OoO0O00 . OoooooooOO
 if 96 - 96: i1IIi . OoOoOO00 * OOooOOo % ooOoO0o
 if 60 - 60: oO0o * o0oOOo0O0Ooo % o0oOOo0O0Ooo % I11i * II111iiii + i1IIi
 if 64 - 64: oO0o - O0 / II111iiii / o0oOOo0O0Ooo / iIii1I11I1II1
def IiIIIiI1I1 ( ) :
 OoO000 = __addon__ . getSetting ( 'id' )
 IIiiIiI1 = __addon__ . getSetting ( 'pw' )
 iiIiIIi = __addon__ . getSetting ( 'selected_profile' )
 return ( OoO000 , IIiiIiI1 , iiIiIIi )
 if 65 - 65: OoOoOO00
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
 ( oo0oOo , o000O0o , iI1iII1 ) = IiIIIiI1I1 ( )
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
 III1iII1I1ii = xbmcgui . Window ( 10000 ) . getProperty ( 'WAVVE_M_LOGINTIME' )
 if 61 - 61: II111iiii
 if III1iII1I1ii != '' :
  if 64 - 64: ooOoO0o / OoOoOO00 - O0 - I11i
  if III1iII1I1ii == datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) :
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
   return
   if 68 - 68: OoOoOO00 - OoO0O00
   if 28 - 28: OoO0O00 . OOooOOo / OOooOOo + Oo0Ooo . I1ii11iIi11i
   if 1 - 1: iIii1I11I1II1 / II111iiii
 if not iiI1I11i1i . GetCredential ( oo0oOo , o000O0o , iI1iII1 ) :
  ooO00oOoo ( __language__ ( 30103 ) . encode ( 'utf8' ) )
  sys . exit ( )
  if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % iII111i
  if 92 - 92: iII111i
 O00 ( iiI1I11i1i . LoadCredential ( ) )
 III1ii1iII ( 'desc' )
 if 25 - 25: Oo0Ooo - I1IiiI / OoooooooOO / o0oOOo0O0Ooo
 if 12 - 12: I1IiiI * iII111i % i1IIi % iIii1I11I1II1
 if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
 if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
def oo0o00O ( args ) :
 o00O0OoO = args . get ( 'orderby' )
 if 16 - 16: iIii1I11I1II1
 III1ii1iII ( o00O0OoO )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 90 - 90: o0oOOo0O0Ooo % i1IIi / OoO0O00
 if 44 - 44: Oo0Ooo . OoO0O00 / I1ii11iIi11i + Ii1I
 if 65 - 65: O0
 if 68 - 68: OOooOOo % I1Ii111
def ooO00OO0 ( args ) :
 if 31 - 31: iII111i % iII111i % I11i
 iiI1I11i1i . SaveCredential ( IIII ( ) )
 if 69 - 69: OoO0O00 - Oo0Ooo + i1IIi / I1Ii111
 ii1 = iiI1I11i1i . GetGnList ( args . get ( 'uicode' ) )
 if 11 - 11: IiII * I1IiiI . iIii1I11I1II1 % OoooooooOO + iII111i
 if 78 - 78: OoO0O00 . OOooOOo + OoO0O00 / I11i / OoO0O00
 if 54 - 54: OoOoOO00 % iII111i
 if 37 - 37: OoOoOO00 * Oo0Ooo / ooOoO0o - iII111i % II111iiii . oO0o
 for O00I1iI1 in ii1 :
  i11 = O00I1iI1 . get ( 'title' )
  oOoOO0 = { 'mode' : 'GN_LIST' if O00I1iI1 . get ( 'uicode' ) != 'CY1' else 'GN_MYVIEW'
  , 'uicode' : O00I1iI1 . get ( 'uicode' )
 , 'came' : args . get ( 'came' )
 , 'page' : '1'
 }
  if 23 - 23: i11iIiiIii + o0oOOo0O0Ooo . i1IIi
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if len ( ii1 ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 100 - 100: I1Ii111 . oO0o * Ii1I
 if 14 - 14: OOooOOo % iIii1I11I1II1
 if 71 - 71: O0 . iII111i / o0oOOo0O0Ooo
 if 73 - 73: II111iiii . i11iIiiIii / Ii1I + OoOoOO00
def IiIiiIIiI ( args ) :
 i11 = 'VOD 시청내역'
 oOoOO0 = { 'mode' : 'MYVIEW_LIST'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
 o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if 67 - 67: ooOoO0o
 i11 = '영화 시청내역'
 oOoOO0 [ 'uicode' ] = 'movie'
 o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if 7 - 7: ooOoO0o - Oo0Ooo - oO0o + ooOoO0o
 xbmcplugin . endOfDirectory ( i1I1iI )
 if 26 - 26: Ii1I
 if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
 if 47 - 47: iII111i - Ii1I . II111iiii + OoooooooOO . i11iIiiIii
 if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
def oO0 ( args ) :
 if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
 iiI1I11i1i . SaveCredential ( IIII ( ) )
 if 55 - 55: OOooOOo . I1IiiI
 oOo0O0o00o = args . get ( 'uicode' )
 o00oO0oo0OO = int ( args . get ( 'page' ) )
 O0O0OOOOoo , oOooO0 = iiI1I11i1i . GetMyviewList ( oOo0O0o00o , o00oO0oo0OO )
 if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
 for I111I1Iiii1i in O0O0OOOOoo :
  i11 = I111I1Iiii1i . get ( 'title' )
  oOOoo00O00o = I111I1Iiii1i . get ( 'subtitle' )
  O0O00Oo = I111I1Iiii1i . get ( 'thumbnail' )
  if 97 - 97: O0 * OoooooooOO . OoooooooOO
  I111iI = { }
  I111iI [ 'plot' ] = i11
  if 56 - 56: I1IiiI
  if oOo0O0o00o == 'vod' :
   oOoOO0 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : I111I1Iiii1i . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : oOOoo00O00o
   , 'thumbnail' : O0O00Oo
   , 'viewage' : I111I1Iiii1i . get ( 'viewage' )
 }
   oO00O0O0O = True
   if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
  else :
   oOoOO0 = { 'mode' : 'MOVIE'
 , 'contentid' : I111I1Iiii1i . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : oOOoo00O00o
   , 'thumbnail' : O0O00Oo
   , 'viewage' : I111I1Iiii1i . get ( 'viewage' )
 }
   oO00O0O0O = False
   if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
  if I111I1Iiii1i . get ( 'viewage' ) == '21' : oOOoo00O00o += ' (%s)' % ( I111I1Iiii1i . get ( 'viewage' ) )
  if 63 - 63: OoOoOO00 * iII111i
  o00O ( i11 , sublabel = oOOoo00O00o , img = O0O00Oo , infoLabels = I111iI , isFolder = oO00O0O0O , params = oOoOO0 )
  if 69 - 69: O0 . OoO0O00
 if oOooO0 :
  if 49 - 49: I1IiiI - I11i
  oOoOO0 [ 'mode' ] = 'MYVIEW_LIST'
  oOoOO0 [ 'uicode' ] = oOo0O0o00o
  oOoOO0 [ 'page' ] = str ( o00oO0oo0OO + 1 )
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  oOOoo00O00o = str ( o00oO0oo0OO + 1 )
  o00O ( i11 , sublabel = oOOoo00O00o , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
 if len ( O0O0OOOOoo ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 62 - 62: OoooooooOO * I1IiiI
 if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
 if 50 - 50: I1Ii111 . o0oOOo0O0Ooo
 if 97 - 97: O0 + OoOoOO00
 if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
def iiIiI1i1 ( args ) :
 if 69 - 69: ooOoO0o
 iiI1I11i1i . SaveCredential ( IIII ( ) )
 if 40 - 40: I1Ii111 + OoooooooOO % o0oOOo0O0Ooo - iIii1I11I1II1 . I1IiiI
 iIiIi11iI = args . get ( 'mode' )
 Oo0O00O000 = args . get ( 'uicode' )
 i11I1IiII1i1i = args . get ( 'genre' )
 ooI1111i = args . get ( 'subgenre' )
 if 14 - 14: OOooOOo / o0oOOo0O0Ooo
 if i11I1IiII1i1i == '-' :
  iII11I1IiiIi = iiI1I11i1i . GetGenreGroup ( Oo0O00O000 , i11I1IiII1i1i , exclusion21 = o0O00oooo ( ) )
 else :
  oo0oO = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 }
  iII11I1IiiIi = iiI1I11i1i . GetGenreGroup_sub ( oo0oO )
  if 94 - 94: iIii1I11I1II1 / Oo0Ooo % iII111i * iII111i * II111iiii
  if 29 - 29: OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / OOooOOo * iIii1I11I1II1
 for O0OO in iII11I1IiiIi :
  i11 = O0OO . get ( 'title' )
  if 6 - 6: iIii1I11I1II1 % i11iIiiIii % I1ii11iIi11i
  oOoOO0 = { 'mode' : iIiIi11iI
 , 'uicode' : Oo0O00O000
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
  if Oo0O00O000 == 'moviegenre' or O0OO . get ( 'subgenre' ) != '-' :
   oOoOO0 [ 'mode' ] = 'GENRE_LIST'
   if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
  else :
   if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
   None
   if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 26 - 26: Ii1I % I1ii11iIi11i
 if len ( iII11I1IiiIi ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 76 - 76: IiII * iII111i
 if 52 - 52: OOooOOo
 if 19 - 19: I1IiiI
 if 25 - 25: Ii1I / ooOoO0o
def II ( args ) :
 if 70 - 70: iIii1I11I1II1
 iiI1I11i1i . SaveCredential ( IIII ( ) )
 if 31 - 31: IiII - I1IiiI % iIii1I11I1II1
 Oo0O00O000 = args . get ( 'uicode' )
 o00oO0oo0OO = int ( args . get ( 'page' ) )
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
 iII11I1IiiIi , oOooO0 = iiI1I11i1i . GetGenreList ( Oo0O00O000 , oOoOO0 , o00oO0oo0OO )
 if 88 - 88: OoO0O00
 if 71 - 71: I1ii11iIi11i
 if 7 - 7: I1ii11iIi11i - I1IiiI . iIii1I11I1II1 - i1IIi
 for O0OO in iII11I1IiiIi :
  i11 = O0OO . get ( 'title' )
  O0O00Oo = O0OO . get ( 'thumbnail' )
  if 59 - 59: o0oOOo0O0Ooo
  I111iI = { }
  I111iI [ 'plot' ] = i11
  if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
  if Oo0O00O000 == 'vodgenre' :
   o0OoOo00o0o = { 'mode' : 'DEEP_LIST'
 , 'contentid' : O0OO . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : ''
   , 'thumbnail' : O0O00Oo
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
   , 'thumbnail' : O0O00Oo
   , 'viewage' : O0OO . get ( 'viewage' )
 }
   if 69 - 69: OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
   oO00O0O0O = False
   if 23 - 23: i11iIiiIii
  if o0OoOo00o0o . get ( 'viewage' ) == '21' : i11 += ' (%s)' % ( o0OoOo00o0o . get ( 'viewage' ) )
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
  o00O ( i11 , sublabel = '' , img = O0O00Oo , infoLabels = I111iI , isFolder = oO00O0O0O , params = o0OoOo00o0o )
  if 81 - 81: IiII % i1IIi . iIii1I11I1II1
 if oOooO0 :
  if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / IiII
  oOoOO0 [ 'mode' ] = 'GENRE_LIST'
  oOoOO0 [ 'uicode' ] = Oo0O00O000
  oOoOO0 [ 'page' ] = str ( o00oO0oo0OO + 1 )
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  oOOoo00O00o = str ( o00oO0oo0OO + 1 )
  o00O ( i11 , sublabel = oOOoo00O00o , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 6 - 6: iII111i / I1IiiI % OOooOOo - I1IiiI
 if len ( iII11I1IiiIi ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 31 - 31: OOooOOo
 if 23 - 23: I1Ii111 . IiII
 if 92 - 92: OoOoOO00 + I1Ii111 * Ii1I % I1IiiI
 if 42 - 42: Oo0Ooo
def oo000O0OoooO ( args ) :
 if 93 - 93: I11i . II111iiii / oO0o % OoooooooOO * I11i % I1ii11iIi11i
 iiI1I11i1i . SaveCredential ( IIII ( ) )
 if 48 - 48: ooOoO0o / I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / i1IIi
 Oo0O00O000 = args . get ( 'uicode' )
 OOOOoOOo0O0 = args . get ( 'came' )
 o00oO0oo0OO = int ( args . get ( 'page' ) )
 if 92 - 92: I1ii11iIi11i + iIii1I11I1II1 / II111iiii
 if 94 - 94: OoooooooOO + Oo0Ooo / OoOoOO00 * OOooOOo
 if 69 - 69: ooOoO0o % oO0o
 ii1I1IIii11 , oOooO0 = iiI1I11i1i . GetDeeplinkList ( Oo0O00O000 , OOOOoOOo0O0 , o00oO0oo0OO )
 if 67 - 67: iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
 for ooOoOo0 in ii1I1IIii11 :
  i11 = ooOoOo0 . get ( 'title' )
  oOOoo00O00o = ooOoOo0 . get ( 'subtitle' )
  O0O00Oo = ooOoOo0 . get ( 'thumbnail' )
  I11iiiiI1i = ooOoOo0 . get ( 'uicode' )
  iI1i11 = ooOoOo0 . get ( 'channelepg' )
  if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / Ii1I + I1ii11iIi11i
  oOoOO0 = { 'uicode' : I11iiiiI1i
  , 'came' : OOOOoOOo0O0
 , 'contentid' : ooOoOo0 . get ( 'contentid' )
 , 'contentidType' : ooOoOo0 . get ( 'contentidType' )
 , 'page' : '1'
 , 'title' : i11
  , 'subtitle' : oOOoo00O00o
  , 'thumbnail' : O0O00Oo
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
  I111iI = { }
  if iI1i11 :
   I111iI [ 'plot' ] = '%s\n\n%s' % ( i11 , iI1i11 )
  else :
   I111iI [ 'plot' ] = '%s\n\n%s' % ( i11 , oOOoo00O00o )
   if 90 - 90: I1Ii111 . ooOoO0o / Ii1I - I11i
  if ooOoOo0 . get ( 'viewage' ) == '21' : oOOoo00O00o += ' (%s)' % ( ooOoOo0 . get ( 'viewage' ) )
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
  o00O ( i11 , sublabel = oOOoo00O00o , img = O0O00Oo , infoLabels = I111iI , isFolder = oO00O0O0O , params = oOoOO0 )
  if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
 if oOooO0 :
  if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
  oOoOO0 [ 'mode' ] = 'GN_LIST'
  oOoOO0 [ 'uicode' ] = Oo0O00O000
  oOoOO0 [ 'page' ] = str ( o00oO0oo0OO + 1 )
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  oOOoo00O00o = str ( o00oO0oo0OO + 1 )
  o00O ( i11 , sublabel = oOOoo00O00o , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 19 - 19: OoO0O00 - Oo0Ooo . O0
 if len ( ii1I1IIii11 ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 60 - 60: II111iiii + Oo0Ooo
 if 9 - 9: ooOoO0o * OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoO0O00
 if 49 - 49: II111iiii
def Iiii1iI1i ( args ) :
 if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
 iiI1I11i1i . SaveCredential ( IIII ( ) )
 if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
 O0O0Oo00 = args . get ( 'contentid' )
 oOoO00o = args . get ( 'contentidType' )
 oOo0O0o00o = args . get ( 'uicode' )
 if 100 - 100: o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
 o00oO0oo0OO = int ( args . get ( 'page' ) )
 if 80 - 80: o0oOOo0O0Ooo * O0 - Ii1I
 oo00O00Oo , oOooO0 = iiI1I11i1i . GetEpisodeList ( O0O0Oo00 , oOo0O0o00o , oOoO00o , o00oO0oo0OO , orderby = iI1 ( ) )
 if 26 - 26: I1ii11iIi11i - OoO0O00 - Ii1I + I1ii11iIi11i
 for ooI1i in oo00O00Oo :
  i11 = ooI1i . get ( 'title' )
  oOOoo00O00o = ooI1i . get ( 'subtitle' )
  O0O00Oo = ooI1i . get ( 'thumbnail' )
  oOoOO0 = { 'mode' : 'VOD'
 , 'uicode' : ooI1i . get ( 'uicode' )
  , 'contentid' : ooI1i . get ( 'contentid' )
 , 'programid' : ooI1i . get ( 'programid' )
 , 'title' : i11
  , 'subtitle' : oOOoo00O00o
  , 'thumbnail' : O0O00Oo
  , 'viewage' : ooI1i . get ( 'viewage' )
 }
  if 32 - 32: OoOoOO00 / OoO0O00 + OOooOOo
  if ooI1i . get ( 'viewage' ) == '21' : oOOoo00O00o += ' (%s)' % ( ooI1i . get ( 'viewage' ) )
  if 32 - 32: iIii1I11I1II1 % iII111i
  O0o = { }
  O0o [ 'plot' ] = ooI1i . get ( 'synopsis' )
  if 18 - 18: I1ii11iIi11i
  if 96 - 96: OoooooooOO + oO0o
  o00O ( i11 , sublabel = oOOoo00O00o , img = O0O00Oo , infoLabels = O0o , isFolder = False , params = oOoOO0 )
  if 44 - 44: oO0o
 if o00oO0oo0OO == 1 :
  I111iI = { 'plot' : '정렬순서를 변경합니다.' }
  oOoOO0 = { }
  oOoOO0 [ 'mode' ] = 'ORDER_BY'
  if iI1 ( ) == 'desc' :
   i11 = '정렬순서변경 : 최신화부터 -> 1회부터'
   oOoOO0 [ 'orderby' ] = 'asc'
  else :
   i11 = '정렬순서변경 : 1회부터 -> 최신화부터'
   oOoOO0 [ 'orderby' ] = 'desc'
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = I111iI , isFolder = False , params = oOoOO0 )
  if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
 if oOooO0 :
  if 88 - 88: OoOoOO00 / II111iiii
  oOoOO0 [ 'mode' ] = 'DEEP_LIST'
  oOoOO0 [ 'uicode' ] = oOo0O0o00o
  oOoOO0 [ 'contentid' ] = O0O0Oo00
  oOoOO0 [ 'contentidType' ] = oOoO00o
  oOoOO0 [ 'page' ] = str ( o00oO0oo0OO + 1 )
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  oOOoo00O00o = str ( o00oO0oo0OO + 1 )
  o00O ( i11 , sublabel = oOOoo00O00o , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iII111i + oO0o
 if len ( oo00O00Oo ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 82 - 82: oO0o / iIii1I11I1II1 . I1IiiI . OOooOOo / o0oOOo0O0Ooo
 if 42 - 42: Oo0Ooo
 if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
def iii11I ( args ) :
 if 50 - 50: iII111i + O0 + Ii1I . II111iiii / o0oOOo0O0Ooo
 iiI1I11i1i . SaveCredential ( IIII ( ) )
 if 17 - 17: Ii1I % iIii1I11I1II1 - iIii1I11I1II1
 O0O0Oo00 = args . get ( 'contentid' )
 oOo0O0o00o = args . get ( 'uicode' )
 O0o0O0 = O0O0O ( )
 if 11 - 11: II111iiii % OoO0O00 * iII111i + ooOoO0o + Ii1I
 o000o0o00o0Oo ( O0O0Oo00 + ' - ' + oOo0O0o00o , False )
 II1Iiiiii , ii1ii111 , I111i1i1111 , IIII1 = iiI1I11i1i . GetStreamingURL ( O0O0Oo00 , oOo0O0o00o , O0o0O0 )
 if 10 - 10: I1Ii111 / ooOoO0o + i11iIiiIii / Ii1I
 if 74 - 74: OOooOOo + O0 + i1IIi - i1IIi + II111iiii
 oOOO0oo0 = '%s|Cookie=%s' % ( II1Iiiiii , ii1ii111 )
 o000o0o00o0Oo ( oOOO0oo0 , False )
 if 46 - 46: IiII
 if II1Iiiiii == '' :
  ooO00oOoo ( __language__ ( 30303 ) . encode ( 'utf8' ) )
  return
  if 45 - 45: ooOoO0o
 IIi = xbmcgui . ListItem ( path = oOOO0oo0 )
 if 94 - 94: II111iiii - Oo0Ooo
 if I111i1i1111 :
  if 91 - 91: Oo0Ooo
  if 31 - 31: OOooOOo / i11iIiiIii % iIii1I11I1II1 + OOooOOo / i11iIiiIii
  OOooO0oo0o00o = I111i1i1111 [ 'customdata' ]
  ooOO0OoO = I111i1i1111 [ 'drmhost' ]
  if 69 - 69: iIii1I11I1II1 . I1ii11iIi11i % ooOoO0o + iIii1I11I1II1 / O0 / I1ii11iIi11i
  O00OoOO0oo0 = 'mpd'
  oOO = 'com.widevine.alpha'
  if 53 - 53: I1Ii111 * IiII . Oo0Ooo - Ii1I % Ii1I * i11iIiiIii
  ii = inputstreamhelper . Helper ( O00OoOO0oo0 , drm = oOO )
  if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
  if ii . check_inputstream ( ) :
   if 28 - 28: i1IIi - iII111i
   if oOo0O0o00o == 'movie' :
    o00o000oo = 'https://www.wavve.com/player/movie?movieid=%s' % O0O0Oo00
   else :
    o00o000oo = 'https://www.wavve.com/player/vod?programid=%s&page=1' % O0O0Oo00
    if 44 - 44: I1IiiI - I11i % iIii1I11I1II1
   O0O = { 'content-type' : 'application/octet-stream'
 , 'origin' : 'https://www.wavve.com'
 , 'pallycon-customdata' : OOooO0oo0o00o
 , 'referer' : o00o000oo
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'

   , 'user-agent' : oo00
 }
   Oo0o = ooOO0OoO + '|' + urllib . urlencode ( O0O ) + '|R{SSM}|'
   if 89 - 89: iII111i . O0 / I1ii11iIi11i % OoOoOO00 . Oo0Ooo
   IIi . setProperty ( 'inputstreamaddon' , ii . inputstream_addon )
   IIi . setProperty ( 'inputstream.adaptive.manifest_type' , O00OoOO0oo0 )
   IIi . setProperty ( 'inputstream.adaptive.license_type' , oOO )
   if 50 - 50: II111iiii + I1ii11iIi11i . i1IIi % o0oOOo0O0Ooo
   IIi . setProperty ( 'inputstream.adaptive.license_key' , Oo0o )
   IIi . setProperty ( 'inputstream.adaptive.stream_headers' , 'Cookie=%s' % ii1ii111 )
   if 5 - 5: OoOoOO00 / OoooooooOO + IiII * I1Ii111 - OoO0O00 % I1IiiI
 xbmcplugin . setResolvedUrl ( i1I1iI , True , IIi )
 if 42 - 42: O0 / o0oOOo0O0Ooo + OoooooooOO * ooOoO0o % ooOoO0o
 if IIII1 :
  ooO00oOoo ( IIII1 . encode ( 'utf-8' ) )
 else :
  if '/preview.' in urlparse . urlsplit ( II1Iiiiii ) . path : ooO00oOoo ( __language__ ( 30401 ) . encode ( 'utf8' ) )
  if 7 - 7: iII111i / I1ii11iIi11i / i11iIiiIii
 if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) and args . get ( 'viewage' ) != '21' :
  oOoOO0 = { 'code' : args . get ( 'programid' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'contentid' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 , 'subtitle' : args . get ( 'subtitle' )
 }
  IIIII ( args . get ( 'mode' ) . lower ( ) , oOoOO0 )
  if 78 - 78: Ii1I * i1IIi
  if 1 - 1: I1IiiI / IiII * ooOoO0o
  if 1 - 1: I11i * o0oOOo0O0Ooo . OoOoOO00 / O0
  if 100 - 100: I1Ii111 . o0oOOo0O0Ooo * Oo0Ooo % O0 * O0
def IIIii1 ( args ) :
 i11I1IiII1i1i = args . get ( 'genre' )
 if 71 - 71: II111iiii / i1IIi . I1ii11iIi11i % OoooooooOO . OoOoOO00
 if i11I1IiII1i1i == '-' :
  i11 = 'VOD 시청내역'
  oOoOO0 = { 'mode' : 'WATCH'
 , 'genre' : 'vod'
 }
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 41 - 41: i1IIi * II111iiii / OoooooooOO . OOooOOo
  i11 = '영화 시청내역'
  oOoOO0 [ 'genre' ] = 'movie'
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
  xbmcplugin . endOfDirectory ( i1I1iI )
  if 100 - 100: OoO0O00
 else :
  II1i = Ii1IIIIi1ii1I ( i11I1IiII1i1i )
  if 13 - 13: I1IiiI % OoOoOO00 . I1ii11iIi11i / Oo0Ooo % OOooOOo . OoooooooOO
  for i1iIi in II1i :
   iiiii1II = dict ( urlparse . parse_qsl ( i1iIi ) )
   if 81 - 81: Ii1I * o0oOOo0O0Ooo + I1Ii111 + Oo0Ooo - OoooooooOO
   i11 = iiiii1II . get ( 'title' ) . strip ( )
   oOOoo00O00o = iiiii1II . get ( 'subtitle' ) . strip ( )
   if oOOoo00O00o == 'None' : oOOoo00O00o = ''
   O0O00Oo = iiiii1II . get ( 'img' )
   if 32 - 32: Ii1I * O0
   I111iI = { }
   I111iI [ 'plot' ] = '%s\n%s' % ( i11 , oOOoo00O00o )
   if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
   if i11I1IiII1i1i == 'vod' :
    oOoOO0 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : iiiii1II . get ( 'code' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
    oO00O0O0O = True
   else :
    oOoOO0 = { 'mode' : 'MOVIE'
 , 'contentid' : iiiii1II . get ( 'code' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'title' : i11
 , 'thumbnail' : O0O00Oo
 }
    oO00O0O0O = False
    if 92 - 92: ooOoO0o
   o00O ( i11 , sublabel = oOOoo00O00o , img = O0O00Oo , infoLabels = I111iI , isFolder = oO00O0O0O , params = oOoOO0 )
   if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
  I111iI = { 'plot' : '시청목록을 삭제합니다.' }
  i11 = '*** 시청목록 삭제 ***'
  oOoOO0 = { 'mode' : 'MYVIEW_REMOVE'
 , 'genre' : i11I1IiII1i1i
 }
  if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
  o00O ( i11 , sublabel = '' , img = '' , infoLabels = I111iI , isFolder = False , params = oOoOO0 )
  if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
  xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
  if 92 - 92: I11i . I1Ii111
  if 85 - 85: I1ii11iIi11i . I1Ii111
  if 78 - 78: ooOoO0o * I1Ii111 + iIii1I11I1II1 + iIii1I11I1II1 / I1Ii111 . Ii1I
  if 97 - 97: ooOoO0o / I1Ii111 % i1IIi % I1ii11iIi11i
  if 18 - 18: iIii1I11I1II1 % I11i
def O00oO0 ( args ) :
 i11 = 'VOD 검색'
 oOoOO0 = { 'mode' : 'SEARCH_LIST'
 , 'genre' : 'vod'
 , 'page' : '1'
 }
 o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if 97 - 97: I1Ii111 - iIii1I11I1II1
 i11 = '영화 검색'
 oOoOO0 [ 'genre' ] = 'movie'
 o00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if 75 - 75: OoooooooOO * IiII
 xbmcplugin . endOfDirectory ( i1I1iI )
 if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
 if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
 if 69 - 69: O0
 if 85 - 85: ooOoO0o / O0
def iI1iIIIi1i ( args ) :
 if 89 - 89: iIii1I11I1II1
 iiI1I11i1i . SaveCredential ( IIII ( ) )
 if 21 - 21: I11i % I11i
 oOo0O0o00o = args . get ( 'genre' )
 o00oO0oo0OO = int ( args . get ( 'page' ) )
 if 27 - 27: i11iIiiIii / I1ii11iIi11i
 if 'search_key' in args :
  oOoOOo = args . get ( 'search_key' )
 else :
  oOoOOo = oOOOO ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
  if not oOoOOo : return
  if 3 - 3: O0 / iII111i
 iIiIi1I , oOooO0 = iiI1I11i1i . GetSearchList ( oOoOOo , oOo0O0o00o , o00oO0oo0OO , exclusion21 = o0O00oooo ( ) )
 if 45 - 45: i1IIi + II111iiii
 for IiII1II11I in iIiIi1I :
  i11 = IiII1II11I . get ( 'title' )
  O0O00Oo = IiII1II11I . get ( 'thumbnail' )
  if 54 - 54: IiII + O0 + I11i * I1Ii111 - OOooOOo % oO0o
  I111iI = { }
  I111iI [ 'plot' ] = i11
  if 13 - 13: ooOoO0o / iII111i * OoO0O00 . OoO0O00 * ooOoO0o
  if oOo0O0o00o == 'vod' :
   oOoOO0 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : IiII1II11I . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : ''
   , 'thumbnail' : O0O00Oo
   , 'viewage' : IiII1II11I . get ( 'viewage' )
 }
   oO00O0O0O = True
   if 63 - 63: I1Ii111 / O0 * Oo0Ooo + II111iiii / IiII + Ii1I
  else :
   oOoOO0 = { 'mode' : 'MOVIE'
 , 'contentid' : IiII1II11I . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : ''
   , 'thumbnail' : O0O00Oo
   , 'viewage' : IiII1II11I . get ( 'viewage' )
 }
   if 63 - 63: OoO0O00 + I1ii11iIi11i . I1Ii111 % I1Ii111
   oO00O0O0O = False
   if 57 - 57: II111iiii
  if oOoOO0 . get ( 'viewage' ) == '21' : i11 += ' (%s)' % ( oOoOO0 . get ( 'viewage' ) )
  if 54 - 54: Oo0Ooo + oO0o + i11iIiiIii
  o00O ( i11 , sublabel = '' , img = O0O00Oo , infoLabels = I111iI , isFolder = oO00O0O0O , params = oOoOO0 )
  if 28 - 28: oO0o
 if oOooO0 :
  if 70 - 70: IiII
  oOoOO0 [ 'mode' ] = 'SEARCH_LIST'
  oOoOO0 [ 'genre' ] = oOo0O0o00o
  oOoOO0 [ 'page' ] = str ( o00oO0oo0OO + 1 )
  oOoOO0 [ 'search_key' ] = oOoOOo
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  oOOoo00O00o = str ( o00oO0oo0OO + 1 )
  o00O ( i11 , sublabel = oOOoo00O00o , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 34 - 34: I1Ii111 % IiII
 if len ( iIiIi1I ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI )
 if 3 - 3: II111iiii / OOooOOo + IiII . ooOoO0o . OoO0O00
 if 83 - 83: oO0o + OoooooooOO
 if 22 - 22: Ii1I % iII111i * OoooooooOO - o0oOOo0O0Ooo / iIii1I11I1II1
 if 86 - 86: OoooooooOO . iII111i % OoOoOO00 / I11i * iII111i / o0oOOo0O0Ooo
 if 64 - 64: i11iIiiIii
def Ii1IIIIi1ii1I ( genre ) :
 try :
  I1II = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  with open ( I1II , 'r' ) as I1iIiI11I1 :
   i1oOOoo0o0OOOO = I1iIiI11I1 . readlines ( )
 except :
  i1oOOoo0o0OOOO = [ ]
  if 26 - 26: iII111i % iIii1I11I1II1 + o0oOOo0O0Ooo
 return i1oOOoo0o0OOOO
 if 67 - 67: oO0o + II111iiii - O0 . oO0o * II111iiii * I11i
 if 90 - 90: Ii1I . IiII
 if 81 - 81: OOooOOo - I11i % ooOoO0o - OoO0O00 / Oo0Ooo
 if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
def IIIII ( genre , in_params ) :
 try :
  I1II = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  Ooooo00o0OoO = Ii1IIIIi1ii1I ( genre )
  if 75 - 75: I1IiiI % II111iiii
  with open ( I1II , 'w' ) as I1iIiI11I1 :
   I1I1i1I = urllib . urlencode ( in_params )
   I1I1i1I = I1I1i1I . encode ( 'utf-8' ) + '\n'
   I1iIiI11I1 . write ( I1I1i1I )
   if 87 - 87: O0 / iIii1I11I1II1 * i1IIi
   IIi11IIiIii1 = 0
   for I1iIII1 in Ooooo00o0OoO :
    iIii = dict ( urlparse . parse_qsl ( I1iIII1 ) )
    if in_params . get ( 'code' ) != iIii . get ( 'code' ) :
     I1iIiI11I1 . write ( I1iIII1 )
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
  I1II = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  with open ( I1II , 'w' ) as I1iIiI11I1 :
   I1iIiI11I1 . write ( '' )
 except :
  None
  if 5 - 5: OOooOOo - OOooOOo . Oo0Ooo + OoOoOO00 - OOooOOo . oO0o
  if 31 - 31: II111iiii - iIii1I11I1II1 - iIii1I11I1II1 % I11i
  if 12 - 12: iIii1I11I1II1
  if 20 - 20: o0oOOo0O0Ooo / i1IIi
def oO ( args ) :
 i11I1IiII1i1i = args . get ( 'genre' )
 if 21 - 21: i11iIiiIii / I1Ii111 % OOooOOo * O0 . I11i - iIii1I11I1II1
 O0OOo = xbmcgui . Dialog ( )
 Iiii = O0OOo . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
 if Iiii == False : sys . exit ( )
 if 26 - 26: II111iiii * OoOoOO00
 oOo0oO ( i11I1IiII1i1i )
 if 10 - 10: II111iiii . iII111i
 xbmc . executebuiltin ( "Container.Refresh" )
 if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
 if 88 - 88: iII111i
 if 19 - 19: II111iiii * IiII + Ii1I
 if 65 - 65: OOooOOo . I1Ii111 . OoO0O00 . iII111i - OOooOOo
 if 19 - 19: i11iIiiIii + iII111i % ooOoO0o
 if 14 - 14: OoO0O00 . II111iiii . I11i / Ii1I % I1ii11iIi11i - ooOoO0o
 if 67 - 67: I11i - OOooOOo . i1IIi
 if 35 - 35: iII111i + ooOoO0o - oO0o . iII111i . IiII
 if 87 - 87: OoOoOO00
 if 25 - 25: i1IIi . OoO0O00 - OoOoOO00 / OoO0O00 % OoO0O00 * iIii1I11I1II1
 if 50 - 50: OoO0O00 . i11iIiiIii - oO0o . oO0o
iiI1I11i1i = iIi ( )
i1I1iI = int ( sys . argv [ 1 ] )
if 31 - 31: OOooOOo / Oo0Ooo * i1IIi . OoOoOO00
if 57 - 57: OOooOOo + iIii1I11I1II1 % i1IIi % I1IiiI
if 83 - 83: o0oOOo0O0Ooo / i11iIiiIii % iIii1I11I1II1 . I11i % oO0o . OoooooooOO
if 94 - 94: Ii1I + iIii1I11I1II1 % OoO0O00
oOoOO0 = I1i1I1II ( )
iIiIi11iI = oOoOO0 . get ( 'mode' , None )
if 93 - 93: Ii1I - OOooOOo + iIii1I11I1II1 * o0oOOo0O0Ooo + I1Ii111 . iII111i
o0 ( )
if iIiIi11iI is None :
 if 49 - 49: OoooooooOO * I11i - Oo0Ooo . oO0o
 i1I11i1iI ( )
 if 89 - 89: ooOoO0o + Ii1I * ooOoO0o / ooOoO0o
 if 46 - 46: OoO0O00
 if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
 if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
 if 58 - 58: I11i + II111iiii * iII111i * i11iIiiIii - iIii1I11I1II1
 if 68 - 68: OoooooooOO % II111iiii
 if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
 if 24 - 24: II111iiii % I1Ii111 - ooOoO0o + I1IiiI * I1ii11iIi11i
 if 2 - 2: Ii1I - IiII
elif iIiIi11iI == 'GNB_LIST' :
 ooO00OO0 ( oOoOO0 )
 if 83 - 83: oO0o % o0oOOo0O0Ooo % Ii1I - II111iiii * OOooOOo / OoooooooOO
elif iIiIi11iI == 'GN_LIST' :
 oo000O0OoooO ( oOoOO0 )
 if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
elif iIiIi11iI == 'DEEP_LIST' :
 oOo0O0o00o = oOoOO0 . get ( 'uicode' , None )
 if 71 - 71: OoooooooOO
 if oOo0O0o00o in [ 'quick' , 'vod' , 'program' , 'x' ] :
  Iiii1iI1i ( oOoOO0 )
  if 33 - 33: I1Ii111
 else : None
 if 62 - 62: I1ii11iIi11i + Ii1I + i1IIi / OoooooooOO
elif iIiIi11iI in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
 iii11I ( oOoOO0 )
 xbmc . sleep ( 200 )
 if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
elif iIiIi11iI == 'GN_MYVIEW' :
 IiIiiIIiI ( oOoOO0 )
 if 22 - 22: ooOoO0o - ooOoO0o % OOooOOo . I1Ii111 + oO0o
elif iIiIi11iI == 'MYVIEW_LIST' :
 oO0 ( oOoOO0 )
 if 63 - 63: I1IiiI % I1Ii111 * o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % iII111i
elif iIiIi11iI == 'GENRE' :
 iiIiI1i1 ( oOoOO0 )
 if 45 - 45: IiII
elif iIiIi11iI == 'GENRE_LIST' :
 II ( oOoOO0 )
 if 20 - 20: OoooooooOO * o0oOOo0O0Ooo * O0 . OOooOOo
elif iIiIi11iI == 'WATCH' :
 IIIii1 ( oOoOO0 )
 if 78 - 78: iIii1I11I1II1 + I11i - Ii1I * I1Ii111 - OoooooooOO % OoOoOO00
elif iIiIi11iI == 'MYVIEW_REMOVE' :
 oO ( oOoOO0 )
 if 34 - 34: O0
elif iIiIi11iI == 'SEARCH' :
 O00oO0 ( oOoOO0 )
 if 80 - 80: i1IIi - Oo0Ooo / OoO0O00 - i11iIiiIii
elif iIiIi11iI == 'SEARCH_LIST' :
 iI1iIIIi1i ( oOoOO0 )
 if 68 - 68: oO0o - I1ii11iIi11i % O0 % I1Ii111
elif iIiIi11iI == 'ORDER_BY' :
 oo0o00O ( oOoOO0 )
 if 11 - 11: O0 / OoO0O00 % OOooOOo + o0oOOo0O0Ooo + iIii1I11I1II1
else :
 None
 if 40 - 40: ooOoO0o - OOooOOo . Ii1I * Oo0Ooo % I1Ii111
 if 56 - 56: i11iIiiIii . o0oOOo0O0Ooo - I1IiiI * I11i
 if 91 - 91: oO0o + OoooooooOO - i1IIi
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
