#!/usr/bin/env python
# coding: utf-8

class Opml:

  HEAD            = '<'
  TAIL            = '>'
  SLASH           = '/'
  QUOTATION       = '\''
  DOUBLEQUOTATION = '\"'


  OPML            = 'opml'
  VERSION         = 'version'

  HEAD            = 'head'
  TITLE           = 'title'              # タイトル.
  DATECREATED     = 'dateCreated'        # 作成日時.
  DATEMODIFIED    = 'dateModified'       # 更新日時.
  OWNERNAME       = 'ownerName'          # オーナー名 (著作権保持者).
  OWNEREMAIL      = 'ownerEmail'         # オーナーのメールアドレス.
  OWNERID         = 'ownerId'            # オーナーの ID.
  DOCS            = 'docs'               # OPMLファイルで使用されるフ​​ォーマットのドキュメントのHTTPアドレス.
  EXPANSIONSTATE  = 'expansionState'     # 展開する行番号 >1,3,17</ なら上から 1,3,17 番目の outline を展開する.
  VERTSCROLLSTATE = 'vertScrollState'    # どの outline をウィンドウの一番上に表示するか.
  WINDOWTOP       = 'windowTop'          # ウィンドウの上端の座標.
  WINDOWLEFT      = 'windowLeft'         # ウィンドウの左端の座標.
  WINDOWBOTTOM    = 'windowBottom'       # ウィンドウの下端の座標.
  WINDOWRIGHT     = 'windowRight'        # ウィンドウの右端の座標.

  BODY            = 'body'
  OUTLINE         = 'outline'
  TEXT            = 'text'
  TYPE            = 'type'
  ISCOMMENT       = 'isComment'          # コメントかどうか. default = false.
  ISBREAKPOINT    = 'isBreakpoint'       # ブレークポイントが設定さｒているかどうか. default = false.
  CREATED         = 'created'
  CATEGORY        = 'category'

  MIMETYPE        = 'text/xml'

  ACCEPTHEADER    = 'text/x-opml'

  XML = '<?xml version="1.0" encoding="ISO-8859-1"?>'
  OPML = '<opml version="2.0">'

  # コンストラクタ
  def __init__(self, text):
    self.text = text
    self.xmlVersion = "1.0"
    self.xmlCoding = "UTF-8"

    self.version = "1.0"


class Head:
  def __init__(self, text):
    self.title = "title"

class Body:
  def __init__(self, text):
    self.outlines = []
