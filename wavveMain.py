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
 iII11i . setProperty ( 'WAVVE_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d %H:%M:%S' ) )
 if 97 - 97: I11i % I11i + II111iiii * iII111i
def o0o00o0 ( ) :
 iII11i = xbmcgui . Window ( 10000 )
 return iII11i . getProperty ( 'WAVVE_M_CREDENTIAL' )
 if 25 - 25: Oo0Ooo - IiII . OoooooooOO
def I11ii1 ( orderby ) :
 iII11i = xbmcgui . Window ( 10000 )
 iII11i . setProperty ( 'WAVVE_M_ORDERBY' , orderby )
 if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
def III1i1i ( ) :
 iII11i = xbmcgui . Window ( 10000 )
 return iII11i . getProperty ( 'WAVVE_M_ORDERBY' )
 if 26 - 26: OoooooooOO
 if 12 - 12: OoooooooOO % OoOoOO00 / ooOoO0o % o0oOOo0O0Ooo
 if 29 - 29: OoooooooOO
def iI ( ) :
 I1i1I1II = urlparse . parse_qs ( sys . argv [ 2 ] [ 1 : ] )
 for i1 in I1i1I1II . keys ( ) :
  I1i1I1II [ i1 ] = I1i1I1II [ i1 ] [ 0 ]
 return I1i1I1II
 if 48 - 48: O0 + O0 - I1ii11iIi11i . ooOoO0o / iIii1I11I1II1
 if 77 - 77: i1IIi % OoOoOO00 - IiII + ooOoO0o
 if 31 - 31: I11i - i1IIi * OOooOOo / OoooooooOO
def iIo00O ( label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
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
  iIo00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = oO00O0O0O , params = oOoOO0 )
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
  try :
   O0oOoOOOoOO = datetime . datetime . strptime ( III1iII1I1ii , '%Y-%m-%d %H:%M:%S' )
  except TypeError :
   import time
   O0oOoOOOoOO = datetime . datetime . fromtimestamp ( time . mktime ( time . strptime ( III1iII1I1ii , '%Y-%m-%d %H:%M:%S' ) ) )
   o000o0o00o0Oo ( 'loginTime_str2 : ' + III1iII1I1ii )
   if 38 - 38: I1Ii111
  if datetime . datetime . now ( ) < O0oOoOOOoOO + datetime . timedelta ( days = 1 ) :
   return
   if 7 - 7: O0 . iII111i % I1ii11iIi11i - I1IiiI - iIii1I11I1II1
   if 36 - 36: IiII % ooOoO0o % Oo0Ooo - I1ii11iIi11i
 if not Ii1IO000OOo00oo . GetCredential ( oo0oOo , o000O0o , iI1iII1 ) :
  ooO00oOoo ( __language__ ( 30103 ) . encode ( 'utf8' ) )
  sys . exit ( )
  if 71 - 71: i11iIiiIii + IiII
  if 57 - 57: oO0o . I11i . i1IIi
 O00 ( Ii1IO000OOo00oo . LoadCredential ( ) )
 I11ii1 ( 'desc' )
 if 42 - 42: I11i + I1ii11iIi11i % O0
 if 6 - 6: oO0o
 if 68 - 68: OoOoOO00 - OoO0O00
 if 28 - 28: OoO0O00 . OOooOOo / OOooOOo + Oo0Ooo . I1ii11iIi11i
def iiii ( args ) :
 II1I = args . get ( 'orderby' )
 if 84 - 84: IiII . i11iIiiIii . IiII * I1ii11iIi11i - I11i
 I11ii1 ( II1I )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 42 - 42: i11iIiiIii
 if 33 - 33: iII111i - O0 * i1IIi * o0oOOo0O0Ooo - Oo0Ooo
 if 32 - 32: OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
 if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
def IIi1I11I1II ( args ) :
 if 63 - 63: OoooooooOO - OoO0O00 . II111iiii / o0oOOo0O0Ooo . OoOoOO00 / O0
 Ii1IO000OOo00oo . SaveCredential ( o0o00o0 ( ) )
 if 84 - 84: IiII
 OOO00O0O = Ii1IO000OOo00oo . GetGnList ( args . get ( 'uicode' ) )
 if 33 - 33: O0 . IiII . I1IiiI
 if 72 - 72: i1IIi / OoO0O00 + OoooooooOO - Oo0Ooo
 if 29 - 29: I1ii11iIi11i + oO0o % O0
 if 10 - 10: I11i / I1Ii111 - I1IiiI * iIii1I11I1II1 - I1IiiI
 for OO0oO0 in OOO00O0O :
  i11 = OO0oO0 . get ( 'title' )
  oOoOO0 = { 'mode' : 'GN_LIST' if OO0oO0 . get ( 'uicode' ) != 'CY1' else 'GN_MYVIEW'
  , 'uicode' : OO0oO0 . get ( 'uicode' )
 , 'came' : args . get ( 'came' )
 , 'page' : '1'
 }
  if 82 - 82: I11i % o0oOOo0O0Ooo % OoO0O00 - Oo0Ooo + OoooooooOO
  iIo00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if len ( OOO00O0O ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 22 - 22: i1IIi + O0 . iIii1I11I1II1 * iII111i % i11iIiiIii * I1IiiI
 if 77 - 77: Oo0Ooo
 if 17 - 17: iII111i % OoO0O00 . OOooOOo + OoO0O00 / II111iiii
 if 75 - 75: I1IiiI - OoOoOO00 % iII111i
def IIiII111iiI1I ( args ) :
 i11 = 'VOD 시청내역'
 oOoOO0 = { 'mode' : 'MYVIEW_LIST'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
 iIo00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if 11 - 11: II111iiii * II111iiii % iIii1I11I1II1 * I1Ii111 + OoOoOO00 / I1IiiI
 i11 = '영화 시청내역'
 oOoOO0 [ 'uicode' ] = 'movie'
 iIo00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if 3 - 3: o0oOOo0O0Ooo
 xbmcplugin . endOfDirectory ( i1I1iI )
 if 24 - 24: i11iIiiIii + iII111i * Ii1I - II111iiii . OOooOOo % iIii1I11I1II1
 if 71 - 71: O0 . iII111i / o0oOOo0O0Ooo
 if 73 - 73: II111iiii . i11iIiiIii / Ii1I + OoOoOO00
 if 12 - 12: i11iIiiIii - i1IIi - OoO0O00 . i1IIi - OOooOOo + O0
def oO0OOOO0 ( args ) :
 if 26 - 26: Ii1I
 Ii1IO000OOo00oo . SaveCredential ( o0o00o0 ( ) )
 if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
 I1i1Iiiii = args . get ( 'uicode' )
 OOo0oO00ooO00 = int ( args . get ( 'page' ) )
 oOO0O00oO0Ooo , oO0Oo0O0o = Ii1IO000OOo00oo . GetMyviewList ( I1i1Iiiii , OOo0oO00ooO00 )
 if 99 - 99: oO0o . iII111i + ooOoO0o % oO0o . i11iIiiIii % O0
 for oOO00O in oOO0O00oO0Ooo :
  i11 = oOO00O . get ( 'title' )
  OOOoo0OO = oOO00O . get ( 'subtitle' )
  oO0o0 = oOO00O . get ( 'thumbnail' )
  if 50 - 50: IiII
  Ii11iIi = { }
  Ii11iIi [ 'plot' ] = i11
  if 55 - 55: I11i * oO0o * o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
  if I1i1Iiiii == 'vod' :
   oOoOO0 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : oOO00O . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : OOOoo0OO
   , 'thumbnail' : oO0o0
   , 'viewage' : oOO00O . get ( 'viewage' )
 }
   oO00O0O0O = True
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  else :
   oOoOO0 = { 'mode' : 'MOVIE'
 , 'contentid' : oOO00O . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : OOOoo0OO
   , 'thumbnail' : oO0o0
   , 'viewage' : oOO00O . get ( 'viewage' )
 }
   oO00O0O0O = False
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
  if oOO00O . get ( 'viewage' ) == '21' : OOOoo0OO += ' (%s)' % ( oOO00O . get ( 'viewage' ) )
  if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
  iIo00O ( i11 , sublabel = OOOoo0OO , img = oO0o0 , infoLabels = Ii11iIi , isFolder = oO00O0O0O , params = oOoOO0 )
  if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
 if oO0Oo0O0o :
  if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
  oOoOO0 [ 'mode' ] = 'MYVIEW_LIST'
  oOoOO0 [ 'uicode' ] = I1i1Iiiii
  oOoOO0 [ 'page' ] = str ( OOo0oO00ooO00 + 1 )
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  OOOoo0OO = str ( OOo0oO00ooO00 + 1 )
  iIo00O ( i11 , sublabel = OOOoo0OO , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
 if len ( oOO0O00oO0Ooo ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 63 - 63: OoOoOO00 * iII111i
 if 69 - 69: O0 . OoO0O00
 if 49 - 49: I1IiiI - I11i
 if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
 if 62 - 62: OoooooooOO * I1IiiI
def oOOOoo0O0oO ( args ) :
 if 6 - 6: OOooOOo * o0oOOo0O0Ooo + iII111i
 Ii1IO000OOo00oo . SaveCredential ( o0o00o0 ( ) )
 if 44 - 44: Ii1I % OoO0O00 + OoooooooOO - O0 - Ii1I - II111iiii
 O0O = args . get ( 'mode' )
 o0oOOoooOOOOo = args . get ( 'uicode' )
 o0oO0O0o0O00O = args . get ( 'genre' )
 OoO000O0Oo = args . get ( 'subgenre' )
 if 63 - 63: iIii1I11I1II1 * i11iIiiIii % iIii1I11I1II1 * i11iIiiIii
 if o0oO0O0o0O00O == '-' :
  iI1111iiii = Ii1IO000OOo00oo . GetGenreGroup ( o0oOOoooOOOOo , o0oO0O0o0O00O , exclusion21 = o0O00oooo ( ) )
 else :
  Oo0OO = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 }
  iI1111iiii = Ii1IO000OOo00oo . GetGenreGroup_sub ( Oo0OO )
  if 78 - 78: OOooOOo - OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii
  if 29 - 29: I1IiiI % I1IiiI
 for Oo0O0 in iI1111iiii :
  i11 = Oo0O0 . get ( 'title' )
  if 82 - 82: II111iiii % I11i / OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / I1Ii111
  oOoOO0 = { 'mode' : O0O
 , 'uicode' : o0oOOoooOOOOo
  , 'genre' : Oo0O0 . get ( 'genre' )
 , 'subgenre' : Oo0O0 . get ( 'subgenre' )
 , 'adult' : Oo0O0 . get ( 'adult' )
 , 'page' : '1'
 , 'broadcastid' : Oo0O0 . get ( 'broadcastid' )
 , 'contenttype' : Oo0O0 . get ( 'contenttype' )
 , 'uiparent' : Oo0O0 . get ( 'uiparent' )
 , 'uirank' : Oo0O0 . get ( 'uirank' )
 , 'uitype' : Oo0O0 . get ( 'uitype' )
 }
  if 70 - 70: oO0o
  if o0oOOoooOOOOo == 'moviegenre' or Oo0O0 . get ( 'subgenre' ) != '-' :
   oOoOO0 [ 'mode' ] = 'GENRE_LIST'
   if 59 - 59: o0oOOo0O0Ooo % oO0o
  else :
   if 6 - 6: iIii1I11I1II1 % i11iIiiIii % I1ii11iIi11i
   None
   if 93 - 93: IiII * OoooooooOO + ooOoO0o
  iIo00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
 if len ( iI1111iiii ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
 if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
 if 26 - 26: Ii1I % I1ii11iIi11i
 if 76 - 76: IiII * iII111i
def ooooooo00o ( args ) :
 if 73 - 73: OOooOOo
 Ii1IO000OOo00oo . SaveCredential ( o0o00o0 ( ) )
 if 70 - 70: iIii1I11I1II1
 o0oOOoooOOOOo = args . get ( 'uicode' )
 OOo0oO00ooO00 = int ( args . get ( 'page' ) )
 if 31 - 31: IiII - I1IiiI % iIii1I11I1II1
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
  if 92 - 92: i1IIi - iIii1I11I1II1
 iI1111iiii , oO0Oo0O0o = Ii1IO000OOo00oo . GetGenreList ( o0oOOoooOOOOo , oOoOO0 , OOo0oO00ooO00 )
 if 16 - 16: OoO0O00 - OoOoOO00 - OOooOOo - i1IIi / Ii1I
 if 88 - 88: OoO0O00
 if 71 - 71: I1ii11iIi11i
 for Oo0O0 in iI1111iiii :
  i11 = Oo0O0 . get ( 'title' )
  oO0o0 = Oo0O0 . get ( 'thumbnail' )
  if 7 - 7: I1ii11iIi11i - I1IiiI . iIii1I11I1II1 - i1IIi
  Ii11iIi = { }
  Ii11iIi [ 'plot' ] = i11
  if 59 - 59: o0oOOo0O0Ooo
  if o0oOOoooOOOOo == 'vodgenre' :
   oOoO00O0 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : Oo0O0 . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : ''
   , 'thumbnail' : oO0o0
   , 'viewage' : Oo0O0 . get ( 'viewage' )
 }
   oO00O0O0O = True
   if 75 - 75: I1IiiI . ooOoO0o . O0 * I1Ii111
  else :
   oOoO00O0 = { 'mode' : 'MOVIE'
 , 'contentid' : Oo0O0 . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : ''
   , 'thumbnail' : oO0o0
   , 'viewage' : Oo0O0 . get ( 'viewage' )
 }
   if 4 - 4: Ii1I % oO0o * OoO0O00
   oO00O0O0O = False
   if 100 - 100: I1Ii111 * OOooOOo + OOooOOo
  if oOoO00O0 . get ( 'viewage' ) == '21' : i11 += ' (%s)' % ( oOoO00O0 . get ( 'viewage' ) )
  if 54 - 54: OoooooooOO + o0oOOo0O0Ooo - i1IIi % i11iIiiIii
  iIo00O ( i11 , sublabel = '' , img = oO0o0 , infoLabels = Ii11iIi , isFolder = oO00O0O0O , params = oOoO00O0 )
  if 3 - 3: o0oOOo0O0Ooo % o0oOOo0O0Ooo
 if oO0Oo0O0o :
  if 83 - 83: II111iiii + I1Ii111
  oOoOO0 [ 'mode' ] = 'GENRE_LIST'
  oOoOO0 [ 'uicode' ] = o0oOOoooOOOOo
  oOoOO0 [ 'page' ] = str ( OOo0oO00ooO00 + 1 )
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  OOOoo0OO = str ( OOo0oO00ooO00 + 1 )
  iIo00O ( i11 , sublabel = OOOoo0OO , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 73 - 73: iII111i
 if len ( iI1111iiii ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 42 - 42: i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . i11iIiiIii % I11i
 if 41 - 41: IiII / O0
 if 51 - 51: I11i % I1IiiI
 if 60 - 60: I1IiiI / OOooOOo . I1IiiI / I1Ii111 . IiII
def OO0000o ( args ) :
 if 42 - 42: Oo0Ooo
 Ii1IO000OOo00oo . SaveCredential ( o0o00o0 ( ) )
 if 76 - 76: I1IiiI * iII111i % I1Ii111
 o0oOOoooOOOOo = args . get ( 'uicode' )
 OoooO00o = args . get ( 'came' )
 OOo0oO00ooO00 = int ( args . get ( 'page' ) )
 if 73 - 73: OOooOOo / oO0o
 if 88 - 88: I11i % I1ii11iIi11i
 if 48 - 48: ooOoO0o / I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / i1IIi
 OOOOoOOo0O0 , oO0Oo0O0o = Ii1IO000OOo00oo . GetDeeplinkList ( o0oOOoooOOOOo , OoooO00o , OOo0oO00ooO00 )
 if 92 - 92: I1ii11iIi11i + iIii1I11I1II1 / II111iiii
 for OooO0OO in OOOOoOOo0O0 :
  i11 = OooO0OO . get ( 'title' )
  OOOoo0OO = OooO0OO . get ( 'subtitle' )
  oO0o0 = OooO0OO . get ( 'thumbnail' )
  o0OOo0o0O0O = OooO0OO . get ( 'uicode' )
  o0OO0o0oOOO0O = OooO0OO . get ( 'channelepg' )
  if 49 - 49: I1ii11iIi11i . o0oOOo0O0Ooo . II111iiii
  oOoOO0 = { 'uicode' : o0OOo0o0O0O
  , 'came' : OoooO00o
 , 'contentid' : OooO0OO . get ( 'contentid' )
 , 'contentidType' : OooO0OO . get ( 'contentidType' )
 , 'page' : '1'
 , 'title' : i11
  , 'subtitle' : OOOoo0OO
  , 'thumbnail' : oO0o0
  , 'viewage' : OooO0OO . get ( 'viewage' )
 }
  if 98 - 98: iII111i
  if o0OOo0o0O0O == 'channel' :
   oOoOO0 [ 'mode' ] = 'LIVE'
  elif o0OOo0o0O0O == 'movie' :
   oOoOO0 [ 'mode' ] = 'MOVIE'
  else :
   oOoOO0 [ 'mode' ] = 'DEEP_LIST'
   if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / II111iiii % Oo0Ooo
   if 38 - 38: ooOoO0o - OOooOOo / iII111i
  Ii11iIi = { }
  if o0OO0o0oOOO0O :
   Ii11iIi [ 'plot' ] = '%s\n\n%s' % ( i11 , o0OO0o0oOOO0O )
  else :
   Ii11iIi [ 'plot' ] = '%s\n\n%s' % ( i11 , OOOoo0OO )
   if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / Ii1I + I1ii11iIi11i
  if OooO0OO . get ( 'viewage' ) == '21' : OOOoo0OO += ' (%s)' % ( OooO0OO . get ( 'viewage' ) )
  if 86 - 86: o0oOOo0O0Ooo
  if o0OOo0o0O0O in [ 'channel' , 'movie' ] :
   oO00O0O0O = False
  elif oOoOO0 [ 'contentidType' ] == 'direct' :
   oO00O0O0O = False
   oOoOO0 [ 'mode' ] = 'VOD'
  else :
   oO00O0O0O = True
   if 5 - 5: IiII * OoOoOO00
   if 5 - 5: I1Ii111
  iIo00O ( i11 , sublabel = OOOoo0OO , img = oO0o0 , infoLabels = Ii11iIi , isFolder = oO00O0O0O , params = oOoOO0 )
  if 90 - 90: I1Ii111 . ooOoO0o / Ii1I - I11i
 if oO0Oo0O0o :
  if 40 - 40: OoooooooOO
  oOoOO0 [ 'mode' ] = 'GN_LIST'
  oOoOO0 [ 'uicode' ] = o0oOOoooOOOOo
  oOoOO0 [ 'page' ] = str ( OOo0oO00ooO00 + 1 )
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  OOOoo0OO = str ( OOo0oO00ooO00 + 1 )
  iIo00O ( i11 , sublabel = OOOoo0OO , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
 if len ( OOOOoOOo0O0 ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
 if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
 if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
def iIiIiIiI ( args ) :
 if 30 - 30: I1Ii111 . ooOoO0o * I1ii11iIi11i
 Ii1IO000OOo00oo . SaveCredential ( o0o00o0 ( ) )
 if 17 - 17: I1IiiI . O0 + OoO0O00
 ii = args . get ( 'contentid' )
 Iiii1iI1i = args . get ( 'contentidType' )
 I1i1Iiiii = args . get ( 'uicode' )
 if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
 OOo0oO00ooO00 = int ( args . get ( 'page' ) )
 if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
 O0O0Oo00 , oO0Oo0O0o = Ii1IO000OOo00oo . GetEpisodeList ( ii , I1i1Iiiii , Iiii1iI1i , OOo0oO00ooO00 , orderby = III1i1i ( ) )
 if 80 - 80: oO0o + OOooOOo / I11i
 for oOOO00O0O0OOo in O0O0Oo00 :
  i11 = oOOO00O0O0OOo . get ( 'title' )
  OOOoo0OO = oOOO00O0O0OOo . get ( 'subtitle' )
  oO0o0 = oOOO00O0O0OOo . get ( 'thumbnail' )
  oOoOO0 = { 'mode' : 'VOD'
 , 'uicode' : oOOO00O0O0OOo . get ( 'uicode' )
  , 'contentid' : oOOO00O0O0OOo . get ( 'contentid' )
 , 'programid' : oOOO00O0O0OOo . get ( 'programid' )
 , 'title' : i11
  , 'subtitle' : OOOoo0OO
  , 'thumbnail' : oO0o0
  , 'viewage' : oOOO00O0O0OOo . get ( 'viewage' )
 }
  if 77 - 77: oO0o + ooOoO0o . Oo0Ooo % Ii1I
  if oOOO00O0O0OOo . get ( 'viewage' ) == '21' : OOOoo0OO += ' (%s)' % ( oOOO00O0O0OOo . get ( 'viewage' ) )
  if 97 - 97: II111iiii . o0oOOo0O0Ooo - I1ii11iIi11i
  o0OOOo = { }
  o0OOOo [ 'plot' ] = oOOO00O0O0OOo . get ( 'synopsis' )
  if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * I1IiiI
  if 46 - 46: OoOoOO00 + OoO0O00
  iIo00O ( i11 , sublabel = OOOoo0OO , img = oO0o0 , infoLabels = o0OOOo , isFolder = False , params = oOoOO0 )
  if 70 - 70: iII111i / iIii1I11I1II1
 if OOo0oO00ooO00 == 1 :
  Ii11iIi = { 'plot' : '정렬순서를 변경합니다.' }
  oOoOO0 = { }
  oOoOO0 [ 'mode' ] = 'ORDER_BY'
  if III1i1i ( ) == 'desc' :
   i11 = '정렬순서변경 : 최신화부터 -> 1회부터'
   oOoOO0 [ 'orderby' ] = 'asc'
  else :
   i11 = '정렬순서변경 : 1회부터 -> 최신화부터'
   oOoOO0 [ 'orderby' ] = 'desc'
  iIo00O ( i11 , sublabel = '' , img = '' , infoLabels = Ii11iIi , isFolder = False , params = oOoOO0 )
  if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
 if oO0Oo0O0o :
  if 96 - 96: OoooooooOO + oO0o
  oOoOO0 [ 'mode' ] = 'DEEP_LIST'
  oOoOO0 [ 'uicode' ] = I1i1Iiiii
  oOoOO0 [ 'contentid' ] = ii
  oOoOO0 [ 'contentidType' ] = Iiii1iI1i
  oOoOO0 [ 'page' ] = str ( OOo0oO00ooO00 + 1 )
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  OOOoo0OO = str ( OOo0oO00ooO00 + 1 )
  iIo00O ( i11 , sublabel = OOOoo0OO , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 44 - 44: oO0o
 if len ( O0O0Oo00 ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
 if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
 if 88 - 88: OoOoOO00 / II111iiii
 if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iII111i + oO0o
def OOooo ( args ) :
 if 31 - 31: o0oOOo0O0Ooo % OoO0O00
 Ii1IO000OOo00oo . SaveCredential ( o0o00o0 ( ) )
 if 14 - 14: oO0o / oO0o % ooOoO0o
 ii = args . get ( 'contentid' )
 I1i1Iiiii = args . get ( 'uicode' )
 ooO = O0O0O ( )
 if 6 - 6: iIii1I11I1II1 . ooOoO0o % o0oOOo0O0Ooo
 o000o0o00o0Oo ( ii + ' - ' + I1i1Iiiii , False )
 I1Iii1 , iiI11Iii , O0o0O0 , Ii1II1I11i1 = Ii1IO000OOo00oo . GetStreamingURL ( ii , I1i1Iiiii , ooO )
 if 59 - 59: oO0o % iIii1I11I1II1 . i1IIi
 if 21 - 21: Oo0Ooo
 I1ii1 = '%s|Cookie=%s' % ( I1Iii1 , iiI11Iii )
 o000o0o00o0Oo ( I1ii1 , False )
 if 99 - 99: ooOoO0o . I1Ii111 % IiII * IiII . i1IIi
 if I1Iii1 == '' :
  ooO00oOoo ( __language__ ( 30303 ) . encode ( 'utf8' ) )
  return
  if 72 - 72: OOooOOo % I1ii11iIi11i + OoO0O00 / oO0o + IiII
 I1I1i = xbmcgui . ListItem ( path = I1ii1 )
 if 1 - 1: I11i % OOooOOo + O0 + i1IIi - OoO0O00
 if O0o0O0 :
  if 22 - 22: I1IiiI % I1ii11iIi11i
  if 57 - 57: OOooOOo + O0 . Ii1I
  iIi1i1iIi1iI = O0o0O0 [ 'customdata' ]
  iiIi1iI1iIii = O0o0O0 [ 'drmhost' ]
  if 68 - 68: OOooOOo
  OooO0oo = 'mpd'
  o0o0oOoOO0O = 'com.widevine.alpha'
  if 16 - 16: IiII % iIii1I11I1II1 . Ii1I
  oooooOOO000Oo = inputstreamhelper . Helper ( OooO0oo , drm = o0o0oOoOO0O )
  if 52 - 52: II111iiii % IiII . OoOoOO00 * iIii1I11I1II1
  if oooooOOO000Oo . check_inputstream ( ) :
   if 50 - 50: ooOoO0o - I1Ii111 * IiII . I1ii11iIi11i
   if I1i1Iiiii == 'movie' :
    I11iiiii1II = 'https://www.wavve.com/player/movie?movieid=%s' % ii
   else :
    I11iiiii1II = 'https://www.wavve.com/player/vod?programid=%s&page=1' % ii
    if 51 - 51: O0 % oO0o - II111iiii
   I1II = { 'content-type' : 'application/octet-stream'
 , 'origin' : 'https://www.wavve.com'
 , 'pallycon-customdata' : iIi1i1iIi1iI
 , 'referer' : I11iiiii1II
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'

   , 'user-agent' : oo00
 }
   Oo000ooOOO = iiIi1iI1iIii + '|' + urllib . urlencode ( I1II ) + '|R{SSM}|'
   if 31 - 31: iIii1I11I1II1 % I11i % ooOoO0o . Ii1I - I11i
   I1I1i . setProperty ( 'inputstreamaddon' , oooooOOO000Oo . inputstream_addon )
   I1I1i . setProperty ( 'inputstream.adaptive.manifest_type' , OooO0oo )
   I1I1i . setProperty ( 'inputstream.adaptive.license_type' , o0o0oOoOO0O )
   if 17 - 17: Ii1I
   I1I1i . setProperty ( 'inputstream.adaptive.license_key' , Oo000ooOOO )
   I1I1i . setProperty ( 'inputstream.adaptive.stream_headers' , 'Cookie=%s' % iiI11Iii )
   if 27 - 27: i11iIiiIii % II111iiii % I11i . O0 - Oo0Ooo + OoOoOO00
 xbmcplugin . setResolvedUrl ( i1I1iI , True , I1I1i )
 if 57 - 57: iIii1I11I1II1 / I11i - i1IIi
 if Ii1II1I11i1 :
  ooO00oOoo ( Ii1II1I11i1 . encode ( 'utf-8' ) )
 else :
  if '/preview.' in urlparse . urlsplit ( I1Iii1 ) . path : ooO00oOoo ( __language__ ( 30401 ) . encode ( 'utf8' ) )
  if 51 - 51: IiII
 if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) and args . get ( 'viewage' ) != '21' :
  oOoOO0 = { 'code' : args . get ( 'programid' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'contentid' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 , 'subtitle' : args . get ( 'subtitle' )
 }
  ii11I1 ( args . get ( 'mode' ) . lower ( ) , oOoOO0 )
  if 75 - 75: OoO0O00 / II111iiii % O0
  if 38 - 38: OoooooooOO * ooOoO0o % O0 * OoOoOO00
  if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - Ii1I
  if 20 - 20: i1IIi % OoO0O00 . I1IiiI / IiII * i11iIiiIii * OOooOOo
def OOo ( args ) :
 o0oO0O0o0O00O = args . get ( 'genre' )
 if 50 - 50: ooOoO0o
 if o0oO0O0o0O00O == '-' :
  i11 = 'VOD 시청내역'
  oOoOO0 = { 'mode' : 'WATCH'
 , 'genre' : 'vod'
 }
  iIo00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 72 - 72: I1Ii111
  i11 = '영화 시청내역'
  oOoOO0 [ 'genre' ] = 'movie'
  iIo00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iII111i
  xbmcplugin . endOfDirectory ( i1I1iI )
  if 8 - 8: ooOoO0o + II111iiii / iII111i / I11i
 else :
  ooo0O = iII1iii ( o0oO0O0o0O00O )
  if 12 - 12: OOooOOo
  for O0iII1 in ooo0O :
   II = dict ( urlparse . parse_qsl ( O0iII1 ) )
   if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
   i11 = II . get ( 'title' ) . strip ( )
   OOOoo0OO = II . get ( 'subtitle' ) . strip ( )
   if OOOoo0OO == 'None' : OOOoo0OO = ''
   oO0o0 = II . get ( 'img' )
   if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
   Ii11iIi = { }
   Ii11iIi [ 'plot' ] = '%s\n%s' % ( i11 , OOOoo0OO )
   if 45 - 45: I1Ii111
   if o0oO0O0o0O00O == 'vod' :
    oOoOO0 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : II . get ( 'code' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
    oO00O0O0O = True
   else :
    oOoOO0 = { 'mode' : 'MOVIE'
 , 'contentid' : II . get ( 'code' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'title' : i11
 , 'thumbnail' : oO0o0
 }
    oO00O0O0O = False
    if 83 - 83: OoOoOO00 . OoooooooOO
   iIo00O ( i11 , sublabel = OOOoo0OO , img = oO0o0 , infoLabels = Ii11iIi , isFolder = oO00O0O0O , params = oOoOO0 )
   if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
  Ii11iIi = { 'plot' : '시청목록을 삭제합니다.' }
  i11 = '*** 시청목록 삭제 ***'
  oOoOO0 = { 'mode' : 'MYVIEW_REMOVE'
 , 'genre' : o0oO0O0o0O00O
 }
  if 62 - 62: OoO0O00 / I1ii11iIi11i
  iIo00O ( i11 , sublabel = '' , img = '' , infoLabels = Ii11iIi , isFolder = False , params = oOoOO0 )
  if 7 - 7: OoooooooOO . IiII
  xbmcplugin . endOfDirectory ( i1I1iI , cacheToDisc = False )
  if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
  if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
  if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
  if 92 - 92: ooOoO0o
  if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
def Oo00OoOo ( args ) :
 i11 = 'VOD 검색'
 oOoOO0 = { 'mode' : 'SEARCH_LIST'
 , 'genre' : 'vod'
 , 'page' : '1'
 }
 iIo00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if 24 - 24: i11iIiiIii - I1Ii111
 i11 = '영화 검색'
 oOoOO0 [ 'genre' ] = 'movie'
 iIo00O ( i11 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
 if 21 - 21: I11i
 xbmcplugin . endOfDirectory ( i1I1iI )
 if 92 - 92: i11iIiiIii / I1Ii111 - iII111i % ooOoO0o * I1Ii111 + Oo0Ooo
 if 11 - 11: OoooooooOO . I1Ii111
 if 80 - 80: OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / I1IiiI / OOooOOo
 if 13 - 13: I1Ii111 * ooOoO0o + i11iIiiIii * I1Ii111 - ooOoO0o
def Ii1i1i1i1I1Ii ( args ) :
 if 25 - 25: II111iiii
 Ii1IO000OOo00oo . SaveCredential ( o0o00o0 ( ) )
 if 11 - 11: Oo0Ooo
 I1i1Iiiii = args . get ( 'genre' )
 OOo0oO00ooO00 = int ( args . get ( 'page' ) )
 if 74 - 74: OoOoOO00 * o0oOOo0O0Ooo + OoOoOO00 . OOooOOo * OoooooooOO % O0
 if 'search_key' in args :
  o0ooO = args . get ( 'search_key' )
 else :
  o0ooO = oOOOO ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
  if not o0ooO : return
  if 74 - 74: O0 * oO0o - i11iIiiIii + I1Ii111
 Iii , oO0Oo0O0o = Ii1IO000OOo00oo . GetSearchList ( o0ooO , I1i1Iiiii , OOo0oO00ooO00 , exclusion21 = o0O00oooo ( ) )
 if 19 - 19: I11i % II111iiii / i11iIiiIii / iII111i - OoooooooOO
 for iIIii in Iii :
  i11 = iIIii . get ( 'title' )
  oO0o0 = iIIii . get ( 'thumbnail' )
  if 18 - 18: iII111i . I1IiiI
  Ii11iIi = { }
  Ii11iIi [ 'plot' ] = i11
  if 40 - 40: O0 - OoooooooOO - IiII
  if I1i1Iiiii == 'vod' :
   oOoOO0 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : iIIii . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : ''
   , 'thumbnail' : oO0o0
   , 'viewage' : iIIii . get ( 'viewage' )
 }
   oO00O0O0O = True
   if 37 - 37: OoOoOO00 / II111iiii / O0
  else :
   oOoOO0 = { 'mode' : 'MOVIE'
 , 'contentid' : iIIii . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : i11
   , 'subtitle' : ''
   , 'thumbnail' : oO0o0
   , 'viewage' : iIIii . get ( 'viewage' )
 }
   if 76 - 76: I1IiiI . ooOoO0o - I1ii11iIi11i - iII111i * OoO0O00
   oO00O0O0O = False
   if 54 - 54: IiII + O0 + I11i * I1Ii111 - OOooOOo % oO0o
  if oOoOO0 . get ( 'viewage' ) == '21' : i11 += ' (%s)' % ( oOoOO0 . get ( 'viewage' ) )
  if 13 - 13: ooOoO0o / iII111i * OoO0O00 . OoO0O00 * ooOoO0o
  iIo00O ( i11 , sublabel = '' , img = oO0o0 , infoLabels = Ii11iIi , isFolder = oO00O0O0O , params = oOoOO0 )
  if 63 - 63: I1Ii111 / O0 * Oo0Ooo + II111iiii / IiII + Ii1I
 if oO0Oo0O0o :
  if 63 - 63: OoO0O00 + I1ii11iIi11i . I1Ii111 % I1Ii111
  oOoOO0 [ 'mode' ] = 'SEARCH_LIST'
  oOoOO0 [ 'genre' ] = I1i1Iiiii
  oOoOO0 [ 'page' ] = str ( OOo0oO00ooO00 + 1 )
  oOoOO0 [ 'search_key' ] = o0ooO
  i11 = '[B]%s >>[/B]' % '다음 페이지'
  OOOoo0OO = str ( OOo0oO00ooO00 + 1 )
  iIo00O ( i11 , sublabel = OOOoo0OO , img = '' , infoLabels = None , isFolder = True , params = oOoOO0 )
  if 57 - 57: II111iiii
 if len ( Iii ) > 0 : xbmcplugin . endOfDirectory ( i1I1iI )
 if 54 - 54: Oo0Ooo + oO0o + i11iIiiIii
 if 28 - 28: oO0o
 if 70 - 70: IiII
 if 34 - 34: I1Ii111 % IiII
 if 3 - 3: II111iiii / OOooOOo + IiII . ooOoO0o . OoO0O00
def iII1iii ( genre ) :
 try :
  oOoo000 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  with open ( oOoo000 , 'r' ) as OooOo00o :
   IiI11i1IIiiI = OooOo00o . readlines ( )
 except :
  IiI11i1IIiiI = [ ]
  if 60 - 60: I1ii11iIi11i * I1IiiI
 return IiI11i1IIiiI
 if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
 if 41 - 41: Ii1I
 if 77 - 77: I1Ii111
 if 65 - 65: II111iiii . I1IiiI % oO0o * OoO0O00
def ii11I1 ( genre , in_params ) :
 try :
  oOoo000 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  iI11I = iII1iii ( genre )
  if 11 - 11: iII111i - oO0o + II111iiii - iIii1I11I1II1
  with open ( oOoo000 , 'w' ) as OooOo00o :
   I1i11ii11 = urllib . urlencode ( in_params )
   I1i11ii11 = I1i11ii11 . encode ( 'utf-8' ) + '\n'
   OooOo00o . write ( I1i11ii11 )
   if 81 - 81: OOooOOo - I11i % ooOoO0o - OoO0O00 / Oo0Ooo
   Ii1iI111 = 0
   for O0oooo00o0Oo in iI11I :
    I1iii = dict ( urlparse . parse_qsl ( O0oooo00o0Oo ) )
    if in_params . get ( 'code' ) != I1iii . get ( 'code' ) :
     OooOo00o . write ( O0oooo00o0Oo )
     Ii1iI111 += 1
     if Ii1iI111 >= 50 : break
 except :
  None
  if 86 - 86: I1ii11iIi11i * O0 * IiII
  if 51 - 51: II111iiii + IiII . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
  if 72 - 72: oO0o + oO0o / II111iiii . OoooooooOO % Ii1I
  if 49 - 49: oO0o . OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
def ii1Ii1IiIIi ( genre ) :
 try :
  oOoo000 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  with open ( oOoo000 , 'w' ) as OooOo00o :
   OooOo00o . write ( '' )
 except :
  None
  if 83 - 83: I11i / I1ii11iIi11i
  if 34 - 34: I1IiiI * Oo0Ooo * I1Ii111 / OoO0O00 * I11i / iIii1I11I1II1
  if 74 - 74: Oo0Ooo / i11iIiiIii - II111iiii * o0oOOo0O0Ooo
  if 5 - 5: OOooOOo - OOooOOo . Oo0Ooo + OoOoOO00 - OOooOOo . oO0o
def IiIi1i1ii ( args ) :
 o0oO0O0o0O00O = args . get ( 'genre' )
 if 11 - 11: II111iiii / o0oOOo0O0Ooo
 O0OOo = xbmcgui . Dialog ( )
 Iiii = O0OOo . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
 if Iiii == False : sys . exit ( )
 if 21 - 21: i11iIiiIii / i1IIi + I1IiiI * OOooOOo . I1Ii111
 ii1Ii1IiIIi ( o0oO0O0o0O00O )
 if 84 - 84: O0 . I11i - II111iiii . ooOoO0o / II111iiii
 xbmc . executebuiltin ( "Container.Refresh" )
 if 47 - 47: OoooooooOO
 if 4 - 4: I1IiiI % I11i
 if 10 - 10: IiII . OoooooooOO - OoO0O00 + IiII - O0
 if 82 - 82: ooOoO0o + II111iiii
 if 39 - 39: oO0o % iIii1I11I1II1 % O0 % OoooooooOO * I1ii11iIi11i + iII111i
 if 68 - 68: Oo0Ooo + i11iIiiIii
 if 69 - 69: iIii1I11I1II1 * iIii1I11I1II1 * i11iIiiIii + I1IiiI / OOooOOo % Ii1I
 if 58 - 58: OOooOOo * o0oOOo0O0Ooo + O0 % OOooOOo
 if 25 - 25: Oo0Ooo % I1ii11iIi11i * ooOoO0o
 if 6 - 6: iII111i . IiII * OoOoOO00 . i1IIi
 if 98 - 98: i1IIi
Ii1IO000OOo00oo = iIi ( )
i1I1iI = int ( sys . argv [ 1 ] )
if 65 - 65: OoOoOO00 / OoO0O00 % IiII
if 45 - 45: OoOoOO00
if 66 - 66: OoO0O00
if 56 - 56: O0
oOoOO0 = iI ( )
O0O = oOoOO0 . get ( 'mode' , None )
if 61 - 61: o0oOOo0O0Ooo / OOooOOo / Oo0Ooo * O0
o0 ( )
if O0O is None :
 if 23 - 23: oO0o - OOooOOo + I11i
 i1I11i1iI ( )
 if 12 - 12: I1IiiI / ooOoO0o % o0oOOo0O0Ooo / i11iIiiIii % OoooooooOO
 if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo0Ooo * Ii1I + I11i
 if 11 - 11: iII111i * Ii1I - OoOoOO00
 if 66 - 66: OoOoOO00 . i11iIiiIii - iII111i * o0oOOo0O0Ooo + OoooooooOO * I1ii11iIi11i
 if 74 - 74: Oo0Ooo
 if 61 - 61: Oo0Ooo - I1Ii111 * II111iiii % ooOoO0o * iIii1I11I1II1 + OoO0O00
 if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
 if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
 if 58 - 58: I11i + II111iiii * iII111i * i11iIiiIii - iIii1I11I1II1
elif O0O == 'GNB_LIST' :
 IIi1I11I1II ( oOoOO0 )
 if 68 - 68: OoooooooOO % II111iiii
elif O0O == 'GN_LIST' :
 OO0000o ( oOoOO0 )
 if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
elif O0O == 'DEEP_LIST' :
 I1i1Iiiii = oOoOO0 . get ( 'uicode' , None )
 if 24 - 24: II111iiii % I1Ii111 - ooOoO0o + I1IiiI * I1ii11iIi11i
 if I1i1Iiiii in [ 'quick' , 'vod' , 'program' , 'x' ] :
  iIiIiIiI ( oOoOO0 )
  if 2 - 2: Ii1I - IiII
 else : None
 if 83 - 83: oO0o % o0oOOo0O0Ooo % Ii1I - II111iiii * OOooOOo / OoooooooOO
elif O0O in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
 OOooo ( oOoOO0 )
 xbmc . sleep ( 200 )
 if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
elif O0O == 'GN_MYVIEW' :
 IIiII111iiI1I ( oOoOO0 )
 if 71 - 71: OoooooooOO
elif O0O == 'MYVIEW_LIST' :
 oO0OOOO0 ( oOoOO0 )
 if 33 - 33: I1Ii111
elif O0O == 'GENRE' :
 oOOOoo0O0oO ( oOoOO0 )
 if 62 - 62: I1ii11iIi11i + Ii1I + i1IIi / OoooooooOO
elif O0O == 'GENRE_LIST' :
 ooooooo00o ( oOoOO0 )
 if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
elif O0O == 'WATCH' :
 OOo ( oOoOO0 )
 if 22 - 22: ooOoO0o - ooOoO0o % OOooOOo . I1Ii111 + oO0o
elif O0O == 'MYVIEW_REMOVE' :
 IiIi1i1ii ( oOoOO0 )
 if 63 - 63: I1IiiI % I1Ii111 * o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % iII111i
elif O0O == 'SEARCH' :
 Oo00OoOo ( oOoOO0 )
 if 45 - 45: IiII
elif O0O == 'SEARCH_LIST' :
 Ii1i1i1i1I1Ii ( oOoOO0 )
 if 20 - 20: OoooooooOO * o0oOOo0O0Ooo * O0 . OOooOOo
elif O0O == 'ORDER_BY' :
 iiii ( oOoOO0 )
 if 78 - 78: iIii1I11I1II1 + I11i - Ii1I * I1Ii111 - OoooooooOO % OoOoOO00
else :
 None
 if 34 - 34: O0
 if 80 - 80: i1IIi - Oo0Ooo / OoO0O00 - i11iIiiIii
 if 68 - 68: oO0o - I1ii11iIi11i % O0 % I1Ii111
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
