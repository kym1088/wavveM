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
  if 31 - 31: II111iiii + OoO0O00 . O0oo0OO0
  self . TARGETAGE = 'all'
  self . CREDENTIAL = 'none'
  self . HTTPTAG = 'https://'
  self . LIST_LIMIT = 30
  self . EP_LIMIT = 30
  self . MV_LIMIT = 24
  self . guid = 'none'
  self . guidtimestamp = 'none'
  if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
 def SaveCredential ( self , credential ) :
  self . CREDENTIAL = credential
  if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
 def LoadCredential ( self ) :
  return self . CREDENTIAL
  if 3 - 3: iii1I1I + O0
 def GetDefaultParams ( self ) :
  I1Ii = { 'apikey' : self . APIKEY ,
 'credential' : self . CREDENTIAL ,
 'device' : self . DEVICE ,
 'drm' : self . DRM ,
 'partner' : self . PARTNER ,
 'pooqzone' : self . POOQZONE ,
 'region' : self . REGION ,
 'targetage' : self . TARGETAGE
 }
  return I1Ii
  if 66 - 66: Ii1I
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
   I1Ii = self . GetDefaultParams ( )
   OOOO00ooo0Ooo = { 'id' : user_id
 , 'password' : user_pw
 , 'profile' : '0'
 , 'pushid' : ''
 , 'type' : 'general'
 }
   oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , I1Ii )
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
   I1Ii = self . GetDefaultParams ( )
   oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , I1Ii )
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
   I1Ii = self . GetDefaultParams ( )
   oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , I1Ii )
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
 def GetDeeplinkList ( self , gn_str , came_str , page_int , addinfoyn = False ) :
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
   I1Ii = self . GetDefaultParams ( )
   oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , I1Ii )
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
   oo0Ooo0 = self . HTTPTAG + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( I1Ii )
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
    I1IiO0oo00o0O = i1I1I = iiI1I = ''
    if 12 - 12: i11iIiiIii - i1IIi - OoO0O00 . i1IIi - OOooOOo + O0
    I1IiO0oo00o0O = O0ooo0O0oo0 . get ( 'title_list' ) [ 0 ] . get ( 'text' )
    if ( len ( O0ooo0O0oo0 . get ( 'title_list' ) ) > 1 ) :
     if ( O0ooo0O0oo0 . get ( 'title_list' ) [ 1 ] . get ( 'text' ) . startswith ( '@' ) ) :
      for oO0OOOO0 in O0ooo0O0oo0 . get ( 'bottom_taglist' ) :
       if oO0OOOO0 == 'playy' or oO0OOOO0 == 'won' : i1I1I = oO0OOOO0
     else :
      i1I1I = O0ooo0O0oo0 . get ( 'title_list' ) [ 1 ] . get ( 'text' )
      i1I1I = re . sub ( r'(\$O\$)|(\&[a-z]{2}\;)' , '' , i1I1I )
    if ( O0ooo0O0oo0 . get ( 'thumbnail' ) != '' ) : iiI1I = 'https://%s' % O0ooo0O0oo0 . get ( 'thumbnail' )
    if 26 - 26: Ii1I
    I11iiI1i1 = O0ooo0O0oo0 [ 'event_list' ] [ 1 ] . get ( 'url' )
    I1i1Iiiii = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( I11iiI1i1 ) . query ) )
    if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
    if re . search ( u'programid=\&' , I11iiI1i1 ) and ( 'contentid' in I1i1Iiiii ) :
     i1IIIiiII1 = I1i1Iiiii [ 'contentid' ]
     OOOOoOoo0O0O0 = 'direct'
    elif ( 'contentid' in I1i1Iiiii ) :
     i1IIIiiII1 = I1i1Iiiii [ 'contentid' ]
     OOOOoOoo0O0O0 = 'contentid'
    elif ( 'programid' in I1i1Iiiii ) :
     i1IIIiiII1 = I1i1Iiiii [ 'programid' ]
     OOOOoOoo0O0O0 = 'programid'
     iIIi1i1 = 'program'
    elif ( 'channelid' in I1i1Iiiii ) :
     i1IIIiiII1 = I1i1Iiiii [ 'channelid' ]
     OOOOoOoo0O0O0 = 'channelid'
     if 87 - 87: Oo0Ooo . O00oOoOoO0o0O
     if i1IIIiiII1 in i1IiiiI1iI :
      OOOo00oo0oO = i1IiiiI1iI [ i1IIIiiII1 ]
     else :
      OOOo00oo0oO = ''
      if 75 - 75: Oo0ooO0oo0oO + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iii1I1I
    elif ( 'movieid' in I1i1Iiiii ) :
     i1IIIiiII1 = I1i1Iiiii [ 'movieid' ]
     OOOOoOoo0O0O0 = 'movieid'
     if 55 - 55: OOooOOo . I1IiiI
     iIIi1i1 = 'movie'
    else :
     i1IIIiiII1 = '-'
     OOOOoOoo0O0O0 = '-'
     if 61 - 61: Oo0Ooo % O00oOoOoO0o0O . Oo0Ooo
    o0oOO000oO0oo = { }
    o0oOO000oO0oo [ 'mpaa' ] = O0ooo0O0oo0 . get ( 'age' )
    try :
     if ( 'channelid' in I1i1Iiiii ) :
      o0oOO000oO0oo [ 'mediatype' ] = 'video'
      o0oOO000oO0oo [ 'title' ] = '%s < %s >' % ( unicode ( I1IiO0oo00o0O ) , unicode ( i1I1I ) )
      o0oOO000oO0oo [ 'tvshowtitle' ] = unicode ( i1I1I )
      o0oOO000oO0oo [ 'studio' ] = unicode ( I1IiO0oo00o0O )
     elif ( 'movieid' in I1i1Iiiii ) :
      o0oOO000oO0oo [ 'mediatype' ] = 'movie'
      o0oOO000oO0oo [ 'title' ] = unicode ( title_list )
     else :
      o0oOO000oO0oo [ 'mediatype' ] = 'episode'
      o0oOO000oO0oo [ 'title' ] = unicode ( title_list )
    except :
     None
     if 78 - 78: I1ii11iIi11i + OOooOOo - O0oo0OO0
    Oo0ooOo0o = { 'title' : unicode ( I1IiO0oo00o0O )
 , 'subtitle' : unicode ( i1I1I )
 , 'thumbnail' : iiI1I
 , 'uicode' : iIIi1i1
 , 'contentid' : i1IIIiiII1
 , 'contentidType' : OOOOoOoo0O0O0
 , 'viewage' : O0ooo0O0oo0 . get ( 'age' )
 , 'channelepg' : OOOo00oo0oO
 , 'info' : o0oOO000oO0oo
 }
    o0OO0oOO0O0 . append ( Oo0ooOo0o )
    if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
   iiiIIi1II = int ( OoOo00o [ 'cell_toplist' ] [ 'pagecount' ] )
   if OoOo00o [ 'cell_toplist' ] [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 'cell_toplist' ] [ 'count' ] )
   else : o0O00oOoOO = self . LIST_LIMIT
   if 57 - 57: OoO0O00 / Oo0ooO0oo0oO
   if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 7 - 7: O00oOoOoO0o0O * O0oo0OO0 % Ii1I - o0oOOo0O0Ooo
   if 13 - 13: Ii1I . i11iIiiIii
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
  try :
   if o0OO0oOO0O0 [ 0 ] . get ( 'contentidType' ) == 'movieid' and addinfoyn == True :
    I111iI = [ ]
    oOOo0 = { }
    if 16 - 16: oO0o % I1ii11iIi11i * i11iIiiIii % i11iIiiIii
    for O0OOOOo0O in o0OO0oOO0O0 : I111iI . append ( O0OOOOo0O . get ( 'contentid' ) )
    if 81 - 81: O0 / OoO0O00 . i1IIi + I1IiiI - I11i
    oOOo0 = self . GetMovieInfoList ( I111iI )
    if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
    for Ooo in range ( len ( o0OO0oOO0O0 ) ) :
     o0OO0oOO0O0 [ Ooo ] [ 'info' ] = oOOo0 . get ( o0OO0oOO0O0 [ Ooo ] [ 'contentid' ] )
  except :
   None
   if 62 - 62: OoooooooOO * I1IiiI
   if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
   if 50 - 50: O0oo0OO0 . o0oOOo0O0Ooo
  return ( o0OO0oOO0O0 , IIiIi1iI )
  if 97 - 97: O0 + OoOoOO00
  if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
 def GetEpisodeList ( self , contentid , contenttype , contentidType , page_int , orderby = 'desc' ) :
  iiIiI1i1 = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  IIiIi1iI = False
  if 69 - 69: Oo0ooO0oo0oO
  if orderby == 'desc' :
   orderby = 'new'
  else :
   orderby = 'old'
   if 40 - 40: O0oo0OO0 + OoooooooOO % o0oOOo0O0Ooo - iIii1I11I1II1 . I1IiiI
  try :
   I1Ii = self . GetDefaultParams ( )
   if 48 - 48: o0oOOo0O0Ooo - oO0o / OoooooooOO
   if 100 - 100: I1IiiI / o0oOOo0O0Ooo % II111iiii % Oo0Ooo % OOooOOo
   if contentidType == 'contentid' :
    iii11I111 = '/cf/vod/contents/' + contentid
    if 98 - 98: I11i % i11iIiiIii % Oo0ooO0oo0oO + Ii1I
    oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , I1Ii )
    II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
    OoOo00o = json . loads ( II1Iiii1111i )
    if 78 - 78: I1ii11iIi11i % oO0o / iii1I1I - iIii1I11I1II1
    if not ( 'programid' in OoOo00o ) : return None
    ooooo0O0000oo = OoOo00o [ 'programid' ]
    if 21 - 21: o0oOOo0O0Ooo - I1IiiI
   else :
    ooooo0O0000oo = contentid
    if 18 - 18: Oo0Ooo + I11i % OOooOOo - OoooooooOO - I1ii11iIi11i / i1IIi
    if 98 - 98: i1IIi / I11i
    if 32 - 32: Ii1I * iIii1I11I1II1 / OOooOOo
   iii11I111 = '/vod/programs-contents/' + ooooo0O0000oo
   if 38 - 38: Oo0ooO0oo0oO % II111iiii % I11i / OoO0O00 + OoOoOO00 / i1IIi
   iiIiI = { 'limit' : self . EP_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . EP_LIMIT )
 , 'orderby' : orderby
   }
   if 54 - 54: iIii1I11I1II1 % I1ii11iIi11i - OOooOOo / oO0o - OoO0O00 . I11i
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( I1Ii )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 11 - 11: I1ii11iIi11i . OoO0O00 * O00oOoOoO0o0O * OoooooooOO + Oo0ooO0oo0oO
   if not ( 'list' in OoOo00o ) : return None
   IiII111i1i11 = OoOo00o [ 'list' ]
   if 40 - 40: Oo0ooO0oo0oO * O00oOoOoO0o0O * i11iIiiIii
   if 57 - 57: Oo0ooO0oo0oO
   for O0ooo0O0oo0 in IiII111i1i11 :
    II11Iiii = O0ooo0O0oo0 . get ( 'programtitle' )
    i11I = '%s회, %s(%s)' % ( O0ooo0O0oo0 . get ( 'episodenumber' ) , O0ooo0O0oo0 . get ( 'releasedate' ) , O0ooo0O0oo0 . get ( 'releaseweekday' ) )
    if ( O0ooo0O0oo0 . get ( 'image' ) != '' ) : o00Oo0oooooo = 'https://%s' % O0ooo0O0oo0 . get ( 'image' )
    if 76 - 76: I11i / OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + O00oOoOoO0o0O
    o0o = unicode ( O0ooo0O0oo0 . get ( 'synopsis' ) )
    o0o = re . sub ( u'(\<[a-zA-Z]{1,2}\>)|(\<\/[a-zA-Z]{1,2}\>)' , '' , o0o )
    if 62 - 62: OoooooooOO . I11i
    o0oOO000oO0oo = { }
    o0oOO000oO0oo [ 'title' ] = unicode ( II11Iiii )
    o0oOO000oO0oo [ 'mediatype' ] = 'episode'
    o0oOO000oO0oo [ 'mpaa' ] = O0ooo0O0oo0 . get ( 'targetage' )
    try :
     if 'episodenumber' in O0ooo0O0oo0 : o0oOO000oO0oo [ 'episode' ] = O0ooo0O0oo0 . get ( 'episodenumber' )
     if 'releasedate' in O0ooo0O0oo0 : o0oOO000oO0oo [ 'year' ] = int ( O0ooo0O0oo0 . get ( 'releasedate' ) [ : 4 ] )
     if 'releasedate' in O0ooo0O0oo0 : o0oOO000oO0oo [ 'aired' ] = O0ooo0O0oo0 . get ( 'releasedate' )
     if 'playtime' in O0ooo0O0oo0 : o0oOO000oO0oo [ 'duration' ] = O0ooo0O0oo0 . get ( 'playtime' )
     if 'episodeactors' in O0ooo0O0oo0 :
      if O0ooo0O0oo0 . get ( 'episodeactors' ) != '' : o0oOO000oO0oo [ 'cast' ] = O0ooo0O0oo0 . get ( 'episodeactors' ) . split ( ',' )
    except :
     None
     if 61 - 61: OoOoOO00 - OOooOOo - i1IIi
    IiI1iIiIIIii = { 'title' : unicode ( II11Iiii )
 , 'subtitle' : unicode ( i11I )
 , 'thumbnail' : o00Oo0oooooo
 , 'uicode' : contenttype
 , 'contentid' : O0ooo0O0oo0 . get ( 'contentid' )
 , 'programid' : O0ooo0O0oo0 . get ( 'programid' )
 , 'synopsis' : o0o
 , 'viewage' : O0ooo0O0oo0 . get ( 'targetage' )
 , 'info' : o0oOO000oO0oo
    }
    iiIiI1i1 . append ( IiI1iIiIIIii )
    if 53 - 53: i1IIi
   iiiIIi1II = int ( OoOo00o [ 'pagecount' ] )
   if OoOo00o [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 'count' ] )
   else : o0O00oOoOO = self . EP_LIMIT
   if 59 - 59: o0oOOo0O0Ooo
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 81 - 81: OoOoOO00 - OoOoOO00 . iii1I1I
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 73 - 73: I11i % i11iIiiIii - I1IiiI
  return ( iiIiI1i1 , IIiIi1iI )
  if 7 - 7: O0 * i11iIiiIii * Ii1I + Oo0ooO0oo0oO % OoO0O00 - Oo0ooO0oo0oO
  if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
 def GetMyviewList ( self , contenttype , page_int , addinfoyn = False ) :
  ii = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  IIiIi1iI = False
  if 68 - 68: iii1I1I - I1IiiI / O0oo0OO0 / I11i
  try :
   I1Ii = self . GetDefaultParams ( )
   if 12 - 12: Ii1I + i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . I11i
   iii11I111 = '/myview/contents'
   if 5 - 5: i1IIi + O00oOoOoO0o0O / o0oOOo0O0Ooo . iii1I1I / I11i
   iiIiI = { 'contenttype' : contenttype
 , 'limit' : self . MV_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . MV_LIMIT )
 , 'orderby' : 'new'
 }
   if 32 - 32: I1IiiI % iIii1I11I1II1 / i1IIi - I1IiiI
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( I1Ii )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 7 - 7: O0oo0OO0 * OoO0O00 - Oo0ooO0oo0oO + OOooOOo * I1IiiI % OoO0O00
   if not ( 'list' in OoOo00o [ 0 ] ) : return None
   iI1i111I1Ii = OoOo00o [ 0 ] [ 'list' ]
   if 25 - 25: O0oo0OO0 - iii1I1I
   for O0ooo0O0oo0 in iI1i111I1Ii :
    o0oOO000oO0oo = { }
    if 10 - 10: II111iiii / oO0o % OoooooooOO * I11i % I1ii11iIi11i
    if contenttype == 'vod' :
     II11Iiii = O0ooo0O0oo0 . get ( 'programtitle' )
     i11I = '%s회, %s' % ( O0ooo0O0oo0 . get ( 'episodenumber' ) , O0ooo0O0oo0 . get ( 'releasedate' ) )
     i1IIIiiII1 = O0ooo0O0oo0 . get ( 'contentid' )
     ooooo0O0000oo = O0ooo0O0oo0 . get ( 'programid' )
     if 48 - 48: Oo0ooO0oo0oO / O0oo0OO0 . iIii1I11I1II1 * OoOoOO00 * oO0o / i1IIi
     o0oOO000oO0oo [ 'title' ] = unicode ( II11Iiii )
     o0oOO000oO0oo [ 'mediatype' ] = 'episode'
     o0oOO000oO0oo [ 'mpaa' ] = O0ooo0O0oo0 . get ( 'targetage' )
     try :
      o0oOO000oO0oo [ 'studio' ] = O0ooo0O0oo0 . get ( 'channelname' )
     except :
      None
     try :
      if 'releasedate' in O0ooo0O0oo0 : o0oOO000oO0oo [ 'year' ] = int ( O0ooo0O0oo0 . get ( 'releasedate' ) [ : 4 ] )
      if 'releasedate' in O0ooo0O0oo0 : o0oOO000oO0oo [ 'aired' ] = O0ooo0O0oo0 . get ( 'releasedate' )
     except :
      None
      if 92 - 92: Oo0Ooo % Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
      if 10 - 10: iii1I1I + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / O0oo0OO0 / I1ii11iIi11i
    else :
     II11Iiii = O0ooo0O0oo0 . get ( 'title' )
     i11I = ''
     i1IIIiiII1 = ooooo0O0000oo = O0ooo0O0oo0 . get ( 'movieid' )
     if 42 - 42: I1IiiI
     o0oOO000oO0oo [ 'title' ] = unicode ( II11Iiii )
     o0oOO000oO0oo [ 'mediatype' ] = 'movie'
     o0oOO000oO0oo [ 'mpaa' ] = O0ooo0O0oo0 . get ( 'targetage' )
     try :
      if 'releasedate' in O0ooo0O0oo0 : o0oOO000oO0oo [ 'year' ] = int ( O0ooo0O0oo0 . get ( 'releasedate' ) [ : 4 ] )
      if 'releasedate' in O0ooo0O0oo0 : o0oOO000oO0oo [ 'aired' ] = O0ooo0O0oo0 . get ( 'releasedate' )
     except :
      None
      if 38 - 38: OOooOOo + II111iiii % Oo0ooO0oo0oO % OoOoOO00 - Ii1I / OoooooooOO
      if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
    if ( O0ooo0O0oo0 . get ( 'image' ) != '' ) : o00Oo0oooooo = 'https://%s' % O0ooo0O0oo0 . get ( 'image' )
    if 85 - 85: Ii1I % iii1I1I + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
    ooOoOo0 = { 'title' : unicode ( II11Iiii )
 , 'subtitle' : unicode ( i11I )
 , 'thumbnail' : o00Oo0oooooo
 , 'uicode' : contenttype
 , 'contentid' : i1IIIiiII1
 , 'programid' : ooooo0O0000oo
 , 'viewage' : O0ooo0O0oo0 . get ( 'targetage' )
 , 'info' : o0oOO000oO0oo
 }
    if 2 - 2: iii1I1I % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iii1I1I
    ii . append ( ooOoOo0 )
    if 27 - 27: OoO0O00 + Oo0ooO0oo0oO - i1IIi
    if 69 - 69: O00oOoOoO0o0O - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
   iiiIIi1II = int ( OoOo00o [ 0 ] [ 'pagecount' ] )
   if OoOo00o [ 0 ] [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 0 ] [ 'count' ] )
   else : o0O00oOoOO = self . MV_LIMIT
   if 79 - 79: O0 * i11iIiiIii - O00oOoOoO0o0O / O00oOoOoO0o0O
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 48 - 48: O0
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
   if 25 - 25: O00oOoOoO0o0O + Ii1I / Oo0ooO0oo0oO . o0oOOo0O0Ooo % O0 * OoO0O00
   if 84 - 84: Oo0ooO0oo0oO % Ii1I + i11iIiiIii
  try :
   if contenttype == 'movie' and addinfoyn == True :
    I111iI = [ ]
    oOOo0 = { }
    if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
    for O0OOOOo0O in ii : I111iI . append ( O0OOOOo0O . get ( 'contentid' ) )
    if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
    oOOo0 = self . GetMovieInfoList ( I111iI )
    if 19 - 19: OoO0O00 - Oo0Ooo . O0
    for Ooo in range ( len ( ii ) ) :
     ii [ Ooo ] [ 'info' ] = oOOo0 . get ( ii [ Ooo ] [ 'contentid' ] )
  except :
   None
   if 60 - 60: II111iiii + Oo0Ooo
   if 9 - 9: Oo0ooO0oo0oO * OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoO0O00
   if 49 - 49: II111iiii
  return ii , IIiIi1iI
  if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
  if 81 - 81: iii1I1I + O00oOoOoO0o0O
 def GetSearchList ( self , search_key , genre , page_int , exclusion21 = False , addinfoyn = False ) :
  o0oo0 = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  IIiIi1iI = False
  if 97 - 97: OoOoOO00 % I1ii11iIi11i
  try :
   I1Ii = self . GetDefaultParams ( )
   if 25 - 25: Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
   iii11I111 = '/cf/search/list.js'
   if 55 - 55: Oo0ooO0oo0oO - I11i + II111iiii + iii1I1I % Ii1I
   iiIiI = { 'type' : 'program' if genre == 'vod' else 'movie'
 , 'keyword' : search_key
 , 'offset' : str ( ( page_int - 1 ) * self . LIST_LIMIT )
 , 'limit' : self . LIST_LIMIT
   , 'orderby' : 'score'
 , 'isplayymovie' : 'y'
 }
   if 41 - 41: i1IIi - I11i - Ii1I
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( I1Ii )
   if 8 - 8: OoO0O00 + O0oo0OO0 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + Oo0ooO0oo0oO
   if not ( 'celllist' in OoOo00o [ 'cell_toplist' ] ) : return o0oo0 , IIiIi1iI
   iIIII = OoOo00o [ 'cell_toplist' ] [ 'celllist' ]
   if 45 - 45: I1ii11iIi11i % I1IiiI - i11iIiiIii
   if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * I1IiiI
   for O0ooo0O0oo0 in iIIII :
    o0oOO000oO0oo = { }
    if 46 - 46: OoOoOO00 + OoO0O00
    II11Iiii = O0ooo0O0oo0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if ( O0ooo0O0oo0 . get ( 'thumbnail' ) != '' ) : o00Oo0oooooo = 'https://%s' % O0ooo0O0oo0 . get ( 'thumbnail' )
    if 70 - 70: iii1I1I / iIii1I11I1II1
    for OOoo0O in O0ooo0O0oo0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , OOoo0O ) :
      if genre == 'vod' :
       i1IIIiiII1 = ''
       ooooo0O0000oo = re . sub ( r'uicode:' , '' , OOoo0O )
       o0oOO000oO0oo [ 'mediatype' ] = 'episode'
       if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
      else :
       i1IIIiiII1 = re . sub ( r'uicode:' , '' , OOoo0O )
       ooooo0O0000oo = ''
       if O0ooo0O0oo0 . get ( 'bottom_taglist' ) [ 0 ] == 'playy' :
        II11Iiii += ' [playy]'
       o0oOO000oO0oo [ 'mediatype' ] = 'movie'
       if 96 - 96: OoooooooOO + oO0o
       if 44 - 44: oO0o
      o0oOO000oO0oo [ 'title' ] = unicode ( O0ooo0O0oo0 [ 'title_list' ] [ 0 ] [ 'text' ] )
      o0oOO000oO0oo [ 'mpaa' ] = O0ooo0O0oo0 . get ( 'age' )
      if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
      ooOoOo0 = { 'title' : unicode ( II11Iiii )
 , 'thumbnail' : o00Oo0oooooo
 , 'uicode' : genre
 , 'contentid' : i1IIIiiII1
 , 'programid' : ooooo0O0000oo
 , 'viewage' : O0ooo0O0oo0 . get ( 'age' )
 , 'info' : o0oOO000oO0oo
 }
      if 88 - 88: OoOoOO00 / II111iiii
    if exclusion21 == False or O0ooo0O0oo0 . get ( 'age' ) != '21' :
     o0oo0 . append ( ooOoOo0 )
     if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iii1I1I + oO0o
     if 82 - 82: oO0o / iIii1I11I1II1 . I1IiiI . OOooOOo / o0oOOo0O0Ooo
   iiiIIi1II = int ( OoOo00o [ 'cell_toplist' ] [ 'pagecount' ] )
   if OoOo00o [ 'cell_toplist' ] [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 'cell_toplist' ] [ 'count' ] )
   else : o0O00oOoOO = self . LIST_LIMIT
   if 42 - 42: Oo0Ooo
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 46 - 46: Oo0Ooo
   if 1 - 1: iii1I1I
   if 97 - 97: OOooOOo + iii1I1I + O0 + i11iIiiIii
  try :
   if genre == 'movie' and addinfoyn == True :
    I111iI = [ ]
    oOOo0 = { }
    if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
    for O0OOOOo0O in o0oo0 : I111iI . append ( O0OOOOo0O . get ( 'contentid' ) )
    if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iii1I1I % iii1I1I + i11iIiiIii
    oOOo0 = self . GetMovieInfoList ( I111iI )
    if 72 - 72: iIii1I11I1II1 * Ii1I % Oo0ooO0oo0oO / OoO0O00
    for Ooo in range ( len ( o0oo0 ) ) :
     o0oo0 [ Ooo ] [ 'info' ] = oOOo0 . get ( o0oo0 [ Ooo ] [ 'contentid' ] )
  except :
   None
   if 35 - 35: Oo0ooO0oo0oO + i1IIi % I1ii11iIi11i % I11i + oO0o
   if 17 - 17: i1IIi
   if 21 - 21: Oo0Ooo
  return o0oo0 , IIiIi1iI
  if 29 - 29: I11i / II111iiii / Oo0ooO0oo0oO * OOooOOo
  if 10 - 10: O0oo0OO0 % O00oOoOoO0o0O * O00oOoOoO0o0O . I11i / Ii1I % OOooOOo
 def GetGenreGroup ( self , maintype , subtype , orderby , ordernm , exclusion21 = False ) :
  IIII1 = [ ]
  if 10 - 10: O0oo0OO0 / Oo0ooO0oo0oO + i11iIiiIii / Ii1I
  try :
   I1Ii = self . GetDefaultParams ( )
   if 74 - 74: OOooOOo + O0 + i1IIi - i1IIi + II111iiii
   iii11I111 = '/cf/filters'
   if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
   iiIiI = { 'type' : maintype }
   if 5 - 5: Ii1I
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( I1Ii )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 46 - 46: O00oOoOoO0o0O
   if not ( maintype in OoOo00o ) : return None
   ii1iIi1iIiI1i = OoOo00o [ maintype ]
   if 40 - 40: i1IIi % OOooOOo
   if subtype == '-' :
    if 71 - 71: OoOoOO00
    for O0ooo0O0oo0 in ii1iIi1iIiI1i :
     ii111IiiI1 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( O0ooo0O0oo0 . get ( 'url' ) ) . query ) )
     if 11 - 11: iIii1I11I1II1 * Ii1I
     ooOoOo0 = { 'title' : O0ooo0O0oo0 . get ( 'text' )
 , 'genre' : O0ooo0O0oo0 . get ( 'id' )
 , 'subgenre' : '-'
 , 'adult' : O0ooo0O0oo0 . get ( 'adult' )
 , 'broadcastid' : ii111IiiI1 . get ( 'broadcastid' )
 , 'contenttype' : ii111IiiI1 . get ( 'contenttype' )
 , 'uiparent' : ii111IiiI1 . get ( 'uiparent' )
 , 'uirank' : ii111IiiI1 . get ( 'uirank' )
 , 'uitype' : ii111IiiI1 . get ( 'uitype' )
 , 'orderby' : orderby
 , 'ordernm' : ordernm
 }
     if exclusion21 == False or ooOoOo0 . get ( 'adult' ) == 'n' :
      IIII1 . append ( ooOoOo0 )
      if 76 - 76: Oo0ooO0oo0oO
   else :
    for O0ooo0O0oo0 in ii1iIi1iIiI1i :
     if O0ooo0O0oo0 . get ( 'id' ) == subtype :
      for II in O0ooo0O0oo0 [ 'sublist' ] :
       ii111IiiI1 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( II . get ( 'url' ) ) . query ) )
       if 45 - 45: OoooooooOO - OOooOOo + O0 * Ii1I . I1ii11iIi11i
       ooOoOo0 = { 'title' : II . get ( 'text' )
 , 'genre' : subtype
 , 'subgenre' : II . get ( 'id' )
 , 'adult' : II . get ( 'adult' )
 , 'broadcastid' : ii111IiiI1 . get ( 'broadcastid' )
 , 'contenttype' : ii111IiiI1 . get ( 'contenttype' )
 , 'uiparent' : ii111IiiI1 . get ( 'uiparent' )
 , 'uirank' : ii111IiiI1 . get ( 'uirank' )
 , 'uitype' : ii111IiiI1 . get ( 'uitype' )
 , 'orderby' : orderby
 , 'ordernm' : ordernm
 }
       IIII1 . append ( ooOoOo0 )
      break
      if 39 - 39: iIii1I11I1II1 / O0 / oO0o - Ii1I - iii1I1I % OOooOOo
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 31 - 31: I11i - O0 / Oo0ooO0oo0oO * OoOoOO00
  return IIII1
  if 12 - 12: o0oOOo0O0Ooo - Oo0ooO0oo0oO * O0oo0OO0
  if 14 - 14: Oo0Ooo - Ii1I % Ii1I * O0 . i11iIiiIii / O0
 def GetGenreGroup_sub ( self , in_params ) :
  IIII1 = [ ]
  if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
  try :
   I1Ii = self . GetDefaultParams ( )
   if 28 - 28: i1IIi - iii1I1I
   iii11I111 = '/cf/vod/newcontents'
   if 54 - 54: iii1I1I - O0 % OOooOOo
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
   if 73 - 73: O0 . OoOoOO00 + I1IiiI - I11i % I11i . I11i
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( I1Ii )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 17 - 17: Ii1I - OoooooooOO % Ii1I . O00oOoOoO0o0O / i11iIiiIii % iii1I1I
   if not ( 'filter_item_list' in OoOo00o [ 'filter' ] [ 'filterlist' ] [ 1 ] ) : return None
   ii1iIi1iIiI1i = OoOo00o [ 'filter' ] [ 'filterlist' ] [ 1 ] [ 'filter_item_list' ]
   if 28 - 28: I11i
   for O0ooo0O0oo0 in ii1iIi1iIiI1i :
    ooOoOo0 = { 'broadcastid' : in_params . get ( 'broadcastid' )
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
    IIII1 . append ( ooOoOo0 )
    if 58 - 58: OoOoOO00
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 37 - 37: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i
  return IIII1
  if 73 - 73: i11iIiiIii - O00oOoOoO0o0O
  if 25 - 25: OoooooooOO + O00oOoOoO0o0O * I1ii11iIi11i
 def GetGenreList ( self , genre , in_params , page_int , addinfoyn = False ) :
  IIII1 = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  IIiIi1iI = False
  if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + O0oo0OO0
  try :
   I1Ii = self . GetDefaultParams ( )
   if 18 - 18: Oo0ooO0oo0oO * OoOoOO00 . iii1I1I / I1ii11iIi11i / i11iIiiIii
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
   if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
   if genre == 'vodgenre' :
    iii11I111 = '/cf/vod/newcontents'
    if 91 - 91: i11iIiiIii / i1IIi + iii1I1I + Oo0ooO0oo0oO * i11iIiiIii
    if in_params . get ( 'subgenre' ) != '-' :
     iiIiI [ 'subgenre' ] = in_params . get ( 'subgenre' )
   else :
    iii11I111 = '/cf/movie/contents'
    if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * O0oo0OO0 . O00oOoOoO0o0O
    iiIiI [ 'price' ] = 'all'
    if 52 - 52: Oo0ooO0oo0oO + O0 . iii1I1I . I1ii11iIi11i . OoO0O00
    if 97 - 97: I1IiiI / iii1I1I
    iiIiI [ 'sptheme' ] = 'svod'
    if 71 - 71: II111iiii / i1IIi . I1ii11iIi11i % OoooooooOO . OoOoOO00
    if 41 - 41: i1IIi * II111iiii / OoooooooOO . OOooOOo
   iiIiI [ 'limit' ] = self . LIST_LIMIT
   iiIiI [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
   iiIiI [ 'page' ] = str ( page_int )
   if 83 - 83: iii1I1I . O0 / Oo0Ooo / OOooOOo - II111iiii
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( I1Ii )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 100 - 100: OoO0O00
   if not ( 'celllist' in OoOo00o [ 'cell_toplist' ] ) : return None
   ii1iIi1iIiI1i = OoOo00o [ 'cell_toplist' ] [ 'celllist' ]
   if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iii1I1I . iIii1I11I1II1 * iii1I1I
   for O0ooo0O0oo0 in ii1iIi1iIiI1i :
    o0oOO000oO0oo = { }
    II11Iiii = o00Oo0oooooo = ''
    if 38 - 38: I1ii11iIi11i - iii1I1I / O0 . O0oo0OO0
    II11Iiii = O0ooo0O0oo0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if 45 - 45: O0oo0OO0
    if ( O0ooo0O0oo0 . get ( 'thumbnail' ) != '' ) : o00Oo0oooooo = 'https://%s' % O0ooo0O0oo0 . get ( 'thumbnail' )
    if 83 - 83: OoOoOO00 . OoooooooOO
    for OOoo0O in O0ooo0O0oo0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , OOoo0O ) :
      if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / O00oOoOoO0o0O / i11iIiiIii
      o0oOO000oO0oo [ 'title' ] = unicode ( II11Iiii )
      o0oOO000oO0oo [ 'mpaa' ] = O0ooo0O0oo0 . get ( 'age' )
      if genre == 'moviegenre_svod' :
       o0oOO000oO0oo [ 'mediatype' ] = 'movie'
      else :
       o0oOO000oO0oo [ 'mediatype' ] = 'episode'
       if 62 - 62: OoO0O00 / I1ii11iIi11i
       if 7 - 7: OoooooooOO . O00oOoOoO0o0O
      ooOoOo0 = { 'title' : unicode ( II11Iiii )
 , 'uicode' : re . sub ( r'uicode:' , '' , OOoo0O )
 , 'thumbnail' : o00Oo0oooooo
 , 'viewage' : O0ooo0O0oo0 . get ( 'age' )
 , 'info' : o0oOO000oO0oo
 }
      if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
    IIII1 . append ( ooOoOo0 )
    if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
    if 100 - 100: Oo0ooO0oo0oO % iIii1I11I1II1 * II111iiii - iii1I1I
   iiiIIi1II = int ( OoOo00o [ 'cell_toplist' ] [ 'pagecount' ] )
   if OoOo00o [ 'cell_toplist' ] [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 'cell_toplist' ] [ 'count' ] )
   else : o0O00oOoOO = self . LIST_LIMIT
   if 92 - 92: Oo0ooO0oo0oO
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 22 - 22: Oo0Ooo % iii1I1I * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 95 - 95: OoooooooOO - O00oOoOoO0o0O * I1IiiI + OoOoOO00
   if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
   if 92 - 92: I11i . O0oo0OO0
  try :
   if genre == 'moviegenre_svod' and addinfoyn == True :
    I111iI = [ ]
    oOOo0 = { }
    if 85 - 85: I1ii11iIi11i . O0oo0OO0
    for O0OOOOo0O in IIII1 : I111iI . append ( O0OOOOo0O . get ( 'uicode' ) )
    if 78 - 78: Oo0ooO0oo0oO * O0oo0OO0 + iIii1I11I1II1 + iIii1I11I1II1 / O0oo0OO0 . Ii1I
    oOOo0 = self . GetMovieInfoList ( I111iI )
    if 97 - 97: Oo0ooO0oo0oO / O0oo0OO0 % i1IIi % I1ii11iIi11i
    for Ooo in range ( len ( IIII1 ) ) :
     IIII1 [ Ooo ] [ 'info' ] = oOOo0 . get ( IIII1 [ Ooo ] [ 'uicode' ] )
  except :
   None
   if 18 - 18: iIii1I11I1II1 % I11i
   if 95 - 95: Oo0ooO0oo0oO + i11iIiiIii * O0oo0OO0 - i1IIi * O0oo0OO0 - iIii1I11I1II1
   if 75 - 75: OoooooooOO * O00oOoOoO0o0O
  return IIII1 , IIiIi1iI
  if 9 - 9: O00oOoOoO0o0O - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  if 39 - 39: O00oOoOoO0o0O * Oo0Ooo + iIii1I11I1II1 - O00oOoOoO0o0O + OOooOOo
 def GetEPGList ( self , genre ) :
  o0 = { }
  if 30 - 30: O0 * OoooooooOO
  try :
   import datetime
   I1iIIIi1 = datetime . datetime . now ( )
   if genre == 'all' :
    Iii = I1iIIIi1 + datetime . timedelta ( hours = 2 )
   else :
    Iii = I1iIIIi1 + datetime . timedelta ( hours = 3 )
    if 19 - 19: I11i % II111iiii / i11iIiiIii / iii1I1I - OoooooooOO
   I1Ii = self . GetDefaultParams ( )
   if 37 - 37: OOooOOo / OoooooooOO - i11iIiiIii
   iiIiI = { 'limit' : '100'
 , 'offset' : '0'
 , 'genre' : genre
 , 'startdatetime' : I1iIIIi1 . strftime ( '%Y-%m-%d %H:%M' )
 , 'enddatetime' : Iii . strftime ( '%Y-%m-%d %H:%M' )
 }
   iii11I111 = '/live/epgs'
   if 18 - 18: iii1I1I . I1IiiI
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( iiIiI ) + '&' + urllib . urlencode ( I1Ii )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 40 - 40: O0 - OoooooooOO - O00oOoOoO0o0O
   iIiii = OoOo00o [ 'list' ]
   if 76 - 76: I1IiiI . Oo0ooO0oo0oO - I1ii11iIi11i - iii1I1I * OoO0O00
   if 54 - 54: O00oOoOoO0o0O + O0 + I11i * O0oo0OO0 - OOooOOo % oO0o
   for O0ooo0O0oo0 in iIiii :
    I111 = ''
    if 13 - 13: OoO0O00 * oO0o * iii1I1I
    for IiIIiiI11III in O0ooo0O0oo0 [ 'list' ] :
     if I111 : I111 += '\n'
     I111 += IiIIiiI11III [ 'title' ] + '\n'
     I111 += ' [%s ~ %s]' % ( IiIIiiI11III [ 'starttime' ] [ - 5 : ] , IiIIiiI11III [ 'endtime' ] [ - 5 : ] ) + '\n'
     if 42 - 42: I1ii11iIi11i
     if 76 - 76: I1ii11iIi11i * II111iiii . I1IiiI - Oo0Ooo + oO0o + i11iIiiIii
     if 28 - 28: oO0o
    o0 [ O0ooo0O0oo0 [ 'channelid' ] ] = unicode ( I111 )
    if 70 - 70: O00oOoOoO0o0O
    if 34 - 34: O0oo0OO0 % O00oOoOoO0o0O
    if 3 - 3: II111iiii / OOooOOo + O00oOoOoO0o0O . Oo0ooO0oo0oO . OoO0O00
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 83 - 83: oO0o + OoooooooOO
  return o0
  if 22 - 22: Ii1I % iii1I1I * OoooooooOO - o0oOOo0O0Ooo / iIii1I11I1II1
  if 86 - 86: OoooooooOO . iii1I1I % OoOoOO00 / I11i * iii1I1I / o0oOOo0O0Ooo
 def GetMovieInfoList ( self , movie_list ) :
  oO = { }
  if 60 - 60: I1ii11iIi11i * I1IiiI
  try :
   I1Ii = self . GetDefaultParams ( )
   iii11I111 = self . API_DOMAIN + '/movie/contents/'
   if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . O00oOoOoO0o0O * OOooOOo - II111iiii
   for O0OOOOo0O in movie_list :
    if 41 - 41: Ii1I
    oo0Ooo0 = iii11I111 + O0OOOOo0O
    II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
    OoOo00o = json . loads ( II1Iiii1111i )
    if 77 - 77: O0oo0OO0
    o0oOO000oO0oo = { }
    o0oOO000oO0oo [ 'mediatype' ] = 'movie'
    if 65 - 65: II111iiii . I1IiiI % oO0o * OoO0O00
    iI11I = [ ]
    for I1IIIiii1 in OoOo00o [ 'actors' ] [ 'list' ] : iI11I . append ( I1IIIiii1 . get ( 'text' ) )
    if iI11I [ 0 ] != '' : o0oOO000oO0oo [ 'cast' ] = iI11I
    if 65 - 65: I11i / II111iiii * Ii1I . iii1I1I * oO0o % OOooOOo
    O0oOOo0Oo = [ ]
    for o000O000 in OoOo00o [ 'directors' ] [ 'list' ] : O0oOOo0Oo . append ( o000O000 . get ( 'text' ) )
    if O0oOOo0Oo [ 0 ] != '' : o0oOO000oO0oo [ 'director' ] = O0oOOo0Oo
    if 19 - 19: iIii1I11I1II1
    IIII1 = [ ]
    for Ii1IiI1i1ii in OoOo00o [ 'genre' ] [ 'list' ] : IIII1 . append ( Ii1IiI1i1ii . get ( 'text' ) )
    if IIII1 [ 0 ] != '' : o0oOO000oO0oo [ 'genre' ] = IIII1
    if 30 - 30: O00oOoOoO0o0O + O0oo0OO0 - O00oOoOoO0o0O . O00oOoOoO0o0O - II111iiii + O0
    if OoOo00o . get ( 'releasedate' ) != '' :
     o0oOO000oO0oo [ 'year' ] = OoOo00o [ 'releasedate' ] [ : 4 ]
     o0oOO000oO0oo [ 'aired' ] = OoOo00o [ 'releasedate' ]
     if 86 - 86: i1IIi
    o0oOO000oO0oo [ 'country' ] = OoOo00o [ 'country' ]
    o0oOO000oO0oo [ 'duration' ] = OoOo00o [ 'playtime' ]
    o0oOO000oO0oo [ 'title' ] = OoOo00o [ 'title' ]
    o0oOO000oO0oo [ 'mpaa' ] = OoOo00o [ 'targetage' ]
    o0oOO000oO0oo [ 'plot' ] = OoOo00o [ 'synopsis' ]
    if 41 - 41: OoOoOO00 * I11i / OoOoOO00 % oO0o
    oO [ O0OOOOo0O ] = o0oOO000oO0oo
    if 18 - 18: II111iiii . OoooooooOO % OoOoOO00 % Ii1I
  except Exception as OO00Oo :
   return { }
   if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
  return oO
  if 2 - 2: OoooooooOO % OOooOOo
  if 63 - 63: I1IiiI % iIii1I11I1II1
 def GetStreamingURL ( self , contentid , contenttype , quality_int ) :
  I1ii = O00O0O = IIi1i1IiIIi1i = oOOo0OOOOo0Oo = ''
  OOo0o = [ ]
  if 72 - 72: iIii1I11I1II1
  if 11 - 11: II111iiii / o0oOOo0O0Ooo
  try :
   if contenttype == 'channel' :
    iii11I111 = '/live/channels/' + contentid
    IiIi1 = 'live'
   elif contenttype == 'movie' :
    iii11I111 = '/cf/movie/contents/' + contentid
    IiIi1 = 'movie'
   else :
    iii11I111 = '/cf/vod/contents/' + contentid
    IiIi1 = 'vod'
    if 34 - 34: OOooOOo
   I1Ii = self . GetDefaultParams ( )
   oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , I1Ii )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 91 - 91: iIii1I11I1II1 % o0oOOo0O0Ooo . iIii1I11I1II1 % i1IIi / II111iiii * OoOoOO00
   iioo0o0OoOOO = OoOo00o [ 'qualities' ] [ 'list' ]
   if iioo0o0OoOOO == None : return ( I1ii , O00O0O , IIi1i1IiIIi1i , oOOo0OOOOo0Oo )
   if 88 - 88: iii1I1I
   iiI11I1i1i1iI = 'hls'
   if 'drms' in OoOo00o :
    if OoOo00o [ 'drms' ] :
     iiI11I1i1i1iI = 'dash'
     if 60 - 60: OoooooooOO % Oo0Ooo + OOooOOo . Oo0ooO0oo0oO * iIii1I11I1II1
   print ( iiI11I1i1i1iI )
   if 93 - 93: OoO0O00
   if 'type' in OoOo00o :
    if OoOo00o [ 'type' ] == 'onair' :
     IiIi1 = 'onairvod'
     if 5 - 5: I11i / OOooOOo
     if 77 - 77: Oo0ooO0oo0oO - I1IiiI % I11i - O0
   for o0O0O0 in iioo0o0OoOOO :
    OOo0o . append ( int ( o0O0O0 . get ( 'id' ) . rstrip ( 'p' ) ) )
    if 6 - 6: iii1I1I . O00oOoOoO0o0O * OoOoOO00 . i1IIi
  except Exception as OO00Oo :
   return ( I1ii , O00O0O , IIi1i1IiIIi1i , oOOo0OOOOo0Oo )
   if 98 - 98: i1IIi
   if 65 - 65: OoOoOO00 / OoO0O00 % O00oOoOoO0o0O
   if 45 - 45: OoOoOO00
  try :
   oOooOO = self . CheckQuality ( quality_int , OOo0o )
   iii11I111 = '/streaming'
   iiIiI = { 'contentid' : contentid
 , 'contenttype' : IiIi1
 , 'action' : iiI11I1i1i1iI
 , 'quality' : str ( oOooOO ) + 'p'
 , 'deviceModelId' : 'Windows 10'
 , 'guid' : self . GetGUID ( guidType = 2 )
 , 'lastplayid' : self . guid
 , 'authtype' : 'cookie'
 , 'isabr' : 'y'
 , 'ishevc' : 'n'
 }
   if 31 - 31: OOooOOo / Oo0Ooo * i1IIi . OoOoOO00
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( I1Ii ) + '&' + urllib . urlencode ( iiIiI )
   if 57 - 57: OOooOOo + iIii1I11I1II1 % i1IIi % I1IiiI
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 83 - 83: o0oOOo0O0Ooo / i11iIiiIii % iIii1I11I1II1 . I11i % oO0o . OoooooooOO
   I1ii = OoOo00o [ 'playurl' ]
   if I1ii == None : return None
   O00O0O = OoOo00o [ 'awscookie' ]
   IIi1i1IiIIi1i = OoOo00o [ 'drm' ]
   if 'previewmsg' in OoOo00o [ 'preview' ] : oOOo0OOOOo0Oo = OoOo00o [ 'preview' ] [ 'previewmsg' ]
   if 94 - 94: Ii1I + iIii1I11I1II1 % OoO0O00
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 93 - 93: Ii1I - OOooOOo + iIii1I11I1II1 * o0oOOo0O0Ooo + O0oo0OO0 . iii1I1I
  I1ii = I1ii . replace ( 'pooq.co.kr' , 'wavve.com' )
  if 49 - 49: OoooooooOO * I11i - Oo0Ooo . oO0o
  return ( I1ii , O00O0O , IIi1i1IiIIi1i , oOOo0OOOOo0Oo )
  if 89 - 89: Oo0ooO0oo0oO + Ii1I * Oo0ooO0oo0oO / Oo0ooO0oo0oO
  if 46 - 46: OoO0O00
  if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
  if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
  if 58 - 58: I11i + II111iiii * iii1I1I * i11iIiiIii - iIii1I11I1II1
  if 68 - 68: OoooooooOO % II111iiii
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
