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
  self . CREDENTIAL = 'none'
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
   i11i1 = OOOO [ 'credential' ]
   if 29 - 29: I1ii11iIi11i % I1IiiI + Oo0ooO0oo0oO / o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
   if 42 - 42: Ii1I + oO0o
   if user_pf != 0 :
    oo = { 'id' : i11i1
 , 'password' : ''
 , 'profile' : str ( user_pf )
 , 'pushid' : ''
 , 'type' : 'credential'
 }
    if 76 - 76: O0oo0OO0 - OoO0O00
    II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 , postdata = urllib . urlencode ( oo ) )
    OOOO = json . loads ( II1Iiii1111i )
    i11i1 = OOOO [ 'credential' ]
    if 70 - 70: Oo0ooO0oo0oO
    if 61 - 61: I1ii11iIi11i . I1ii11iIi11i
   if i11i1 : I1II1III11iii = True
   if 10 - 10: OoOoOO00 * iii1I1I . I11i + II111iiii - Oo0ooO0oo0oO * i1IIi
   if 56 - 56: o0oOOo0O0Ooo * O00oOoOoO0o0O * II111iiii
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   i11i1 = 'none'
   if 46 - 46: OOooOOo / I1ii11iIi11i
  self . SaveCredential ( i11i1 )
  return I1II1III11iii
  if 24 - 24: I11i . iii1I1I % OOooOOo + Oo0ooO0oo0oO % OoOoOO00
 def GetIssue ( self ) :
  I11III1II = False
  try :
   Oo000 = '/guid/issue'
   O0O00Ooo = self . GetDefaultParams ( )
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   if 16 - 16: I1IiiI * oO0o % O00oOoOoO0o0O
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   if 86 - 86: I1IiiI + Ii1I % i11iIiiIii * oO0o . Oo0ooO0oo0oO * I11i
   OOOO = json . loads ( II1Iiii1111i )
   i1I11i1iI = OOOO [ 'guid' ]
   I1ii1Ii1 = OOOO [ 'guidtimestamp' ]
   if i1I11i1iI : I11III1II = True
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   i1I11i1iI = 'none'
   I1ii1Ii1 = 'none'
   if 15 - 15: II111iiii / iii1I1I . O0oo0OO0
  self . guid = i1I11i1iI
  self . guidtimestamp = I1ii1Ii1
  if 68 - 68: OoO0O00
  return I11III1II
  if 35 - 35: OoO0O00 - iii1I1I / Oo0Ooo / OoOoOO00
 def GetGnList ( self , gn_str ) :
  I1i1IiI1 = [ ]
  try :
   Oo000 = '/cf/supermultisections/' + gn_str
   O0O00Ooo = self . GetDefaultParams ( )
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   if 75 - 75: oO0o
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 50 - 50: Ii1I / Oo0Ooo - oO0o - I11i % iii1I1I - oO0o
   if not ( 'multisectionlist' in OOOO ) : return None
   OOO0o = OOOO [ 'multisectionlist' ]
   if 30 - 30: iIii1I11I1II1 / Oo0ooO0oo0oO - O0oo0OO0 - II111iiii % iii1I1I
   if 49 - 49: I1IiiI % Oo0ooO0oo0oO . Oo0ooO0oo0oO . I11i * Oo0ooO0oo0oO
   for O0oOO0 in OOO0o :
    O0ooo0O0oo0 = O0oOO0 [ 'title' ]
    if len ( O0ooo0O0oo0 ) == 0 : continue
    if O0ooo0O0oo0 == 'minor' : continue
    if 91 - 91: iIii1I11I1II1 + O0oo0OO0
    if re . search ( u'베너' , O0ooo0O0oo0 ) : continue
    if 31 - 31: O00oOoOoO0o0O . OoOoOO00 . OOooOOo
    O0ooo0O0oo0 = re . sub ( '\n|\!|\~|(@0@)|(@\^0@)' , '' , O0ooo0O0oo0 )
    O0ooo0O0oo0 = O0ooo0O0oo0 . lstrip ( '#' )
    if 75 - 75: I11i + OoO0O00 . OoOoOO00 . Oo0ooO0oo0oO + Oo0Ooo . OoO0O00
    for O0O in O0oOO0 [ 'eventlist' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , O0O ) :
      ooo0OO = { 'title' : unicode ( O0ooo0O0oo0 )
 , 'uicode' : re . sub ( r'uicode:' , '' , O0O )
 }
      I1i1IiI1 . append ( ooo0OO )
      break
      if 65 - 65: Ii1I . iIii1I11I1II1 / O0 - Ii1I
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   if 21 - 21: I1IiiI * iIii1I11I1II1
  return I1i1IiI1
  if 91 - 91: O00oOoOoO0o0O
 def GetDeeplinkList ( self , gn_str , came_str , page_int , addinfoyn = False ) :
  iiIii = [ ]
  ooo0O = oOoO0o00OO0 = 1
  i1I1ii = 'quick'
  oOOo0 = oo00O00oO = iIiIIIi = ''
  ooo00OOOooO = False
  O00OOOoOoo0O = { }
  if 77 - 77: iii1I1I % iii1I1I * oO0o - i11iIiiIii
  try :
   if 93 - 93: OoooooooOO / I1IiiI % i11iIiiIii + I1ii11iIi11i * OoO0O00
   Oo000 = '/cf/deeplink/' + gn_str
   O0O00Ooo = self . GetDefaultParams ( )
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 15 - 15: I11i . OoO0O00 / Oo0Ooo + I11i
   if not ( 'url' in OOOO ) : return None
   OooOOOOo = OOOO [ 'url' ]
   if 76 - 76: OoO0O00
   print OooOOOOo
   if 29 - 29: OOooOOo + Oo0Ooo . i11iIiiIii - i1IIi / iIii1I11I1II1
   if 26 - 26: I11i . OoooooooOO
   Oo000 = urlparse . urlsplit ( OooOOOOo ) . path
   I11i1ii1 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( OooOOOOo ) . query ) )
   if 87 - 87: I11i - iIii1I11I1II1 + I1IiiI . iii1I1I
   I11i1ii1 [ 'came' ] = came_str
   I11i1ii1 [ 'limit' ] = str ( self . LIST_LIMIT )
   if 'contenttype' in I11i1ii1 : i1I1ii = I11i1ii1 [ 'contenttype' ]
   if came_str == 'movie' : I11i1ii1 [ 'mtype' ] = 'svod'
   if 62 - 62: O0 * i1IIi * o0oOOo0O0Ooo - I1IiiI + I1IiiI
   if page_int != 1 :
    I11i1ii1 [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
    I11i1ii1 [ 'page' ] = str ( page_int )
    if 34 - 34: iIii1I11I1II1 - o0oOOo0O0Ooo
   IiIIIiI1I1 = self . HTTPTAG + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   if 91 - 91: iii1I1I % i1IIi % iIii1I11I1II1
   if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
   if 45 - 45: oO0o - O00oOoOoO0o0O - OoooooooOO - OoO0O00 . II111iiii / O0
   if 51 - 51: O0 + iii1I1I
   if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
   if 48 - 48: O0
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
   if 41 - 41: Ii1I - O0 - O0
   if not ( 'celllist' in OOOO [ 'cell_toplist' ] ) : return iiIii , ooo00OOOooO
   oO00OOoO00 = OOOO [ 'cell_toplist' ] [ 'celllist' ]
   if 40 - 40: I1IiiI * Ii1I + OOooOOo % iii1I1I
   if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + O0oo0OO0 / OoOoOO00
   if 23 - 23: O0
   if ( i1I1ii == 'channel' and came_str == 'live' ) :
    if ( 'genre' in I11i1ii1 ) :
     o00oO0oOo00 = I11i1ii1 [ 'genre' ]
    else :
     o00oO0oOo00 = 'all'
    print "*epgcall*"
    O00OOOoOoo0O = self . GetEPGList ( o00oO0oOo00 )
    if 81 - 81: OoO0O00
    if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iii1I1I / OoOoOO00
    if 84 - 84: Oo0ooO0oo0oO * II111iiii + Oo0Ooo
   for O0oOO0 in oO00OOoO00 :
    O0ooO0Oo00o = ooO0oOOooOo0 = i1I1ii11i1Iii = ''
    if 26 - 26: I11i - iIii1I11I1II1 - I1IiiI / OoO0O00 . OoOoOO00 % iIii1I11I1II1
    O0ooO0Oo00o = O0oOO0 . get ( 'title_list' ) [ 0 ] . get ( 'text' )
    if ( len ( O0oOO0 . get ( 'title_list' ) ) > 1 ) :
     if ( O0oOO0 . get ( 'title_list' ) [ 1 ] . get ( 'text' ) . startswith ( '@' ) ) :
      for OO in O0oOO0 . get ( 'bottom_taglist' ) :
       if OO == 'playy' or OO == 'won' : ooO0oOOooOo0 = OO
     else :
      ooO0oOOooOo0 = O0oOO0 . get ( 'title_list' ) [ 1 ] . get ( 'text' )
      ooO0oOOooOo0 = re . sub ( r'(\$O\$)|(\&[a-z]{2}\;)' , '' , ooO0oOOooOo0 )
    if ( O0oOO0 . get ( 'thumbnail' ) != '' ) : i1I1ii11i1Iii = 'https://%s' % O0oOO0 . get ( 'thumbnail' )
    if 25 - 25: OoO0O00
    oOo0oO = O0oOO0 [ 'event_list' ] [ 1 ] . get ( 'url' )
    OOOO0oo0 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( oOo0oO ) . query ) )
    if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
    if re . search ( u'programid=\&' , oOo0oO ) and ( 'contentid' in OOOO0oo0 ) :
     oOOo0 = OOOO0oo0 [ 'contentid' ]
     oo00O00oO = 'direct'
    elif ( 'contentid' in OOOO0oo0 ) :
     oOOo0 = OOOO0oo0 [ 'contentid' ]
     oo00O00oO = 'contentid'
    elif ( 'programid' in OOOO0oo0 ) :
     oOOo0 = OOOO0oo0 [ 'programid' ]
     oo00O00oO = 'programid'
     i1I1ii = 'program'
    elif ( 'channelid' in OOOO0oo0 ) :
     oOOo0 = OOOO0oo0 [ 'channelid' ]
     oo00O00oO = 'channelid'
     if 47 - 47: iii1I1I - Ii1I . II111iiii + OoooooooOO . i11iIiiIii
     if oOOo0 in O00OOOoOoo0O :
      iIiIIIi = O00OOOoOoo0O [ oOOo0 ]
     else :
      iIiIIIi = ''
      if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
    elif ( 'movieid' in OOOO0oo0 ) :
     oOOo0 = OOOO0oo0 [ 'movieid' ]
     oo00O00oO = 'movieid'
     if 87 - 87: Oo0Ooo . O00oOoOoO0o0O
     i1I1ii = 'movie'
    else :
     oOOo0 = '-'
     oo00O00oO = '-'
     if 75 - 75: Oo0ooO0oo0oO + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iii1I1I
    oO = { }
    oO [ 'mpaa' ] = O0oOO0 . get ( 'age' )
    try :
     if ( 'channelid' in OOOO0oo0 ) :
      oO [ 'mediatype' ] = 'video'
      oO [ 'title' ] = '%s < %s >' % ( unicode ( O0ooO0Oo00o ) , unicode ( ooO0oOOooOo0 ) )
      oO [ 'tvshowtitle' ] = unicode ( ooO0oOOooOo0 )
      oO [ 'studio' ] = unicode ( O0ooO0Oo00o )
     elif ( 'movieid' in OOOO0oo0 ) :
      oO [ 'mediatype' ] = 'movie'
      oO [ 'title' ] = unicode ( title_list )
     else :
      oO [ 'mediatype' ] = 'episode'
      oO [ 'title' ] = unicode ( title_list )
    except :
     None
     if 31 - 31: OOooOOo + i11iIiiIii + Oo0Ooo * Oo0ooO0oo0oO
    ooo0OO = { 'title' : unicode ( O0ooO0Oo00o )
 , 'subtitle' : unicode ( ooO0oOOooOo0 )
 , 'thumbnail' : i1I1ii11i1Iii
 , 'uicode' : i1I1ii
 , 'contentid' : oOOo0
 , 'contentidType' : oo00O00oO
 , 'viewage' : O0oOO0 . get ( 'age' )
 , 'channelepg' : iIiIIIi
 , 'info' : oO
 }
    iiIii . append ( ooo0OO )
    if 28 - 28: O0 * Oo0Ooo - OOooOOo % iIii1I11I1II1 * Ii1I - i11iIiiIii
   ooo0O = int ( OOOO [ 'cell_toplist' ] [ 'pagecount' ] )
   if OOOO [ 'cell_toplist' ] [ 'count' ] : oOoO0o00OO0 = int ( OOOO [ 'cell_toplist' ] [ 'count' ] )
   else : oOoO0o00OO0 = self . LIST_LIMIT
   if 7 - 7: Oo0Ooo + oO0o - O0oo0OO0 % Ii1I + I1ii11iIi11i
   if 53 - 53: i1IIi - I11i . OoOoOO00
   ooo00OOOooO = ooo0O > oOoO0o00OO0
   if 39 - 39: II111iiii / Oo0ooO0oo0oO + O0oo0OO0 / OoOoOO00
   if 13 - 13: O00oOoOoO0o0O + O0 + iii1I1I % I1IiiI / o0oOOo0O0Ooo . O00oOoOoO0o0O
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   if 86 - 86: oO0o * o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
  try :
   if iiIii [ 0 ] . get ( 'contentidType' ) == 'movieid' and addinfoyn == True :
    Oo0O0oooo = [ ]
    I111iI = { }
    if 56 - 56: I1IiiI
    for O0oO in iiIii : Oo0O0oooo . append ( O0oO . get ( 'contentid' ) )
    if 73 - 73: I1ii11iIi11i * i11iIiiIii % oO0o . I1ii11iIi11i
    I111iI = self . GetMovieInfoList ( Oo0O0oooo )
    if 66 - 66: oO0o + oO0o + Oo0ooO0oo0oO / iii1I1I + OOooOOo
    for O0O00o0OOO0 in range ( len ( iiIii ) ) :
     iiIii [ O0O00o0OOO0 ] [ 'info' ] = I111iI . get ( iiIii [ O0O00o0OOO0 ] [ 'contentid' ] )
  except :
   None
   if 30 - 30: O0
   if 44 - 44: oO0o / I11i / I11i
   if 87 - 87: Oo0Ooo . I1IiiI - II111iiii + O0 / Oo0Ooo / oO0o
  return ( iiIii , ooo00OOOooO )
  if 25 - 25: I1IiiI . I1IiiI - OoOoOO00 % OoOoOO00 - i11iIiiIii / O0oo0OO0
  if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * O00oOoOoO0o0O
 def GetEpisodeList ( self , contentid , contenttype , contentidType , page_int , orderby = 'desc' ) :
  OOOoOo = [ ]
  ooo0O = oOoO0o00OO0 = 1
  ooo00OOOooO = False
  if 51 - 51: Oo0ooO0oo0oO / iIii1I11I1II1 % Oo0Ooo * I1IiiI % O0oo0OO0
  if orderby == 'desc' :
   orderby = 'new'
  else :
   orderby = 'old'
   if 76 - 76: o0oOOo0O0Ooo - i11iIiiIii
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if 14 - 14: OoOoOO00 + oO0o
   if 52 - 52: OoooooooOO - Oo0ooO0oo0oO
   if contentidType == 'contentid' :
    Oo000 = '/cf/vod/contents/' + contentid
    if 74 - 74: iii1I1I + o0oOOo0O0Ooo
    IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
    II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
    OOOO = json . loads ( II1Iiii1111i )
    if 71 - 71: Oo0Ooo % OOooOOo
    if not ( 'programid' in OOOO ) : return None
    O00oO000O0O = OOOO [ 'programid' ]
    if 18 - 18: iii1I1I - OOooOOo . O0oo0OO0 . iIii1I11I1II1
   else :
    O00oO000O0O = contentid
    if 2 - 2: OOooOOo . OoO0O00
    if 78 - 78: I11i * iIii1I11I1II1 . I1IiiI / o0oOOo0O0Ooo - OoooooooOO / O0oo0OO0
    if 35 - 35: I11i % OOooOOo - oO0o
   Oo000 = '/vod/programs-contents/' + O00oO000O0O
   if 20 - 20: i1IIi - Oo0ooO0oo0oO
   I11i1ii1 = { 'limit' : self . EP_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . EP_LIMIT )
 , 'orderby' : orderby
   }
   if 30 - 30: I11i / I1IiiI
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 35 - 35: II111iiii % OOooOOo . Oo0ooO0oo0oO + Oo0ooO0oo0oO % II111iiii % II111iiii
   if not ( 'list' in OOOO ) : return None
   ooOoO00 = OOOO [ 'list' ]
   if 14 - 14: i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
   if 72 - 72: Ii1I
   for O0oOO0 in ooOoO00 :
    II11Ii1iI1iII = O0oOO0 . get ( 'programtitle' )
    Oo0o00OO0000 = '%s회, %s(%s)' % ( O0oOO0 . get ( 'episodenumber' ) , O0oOO0 . get ( 'releasedate' ) , O0oOO0 . get ( 'releaseweekday' ) )
    if ( O0oOO0 . get ( 'image' ) != '' ) : I1i = 'https://%s' % O0oOO0 . get ( 'image' )
    if 99 - 99: O0oo0OO0 + OoOoOO00 * iIii1I11I1II1 / OoooooooOO
    i11I = unicode ( O0oOO0 . get ( 'synopsis' ) )
    i11I = re . sub ( u'(\<[a-zA-Z]{1,2}\>)|(\<\/[a-zA-Z]{1,2}\>)' , '' , i11I )
    if 76 - 76: O00oOoOoO0o0O * iii1I1I
    oO = { }
    oO [ 'title' ] = unicode ( II11Ii1iI1iII )
    oO [ 'mediatype' ] = 'episode'
    oO [ 'mpaa' ] = O0oOO0 . get ( 'targetage' )
    try :
     if 'episodenumber' in O0oOO0 : oO [ 'episode' ] = O0oOO0 . get ( 'episodenumber' )
     if 'releasedate' in O0oOO0 : oO [ 'year' ] = int ( O0oOO0 . get ( 'releasedate' ) [ : 4 ] )
     if 'releasedate' in O0oOO0 : oO [ 'aired' ] = O0oOO0 . get ( 'releasedate' )
     if 'playtime' in O0oOO0 : oO [ 'duration' ] = O0oOO0 . get ( 'playtime' )
     if 'episodeactors' in O0oOO0 :
      if O0oOO0 . get ( 'episodeactors' ) != '' : oO [ 'cast' ] = O0oOO0 . get ( 'episodeactors' ) . split ( ',' )
    except :
     None
     if 52 - 52: OOooOOo
    iiii1 = { 'title' : unicode ( II11Ii1iI1iII )
 , 'subtitle' : unicode ( Oo0o00OO0000 )
 , 'thumbnail' : I1i
 , 'uicode' : contenttype
 , 'contentid' : O0oOO0 . get ( 'contentid' )
 , 'programid' : O0oOO0 . get ( 'programid' )
 , 'synopsis' : i11I
 , 'viewage' : O0oOO0 . get ( 'targetage' )
 , 'info' : oO
    }
    OOOoOo . append ( iiii1 )
    if 96 - 96: i11iIiiIii % OOooOOo
   ooo0O = int ( OOOO [ 'pagecount' ] )
   if OOOO [ 'count' ] : oOoO0o00OO0 = int ( OOOO [ 'count' ] )
   else : oOoO0o00OO0 = self . EP_LIMIT
   if 70 - 70: iIii1I11I1II1
   ooo00OOOooO = ooo0O > oOoO0o00OO0
   if 31 - 31: O00oOoOoO0o0O - I1IiiI % iIii1I11I1II1
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   if 92 - 92: i1IIi - iIii1I11I1II1
  return ( OOOoOo , ooo00OOOooO )
  if 16 - 16: OoO0O00 - OoOoOO00 - OOooOOo - i1IIi / Ii1I
  if 88 - 88: OoO0O00
 def GetMyviewList ( self , contenttype , page_int , addinfoyn = False ) :
  ooOOOooO = [ ]
  ooo0O = oOoO0o00OO0 = 1
  ooo00OOOooO = False
  if 12 - 12: O0 - o0oOOo0O0Ooo
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if 81 - 81: OoOoOO00 - OoOoOO00 . iii1I1I
   Oo000 = '/myview/contents'
   if 73 - 73: I11i % i11iIiiIii - I1IiiI
   I11i1ii1 = { 'contenttype' : contenttype
 , 'limit' : self . MV_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . MV_LIMIT )
 , 'orderby' : 'new'
 }
   if 7 - 7: O0 * i11iIiiIii * Ii1I + Oo0ooO0oo0oO % OoO0O00 - Oo0ooO0oo0oO
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
   if not ( 'list' in OOOO [ 0 ] ) : return None
   ii = OOOO [ 0 ] [ 'list' ]
   if 68 - 68: iii1I1I - I1IiiI / O0oo0OO0 / I11i
   for O0oOO0 in ii :
    oO = { }
    if 12 - 12: Ii1I + i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . I11i
    if contenttype == 'vod' :
     II11Ii1iI1iII = O0oOO0 . get ( 'programtitle' )
     Oo0o00OO0000 = '%s회, %s' % ( O0oOO0 . get ( 'episodenumber' ) , O0oOO0 . get ( 'releasedate' ) )
     oOOo0 = O0oOO0 . get ( 'contentid' )
     O00oO000O0O = O0oOO0 . get ( 'programid' )
     if 5 - 5: i1IIi + O00oOoOoO0o0O / o0oOOo0O0Ooo . iii1I1I / I11i
     oO [ 'title' ] = unicode ( II11Ii1iI1iII )
     oO [ 'mediatype' ] = 'episode'
     oO [ 'mpaa' ] = O0oOO0 . get ( 'targetage' )
     try :
      oO [ 'studio' ] = O0oOO0 . get ( 'channelname' )
     except :
      None
     try :
      if 'releasedate' in O0oOO0 : oO [ 'year' ] = int ( O0oOO0 . get ( 'releasedate' ) [ : 4 ] )
      if 'releasedate' in O0oOO0 : oO [ 'aired' ] = O0oOO0 . get ( 'releasedate' )
     except :
      None
      if 32 - 32: I1IiiI % iIii1I11I1II1 / i1IIi - I1IiiI
      if 7 - 7: O0oo0OO0 * OoO0O00 - Oo0ooO0oo0oO + OOooOOo * I1IiiI % OoO0O00
    else :
     II11Ii1iI1iII = O0oOO0 . get ( 'title' )
     Oo0o00OO0000 = ''
     oOOo0 = O00oO000O0O = O0oOO0 . get ( 'movieid' )
     if 15 - 15: OoOoOO00 % I1IiiI * I11i
     oO [ 'title' ] = unicode ( II11Ii1iI1iII )
     oO [ 'mediatype' ] = 'movie'
     oO [ 'mpaa' ] = O0oOO0 . get ( 'targetage' )
     try :
      if 'releasedate' in O0oOO0 : oO [ 'year' ] = int ( O0oOO0 . get ( 'releasedate' ) [ : 4 ] )
      if 'releasedate' in O0oOO0 : oO [ 'aired' ] = O0oOO0 . get ( 'releasedate' )
     except :
      None
      if 81 - 81: Oo0ooO0oo0oO - iIii1I11I1II1 - i1IIi / O0oo0OO0 - O0 * I11i
      if 20 - 20: oO0o % O00oOoOoO0o0O
    if ( O0oOO0 . get ( 'image' ) != '' ) : I1i = 'https://%s' % O0oOO0 . get ( 'image' )
    if 19 - 19: I1ii11iIi11i % O00oOoOoO0o0O + Oo0ooO0oo0oO / O0oo0OO0 . Oo0ooO0oo0oO
    IiIi1I1 = { 'title' : unicode ( II11Ii1iI1iII )
 , 'subtitle' : unicode ( Oo0o00OO0000 )
 , 'thumbnail' : I1i
 , 'uicode' : contenttype
 , 'contentid' : oOOo0
 , 'programid' : O00oO000O0O
 , 'viewage' : O0oOO0 . get ( 'targetage' )
 , 'info' : oO
 }
    if 39 - 39: II111iiii + OoOoOO00 - Oo0ooO0oo0oO . OoOoOO00
    ooOOOooO . append ( IiIi1I1 )
    if 84 - 84: OoO0O00 + i1IIi - II111iiii . I1ii11iIi11i * OoooooooOO + I1IiiI
    if 38 - 38: OOooOOo + II111iiii % Oo0ooO0oo0oO % OoOoOO00 - Ii1I / OoooooooOO
   ooo0O = int ( OOOO [ 0 ] [ 'pagecount' ] )
   if OOOO [ 0 ] [ 'count' ] : oOoO0o00OO0 = int ( OOOO [ 0 ] [ 'count' ] )
   else : oOoO0o00OO0 = self . MV_LIMIT
   if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
   ooo00OOOooO = ooo0O > oOoO0o00OO0
   if 85 - 85: Ii1I % iii1I1I + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
   if 28 - 28: iii1I1I . iii1I1I % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iii1I1I
   if 27 - 27: OoO0O00 + Oo0ooO0oo0oO - i1IIi
  try :
   if contenttype == 'movie' and addinfoyn == True :
    Oo0O0oooo = [ ]
    I111iI = { }
    if 69 - 69: O00oOoOoO0o0O - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
    for O0oO in ooOOOooO : Oo0O0oooo . append ( O0oO . get ( 'contentid' ) )
    if 79 - 79: O0 * i11iIiiIii - O00oOoOoO0o0O / O00oOoOoO0o0O
    I111iI = self . GetMovieInfoList ( Oo0O0oooo )
    if 48 - 48: O0
    for O0O00o0OOO0 in range ( len ( ooOOOooO ) ) :
     ooOOOooO [ O0O00o0OOO0 ] [ 'info' ] = I111iI . get ( ooOOOooO [ O0O00o0OOO0 ] [ 'contentid' ] )
  except :
   None
   if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
   if 25 - 25: O00oOoOoO0o0O + Ii1I / Oo0ooO0oo0oO . o0oOOo0O0Ooo % O0 * OoO0O00
   if 84 - 84: Oo0ooO0oo0oO % Ii1I + i11iIiiIii
  return ooOOOooO , ooo00OOOooO
  if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
  if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
 def GetSearchList ( self , search_key , genre , page_int , exclusion21 = False , addinfoyn = False ) :
  iIiIiIiI = [ ]
  ooo0O = oOoO0o00OO0 = 1
  ooo00OOOooO = False
  if 30 - 30: O0oo0OO0 . Oo0ooO0oo0oO * I1ii11iIi11i
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if 17 - 17: I1IiiI . O0 + OoO0O00
   Oo000 = '/cf/search/list.js'
   if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
   I11i1ii1 = { 'type' : 'program' if genre == 'vod' else 'movie'
 , 'keyword' : search_key
 , 'offset' : str ( ( page_int - 1 ) * self . LIST_LIMIT )
 , 'limit' : self . LIST_LIMIT
   , 'orderby' : 'score'
 , 'isplayymovie' : 'y'
 }
   if 20 - 20: I1IiiI
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   if 95 - 95: iii1I1I - I1IiiI
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 34 - 34: Oo0ooO0oo0oO * I1IiiI . i1IIi * Oo0ooO0oo0oO / Oo0ooO0oo0oO
   if not ( 'celllist' in OOOO [ 'cell_toplist' ] ) : return iIiIiIiI , ooo00OOOooO
   IIiI1Ii = OOOO [ 'cell_toplist' ] [ 'celllist' ]
   if 57 - 57: OOooOOo - Oo0ooO0oo0oO - I11i + OoO0O00
   if 30 - 30: Ii1I % OoOoOO00 + i1IIi - I11i - Ii1I
   for O0oOO0 in IIiI1Ii :
    oO = { }
    if 8 - 8: OoO0O00 + O0oo0OO0 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
    II11Ii1iI1iII = O0oOO0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if ( O0oOO0 . get ( 'thumbnail' ) != '' ) : I1i = 'https://%s' % O0oOO0 . get ( 'thumbnail' )
    if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + Oo0ooO0oo0oO
    for O0O in O0oOO0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , O0O ) :
      if genre == 'vod' :
       oOOo0 = ''
       O00oO000O0O = re . sub ( r'uicode:' , '' , O0O )
       oO [ 'mediatype' ] = 'episode'
       if 44 - 44: II111iiii
      else :
       oOOo0 = re . sub ( r'uicode:' , '' , O0O )
       O00oO000O0O = ''
       if O0oOO0 . get ( 'bottom_taglist' ) [ 0 ] == 'playy' :
        II11Ii1iI1iII += ' [playy]'
       oO [ 'mediatype' ] = 'movie'
       if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
       if 35 - 35: iIii1I11I1II1
      oO [ 'title' ] = unicode ( O0oOO0 [ 'title_list' ] [ 0 ] [ 'text' ] )
      oO [ 'mpaa' ] = O0oOO0 . get ( 'age' )
      if 42 - 42: O0oo0OO0 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
      IiIi1I1 = { 'title' : unicode ( II11Ii1iI1iII )
 , 'thumbnail' : I1i
 , 'uicode' : genre
 , 'contentid' : oOOo0
 , 'programid' : O00oO000O0O
 , 'viewage' : O0oOO0 . get ( 'age' )
 , 'info' : oO
 }
      if 31 - 31: iii1I1I . OOooOOo - Oo0ooO0oo0oO . OoooooooOO / OoooooooOO
    if exclusion21 == False or O0oOO0 . get ( 'age' ) != '21' :
     iIiIiIiI . append ( IiIi1I1 )
     if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
     if 21 - 21: O0 % O00oOoOoO0o0O . I1IiiI / II111iiii + O00oOoOoO0o0O
   ooo0O = int ( OOOO [ 'cell_toplist' ] [ 'pagecount' ] )
   if OOOO [ 'cell_toplist' ] [ 'count' ] : oOoO0o00OO0 = int ( OOOO [ 'cell_toplist' ] [ 'count' ] )
   else : oOoO0o00OO0 = self . LIST_LIMIT
   if 53 - 53: oO0o - I1IiiI - oO0o * iii1I1I
   ooo00OOOooO = ooo0O > oOoO0o00OO0
   if 71 - 71: O0 - iIii1I11I1II1
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   if 12 - 12: OOooOOo / o0oOOo0O0Ooo
   if 42 - 42: Oo0Ooo
   if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
  try :
   if genre == 'movie' and addinfoyn == True :
    Oo0O0oooo = [ ]
    I111iI = { }
    if 46 - 46: Oo0Ooo
    for O0oO in iIiIiIiI : Oo0O0oooo . append ( O0oO . get ( 'contentid' ) )
    if 1 - 1: iii1I1I
    I111iI = self . GetMovieInfoList ( Oo0O0oooo )
    if 97 - 97: OOooOOo + iii1I1I + O0 + i11iIiiIii
    for O0O00o0OOO0 in range ( len ( iIiIiIiI ) ) :
     iIiIiIiI [ O0O00o0OOO0 ] [ 'info' ] = I111iI . get ( iIiIiIiI [ O0O00o0OOO0 ] [ 'contentid' ] )
  except :
   None
   if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
   if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iii1I1I % iii1I1I + i11iIiiIii
   if 72 - 72: iIii1I11I1II1 * Ii1I % Oo0ooO0oo0oO / OoO0O00
  return iIiIiIiI , ooo00OOOooO
  if 35 - 35: Oo0ooO0oo0oO + i1IIi % I1ii11iIi11i % I11i + oO0o
  if 17 - 17: i1IIi
 def GetGenreGroup ( self , maintype , subtype , orderby , ordernm , exclusion21 = False ) :
  iiIi1i = [ ]
  if 27 - 27: OOooOOo * Oo0ooO0oo0oO . O0oo0OO0 % O00oOoOoO0o0O * O00oOoOoO0o0O . i1IIi
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if 72 - 72: OOooOOo % I1ii11iIi11i + OoO0O00 / oO0o + O00oOoOoO0o0O
   Oo000 = '/cf/filters'
   if 10 - 10: O0oo0OO0 / Oo0ooO0oo0oO + i11iIiiIii / Ii1I
   I11i1ii1 = { 'type' : maintype }
   if 74 - 74: OOooOOo + O0 + i1IIi - i1IIi + II111iiii
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
   if not ( maintype in OOOO ) : return None
   iIi1Ii1i1iI = OOOO [ maintype ]
   if 16 - 16: OOooOOo / Oo0Ooo / OoooooooOO * I1IiiI + i1IIi % OOooOOo
   if subtype == '-' :
    if 71 - 71: OoOoOO00
    for O0oOO0 in iIi1Ii1i1iI :
     ii111IiiI1 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( O0oOO0 . get ( 'url' ) ) . query ) )
     if 11 - 11: iIii1I11I1II1 * Ii1I
     IiIi1I1 = { 'title' : O0oOO0 . get ( 'text' )
 , 'genre' : O0oOO0 . get ( 'id' )
 , 'subgenre' : '-'
 , 'adult' : O0oOO0 . get ( 'adult' )
 , 'broadcastid' : ii111IiiI1 . get ( 'broadcastid' )
 , 'contenttype' : ii111IiiI1 . get ( 'contenttype' )
 , 'uiparent' : ii111IiiI1 . get ( 'uiparent' )
 , 'uirank' : ii111IiiI1 . get ( 'uirank' )
 , 'uitype' : ii111IiiI1 . get ( 'uitype' )
 , 'orderby' : orderby
 , 'ordernm' : ordernm
 }
     if exclusion21 == False or IiIi1I1 . get ( 'adult' ) == 'n' :
      iiIi1i . append ( IiIi1I1 )
      if 76 - 76: Oo0ooO0oo0oO
   else :
    for O0oOO0 in iIi1Ii1i1iI :
     if O0oOO0 . get ( 'id' ) == subtype :
      for II in O0oOO0 [ 'sublist' ] :
       ii111IiiI1 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( II . get ( 'url' ) ) . query ) )
       if 45 - 45: OoooooooOO - OOooOOo + O0 * Ii1I . I1ii11iIi11i
       IiIi1I1 = { 'title' : II . get ( 'text' )
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
       iiIi1i . append ( IiIi1I1 )
      break
      if 39 - 39: iIii1I11I1II1 / O0 / oO0o - Ii1I - iii1I1I % OOooOOo
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   if 31 - 31: I11i - O0 / Oo0ooO0oo0oO * OoOoOO00
  return iiIi1i
  if 12 - 12: o0oOOo0O0Ooo - Oo0ooO0oo0oO * O0oo0OO0
  if 14 - 14: Oo0Ooo - Ii1I % Ii1I * O0 . i11iIiiIii / O0
 def GetGenreGroup_sub ( self , in_params ) :
  iiIi1i = [ ]
  if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if 28 - 28: i1IIi - iii1I1I
   Oo000 = '/cf/vod/newcontents'
   if 54 - 54: iii1I1I - O0 % OOooOOo
   I11i1ii1 = { 'WeekDay' : 'all'
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
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 17 - 17: Ii1I - OoooooooOO % Ii1I . O00oOoOoO0o0O / i11iIiiIii % iii1I1I
   if not ( 'filter_item_list' in OOOO [ 'filter' ] [ 'filterlist' ] [ 1 ] ) : return None
   iIi1Ii1i1iI = OOOO [ 'filter' ] [ 'filterlist' ] [ 1 ] [ 'filter_item_list' ]
   if 28 - 28: I11i
   for O0oOO0 in iIi1Ii1i1iI :
    IiIi1I1 = { 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )

 , 'adult' : O0oOO0 . get ( 'adult' )
 , 'title' : O0oOO0 . get ( 'title' )
 , 'subgenre' : O0oOO0 . get ( 'api_parameters' ) [ O0oOO0 . get ( 'api_parameters' ) . find ( '=' ) + 1 : ]
 , 'orderby' : in_params . get ( 'orderby' )
 }
    iiIi1i . append ( IiIi1I1 )
    if 58 - 58: OoOoOO00
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   if 37 - 37: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i
  return iiIi1i
  if 73 - 73: i11iIiiIii - O00oOoOoO0o0O
  if 25 - 25: OoooooooOO + O00oOoOoO0o0O * I1ii11iIi11i
 def GetGenreList ( self , genre , in_params , page_int , addinfoyn = False ) :
  iiIi1i = [ ]
  ooo0O = oOoO0o00OO0 = 1
  ooo00OOOooO = False
  if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + O0oo0OO0
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if 18 - 18: Oo0ooO0oo0oO * OoOoOO00 . iii1I1I / I1ii11iIi11i / i11iIiiIii
   I11i1ii1 = { 'WeekDay' : 'all'
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
    Oo000 = '/cf/vod/newcontents'
    if 91 - 91: i11iIiiIii / i1IIi + iii1I1I + Oo0ooO0oo0oO * i11iIiiIii
    if in_params . get ( 'subgenre' ) != '-' :
     I11i1ii1 [ 'subgenre' ] = in_params . get ( 'subgenre' )
   else :
    Oo000 = '/cf/movie/contents'
    if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * O0oo0OO0 . O00oOoOoO0o0O
    I11i1ii1 [ 'price' ] = 'all'
    if 52 - 52: Oo0ooO0oo0oO + O0 . iii1I1I . I1ii11iIi11i . OoO0O00
    if 97 - 97: I1IiiI / iii1I1I
    I11i1ii1 [ 'sptheme' ] = 'svod'
    if 71 - 71: II111iiii / i1IIi . I1ii11iIi11i % OoooooooOO . OoOoOO00
    if 41 - 41: i1IIi * II111iiii / OoooooooOO . OOooOOo
   I11i1ii1 [ 'limit' ] = self . LIST_LIMIT
   I11i1ii1 [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
   I11i1ii1 [ 'page' ] = str ( page_int )
   if 83 - 83: iii1I1I . O0 / Oo0Ooo / OOooOOo - II111iiii
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 100 - 100: OoO0O00
   if not ( 'celllist' in OOOO [ 'cell_toplist' ] ) : return None
   iIi1Ii1i1iI = OOOO [ 'cell_toplist' ] [ 'celllist' ]
   if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iii1I1I . iIii1I11I1II1 * iii1I1I
   for O0oOO0 in iIi1Ii1i1iI :
    oO = { }
    II11Ii1iI1iII = I1i = ''
    if 38 - 38: I1ii11iIi11i - iii1I1I / O0 . O0oo0OO0
    II11Ii1iI1iII = O0oOO0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if 45 - 45: O0oo0OO0
    if ( O0oOO0 . get ( 'thumbnail' ) != '' ) : I1i = 'https://%s' % O0oOO0 . get ( 'thumbnail' )
    if 83 - 83: OoOoOO00 . OoooooooOO
    for O0O in O0oOO0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , O0O ) :
      if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / O00oOoOoO0o0O / i11iIiiIii
      oO [ 'title' ] = unicode ( II11Ii1iI1iII )
      oO [ 'mpaa' ] = O0oOO0 . get ( 'age' )
      if genre == 'moviegenre_svod' :
       oO [ 'mediatype' ] = 'movie'
      else :
       oO [ 'mediatype' ] = 'episode'
       if 62 - 62: OoO0O00 / I1ii11iIi11i
       if 7 - 7: OoooooooOO . O00oOoOoO0o0O
      IiIi1I1 = { 'title' : unicode ( II11Ii1iI1iII )
 , 'uicode' : re . sub ( r'uicode:' , '' , O0O )
 , 'thumbnail' : I1i
 , 'viewage' : O0oOO0 . get ( 'age' )
 , 'info' : oO
 }
      if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
    iiIi1i . append ( IiIi1I1 )
    if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
    if 100 - 100: Oo0ooO0oo0oO % iIii1I11I1II1 * II111iiii - iii1I1I
   ooo0O = int ( OOOO [ 'cell_toplist' ] [ 'pagecount' ] )
   if OOOO [ 'cell_toplist' ] [ 'count' ] : oOoO0o00OO0 = int ( OOOO [ 'cell_toplist' ] [ 'count' ] )
   else : oOoO0o00OO0 = self . LIST_LIMIT
   if 92 - 92: Oo0ooO0oo0oO
   ooo00OOOooO = ooo0O > oOoO0o00OO0
   if 22 - 22: Oo0Ooo % iii1I1I * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   if 95 - 95: OoooooooOO - O00oOoOoO0o0O * I1IiiI + OoOoOO00
   if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
   if 92 - 92: I11i . O0oo0OO0
  try :
   if genre == 'moviegenre_svod' and addinfoyn == True :
    Oo0O0oooo = [ ]
    I111iI = { }
    if 85 - 85: I1ii11iIi11i . O0oo0OO0
    for O0oO in iiIi1i : Oo0O0oooo . append ( O0oO . get ( 'uicode' ) )
    if 78 - 78: Oo0ooO0oo0oO * O0oo0OO0 + iIii1I11I1II1 + iIii1I11I1II1 / O0oo0OO0 . Ii1I
    I111iI = self . GetMovieInfoList ( Oo0O0oooo )
    if 97 - 97: Oo0ooO0oo0oO / O0oo0OO0 % i1IIi % I1ii11iIi11i
    for O0O00o0OOO0 in range ( len ( iiIi1i ) ) :
     iiIi1i [ O0O00o0OOO0 ] [ 'info' ] = I111iI . get ( iiIi1i [ O0O00o0OOO0 ] [ 'uicode' ] )
  except :
   None
   if 18 - 18: iIii1I11I1II1 % I11i
   if 95 - 95: Oo0ooO0oo0oO + i11iIiiIii * O0oo0OO0 - i1IIi * O0oo0OO0 - iIii1I11I1II1
   if 75 - 75: OoooooooOO * O00oOoOoO0o0O
  return iiIi1i , ooo00OOOooO
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
   O0O00Ooo = self . GetDefaultParams ( )
   if 37 - 37: OOooOOo / OoooooooOO - i11iIiiIii
   I11i1ii1 = { 'limit' : '100'
 , 'offset' : '0'
 , 'genre' : genre
 , 'startdatetime' : I1iIIIi1 . strftime ( '%Y-%m-%d %H:%M' )
 , 'enddatetime' : Iii . strftime ( '%Y-%m-%d %H:%M' )
 }
   Oo000 = '/live/epgs'
   if 18 - 18: iii1I1I . I1IiiI
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if 40 - 40: O0 - OoooooooOO - O00oOoOoO0o0O
   iIiii = OOOO [ 'list' ]
   if 76 - 76: I1IiiI . Oo0ooO0oo0oO - I1ii11iIi11i - iii1I1I * OoO0O00
   if 54 - 54: O00oOoOoO0o0O + O0 + I11i * O0oo0OO0 - OOooOOo % oO0o
   for O0oOO0 in iIiii :
    I111 = ''
    if 13 - 13: OoO0O00 * oO0o * iii1I1I
    for IiIIiiI11III in O0oOO0 [ 'list' ] :
     if I111 : I111 += '\n'
     I111 += IiIIiiI11III [ 'title' ] + '\n'
     I111 += ' [%s ~ %s]' % ( IiIIiiI11III [ 'starttime' ] [ - 5 : ] , IiIIiiI11III [ 'endtime' ] [ - 5 : ] ) + '\n'
     if 42 - 42: I1ii11iIi11i
     if 76 - 76: I1ii11iIi11i * II111iiii . I1IiiI - Oo0Ooo + oO0o + i11iIiiIii
     if 28 - 28: oO0o
    o0 [ O0oOO0 [ 'channelid' ] ] = unicode ( I111 )
    if 70 - 70: O00oOoOoO0o0O
    if 34 - 34: O0oo0OO0 % O00oOoOoO0o0O
    if 3 - 3: II111iiii / OOooOOo + O00oOoOoO0o0O . Oo0ooO0oo0oO . OoO0O00
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   if 83 - 83: oO0o + OoooooooOO
  return o0
  if 22 - 22: Ii1I % iii1I1I * OoooooooOO - o0oOOo0O0Ooo / iIii1I11I1II1
  if 86 - 86: OoooooooOO . iii1I1I % OoOoOO00 / I11i * iii1I1I / o0oOOo0O0Ooo
 def GetMovieInfoList ( self , movie_list ) :
  oOoOOo000oOoO0 = { }
  if 86 - 86: II111iiii % i11iIiiIii + Ii1I % i11iIiiIii
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   Oo000 = self . API_DOMAIN + '/movie/contents/'
   if 92 - 92: i11iIiiIii - iii1I1I / Oo0ooO0oo0oO / oO0o
   for O0oO in movie_list :
    if 43 - 43: II111iiii + OOooOOo + iii1I1I
    IiIIIiI1I1 = Oo000 + O0oO
    II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
    OOOO = json . loads ( II1Iiii1111i )
    if 40 - 40: o0oOOo0O0Ooo
    oO = { }
    oO [ 'mediatype' ] = 'movie'
    if 67 - 67: oO0o + II111iiii - O0 . oO0o * II111iiii * I11i
    o00 = [ ]
    for OO00O0oOO in OOOO [ 'actors' ] [ 'list' ] : o00 . append ( OO00O0oOO . get ( 'text' ) )
    if o00 [ 0 ] != '' : oO [ 'cast' ] = o00
    if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
    Ooooo00o0OoO = [ ]
    for oooo0O0O0o0 in OOOO [ 'directors' ] [ 'list' ] : Ooooo00o0OoO . append ( oooo0O0O0o0 . get ( 'text' ) )
    if Ooooo00o0OoO [ 0 ] != '' : oO [ 'director' ] = Ooooo00o0OoO
    if 51 - 51: II111iiii + O00oOoOoO0o0O . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
    iiIi1i = [ ]
    for OOoOoo0 in OOOO [ 'genre' ] [ 'list' ] : iiIi1i . append ( OOoOoo0 . get ( 'text' ) )
    if iiIi1i [ 0 ] != '' : oO [ 'genre' ] = iiIi1i
    if 17 - 17: Ii1I + oO0o . OoO0O00 - Oo0Ooo * i11iIiiIii
    if OOOO . get ( 'releasedate' ) != '' :
     oO [ 'year' ] = OOOO [ 'releasedate' ] [ : 4 ]
     oO [ 'aired' ] = OOOO [ 'releasedate' ]
     if 20 - 20: I1IiiI . OoooooooOO % OOooOOo
    oO [ 'country' ] = OOOO [ 'country' ]
    oO [ 'duration' ] = OOOO [ 'playtime' ]
    oO [ 'title' ] = OOOO [ 'title' ]
    oO [ 'mpaa' ] = OOOO [ 'targetage' ]
    oO [ 'plot' ] = OOOO [ 'synopsis' ]
    if 63 - 63: I1IiiI % iIii1I11I1II1
    oOoOOo000oOoO0 [ O0oO ] = oO
    if 39 - 39: iii1I1I / II111iiii / I1ii11iIi11i % I1IiiI
  except Exception as oO0ooO0OoOOOO :
   return { }
   if 89 - 89: O0oo0OO0 + OoooooooOO + O0oo0OO0 * i1IIi + iIii1I11I1II1 % I11i
  return oOoOOo000oOoO0
  if 59 - 59: OOooOOo + i11iIiiIii
  if 88 - 88: i11iIiiIii - Oo0ooO0oo0oO
 def GetStreamingURL ( self , contentid , contenttype , quality_int ) :
  O0iIi1IiII = I1iooo = ii1iiIi1 = i111iiI1ii = ''
  IIiii = [ ]
  if 30 - 30: I11i / Ii1I . O00oOoOoO0o0O . OoooooooOO - Oo0Ooo
  if 44 - 44: O0 * OoooooooOO % Oo0ooO0oo0oO + II111iiii
  try :
   if contenttype == 'channel' :
    Oo000 = '/live/channels/' + contentid
    II1i1i1iII1 = 'live'
   elif contenttype == 'movie' :
    Oo000 = '/cf/movie/contents/' + contentid
    II1i1i1iII1 = 'movie'
   else :
    Oo000 = '/cf/vod/contents/' + contentid
    II1i1i1iII1 = 'vod'
    if 68 - 68: Oo0Ooo + i11iIiiIii
   O0O00Ooo = self . GetDefaultParams ( )
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   if 69 - 69: iIii1I11I1II1 * iIii1I11I1II1 * i11iIiiIii + I1IiiI / OOooOOo % Ii1I
   if 58 - 58: OOooOOo * o0oOOo0O0Ooo + O0 % OOooOOo
   OOOO = self . SESSION . Request2 ( self . API_DOMAIN + Oo000 , params = O0O00Ooo )
   if 25 - 25: Oo0Ooo % I1ii11iIi11i * Oo0ooO0oo0oO
   I11 = OOOO [ 'qualities' ] [ 'list' ]
   if I11 == None : return ( O0iIi1IiII , I1iooo , ii1iiIi1 , i111iiI1ii )
   if 87 - 87: OoOoOO00
   IioO0O = 'hls'
   if 'drms' in OOOO :
    if OOOO [ 'drms' ] :
     IioO0O = 'dash'
     if 86 - 86: OoOoOO00 . iIii1I11I1II1 - OoO0O00
     if 56 - 56: O0
     if 61 - 61: o0oOOo0O0Ooo / OOooOOo / Oo0Ooo * O0
   if 'type' in OOOO :
    if OOOO [ 'type' ] == 'onair' :
     II1i1i1iII1 = 'onairvod'
     if 23 - 23: oO0o - OOooOOo + I11i
     if 12 - 12: I1IiiI / Oo0ooO0oo0oO % o0oOOo0O0Ooo / i11iIiiIii % OoooooooOO
   for IiIi1II11i in I11 :
    IIiii . append ( int ( IiIi1II11i . get ( 'id' ) . rstrip ( 'p' ) ) )
    if 42 - 42: I1ii11iIi11i * OoOoOO00 % Oo0ooO0oo0oO - OoOoOO00 . i11iIiiIii - O0oo0OO0
  except Exception as oO0ooO0OoOOOO :
   return ( O0iIi1IiII , I1iooo , ii1iiIi1 , i111iiI1ii )
   if 84 - 84: O0oo0OO0 - I1ii11iIi11i / I11i
   if 13 - 13: O00oOoOoO0o0O - Oo0Ooo - Oo0ooO0oo0oO
   if 92 - 92: Oo0ooO0oo0oO / OoOoOO00 * OoO0O00 . I11i % II111iiii
  try :
   O0OoOoO00O = self . CheckQuality ( quality_int , IIiii )
   Oo000 = '/streaming'
   I11i1ii1 = { 'contentid' : contentid
 , 'contenttype' : II1i1i1iII1
 , 'action' : IioO0O
 , 'quality' : str ( O0OoOoO00O ) + 'p'
 , 'deviceModelId' : 'Windows 10'
 , 'guid' : self . GetGUID ( guidType = 2 )
 , 'lastplayid' : self . guid
 , 'authtype' : 'cookie'
 , 'isabr' : 'y'
 , 'ishevc' : 'n'
 }
   if 96 - 96: I1IiiI % Oo0Ooo . I1ii11iIi11i + OOooOOo
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( O0O00Ooo ) + '&' + urllib . urlencode ( I11i1ii1 )
   if 42 - 42: II111iiii * iii1I1I * i11iIiiIii - OOooOOo . OoooooooOO
   if 76 - 76: II111iiii
   if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
   I11i1ii1 . update ( O0O00Ooo )
   OOOO = self . SESSION . Request2 ( self . API_DOMAIN + Oo000 , params = I11i1ii1 )
   if 24 - 24: II111iiii % O0oo0OO0 - Oo0ooO0oo0oO + I1IiiI * I1ii11iIi11i
   if 2 - 2: Ii1I - O00oOoOoO0o0O
   O0iIi1IiII = OOOO [ 'playurl' ]
   if O0iIi1IiII == None : return None
   I1iooo = OOOO [ 'awscookie' ]
   ii1iiIi1 = OOOO [ 'drm' ]
   if 'previewmsg' in OOOO [ 'preview' ] : i111iiI1ii = OOOO [ 'preview' ] [ 'previewmsg' ]
   if 83 - 83: oO0o % o0oOOo0O0Ooo % Ii1I - II111iiii * OOooOOo / OoooooooOO
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
  O0iIi1IiII = O0iIi1IiII . replace ( 'pooq.co.kr' , 'wavve.com' )
  if 71 - 71: OoooooooOO
  return ( O0iIi1IiII , I1iooo , ii1iiIi1 , i111iiI1ii )
  if 33 - 33: O0oo0OO0
  if 62 - 62: I1ii11iIi11i + Ii1I + i1IIi / OoooooooOO
  if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
  if 22 - 22: Oo0ooO0oo0oO - Oo0ooO0oo0oO % OOooOOo . O0oo0OO0 + oO0o
  if 63 - 63: I1IiiI % O0oo0OO0 * o0oOOo0O0Ooo + O0oo0OO0 / Oo0Ooo % iii1I1I
  if 45 - 45: O00oOoOoO0o0O
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
