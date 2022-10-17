import os

def _get_default_apps():
    '''尝试获取edge浏览器作为默认的搜索软件,若无法获取则返回空'''
    edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    if os.path.exists(edge):
        default_apps = {
            "apps":{
                "edge":edge
            },
            "default":"edge"
        }
    else:
        default_apps = None
    return default_apps

def _get_apps():
    '''结合用户配置的user_apps,返回全部的可使用的user_apps'''
    default_apps = _get_default_apps()
    if not default_apps and not user_apps:
        raise ValueError(
            "can't get default edge,"
            "and user not config user_apps"
            f"please config user_apps <locate {os.path.abspath('.')}>"
        )
    if not default_apps:
        return user_apps
    else:
        if not user_apps.get('default'):
            user_apps['default'] = default_apps['default']
        user_apps.setdefault("apps",{}).update(default_apps['apps'])
        return user_apps

# 用户配置的搜索软件
# 注释为示例
user_apps = {
    # "apps":{
    #     "google":r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", # 搜索软件名和软件路径
    # },
    # "default":"" # 默认搜索软件
}

apps = _get_apps()


# 搜索引擎
engines = {
    "engines":{
        "bing":{
            "base_url":"https://www.cn.bing.com", # 引擎首页的url
            "search_url":"https://www.cn.bing.com/search?q=" # 引擎的搜索功能url
        },
        "baidu":{
            "base_url":"https://www.baidu.com",
            "search_url":"https://www.baidu.com/s?wd="
        },
        "github":{
            "base_url":"https://github.com/",
            "search_url":"https://github.com/search?q="
        }
    },
    "default":"bing"
}

