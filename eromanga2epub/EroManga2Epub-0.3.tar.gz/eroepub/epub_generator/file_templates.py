import textwrap

mimetype= u"application/epub+zip"

container_xml = textwrap.dedent(
    u"""    <?xml version="1.0"?>
    <container
     version="1.0"
     xmlns="urn:oasis:names:tc:opendocument:xmlns:container"
    >
    <rootfiles>
    <rootfile
     full-path="OEBPS/standard.opf"
     media-type="application/oebps-package+xml"
    />
    </rootfiles>
    </container>"""
)

navigation_documents_xhtml = textwrap.dedent(
    u"""    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="ja">
    <head>
    <meta charset="UTF-8"></meta>
    <title>Navigation</title>
    </head>
    <body>
    <nav epub:type="toc" id="toc">
    <h1>Navigation</h1>
    <ol>
    <li><a href="text/p_cover.xhtml">表紙</a></li>
    </ol>
    </nav>
    <nav epub:type="landmarks">
    <ol>
    <li><a epub:type="bodymatter" href="text/p_cover.xhtml">Start of Content</a></li>
    </ol>
    </nav>
    </body>
    </html>"""
)

fixed_layout_jp_css = textwrap.dedent(
    u"""    @charset "UTF-8";

    html,
    body {
        margin:    0;
        padding:   0;
        font-size: 0;
    }
    svg {
        margin:    0;
        padding:   0;
    }"""
)

xhtml_template = textwrap.dedent(
    u"""    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE html>
    <html
     xmlns="http://www.w3.org/1999/xhtml"
     xmlns:epub="http://www.idpf.org/2007/ops"
     xml:lang="ja"
    >
    <head>
    <meta charset="UTF-8" />
    <title>{book_name}</title>
    <link rel="stylesheet" type="text/css" href="../style/fixed-layout-jp.css"/>
    <meta name="viewport" content="width={width}, height={height}"/>
    </head>
    <body>
    <div class="main">
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="100%" height="100%" viewBox="0 0 {width} {height}">
    <image width="100%" height="100%" preserveAspectRatio="xMidYMid meet" xlink:href="../image/{image_filename}" />
    </svg>
    </div>
    </body>
    </html>"""
)

manifest_template = textwrap.dedent(
    u"""    <?xml version="1.0" encoding="UTF-8"?>
    <package xmlns="http://www.idpf.org/2007/opf" version="3.0" xml:lang="ja" unique-identifier="unique-id" prefix="rendition: http://www.idpf.org/vocab/rendition/#         epub-bundle-tool: https://wing-kai.github.io/epub-manga-creator/         ebpaj: http://www.ebpaj.jp/         fixed-layout-jp: http://www.digital-comic.jp/">

    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">

    <!-- 作品名 -->
    <dc:title id="title">{book_name}</dc:title>
    <meta refines="#title" property="file-as"></meta>

    <!-- 著者名 -->
    <dc:creator id="creator01">{author}</dc:creator>
    <meta refines="#creator01" property="role" scheme="marc:relators">aut</meta>
    <meta refines="#creator01" property="file-as"></meta>
    <meta refines="#creator01" property="display-seq">0</meta>

    <dc:subject>成年コミック</dc:subject>

    <!-- 出版社名 -->
    <dc:publisher id="publisher">{publisher}</dc:publisher>
    <meta refines="#publisher" property="file-as"></meta>

    <!-- 言語 -->
    <dc:language>ja</dc:language>

    <!-- ファイルid -->
    <dc:identifier id="unique-id">urn:uuid:{uuid}</dc:identifier>

    <!-- 更新日 -->
    <meta property="dcterms:modified">{time}</meta>

    <!-- Fixed-Layout Documents指定 -->
    <meta property="rendition:layout">pre-paginated</meta>
    <meta property="rendition:spread">landscape</meta>

    <!-- etc. -->
    <meta property="ebpaj:guide-version">1.1</meta>
    <meta name="SpineColor" content="#FFFFFF"></meta>
    <meta name="cover" content="cover"></meta>

    </metadata>

    <manifest>

    <!-- navigation -->
    <item media-type="application/xhtml+xml" id="toc" href="navigation-documents.xhtml" properties="nav"></item>

    <!-- style -->
    <item media-type="text/css" id="fixed-layout-jp" href="style/fixed-layout-jp.css"></item>

    <!-- image -->
    {images}
    <!-- text -->
    {xhtmls}
    </manifest>

    <spine page-progression-direction="rtl">

    {itemrefs}
    </spine>

    </package>"""
)

cover_image_item = u'<item id="cover" href="image/cover.{suffix}" media-type="image/{suffix}" properties="cover-image"></item>\n'

image_item = u'<item id="{id}" href="image/{image_filename}" media-type="image/{suffix}"></item>\n'

cover_xhtml_item = u'<item id="p_cover" href="text/p_cover.xhtml" media-type="application/xhtml+xml" properties="svg" fallback="cover"></item>\n\n'

xhtml_item = u'<item id="{xhtml_id}" href="text/{xhtml_filename}" media-type="application/xhtml+xml" properties="svg" fallback="{image_id}"></item>\n'

cover_itemref = u'<itemref linear="yes" idref="p_cover" properties="rendition:page-spread-center"></itemref>\n\n'

right_itemref = u'<itemref linear="yes" idref="{id}" properties="page-spread-right"></itemref>\n'

left_itemref = u'<itemref linear="yes" idref="{id}" properties="page-spread-left"></itemref>\n'