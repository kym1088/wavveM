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
   if 42 - 42: i11iIiiIii
   if 33 - 33: iii1I1I - O0 * i1IIi * o0oOOo0O0Ooo - Oo0Ooo
   if 32 - 32: OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
   iii11I111 = urlparse . urlsplit ( II1I ) . path
   o00oooO0Oo = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( II1I ) . query ) )
   if 78 - 78: Ii1I % O0oo0OO0 + I1ii11iIi11i
   o00oooO0Oo [ 'came' ] = came_str
   o00oooO0Oo [ 'limit' ] = str ( self . LIST_LIMIT )
   if 'contenttype' in o00oooO0Oo : iIIi1i1 = o00oooO0Oo [ 'contenttype' ]
   if 64 - 64: oO0o * O0 . I1IiiI + II111iiii
   if page_int != 1 :
    o00oooO0Oo [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
    o00oooO0Oo [ 'page' ] = str ( page_int )
    if 6 - 6: OoOoOO00 / iii1I1I . O00oOoOoO0o0O . O00oOoOoO0o0O
   oo0Ooo0 = self . HTTPTAG + iii11I111 + '?' + urllib . urlencode ( o00oooO0Oo ) + '&' + urllib . urlencode ( i1iIIi1 )
   if 62 - 62: I1ii11iIi11i + O00oOoOoO0o0O % iii1I1I + OOooOOo
   if 33 - 33: O0 . O00oOoOoO0o0O . I1IiiI
   if 72 - 72: i1IIi / OoO0O00 + OoooooooOO - Oo0Ooo
   if 29 - 29: I1ii11iIi11i + oO0o % O0
   if 10 - 10: I11i / O0oo0OO0 - I1IiiI * iIii1I11I1II1 - I1IiiI
   if 97 - 97: I1ii11iIi11i + I1IiiI * Ii1I + OOooOOo % iii1I1I
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + O0oo0OO0 / OoOoOO00
   if 23 - 23: O0
   if not ( 'celllist' in OoOo00o [ 'cell_toplist' ] ) : return o0OO0oOO0O0 , IIiIi1iI
   o00oO0oOo00 = OoOo00o [ 'cell_toplist' ] [ 'celllist' ]
   if 81 - 81: OoO0O00
   if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iii1I1I / OoOoOO00
   if 84 - 84: Oo0ooO0oo0oO * II111iiii + Oo0Ooo
   if ( iIIi1i1 == 'channel' ) :
    if ( 'genre' in o00oooO0Oo ) :
     O0ooO0Oo00o = o00oooO0Oo [ 'genre' ]
    else :
     O0ooO0Oo00o = 'all'
     if 77 - 77: iIii1I11I1II1 * OoO0O00
    i1IiiiI1iI = self . GetEPGList ( O0ooO0Oo00o )
    if 95 - 95: I1IiiI + i11iIiiIii
    if 6 - 6: Oo0ooO0oo0oO / i11iIiiIii + iii1I1I * oO0o
    if 80 - 80: II111iiii
   for O0ooo0O0oo0 in o00oO0oOo00 :
    O0O = i1I1I = iiI1I = ''
    if 12 - 12: i11iIiiIii - i1IIi - OoO0O00 . i1IIi - OOooOOo + O0
    O0O = O0ooo0O0oo0 . get ( 'title_list' ) [ 0 ] . get ( 'text' )
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
     if iIIi1i1 == 'x' : iIIi1i1 = 'movie'
    else :
     i1IIIiiII1 = '-'
     OOOOoOoo0O0O0 = '-'
     if 55 - 55: OOooOOo . I1IiiI
    Oo0ooOo0o = { 'title' : unicode ( O0O )
 , 'subtitle' : unicode ( i1I1I )
 , 'thumbnail' : iiI1I
 , 'uicode' : iIIi1i1
 , 'contentid' : i1IIIiiII1
 , 'contentidType' : OOOOoOoo0O0O0
 , 'viewage' : O0ooo0O0oo0 . get ( 'age' )
 , 'channelepg' : OOOo00oo0oO
 }
    o0OO0oOO0O0 . append ( Oo0ooOo0o )
    if 61 - 61: Oo0Ooo % O00oOoOoO0o0O . Oo0Ooo
   iiiIIi1II = int ( OoOo00o [ 'cell_toplist' ] [ 'pagecount' ] )
   if OoOo00o [ 'cell_toplist' ] [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 'cell_toplist' ] [ 'count' ] )
   else : o0O00oOoOO = self . LIST_LIMIT
   if 100 - 100: O0oo0OO0 * O0
   if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 79 - 79: O0
   if 78 - 78: I1ii11iIi11i + OOooOOo - O0oo0OO0
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
  return ( o0OO0oOO0O0 , IIiIi1iI )
  if 57 - 57: OoO0O00 / Oo0ooO0oo0oO
  if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
 def GetEpisodeList ( self , contentid , contenttype , contentidType , page_int , orderby = 'desc' ) :
  I111I1Iiii1i = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  IIiIi1iI = False
  if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  if orderby == 'desc' :
   orderby = 'new'
  else :
   orderby = 'old'
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
  try :
   i1iIIi1 = self . GetDefaultParams ( )
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
   if 33 - 33: O0oo0OO0 + iii1I1I * oO0o / iIii1I11I1II1 - I1IiiI
   if contentidType == 'contentid' :
    iii11I111 = '/cf/vod/contents/' + contentid
    if 54 - 54: O0oo0OO0 / OOooOOo . oO0o % iii1I1I
    oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , i1iIIi1 )
    II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
    OoOo00o = json . loads ( II1Iiii1111i )
    if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
    if not ( 'programid' in OoOo00o ) : return None
    oO00oooOOoOo0 = OoOo00o [ 'programid' ]
    if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
   else :
    oO00oooOOoOo0 = contentid
    if 62 - 62: OoooooooOO * I1IiiI
    if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
    if 50 - 50: O0oo0OO0 . o0oOOo0O0Ooo
   iii11I111 = '/vod/programs-contents/' + oO00oooOOoOo0
   if 97 - 97: O0 + OoOoOO00
   o00oooO0Oo = { 'limit' : self . EP_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . EP_LIMIT )
 , 'orderby' : orderby
   }
   if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( o00oooO0Oo ) + '&' + urllib . urlencode ( i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
   if not ( 'list' in OoOo00o ) : return None
   o0o0O0O00oOOo = OoOo00o [ 'list' ]
   if 14 - 14: OoOoOO00 + oO0o
   if 52 - 52: OoooooooOO - Oo0ooO0oo0oO
   for O0ooo0O0oo0 in o0o0O0O00oOOo :
    o0O0o0 = O0ooo0O0oo0 . get ( 'programtitle' )
    II111iI111I1I = '%s회, %s(%s)' % ( O0ooo0O0oo0 . get ( 'episodenumber' ) , O0ooo0O0oo0 . get ( 'releasedate' ) , O0ooo0O0oo0 . get ( 'releaseweekday' ) )
    if ( O0ooo0O0oo0 . get ( 'image' ) != '' ) : I1i1i1iii = 'https://%s' % O0ooo0O0oo0 . get ( 'image' )
    if 16 - 16: Ii1I + O00oOoOoO0o0O * O0 % i1IIi . I1IiiI
    Oo0OO = unicode ( O0ooo0O0oo0 . get ( 'synopsis' ) )
    Oo0OO = re . sub ( u'(\<[a-zA-Z]{1,2}\>)|(\<\/[a-zA-Z]{1,2}\>)' , '' , Oo0OO )
    if 78 - 78: OOooOOo - OoooooooOO - I1ii11iIi11i / Oo0ooO0oo0oO / II111iiii
    iiI11ii1I1 = { 'title' : unicode ( o0O0o0 )
 , 'subtitle' : unicode ( II111iI111I1I )
 , 'thumbnail' : I1i1i1iii
 , 'uicode' : contenttype
 , 'contentid' : O0ooo0O0oo0 . get ( 'contentid' )
 , 'programid' : O0ooo0O0oo0 . get ( 'programid' )
 , 'synopsis' : Oo0OO
 , 'viewage' : O0ooo0O0oo0 . get ( 'targetage' )
 }
    I111I1Iiii1i . append ( iiI11ii1I1 )
    if 82 - 82: II111iiii % I11i / OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / O0oo0OO0
   iiiIIi1II = int ( OoOo00o [ 'pagecount' ] )
   if OoOo00o [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 'count' ] )
   else : o0O00oOoOO = self . EP_LIMIT
   if 70 - 70: oO0o
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 59 - 59: o0oOOo0O0Ooo % oO0o
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 6 - 6: iIii1I11I1II1 % i11iIiiIii % I1ii11iIi11i
  return ( I111I1Iiii1i , IIiIi1iI )
  if 93 - 93: O00oOoOoO0o0O * OoooooooOO + Oo0ooO0oo0oO
  if 33 - 33: O0 * o0oOOo0O0Ooo - O0oo0OO0 % O0oo0OO0
 def GetMyviewList ( self , contenttype , page_int ) :
  I11I = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  IIiIi1iI = False
  if 50 - 50: O0oo0OO0 * i11iIiiIii * iIii1I11I1II1 - II111iiii * o0oOOo0O0Ooo * OoOoOO00
  try :
   i1iIIi1 = self . GetDefaultParams ( )
   if 94 - 94: OoooooooOO + OoooooooOO . II111iiii + I11i / I1ii11iIi11i % Ii1I
   iii11I111 = '/myview/contents'
   if 18 - 18: iii1I1I * O0 - OoooooooOO % I1IiiI . II111iiii / i1IIi
   o00oooO0Oo = { 'contenttype' : contenttype
 , 'limit' : self . MV_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . MV_LIMIT )
 , 'orderby' : 'new'
 }
   if 76 - 76: I11i / OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + O00oOoOoO0o0O
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( o00oooO0Oo ) + '&' + urllib . urlencode ( i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 71 - 71: O0oo0OO0 . II111iiii
   if not ( 'list' in OoOo00o [ 0 ] ) : return None
   oo0 = OoOo00o [ 0 ] [ 'list' ]
   if 61 - 61: OoOoOO00 - OOooOOo - i1IIi
   for O0ooo0O0oo0 in oo0 :
    if 25 - 25: O0 * I11i + I1ii11iIi11i . o0oOOo0O0Ooo . o0oOOo0O0Ooo
    if contenttype == 'vod' :
     o0O0o0 = O0ooo0O0oo0 . get ( 'programtitle' )
     II111iI111I1I = '%s회, %s' % ( O0ooo0O0oo0 . get ( 'episodenumber' ) , O0ooo0O0oo0 . get ( 'releasedate' ) )
     i1IIIiiII1 = O0ooo0O0oo0 . get ( 'contentid' )
     oO00oooOOoOo0 = O0ooo0O0oo0 . get ( 'programid' )
     if 58 - 58: I1IiiI
    else :
     o0O0o0 = O0ooo0O0oo0 . get ( 'title' )
     II111iI111I1I = '%s' % ( O0ooo0O0oo0 . get ( 'releasedate' ) )
     i1IIIiiII1 = oO00oooOOoOo0 = O0ooo0O0oo0 . get ( 'movieid' )
     if 53 - 53: i1IIi
    if ( O0ooo0O0oo0 . get ( 'image' ) != '' ) : I1i1i1iii = 'https://%s' % O0ooo0O0oo0 . get ( 'image' )
    if 59 - 59: o0oOOo0O0Ooo
    oOoO00O0 = { 'title' : unicode ( o0O0o0 )
 , 'subtitle' : unicode ( II111iI111I1I )
 , 'thumbnail' : I1i1i1iii
 , 'uicode' : contenttype
 , 'contentid' : i1IIIiiII1
 , 'programid' : oO00oooOOoOo0
 , 'viewage' : O0ooo0O0oo0 . get ( 'targetage' )
 }
    if 75 - 75: I1IiiI . Oo0ooO0oo0oO . O0 * O0oo0OO0
    I11I . append ( oOoO00O0 )
    if 4 - 4: Ii1I % oO0o * OoO0O00
    if 100 - 100: O0oo0OO0 * OOooOOo + OOooOOo
   iiiIIi1II = int ( OoOo00o [ 0 ] [ 'pagecount' ] )
   if OoOo00o [ 0 ] [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 0 ] [ 'count' ] )
   else : o0O00oOoOO = self . MV_LIMIT
   if 54 - 54: OoooooooOO + o0oOOo0O0Ooo - i1IIi % i11iIiiIii
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 3 - 3: o0oOOo0O0Ooo % o0oOOo0O0Ooo
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 83 - 83: II111iiii + O0oo0OO0
  return I11I , IIiIi1iI
  if 73 - 73: iii1I1I
  if 42 - 42: i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . i11iIiiIii % I11i
 def GetSearchList ( self , search_key , genre , page_int , exclusion21 = False ) :
  i1iI = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  IIiIi1iI = False
  if 29 - 29: I1IiiI % OOooOOo - I1IiiI / OOooOOo . i1IIi
  try :
   i1iIIi1 = self . GetDefaultParams ( )
   if 31 - 31: O0oo0OO0
   iii11I111 = '/cf/search/list.js'
   if 88 - 88: OoO0O00 - Oo0ooO0oo0oO + OOooOOo * I1IiiI % iIii1I11I1II1 + Oo0Ooo
   o00oooO0Oo = { 'type' : 'program' if genre == 'vod' else 'movie'
 , 'keyword' : search_key
 , 'offset' : str ( ( page_int - 1 ) * self . LIST_LIMIT )
 , 'limit' : self . LIST_LIMIT
   , 'orderby' : 'score'
 , 'isplayymovie' : 'y'
 }
   if 76 - 76: I1IiiI * iii1I1I % O0oo0OO0
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( o00oooO0Oo ) + '&' + urllib . urlencode ( i1iIIi1 )
   if 57 - 57: iIii1I11I1II1 - i1IIi / O0oo0OO0 - O0 * OoooooooOO % II111iiii
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 68 - 68: OoooooooOO * I11i % OoOoOO00 - O00oOoOoO0o0O
   if not ( 'celllist' in OoOo00o [ 'cell_toplist' ] ) : return i1iI , IIiIi1iI
   I1 = OoOo00o [ 'cell_toplist' ] [ 'celllist' ]
   if 97 - 97: Oo0ooO0oo0oO
   if 48 - 48: i1IIi - O0oo0OO0
   for O0ooo0O0oo0 in I1 :
    if 56 - 56: o0oOOo0O0Ooo + II111iiii + OoOoOO00 - Oo0ooO0oo0oO . OoOoOO00
    o0O0o0 = O0ooo0O0oo0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if ( O0ooo0O0oo0 . get ( 'thumbnail' ) != '' ) : I1i1i1iii = 'https://%s' % O0ooo0O0oo0 . get ( 'thumbnail' )
    if 84 - 84: OoO0O00 + i1IIi - II111iiii . I1ii11iIi11i * OoooooooOO + I1IiiI
    for OOoo0O in O0ooo0O0oo0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , OOoo0O ) :
      if genre == 'vod' :
       i1IIIiiII1 = ''
       oO00oooOOoOo0 = re . sub ( r'uicode:' , '' , OOoo0O )
      else :
       i1IIIiiII1 = re . sub ( r'uicode:' , '' , OOoo0O )
       oO00oooOOoOo0 = ''
       if O0ooo0O0oo0 . get ( 'bottom_taglist' ) [ 0 ] == 'playy' :
        o0O0o0 += ' [playy]'
        if 38 - 38: OOooOOo + II111iiii % Oo0ooO0oo0oO % OoOoOO00 - Ii1I / OoooooooOO
      oOoO00O0 = { 'title' : unicode ( o0O0o0 )
 , 'thumbnail' : I1i1i1iii
 , 'uicode' : genre
 , 'contentid' : i1IIIiiII1
 , 'programid' : oO00oooOOoOo0
 , 'viewage' : O0ooo0O0oo0 . get ( 'age' )
 }
      if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
    if exclusion21 == False or O0ooo0O0oo0 . get ( 'age' ) != '21' :
     i1iI . append ( oOoO00O0 )
     if 85 - 85: Ii1I % iii1I1I + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
     if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
   iiiIIi1II = int ( OoOo00o [ 'cell_toplist' ] [ 'pagecount' ] )
   if OoOo00o [ 'cell_toplist' ] [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 'cell_toplist' ] [ 'count' ] )
   else : o0O00oOoOO = self . LIST_LIMIT
   if 28 - 28: iii1I1I . iii1I1I % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iii1I1I
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 27 - 27: OoO0O00 + Oo0ooO0oo0oO - i1IIi
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 69 - 69: O00oOoOoO0o0O - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
  return i1iI , IIiIi1iI
  if 79 - 79: O0 * i11iIiiIii - O00oOoOoO0o0O / O00oOoOoO0o0O
  if 48 - 48: O0
 def GetGenreGroup ( self , maintype , subtype , orderby , ordernm , exclusion21 = False ) :
  Oo0o0O00 = [ ]
  if 40 - 40: OoooooooOO
  try :
   i1iIIi1 = self . GetDefaultParams ( )
   if 25 - 25: O00oOoOoO0o0O + Ii1I / Oo0ooO0oo0oO . o0oOOo0O0Ooo % O0 * OoO0O00
   iii11I111 = '/cf/filters'
   if 84 - 84: Oo0ooO0oo0oO % Ii1I + i11iIiiIii
   o00oooO0Oo = { 'type' : maintype }
   if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( o00oooO0Oo ) + '&' + urllib . urlencode ( i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
   if not ( maintype in OoOo00o ) : return None
   iIiIiIiI = OoOo00o [ maintype ]
   if 30 - 30: O0oo0OO0 . Oo0ooO0oo0oO * I1ii11iIi11i
   if subtype == '-' :
    if 17 - 17: I1IiiI . O0 + OoO0O00
    for O0ooo0O0oo0 in iIiIiIiI :
     ii = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( O0ooo0O0oo0 . get ( 'url' ) ) . query ) )
     if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
     oOoO00O0 = { 'title' : O0ooo0O0oo0 . get ( 'text' )
 , 'genre' : O0ooo0O0oo0 . get ( 'id' )
 , 'subgenre' : '-'
 , 'adult' : O0ooo0O0oo0 . get ( 'adult' )
 , 'broadcastid' : ii . get ( 'broadcastid' )
 , 'contenttype' : ii . get ( 'contenttype' )
 , 'uiparent' : ii . get ( 'uiparent' )
 , 'uirank' : ii . get ( 'uirank' )
 , 'uitype' : ii . get ( 'uitype' )
 , 'orderby' : orderby
 , 'ordernm' : ordernm
 }
     if exclusion21 == False or oOoO00O0 . get ( 'adult' ) == 'n' :
      Oo0o0O00 . append ( oOoO00O0 )
      if 81 - 81: iii1I1I + O00oOoOoO0o0O
   else :
    for O0ooo0O0oo0 in iIiIiIiI :
     if O0ooo0O0oo0 . get ( 'id' ) == subtype :
      for o0oo0 in O0ooo0O0oo0 [ 'sublist' ] :
       ii = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( o0oo0 . get ( 'url' ) ) . query ) )
       if 97 - 97: OoOoOO00 % I1ii11iIi11i
       oOoO00O0 = { 'title' : o0oo0 . get ( 'text' )
 , 'genre' : subtype
 , 'subgenre' : o0oo0 . get ( 'id' )
 , 'adult' : o0oo0 . get ( 'adult' )
 , 'broadcastid' : ii . get ( 'broadcastid' )
 , 'contenttype' : ii . get ( 'contenttype' )
 , 'uiparent' : ii . get ( 'uiparent' )
 , 'uirank' : ii . get ( 'uirank' )
 , 'uitype' : ii . get ( 'uitype' )
 , 'orderby' : orderby
 , 'ordernm' : ordernm
 }
       Oo0o0O00 . append ( oOoO00O0 )
      break
      if 25 - 25: Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 55 - 55: Oo0ooO0oo0oO - I11i + II111iiii + iii1I1I % Ii1I
  return Oo0o0O00
  if 41 - 41: i1IIi - I11i - Ii1I
  if 8 - 8: OoO0O00 + O0oo0OO0 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
 def GetGenreGroup_sub ( self , in_params ) :
  Oo0o0O00 = [ ]
  if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + Oo0ooO0oo0oO
  try :
   i1iIIi1 = self . GetDefaultParams ( )
   if 44 - 44: II111iiii
   iii11I111 = '/cf/vod/newcontents'
   if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
   o00oooO0Oo = { 'WeekDay' : 'all'
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
   if 35 - 35: iIii1I11I1II1
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( o00oooO0Oo ) + '&' + urllib . urlencode ( i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 42 - 42: O0oo0OO0 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
   if not ( 'filter_item_list' in OoOo00o [ 'filter' ] [ 'filterlist' ] [ 1 ] ) : return None
   iIiIiIiI = OoOo00o [ 'filter' ] [ 'filterlist' ] [ 1 ] [ 'filter_item_list' ]
   if 31 - 31: iii1I1I . OOooOOo - Oo0ooO0oo0oO . OoooooooOO / OoooooooOO
   for O0ooo0O0oo0 in iIiIiIiI :
    oOoO00O0 = { 'broadcastid' : in_params . get ( 'broadcastid' )
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
    Oo0o0O00 . append ( oOoO00O0 )
    if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 21 - 21: O0 % O00oOoOoO0o0O . I1IiiI / II111iiii + O00oOoOoO0o0O
  return Oo0o0O00
  if 53 - 53: oO0o - I1IiiI - oO0o * iii1I1I
  if 71 - 71: O0 - iIii1I11I1II1
 def GetGenreList ( self , genre , in_params , page_int ) :
  Oo0o0O00 = [ ]
  iiiIIi1II = o0O00oOoOO = 1
  IIiIi1iI = False
  if 12 - 12: OOooOOo / o0oOOo0O0Ooo
  try :
   i1iIIi1 = self . GetDefaultParams ( )
   if 42 - 42: Oo0Ooo
   o00oooO0Oo = { 'WeekDay' : 'all'
 , 'adult' : in_params . get ( 'adult' )
 , 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )

   , 'orderby' : in_params . get ( 'orderby' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )
 }
   if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
   if genre == 'vodgenre' :
    iii11I111 = '/cf/vod/newcontents'
    if 46 - 46: Oo0Ooo
    if in_params . get ( 'subgenre' ) != '-' :
     o00oooO0Oo [ 'subgenre' ] = in_params . get ( 'subgenre' )
   else :
    iii11I111 = '/cf/movie/contents'
    if 1 - 1: iii1I1I
    o00oooO0Oo [ 'price' ] = 'all'
    if 97 - 97: OOooOOo + iii1I1I + O0 + i11iIiiIii
    if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
    o00oooO0Oo [ 'sptheme' ] = 'svod'
    if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iii1I1I % iii1I1I + i11iIiiIii
    if 72 - 72: iIii1I11I1II1 * Ii1I % Oo0ooO0oo0oO / OoO0O00
   o00oooO0Oo [ 'limit' ] = self . LIST_LIMIT
   o00oooO0Oo [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
   o00oooO0Oo [ 'page' ] = str ( page_int )
   if 35 - 35: Oo0ooO0oo0oO + i1IIi % I1ii11iIi11i % I11i + oO0o
   if 17 - 17: i1IIi
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( o00oooO0Oo ) + '&' + urllib . urlencode ( i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 21 - 21: Oo0Ooo
   if not ( 'celllist' in OoOo00o [ 'cell_toplist' ] ) : return None
   iIiIiIiI = OoOo00o [ 'cell_toplist' ] [ 'celllist' ]
   if 29 - 29: I11i / II111iiii / Oo0ooO0oo0oO * OOooOOo
   if 10 - 10: O0oo0OO0 % O00oOoOoO0o0O * O00oOoOoO0o0O . I11i / Ii1I % OOooOOo
   for O0ooo0O0oo0 in iIiIiIiI :
    o0O0o0 = I1i1i1iii = ''
    if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
    o0O0o0 = O0ooo0O0oo0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if 28 - 28: Oo0ooO0oo0oO + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
    if ( O0ooo0O0oo0 . get ( 'thumbnail' ) != '' ) : I1i1i1iii = 'https://%s' % O0ooo0O0oo0 . get ( 'thumbnail' )
    if 54 - 54: i1IIi + II111iiii
    for OOoo0O in O0ooo0O0oo0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , OOoo0O ) :
      oOoO00O0 = { 'title' : unicode ( o0O0o0 )
 , 'uicode' : re . sub ( r'uicode:' , '' , OOoo0O )
 , 'thumbnail' : I1i1i1iii
 , 'viewage' : O0ooo0O0oo0 . get ( 'age' )
 }
      if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
    Oo0o0O00 . append ( oOoO00O0 )
    if 5 - 5: Ii1I
    if 46 - 46: O00oOoOoO0o0O
   iiiIIi1II = int ( OoOo00o [ 'cell_toplist' ] [ 'pagecount' ] )
   if OoOo00o [ 'cell_toplist' ] [ 'count' ] : o0O00oOoOO = int ( OoOo00o [ 'cell_toplist' ] [ 'count' ] )
   else : o0O00oOoOO = self . LIST_LIMIT
   if 45 - 45: Oo0ooO0oo0oO
   IIiIi1iI = iiiIIi1II > o0O00oOoOO
   if 21 - 21: oO0o . O0oo0OO0 . OOooOOo / Oo0Ooo / O0oo0OO0
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 17 - 17: OOooOOo / OOooOOo / I11i
  return Oo0o0O00 , IIiIi1iI
  if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
  if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % O00oOoOoO0o0O / Ii1I . Ii1I
 def GetEPGList ( self , genre ) :
  IIi = { }
  if 66 - 66: oO0o % OoO0O00 . OOooOOo
  try :
   import datetime
   o0O = datetime . datetime . now ( )
   if genre == 'all' :
    IiiiI = o0O + datetime . timedelta ( hours = 2 )
   else :
    IiiiI = o0O + datetime . timedelta ( hours = 3 )
    if 61 - 61: OOooOOo % OOooOOo * o0oOOo0O0Ooo / o0oOOo0O0Ooo
   i1iIIi1 = self . GetDefaultParams ( )
   if 75 - 75: O00oOoOoO0o0O . Oo0ooO0oo0oO
   o00oooO0Oo = { 'limit' : '100'
 , 'offset' : '0'
 , 'genre' : genre
 , 'startdatetime' : o0O . strftime ( '%Y-%m-%d %H:%M' )
 , 'enddatetime' : IiiiI . strftime ( '%Y-%m-%d %H:%M' )
 }
   iii11I111 = '/live/epgs'
   if 50 - 50: OoOoOO00
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( o00oooO0Oo ) + '&' + urllib . urlencode ( i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 60 - 60: Oo0ooO0oo0oO * iIii1I11I1II1 * I1ii11iIi11i * Oo0Ooo
   O0ooooo0OOOO0 = OoOo00o [ 'list' ]
   if 9 - 9: II111iiii - o0oOOo0O0Ooo / iii1I1I / o0oOOo0O0Ooo
   if 40 - 40: OOooOOo * OOooOOo . iii1I1I % O0
   for O0ooo0O0oo0 in O0ooooo0OOOO0 :
    iIi11i1 = ''
    if 71 - 71: Oo0ooO0oo0oO
    for Ooo0o00o0o in O0ooo0O0oo0 [ 'list' ] :
     if iIi11i1 : iIi11i1 += '\n'
     iIi11i1 += Ooo0o00o0o [ 'title' ] + '\n'
     iIi11i1 += ' [%s ~ %s]' % ( Ooo0o00o0o [ 'starttime' ] [ - 5 : ] , Ooo0o00o0o [ 'endtime' ] [ - 5 : ] ) + '\n'
     if 7 - 7: O0 - Oo0Ooo + I1ii11iIi11i + II111iiii + iIii1I11I1II1
     if 58 - 58: o0oOOo0O0Ooo / O00oOoOoO0o0O . OoOoOO00 / OoooooooOO + O0oo0OO0
     if 86 - 86: I11i * I1IiiI + I11i + II111iiii
    IIi [ O0ooo0O0oo0 [ 'channelid' ] ] = unicode ( iIi11i1 )
    if 8 - 8: O0oo0OO0 - iii1I1I / Oo0ooO0oo0oO
    if 96 - 96: OoOoOO00
    if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - Ii1I
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 20 - 20: i1IIi % OoO0O00 . I1IiiI / O00oOoOoO0o0O * i11iIiiIii * OOooOOo
  return IIi
  if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / Oo0ooO0oo0oO . O0 % O0oo0OO0
  if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iii1I1I
 def GetStreamingURL ( self , contentid , contenttype , quality_int ) :
  I1iii11 = ooo0O = iII1iii = i11i1iiiII = ''
  ooOO0oO0oo00o = [ ]
  if 83 - 83: oO0o - II111iiii - iii1I1I
  if 3 - 3: O0oo0OO0
  try :
   if contenttype == 'channel' :
    iii11I111 = '/live/channels/' + contentid
    i1iiIiI1Ii1i = 'live'
   elif contenttype == 'movie' :
    iii11I111 = '/cf/movie/contents/' + contentid
    i1iiIiI1Ii1i = 'movie'
   else :
    iii11I111 = '/cf/vod/contents/' + contentid
    i1iiIiI1Ii1i = 'vod'
    if 22 - 22: O00oOoOoO0o0O / i11iIiiIii
   i1iIIi1 = self . GetDefaultParams ( )
   oo0Ooo0 = self . MakeServiceUrl ( iii11I111 , i1iIIi1 )
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 62 - 62: OoO0O00 / I1ii11iIi11i
   ii1 = OoOo00o [ 'qualities' ] [ 'list' ]
   if ii1 == None : return ( I1iii11 , ooo0O , iII1iii , i11i1iiiII )
   if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
   Oooo00 = 'hls'
   if 'drms' in OoOo00o :
    if OoOo00o [ 'drms' ] :
     Oooo00 = 'dash'
     if 6 - 6: Ii1I - Oo0ooO0oo0oO * OOooOOo . iii1I1I / O0 * Oo0ooO0oo0oO
   print ( Oooo00 )
   if 22 - 22: Oo0Ooo % iii1I1I * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
   if 'type' in OoOo00o :
    if OoOo00o [ 'type' ] == 'onair' :
     i1iiIiI1Ii1i = 'onairvod'
     if 95 - 95: OoooooooOO - O00oOoOoO0o0O * I1IiiI + OoOoOO00
     if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
   for o00 in ii1 :
    ooOO0oO0oo00o . append ( int ( o00 . get ( 'id' ) . rstrip ( 'p' ) ) )
    if 85 - 85: I1ii11iIi11i . O0oo0OO0
  except Exception as OO00Oo :
   return ( I1iii11 , ooo0O , iII1iii , i11i1iiiII )
   if 78 - 78: Oo0ooO0oo0oO * O0oo0OO0 + iIii1I11I1II1 + iIii1I11I1II1 / O0oo0OO0 . Ii1I
   if 97 - 97: Oo0ooO0oo0oO / O0oo0OO0 % i1IIi % I1ii11iIi11i
   if 18 - 18: iIii1I11I1II1 % I11i
  try :
   O00oO0 = self . CheckQuality ( quality_int , ooOO0oO0oo00o )
   iii11I111 = '/streaming'
   o00oooO0Oo = { 'contentid' : contentid
 , 'contenttype' : i1iiIiI1Ii1i
 , 'action' : Oooo00
 , 'quality' : str ( O00oO0 ) + 'p'
 , 'deviceModelId' : 'Windows 10'
 , 'guid' : self . GetGUID ( guidType = 2 )
 , 'lastplayid' : self . guid
 , 'authtype' : 'cookie'
 , 'isabr' : 'y'
 , 'ishevc' : 'n'
 }
   if 97 - 97: O0oo0OO0 - iIii1I11I1II1
   oo0Ooo0 = self . API_DOMAIN + iii11I111 + '?' + urllib . urlencode ( i1iIIi1 ) + '&' + urllib . urlencode ( o00oooO0Oo )
   if 75 - 75: OoooooooOO * O00oOoOoO0o0O
   II1Iiii1111i = self . SESSION . Request ( oo0Ooo0 )
   OoOo00o = json . loads ( II1Iiii1111i )
   if 9 - 9: O00oOoOoO0o0O - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
   I1iii11 = OoOo00o [ 'playurl' ]
   if I1iii11 == None : return None
   ooo0O = OoOo00o [ 'awscookie' ]
   iII1iii = OoOo00o [ 'drm' ]
   if 'previewmsg' in OoOo00o [ 'preview' ] : i11i1iiiII = OoOo00o [ 'preview' ] [ 'previewmsg' ]
   if 39 - 39: O00oOoOoO0o0O * Oo0Ooo + iIii1I11I1II1 - O00oOoOoO0o0O + OOooOOo
  except Exception as OO00Oo :
   print ( OO00Oo )
   if 69 - 69: O0
  I1iii11 = I1iii11 . replace ( 'pooq.co.kr' , 'wavve.com' )
  if 85 - 85: Oo0ooO0oo0oO / O0
  return ( I1iii11 , ooo0O , iII1iii , i11i1iiiII )
  if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
  if 62 - 62: O0oo0OO0 . O00oOoOoO0o0O . OoooooooOO
  if 11 - 11: OOooOOo / I11i
  if 73 - 73: i1IIi / i11iIiiIii
  if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
  if 85 - 85: OoOoOO00 + OOooOOo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
