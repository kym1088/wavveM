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
  if 99 - 99: iIii1I11I1II1 * OoooooooOO * II111iiii * iIii1I11I1II1
  if 44 - 44: oO0o / Oo0Ooo - II111iiii - i11iIiiIii % O0oo0OO0
class O0OoOoo00o ( object ) :
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
  self . TARGETAGE = 'auto'
  self . CREDENTIAL = 'none'
  self . HTTPTAG = 'https://'
  self . LIST_LIMIT = 30
  self . EP_LIMIT = 30
  self . MV_LIMIT = 24
  self . guid = 'none'
  self . guidtimestamp = 'none'
  if 31 - 31: II111iiii + OoO0O00 . O0oo0OO0
 def SaveCredential ( self , credential ) :
  self . CREDENTIAL = credential
  if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
 def LoadCredential ( self ) :
  return self . CREDENTIAL
  if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
 def GetDefaultParams ( self ) :
  i1iIIi1 = { 'apikey' : self . APIKEY ,
 'credential' : self . CREDENTIAL ,
 'device' : self . DEVICE ,
 'drm' : self . DRM ,
 'partner' : self . PARTNER ,
 'pooqzone' : self . POOQZONE ,
 'region' : self . REGION ,
 'targetage' : self . TARGETAGE
 }
  return i1iIIi1
  if 50 - 50: i11iIiiIii - Ii1I
 def makeurl ( self , domain , path , query = None ) :
  oo0Ooo0 = ''
  if domain :
   if re . search ( r'http[s]*://' , domain ) :
    oo0Ooo0 += domain
   else :
    oo0Ooo0 += 'http://%s' % domain
   if path :
    oo0Ooo0 += path
    if query : oo0Ooo0 += '?%s' % query
  return oo0Ooo0
  if 46 - 46: Oo0ooO0oo0oO % Oo0ooO0oo0oO - oO0o * o0oOOo0O0Ooo % iii1I1I
 def MakeServiceUrl ( self , path , params ) :
  if 55 - 55: OoOoOO00 % i1IIi / Ii1I - oO0o - O0 / II111iiii
  oo0Ooo0 = self . makeurl ( self . API_DOMAIN , path , urllib . urlencode ( params ) )
  return oo0Ooo0
  if 28 - 28: iIii1I11I1II1 - i1IIi
 def GetGUID ( self , guid_str = 'POOQ' , guidType = 1 ) :
  if 70 - 70: OoO0O00 . OoO0O00 - OoO0O00 / I1ii11iIi11i * OOooOOo
  def OoO000 ( media ) :
   from datetime import datetime
   IIiiIiI1 = datetime . now ( ) . strftime ( '%Y%m%d%H%M%S' )
   iiIiIIi = ooOoo0O ( 5 )
   OooO0 = iiIiIIi + media + IIiiIiI1
   return OooO0
   if 35 - 35: OOooOOo % O0oo0OO0 % i11iIiiIii / OoooooooOO
  def ooOoo0O ( num ) :
   from random import randint
   Ii11iI1i = ""
   for Ooo in range ( 0 , num ) :
    O0o0Oo = str ( randint ( 1 , 5 ) )
    Ii11iI1i += O0o0Oo
   return Ii11iI1i
   if 78 - 78: iIii1I11I1II1 - Ii1I * OoO0O00 + o0oOOo0O0Ooo + iii1I1I + iii1I1I
  OooO0 = OoO000 ( guid_str )
  if 11 - 11: iii1I1I - OoO0O00 % Oo0ooO0oo0oO % iii1I1I / OoOoOO00 - OoO0O00
  o0o0oOOOo0oo = self . GetHash ( OooO0 )
  if guidType == 2 :
   o0o0oOOOo0oo = '%s-%s-%s-%s-%s' % ( o0o0oOOOo0oo [ : 8 ] , o0o0oOOOo0oo [ 8 : 12 ] , o0o0oOOOo0oo [ 12 : 16 ] , o0o0oOOOo0oo [ 16 : 20 ] , o0o0oOOOo0oo [ 20 : ] )
   if 80 - 80: I11i * i11iIiiIii / O0oo0OO0
  return o0o0oOOOo0oo
  if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
 def GetHash ( self , hash_str ) :
  import hashlib
  III1i1i = hashlib . md5 ( )
  if 26 - 26: OoooooooOO
  III1i1i . update ( hash_str )
  return str ( III1i1i . hexdigest ( ) )
  if 12 - 12: OoooooooOO % OoOoOO00 / Oo0ooO0oo0oO % o0oOOo0O0Ooo
 def CheckQuality ( self , sel_qt , qt_list ) :
  iiii = 0
  for oO0o0O0OOOoo0 in qt_list :
   if sel_qt >= oO0o0O0OOOoo0 : return oO0o0O0OOOoo0
   iiii = oO0o0O0OOOoo0
  return iiii
  if 48 - 48: O0 + O0 - I1ii11iIi11i . Oo0ooO0oo0oO / iIii1I11I1II1
  if 77 - 77: i1IIi % OoOoOO00 - O00oOoOoO0o0O + Oo0ooO0oo0oO
 def GetCredential ( self , user_id , user_pw , user_pf ) :
  I11iiIiii = False
  try :
   iii11I111 = '/login'
   i1iIIi1 = self . GetDefaultParams ( )
   OOOO00ooo0Ooo = { 'id' : user_id
 , 'password' : user_pw
 , 'profile' : '0'
 , 'pushid' : ''
 , 'type' : 'general'
 }
   oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , i1iIIi1 )
   if 69 - 69: o0oOOo0O0Ooo * O0 + OoO0O00 . II111iiii / O0
   if 97 - 97: Oo0ooO0oo0oO - OOooOOo * i11iIiiIii / OoOoOO00 % O0oo0OO0 - OoooooooOO
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 , postdata = urllib . urlencode ( OOOO00ooo0Ooo ) )
   OoOo00o = json . loads ( II1Iiii1111i )
   o0OOoo0OO0OOO = OoOo00o [ 'credential' ]
   if 19 - 19: oO0o % i1IIi % o0oOOo0O0Ooo
   if 93 - 93: iIii1I11I1II1 % oO0o * i1IIi
   if user_pf != 0 :
    OOOO00ooo0Ooo = { 'id' : o0OOoo0OO0OOO
 , 'password' : ''
 , 'profile' : str ( user_pf )
 , 'pushid' : ''
 , 'type' : 'credential'
 }
    if 16 - 16: O0 - O0oo0OO0 * iIii1I11I1II1 + iii1I1I
    II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 , postdata = urllib . urlencode ( OOOO00ooo0Ooo ) )
    OoOo00o = json . loads ( II1Iiii1111i )
    o0OOoo0OO0OOO = OoOo00o [ 'credential' ]
    if 50 - 50: II111iiii - Oo0ooO0oo0oO * I1ii11iIi11i / O0oo0OO0 + o0oOOo0O0Ooo
    if 88 - 88: Ii1I / O0oo0OO0 + iii1I1I - II111iiii / Oo0ooO0oo0oO - OoOoOO00
   if o0OOoo0OO0OOO : I11iiIiii = True
   if 15 - 15: I1ii11iIi11i + OoOoOO00 - OoooooooOO / OOooOOo
   if 58 - 58: i11iIiiIii % I11i
  except Exception as OO00Oo :
   print ( OO00Oo )
   o0OOoo0OO0OOO = 'none'
   if 51 - 51: O00oOoOoO0o0O * o0oOOo0O0Ooo + I11i + OoO0O00
  self . SaveCredential ( o0OOoo0OO0OOO )
  return I11iiIiii
  if 66 - 66: OoOoOO00
 def GetIssue ( self ) :
  oO000Oo000 = False
  try :
   iii11I111 = '/guid/issue'
   i1iIIi1 = self . GetDefaultParams ( )
   oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , i1iIIi1 )
   if 4 - 4: oO0o
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   if 93 - 93: OoO0O00 % oO0o . OoO0O00 * O0oo0OO0 % Ii1I . II111iiii
   OoOo00o = json . loads ( II1Iiii1111i )
   iI1ii1Ii = OoOo00o [ 'guid' ]
   oooo000 = OoOo00o [ 'guidtimestamp' ]
   if iI1ii1Ii : oO000Oo000 = True
  except Exception as OO00Oo :
   print ( OO00Oo )
   iI1ii1Ii = 'none'
   oooo000 = 'none'
   if 16 - 16: I1ii11iIi11i + OoO0O00 - II111iiii
  self . guid = iI1ii1Ii
  self . guidtimestamp = oooo000
  if 85 - 85: OoOoOO00 + i1IIi
  return oO000Oo000
  if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
 def GetGnList ( self , gn_str ) :
  oO0o0OOOO = [ ]
  try :
   iii11I111 = '/cf/supermultisections/' + gn_str
   i1iIIi1 = self . GetDefaultParams ( )
   oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , i1iIIi1 )
   if 68 - 68: iii1I1I - O0oo0OO0 - I1IiiI - I1ii11iIi11i + I11i
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 10 - 10: OoooooooOO % iIii1I11I1II1
   if not ( 'multisectionlist' in OoOo00o ) : return None
   O00o0O00 = OoOo00o [ 'multisectionlist' ]
   if 34 - 34: Oo0ooO0oo0oO
   if 15 - 15: I11i * Oo0ooO0oo0oO * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
   for O0ooo0O0oo0 in O00o0O00 :
    oo0oOo = O0ooo0O0oo0 [ 'title' ]
    if len ( oo0oOo ) == 0 : continue
    if oo0oOo == 'minor' : continue
    if 89 - 89: OoOoOO00
    if re . search ( u'베너' , oo0oOo ) : continue
    if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + Oo0ooO0oo0oO
    oo0oOo = re . sub ( '\n|\!|\~|(@0@)|(@\^0@)' , '' , oo0oOo )
    oo0oOo = oo0oOo . lstrip ( '#' )
    if 4 - 4: Oo0ooO0oo0oO + O0 * OOooOOo
    for OOoo0O in O0ooo0O0oo0 [ 'eventlist' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , OOoo0O ) :
      Oo0ooOo0o = { 'title' : unicode ( oo0oOo )
 , 'uicode' : re . sub ( r'uicode:' , '' , OOoo0O )
 }
      oO0o0OOOO . append ( Oo0ooOo0o )
      break
      if 22 - 22: iIii1I11I1II1 / i11iIiiIii * iIii1I11I1II1 * II111iiii . OOooOOo / i11iIiiIii
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
  return oO0o0OOOO
  if 52 - 52: o0oOOo0O0Ooo
 def GetDeeplinkList ( self , gn_str , came_str , page_int ) :
  o0OO0oOO0O0 = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  iIIi1i1 = 'quick'
  i1IIIiiII1 = OOOOoOoo0O0O0 = OOOo00oo0oO = ''
  IIiIi1iI = False
  i1IiiiI1iI = { }
  if 49 - 49: Ii1I / OoO0O00 . II111iiii
  try :
   if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
   iii11I111 = '/cf/deeplink/' + gn_str
   i1iIIi1 = self . GetDefaultParams ( )
   oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 31 - 31: II111iiii . I1IiiI
   if not ( 'url' in OoOo00o ) : return None
   II1I = OoOo00o [ 'url' ]
   if 84 - 84: O00oOoOoO0o0O . i11iIiiIii . O00oOoOoO0o0O * I1ii11iIi11i - I11i
   print II1I
   if 42 - 42: i11iIiiIii
   if 33 - 33: iii1I1I - O0 * i1IIi * o0oOOo0O0Ooo - Oo0Ooo
   iii11I111 = urlparse . urlsplit ( II1I ) . path
   iiIiI = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( II1I ) . query ) )
   if 91 - 91: iii1I1I % i1IIi % iIii1I11I1II1
   iiIiI [ 'came' ] = came_str
   iiIiI [ 'limit' ] = str ( self . LIST_LIMIT )
   if 'contenttype' in iiIiI : iIIi1i1 = iiIiI [ 'contenttype' ]
   if came_str == 'movie' : iiIiI [ 'mtype' ] = 'svod'
   if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
   if page_int != 1 :
    iiIiI [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
    iiIiI [ 'page' ] = str ( page_int )
    if 45 - 45: oO0o - O00oOoOoO0o0O - OoooooooOO - OoO0O00 . II111iiii / O0
   oo0Ooo0 = self . HTTPTAG + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( i1iIIi1 )
   if 51 - 51: O0 + iii1I1I
   if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
   if 48 - 48: O0
   if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
   if 41 - 41: Ii1I - O0 - O0
   if 68 - 68: OOooOOo % O0oo0OO0
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 88 - 88: iIii1I11I1II1 - Oo0ooO0oo0oO + OOooOOo
   if 40 - 40: I1IiiI * Ii1I + OOooOOo % iii1I1I
   if not ( 'celllist' in OoOo00o [ 'cell_toplist' ] ) : return o0OO0oOO0O0 , IIiIi1iI
   OOOOOoo0 = OoOo00o [ 'cell_toplist' ] [ 'celllist' ]
   if 49 - 49: O0 . iii1I1I
   if 11 - 11: O00oOoOoO0o0O * I1IiiI . iIii1I11I1II1 % OoooooooOO + iii1I1I
   if 78 - 78: OoO0O00 . OOooOOo + OoO0O00 / I11i / OoO0O00
   if ( iIIi1i1 == 'channel' and came_str == 'live' ) :
    if ( 'genre' in iiIiI ) :
     oO0O00OoOO0 = iiIiI [ 'genre' ]
    else :
     oO0O00OoOO0 = 'all'
    print "*epgcall*"
    i1IiiiI1iI = self . GetEPGList ( oO0O00OoOO0 )
    if 82 - 82: II111iiii . O00oOoOoO0o0O - iIii1I11I1II1 - O00oOoOoO0o0O * II111iiii
    if 77 - 77: iIii1I11I1II1 * OoO0O00
    if 95 - 95: I1IiiI + i11iIiiIii
   for O0ooo0O0oo0 in OOOOOoo0 :
    I1Ii = O0oo00o0O = i1I1I = ''
    if 12 - 12: i11iIiiIii / OoO0O00
    I1Ii = O0ooo0O0oo0 . get ( 'title_list' ) [ 0 ] . get ( 'text' )
    if ( len ( O0ooo0O0oo0 . get ( 'title_list' ) ) > 1 ) :
     if ( O0ooo0O0oo0 . get ( 'title_list' ) [ 1 ] . get ( 'text' ) . startswith ( '@' ) ) :
      for o0O in O0ooo0O0oo0 . get ( 'bottom_taglist' ) :
       if o0O == 'playy' or o0O == 'won' : O0oo00o0O = o0O
     else :
      O0oo00o0O = O0ooo0O0oo0 . get ( 'title_list' ) [ 1 ] . get ( 'text' )
      O0oo00o0O = re . sub ( r'(\$O\$)|(\&[a-z]{2}\;)' , '' , O0oo00o0O )
    if ( O0ooo0O0oo0 . get ( 'thumbnail' ) != '' ) : i1I1I = 'https://%s' % O0ooo0O0oo0 . get ( 'thumbnail' )
    if 2 - 2: iIii1I11I1II1 / oO0o + OoO0O00 / OOooOOo
    II = O0ooo0O0oo0 [ 'event_list' ] [ 1 ] . get ( 'url' )
    OOOO0oo0 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( II ) . query ) )
    if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
    if re . search ( u'programid=\&' , II ) and ( 'contentid' in OOOO0oo0 ) :
     i1IIIiiII1 = OOOO0oo0 [ 'contentid' ]
     OOOOoOoo0O0O0 = 'direct'
    elif ( 'contentid' in OOOO0oo0 ) :
     i1IIIiiII1 = OOOO0oo0 [ 'contentid' ]
     OOOOoOoo0O0O0 = 'contentid'
    elif ( 'programid' in OOOO0oo0 ) :
     i1IIIiiII1 = OOOO0oo0 [ 'programid' ]
     OOOOoOoo0O0O0 = 'programid'
     iIIi1i1 = 'program'
    elif ( 'channelid' in OOOO0oo0 ) :
     i1IIIiiII1 = OOOO0oo0 [ 'channelid' ]
     OOOOoOoo0O0O0 = 'channelid'
     if 47 - 47: iii1I1I - Ii1I . II111iiii + OoooooooOO . i11iIiiIii
     if i1IIIiiII1 in i1IiiiI1iI :
      OOOo00oo0oO = i1IiiiI1iI [ i1IIIiiII1 ]
     else :
      OOOo00oo0oO = ''
      if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
    elif ( 'movieid' in OOOO0oo0 ) :
     i1IIIiiII1 = OOOO0oo0 [ 'movieid' ]
     OOOOoOoo0O0O0 = 'movieid'
     if 87 - 87: Oo0Ooo . O00oOoOoO0o0O
     iIIi1i1 = 'movie'
    else :
     i1IIIiiII1 = '-'
     OOOOoOoo0O0O0 = '-'
     if 75 - 75: Oo0ooO0oo0oO + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iii1I1I
    Oo0ooOo0o = { 'title' : unicode ( I1Ii )
 , 'subtitle' : unicode ( O0oo00o0O )
 , 'thumbnail' : i1I1I
 , 'uicode' : iIIi1i1
 , 'contentid' : i1IIIiiII1
 , 'contentidType' : OOOOoOoo0O0O0
 , 'viewage' : O0ooo0O0oo0 . get ( 'age' )
 , 'channelepg' : OOOo00oo0oO
 }
    o0OO0oOO0O0 . append ( Oo0ooOo0o )
    if 55 - 55: OOooOOo . I1IiiI
   iiiIIi1II = int ( OoOo00o [ 'cell_toplist' ] [ 'pagecount' ] )
   if OoOo00o [ 'cell_toplist' ] [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 'cell_toplist' ] [ 'count' ] )
   else : o0O00oOoOO = self . LIST_LIMIT
   if 61 - 61: Oo0Ooo % O00oOoOoO0o0O . Oo0Ooo
   if 100 - 100: O0oo0OO0 * O0
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
   if 79 - 79: O0
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 78 - 78: I1ii11iIi11i + OOooOOo - O0oo0OO0
  return ( o0OO0oOO0O0 , IIiIi1iI )
  if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
  if 57 - 57: OoO0O00 / Oo0ooO0oo0oO
 def GetEpisodeList ( self , contentid , contenttype , contentidType , page_int , orderby = 'desc' ) :
  Ii1I1Ii = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  IIiIi1iI = False
  if 69 - 69: I1IiiI / o0oOOo0O0Ooo . O00oOoOoO0o0O * O0oo0OO0 % Ii1I - o0oOOo0O0Ooo
  if orderby == 'desc' :
   orderby = 'new'
  else :
   orderby = 'old'
   if 13 - 13: Ii1I . i11iIiiIii
  try :
   i1iIIi1 = self . GetDefaultParams ( )
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
   if contentidType == 'contentid' :
    iii11I111 = '/cf/vod/contents/' + contentid
    if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
    oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , i1iIIi1 )
    II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
    OoOo00o = json . loads ( II1Iiii1111i )
    if 33 - 33: O0oo0OO0 + iii1I1I * oO0o / iIii1I11I1II1 - I1IiiI
    if not ( 'programid' in OoOo00o ) : return None
    O0oO = OoOo00o [ 'programid' ]
    if 73 - 73: I1ii11iIi11i * i11iIiiIii % oO0o . I1ii11iIi11i
   else :
    O0oO = contentid
    if 66 - 66: oO0o + oO0o + Oo0ooO0oo0oO / iii1I1I + OOooOOo
    if 30 - 30: O0
    if 44 - 44: oO0o / I11i / I11i
   iii11I111 = '/vod/programs-contents/' + O0oO
   if 87 - 87: Oo0Ooo . I1IiiI - II111iiii + O0 / Oo0Ooo / oO0o
   iiIiI = { 'limit' : self . EP_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . EP_LIMIT )
 , 'orderby' : orderby
   }
   if 25 - 25: I1IiiI . I1IiiI - OoOoOO00 % OoOoOO00 - i11iIiiIii / O0oo0OO0
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * O00oOoOoO0o0O
   if not ( 'list' in OoOo00o ) : return None
   OOOoOo = OoOo00o [ 'list' ]
   if 51 - 51: Oo0ooO0oo0oO / iIii1I11I1II1 % Oo0Ooo * I1IiiI % O0oo0OO0
   if 76 - 76: o0oOOo0O0Ooo - i11iIiiIii
   for O0ooo0O0oo0 in OOOoOo :
    iIIIiIi = O0ooo0O0oo0 . get ( 'programtitle' )
    OO0O0 = '%s회, %s(%s)' % ( O0ooo0O0oo0 . get ( 'episodenumber' ) , O0ooo0O0oo0 . get ( 'releasedate' ) , O0ooo0O0oo0 . get ( 'releaseweekday' ) )
    if ( O0ooo0O0oo0 . get ( 'image' ) != '' ) : I11I11 = 'https://%s' % O0ooo0O0oo0 . get ( 'image' )
    if 69 - 69: OoOoOO00
    OO0OoOO0o0o = unicode ( O0ooo0O0oo0 . get ( 'synopsis' ) )
    OO0OoOO0o0o = re . sub ( u'(\<[a-zA-Z]{1,2}\>)|(\<\/[a-zA-Z]{1,2}\>)' , '' , OO0OoOO0o0o )
    if 95 - 95: i11iIiiIii
    iI1111iiii = { 'title' : unicode ( iIIIiIi )
 , 'subtitle' : unicode ( OO0O0 )
 , 'thumbnail' : I11I11
 , 'uicode' : contenttype
 , 'contentid' : O0ooo0O0oo0 . get ( 'contentid' )
 , 'programid' : O0ooo0O0oo0 . get ( 'programid' )
 , 'synopsis' : OO0OoOO0o0o
 , 'viewage' : O0ooo0O0oo0 . get ( 'targetage' )
 }
    Ii1I1Ii . append ( iI1111iiii )
    if 67 - 67: OoooooooOO / I1IiiI * Ii1I + I11i
   iiiIIi1II = int ( OoOo00o [ 'pagecount' ] )
   if OoOo00o [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 'count' ] )
   else : o0O00oOoOO = self . EP_LIMIT
   if 65 - 65: OoooooooOO - I1ii11iIi11i / Oo0ooO0oo0oO / II111iiii / i1IIi
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 71 - 71: O0oo0OO0 + Ii1I
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 28 - 28: OOooOOo
  return ( Ii1I1Ii , IIiIi1iI )
  if 38 - 38: Oo0ooO0oo0oO % II111iiii % I11i / OoO0O00 + OoOoOO00 / i1IIi
  if 54 - 54: iIii1I11I1II1 % I1ii11iIi11i - OOooOOo / oO0o - OoO0O00 . I11i
 def GetMyviewList ( self , contenttype , page_int ) :
  IIo0Oo0oO0oOO00 = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  IIiIi1iI = False
  if 92 - 92: OoooooooOO * O0oo0OO0
  try :
   i1iIIi1 = self . GetDefaultParams ( )
   if 100 - 100: O0oo0OO0 + O0oo0OO0 * O00oOoOoO0o0O
   iii11I111 = '/myview/contents'
   if 1 - 1: Oo0ooO0oo0oO . Oo0ooO0oo0oO / OoOoOO00 - O0oo0OO0
   iiIiI = { 'contenttype' : contenttype
 , 'limit' : self . MV_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . MV_LIMIT )
 , 'orderby' : 'new'
 }
   if 86 - 86: iIii1I11I1II1 / OoOoOO00 . II111iiii
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 19 - 19: I1ii11iIi11i % OoooooooOO % O00oOoOoO0o0O * o0oOOo0O0Ooo % O0
   if not ( 'list' in OoOo00o [ 0 ] ) : return None
   ooo = OoOo00o [ 0 ] [ 'list' ]
   if 27 - 27: Oo0ooO0oo0oO % I1IiiI
   for O0ooo0O0oo0 in ooo :
    if 73 - 73: OOooOOo
    if contenttype == 'vod' :
     iIIIiIi = O0ooo0O0oo0 . get ( 'programtitle' )
     OO0O0 = '%s회, %s' % ( O0ooo0O0oo0 . get ( 'episodenumber' ) , O0ooo0O0oo0 . get ( 'releasedate' ) )
     i1IIIiiII1 = O0ooo0O0oo0 . get ( 'contentid' )
     O0oO = O0ooo0O0oo0 . get ( 'programid' )
     if 70 - 70: iIii1I11I1II1
    else :
     iIIIiIi = O0ooo0O0oo0 . get ( 'title' )
     OO0O0 = '%s' % ( O0ooo0O0oo0 . get ( 'releasedate' ) )
     i1IIIiiII1 = O0oO = O0ooo0O0oo0 . get ( 'movieid' )
     if 31 - 31: O00oOoOoO0o0O - I1IiiI % iIii1I11I1II1
    if ( O0ooo0O0oo0 . get ( 'image' ) != '' ) : I11I11 = 'https://%s' % O0ooo0O0oo0 . get ( 'image' )
    if 92 - 92: i1IIi - iIii1I11I1II1
    IIIIIIii1 = { 'title' : unicode ( iIIIiIi )
 , 'subtitle' : unicode ( OO0O0 )
 , 'thumbnail' : I11I11
 , 'uicode' : contenttype
 , 'contentid' : i1IIIiiII1
 , 'programid' : O0oO
 , 'viewage' : O0ooo0O0oo0 . get ( 'targetage' )
 }
    if 88 - 88: OoO0O00
    IIo0Oo0oO0oOO00 . append ( IIIIIIii1 )
    if 71 - 71: I1ii11iIi11i
    if 7 - 7: I1ii11iIi11i - I1IiiI . iIii1I11I1II1 - i1IIi
   iiiIIi1II = int ( OoOo00o [ 0 ] [ 'pagecount' ] )
   if OoOo00o [ 0 ] [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 0 ] [ 'count' ] )
   else : o0O00oOoOO = self . MV_LIMIT
   if 59 - 59: o0oOOo0O0Ooo
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 81 - 81: OoOoOO00 - OoOoOO00 . iii1I1I
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 73 - 73: I11i % i11iIiiIii - I1IiiI
  return IIo0Oo0oO0oOO00 , IIiIi1iI
  if 7 - 7: O0 * i11iIiiIii * Ii1I + Oo0ooO0oo0oO % OoO0O00 - Oo0ooO0oo0oO
  if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
 def GetSearchList ( self , search_key , genre , page_int , exclusion21 = False ) :
  ii = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  IIiIi1iI = False
  if 68 - 68: iii1I1I - I1IiiI / O0oo0OO0 / I11i
  try :
   i1iIIi1 = self . GetDefaultParams ( )
   if 12 - 12: Ii1I + i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . I11i
   iii11I111 = '/cf/search/list.js'
   if 5 - 5: i1IIi + O00oOoOoO0o0O / o0oOOo0O0Ooo . iii1I1I / I11i
   iiIiI = { 'type' : 'program' if genre == 'vod' else 'movie'
 , 'keyword' : search_key
 , 'offset' : str ( ( page_int - 1 ) * self . LIST_LIMIT )
 , 'limit' : self . LIST_LIMIT
   , 'orderby' : 'score'
 , 'isplayymovie' : 'y'
 }
   if 32 - 32: I1IiiI % iIii1I11I1II1 / i1IIi - I1IiiI
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( i1iIIi1 )
   if 7 - 7: O0oo0OO0 * OoO0O00 - Oo0ooO0oo0oO + OOooOOo * I1IiiI % OoO0O00
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 15 - 15: OoOoOO00 % I1IiiI * I11i
   if not ( 'celllist' in OoOo00o [ 'cell_toplist' ] ) : return ii , IIiIi1iI
   O0OoooO0 = OoOo00o [ 'cell_toplist' ] [ 'celllist' ]
   if 85 - 85: I11i
   if 20 - 20: oO0o % O00oOoOoO0o0O
   for O0ooo0O0oo0 in O0OoooO0 :
    if 19 - 19: I1ii11iIi11i % O00oOoOoO0o0O + Oo0ooO0oo0oO / O0oo0OO0 . Oo0ooO0oo0oO
    iIIIiIi = O0ooo0O0oo0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if ( O0ooo0O0oo0 . get ( 'thumbnail' ) != '' ) : I11I11 = 'https://%s' % O0ooo0O0oo0 . get ( 'thumbnail' )
    if 12 - 12: i1IIi + i1IIi - I1ii11iIi11i * Oo0Ooo % Oo0Ooo - II111iiii
    for OOoo0O in O0ooo0O0oo0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , OOoo0O ) :
      if genre == 'vod' :
       i1IIIiiII1 = ''
       O0oO = re . sub ( r'uicode:' , '' , OOoo0O )
      else :
       i1IIIiiII1 = re . sub ( r'uicode:' , '' , OOoo0O )
       O0oO = ''
       if O0ooo0O0oo0 . get ( 'bottom_taglist' ) [ 0 ] == 'playy' :
        iIIIiIi += ' [playy]'
        if 52 - 52: Oo0ooO0oo0oO . iii1I1I + O0oo0OO0
      IIIIIIii1 = { 'title' : unicode ( iIIIiIi )
 , 'thumbnail' : I11I11
 , 'uicode' : genre
 , 'contentid' : i1IIIiiII1
 , 'programid' : O0oO
 , 'viewage' : O0ooo0O0oo0 . get ( 'age' )
 }
      if 38 - 38: i1IIi - II111iiii . O0oo0OO0
    if exclusion21 == False or O0ooo0O0oo0 . get ( 'age' ) != '21' :
     ii . append ( IIIIIIii1 )
     if 58 - 58: I1IiiI . iii1I1I + OoOoOO00
     if 66 - 66: iii1I1I / oO0o * OoooooooOO + OoooooooOO % I11i
   iiiIIi1II = int ( OoOo00o [ 'cell_toplist' ] [ 'pagecount' ] )
   if OoOo00o [ 'cell_toplist' ] [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 'cell_toplist' ] [ 'count' ] )
   else : o0O00oOoOO = self . LIST_LIMIT
   if 49 - 49: oO0o - i11iIiiIii . O0oo0OO0 * Ii1I % iii1I1I + i1IIi
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 71 - 71: o0oOOo0O0Ooo
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 38 - 38: oO0o % OoOoOO00 + I1ii11iIi11i . i11iIiiIii
  return ii , IIiIi1iI
  if 53 - 53: i11iIiiIii * iii1I1I
  if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / II111iiii % Oo0Ooo
 def GetGenreGroup ( self , maintype , subtype , orderby , ordernm , exclusion21 = False ) :
  i1i11I11 = [ ]
  if 10 - 10: O0 - OoooooooOO . OoOoOO00
  try :
   i1iIIi1 = self . GetDefaultParams ( )
   if 44 - 44: O00oOoOoO0o0O - o0oOOo0O0Ooo . i1IIi . O00oOoOoO0o0O * OoOoOO00
   iii11I111 = '/cf/filters'
   if 5 - 5: O0oo0OO0
   iiIiI = { 'type' : maintype }
   if 90 - 90: O0oo0OO0 . Oo0ooO0oo0oO / Ii1I - I11i
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 40 - 40: OoooooooOO
   if not ( maintype in OoOo00o ) : return None
   I1i1i1 = OoOo00o [ maintype ]
   if 73 - 73: O0 * iii1I1I + Ii1I + Oo0ooO0oo0oO
   if subtype == '-' :
    if 40 - 40: II111iiii . OoOoOO00 * O0oo0OO0 + OOooOOo + OOooOOo
    for O0ooo0O0oo0 in I1i1i1 :
     I1ii1I1iiii = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( O0ooo0O0oo0 . get ( 'url' ) ) . query ) )
     if 36 - 36: OoooooooOO . OoO0O00
     IIIIIIii1 = { 'title' : O0ooo0O0oo0 . get ( 'text' )
 , 'genre' : O0ooo0O0oo0 . get ( 'id' )
 , 'subgenre' : '-'
 , 'adult' : O0ooo0O0oo0 . get ( 'adult' )
 , 'broadcastid' : I1ii1I1iiii . get ( 'broadcastid' )
 , 'contenttype' : I1ii1I1iiii . get ( 'contenttype' )
 , 'uiparent' : I1ii1I1iiii . get ( 'uiparent' )
 , 'uirank' : I1ii1I1iiii . get ( 'uirank' )
 , 'uitype' : I1ii1I1iiii . get ( 'uitype' )
 , 'orderby' : orderby
 , 'ordernm' : ordernm
 }
     if exclusion21 == False or IIIIIIii1 . get ( 'adult' ) == 'n' :
      i1i11I11 . append ( IIIIIIii1 )
      if 56 - 56: Oo0Ooo . I1ii11iIi11i . I1IiiI
   else :
    for O0ooo0O0oo0 in I1i1i1 :
     if O0ooo0O0oo0 . get ( 'id' ) == subtype :
      for ii111I in O0ooo0O0oo0 [ 'sublist' ] :
       I1ii1I1iiii = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( ii111I . get ( 'url' ) ) . query ) )
       if 17 - 17: I1IiiI . O0 + OoO0O00
       IIIIIIii1 = { 'title' : ii111I . get ( 'text' )
 , 'genre' : subtype
 , 'subgenre' : ii111I . get ( 'id' )
 , 'adult' : ii111I . get ( 'adult' )
 , 'broadcastid' : I1ii1I1iiii . get ( 'broadcastid' )
 , 'contenttype' : I1ii1I1iiii . get ( 'contenttype' )
 , 'uiparent' : I1ii1I1iiii . get ( 'uiparent' )
 , 'uirank' : I1ii1I1iiii . get ( 'uirank' )
 , 'uitype' : I1ii1I1iiii . get ( 'uitype' )
 , 'orderby' : orderby
 , 'ordernm' : ordernm
 }
       i1i11I11 . append ( IIIIIIii1 )
      break
      if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 20 - 20: I1IiiI
  return i1i11I11
  if 95 - 95: iii1I1I - I1IiiI
  if 34 - 34: Oo0ooO0oo0oO * I1IiiI . i1IIi * Oo0ooO0oo0oO / Oo0ooO0oo0oO
 def GetGenreGroup_sub ( self , in_params ) :
  i1i11I11 = [ ]
  if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
  try :
   i1iIIi1 = self . GetDefaultParams ( )
   if 55 - 55: Oo0ooO0oo0oO - I11i + II111iiii + iii1I1I % Ii1I
   iii11I111 = '/cf/vod/newcontents'
   if 41 - 41: i1IIi - I11i - Ii1I
   iiIiI = { 'WeekDay' : 'all'
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
   if 8 - 8: OoO0O00 + O0oo0OO0 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + Oo0ooO0oo0oO
   if not ( 'filter_item_list' in OoOo00o [ 'filter' ] [ 'filterlist' ] [ 1 ] ) : return None
   I1i1i1 = OoOo00o [ 'filter' ] [ 'filterlist' ] [ 1 ] [ 'filter_item_list' ]
   if 44 - 44: II111iiii
   for O0ooo0O0oo0 in I1i1i1 :
    IIIIIIii1 = { 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )

 , 'adult' : O0ooo0O0oo0 . get ( 'adult' )
 , 'title' : O0ooo0O0oo0 . get ( 'title' )
 , 'subgenre' : O0ooo0O0oo0 . get ( 'api_parameters' ) [ O0ooo0O0oo0 . get ( 'api_parameters' ) . find ( '=' ) + 1 : ]
 , 'orderby' : in_params . get ( 'orderby' )
 }
    i1i11I11 . append ( IIIIIIii1 )
    if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 35 - 35: iIii1I11I1II1
  return i1i11I11
  if 42 - 42: O0oo0OO0 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
  if 31 - 31: iii1I1I . OOooOOo - Oo0ooO0oo0oO . OoooooooOO / OoooooooOO
 def GetGenreList ( self , genre , in_params , page_int ) :
  i1i11I11 = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  IIiIi1iI = False
  if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
  try :
   i1iIIi1 = self . GetDefaultParams ( )
   if 21 - 21: O0 % O00oOoOoO0o0O . I1IiiI / II111iiii + O00oOoOoO0o0O
   iiIiI = { 'WeekDay' : 'all'
 , 'adult' : in_params . get ( 'adult' )
 , 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )

   , 'orderby' : in_params . get ( 'orderby' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )
 }
   if 53 - 53: oO0o - I1IiiI - oO0o * iii1I1I
   if genre == 'vodgenre' :
    iii11I111 = '/cf/vod/newcontents'
    if 71 - 71: O0 - iIii1I11I1II1
    if in_params . get ( 'subgenre' ) != '-' :
     iiIiI [ 'subgenre' ] = in_params . get ( 'subgenre' )
   else :
    iii11I111 = '/cf/movie/contents'
    if 12 - 12: OOooOOo / o0oOOo0O0Ooo
    iiIiI [ 'price' ] = 'all'
    if 42 - 42: Oo0Ooo
    if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
    iiIiI [ 'sptheme' ] = 'svod'
    if 46 - 46: Oo0Ooo
    if 1 - 1: iii1I1I
   iiIiI [ 'limit' ] = self . LIST_LIMIT
   iiIiI [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
   iiIiI [ 'page' ] = str ( page_int )
   if 97 - 97: OOooOOo + iii1I1I + O0 + i11iIiiIii
   if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iii1I1I % iii1I1I + i11iIiiIii
   if not ( 'celllist' in OoOo00o [ 'cell_toplist' ] ) : return None
   I1i1i1 = OoOo00o [ 'cell_toplist' ] [ 'celllist' ]
   if 72 - 72: iIii1I11I1II1 * Ii1I % Oo0ooO0oo0oO / OoO0O00
   if 35 - 35: Oo0ooO0oo0oO + i1IIi % I1ii11iIi11i % I11i + oO0o
   for O0ooo0O0oo0 in I1i1i1 :
    iIIIiIi = I11I11 = ''
    if 17 - 17: i1IIi
    iIIIiIi = O0ooo0O0oo0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if 21 - 21: Oo0Ooo
    if ( O0ooo0O0oo0 . get ( 'thumbnail' ) != '' ) : I11I11 = 'https://%s' % O0ooo0O0oo0 . get ( 'thumbnail' )
    if 29 - 29: I11i / II111iiii / Oo0ooO0oo0oO * OOooOOo
    for OOoo0O in O0ooo0O0oo0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , OOoo0O ) :
      IIIIIIii1 = { 'title' : unicode ( iIIIiIi )
 , 'uicode' : re . sub ( r'uicode:' , '' , OOoo0O )
 , 'thumbnail' : I11I11
 , 'viewage' : O0ooo0O0oo0 . get ( 'age' )
 }
      if 10 - 10: O0oo0OO0 % O00oOoOoO0o0O * O00oOoOoO0o0O . I11i / Ii1I % OOooOOo
    i1i11I11 . append ( IIIIIIii1 )
    if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
    if 28 - 28: Oo0ooO0oo0oO + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
   iiiIIi1II = int ( OoOo00o [ 'cell_toplist' ] [ 'pagecount' ] )
   if OoOo00o [ 'cell_toplist' ] [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 'cell_toplist' ] [ 'count' ] )
   else : o0O00oOoOO = self . LIST_LIMIT
   if 54 - 54: i1IIi + II111iiii
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 5 - 5: Ii1I
  return i1i11I11 , IIiIi1iI
  if 46 - 46: O00oOoOoO0o0O
  if 45 - 45: Oo0ooO0oo0oO
 def GetEPGList ( self , genre ) :
  IIi = { }
  if 94 - 94: II111iiii - Oo0Ooo
  try :
   import datetime
   oo0oO0 = datetime . datetime . now ( )
   if genre == 'all' :
    ii1 = oo0oO0 + datetime . timedelta ( hours = 2 )
   else :
    ii1 = oo0oO0 + datetime . timedelta ( hours = 3 )
    if 1 - 1: Oo0ooO0oo0oO % iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % I1IiiI
   i1iIIi1 = self . GetDefaultParams ( )
   if 89 - 89: Ii1I
   iiIiI = { 'limit' : '100'
 , 'offset' : '0'
 , 'genre' : genre
 , 'startdatetime' : oo0oO0 . strftime ( '%Y-%m-%d %H:%M' )
 , 'enddatetime' : ii1 . strftime ( '%Y-%m-%d %H:%M' )
 }
   iii11I111 = '/live/epgs'
   if 76 - 76: Oo0ooO0oo0oO
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 15 - 15: OOooOOo . I11i + OoooooooOO - OoO0O00
   Oo0 = OoOo00o [ 'list' ]
   if 59 - 59: I1IiiI * II111iiii . O0
   if 56 - 56: Ii1I - iii1I1I % I1IiiI - o0oOOo0O0Ooo
   for O0ooo0O0oo0 in Oo0 :
    Oo00O = ''
    if 12 - 12: o0oOOo0O0Ooo - Oo0ooO0oo0oO * O0oo0OO0
    for II1111ii in O0ooo0O0oo0 [ 'list' ] :
     if Oo00O : Oo00O += '\n'
     Oo00O += II1111ii [ 'title' ] + '\n'
     Oo00O += ' [%s ~ %s]' % ( II1111ii [ 'starttime' ] [ - 5 : ] , II1111ii [ 'endtime' ] [ - 5 : ] ) + '\n'
     if 27 - 27: O0
     if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
     if 28 - 28: i1IIi - iii1I1I
    IIi [ O0ooo0O0oo0 [ 'channelid' ] ] = unicode ( Oo00O )
    if 54 - 54: iii1I1I - O0 % OOooOOo
    if 73 - 73: O0 . OoOoOO00 + I1IiiI - I11i % I11i . I11i
    if 17 - 17: Ii1I - OoooooooOO % Ii1I . O00oOoOoO0o0O / i11iIiiIii % iii1I1I
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 28 - 28: I11i
  return IIi
  if 58 - 58: OoOoOO00
  if 37 - 37: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i
 def GetStreamingURL ( self , contentid , contenttype , quality_int ) :
  oo0oOOo0 = O0OoO0ooOO0o = OoOo0oOooOoOO = oo00ooOoO00 = ''
  o00oOoOo0 = [ ]
  if 72 - 72: O0oo0OO0
  if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iii1I1I
  try :
   if contenttype == 'channel' :
    iii11I111 = '/live/channels/' + contentid
    I1iii11 = 'live'
   elif contenttype == 'movie' :
    iii11I111 = '/cf/movie/contents/' + contentid
    I1iii11 = 'movie'
   else :
    iii11I111 = '/cf/vod/contents/' + contentid
    I1iii11 = 'vod'
    if 74 - 74: O0 / i1IIi
   i1iIIi1 = self . GetDefaultParams ( )
   oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 78 - 78: OoooooooOO . OoO0O00 + Oo0ooO0oo0oO - i1IIi
   ii1O0 = OoOo00o [ 'qualities' ] [ 'list' ]
   if ii1O0 == None : return ( oo0oOOo0 , O0OoO0ooOO0o , OoOo0oOooOoOO , oo00ooOoO00 )
   if 33 - 33: i1IIi
   Ii1iII1iI1 = 'hls'
   if 'drms' in OoOo00o :
    if OoOo00o [ 'drms' ] :
     Ii1iII1iI1 = 'dash'
     if 14 - 14: iii1I1I
   print ( Ii1iII1iI1 )
   if 99 - 99: iii1I1I
   if 'type' in OoOo00o :
    if OoOo00o [ 'type' ] == 'onair' :
     I1iii11 = 'onairvod'
     if 38 - 38: I1ii11iIi11i - iii1I1I / O0 . O0oo0OO0
     if 45 - 45: O0oo0OO0
   for oO in ii1O0 :
    o00oOoOo0 . append ( int ( oO . get ( 'id' ) . rstrip ( 'p' ) ) )
    if 17 - 17: Oo0Ooo % OOooOOo . i1IIi / OoooooooOO
  except Exception as OO00Oo :
   return ( oo0oOOo0 , O0OoO0ooOO0o , OoOo0oOooOoOO , oo00ooOoO00 )
   if 28 - 28: oO0o . II111iiii / I1ii11iIi11i + II111iiii . OoooooooOO . O00oOoOoO0o0O
   if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
   if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
  try :
   O00oOo00o0o = self . CheckQuality ( quality_int , o00oOoOo0 )
   iii11I111 = '/streaming'
   iiIiI = { 'contentid' : contentid
 , 'contenttype' : I1iii11
 , 'action' : Ii1iII1iI1
 , 'quality' : str ( O00oOo00o0o ) + 'p'
 , 'deviceModelId' : 'Windows 10'
 , 'guid' : self . GetGUID ( guidType = 2 )
 , 'lastplayid' : self . guid
 , 'authtype' : 'cookie'
 , 'isabr' : 'y'
 , 'ishevc' : 'n'
 }
   if 85 - 85: iii1I1I + OoooooooOO * iii1I1I - O0oo0OO0 % i11iIiiIii
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( i1iIIi1 ) + '&' + urllib . urlencode ( iiIiI )
   if 71 - 71: I1ii11iIi11i - Oo0ooO0oo0oO / OoOoOO00 * OoOoOO00 / i1IIi . i1IIi
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 53 - 53: O0oo0OO0
   oo0oOOo0 = OoOo00o [ 'playurl' ]
   if oo0oOOo0 == None : return None
   O0OoO0ooOO0o = OoOo00o [ 'awscookie' ]
   OoOo0oOooOoOO = OoOo00o [ 'drm' ]
   if 'previewmsg' in OoOo00o [ 'preview' ] : oo00ooOoO00 = OoOo00o [ 'preview' ] [ 'previewmsg' ]
   if 21 - 21: I11i
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 92 - 92: i11iIiiIii / O0oo0OO0 - iii1I1I % Oo0ooO0oo0oO * O0oo0OO0 + Oo0Ooo
  oo0oOOo0 = oo0oOOo0 . replace ( 'pooq.co.kr' , 'wavve.com' )
  if 11 - 11: OoooooooOO . O0oo0OO0
  return ( oo0oOOo0 , O0OoO0ooOO0o , OoOo0oOooOoOO , oo00ooOoO00 )
  if 80 - 80: OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / I1IiiI / OOooOOo
  if 13 - 13: O0oo0OO0 * Oo0ooO0oo0oO + i11iIiiIii * O0oo0OO0 - Oo0ooO0oo0oO
  if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * O00oOoOoO0o0O
  if 9 - 9: O00oOoOoO0o0O - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  if 39 - 39: O00oOoOoO0o0O * Oo0Ooo + iIii1I11I1II1 - O00oOoOoO0o0O + OOooOOo
  if 69 - 69: O0
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
