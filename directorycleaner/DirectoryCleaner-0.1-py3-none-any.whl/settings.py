import sys
import os
import json
import platform
from .color_print import BColors
from .main import DIRNAMES

class Settings:
    """
    Core settings for Directory Cleaner. Houses the
    default settings that will be reverted to if the user
    uses the revert settings flag.
    """
    ANSWERS = {
        "yes": ("yes", "y", "Yes", "Y", "YES"),
        "no": ("no", "n", "No", "N", "NO")
    }

    OS_CONVENTIONS = {
    "unix": ("Darwin", "Linux", "Linux2"),
    "windows": "Windows"
    }

    RESTRICTED_CHARS = {
    "unix": "/",
    "windows": ("<", ">", ":", '"', "/", "\\", "|", "?", "*")
    }

    DEFAULT_SETTINGS = {
    "main_folder_name": "DirectoryCleaner",
    "unknowns_folder_name": "Unknown",
    "txt_file_name": "DirectoryCleaner",
      "groups": {
        "Images": {
            "group_items": ["jpg", "jpeg", "png", "tif", "tiff", "gif", "bmp", "eps", "raw", "cr2", "nef", "orf", "sr2"],
            "name": "Images"
        },
        "Audio": {
            "group_items": ["pcm", "wav", "mp3", "aiff", "aac", "ogg", "wma", "flac", "alac", "opus"],
            "name": "Audio"
        },
        "Video": {
            "group_items": ["mov", "mp4", "avi", "flv", "wmv", "webm", "m4a", "m4v"],
            "name": "Video"
        },
        "Documents": {
            "group_items": ["doc", "docx", "docm"],
            "name": "Documents"
        },
        "PDFS": {
            "group_items": ["pdf"],
            "name": "PDFS"
        },
        "SpreadSheets": {
            "group_items": ["xls", "xlsx", "xlsm", "xltx", "xltm", "xlsx", "xlt", "xlm"],
            "name": "SpreadSheets"
        },
        "TextFiles": {
            "group_items": ["txt", "rtf"],
            "name": "TextFiles"
        }
    },
  "extensions":{
  	"7z": "(7z)7z compressed archive file",
  	"ace": "(ace)WinAce Compressed File",
  	"apk": "(apk)Android Package File",
  	"bz2": "(bz2)BZzip2 compressed archive file",
  	"crx": "(crx)Chrome Extension",
  	"dd": "(dd)DiskDoubler Archive",
  	"deb": "(deb)Debian Software Package",
  	"gz": "(gz)Gnu Zipped Archive File",
  	"gzip": "(gzip)Gnu Zipped File",
  	"jar": "(jar)Java Archive File",
  	"rar": "(rar)WinRAR Compressed Archive",
  	"rpm": "(rpm)Red Hat Package Manager File",
  	"sit": "(sit)StuffIt Archive",
  	"sitx": "(sitx)StuffIt X Archive",
  	"snb": "(snb)S Note File",
  	"tar": "(tar)Consolidated Unix File Archive",
  	"tar.gz": "(tar.gz)Compressed Tarball File",
  	"tgz": "(tgz)Gzipped Tar File",
  	"zip": "(zip)ZIP compression",
  	"zipx": "(zipx)Extended Zip File",
  	"3ga": "(3ga)3GPP Audio File",
  	"aa": "(aa)Audible Audio Book File",
  	"aac": "(aac)MPEG-2 Advanced Audio Coding File",
  	"aax": "(aax)Audible Enhanced Audiobook File",
  	"aif": "(aif)Audio Interchange File Format",
  	"aifc": "(aifc)Compressed Audio Interchange File",
  	"aiff": "(aiff)Audio Interchage File Format",
  	"amr": "(amr)Adaptive Multi-Rate Codec File",
  	"ape": "(ape)Monkey's Audio Lossless Audio File",
  	"asx": "(asx)Microsoft Advanced Stream Redirector File",
  	"au": "(au)Audio File",
  	"aup": "(aup)Audacity Project File",
  	"awb": "(awb)AMR-WB Audio File",
  	"caf": "(caf)Apple Core Audio Format",
  	"cda": "(cda)CD Audio Track Shortcut",
  	"flac": "(flac)Free Lossless Audio Codec File",
  	"gsm": "(gsm)Global System for Mobile Audio File",
  	"iff": "(iff)EA Interchange File Format",
  	"kar": "(kar)Karaoke files",
  	"koz": "(koz)Audiokoz Music File",
  	"m3u8": "(m3u8)UTF-8 M3U Playlist File",
  	"m4a": "(m4a)MPEG-4 Audio Layer",
  	"m4p": "(m4p)iTunes Music Store Audio File",
  	"m4r": "(m4r)iPhone Ringtone File",
  	"mid": "(mid)Musical Instrument Digital Interface MIDI-sequention Sound",
  	"midi": "(midi)MIDI files",
  	"mmf": "(mmf)Synthetic Music Mobile Application File",
  	"mp2": "(mp2)MPEG Layer II Compressed Audio File",
  	"mp3": "(mp3)MPEG Layer 3 Audio",
  	"mpa": "(mpa)MPEG-2 Audio File",
  	"mpc": "(mpc)Musepack Compressed Audio File",
  	"mpga": "(mpga)MPEG-1 Layer 3 Audio File",
  	"ogg": "(ogg)Ogg Vorbis Audio File",
  	"oma": "(oma)Sony OpenMG audio",
  	"opus": "(opus)Opus Audio File",
  	"qcp": "(qcp)Qualcomm PureVoice Audio File",
  	"ra": "(ra)Real Audio File",
  	"ram": "(ram)Real Media Audio Metadata File",
  	"rta": "(rta)TrueRTA Project File",
  	"wav": "(wav)WAVE Audio",
  	"wma": "(wma)Windows Media (Metafile)",
  	"xspf": "(xspf)XML Shareable Playlist Format",
  	"3dm": "(3dm)Rhino 3D Model",
  	"3ds": "(3ds)3D Studio Scene",
  	"dwg": "(dwg)AutoCAD Drawing Database File",
  	"dxf": "(dxf)Drawing Exchange Format File",
  	"max": "(max)3ds Max Scene File",
  	"obj": "(obj)Wavefront 3D Object File",
  	"clp": "(clp)Windows Clipboard File",
  	"dif": "(dif)Data Interchange Format",
  	"efx": "(efx)eFax Document",
  	"gbr": "(gbr)Gerber File",
  	"ged": "(ged)GEDCOM Genealogy Data File",
  	"itl": "(itl)iTunes Library File",
  	"keychain": "(keychain)Mac OS X Keychain File",
  	"mtw": "(mtw)Minitab Worksheet File",
  	"one": "(one)OneNote Document",
  	"sdf": "(sdf)Standard Data File",
  	"tax2012": "(tax2012)TurboTax 2012 Tax Return",
  	"tax2014": "(tax2014)TurboTax 2014 Tax Return",
  	"vcf": "(vcf)vCard File",
  	"accdb": "(accdb)Access 2007 Database File",
  	"bup": "(bup)DVD Info Backup File",
  	"crypt": "(crypt)WhatsApp Encrypted Dastabase File",
  	"db": "(db)Database file",
  	"dbf": "(dbf)Database File",
  	"mdb": "(mdb)Microsoft Access Database",
  	"pdb": "(pdb)Program Database",
  	"sql": "(sql)Structured Query Language Data File",
  	"apa": "(apa)RSView Development Project Archive",
  	"asc": "(asc)ActionScript Communication File",
  	"asm": "(asm)Assembly Language Source Code File",
  	"b": "(b)BASIC Source Code File",
  	"bas": "(bas)BASIC Source Code File",
  	"bet": "(bet)BETA Source File",
  	"bluej": "(bluej)BlueJ Package File",
  	"c": "(c)C/C++ Source Code File",
  	"cbl": "(cbl)COBOL Source Code File",
  	"cd": "(cd)Visual Studio Class Diagram",
  	"class": "(class)Java Class File",
  	"cod": "(cod)Compiled Source Code",
  	"cpp": "(cpp)C++ Source Code File",
  	"cs": "(cs)Visual C# Source Code File",
  	"d": "(d)D Source Code File",
  	"def": "(def)C++ Module-Definition File",
  	"dtd": "(dtd)Document Type Definition File",
  	"erb": "(erb)Ruby ERB Script",
  	"fla": "(fla)Adobe Flash Animation",
  	"fsproj": "(fsproj)Visual F# Project File",
  	"fxc": "(fxc)FilePackager Configuration",
  	"h": "(h)C/C++/Objective-C Header File",
  	"hpp": "(hpp)C++ Header File",
  	"ise": "(ise)InstallShield Express Project File",
  	"java": "(java)Java Source Code File",
  	"kv": "(kv)Kivy Language File",
  	"lua": "(lua)Lua Source File",
  	"m": "(m)Objective-C Implementation File",
  	"m4": "(m4)Macro Processor Library",
  	"nib": "(nib)Interface Builder User Interface File",
  	"o": "(o)Compiled Object File",
  	"owl": "(owl)OWL Source Code File",
  	"p": "(p)PASCAL Program File",
  	"pas": "(pas)Pascal Source File",
  	"pb": "(pb)PureBasic Source File",
  	"pbj": "(pbj)Pixel Bender Bytecode File",
  	"pbxuser": "(pbxuser)Xcode Project User Data File",
  	"pika": "(pika)Pika Software Builder Project File",
  	"pl": "(pl)Perl Script",
  	"pwn": "(pwn)Pawn Source Code File",
  	"py": "(py)Python Script",
  	"pyw": "(pyw)Python GUI Source File",
  	"qpr": "(qpr)FoxPro Generated Query Program",
  	"rc": "(rc)Resource Script",
  	"resources": "(resources)Visual Studio Resource File",
  	"s19": "(s19)Motorola S19 File Record",
  	"sb": "(sb)Scratch Project File",
  	"sb2": "(sb2)Scratch 2.0 Project File",
  	"sh": "(sh)Bash Shell Script",
  	"sln": "(sln)Visual Studio Solution File",
  	"sma": "(sma)AMX Mod Plugin Source File",
  	"suo": "(suo)Visual Studio Solution User Options File",
  	"swift": "(swift)Swift Source Code File",
  	"trx": "(trx)Microsoft Visual Studio Test Results File",
  	"vbp": "(vbp)Visual Basic Project File",
  	"vbproj": "(vbproj)Visual Studio Visual Basic Project",
  	"vbx": "(vbx)Visual Basic Custom Control",
  	"vc": "(vc)Verge Source Code File",
  	"vcxproj": "(vcxproj)Visual C++ Project",
  	"xap": "(xap)XACT Project File",
  	"xcodeproj": "(xcodeproj)Xcode Project",
  	"xq": "(xq)XQuery File",
  	"xt": "(xt)Xdebug Trace File",
  	"yml": "(yml)YAML Document",
  	"chm": "(chm)Compiled HTML Help File",
  	"csk": "(csk)Claris Works File",
  	"doc": "(doc)Microsoft Word Binary File Format",
  	"docm": "(docm)Word Open XML Macro-Enabled Document",
  	"docx": "(docx)Microsoft Word Open XML Document",
  	"dot": "(dot)Microsoft Word Document Template File",
  	"dotx": "(dotx)Word Open XML Document Template",
  	"eml": "(eml)E-Mail Message",
  	"hwp": "(hwp)Hanword Document",
  	"log": "(log)Log File",
  	"m3u": "(m3u)Media Playlist File",
  	"msg": "(msg)Outlook Mail Message",
  	"odm": "(odm)OpenDocument Master Document",
  	"odt": "(odt)OpenDocument Text Document",
  	"oxps": "(oxps)OpenXPS File",
  	"pages": "(pages)Pages Document",
  	"pdf": "(pdf)Portable Document Format",
  	"pmd": "(pmd)PageMaker Document",
  	"pub": "(pub)Microsoft Publisher Document File",
  	"rtf": "(rtf)Rich Text Format",
  	"shs": "(shs)Shell Scrap Object File",
  	"sxw": "(sxw)StarOffice Writer Document",
  	"tex": "(tex)LaTeX Source Document",
  	"txt": "(txt)Raw text file",
  	"vmg": "(vmg)Nokia vMessage",
  	"vnt": "(vnt)Mobile Phone vNote File",
  	"wp5": "(wp5)WordPerfect 5 Document",
  	"wpd": "(wpd)WordPerfect Document File",
  	"wps": "(wps)Microsoft Works Word Processor Document",
  	"xml": "(xml)Extensible Markup Language File",
  	"xps": "(xps)Microsoft XML Paper Specification File",
  	"apnx": "(apnx)Amazon Page Number Index File",
  	"azw": "(azw)Amazon Kindle ebook file",
  	"azw3": "(azw3)Amazon KF8 eBook File",
  	"cbr": "(cbr)ComicBook RAR Archive",
  	"cbt": "(cbt)Comic Book TAR File",
  	"cbz": "(cbz)Comic Book Zip Archive",
  	"epub": "(epub)Electronic Publication",
  	"fb2": "(fb2)FictionBook 2.0 File",
  	"lit": "(lit)Microsoft eBook File",
  	"lrf": "(lrf)Sony Portable Reader File",
  	"mbp": "(mbp)Mobipocket Notes File",
  	"mobi": "(mobi)Mobipocket",
  	"opf": "(opf)Open Packaging Format File",
  	"prc": "(prc)Mobipocket eBook File",
  	"tcr": "(tcr)Psion Series 3 eBook File",
  	"app": "(app)Mac OS X Application",
  	"bat": "(bat)DOS Batch File",
  	"cgi": "(cgi)Common Gateway Interface Script",
  	"cmd": "(cmd)Windows Command File",
  	"com": "(com)DOS Command File",
  	"ds": "(ds)DAZ Studio 1/2 Script",
  	"exe": "(exe)Windows Executable File",
  	"gadget": "(gadget)Windows Gadget",
  	"ipa": "(ipa)iOS Application",
  	"pif": "(pif)Program Information File",
  	"scr": "(scr)Script File",
  	"vb": "(vb)Visual Basic Project Item File",
  	"wsf": "(wsf)Windows Script File",
  	"8bi": "(8bi)Photoshop Plug-in",
  	"bak": "(bak)Firefox Bookmarks Backup, Backup File",
  	"bfc": "(bfc)Windows Briefcase File",
  	"cmf": "(cmf)Cal3D Binary Mesh File",
  	"crdownload": "(crdownload)Chrome Partially Downloaded File",
  	"cue": "(cue)Cue Sheet File",
  	"dao": "(dao)Disk at Once CD/DVD Image",
  	"dbx": "(dbx)Outlook Express E-mail Folder",
  	"dem": "(dem)Video Game Demo File",
  	"dic": "(dic)Dictionary File",
  	"epc": "(epc)Game Data File",
  	"fnt": "(fnt)Windows Font File",
  	"fon": "(fon)Generic Font File",
  	"gam": "(gam)Saved Game File",
  	"gho": "(gho)Norton Ghost Backup File",
  	"gpx": "(gpx)GPS Exchange File",
  	"grp": "(grp)StarCraft Graphics Group File",
  	"hex": "(hex)Hexadecimal Source File",
  	"hqx": "(hqx)BinHex 4.0 Encoded File",
  	"ics": "(ics)iCalendar File",
  	"idx": "(idx)Movie Subtitle File",
  	"img": "(img)Disk Image File",
  	"iso": "(iso)Disc Image File",
  	"jad": "(jad)Java Application Descriptor File",
  	"kml": "(kml)Keyhole Markup Language File",
  	"kmz": "(kmz)Keyhole Markup Language (Zipped)",
  	"map": "(map)Quake Engine Map File",
  	"mdf": "(mdf)Media Disc Image File",
  	"mim": "(mim)Multi-Purpose Internet Mail Message File",
  	"msi": "(msi)Windows Installer Package",
  	"mtb": "(mtb)MINITAB Exec File",
  	"nes": "(nes)Nintendo (NES) ROM File",
  	"ori": "(ori)Original File",
  	"otf": "(otf)OpenType Font",
  	"part": "(part)Partially Downloaded File",
  	"pes": "(pes)Brother Embroidery Format",
  	"plugin": "(plugin)Mac OS X Plug-in",
  	"ps": "(ps)Adobe PostScript File",
  	"qxp": "(qxp)QuarkXPress Project File",
  	"rem": "(rem)BlackBerry Encrypted Data File",
  	"rom": "(rom)N64 Game ROM File",
  	"sav": "(sav)Saved Game",
  	"t65": "(t65)PageMaker Template File",
  	"tec": "(tec)TECkit Compiled Mapping File",
  	"tmp": "(tmp)Temporary File",
  	"toast": "(toast)Toast Disc Image",
  	"torrent": "(torrent)BitTorrent File",
  	"ttf": "(ttf)TrueType Font",
  	"uue": "(uue)Uuencoded File",
  	"vcd": "(vcd)Virtual CD",
  	"xll": "(xll)Excel Add-In File",
  	"dtp": "(dtp)Publish-iT Document",
  	"indd": "(indd)Adobe InDesign Document",
  	"mdi": "(mdi)Microsoft Document Imaging File",
  	"p65": "(p65)PageMaker 6.5 Document",
  	"qxd": "(qxd)QuarkXPress Document",
  	"rels": "(rels)Open Office XML Relationships File",
  	"key": "(key)Keynote Presentation",
  	"odp": "(odp)OpenDocument Presentation File",
  	"pps": "(pps)PowerPoint Slide Show",
  	"ppsx": "(ppsx)PowerPoint Open XML Slide Show",
  	"ppt": "(ppt)Microsoft PowerPoint Presentation File",
  	"pptm": "(pptm)PowerPoint Open XML Macro-Enabled Presentation",
  	"pptx": "(pptx)Microsoft PowerPoint 2007 XML Presentation",
  	"art": "(art)AOL Compressed Image File",
  	"arw": "(arw)Sony Digital Camera Alpha Raw Image Format",
  	"bmp": "(bmp)Microsoft Windows bitmap",
  	"cr2": "(cr2)Canon Digital Camera Raw Image File",
  	"crw": "(crw)Canon Digital Camera Raw Image Format",
  	"dcm": "(dcm)Digital Imaging and Communications in Medicine Image File",
  	"dds": "(dds)Microsoft DirectDraw Surface",
  	"djvu": "(djvu)DjVu image files",
  	"dmg": "(dmg)Mac OS X Disk Image",
  	"dng": "(dng)Digital Negative Image File",
  	"exr": "(exr)OpenEXR Image",
  	"fpx": "(fpx)FlashPix Bitmap Image File",
  	"gif": "(gif)CompuServe Graphics Interchange Format",
  	"hdr": "(hdr)High Dynamic Range Image File",
  	"heic": "(heic)High Efficiency Image Format",
  	"ico": "(ico)Microsoft icon file",
  	"ithmb": "(ithmb)iPod and iPhone Photo Thumbnails File",
  	"jp2": "(jp2)JPEG 2000 Core Image File",
  	"jpeg": "(jpeg)Joint Photographic Experts Group JFIF format",
  	"jpg": "(jpg)Joint Photographic Experts Group JFIF format",
  	"kdc": "(kdc)Kodak Photo-Enhancer File",
  	"mac": "(mac)MacPaint Image",
  	"nef": "(nef)Nikon Digital Camera Raw Image File",
  	"nrw": "(nrw)Nikon Digital SLR Camera Raw Image File",
  	"orf": "(orf)Olympus Digital Camera Raw Image File",
  	"pcd": "(pcd)Photo CD",
  	"pct": "(pct)Apple Macintosh QuickDraw Image",
  	"pcx": "(pcx)ZSoft Paintbrush Bitmap Image File",
  	"pef": "(pef)Pentax Electronic File",
  	"pgm": "(pgm)Portable Gray Map Image",
  	"pict": "(pict)Apple Macintosh QuickDraw/picture file",
  	"png": "(png)Portable Network Graphics",
  	"psd": "(psd)Adobe Photoshop Document",
  	"pspimage": "(pspimage)PaintShop Pro Image",
  	"sfw": "(sfw)Seattle FilmWorks image",
  	"tga": "(tga)Truevision Targa Graphic File",
  	"thm": "(thm)Video Thumbnail File",
  	"tif": "(tif)Tagged Image File Format",
  	"tiff": "(tiff)Tagged Image File Format",
  	"wbmp": "(wbmp)Wireless Bitmap Image File",
  	"webp": "(webp)Google Web Picture files",
  	"xcf": "(xcf)eXperimental Computing Facility",
  	"yuv": "(yuv)YUV Encoded Image File",
  	"act": "(act)Adobe Color Table File",
  	"api": "(api)Adobe Photoshop Inks File",
  	"cdt": "(cdt)CorelDRAW Image Template",
  	"cfg": "(cfg)Configuration File",
  	"dun": "(dun)Dial Up Network File",
  	"fm3": "(fm3)Lotus 1-2-3 Spreadsheet Format File",
  	"gid": "(gid)Windows Help Global Index File",
  	"ht": "(ht)HyperTerminal Session File",
  	"icm": "(icm)Image Color Matching Profile",
  	"inf": "(inf)Setup Information File",
  	"ini": "(ini)Windows Initialization File",
  	"pkg": "(pkg)Mac OS X Installer Package",
  	"prf": "(prf)Outlook Profile File",
  	"csv": "(csv)Comma Separated Values File",
  	"ods": "(ods)OpenDocument Spreadsheet",
  	"wk3": "(wk3)Lotus 3 Worksheet",
  	"wks": "(wks)Lotus 1-2-3 Spreadsheet",
  	"xlr": "(xlr)Microsoft Works spreadsheet or chart",
  	"xls": "(xls)Microsoft Excel Spreadsheet",
  	"xlsb": "(xlsb)Excel Binary Spreadsheet",
  	"xlsm": "(xlsm)Excel Open XML Macro-Enabled Spreadsheet",
  	"xlsx": "(xlsx)Microsoft Excel Open XML Spreadsheet",
    "xltx": "(xltx)Microsoft Excel Template",
    "xlm": "(xlm)Legacy Excel Macro",
    "xlt": "(xlt)Legacy Excel Template",
  	"ani": "(ani)Windows Animated Cursor",
  	"bin": "(bin)Generic Binary File",
  	"bud": "(bud)Binary Printer Description File",
  	"cab": "(cab)Windows Cabinet File",
  	"cat": "(cat)Windows Catalog File",
  	"cpl": "(cpl)Windows Control Panel Item",
  	"cur": "(cur)Windows Cursor",
  	"dat": "(dat)Data File",
  	"deskthemepack": "(deskthemepack)Windows 8 Desktop Theme Pack File",
  	"dev": "(dev)Windows Device Driver File",
  	"dll": "(dll)Dynamic Link Library",
  	"dmp": "(dmp)Windows Memory Dump",
  	"drv": "(drv)Device Driver",
  	"ffl": "(ffl)Find Fast Document List",
  	"ffo": "(ffo)Find Fast Document Properties Cache",
  	"hlp": "(hlp)Windows Help File",
  	"icl": "(icl)Windows Icon Library File",
  	"icns": "(icns)Mac OS X Icon Resource File",
  	"lnk": "(lnk)Windows File Shortcut",
  	"nfo": "(nfo)System Information File",
  	"prop": "(prop)Android Build Properties File",
  	"sys": "(sys)Windows System File",
  	"ai": "(ai)Adobe Illustrator File",
  	"cdr": "(cdr)CorelDRAW Image File",
  	"cvs": "(cvs)Canvas 3 Drawing File",
  	"emf": "(emf)Microsoft Enhanced Metafile (32-bit)",
  	"emz": "(emz)Windows Compressed Enhanced Metafile",
  	"eps": "(eps)Adobe Encapsulated PostScript File",
  	"mix": "(mix)Microsoft Image Extension",
  	"odg": "(odg)OpenDocument Graphic File",
  	"pd": "(pd)FlexiSIGN 5 Plotter Document",
  	"svg": "(svg)Scalable Vector Graphics File",
  	"vsd": "(vsd)Microsoft Visio Drawing File",
  	"wmf": "(wmf)Windows Metafile",
  	"wpg": "(wpg)WordPerfect Graphics File",
  	"264": "(264)Ripped Video Data File",
  	"3g2": "(3g2)3rd Generation Partnership Project Multimedia File",
  	"3gp": "(3gp)3rd Generation Partnership Project",
  	"3gpp": "(3gpp)Third Generation Partnership Project Media File",
  	"amv": "(amv)Anime Music Video File",
  	"arf": "(arf)WebEx Advanced Recording File",
  	"asf": "(asf)Advanced Systems Format File",
  	"avi": "(avi)Microsoft Audio/Visual Interleaved",
  	"ced": "(ced)JVC Camera Video Data File",
  	"cpi": "(cpi)AVCHD Video Clip Information File",
  	"dav": "(dav)DVR365 Video File",
  	"dir": "(dir)Adobe Director Movie",
  	"divx": "(divx)Digital Video Express Encoded Movie Files",
  	"dvsd": "(dvsd)Digital Video File",
  	"f4v": "(f4v)Flash MP4 Video File",
  	"flv": "(flv)Animated Flash Video File",
  	"h264": "(h264)H.264 Encoded Video File",
  	"ifo": "(ifo)DVD Info File",
  	"m2ts": "(m2ts)MPEG-2 Transport Stream",
  	"m4v": "(m4v)iTunes Video File",
  	"mkv": "(mkv)Matroska Video File",
  	"mod": "(mod)Camcorder Recorded Video (Modul) File",
  	"mov": "(mov)QuickTime Movie",
  	"mp4": "(mp4)MPEG-4 Video Stream",
  	"mpeg": "(mpeg)Motion Picture Experts Group file interchange format",
  	"mpg": "(mpg)MPEG Video Stream",
  	"mswmm": "(mswmm)Microsoft Windows Movie Maker Project File",
  	"mts": "(mts)AVCHD Video File",
  	"mxf": "(mxf)Material Exchange Format File",
  	"ogv": "(ogv)Ogg Video File",
  	"pds": "(pds)PowerDirector Script File",
  	"qt": "(qt)Apple QuickTime Movie",
  	"rm": "(rm)Real Media File",
  	"srt": "(srt)SubRip Text Subtitle file",
  	"swf": "(swf)Shockwave Flash Movie",
  	"ts": "(ts)Video Transport Stream File",
  	"veg": "(veg)Vegas Pro Project",
  	"vep": "(vep)AVS Video Editor Project File",
  	"vob": "(vob)DVD Video Object File",
  	"vpj": "(vpj)VideoPad Video Editor Project File",
  	"webm": "(webm)Web Media File",
  	"wlmp": "(wlmp)Windows Live Movie Maker Project File",
  	"wmv": "(wmv)Windows Media Video",
  	"asp": "(asp)Active Server Page",
  	"aspx": "(aspx)Active Server Page Extended File",
  	"cer": "(cer)Internet Security Certificate",
  	"cfm": "(cfm)ColdFusion Markup File",
  	"cfml": "(cfml)ColdFusion Markup Language File",
  	"csr": "(csr)Certificate Signing Request File",
  	"css": "(css)Cascading Style Sheets",
  	"do": "(do)Java Servlet",
  	"htm": "(htm)Hypertext Markup Language File",
  	"html": "(html)Hypertext Markup Language with a client-side image map",
  	"js": "(js)JavaScript File",
  	"json": "(json)JavaScript Object Notation File",
  	"jsp": "(jsp)Java Server Page",
  	"nzb": "(nzb)NewzBin Usenet Index File",
  	"php": "(php)PHP Source Code File",
    "go": "(go)Golang Source Code File",
  	"rss": "(rss)Rich Site Summary",
  	"webloc": "(webloc)Mac OS X Website Location",
  	"xfdl": "(xfdl)Extensible Forms Description Language File",
  	"xhtml": "(xhtml)Extensible Hypertext Markup Language File",
  	"md": "(md)Markdown File",
  	"markdown": "(markdown)Markdown File",
    "pem": "(pem)Privacy Enhanced Mail File"
  }
}


    def change_group_name(self):
        while True:
            print("\n" + BColors.HEADER + "Here is a list of the current group names. If you would like to change any of them simply type the name of the type of group you want to change followed by an = sign and the name you would like to use. If you don't want to change a group name, type exit." + BColors.ENDC)
            print("--------------------")
            for group in self.extensions["groups"]:
                print(group + " = " + self.extensions["groups"][group]["name"])
            print("--------------------")
            print(BColors.OKBLUE + "What group name would you like to change?: " + BColors.ENDC, end="")
            response = input()
            if "=" in response:
                break
            elif response.strip() == "exit":
                return
            else:
                print("\n" + BColors.FAIL + "ERROR: There was no '=' detected in your response. Please read the formatting again." + BColors.ENDC)

        value = response.split("=")[0:2]
        for i in range(len(value)):
            value[i] = value[i].strip()
        try:
            self.extensions["groups"][value[0]]["name"] = value[1]
        except:
            print("\nERROR: That isn't a group name.")
            return
        with open(DIRNAMES["data"], "w") as f:
             json.dump(self.extensions, f)


    def change_main_folder(self):
        """
        Change name of the main folder that everything is stored in.
        """
        while True:
            print("\n" + BColors.OKBLUE + "What would you like to name the main folder?: " + BColors.ENDC, end="")
            response = input()
            if self.RESTRICTED_CHARS["unix"] in response and platform.system() in self.OS_CONVENTIONS["unix"]:
                print("\n" + BColors.FAIL + "There cannot be a '/' character in the folder name." + BColors.ENDC)
            elif any(char in response for char in self.RESTRICTED_CHARS["windows"]) and platform.system() in self.OS_CONVENTIONS["windows"]:
                print("\n" + BColors.FAIL + "There cannot be any of the following characters in a Windows folder name:")
                for char in self.RESTRICTED_CHARS:
                    print(char)
                print(BColors.ENDC)
            else:
                break
        response = response.strip()
        self.extensions["main_folder_name"] = response
        with open(DIRNAMES["data"], "w") as f:
             json.dump(self.extensions, f)


    def change_folder_name(self):
        """
        Method to change any of the default folder names Directory Cleaner starts out with.
        """
        while True:
            print("\n" + BColors.HEADER + "Here is a list of the current folder names Directory Cleaner will use for your files." + BColors.ENDC)
            for k in self.extensions["extensions"]:
                print(k, "=", self.extensions["extensions"][k])

            while True:
                print("\n" + BColors.OKBLUE + "If you want to change the name of one of the folders simply type the extension of the file, for example png, pdf, docx, followed by an equal sign and whatever you want to replace it with.\nWhenever you're ready 😊: " + BColors.ENDC, end="")
                response = input()
                if "=" in response:
                    break
                else:
                    print("\n" + BColors.FAIL + "ERROR: There was no '=' detected in your response. Please read the formatting again." + BColors.ENDC)

            filtered_response = response.split("=")[0].strip()
            if filtered_response not in self.extensions["extensions"]:
                print("\n" + BColors.FAIL + "ERROR: That isn't a file extension that Directory Cleaner supports." + BColors.ENDC)
                return
            else:
                value = response.split("=")[1].lstrip()
                self.extensions["extensions"][filtered_response] = value
                print(self.extensions["extensions"][filtered_response])

            while True:
                print("\n" + BColors.OKBLUE + "Do you want to change another folder name? Type 'yes' or 'y' if so, else type 'no' or 'n': " + BColors.ENDC, end="")
                exit = input()
                exit = exit.strip()
                if exit in self.ANSWERS["no"]:
                    return
                elif exit in self.ANSWERS["yes"]:
                    break
                else:
                    print("\n" + BColors.FAIL + "ERROR: Unrecognized answer. Please look at the options again." + BColors.ENDC)


    def default_settings(self):
        """
        Reverts all user changed settings to the default values.
        Assign extensions dict to original values and write to extensions.json
        """
        print("\n" + BColors.OKBLUE + "Are you sure you want to revert the settings to their original values? Type 'yes' or 'y' if so, else type 'no' or 'n': " + BColors.ENDC, end="")
        response = input()
        response = response.strip()
        if response in self.ANSWERS["yes"]:
            self.extensions = self.DEFAULT_SETTINGS
            with open(DIRNAMES["data"], 'w') as f:
                json.dump(self.DEFAULT_SETTINGS, f)
            print("\n" + BColors.OKGREEN + "Settings reverted successfully." + BColors.ENDC)
        elif response in self.ANSWERS["no"]:
            return
