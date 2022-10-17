import argparse
from subprocess import run

from sou import config
# import config


def parse_args():
    '''解析命令行参数'''
    parser = argparse.ArgumentParser(description="借助系统搜索软件进行搜索")

    # 可供选择的app和引擎
    apps = config.apps['apps'].keys()
    engines = config.engines['engines'].keys()

    parser.add_argument("-a","--app",choices=apps,help="搜索软件")
    parser.add_argument("-e","--engine",choices=engines,help="搜索引擎")
    parser.add_argument("-l","--link",help="搜索指定链接") 
    parser.add_argument("contents",nargs="*",help="搜索指定内容")

    args = parser.parse_args()
    # print(args)

    return args

class Sou:
    def __init__(self,app,engine):
        self.app = app
        self.engine = engine


    def search_link(self,link):
        '''按链接搜索,对搜索软件本身功能封装'''

        # 使用list形式的表达式而不是shell形式的表达式,第一个参数是应用的路径
        # 这里表达是用xxx执行xxx,交给shell是先解析,再根据解析的xxx去执行xxx,解析有时候会因为转义问题造成意向之外的结果
        # 因此更加推荐用list形式的表达式
        run([self.app,link])

    def _search_default(self):
        self.search_link(self.engine['base_url'])
    
    def _search_content(self,content):
        link = f"{self.engine['search_url']}{content}"
        self.search_link(link)

    def search(self,contents):
        '''根据搜索引擎生成对应的搜索链接,并进行搜索'''
        if not contents:
            self._search_default()
        else:
            for content in contents:
                self._search_content(content)

def main():
    args = parse_args()
    apps = config.apps['apps']
    default_app = apps[config.apps['default']]
    engines = config.engines['engines']
    default_engine = engines[config.engines['default']]

    app = default_app if args.app is None else apps[args.app]
    engine = default_engine if args.engine is None else engines[args.engine]
    
    sou = Sou(app,engine)

    # 指定-l参数时,直接跳转到指定链接
    if args.link is not None:
        sou.search_link(args.link)
    else:
        sou.search(args.contents)

if __name__ == "__main__":
    main()
    
    
