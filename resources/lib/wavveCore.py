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
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
if 94 - 94: i1IIi % Oo0Ooo
if 68 - 68: Ii1I / O0
if 46 - 46: O0 * II111iiii / IiII * Oo0Ooo * iII111i . I11i
if 62 - 62: i11iIiiIii - II111iiii % I1Ii111 - iIii1I11I1II1 . I1ii11iIi11i . II111iiii
if 61 - 61: oO0o / OoOoOO00 / iII111i * OoO0O00 . II111iiii
if 1 - 1: II111iiii - I1ii11iIi11i % i11iIiiIii + IiII . I1Ii111
if 55 - 55: iIii1I11I1II1 - I1IiiI . Ii1I * IiII * i1IIi / iIii1I11I1II1
if 79 - 79: oO0o + I1Ii111 . ooOoO0o * IiII % I11i . I1IiiI
if 94 - 94: iII111i * Ii1I / IiII . i1IIi * iII111i
if 47 - 47: i1IIi % i11iIiiIii
if 20 - 20: ooOoO0o * II111iiii
oO0o0o0ooO0oO = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
if 52 - 52: II111iiii - i11iIiiIii % I1Ii111
if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
class iIiiI1 ( object ) :
 def __init__ ( self ) :
  if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
  self . MyCookie = cookielib . LWPCookieJar ( )
  if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
  self . Opener = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( self . MyCookie ) )
  self . Opener . addheaders = [ ( 'User-Agent' , oO0o0o0ooO0oO ) ]
  if 3 - 3: iII111i + O0
  urllib2 . install_opener ( self . Opener )
  if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
  if 78 - 78: OoO0O00
 def Request ( self , url , postdata = None ) :
  if postdata :
   Iii1I111 = self . Opener . open ( url , postdata )
  else :
   Iii1I111 = self . Opener . open ( url )
   if 60 - 60: oO0o * o0oOOo0O0Ooo % o0oOOo0O0Ooo % I11i * II111iiii + i1IIi
  OOoooooO = Iii1I111 . read ( )
  Iii1I111 . close ( )
  if 14 - 14: I11i % O0
  return OOoooooO
  if 41 - 41: i1IIi + I1Ii111 + OOooOOo - IiII
  if 77 - 77: Oo0Ooo . IiII % ooOoO0o
  if 42 - 42: oO0o - i1IIi / i11iIiiIii + OOooOOo + OoO0O00
class iIi ( object ) :
 def __init__ ( self ) :
  self . SESSION = iIiiI1 ( )
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
  if 40 - 40: oO0o . OoOoOO00 . Oo0Ooo . i1IIi
 def SaveCredential ( self , credential ) :
  self . CREDENTIAL = credential
  if 33 - 33: Ii1I + II111iiii % i11iIiiIii . ooOoO0o - I1IiiI
 def LoadCredential ( self ) :
  return self . CREDENTIAL
  if 66 - 66: Ii1I - OoooooooOO * OoooooooOO . OOooOOo . I1ii11iIi11i
 def GetDefaultParams ( self ) :
  IiI1i11iii1 = { 'apikey' : self . APIKEY ,
 'credential' : self . CREDENTIAL ,
 'device' : self . DEVICE ,
 'drm' : self . DRM ,
 'partner' : self . PARTNER ,
 'pooqzone' : self . POOQZONE ,
 'region' : self . REGION ,
 'targetage' : self . TARGETAGE
 }
  return IiI1i11iii1
  if 96 - 96: O0 % oO0o % iIii1I11I1II1
 def makeurl ( self , domain , path , query = None ) :
  Oo00OOOOO = ''
  if domain :
   if re . search ( r'http[s]*://' , domain ) :
    Oo00OOOOO += domain
   else :
    Oo00OOOOO += 'http://%s' % domain
   if path :
    Oo00OOOOO += path
    if query : Oo00OOOOO += '?%s' % query
  return Oo00OOOOO
  if 85 - 85: ooOoO0o . iII111i - OoO0O00 % ooOoO0o % II111iiii
 def MakeServiceUrl ( self , path , params ) :
  if 81 - 81: OoO0O00 + II111iiii % iII111i * O0
  Oo00OOOOO = self . makeurl ( self . API_DOMAIN , path , urllib . urlencode ( params ) )
  return Oo00OOOOO
  if 89 - 89: oO0o + Oo0Ooo
 def GetGUID ( self , guid_str = 'POOQ' , guidType = 1 ) :
  if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
  def III1ii1iII ( media ) :
   from datetime import datetime
   oo0oooooO0 = datetime . now ( ) . strftime ( '%Y%m%d%H%M%S' )
   i11Iiii = iI ( 5 )
   I1i1I1II = i11Iiii + media + oo0oooooO0
   return I1i1I1II
   if 45 - 45: I1Ii111 . OoOoOO00
  def iI ( num ) :
   from random import randint
   oO = ""
   for ii1i1I1i in range ( 0 , num ) :
    o00oOO0 = str ( randint ( 1 , 5 ) )
    oO += o00oOO0
   return oO
   if 95 - 95: OOooOOo / OoooooooOO
  I1i1I1II = III1ii1iII ( guid_str )
  if 18 - 18: i11iIiiIii
  Ii11I = self . GetHash ( I1i1I1II )
  if guidType == 2 :
   Ii11I = '%s-%s-%s-%s-%s' % ( Ii11I [ : 8 ] , Ii11I [ 8 : 12 ] , Ii11I [ 12 : 16 ] , Ii11I [ 16 : 20 ] , Ii11I [ 20 : ] )
   if 69 - 69: oO0o % I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - O0 % OoooooooOO
  return Ii11I
  if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
 def GetHash ( self , hash_str ) :
  import hashlib
  iii11 = hashlib . md5 ( )
  if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
  iii11 . update ( hash_str )
  return str ( iii11 . hexdigest ( ) )
  if 50 - 50: I1IiiI
 def CheckQuality ( self , sel_qt , qt_list ) :
  Ii1i11IIii1I = 0
  for OOOoO0O0o in qt_list :
   if sel_qt >= OOOoO0O0o : return OOOoO0O0o
   Ii1i11IIii1I = OOOoO0O0o
  return Ii1i11IIii1I
  if 55 - 55: OOooOOo + ooOoO0o . i1IIi - I1ii11iIi11i . O0 - ooOoO0o
  if 92 - 92: iII111i . I11i + o0oOOo0O0Ooo
 def GetCredential ( self , user_id , user_pw , user_pf ) :
  IiII1I11i1I1I = False
  try :
   oO0Oo = '/login'
   IiI1i11iii1 = self . GetDefaultParams ( )
   oOOoo0Oo = { 'id' : user_id
 , 'password' : user_pw
 , 'profile' : '0'
 , 'pushid' : ''
 , 'type' : 'general'
 }
   Oo00OOOOO = self . MakeServiceUrl ( oO0Oo , IiI1i11iii1 )
   if 78 - 78: I11i
   if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO , postdata = urllib . urlencode ( oOOoo0Oo ) )
   oO0OOoO0 = json . loads ( Iii1I111 )
   I111Ii111 = oO0OOoO0 [ 'credential' ]
   if 4 - 4: oO0o
   if 93 - 93: OoO0O00 % oO0o . OoO0O00 * I1Ii111 % Ii1I . II111iiii
   if user_pf != 0 :
    oOOoo0Oo = { 'id' : I111Ii111
 , 'password' : ''
 , 'profile' : str ( user_pf )
 , 'pushid' : ''
 , 'type' : 'credential'
 }
    if 38 - 38: o0oOOo0O0Ooo
    Iii1I111 = self . SESSION . Request ( Oo00OOOOO , postdata = urllib . urlencode ( oOOoo0Oo ) )
    oO0OOoO0 = json . loads ( Iii1I111 )
    I111Ii111 = oO0OOoO0 [ 'credential' ]
    if 57 - 57: O0 / oO0o * I1Ii111 / OoOoOO00 . II111iiii
    if 26 - 26: iII111i
   if I111Ii111 : IiII1I11i1I1I = True
   if 91 - 91: OoO0O00 . I1ii11iIi11i + OoO0O00 - iII111i / OoooooooOO
   if 39 - 39: I1ii11iIi11i / ooOoO0o - II111iiii
  except Exception as OO00o :
   print ( OO00o )
   I111Ii111 = 'none'
   if 61 - 61: II111iiii * oO0o % Oo0Ooo
  self . SaveCredential ( I111Ii111 )
  return IiII1I11i1I1I
  if 64 - 64: I11i % iII111i - I1Ii111 - oO0o
 def GetIssue ( self ) :
  i1ii1iiI = False
  try :
   oO0Oo = '/guid/issue'
   IiI1i11iii1 = self . GetDefaultParams ( )
   Oo00OOOOO = self . MakeServiceUrl ( oO0Oo , IiI1i11iii1 )
   if 98 - 98: iII111i * iII111i / iII111i + I11i
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   if 34 - 34: ooOoO0o
   oO0OOoO0 = json . loads ( Iii1I111 )
   I1111I1iII11 = oO0OOoO0 [ 'guid' ]
   Oooo0O0oo00oO = oO0OOoO0 [ 'guidtimestamp' ]
   if I1111I1iII11 : i1ii1iiI = True
  except Exception as OO00o :
   print ( OO00o )
   I1111I1iII11 = 'none'
   Oooo0O0oo00oO = 'none'
   if 14 - 14: OoOoOO00 / IiII . OoOoOO00 . I11i % OoO0O00 * I11i
  self . guid = I1111I1iII11
  self . guidtimestamp = Oooo0O0oo00oO
  if 16 - 16: OoOoOO00 . ooOoO0o + i11iIiiIii
  return i1ii1iiI
  if 38 - 38: IiII * OOooOOo . o0oOOo0O0Ooo
 def GetGnList ( self , gn_str ) :
  ooo0OO = [ ]
  try :
   oO0Oo = '/cf/supermultisections/' + gn_str
   IiI1i11iii1 = self . GetDefaultParams ( )
   Oo00OOOOO = self . MakeServiceUrl ( oO0Oo , IiI1i11iii1 )
   if 65 - 65: Ii1I . iIii1I11I1II1 / O0 - Ii1I
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 21 - 21: I1IiiI * iIii1I11I1II1
   if not ( 'multisectionlist' in oO0OOoO0 ) : return None
   oooooOoo0ooo = oO0OOoO0 [ 'multisectionlist' ]
   if 6 - 6: I11i - Ii1I + iIii1I11I1II1 - I1Ii111 - i11iIiiIii
   if 79 - 79: OoOoOO00 - O0 * OoO0O00 + OoOoOO00 % O0 * O0
   for oOOo0 in oooooOoo0ooo :
    oo00O00oO = oOOo0 [ 'title' ]
    if len ( oo00O00oO ) == 0 : continue
    if 23 - 23: OoO0O00 + OoO0O00 . OOooOOo
    if re . search ( u'베너' , oo00O00oO ) : continue
    if 38 - 38: I1Ii111
    oo00O00oO = re . sub ( '\n|\!|\~|(@0@)|(@\^0@)' , '' , oo00O00oO )
    oo00O00oO = oo00O00oO . lstrip ( '#' )
    if 7 - 7: O0 . iII111i % I1ii11iIi11i - I1IiiI - iIii1I11I1II1
    for I111IIIiIii in oOOo0 [ 'eventlist' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , I111IIIiIii ) :
      oO0000OOo00 = { 'title' : unicode ( oo00O00oO )
 , 'uicode' : re . sub ( r'uicode:' , '' , I111IIIiIii )
 }
      ooo0OO . append ( oO0000OOo00 )
      break
      if 27 - 27: I1IiiI % I1IiiI
  except Exception as OO00o :
   print ( OO00o )
   if 1 - 1: OoO0O00 - oO0o . I11i . OoO0O00 / Oo0Ooo + I11i
  return ooo0OO
  if 78 - 78: O0 . oO0o . II111iiii % OOooOOo
 def GetDeeplinkList ( self , gn_str , came_str , page_int ) :
  i1iIi = [ ]
  ooOOoooooo = II1I = 1
  O0i1II1Iiii1I11 = 'quick'
  IIII = iiIiI = o00oooO0Oo = ''
  o0O0OOO0Ooo = False
  iiIiII1 = { }
  if 86 - 86: OoOoOO00 - Ii1I - OoO0O00 * iII111i
  try :
   if 66 - 66: OoooooooOO + O0
   oO0Oo = '/cf/deeplink/' + gn_str
   IiI1i11iii1 = self . GetDefaultParams ( )
   Oo00OOOOO = self . MakeServiceUrl ( oO0Oo , IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
   if not ( 'url' in oO0OOoO0 ) : return None
   i1Iii1i1I = oO0OOoO0 [ 'url' ]
   if 91 - 91: I1ii11iIi11i + I1IiiI . OOooOOo * I1ii11iIi11i + I1IiiI * Oo0Ooo
   if 80 - 80: iII111i % OOooOOo % oO0o - Oo0Ooo + Oo0Ooo
   if 19 - 19: OoOoOO00 * i1IIi
   if 14 - 14: iII111i
   oO0Oo = urlparse . urlsplit ( i1Iii1i1I ) . path
   I1iI1iIi111i = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( i1Iii1i1I ) . query ) )
   if 44 - 44: i1IIi % II111iiii + I11i
   I1iI1iIi111i [ 'came' ] = came_str
   I1iI1iIi111i [ 'limit' ] = str ( self . LIST_LIMIT )
   if 'contenttype' in I1iI1iIi111i : O0i1II1Iiii1I11 = I1iI1iIi111i [ 'contenttype' ]
   if 45 - 45: iII111i / iII111i + I1Ii111 + ooOoO0o
   if page_int != 1 :
    I1iI1iIi111i [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
    I1iI1iIi111i [ 'page' ] = str ( page_int )
    if 47 - 47: o0oOOo0O0Ooo + ooOoO0o
   Oo00OOOOO = self . HTTPTAG + oO0Oo + '?' + urllib . urlencode ( I1iI1iIi111i ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   if 82 - 82: II111iiii . IiII - iIii1I11I1II1 - IiII * II111iiii
   if 77 - 77: iIii1I11I1II1 * OoO0O00
   if 95 - 95: I1IiiI + i11iIiiIii
   if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
   if 80 - 80: II111iiii
   if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 53 - 53: II111iiii
   if 31 - 31: OoO0O00
   if not ( 'celllist' in oO0OOoO0 [ 'cell_toplist' ] ) : return i1iIi , o0O0OOO0Ooo
   o0O = oO0OOoO0 [ 'cell_toplist' ] [ 'celllist' ]
   if 2 - 2: iIii1I11I1II1 / oO0o + OoO0O00 / OOooOOo
   if 9 - 9: o0oOOo0O0Ooo . ooOoO0o - Oo0Ooo - oO0o + II111iiii * i11iIiiIii
   if 79 - 79: oO0o % I11i % I1IiiI
   if ( O0i1II1Iiii1I11 == 'channel' ) :
    if ( 'genre' in I1iI1iIi111i ) :
     Ii1I1I1i1Ii = I1iI1iIi111i [ 'genre' ]
    else :
     Ii1I1I1i1Ii = 'all'
     if 5 - 5: I1Ii111 . o0oOOo0O0Ooo
    iiIiII1 = self . GetEPGList ( Ii1I1I1i1Ii )
    if 99 - 99: Ii1I / Oo0Ooo / IiII % I1IiiI
    if 13 - 13: I11i * Oo0Ooo * ooOoO0o
    if 50 - 50: o0oOOo0O0Ooo * I11i % O0
   for oOOo0 in o0O :
    OooOoOO0 = iI1i11iII111 = Iii1IIII11I = ''
    if 77 - 77: Oo0Ooo - i1IIi - I11i . OoOoOO00
    OooOoOO0 = oOOo0 . get ( 'title_list' ) [ 0 ] . get ( 'text' )
    if ( len ( oOOo0 . get ( 'title_list' ) ) > 1 ) :
     if ( oOOo0 . get ( 'title_list' ) [ 1 ] . get ( 'text' ) . startswith ( '@' ) ) :
      for IiI1i in oOOo0 . get ( 'bottom_taglist' ) :
       if IiI1i == 'playy' or IiI1i == 'won' : iI1i11iII111 = IiI1i
     else :
      iI1i11iII111 = oOOo0 . get ( 'title_list' ) [ 1 ] . get ( 'text' )
      iI1i11iII111 = re . sub ( r'(\$O\$)|(\&[a-z]{2}\;)' , '' , iI1i11iII111 )
    if ( oOOo0 . get ( 'thumbnail' ) != '' ) : Iii1IIII11I = 'https://%s' % oOOo0 . get ( 'thumbnail' )
    if 92 - 92: IiII . IiII + OoO0O00
    IiIiI1111I1I = oOOo0 [ 'event_list' ] [ 1 ] . get ( 'url' )
    i1i = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( IiIiI1111I1I ) . query ) )
    if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
    if re . search ( u'programid=\&' , IiIiI1111I1I ) and ( 'contentid' in i1i ) :
     IIII = i1i [ 'contentid' ]
     iiIiI = 'direct'
    elif ( 'contentid' in i1i ) :
     IIII = i1i [ 'contentid' ]
     iiIiI = 'contentid'
    elif ( 'programid' in i1i ) :
     IIII = i1i [ 'programid' ]
     iiIiI = 'programid'
    elif ( 'channelid' in i1i ) :
     IIII = i1i [ 'channelid' ]
     iiIiI = 'channelid'
     if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
     if IIII in iiIiII1 :
      o00oooO0Oo = iiIiII1 [ IIII ]
     else :
      o00oooO0Oo = ''
      if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
    elif ( 'movieid' in i1i ) :
     IIII = i1i [ 'movieid' ]
     iiIiI = 'movieid'
     if O0i1II1Iiii1I11 == 'x' : O0i1II1Iiii1I11 = 'movie'
    else :
     IIII = '-'
     iiIiI = '-'
     if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
    oO0000OOo00 = { 'title' : unicode ( OooOoOO0 )
 , 'subtitle' : unicode ( iI1i11iII111 )
 , 'thumbnail' : Iii1IIII11I
 , 'uicode' : O0i1II1Iiii1I11
 , 'contentid' : IIII
 , 'contentidType' : iiIiI
 , 'viewage' : oOOo0 . get ( 'age' )
 , 'channelepg' : o00oooO0Oo
 }
    i1iIi . append ( oO0000OOo00 )
    if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
   ooOOoooooo = int ( oO0OOoO0 [ 'cell_toplist' ] [ 'pagecount' ] )
   if oO0OOoO0 [ 'cell_toplist' ] [ 'count' ] : II1I = int ( oO0OOoO0 [ 'cell_toplist' ] [ 'count' ] )
   else : II1I = self . LIST_LIMIT
   if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
   if 63 - 63: OoOoOO00 * iII111i
   o0O0OOO0Ooo = ooOOoooooo > II1I
   if 69 - 69: O0 . OoO0O00
   if 49 - 49: I1IiiI - I11i
  except Exception as OO00o :
   print ( OO00o )
   if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
  return ( i1iIi , o0O0OOO0Ooo )
  if 62 - 62: OoooooooOO * I1IiiI
  if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
 def GetEpisodeList ( self , contentid , contenttype , contentidType , page_int , orderby = 'desc' ) :
  i1 = [ ]
  ooOOoooooo = II1I = 1
  o0O0OOO0Ooo = False
  if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * IiII
  if orderby == 'desc' :
   orderby = 'new'
  else :
   orderby = 'old'
   if 73 - 73: OoO0O00 + OoooooooOO - O0 - Ii1I - II111iiii
  try :
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 99 - 99: ooOoO0o . Ii1I + I1Ii111 + OoooooooOO % o0oOOo0O0Ooo
   if 51 - 51: iIii1I11I1II1
   if contentidType == 'contentid' :
    oO0Oo = '/cf/vod/contents/' + contentid
    if 34 - 34: oO0o + I1IiiI - oO0o
    Oo00OOOOO = self . MakeServiceUrl ( oO0Oo , IiI1i11iii1 )
    Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
    oO0OOoO0 = json . loads ( Iii1I111 )
    if 17 - 17: II111iiii % iII111i + I11i - iII111i / OOooOOo + ooOoO0o
    if not ( 'programid' in oO0OOoO0 ) : return None
    O0oO000O0O = oO0OOoO0 [ 'programid' ]
    if 18 - 18: iII111i - OOooOOo . I1Ii111 . iIii1I11I1II1
   else :
    O0oO000O0O = contentid
    if 2 - 2: OOooOOo . OoO0O00
    if 78 - 78: I11i * iIii1I11I1II1 . I1IiiI / o0oOOo0O0Ooo - OoooooooOO / I1Ii111
    if 35 - 35: I11i % OOooOOo - oO0o
   oO0Oo = '/vod/programs-contents/' + O0oO000O0O
   if 20 - 20: i1IIi - ooOoO0o
   I1iI1iIi111i = { 'limit' : self . EP_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . EP_LIMIT )
 , 'orderby' : orderby
   }
   if 30 - 30: I11i / I1IiiI
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1iI1iIi111i ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 35 - 35: II111iiii % OOooOOo . ooOoO0o + ooOoO0o % II111iiii % II111iiii
   if not ( 'list' in oO0OOoO0 ) : return None
   ooOoO00 = oO0OOoO0 [ 'list' ]
   if 14 - 14: i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
   if 72 - 72: Ii1I
   for oOOo0 in ooOoO00 :
    II11Ii1iI1iII = oOOo0 . get ( 'programtitle' )
    Oo0o00OO0000 = '%s회, %s(%s)' % ( oOOo0 . get ( 'episodenumber' ) , oOOo0 . get ( 'releasedate' ) , oOOo0 . get ( 'releaseweekday' ) )
    if ( oOOo0 . get ( 'image' ) != '' ) : I1i = 'https://%s' % oOOo0 . get ( 'image' )
    if 99 - 99: I1Ii111 + OoOoOO00 * iIii1I11I1II1 / OoooooooOO
    i11I = unicode ( oOOo0 . get ( 'synopsis' ) )
    i11I = re . sub ( u'(\<[a-zA-Z]{1,2}\>)|(\<\/[a-zA-Z]{1,2}\>)' , '' , i11I )
    if 76 - 76: IiII * iII111i
    ooooooo00o = { 'title' : unicode ( II11Ii1iI1iII )
 , 'subtitle' : unicode ( Oo0o00OO0000 )
 , 'thumbnail' : I1i
 , 'uicode' : contenttype
 , 'contentid' : oOOo0 . get ( 'contentid' )
 , 'programid' : oOOo0 . get ( 'programid' )
 , 'synopsis' : i11I
 , 'viewage' : oOOo0 . get ( 'targetage' )
 }
    i1 . append ( ooooooo00o )
    if 73 - 73: OOooOOo
   ooOOoooooo = int ( oO0OOoO0 [ 'pagecount' ] )
   if oO0OOoO0 [ 'count' ] : II1I = int ( oO0OOoO0 [ 'count' ] )
   else : II1I = self . EP_LIMIT
   if 70 - 70: iIii1I11I1II1
   o0O0OOO0Ooo = ooOOoooooo > II1I
   if 31 - 31: IiII - I1IiiI % iIii1I11I1II1
  except Exception as OO00o :
   print ( OO00o )
   if 92 - 92: i1IIi - iIii1I11I1II1
  return ( i1 , o0O0OOO0Ooo )
  if 16 - 16: OoO0O00 - OoOoOO00 - OOooOOo - i1IIi / Ii1I
  if 88 - 88: OoO0O00
 def GetMyviewList ( self , contenttype , page_int ) :
  ooOOOooO = [ ]
  ooOOoooooo = II1I = 1
  o0O0OOO0Ooo = False
  if 12 - 12: O0 - o0oOOo0O0Ooo
  try :
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
   oO0Oo = '/myview/contents'
   if 73 - 73: I11i % i11iIiiIii - I1IiiI
   I1iI1iIi111i = { 'contenttype' : contenttype
 , 'limit' : self . MV_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . MV_LIMIT )
 , 'orderby' : 'new'
 }
   if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1iI1iIi111i ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
   if not ( 'list' in oO0OOoO0 [ 0 ] ) : return None
   ii = oO0OOoO0 [ 0 ] [ 'list' ]
   if 68 - 68: iII111i - I1IiiI / I1Ii111 / I11i
   for oOOo0 in ii :
    if 12 - 12: Ii1I + i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . I11i
    if contenttype == 'vod' :
     II11Ii1iI1iII = oOOo0 . get ( 'programtitle' )
     Oo0o00OO0000 = '%s회, %s' % ( oOOo0 . get ( 'episodenumber' ) , oOOo0 . get ( 'releasedate' ) )
     IIII = oOOo0 . get ( 'contentid' )
     O0oO000O0O = oOOo0 . get ( 'programid' )
     if 5 - 5: i1IIi + IiII / o0oOOo0O0Ooo . iII111i / I11i
    else :
     II11Ii1iI1iII = oOOo0 . get ( 'title' )
     Oo0o00OO0000 = '%s' % ( oOOo0 . get ( 'releasedate' ) )
     IIII = O0oO000O0O = oOOo0 . get ( 'movieid' )
     if 32 - 32: I1IiiI % iIii1I11I1II1 / i1IIi - I1IiiI
    if ( oOOo0 . get ( 'image' ) != '' ) : I1i = 'https://%s' % oOOo0 . get ( 'image' )
    if 7 - 7: I1Ii111 * OoO0O00 - ooOoO0o + OOooOOo * I1IiiI % OoO0O00
    iI1i111I1Ii = { 'title' : unicode ( II11Ii1iI1iII )
 , 'subtitle' : unicode ( Oo0o00OO0000 )
 , 'thumbnail' : I1i
 , 'uicode' : contenttype
 , 'contentid' : IIII
 , 'programid' : O0oO000O0O
 , 'viewage' : oOOo0 . get ( 'targetage' )
 }
    if 25 - 25: I1Ii111 - iII111i
    ooOOOooO . append ( iI1i111I1Ii )
    if 10 - 10: II111iiii / oO0o % OoooooooOO * I11i % I1ii11iIi11i
    if 48 - 48: ooOoO0o / I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / i1IIi
   ooOOoooooo = int ( oO0OOoO0 [ 0 ] [ 'pagecount' ] )
   if oO0OOoO0 [ 0 ] [ 'count' ] : II1I = int ( oO0OOoO0 [ 0 ] [ 'count' ] )
   else : II1I = self . MV_LIMIT
   if 92 - 92: Oo0Ooo % Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
   o0O0OOO0Ooo = ooOOoooooo > II1I
   if 10 - 10: iII111i + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / I1ii11iIi11i
  except Exception as OO00o :
   print ( OO00o )
   if 42 - 42: I1IiiI
  return ooOOOooO , o0O0OOO0Ooo
  if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
  if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
 def GetSearchList ( self , search_key , genre , page_int , exclusion21 = False ) :
  O0O0o0oOOO = [ ]
  ooOOoooooo = II1I = 1
  o0O0OOO0Ooo = False
  if 67 - 67: OoOoOO00 + I1ii11iIi11i . o0oOOo0O0Ooo . II111iiii
  try :
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 98 - 98: iII111i
   oO0Oo = '/cf/search/list.js'
   if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / II111iiii % Oo0Ooo
   I1iI1iIi111i = { 'type' : 'program' if genre == 'vod' else 'movie'
 , 'keyword' : search_key
 , 'offset' : str ( ( page_int - 1 ) * self . LIST_LIMIT )
 , 'limit' : self . LIST_LIMIT
   , 'orderby' : 'score'
 , 'isplayymovie' : 'y'
 }
   if 38 - 38: ooOoO0o - OOooOOo / iII111i
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1iI1iIi111i ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / Ii1I + I1ii11iIi11i
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 86 - 86: o0oOOo0O0Ooo
   if not ( 'celllist' in oO0OOoO0 [ 'cell_toplist' ] ) : return O0O0o0oOOO , o0O0OOO0Ooo
   i1Iii11Ii1i1 = oO0OOoO0 [ 'cell_toplist' ] [ 'celllist' ]
   if 59 - 59: Oo0Ooo % OoooooooOO . iII111i / IiII + I1IiiI
   if 76 - 76: ooOoO0o
   for oOOo0 in i1Iii11Ii1i1 :
    if 73 - 73: O0 * iII111i + Ii1I + ooOoO0o
    II11Ii1iI1iII = oOOo0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if ( oOOo0 . get ( 'thumbnail' ) != '' ) : I1i = 'https://%s' % oOOo0 . get ( 'thumbnail' )
    if 40 - 40: II111iiii . OoOoOO00 * I1Ii111 + OOooOOo + OOooOOo
    for I111IIIiIii in oOOo0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , I111IIIiIii ) :
      if genre == 'vod' :
       IIII = ''
       O0oO000O0O = re . sub ( r'uicode:' , '' , I111IIIiIii )
      else :
       IIII = re . sub ( r'uicode:' , '' , I111IIIiIii )
       O0oO000O0O = ''
       if oOOo0 . get ( 'bottom_taglist' ) [ 0 ] == 'playy' :
        II11Ii1iI1iII += ' [playy]'
        if 9 - 9: I11i % OoooooooOO . oO0o % I11i
      iI1i111I1Ii = { 'title' : unicode ( II11Ii1iI1iII )
 , 'thumbnail' : I1i
 , 'uicode' : genre
 , 'contentid' : IIII
 , 'programid' : O0oO000O0O
 , 'viewage' : oOOo0 . get ( 'age' )
 }
      if 32 - 32: i11iIiiIii
    if exclusion21 == False or oOOo0 . get ( 'age' ) != '21' :
     O0O0o0oOOO . append ( iI1i111I1Ii )
     if 31 - 31: iIii1I11I1II1 / OoO0O00 / I1ii11iIi11i
     if 41 - 41: Oo0Ooo
   ooOOoooooo = int ( oO0OOoO0 [ 'cell_toplist' ] [ 'pagecount' ] )
   if oO0OOoO0 [ 'cell_toplist' ] [ 'count' ] : II1I = int ( oO0OOoO0 [ 'cell_toplist' ] [ 'count' ] )
   else : II1I = self . LIST_LIMIT
   if 10 - 10: Oo0Ooo / Oo0Ooo / I1Ii111 . I1Ii111
   o0O0OOO0Ooo = ooOOoooooo > II1I
   if 98 - 98: Oo0Ooo / I1IiiI . O0 + OoO0O00
  except Exception as OO00o :
   print ( OO00o )
   if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
  return O0O0o0oOOO , o0O0OOO0Ooo
  if 20 - 20: I1IiiI
  if 95 - 95: iII111i - I1IiiI
 def GetGenreGroup ( self , maintype , subtype , exclusion21 = False ) :
  I1ii1ii11i1I = [ ]
  if 58 - 58: iII111i + Oo0Ooo
  try :
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 12 - 12: o0oOOo0O0Ooo - I1ii11iIi11i % OoOoOO00 * I11i
   oO0Oo = '/cf/filters'
   if 44 - 44: iII111i % Ii1I
   I1iI1iIi111i = { 'type' : maintype }
   if 41 - 41: i1IIi - I11i - Ii1I
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1iI1iIi111i ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
   if not ( maintype in oO0OOoO0 ) : return None
   IIIi11I11 = oO0OOoO0 [ maintype ]
   if 44 - 44: II111iiii
   if subtype == '-' :
    if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
    for oOOo0 in IIIi11I11 :
     iI1 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( oOOo0 . get ( 'url' ) ) . query ) )
     if 12 - 12: I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI / iII111i
     iI1i111I1Ii = { 'title' : oOOo0 . get ( 'text' )
 , 'genre' : oOOo0 . get ( 'id' )
 , 'subgenre' : '-'
 , 'adult' : oOOo0 . get ( 'adult' )
 , 'broadcastid' : iI1 . get ( 'broadcastid' )
 , 'contenttype' : iI1 . get ( 'contenttype' )
 , 'uiparent' : iI1 . get ( 'uiparent' )
 , 'uirank' : iI1 . get ( 'uirank' )
 , 'uitype' : iI1 . get ( 'uitype' )
 }
     if exclusion21 == False or iI1i111I1Ii . get ( 'adult' ) == 'n' :
      I1ii1ii11i1I . append ( iI1i111I1Ii )
      if 12 - 12: OOooOOo - ooOoO0o . OoooooooOO / I1ii11iIi11i . i1IIi * OoO0O00
   else :
    for oOOo0 in IIIi11I11 :
     if oOOo0 . get ( 'id' ) == subtype :
      for IiIiII1 in oOOo0 [ 'sublist' ] :
       iI1 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( IiIiII1 . get ( 'url' ) ) . query ) )
       if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
       iI1i111I1Ii = { 'title' : IiIiII1 . get ( 'text' )
 , 'genre' : subtype
 , 'subgenre' : IiIiII1 . get ( 'id' )
 , 'adult' : IiIiII1 . get ( 'adult' )
 , 'broadcastid' : iI1 . get ( 'broadcastid' )
 , 'contenttype' : iI1 . get ( 'contenttype' )
 , 'uiparent' : iI1 . get ( 'uiparent' )
 , 'uirank' : iI1 . get ( 'uirank' )
 , 'uitype' : iI1 . get ( 'uitype' )
 }
       I1ii1ii11i1I . append ( iI1i111I1Ii )
      break
      if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
  except Exception as OO00o :
   print ( OO00o )
   if 71 - 71: O0 - iIii1I11I1II1
  return I1ii1ii11i1I
  if 12 - 12: OOooOOo / o0oOOo0O0Ooo
  if 42 - 42: Oo0Ooo
 def GetGenreGroup_sub ( self , in_params ) :
  I1ii1ii11i1I = [ ]
  if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
  try :
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 46 - 46: Oo0Ooo
   oO0Oo = '/cf/vod/newcontents'
   if 1 - 1: iII111i
   I1iI1iIi111i = { 'WeekDay' : 'all'
 , 'limit' : '20'
 , 'offset' : '0'
 , 'orderby' : 'new'
 , 'adult' : in_params . get ( 'adult' )
 , 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )
 }
   if 97 - 97: OOooOOo + iII111i + O0 + i11iIiiIii
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1iI1iIi111i ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
   if not ( 'filter_item_list' in oO0OOoO0 [ 'filter' ] [ 'filterlist' ] [ 1 ] ) : return None
   IIIi11I11 = oO0OOoO0 [ 'filter' ] [ 'filterlist' ] [ 1 ] [ 'filter_item_list' ]
   if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
   for oOOo0 in IIIi11I11 :
    iI1i111I1Ii = { 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )

 , 'adult' : oOOo0 . get ( 'adult' )
 , 'title' : oOOo0 . get ( 'title' )
 , 'subgenre' : oOOo0 . get ( 'api_parameters' ) [ oOOo0 . get ( 'api_parameters' ) . find ( '=' ) + 1 : ]
 }
    I1ii1ii11i1I . append ( iI1i111I1Ii )
    if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
  except Exception as OO00o :
   print ( OO00o )
   if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
  return I1ii1ii11i1I
  if 17 - 17: i1IIi
  if 21 - 21: Oo0Ooo
 def GetGenreList ( self , genre , in_params , page_int ) :
  I1ii1ii11i1I = [ ]
  ooOOoooooo = II1I = 1
  o0O0OOO0Ooo = False
  if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
  try :
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
   I1iI1iIi111i = { 'WeekDay' : 'all'
 , 'adult' : in_params . get ( 'adult' )
 , 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )
 , 'orderby' : 'new'
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )
 }
   if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
   if genre == 'vodgenre' :
    oO0Oo = '/cf/vod/newcontents'
    if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
    if in_params . get ( 'subgenre' ) != '-' :
     I1iI1iIi111i [ 'subgenre' ] = in_params . get ( 'subgenre' )
   else :
    oO0Oo = '/cf/movie/contents'
    if 54 - 54: i1IIi + II111iiii
    I1iI1iIi111i [ 'price' ] = 'all'
    if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
    I1iI1iIi111i [ 'orderby' ] = 'paid'
    I1iI1iIi111i [ 'sptheme' ] = 'svod'
    if 5 - 5: Ii1I
    if 46 - 46: IiII
   I1iI1iIi111i [ 'limit' ] = self . LIST_LIMIT
   I1iI1iIi111i [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
   I1iI1iIi111i [ 'page' ] = str ( page_int )
   if 45 - 45: ooOoO0o
   if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1iI1iIi111i ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 17 - 17: OOooOOo / OOooOOo / I11i
   if not ( 'celllist' in oO0OOoO0 [ 'cell_toplist' ] ) : return None
   IIIi11I11 = oO0OOoO0 [ 'cell_toplist' ] [ 'celllist' ]
   if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
   if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % IiII / Ii1I . Ii1I
   for oOOo0 in IIIi11I11 :
    II11Ii1iI1iII = I1i = ''
    if 14 - 14: o0oOOo0O0Ooo . OOooOOo . I11i + OoooooooOO - OOooOOo + IiII
    II11Ii1iI1iII = oOOo0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if 9 - 9: Ii1I
    if ( oOOo0 . get ( 'thumbnail' ) != '' ) : I1i = 'https://%s' % oOOo0 . get ( 'thumbnail' )
    if 59 - 59: I1IiiI * II111iiii . O0
    for I111IIIiIii in oOOo0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , I111IIIiIii ) :
      iI1i111I1Ii = { 'title' : unicode ( II11Ii1iI1iII )
 , 'uicode' : re . sub ( r'uicode:' , '' , I111IIIiIii )
 , 'thumbnail' : I1i
 , 'viewage' : oOOo0 . get ( 'age' )
 }
      if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
    I1ii1ii11i1I . append ( iI1i111I1Ii )
    if 51 - 51: O0 / ooOoO0o * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
    if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + ooOoO0o % i11iIiiIii % O0
   ooOOoooooo = int ( oO0OOoO0 [ 'cell_toplist' ] [ 'pagecount' ] )
   if oO0OOoO0 [ 'cell_toplist' ] [ 'count' ] : II1I = int ( oO0OOoO0 [ 'cell_toplist' ] [ 'count' ] )
   else : II1I = self . LIST_LIMIT
   if 27 - 27: O0
   o0O0OOO0Ooo = ooOOoooooo > II1I
   if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
  except Exception as OO00o :
   print ( OO00o )
   if 28 - 28: i1IIi - iII111i
  return I1ii1ii11i1I , o0O0OOO0Ooo
  if 54 - 54: iII111i - O0 % OOooOOo
  if 73 - 73: O0 . OoOoOO00 + I1IiiI - I11i % I11i . I11i
 def GetEPGList ( self , genre ) :
  I11ii1i1 = { }
  if 78 - 78: iII111i
  try :
   import datetime
   iIiIIIIIii = datetime . datetime . now ( )
   if genre == 'all' :
    OOo0 = iIiIIIIIii + datetime . timedelta ( hours = 2 )
   else :
    OOo0 = iIiIIIIIii + datetime . timedelta ( hours = 3 )
    if 25 - 25: OoooooooOO + IiII * I1ii11iIi11i
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + I1Ii111
   I1iI1iIi111i = { 'limit' : '100'
 , 'offset' : '0'
 , 'genre' : genre
 , 'startdatetime' : iIiIIIIIii . strftime ( '%Y-%m-%d %H:%M' )
 , 'enddatetime' : OOo0 . strftime ( '%Y-%m-%d %H:%M' )
 }
   oO0Oo = '/live/epgs'
   if 18 - 18: ooOoO0o * OoOoOO00 . iII111i / I1ii11iIi11i / i11iIiiIii
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1iI1iIi111i ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
   OoOo = oO0OOoO0 [ 'list' ]
   if 35 - 35: ooOoO0o * OOooOOo . I11i * o0oOOo0O0Ooo . OoOoOO00 / O0
   if 100 - 100: I1Ii111 . o0oOOo0O0Ooo * Oo0Ooo % O0 * O0
   for oOOo0 in OoOo :
    II = ''
    if 44 - 44: II111iiii / iII111i / I11i % II111iiii / i1IIi . Ii1I
    for oOO in oOOo0 [ 'list' ] :
     if II : II += '\n'
     II += oOO [ 'title' ] + '\n'
     II += ' [%s ~ %s]' % ( oOO [ 'starttime' ] [ - 5 : ] , oOO [ 'endtime' ] [ - 5 : ] ) + '\n'
     if 54 - 54: I1IiiI / iIii1I11I1II1 / OOooOOo . OOooOOo % iII111i . I1IiiI
     if 10 - 10: o0oOOo0O0Ooo + OOooOOo
     if 27 - 27: OoO0O00 . I11i + OoOoOO00 / iIii1I11I1II1 % iII111i . ooOoO0o
    I11ii1i1 [ oOOo0 [ 'channelid' ] ] = unicode ( II )
    if 14 - 14: oO0o + I1ii11iIi11i - iII111i / O0 . I1Ii111
    if 45 - 45: I1Ii111
    if 83 - 83: OoOoOO00 . OoooooooOO
  except Exception as OO00o :
   print ( OO00o )
   if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
  return I11ii1i1
  if 62 - 62: OoO0O00 / I1ii11iIi11i
  if 7 - 7: OoooooooOO . IiII
 def GetStreamingURL ( self , contentid , contenttype , quality_int ) :
  O000OOO0OOo = i1i1I111iIi1 = oo00O00oO000o = OOo00OoO = ''
  iIi1 = [ ]
  if 21 - 21: I11i
  if 92 - 92: i11iIiiIii / I1Ii111 - iII111i % ooOoO0o * I1Ii111 + Oo0Ooo
  try :
   if contenttype == 'channel' :
    oO0Oo = '/live/channels/' + contentid
    ii1 = 'live'
   elif contenttype == 'movie' :
    oO0Oo = '/cf/movie/contents/' + contentid
    ii1 = 'movie'
   else :
    oO0Oo = '/cf/vod/contents/' + contentid
    ii1 = 'vod'
    if 80 - 80: OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / I1IiiI / OOooOOo
   IiI1i11iii1 = self . GetDefaultParams ( )
   Oo00OOOOO = self . MakeServiceUrl ( oO0Oo , IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 13 - 13: I1Ii111 * ooOoO0o + i11iIiiIii * I1Ii111 - ooOoO0o
   Ii1i1i1i1I1Ii = oO0OOoO0 [ 'qualities' ] [ 'list' ]
   if Ii1i1i1i1I1Ii == None : return ( O000OOO0OOo , i1i1I111iIi1 , oo00O00oO000o , OOo00OoO )
   if 25 - 25: II111iiii
   i111II = 'hls'
   if 'drms' in oO0OOoO0 :
    if oO0OOoO0 [ 'drms' ] :
     i111II = 'dash'
     if 55 - 55: OoOoOO00
   print ( i111II )
   if 87 - 87: OoooooooOO % iII111i . I1IiiI / ooOoO0o
   if 'type' in oO0OOoO0 :
    if oO0OOoO0 [ 'type' ] == 'onair' :
     ii1 = 'onairvod'
     if 8 - 8: I11i + o0oOOo0O0Ooo
     if 90 - 90: I1ii11iIi11i
   for o0 in Ii1i1i1i1I1Ii :
    iIi1 . append ( int ( o0 . get ( 'id' ) . rstrip ( 'p' ) ) )
    if 17 - 17: iIii1I11I1II1 . OoooooooOO / I11i % II111iiii % i1IIi / i11iIiiIii
  except Exception as OO00o :
   return ( O000OOO0OOo , i1i1I111iIi1 , oo00O00oO000o , OOo00OoO )
   if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
   if 85 - 85: OoOoOO00 + OOooOOo
   if 10 - 10: IiII / OoO0O00 + OoOoOO00 / i1IIi
  try :
   i1iII1II11I = self . CheckQuality ( quality_int , iIi1 )
   oO0Oo = '/streaming'
   I1iI1iIi111i = { 'contentid' : contentid
 , 'contenttype' : ii1
 , 'action' : i111II
 , 'quality' : str ( i1iII1II11I ) + 'p'
 , 'deviceModelId' : 'Windows 10'
 , 'guid' : self . GetGUID ( guidType = 2 )
 , 'lastplayid' : self . guid
 , 'authtype' : 'cookie'
 , 'isabr' : 'y'
 , 'ishevc' : 'n'
 }
   if 54 - 54: IiII + O0 + I11i * I1Ii111 - OOooOOo % oO0o
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( IiI1i11iii1 ) + '&' + urllib . urlencode ( I1iI1iIi111i )
   if 13 - 13: ooOoO0o / iII111i * OoO0O00 . OoO0O00 * ooOoO0o
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 63 - 63: I1Ii111 / O0 * Oo0Ooo + II111iiii / IiII + Ii1I
   O000OOO0OOo = oO0OOoO0 [ 'playurl' ]
   if O000OOO0OOo == None : return None
   i1i1I111iIi1 = oO0OOoO0 [ 'awscookie' ]
   oo00O00oO000o = oO0OOoO0 [ 'drm' ]
   if 'previewmsg' in oO0OOoO0 [ 'preview' ] : OOo00OoO = oO0OOoO0 [ 'preview' ] [ 'previewmsg' ]
   if 63 - 63: OoO0O00 + I1ii11iIi11i . I1Ii111 % I1Ii111
  except Exception as OO00o :
   print ( OO00o )
   if 57 - 57: II111iiii
  O000OOO0OOo = O000OOO0OOo . replace ( 'pooq.co.kr' , 'wavve.com' )
  if 54 - 54: Oo0Ooo + oO0o + i11iIiiIii
  return ( O000OOO0OOo , i1i1I111iIi1 , oo00O00oO000o , OOo00OoO )
  if 28 - 28: oO0o
  if 70 - 70: IiII
  if 34 - 34: I1Ii111 % IiII
  if 3 - 3: II111iiii / OOooOOo + IiII . ooOoO0o . OoO0O00
  if 83 - 83: oO0o + OoooooooOO
  if 22 - 22: Ii1I % iII111i * OoooooooOO - o0oOOo0O0Ooo / iIii1I11I1II1
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
