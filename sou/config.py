
# 搜索软件
apps = {
    "apps":{
        "edge":r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', # 搜索软件名和软件路径
        "google":r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    },
    "default":"edge" # 默认搜索软件
}

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

