from random import *

love_dic={
    '001 汉语' :'我爱你',
	'002 英语':'I love you',
	'003 法语':"je t'aime",
	'004 德语':'ich liebe dich',
	'005 希腊语':'σε αγαπώ se agapo',
	'006 匈牙利语':'szertlek',
	'007 爱尔兰语':"taim i'ngra leat",
	'008 爱沙尼亚语':'mina armadtansind',
    '009 芬兰语' : "mina' rakastan sinua ",
    '010 比利时弗拉芒语':'ik zie u graag',
    '011 意大利语':'Ti Amo',
    '012 拉丁语':'te amo vos amo',
    '013 拉脱维亚语':'estevi milu',
    '014 荷兰语':'ik hou van jou',
    '015 丹麦语':'jeg elsker dig',
    '016 葡萄牙语':'eu amo-te',
    '017 里斯本语':'lingo gramo',
    '018 立陶宛语':'tave myliu',
    '019 马其顿语':'te sakam',
    '020 阿塞拜疆语':'men seni sevirem',
    '021 孟加拉语':'ami to may halobashi',
    '022 波兰语':'kocham cie',
    '023 罗马尼亚语':'te tu be besc',
    '024 印度语':'vivian',
    '025 捷克语':'milujite',
    '026 马耳他语':'inhobbok',
    '027 克罗地亚语':'volim te',
    '028 缅甸语':'chit pade',
    '029 孟加拉语':'āmi tomāke bhālobāshi',
    '030 柬埔寨语':'bong salang oun',
    '031 菲律宾语':'mahal kita',
    '032 印度尼西亚语':'saja kasih savdari',
    '033 日本语':'爱してる' ,
    '034 韩国语（朝鲜语）':'사랑해（요）',
    '035 爪哇语':'aku tresno marang sliromu',
    '036 老挝语':'khoi huk chau',
    '037 马来西亚语':'saya citamu',
    '038 蒙古语':'би чамд хайртай' ,
    '039 尼泊尔语':'ma timilai maya',
    '040 波斯语':'tora dost daram',
    '041 北部印地语':'main tumse pyar karta hoon',
    '042 俄罗斯语':'Я тебя люблю' ,
    '043 西班牙语':"te amo/te quiero",
    '044 古吉拉特语':'hoon tanepvem karunchuun',
    '045 塞尔维亚语':'volim to',
    '046 瑞典语':"jag &auml;lskar dig",
    '047 土耳其语':'seni seviyorum',
    '048 乌克兰语':'я тебе кохаю',
    '049 越南语':"em ye'u anh / anh ye'u em",
    '050 冰岛语':'eg elska tigi',
    '051 斯瓦希里语':'ninakupenda',
    '052 阿拉伯语':"أُحِبُّكَ",
    '053 马达加斯加语':'tiak ianao',
    '054 阿尔萨斯语':'ich hoar dich gear',
    '055 亚美尼亚语':'yes kezi seeroom',
    '056 巴伐利亚语':'imog di narrisch',
    '057 亚述语':'ana bayanookh',
    '058 他加禄语':'mahal kita',
    '059 南非语':'ek het jou lief',
    '060 加纳语':'me do wo',
    '061 埃塞俄比亚语':'ene ewwdechaly',
    '062 北非柏尔语':'lakb tirikh',
    '063 克里奥尔语':'mon kon tanoui',
    '064 豪萨语':'ndiya kuthanda',
    '065 印度阿萨姆语':'moi tomak bhal pan',
    '066 南亚泰米尔语':"tamil n\`an unnaik",
    '067 斯洛文尼亚语':'ljubim',
    '068 保加利亚语':'ahs te obicham',
    '069 加泰罗尼亚语':"T‘estimo",
    '070 索切尔克斯语': 'wise cas',
    '071 泰语':'ผมรักคุณ phom rak khun',
    '072 乌尔都语':'mein tumhay pyar karta hun',
    '073 新西兰毛利语':'kiahoahai',
    '074 印度泰卢固语':"neenu ninnu pra mistu\`nnany",
    '075 爱斯基摩语':'na gligivaget',
    '076 格陵兰语':'asaoakit i',
    '077 阿尔巴尼亚语':'dna shume',
    '078 威尔士语':'rwyndy garu di',
    '079 世界语':'Mi amas vin',
    '080 希伯来语':"אני אוהב אותך",
    '081 藏语':'nga khyed la dgav',
    '082 祖鲁语':'ngiyakuthanda',
    '083 毛利语':'Kei te aroha au i a koe',
    '084 哈萨克语':'Мен сені сүйемін',
    '085 古英语':"ic lufie &thorn;e",
    '086 苏格兰语':'Ah loove ye',
    '087 斯洛伐克语':"Milujem ťa",
    '088 盖尔语':'ta graih aym ort',
    '089 冰岛语':'Eacute;g elska thorn;ig',
    '090 满语':'Bi shimbe hairambi',
    '091 恩德贝莱语':'Ngiyakuthanda',
    '092 萨摩亚语':'Ou te alofa ia te oe',
    '093 索马里语':'waan ku jecelahay',
    '094 塞索托语':'ke a o rata',
    '095 瓦隆语':"dji t've&ucirc; vol't&icirc ",
    '096 威尔士语':"dw i'n dy garu di",
    '097 齐聪加语':'ndza ku rhandza',
    '098 乌兹别克语':'Men seni sevaman',
    '099 印加克丘亚语':'tawan nitaru o',
    '100 瓜德罗普岛':'mwen enmene',
    '101 最新网络暗语':'8023',
    '102 维吾尔语': 'Men sizni Soyimen',
}

love_list=list(love_dic.values())



def show_all_langs_available():
    for key in love_dic.keys():
        print(key)

        
def message(default_lang=False):
    """ Return the message either in directed language or in a random language.
    :param bool default_lang: If set to True, and given the language ID, then the message returned in that mentioned language. Otherwise the message will be returned in random supported language.
    :return str:
    """
    if default_lang is True:
        print("输入语言编号(三位):\n")
        show_all_langs_available()
        no = input("\n输入语言编号(三位):")
        lang=int(no)
        if(lang>0 and lang<=102):
            index=lang-1
            message=love_list[index]
        else:
            print("语言编号输入有误!请输入:001~102 之间的编号!\n")
            
            
    if default_lang is False:
        no = randint(1, 103)
        lang=int(no)
        index=lang-1
        message=love_list[index]
        
	return message