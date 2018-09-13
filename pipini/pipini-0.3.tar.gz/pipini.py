import configparser
import pathlib
import click
import os

cf = configparser.ConfigParser()
pipiniPath = os.path.expanduser('~')+'\\pip'+'\\pip.ini'


def createini(ctx,param,value):
    if value:
        pathlib.Path(os.path.expanduser('~')+"\\pip").mkdir(exist_ok=True, parents=True)
        cf.add_section("global")
    
        cf["global"]["index-url"] = "https://pypi.douban.com/simple"
        cf["global"]["trusted-host"] = "https://pypi.douban.com"
        cf['global']['timeout'] = '60'

        cf.write(open(pipiniPath, "w", encoding='utf-8'))

def viewini(ctx, parm, vlaue):
    if vlaue:
        cf.read_file(open(pipiniPath,"r", encoding="utf-8"))
        for key,item in cf.items("global"):
            print(key+" : "+item)



@click.command()
@click.option('-c', is_flag=True, expose_value=False, callback=createini,help="this can help you create a defualt pip.ini with douban sources")
@click.option('-l', is_flag=True, expose_value=False, callback=viewini, help="list all pip sources")
@click.option('--index-url',"index_url", help="set the index-url")
@click.option('--timeout',"timeout", help="set the timeout")
@click.option('--trusted-host', 'trusted_host',help="set the trusted-host")
def cli(index_url, timeout, trusted_host):
    cf.read_file(open(pipiniPath, 'r', encoding="utf-8"))
    if index_url:
        cf['global']['index-url'] = index_url
    
    if timeout:
        cf['global']['timeout'] = timeout
    
    if trusted_host:
        cf['global']['trusted_host'] = trusted_host
    
    cf.write(open(pipiniPath, 'w', encoding='utf-8'))


if __name__ == "__main__":
    cls()