# -*- coding: utf-8 -*-
__author__ = "NightRain"
if 64 - 64: i11iIiiIii
import urllib
import urllib2
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import cookielib
import re
import json
import sys
import urlparse
if 73 - 73: II111iiii
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
IiiIII111iI = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . OoO0O00 - I1ii11iIi11i
if 53 - 53: I11i / Oo0Ooo / II111iiii % Ii1I / OoOoOO00 . Oo0ooO0oo0oO
class oo00 ( object ) :
 def __init__ ( self ) :
  if 88 - 88: iii1I1I . oO0o % Oo0ooO0oo0oO
  self . MyCookie = cookielib . LWPCookieJar ( )
  if 66 - 66: iii1I1I
  self . Opener = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( self . MyCookie ) )
  self . Opener . addheaders = [ ( 'User-Agent' , IiiIII111iI ) ]
  if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - oO0o
  urllib2 . install_opener ( self . Opener )
  if 72 - 72: II111iiii - OoOoOO00
  if 91 - 91: OoO0O00 . i11iIiiIii / oO0o % I11i / OoO0O00 - i11iIiiIii
 def Request ( self , url , postdata = None ) :
  if postdata :
   II1Iiii1111i = self . Opener . open ( url , postdata )
  else :
   II1Iiii1111i = self . Opener . open ( url )
   if 25 - 25: Ii1I
  oo00000o0 = II1Iiii1111i . read ( )
  II1Iiii1111i . close ( )
  if 34 - 34: O00oOoOoO0o0O % II111iiii % iIii1I11I1II1 % O00oOoOoO0o0O * iii1I1I / OoOoOO00
  return oo00000o0
  if 31 - 31: i11iIiiIii / I1IiiI / Oo0ooO0oo0oO * oO0o / Oo0Ooo
 def Request2 ( self , url , params = None , postdata = None ) :
  import requests
  Oo0o0ooO0oOOO = { 'User-Agent' : IiiIII111iI }
  if 58 - 58: i11iIiiIii % O0oo0OO0
  if postdata :
   II1Iiii1111i = requests . post ( url , headers = Oo0o0ooO0oOOO , params = params , data = postdata )
  else :
   II1Iiii1111i = requests . get ( url , headers = Oo0o0ooO0oOOO , params = params )
   if 54 - 54: OOooOOo % O0 + I1IiiI - iii1I1I / I11i
  oo00000o0 = II1Iiii1111i . json ( )
  return oo00000o0
  if 31 - 31: OoO0O00 + II111iiii
  if 13 - 13: OOooOOo * oO0o * I1IiiI
  if 55 - 55: II111iiii
  if 43 - 43: OoOoOO00 - i1IIi + O0oo0OO0 + Ii1I
class iII111ii ( object ) :
 def __init__ ( self ) :
  self . SESSION = oo00 ( )
  self . API_DOMAIN = 'https://apis.pooq.co.kr'
  self . APIKEY = 'E5F3E0D30947AA5440556471321BB6D9'
  self . CREDENTIAL = 'none'
  self . DEVICE = 'pc'
  self . DRM = 'wm'
  self . PARTNER = 'pooq'
  self . POOQZONE = 'none'
  self . REGION = 'kor'
  if 3 - 3: iii1I1I + O0
  self . TARGETAGE = 'all'
  self . HTTPTAG = 'https://'
  self . LIST_LIMIT = 30
  self . EP_LIMIT = 30
  self . MV_LIMIT = 24
  self . guid = 'none'
  self . guidtimestamp = 'none'
  if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
 def SaveCredential ( self , credential ) :
  self . CREDENTIAL = credential
  if 78 - 78: OoO0O00
 def LoadCredential ( self ) :
  return self . CREDENTIAL
  if 18 - 18: O0 - iii1I1I / iii1I1I + Oo0ooO0oo0oO % Oo0ooO0oo0oO - O00oOoOoO0o0O
 def GetDefaultParams ( self ) :
  O0O00Ooo = { 'apikey' : self . APIKEY ,
 'credential' : self . CREDENTIAL ,
 'device' : self . DEVICE ,
 'drm' : self . DRM ,
 'partner' : self . PARTNER ,
 'pooqzone' : self . POOQZONE ,
 'region' : self . REGION ,
 'targetage' : self . TARGETAGE
 }
  return O0O00Ooo
  if 64 - 64: oO0o - O0 / II111iiii / o0oOOo0O0Ooo / iIii1I11I1II1
 def makeurl ( self , domain , path , query = None ) :
  IiIIIiI1I1 = ''
  if domain :
   if re . search ( r'http[s]*://' , domain ) :
    IiIIIiI1I1 += domain
   else :
    IiIIIiI1I1 += 'http://%s' % domain
   if path :
    IiIIIiI1I1 += path
    if query : IiIIIiI1I1 += '?%s' % query
  return IiIIIiI1I1
  if 86 - 86: i11iIiiIii + Ii1I + Oo0ooO0oo0oO * I11i + o0oOOo0O0Ooo
 def MakeServiceUrl ( self , path , params ) :
  if 61 - 61: OoO0O00 / i11iIiiIii
  IiIIIiI1I1 = self . makeurl ( self . API_DOMAIN , path , urllib . urlencode ( params ) )
  return IiIIIiI1I1
  if 34 - 34: OoooooooOO + iIii1I11I1II1 + i11iIiiIii - I1ii11iIi11i + i11iIiiIii
 def GetGUID ( self , guid_str = 'POOQ' , guidType = 1 ) :
  if 65 - 65: OoOoOO00
  def ii1I ( media ) :
   from datetime import datetime
   OooO0 = datetime . now ( ) . strftime ( '%Y%m%d%H%M%S' )
   II11iiii1Ii = OO0o ( 5 )
   Ooo = II11iiii1Ii + media + OooO0
   return Ooo
   if 68 - 68: I11i + OOooOOo . iIii1I11I1II1 - O00oOoOoO0o0O % iIii1I11I1II1 - Oo0ooO0oo0oO
  def OO0o ( num ) :
   from random import randint
   oOOO00o = ""
   for O0O00o0OOO0 in range ( 0 , num ) :
    Ii1iIIIi1ii = str ( randint ( 1 , 5 ) )
    oOOO00o += Ii1iIIIi1ii
   return oOOO00o
   if 80 - 80: I11i * i11iIiiIii / O0oo0OO0
  Ooo = ii1I ( guid_str )
  if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
  III1i1i = self . GetHash ( Ooo )
  if guidType == 2 :
   III1i1i = '%s-%s-%s-%s-%s' % ( III1i1i [ : 8 ] , III1i1i [ 8 : 12 ] , III1i1i [ 12 : 16 ] , III1i1i [ 16 : 20 ] , III1i1i [ 20 : ] )
   if 26 - 26: OoooooooOO
  return III1i1i
  if 12 - 12: OoooooooOO % OoOoOO00 / Oo0ooO0oo0oO % o0oOOo0O0Ooo
 def GetHash ( self , hash_str ) :
  import hashlib
  iiii = hashlib . md5 ( )
  if 54 - 54: I1ii11iIi11i * OOooOOo
  iiii . update ( hash_str )
  return str ( iiii . hexdigest ( ) )
  if 13 - 13: O00oOoOoO0o0O + OoOoOO00 - OoooooooOO + O0oo0OO0 . iii1I1I + OoO0O00
 def CheckQuality ( self , sel_qt , qt_list ) :
  Ii = 0
  for oo0O0oOOO00oO in qt_list :
   if sel_qt >= oo0O0oOOO00oO : return oo0O0oOOO00oO
   Ii = oo0O0oOOO00oO
  return Ii
  if 61 - 61: i1IIi * OOooOOo / OoooooooOO . i11iIiiIii . OoOoOO00
  if 60 - 60: I11i / I11i
 def GetCredential ( self , user_id , user_pw , user_pf ) :
  I1II1III11iii = False
  try :
   Oo000 = '/login'
   O0O00Ooo = self . GetDefaultParams ( )
   oo = { 'id' : user_id
 , 'password' : user_pw
 , 'profile' : '0'
 , 'pushid' : ''
 , 'type' : 'general'
 }
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   if 44 - 44: O0 / Oo0ooO0oo0oO
   if 84 - 84: Oo0ooO0oo0oO * II111iiii % Ii1I . OoOoOO00
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 , postdata = urllib . urlencode ( oo ) )
   OOOO = json . loads ( II1Iiii1111i )
   if 10 - 10: OOooOOo / I1IiiI * OOooOOo
   IIIii1II1II = OOOO [ 'credential' ]
   if 42 - 42: Ii1I + oO0o
   if 76 - 76: O0oo0OO0 - OoO0O00
   if user_pf != 0 :
    oo = { 'id' : IIIii1II1II
 , 'password' : ''
 , 'profile' : str ( user_pf )
 , 'pushid' : ''
 , 'type' : 'credential'
 }
    if 70 - 70: Oo0ooO0oo0oO
    O0O00Ooo [ 'credential' ] = IIIii1II1II
    II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 , postdata = urllib . urlencode ( oo ) )
    OOOO = json . loads ( II1Iiii1111i )
    IIIii1II1II = OOOO [ 'credential' ]
    if 61 - 61: I1ii11iIi11i . I1ii11iIi11i
    if 10 - 10: OoOoOO00 * iii1I1I . I11i + II111iiii - Oo0ooO0oo0oO * i1IIi
   if IIIii1II1II : I1II1III11iii = True
   if 56 - 56: o0oOOo0O0Ooo * O00oOoOoO0o0O * II111iiii
   if 80 - 80: o0oOOo0O0Ooo * II111iiii % II111iiii
  except Exception as OoOOOOO :
   print ( OoOOOOO )
   IIIii1II1II = 'none'
   if 33 - 33: I1ii11iIi11i % i1IIi
  self . SaveCredential ( IIIii1II1II )
  return I1II1III11iii
  if 78 - 78: I11i
 def GetIssue ( self ) :
  OO00Oo = False
  try :
   Oo000 = '/guid/issue'
   O0O00Ooo = self . GetDefaultParams ( )
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   if 51 - 51: O00oOoOoO0o0O * o0oOOo0O0Ooo + I11i + OoO0O00
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   if 66 - 66: OoOoOO00
   OOOO = json . loads ( II1Iiii1111i )
   oO000Oo000 = OOOO [ 'guid' ]
   i111IiI1I = OOOO [ 'guidtimestamp' ]
   if oO000Oo000 : OO00Oo = True
  except Exception as OoOOOOO :
   print ( OoOOOOO )
   oO000Oo000 = 'none'
   i111IiI1I = 'none'
   if 70 - 70: Ii1I . Oo0Ooo / o0oOOo0O0Ooo . Ii1I - O0 / O00oOoOoO0o0O
  self . guid = oO000Oo000
  self . guidtimestamp = i111IiI1I
  if 62 - 62: iIii1I11I1II1 * OoOoOO00
  return OO00Oo
  if 26 - 26: iii1I1I . O0oo0OO0
 def GetGnList ( self , gn_str ) :
  oOOOOo0 = [ ]
  try :
   Oo000 = '/cf/supermultisections/' + gn_str
   O0O00Ooo = self . GetDefaultParams ( )
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   if 20 - 20: i1IIi + I1ii11iIi11i - Oo0ooO0oo0oO
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 30 - 30: II111iiii - OOooOOo - i11iIiiIii % OoOoOO00 - II111iiii * Ii1I
   if not ( 'multisectionlist' in OOOO ) : return None
   oO00O0O0O = OOOO [ 'multisectionlist' ]
   if 31 - 31: I11i - II111iiii . I11i
   if 18 - 18: o0oOOo0O0Ooo
   for O0o0O00Oo0o0 in oO00O0O0O :
    O00O0oOO00O00 = O0o0O00Oo0o0 [ 'title' ]
    if len ( O00O0oOO00O00 ) == 0 : continue
    if O00O0oOO00O00 == 'minor' : continue
    if 11 - 11: O00oOoOoO0o0O . I1ii11iIi11i
    if re . search ( u'베너' , O00O0oOO00O00 ) : continue
    if 92 - 92: iii1I1I . O0oo0OO0
    O00O0oOO00O00 = re . sub ( '\n|\!|\~|(@0@)|(@\^0@)' , '' , O00O0oOO00O00 )
    O00O0oOO00O00 = O00O0oOO00O00 . lstrip ( '#' )
    if 31 - 31: O0oo0OO0 . OoOoOO00 / O0
    for o000O0o in O0o0O00Oo0o0 [ 'eventlist' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , o000O0o ) :
      iI1iII1 = { 'title' : unicode ( O00O0oOO00O00 )
 , 'uicode' : re . sub ( r'uicode:' , '' , o000O0o )
 }
      oOOOOo0 . append ( iI1iII1 )
      break
      if 86 - 86: OOooOOo
  except Exception as OoOOOOO :
   print ( OoOOOOO )
   if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
  return oOOOOo0
  if 25 - 25: I1ii11iIi11i
 def GetDeeplinkList ( self , gn_str , came_str , page_int , addinfoyn = False ) :
  Ii1i = [ ]
  I1 = iiIii = 1
  ooo0O = 'quick'
  oOoO0o00OO0 = i1I1ii = oOOo0 = ''
  oo00O00oO = False
  iIiIIIi = { }
  if 93 - 93: iii1I1I
  try :
   if 10 - 10: I11i
   Oo000 = '/cf/deeplink/' + gn_str
   O0O00Ooo = self . GetDefaultParams ( )
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
   if not ( 'url' in OOOO ) : return None
   OOOOoOoo0O0O0 = OOOO [ 'url' ]
   if 85 - 85: oO0o % i11iIiiIii - iii1I1I * OoooooooOO / I1IiiI % I1IiiI
   print OOOOoOoo0O0O0
   if 1 - 1: OoO0O00 - oO0o . I11i . OoO0O00 / Oo0Ooo + I11i
   if 78 - 78: O0 . oO0o . II111iiii % OOooOOo
   Oo000 = urlparse . urlsplit ( OOOOoOoo0O0O0 ) . path
   i1iIi = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( OOOOoOoo0O0O0 ) . query ) )
   if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
   i1iIi [ 'came' ] = came_str
   i1iIi [ 'limit' ] = str ( self . LIST_LIMIT )
   if 'contenttype' in i1iIi : ooo0O = i1iIi [ 'contenttype' ]
   if came_str == 'movie' : i1iIi [ 'mtype' ] = 'svod'
   if 31 - 31: II111iiii . I1IiiI
   if page_int != 1 :
    i1iIi [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
    i1iIi [ 'page' ] = str ( page_int )
    if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iii1I1I * O00oOoOoO0o0O . i11iIiiIii
   IiIIIiI1I1 = self . HTTPTAG + Oo000 + '?' + urllib . urlencode ( i1iIi ) + '&' + urllib . urlencode ( O0O00Ooo )
   if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % iii1I1I
   if 92 - 92: iii1I1I
   if 25 - 25: Oo0Ooo - I1IiiI / OoooooooOO / o0oOOo0O0Ooo
   if 12 - 12: I1IiiI * iii1I1I % i1IIi % iIii1I11I1II1
   if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
   if 45 - 45: oO0o - O00oOoOoO0o0O - OoooooooOO - OoO0O00 . II111iiii / O0
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 51 - 51: O0 + iii1I1I
   if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
   if not ( 'celllist' in OOOO [ 'cell_toplist' ] ) : return Ii1i , oo00O00oO
   ii = OOOO [ 'cell_toplist' ] [ 'celllist' ]
   if 90 - 90: o0oOOo0O0Ooo % i1IIi / OoO0O00
   if 44 - 44: Oo0Ooo . OoO0O00 / I1ii11iIi11i + Ii1I
   if 65 - 65: O0
   if ( ooo0O == 'channel' and came_str == 'live' ) :
    if ( 'genre' in i1iIi ) :
     oO00OOoO00 = i1iIi [ 'genre' ]
    else :
     oO00OOoO00 = 'all'
    print "*epgcall*"
    iIiIIIi = self . GetEPGList ( oO00OOoO00 )
    if 40 - 40: I1IiiI * Ii1I + OOooOOo % iii1I1I
    if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + O0oo0OO0 / OoOoOO00
    if 23 - 23: O0
   for O0o0O00Oo0o0 in ii :
    o00oO0oOo00 = oO0oOo0 = I1I1I = ''
    if 95 - 95: II111iiii + o0oOOo0O0Ooo + iii1I1I * iIii1I11I1II1 % oO0o / O00oOoOoO0o0O
    o00oO0oOo00 = O0o0O00Oo0o0 . get ( 'title_list' ) [ 0 ] . get ( 'text' )
    if ( len ( O0o0O00Oo0o0 . get ( 'title_list' ) ) > 1 ) :
     if ( O0o0O00Oo0o0 . get ( 'title_list' ) [ 1 ] . get ( 'text' ) . startswith ( '@' ) ) :
      for o0o0o0oO0oOO in O0o0O00Oo0o0 . get ( 'bottom_taglist' ) :
       if o0o0o0oO0oOO == 'playy' or o0o0o0oO0oOO == 'won' : oO0oOo0 = o0o0o0oO0oOO
     else :
      oO0oOo0 = O0o0O00Oo0o0 . get ( 'title_list' ) [ 1 ] . get ( 'text' )
      oO0oOo0 = re . sub ( r'(\$O\$)|(\&[a-z]{2}\;)' , '' , oO0oOo0 )
    if ( O0o0O00Oo0o0 . get ( 'thumbnail' ) != '' ) : I1I1I = 'https://%s' % O0o0O00Oo0o0 . get ( 'thumbnail' )
    if 3 - 3: o0oOOo0O0Ooo
    Ii11I1 = O0o0O00Oo0o0 [ 'event_list' ] [ 1 ] . get ( 'url' )
    i1i1Iiii1I1 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( Ii11I1 ) . query ) )
    if 53 - 53: II111iiii
    if re . search ( u'programid=\&' , Ii11I1 ) and ( 'contentid' in i1i1Iiii1I1 ) :
     oOoO0o00OO0 = i1i1Iiii1I1 [ 'contentid' ]
     i1I1ii = 'direct'
    elif ( 'contentid' in i1i1Iiii1I1 ) :
     oOoO0o00OO0 = i1i1Iiii1I1 [ 'contentid' ]
     i1I1ii = 'contentid'
    elif ( 'programid' in i1i1Iiii1I1 ) :
     oOoO0o00OO0 = i1i1Iiii1I1 [ 'programid' ]
     i1I1ii = 'programid'
     ooo0O = 'program'
    elif ( 'channelid' in i1i1Iiii1I1 ) :
     oOoO0o00OO0 = i1i1Iiii1I1 [ 'channelid' ]
     i1I1ii = 'channelid'
     if 31 - 31: OoO0O00
     if oOoO0o00OO0 in iIiIIIi :
      oOOo0 = iIiIIIi [ oOoO0o00OO0 ]
     else :
      oOOo0 = ''
      if 80 - 80: O0oo0OO0 . i11iIiiIii - o0oOOo0O0Ooo
    elif ( 'movieid' in i1i1Iiii1I1 ) :
     oOoO0o00OO0 = i1i1Iiii1I1 [ 'movieid' ]
     i1I1ii = 'movieid'
     if 25 - 25: OoO0O00
     ooo0O = 'movie'
    else :
     oOoO0o00OO0 = '-'
     i1I1ii = '-'
     if 62 - 62: OOooOOo + O0
    oO0OOOO0 = { }
    oO0OOOO0 [ 'mpaa' ] = O0o0O00Oo0o0 . get ( 'age' )
    try :
     if ( 'channelid' in i1i1Iiii1I1 ) :
      oO0OOOO0 [ 'mediatype' ] = 'video'
      oO0OOOO0 [ 'title' ] = '%s < %s >' % ( unicode ( o00oO0oOo00 ) , unicode ( oO0oOo0 ) )
      oO0OOOO0 [ 'tvshowtitle' ] = unicode ( oO0oOo0 )
      oO0OOOO0 [ 'studio' ] = unicode ( o00oO0oOo00 )
     elif ( 'movieid' in i1i1Iiii1I1 ) :
      oO0OOOO0 [ 'mediatype' ] = 'movie'
      oO0OOOO0 [ 'title' ] = unicode ( title_list )
     else :
      oO0OOOO0 [ 'mediatype' ] = 'episode'
      oO0OOOO0 [ 'title' ] = unicode ( title_list )
    except :
     None
     if 26 - 26: Ii1I
    iI1iII1 = { 'title' : unicode ( o00oO0oOo00 )
 , 'subtitle' : unicode ( oO0oOo0 )
 , 'thumbnail' : I1I1I
 , 'uicode' : ooo0O
 , 'contentid' : oOoO0o00OO0
 , 'contentidType' : i1I1ii
 , 'viewage' : O0o0O00Oo0o0 . get ( 'age' )
 , 'channelepg' : oOOo0
 , 'info' : oO0OOOO0
 }
    Ii1i . append ( iI1iII1 )
    if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
   I1 = int ( OOOO [ 'cell_toplist' ] [ 'pagecount' ] )
   if OOOO [ 'cell_toplist' ] [ 'count' ] : iiIii = int ( OOOO [ 'cell_toplist' ] [ 'count' ] )
   else : iiIii = self . LIST_LIMIT
   if 47 - 47: iii1I1I - Ii1I . II111iiii + OoooooooOO . i11iIiiIii
   if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
   oo00O00oO = I1 > iiIii
   if 87 - 87: Oo0Ooo . O00oOoOoO0o0O
   if 75 - 75: Oo0ooO0oo0oO + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iii1I1I
  except Exception as OoOOOOO :
   print ( OoOOOOO )
   if 55 - 55: OOooOOo . I1IiiI
   if 61 - 61: Oo0Ooo % O00oOoOoO0o0O . Oo0Ooo
   if 100 - 100: O0oo0OO0 * O0
  try :
   if Ii1i [ 0 ] . get ( 'contentidType' ) == 'movieid' and addinfoyn == True :
    o00oO0oo0OO = [ ]
    O0O0OOOOoo = { }
    if 74 - 74: I1ii11iIi11i + II111iiii / OoO0O00
    for oOo0O0Oo00oO in Ii1i : o00oO0oo0OO . append ( oOo0O0Oo00oO . get ( 'contentid' ) )
    if 7 - 7: O00oOoOoO0o0O * O0oo0OO0 % Ii1I - o0oOOo0O0Ooo
    O0O0OOOOoo = self . GetMovieInfoList ( o00oO0oo0OO )
    if 13 - 13: Ii1I . i11iIiiIii
    for O0O00o0OOO0 in range ( len ( Ii1i ) ) :
     Ii1i [ O0O00o0OOO0 ] [ 'info' ] = O0O0OOOOoo . get ( Ii1i [ O0O00o0OOO0 ] [ 'contentid' ] )
  except :
   None
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
  return ( Ii1i , oo00O00oO )
  if 33 - 33: O0oo0OO0 + iii1I1I * oO0o / iIii1I11I1II1 - I1IiiI
  if 54 - 54: O0oo0OO0 / OOooOOo . oO0o % iii1I1I
 def GetEpisodeList ( self , contentid , contenttype , contentidType , page_int , orderby = 'desc' ) :
  Oo = [ ]
  I1 = iiIii = 1
  oo00O00oO = False
  if 65 - 65: Ii1I - oO0o + oO0o + II111iiii
  if orderby == 'desc' :
   orderby = 'new'
  else :
   orderby = 'old'
   if 96 - 96: OOooOOo % O0 / O0
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if 44 - 44: oO0o / I11i / I11i
   if 87 - 87: Oo0Ooo . I1IiiI - II111iiii + O0 / Oo0Ooo / oO0o
   if contentidType == 'contentid' :
    Oo000 = '/cf/vod/contents/' + contentid
    if 25 - 25: I1IiiI . I1IiiI - OoOoOO00 % OoOoOO00 - i11iIiiIii / O0oo0OO0
    IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
    II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
    OOOO = json . loads ( II1Iiii1111i )
    if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * O00oOoOoO0o0O
    if not ( 'programid' in OOOO ) : return None
    OOOoOo = OOOO [ 'programid' ]
    if 51 - 51: Oo0ooO0oo0oO / iIii1I11I1II1 % Oo0Ooo * I1IiiI % O0oo0OO0
   else :
    OOOoOo = contentid
    if 76 - 76: o0oOOo0O0Ooo - i11iIiiIii
    if 14 - 14: OoOoOO00 + oO0o
    if 52 - 52: OoooooooOO - Oo0ooO0oo0oO
   Oo000 = '/vod/programs-contents/' + OOOoOo
   if 74 - 74: iii1I1I + o0oOOo0O0Ooo
   i1iIi = { 'limit' : self . EP_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . EP_LIMIT )
 , 'orderby' : orderby
   }
   if 71 - 71: Oo0Ooo % OOooOOo
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( i1iIi ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 98 - 98: I11i % i11iIiiIii % Oo0ooO0oo0oO + Ii1I
   if not ( 'list' in OOOO ) : return None
   OOoOO0o0o0 = OOOO [ 'list' ]
   if 11 - 11: I1IiiI
   if 16 - 16: Ii1I + O00oOoOoO0o0O * O0 % i1IIi . I1IiiI
   for O0o0O00Oo0o0 in OOoOO0o0o0 :
    Oo0OO = O0o0O00Oo0o0 . get ( 'programtitle' )
    O0OooOo0o = '%s회, %s(%s)' % ( O0o0O00Oo0o0 . get ( 'episodenumber' ) , O0o0O00Oo0o0 . get ( 'releasedate' ) , O0o0O00Oo0o0 . get ( 'releaseweekday' ) )
    if ( O0o0O00Oo0o0 . get ( 'image' ) != '' ) : iiI11ii1I1 = 'https://%s' % O0o0O00Oo0o0 . get ( 'image' )
    if 82 - 82: II111iiii % I11i / OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / O0oo0OO0
    oOo0OOoO0 = unicode ( O0o0O00Oo0o0 . get ( 'synopsis' ) )
    oOo0OOoO0 = re . sub ( u'(\<[a-zA-Z]{1,2}\>)|(\<\/[a-zA-Z]{1,2}\>)' , '' , oOo0OOoO0 )
    if 11 - 11: I1ii11iIi11i . OoO0O00 * O00oOoOoO0o0O * OoooooooOO + Oo0ooO0oo0oO
    oO0OOOO0 = { }
    oO0OOOO0 [ 'title' ] = unicode ( Oo0OO )
    oO0OOOO0 [ 'mediatype' ] = 'episode'
    oO0OOOO0 [ 'mpaa' ] = O0o0O00Oo0o0 . get ( 'targetage' )
    try :
     if 'episodenumber' in O0o0O00Oo0o0 : oO0OOOO0 [ 'episode' ] = O0o0O00Oo0o0 . get ( 'episodenumber' )
     if 'releasedate' in O0o0O00Oo0o0 : oO0OOOO0 [ 'year' ] = int ( O0o0O00Oo0o0 . get ( 'releasedate' ) [ : 4 ] )
     if 'releasedate' in O0o0O00Oo0o0 : oO0OOOO0 [ 'aired' ] = O0o0O00Oo0o0 . get ( 'releasedate' )
     if 'playtime' in O0o0O00Oo0o0 : oO0OOOO0 [ 'duration' ] = O0o0O00Oo0o0 . get ( 'playtime' )
     if 'episodeactors' in O0o0O00Oo0o0 :
      if O0o0O00Oo0o0 . get ( 'episodeactors' ) != '' : oO0OOOO0 [ 'cast' ] = O0o0O00Oo0o0 . get ( 'episodeactors' ) . split ( ',' )
    except :
     None
     if 33 - 33: O0 * o0oOOo0O0Ooo - O0oo0OO0 % O0oo0OO0
    I11I = { 'title' : unicode ( Oo0OO )
 , 'subtitle' : unicode ( O0OooOo0o )
 , 'thumbnail' : iiI11ii1I1
 , 'uicode' : contenttype
 , 'contentid' : O0o0O00Oo0o0 . get ( 'contentid' )
 , 'programid' : O0o0O00Oo0o0 . get ( 'programid' )
 , 'synopsis' : oOo0OOoO0
 , 'viewage' : O0o0O00Oo0o0 . get ( 'targetage' )
 , 'info' : oO0OOOO0
    }
    Oo . append ( I11I )
    if 50 - 50: O0oo0OO0 * i11iIiiIii * iIii1I11I1II1 - II111iiii * o0oOOo0O0Ooo * OoOoOO00
   I1 = int ( OOOO [ 'pagecount' ] )
   if OOOO [ 'count' ] : iiIii = int ( OOOO [ 'count' ] )
   else : iiIii = self . EP_LIMIT
   if 94 - 94: OoooooooOO + OoooooooOO . II111iiii + I11i / I1ii11iIi11i % Ii1I
   oo00O00oO = I1 > iiIii
   if 18 - 18: iii1I1I * O0 - OoooooooOO % I1IiiI . II111iiii / i1IIi
  except Exception as OoOOOOO :
   print ( OoOOOOO )
   if 76 - 76: I11i / OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + O00oOoOoO0o0O
  return ( Oo , oo00O00oO )
  if 71 - 71: O0oo0OO0 . II111iiii
  if 62 - 62: OoooooooOO . I11i
 def GetMyviewList ( self , contenttype , page_int , addinfoyn = False ) :
  oOOOoo00 = [ ]
  I1 = iiIii = 1
  oo00O00oO = False
  if 9 - 9: O0 % O0 - o0oOOo0O0Ooo
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if 51 - 51: I1IiiI . iIii1I11I1II1 - I1ii11iIi11i / O0
   Oo000 = '/myview/contents'
   if 52 - 52: o0oOOo0O0Ooo + O0 + iii1I1I + Oo0Ooo % iii1I1I
   i1iIi = { 'contenttype' : contenttype
 , 'limit' : self . MV_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . MV_LIMIT )
 , 'orderby' : 'new'
 }
   if 75 - 75: I1IiiI . Oo0ooO0oo0oO . O0 * O0oo0OO0
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( i1iIi ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 4 - 4: Ii1I % oO0o * OoO0O00
   if not ( 'list' in OOOO [ 0 ] ) : return None
   o0O0OOOOoOO0 = OOOO [ 0 ] [ 'list' ]
   if 23 - 23: i11iIiiIii
   for O0o0O00Oo0o0 in o0O0OOOOoOO0 :
    oO0OOOO0 = { }
    if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
    if contenttype == 'vod' :
     Oo0OO = O0o0O00Oo0o0 . get ( 'programtitle' )
     O0OooOo0o = '%s회, %s' % ( O0o0O00Oo0o0 . get ( 'episodenumber' ) , O0o0O00Oo0o0 . get ( 'releasedate' ) )
     oOoO0o00OO0 = O0o0O00Oo0o0 . get ( 'contentid' )
     OOOoOo = O0o0O00Oo0o0 . get ( 'programid' )
     if 81 - 81: O00oOoOoO0o0O % i1IIi . iIii1I11I1II1
     oO0OOOO0 [ 'title' ] = unicode ( Oo0OO )
     oO0OOOO0 [ 'mediatype' ] = 'episode'
     oO0OOOO0 [ 'mpaa' ] = O0o0O00Oo0o0 . get ( 'targetage' )
     try :
      oO0OOOO0 [ 'studio' ] = O0o0O00Oo0o0 . get ( 'channelname' )
     except :
      None
     try :
      if 'releasedate' in O0o0O00Oo0o0 : oO0OOOO0 [ 'year' ] = int ( O0o0O00Oo0o0 . get ( 'releasedate' ) [ : 4 ] )
      if 'releasedate' in O0o0O00Oo0o0 : oO0OOOO0 [ 'aired' ] = O0o0O00Oo0o0 . get ( 'releasedate' )
     except :
      None
      if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / O00oOoOoO0o0O
      if 6 - 6: iii1I1I / I1IiiI % OOooOOo - I1IiiI
    else :
     Oo0OO = O0o0O00Oo0o0 . get ( 'title' )
     O0OooOo0o = ''
     oOoO0o00OO0 = OOOoOo = O0o0O00Oo0o0 . get ( 'movieid' )
     if 31 - 31: OOooOOo
     oO0OOOO0 [ 'title' ] = unicode ( Oo0OO )
     oO0OOOO0 [ 'mediatype' ] = 'movie'
     oO0OOOO0 [ 'mpaa' ] = O0o0O00Oo0o0 . get ( 'targetage' )
     try :
      if 'releasedate' in O0o0O00Oo0o0 : oO0OOOO0 [ 'year' ] = int ( O0o0O00Oo0o0 . get ( 'releasedate' ) [ : 4 ] )
      if 'releasedate' in O0o0O00Oo0o0 : oO0OOOO0 [ 'aired' ] = O0o0O00Oo0o0 . get ( 'releasedate' )
     except :
      None
      if 23 - 23: O0oo0OO0 . O00oOoOoO0o0O
      if 92 - 92: OoOoOO00 + O0oo0OO0 * Ii1I % I1IiiI
    if ( O0o0O00Oo0o0 . get ( 'image' ) != '' ) : iiI11ii1I1 = 'https://%s' % O0o0O00Oo0o0 . get ( 'image' )
    if 42 - 42: Oo0Ooo
    oo000O0OoooO = { 'title' : unicode ( Oo0OO )
 , 'subtitle' : unicode ( O0OooOo0o )
 , 'thumbnail' : iiI11ii1I1
 , 'uicode' : contenttype
 , 'contentid' : oOoO0o00OO0
 , 'programid' : OOOoOo
 , 'viewage' : O0o0O00Oo0o0 . get ( 'targetage' )
 , 'info' : oO0OOOO0
 }
    if 93 - 93: I11i . II111iiii / oO0o % OoooooooOO * I11i % I1ii11iIi11i
    oOOOoo00 . append ( oo000O0OoooO )
    if 48 - 48: Oo0ooO0oo0oO / O0oo0OO0 . iIii1I11I1II1 * OoOoOO00 * oO0o / i1IIi
    if 92 - 92: Oo0Ooo % Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
   I1 = int ( OOOO [ 0 ] [ 'pagecount' ] )
   if OOOO [ 0 ] [ 'count' ] : iiIii = int ( OOOO [ 0 ] [ 'count' ] )
   else : iiIii = self . MV_LIMIT
   if 10 - 10: iii1I1I + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / O0oo0OO0 / I1ii11iIi11i
   oo00O00oO = I1 > iiIii
   if 42 - 42: I1IiiI
  except Exception as OoOOOOO :
   print ( OoOOOOO )
   if 38 - 38: OOooOOo + II111iiii % Oo0ooO0oo0oO % OoOoOO00 - Ii1I / OoooooooOO
   if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
   if 85 - 85: Ii1I % iii1I1I + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
  try :
   if contenttype == 'movie' and addinfoyn == True :
    o00oO0oo0OO = [ ]
    O0O0OOOOoo = { }
    if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
    for oOo0O0Oo00oO in oOOOoo00 : o00oO0oo0OO . append ( oOo0O0Oo00oO . get ( 'contentid' ) )
    if 28 - 28: iii1I1I . iii1I1I % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iii1I1I
    O0O0OOOOoo = self . GetMovieInfoList ( o00oO0oo0OO )
    if 27 - 27: OoO0O00 + Oo0ooO0oo0oO - i1IIi
    for O0O00o0OOO0 in range ( len ( oOOOoo00 ) ) :
     oOOOoo00 [ O0O00o0OOO0 ] [ 'info' ] = O0O0OOOOoo . get ( oOOOoo00 [ O0O00o0OOO0 ] [ 'contentid' ] )
  except :
   None
   if 69 - 69: O00oOoOoO0o0O - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
   if 79 - 79: O0 * i11iIiiIii - O00oOoOoO0o0O / O00oOoOoO0o0O
   if 48 - 48: O0
  return oOOOoo00 , oo00O00oO
  if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
  if 25 - 25: O00oOoOoO0o0O + Ii1I / Oo0ooO0oo0oO . o0oOOo0O0Ooo % O0 * OoO0O00
 def GetSearchList ( self , search_key , genre , page_int , exclusion21 = False , addinfoyn = False ) :
  o0O0oo0OO0O = [ ]
  I1 = iiIii = 1
  oo00O00oO = False
  if 68 - 68: oO0o . I11i % OoooooooOO . I11i
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if 64 - 64: iIii1I11I1II1 / I1IiiI . II111iiii + OoooooooOO . OoO0O00
   Oo000 = '/cf/search/list.js'
   if 56 - 56: Oo0Ooo . I1ii11iIi11i . I1IiiI
   i1iIi = { 'type' : 'program' if genre == 'vod' else 'movie'
 , 'keyword' : search_key
 , 'offset' : str ( ( page_int - 1 ) * self . LIST_LIMIT )
 , 'limit' : self . LIST_LIMIT
   , 'orderby' : 'score'
 , 'isplayymovie' : 'y'
 }
   if 39 - 39: O0 + O0oo0OO0
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( i1iIi ) + '&' + urllib . urlencode ( O0O00Ooo )
   if 91 - 91: OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoOoOO00 + O0
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 26 - 26: I1ii11iIi11i - OoooooooOO
   if not ( 'celllist' in OOOO [ 'cell_toplist' ] ) : return o0O0oo0OO0O , oo00O00oO
   iiI1iI111ii1i = OOOO [ 'cell_toplist' ] [ 'celllist' ]
   if 32 - 32: II111iiii * OoOoOO00 % i1IIi - iii1I1I + iIii1I11I1II1 + I1ii11iIi11i
   if 60 - 60: I1ii11iIi11i % OoOoOO00 * OoO0O00 % II111iiii
   for O0o0O00Oo0o0 in iiI1iI111ii1i :
    oO0OOOO0 = { }
    if 70 - 70: OoO0O00 % oO0o + OOooOOo / Ii1I % O0
    Oo0OO = O0o0O00Oo0o0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if ( O0o0O00Oo0o0 . get ( 'thumbnail' ) != '' ) : iiI11ii1I1 = 'https://%s' % O0o0O00Oo0o0 . get ( 'thumbnail' )
    if 100 - 100: o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
    for o000O0o in O0o0O00Oo0o0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , o000O0o ) :
      if genre == 'vod' :
       oOoO0o00OO0 = ''
       OOOoOo = re . sub ( r'uicode:' , '' , o000O0o )
       oO0OOOO0 [ 'mediatype' ] = 'episode'
       if 80 - 80: o0oOOo0O0Ooo * O0 - Ii1I
      else :
       oOoO0o00OO0 = re . sub ( r'uicode:' , '' , o000O0o )
       OOOoOo = ''
       if O0o0O00Oo0o0 . get ( 'bottom_taglist' ) [ 0 ] == 'playy' :
        Oo0OO += ' [playy]'
       oO0OOOO0 [ 'mediatype' ] = 'movie'
       if 66 - 66: i11iIiiIii - OOooOOo * Oo0Ooo
       if 76 - 76: i11iIiiIii + o0oOOo0O0Ooo / I1ii11iIi11i - OoO0O00 - Ii1I + I1ii11iIi11i
      oO0OOOO0 [ 'title' ] = unicode ( O0o0O00Oo0o0 [ 'title_list' ] [ 0 ] [ 'text' ] )
      oO0OOOO0 [ 'mpaa' ] = O0o0O00Oo0o0 . get ( 'age' )
      if 51 - 51: iIii1I11I1II1 . Oo0ooO0oo0oO + iIii1I11I1II1
      oo000O0OoooO = { 'title' : unicode ( Oo0OO )
 , 'thumbnail' : iiI11ii1I1
 , 'uicode' : genre
 , 'contentid' : oOoO0o00OO0
 , 'programid' : OOOoOo
 , 'viewage' : O0o0O00Oo0o0 . get ( 'age' )
 , 'info' : oO0OOOO0
 }
      if 95 - 95: I1IiiI
    if exclusion21 == False or O0o0O00Oo0o0 . get ( 'age' ) != '21' :
     o0O0oo0OO0O . append ( oo000O0OoooO )
     if 46 - 46: OoOoOO00 + OoO0O00
     if 70 - 70: iii1I1I / iIii1I11I1II1
   I1 = int ( OOOO [ 'cell_toplist' ] [ 'pagecount' ] )
   if OOOO [ 'cell_toplist' ] [ 'count' ] : iiIii = int ( OOOO [ 'cell_toplist' ] [ 'count' ] )
   else : iiIii = self . LIST_LIMIT
   if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
   oo00O00oO = I1 > iiIii
   if 96 - 96: OoooooooOO + oO0o
  except Exception as OoOOOOO :
   print ( OoOOOOO )
   if 44 - 44: oO0o
   if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
   if 88 - 88: OoOoOO00 / II111iiii
  try :
   if genre == 'movie' and addinfoyn == True :
    o00oO0oo0OO = [ ]
    O0O0OOOOoo = { }
    if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iii1I1I + oO0o
    for oOo0O0Oo00oO in o0O0oo0OO0O : o00oO0oo0OO . append ( oOo0O0Oo00oO . get ( 'contentid' ) )
    if 82 - 82: oO0o / iIii1I11I1II1 . I1IiiI . OOooOOo / o0oOOo0O0Ooo
    O0O0OOOOoo = self . GetMovieInfoList ( o00oO0oo0OO )
    if 42 - 42: Oo0Ooo
    for O0O00o0OOO0 in range ( len ( o0O0oo0OO0O ) ) :
     o0O0oo0OO0O [ O0O00o0OOO0 ] [ 'info' ] = O0O0OOOOoo . get ( o0O0oo0OO0O [ O0O00o0OOO0 ] [ 'contentid' ] )
  except :
   None
   if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
   if 46 - 46: Oo0Ooo
   if 1 - 1: iii1I1I
  return o0O0oo0OO0O , oo00O00oO
  if 97 - 97: OOooOOo + iii1I1I + O0 + i11iIiiIii
  if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
 def GetGenreGroup ( self , maintype , subtype , orderby , ordernm , exclusion21 = False ) :
  IIii11I1i1I = [ ]
  if 99 - 99: iii1I1I
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if 76 - 76: OoO0O00 * I1IiiI
   Oo000 = '/cf/filters'
   if 82 - 82: Ii1I * iii1I1I / I1ii11iIi11i
   i1iIi = { 'type' : maintype }
   if 36 - 36: OoooooooOO - i1IIi . O0 / II111iiii + o0oOOo0O0Ooo
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( i1iIi ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 33 - 33: II111iiii / Oo0ooO0oo0oO * O0 % Ii1I * O0oo0OO0
   if not ( maintype in OOOO ) : return None
   O0o = OOOO [ maintype ]
   if 72 - 72: OOooOOo % I1ii11iIi11i + OoO0O00 / oO0o + O00oOoOoO0o0O
   if subtype == '-' :
    if 10 - 10: O0oo0OO0 / Oo0ooO0oo0oO + i11iIiiIii / Ii1I
    for O0o0O00Oo0o0 in O0o :
     OOOoOoO = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( O0o0O00Oo0o0 . get ( 'url' ) ) . query ) )
     if 22 - 22: I1IiiI % I1ii11iIi11i
     oo000O0OoooO = { 'title' : O0o0O00Oo0o0 . get ( 'text' )
 , 'genre' : O0o0O00Oo0o0 . get ( 'id' )
 , 'subgenre' : '-'
 , 'adult' : O0o0O00Oo0o0 . get ( 'adult' )
 , 'broadcastid' : OOOoOoO . get ( 'broadcastid' )
 , 'contenttype' : OOOoOoO . get ( 'contenttype' )
 , 'uiparent' : OOOoOoO . get ( 'uiparent' )
 , 'uirank' : OOOoOoO . get ( 'uirank' )
 , 'uitype' : OOOoOoO . get ( 'uitype' )
 , 'orderby' : orderby
 , 'ordernm' : ordernm
 }
     if exclusion21 == False or oo000O0OoooO . get ( 'adult' ) == 'n' :
      IIii11I1i1I . append ( oo000O0OoooO )
      if 57 - 57: OOooOOo + O0 . Ii1I
   else :
    for O0o0O00Oo0o0 in O0o :
     if O0o0O00Oo0o0 . get ( 'id' ) == subtype :
      for iIi1i1iIi1iI in O0o0O00Oo0o0 [ 'sublist' ] :
       OOOoOoO = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( iIi1i1iIi1iI . get ( 'url' ) ) . query ) )
       if 26 - 26: OoooooooOO * I1IiiI + OOooOOo
       oo000O0OoooO = { 'title' : iIi1i1iIi1iI . get ( 'text' )
 , 'genre' : subtype
 , 'subgenre' : iIi1i1iIi1iI . get ( 'id' )
 , 'adult' : iIi1i1iIi1iI . get ( 'adult' )
 , 'broadcastid' : OOOoOoO . get ( 'broadcastid' )
 , 'contenttype' : OOOoOoO . get ( 'contenttype' )
 , 'uiparent' : OOOoOoO . get ( 'uiparent' )
 , 'uirank' : OOOoOoO . get ( 'uirank' )
 , 'uitype' : OOOoOoO . get ( 'uitype' )
 , 'orderby' : orderby
 , 'ordernm' : ordernm
 }
       IIii11I1i1I . append ( oo000O0OoooO )
      break
      if 24 - 24: i11iIiiIii % iIii1I11I1II1 + OOooOOo / i11iIiiIii
  except Exception as OoOOOOO :
   print ( OoOOOOO )
   if 70 - 70: OoO0O00 * O0 . I11i + I1IiiI . O00oOoOoO0o0O
  return IIii11I1i1I
  if 14 - 14: iIii1I11I1II1 % iIii1I11I1II1 * i11iIiiIii - OoO0O00 - I11i
  if 63 - 63: OoO0O00
 def GetGenreGroup_sub ( self , in_params ) :
  IIii11I1i1I = [ ]
  if 69 - 69: iIii1I11I1II1 . I1ii11iIi11i % Oo0ooO0oo0oO + iIii1I11I1II1 / O0 / I1ii11iIi11i
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if 61 - 61: OOooOOo % OOooOOo * o0oOOo0O0Ooo / o0oOOo0O0Ooo
   Oo000 = '/cf/vod/newcontents'
   if 75 - 75: O00oOoOoO0o0O . Oo0ooO0oo0oO
   i1iIi = { 'WeekDay' : 'all'
 , 'limit' : '20'
 , 'offset' : '0'

   , 'orderby' : in_params . get ( 'orderby' )
 , 'adult' : in_params . get ( 'adult' )
 , 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )
 }
   if 50 - 50: OoOoOO00
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( i1iIi ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 60 - 60: Oo0ooO0oo0oO * iIii1I11I1II1 * I1ii11iIi11i * Oo0Ooo
   if not ( 'filter_item_list' in OOOO [ 'filter' ] [ 'filterlist' ] [ 1 ] ) : return None
   O0o = OOOO [ 'filter' ] [ 'filterlist' ] [ 1 ] [ 'filter_item_list' ]
   if 69 - 69: Ii1I * O0 . i11iIiiIii / Ii1I . o0oOOo0O0Ooo
   for O0o0O00Oo0o0 in O0o :
    oo000O0OoooO = { 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )

 , 'adult' : O0o0O00Oo0o0 . get ( 'adult' )
 , 'title' : O0o0O00Oo0o0 . get ( 'title' )
 , 'subgenre' : O0o0O00Oo0o0 . get ( 'api_parameters' ) [ O0o0O00Oo0o0 . get ( 'api_parameters' ) . find ( '=' ) + 1 : ]
 , 'orderby' : in_params . get ( 'orderby' )
 }
    IIii11I1i1I . append ( oo000O0OoooO )
    if 63 - 63: I11i + o0oOOo0O0Ooo . II111iiii - I1IiiI
  except Exception as OoOOOOO :
   print ( OoOOOOO )
   if 52 - 52: o0oOOo0O0Ooo % Oo0Ooo
  return IIii11I1i1I
  if 64 - 64: O0 % I11i % O0 * OoO0O00 . oO0o + I1IiiI
  if 75 - 75: I11i . OoooooooOO % o0oOOo0O0Ooo * I11i % OoooooooOO
 def GetGenreList ( self , genre , in_params , page_int , addinfoyn = False ) :
  IIii11I1i1I = [ ]
  I1 = iiIii = 1
  oo00O00oO = False
  if 13 - 13: O00oOoOoO0o0O / i11iIiiIii % II111iiii % I11i . I1ii11iIi11i
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if 8 - 8: OoOoOO00 + Oo0Ooo - II111iiii
   i1iIi = { 'WeekDay' : 'all'
 , 'adult' : in_params . get ( 'adult' )
 , 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )

   , 'orderby' : in_params . get ( 'orderby' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )
 }
   if 11 - 11: i1IIi % i11iIiiIii - i1IIi * OoOoOO00
   if genre == 'vodgenre' :
    Oo000 = '/cf/vod/newcontents'
    if 39 - 39: O0oo0OO0
    if in_params . get ( 'subgenre' ) != '-' :
     i1iIi [ 'subgenre' ] = in_params . get ( 'subgenre' )
   else :
    Oo000 = '/cf/movie/contents'
    if 86 - 86: I11i * I1IiiI + I11i + II111iiii
    i1iIi [ 'price' ] = 'all'
    if 8 - 8: O0oo0OO0 - iii1I1I / Oo0ooO0oo0oO
    if 96 - 96: OoOoOO00
    i1iIi [ 'sptheme' ] = 'svod'
    if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - Ii1I
    if 20 - 20: i1IIi % OoO0O00 . I1IiiI / O00oOoOoO0o0O * i11iIiiIii * OOooOOo
   i1iIi [ 'limit' ] = self . LIST_LIMIT
   i1iIi [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
   i1iIi [ 'page' ] = str ( page_int )
   if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / Oo0ooO0oo0oO . O0 % O0oo0OO0
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( i1iIi ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iii1I1I
   if not ( 'celllist' in OOOO [ 'cell_toplist' ] ) : return None
   O0o = OOOO [ 'cell_toplist' ] [ 'celllist' ]
   if 8 - 8: Oo0ooO0oo0oO + II111iiii / iii1I1I / I11i
   for O0o0O00Oo0o0 in O0o :
    oO0OOOO0 = { }
    Oo0OO = iiI11ii1I1 = ''
    if 74 - 74: O0 / i1IIi
    Oo0OO = O0o0O00Oo0o0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if 78 - 78: OoooooooOO . OoO0O00 + Oo0ooO0oo0oO - i1IIi
    if ( O0o0O00Oo0o0 . get ( 'thumbnail' ) != '' ) : iiI11ii1I1 = 'https://%s' % O0o0O00Oo0o0 . get ( 'thumbnail' )
    if 31 - 31: OoooooooOO . OOooOOo
    for o000O0o in O0o0O00Oo0o0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , o000O0o ) :
      if 83 - 83: iii1I1I . O0 / Oo0Ooo / OOooOOo - II111iiii
      oO0OOOO0 [ 'title' ] = unicode ( Oo0OO )
      oO0OOOO0 [ 'mpaa' ] = O0o0O00Oo0o0 . get ( 'age' )
      if genre == 'moviegenre_svod' :
       oO0OOOO0 [ 'mediatype' ] = 'movie'
      else :
       oO0OOOO0 [ 'mediatype' ] = 'episode'
       if 100 - 100: OoO0O00
       if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iii1I1I . iIii1I11I1II1 * iii1I1I
      oo000O0OoooO = { 'title' : unicode ( Oo0OO )
 , 'uicode' : re . sub ( r'uicode:' , '' , o000O0o )
 , 'thumbnail' : iiI11ii1I1
 , 'viewage' : O0o0O00Oo0o0 . get ( 'age' )
 , 'info' : oO0OOOO0
 }
      if 38 - 38: I1ii11iIi11i - iii1I1I / O0 . O0oo0OO0
    IIii11I1i1I . append ( oo000O0OoooO )
    if 45 - 45: O0oo0OO0
    if 83 - 83: OoOoOO00 . OoooooooOO
   I1 = int ( OOOO [ 'cell_toplist' ] [ 'pagecount' ] )
   if OOOO [ 'cell_toplist' ] [ 'count' ] : iiIii = int ( OOOO [ 'cell_toplist' ] [ 'count' ] )
   else : iiIii = self . LIST_LIMIT
   if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / O00oOoOoO0o0O / i11iIiiIii
   oo00O00oO = I1 > iiIii
   if 62 - 62: OoO0O00 / I1ii11iIi11i
  except Exception as OoOOOOO :
   print ( OoOOOOO )
   if 7 - 7: OoooooooOO . O00oOoOoO0o0O
   if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
   if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
  try :
   if genre == 'moviegenre_svod' and addinfoyn == True :
    o00oO0oo0OO = [ ]
    O0O0OOOOoo = { }
    if 100 - 100: Oo0ooO0oo0oO % iIii1I11I1II1 * II111iiii - iii1I1I
    for oOo0O0Oo00oO in IIii11I1i1I : o00oO0oo0OO . append ( oOo0O0Oo00oO . get ( 'uicode' ) )
    if 92 - 92: Oo0ooO0oo0oO
    O0O0OOOOoo = self . GetMovieInfoList ( o00oO0oo0OO )
    if 22 - 22: Oo0Ooo % iii1I1I * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
    for O0O00o0OOO0 in range ( len ( IIii11I1i1I ) ) :
     IIii11I1i1I [ O0O00o0OOO0 ] [ 'info' ] = O0O0OOOOoo . get ( IIii11I1i1I [ O0O00o0OOO0 ] [ 'uicode' ] )
  except :
   None
   if 95 - 95: OoooooooOO - O00oOoOoO0o0O * I1IiiI + OoOoOO00
   if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
   if 92 - 92: I11i . O0oo0OO0
  return IIii11I1i1I , oo00O00oO
  if 85 - 85: I1ii11iIi11i . O0oo0OO0
  if 78 - 78: Oo0ooO0oo0oO * O0oo0OO0 + iIii1I11I1II1 + iIii1I11I1II1 / O0oo0OO0 . Ii1I
 def GetEPGList ( self , genre ) :
  O000 = { }
  if 79 - 79: OoooooooOO - I1IiiI
  try :
   import datetime
   o00O00oO00 = datetime . datetime . now ( )
   if genre == 'all' :
    Ii1i1i1i1I1Ii = o00O00oO00 + datetime . timedelta ( hours = 2 )
   else :
    Ii1i1i1i1I1Ii = o00O00oO00 + datetime . timedelta ( hours = 3 )
    if 25 - 25: II111iiii
   O0O00Ooo = self . GetDefaultParams ( )
   if 11 - 11: Oo0Ooo
   i1iIi = { 'limit' : '100'
 , 'offset' : '0'
 , 'genre' : genre
 , 'startdatetime' : o00O00oO00 . strftime ( '%Y-%m-%d %H:%M' )
 , 'enddatetime' : Ii1i1i1i1I1Ii . strftime ( '%Y-%m-%d %H:%M' )
 }
   Oo000 = '/live/epgs'
   if 74 - 74: OoOoOO00 * o0oOOo0O0Ooo + OoOoOO00 . OOooOOo * OoooooooOO % O0
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( i1iIi ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 85 - 85: Oo0ooO0oo0oO / O0
   iI1iIIIi1i = OOOO [ 'list' ]
   if 89 - 89: iIii1I11I1II1
   if 21 - 21: I11i % I11i
   for O0o0O00Oo0o0 in iI1iIIIi1i :
    iiI1 = ''
    if 16 - 16: II111iiii + oO0o - OoooooooOO
    for ii1iI in O0o0O00Oo0o0 [ 'list' ] :
     if iiI1 : iiI1 += '\n'
     iiI1 += ii1iI [ 'title' ] + '\n'
     iiI1 += ' [%s ~ %s]' % ( ii1iI [ 'starttime' ] [ - 5 : ] , ii1iI [ 'endtime' ] [ - 5 : ] ) + '\n'
     if 49 - 49: o0oOOo0O0Ooo . O00oOoOoO0o0O / OoO0O00 + II111iiii
     if 47 - 47: O0 / Ii1I
     if 67 - 67: I1IiiI
    O000 [ O0o0O00Oo0o0 [ 'channelid' ] ] = unicode ( iiI1 )
    if 55 - 55: I1ii11iIi11i - iii1I1I * o0oOOo0O0Ooo + OoOoOO00 * OoOoOO00 * O0
    if 91 - 91: O0oo0OO0 - OOooOOo % iIii1I11I1II1 - OoooooooOO % Oo0ooO0oo0oO
    if 98 - 98: OoO0O00 . OoO0O00 * oO0o * II111iiii * O0oo0OO0
  except Exception as OoOOOOO :
   print ( OoOOOOO )
   if 92 - 92: Oo0Ooo
  return O000
  if 40 - 40: OoOoOO00 / O00oOoOoO0o0O
  if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - O0oo0OO0
 def GetMovieInfoList ( self , movie_list ) :
  OoO = { }
  if 35 - 35: OoOoOO00 + i11iIiiIii - II111iiii
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   Oo000 = self . API_DOMAIN + '/movie/contents/'
   if 15 - 15: i11iIiiIii % I1IiiI * I11i / O0oo0OO0
   for oOo0O0Oo00oO in movie_list :
    if 90 - 90: iii1I1I
    IiIIIiI1I1 = Oo000 + oOo0O0Oo00oO
    II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
    OOOO = json . loads ( II1Iiii1111i )
    if 31 - 31: OOooOOo + O0
    oO0OOOO0 = { }
    oO0OOOO0 [ 'mediatype' ] = 'movie'
    if 87 - 87: Oo0ooO0oo0oO
    IIIii = [ ]
    for O00OooOo00o in OOOO [ 'actors' ] [ 'list' ] : IIIii . append ( O00OooOo00o . get ( 'text' ) )
    if IIIii [ 0 ] != '' : oO0OOOO0 [ 'cast' ] = IIIii
    if 20 - 20: i1IIi * O0oo0OO0 + II111iiii % o0oOOo0O0Ooo % oO0o
    iIi1II = [ ]
    for I1iIiI11I1 in OOOO [ 'directors' ] [ 'list' ] : iIi1II . append ( I1iIiI11I1 . get ( 'text' ) )
    if iIi1II [ 0 ] != '' : oO0OOOO0 [ 'director' ] = iIi1II
    if 27 - 27: Ii1I . i11iIiiIii % O0oo0OO0
    IIii11I1i1I = [ ]
    for OooOOOOoO00OoOO in OOOO [ 'genre' ] [ 'list' ] : IIii11I1i1I . append ( OooOOOOoO00OoOO . get ( 'text' ) )
    if IIii11I1i1I [ 0 ] != '' : oO0OOOO0 [ 'genre' ] = IIii11I1i1I
    if 85 - 85: oO0o - iIii1I11I1II1 / O0
    if OOOO . get ( 'releasedate' ) != '' :
     oO0OOOO0 [ 'year' ] = OOOO [ 'releasedate' ] [ : 4 ]
     oO0OOOO0 [ 'aired' ] = OOOO [ 'releasedate' ]
     if 99 - 99: II111iiii * O00oOoOoO0o0O % iIii1I11I1II1 / Ii1I
    oO0OOOO0 [ 'country' ] = OOOO [ 'country' ]
    oO0OOOO0 [ 'duration' ] = OOOO [ 'playtime' ]
    oO0OOOO0 [ 'title' ] = OOOO [ 'title' ]
    oO0OOOO0 [ 'mpaa' ] = OOOO [ 'targetage' ]
    oO0OOOO0 [ 'plot' ] = OOOO [ 'synopsis' ]
    if 90 - 90: oO0o % OOooOOo - OOooOOo % II111iiii * OoO0O00
    OoO [ oOo0O0Oo00oO ] = oO0OOOO0
    if 39 - 39: I11i
  except Exception as OoOOOOO :
   return { }
   if 58 - 58: i1IIi % o0oOOo0O0Ooo
  return OoO
  if 79 - 79: o0oOOo0O0Ooo % iii1I1I * OoooooooOO * iIii1I11I1II1 . iii1I1I / Ii1I
  if 19 - 19: O0 + I11i + Ii1I / II111iiii / II111iiii
 def GetStreamingURL ( self , contentid , contenttype , quality_int ) :
  oO0o0O0Ooo0o = i1Ii11II = IioO0oOOO0Ooo = i1i1I = ''
  IiIIi1 = [ ]
  if 30 - 30: I1ii11iIi11i % I1IiiI
  if 89 - 89: O0oo0OO0 + OoooooooOO + O0oo0OO0 * i1IIi + iIii1I11I1II1 % I11i
  try :
   if contenttype == 'channel' :
    Oo000 = '/live/channels/' + contentid
    oOo0oO = 'live'
   elif contenttype == 'movie' :
    Oo000 = '/cf/movie/contents/' + contentid
    oOo0oO = 'movie'
   else :
    Oo000 = '/cf/vod/contents/' + contentid
    oOo0oO = 'vod'
    if 5 - 5: OOooOOo - OOooOOo . Oo0Ooo + OoOoOO00 - OOooOOo . oO0o
   O0O00Ooo = self . GetDefaultParams ( )
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   if 31 - 31: II111iiii - iIii1I11I1II1 - iIii1I11I1II1 % I11i
   if 12 - 12: iIii1I11I1II1
   OOOO = self . SESSION . Request2 ( self . API_DOMAIN + Oo000 , params = O0O00Ooo )
   if 20 - 20: o0oOOo0O0Ooo / i1IIi
   oO = OOOO [ 'qualities' ] [ 'list' ]
   if oO == None : return ( oO0o0O0Ooo0o , i1Ii11II , IioO0oOOO0Ooo , i1i1I )
   if 21 - 21: i11iIiiIii / O0oo0OO0 % OOooOOo * O0 . I11i - iIii1I11I1II1
   iiIiiii1i1i1i = 'hls'
   if 'drms' in OOOO :
    if OOOO [ 'drms' ] :
     iiIiiii1i1i1i = 'dash'
     if 86 - 86: Oo0Ooo / oO0o + O0 * iii1I1I
     if 19 - 19: II111iiii * O00oOoOoO0o0O + Ii1I
     if 65 - 65: OOooOOo . O0oo0OO0 . OoO0O00 . iii1I1I - OOooOOo
   if 'type' in OOOO :
    if OOOO [ 'type' ] == 'onair' :
     oOo0oO = 'onairvod'
     if 19 - 19: i11iIiiIii + iii1I1I % Oo0ooO0oo0oO
     if 14 - 14: OoO0O00 . II111iiii . I11i / Ii1I % I1ii11iIi11i - Oo0ooO0oo0oO
   for o0oOoO0O in oO :
    IiIIi1 . append ( int ( o0oOoO0O . get ( 'id' ) . rstrip ( 'p' ) ) )
    if 84 - 84: O0 * OoooooooOO - O00oOoOoO0o0O * O00oOoOoO0o0O
  except Exception as OoOOOOO :
   return ( oO0o0O0Ooo0o , i1Ii11II , IioO0oOOO0Ooo , i1i1I )
   if 8 - 8: Oo0ooO0oo0oO / i1IIi . oO0o
   if 41 - 41: iii1I1I + OoO0O00
   if 86 - 86: OoOoOO00 . iIii1I11I1II1 - OoO0O00
  try :
   oOO = self . CheckQuality ( quality_int , IiIIi1 )
   Oo000 = '/streaming'
   i1iIi = { 'contentid' : contentid
 , 'contenttype' : oOo0oO
 , 'action' : iiIiiii1i1i1i
 , 'quality' : str ( oOO ) + 'p'
 , 'deviceModelId' : 'Windows 10'
 , 'guid' : self . GetGUID ( guidType = 2 )
 , 'lastplayid' : self . guid
 , 'authtype' : 'cookie'
 , 'isabr' : 'y'
 , 'ishevc' : 'n'
 }
   if 31 - 31: OOooOOo / Oo0Ooo * i1IIi . OoOoOO00
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( O0O00Ooo ) + '&' + urllib . urlencode ( i1iIi )
   if 57 - 57: OOooOOo + iIii1I11I1II1 % i1IIi % I1IiiI
   if 83 - 83: o0oOOo0O0Ooo / i11iIiiIii % iIii1I11I1II1 . I11i % oO0o . OoooooooOO
   if 94 - 94: Ii1I + iIii1I11I1II1 % OoO0O00
   i1iIi . update ( O0O00Ooo )
   OOOO = self . SESSION . Request2 ( self . API_DOMAIN + Oo000 , params = i1iIi )
   if 93 - 93: Ii1I - OOooOOo + iIii1I11I1II1 * o0oOOo0O0Ooo + O0oo0OO0 . iii1I1I
   if 49 - 49: OoooooooOO * I11i - Oo0Ooo . oO0o
   oO0o0O0Ooo0o = OOOO [ 'playurl' ]
   if oO0o0O0Ooo0o == None : return None
   i1Ii11II = OOOO [ 'awscookie' ]
   IioO0oOOO0Ooo = OOOO [ 'drm' ]
   if 'previewmsg' in OOOO [ 'preview' ] : i1i1I = OOOO [ 'preview' ] [ 'previewmsg' ]
   if 89 - 89: Oo0ooO0oo0oO + Ii1I * Oo0ooO0oo0oO / Oo0ooO0oo0oO
  except Exception as OoOOOOO :
   print ( OoOOOOO )
   if 46 - 46: OoO0O00
  oO0o0O0Ooo0o = oO0o0O0Ooo0o . replace ( 'pooq.co.kr' , 'wavve.com' )
  if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
  return ( oO0o0O0Ooo0o , i1Ii11II , IioO0oOOO0Ooo , i1i1I )
  if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
  if 58 - 58: I11i + II111iiii * iii1I1I * i11iIiiIii - iIii1I11I1II1
  if 68 - 68: OoooooooOO % II111iiii
  if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
  if 24 - 24: II111iiii % O0oo0OO0 - Oo0ooO0oo0oO + I1IiiI * I1ii11iIi11i
  if 2 - 2: Ii1I - O00oOoOoO0o0O
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
