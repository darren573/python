# -*- coding:utf-8 -*-

import urllib.request
import re


# 糗事百科爬虫类
class QSBK:
    # 初始化方法，定义一些变量
    def __init__(self):
        # 当前页码
        self.pageIndex = 1
        # 模拟浏览器的user_agent
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        # 存放每页段子的列表，每一个元素是每一页的段子们
        self.stories = []
        # 保存数据的文件
        self.file = open("糗事百科.txt", "w", encoding='utf-8')

    def __del__(self):
        self.file.close()

    # 传入某一页的索引获得页面代码
    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            # 构建请求的request
            req = urllib.request.Request(url, headers=self.headers)
            # 利用urlopen获取页面代码
            response = urllib.request.urlopen(req)
            # 将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode
        except Exception as e:
            if hasattr(e, "reason"):
                print(u"连接糗事百科失败,错误原因：", e.reason)
                return None

    # 传入某一页代码，返回本页不带图片的段子列表
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print("页面加载失败....")
            return None
        pattern = re.compile(
            '<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>.*?<h2>(.*?)</h2>.*?<a href="(.*?)".*?<div.*?class="content".*?>.*?<span>(.*?)</span>(.*?)</a>(.*?)<div class="stats.*?class="number">(.*?)</i>',
            re.S)
        # print pageCode
        items = re.findall(pattern, pageCode)
        # 用来存储每页的段子们
        pageStories = []
        # 遍历正则表达式匹配的信息
        for item in items:
            # 判断是否已经展示全文
            isAll = re.search('<span class="contentForAll">', item[3])
            content = item[2].strip()
            if isAll is not None:
                # 从段子详情页获取完整的段子
                url = 'http://www.qiushibaike.com' + item[1]
                requ = urllib.request.Request(url, headers=self.headers)
                response = urllib.request.urlopen(requ)
                contentCode = response.read().decode('utf-8')
                contentPattern = re.compile('<div class="content">(.*?)</div>', re.S)
                content = re.findall(contentPattern, contentCode)[0].strip()
                content.replace("\n", "<br/>")
            # 判断是否有图片
            imgSrc = re.findall('<img src="//(.*?)"', item[4])
            if not imgSrc:
                # 不包含图片
                # 作者 内容 图片链接 赞数
                pageStories.append([item[0].strip(), content, "", item[5].strip()])
            else:
                pageStories.append([item[0].strip(), content, imgSrc[0].strip(), item[5].strip()])
        return pageStories

    # 加载并提取页面的内容，加入到列表中
    def loadPage(self):
        # 获取新一页
        pageStories = self.getPageItems(self.pageIndex)
        # 将该页的段子存放到全局list中
        if pageStories:
            self.stories.append(pageStories)

    def printStory(self, pageStories, page):
        # 遍历一页的段子
        for story in pageStories:
            if story[2] == "":
                # 无图段子
                self.file.write(u'{"author":"%s","content":"%s","type":"110"}\n' % (story[0], story[1]))
                print(u"第%d页\t发布人:%s\n%s\n赞:%s\n" % (page, story[0], story[1], story[3]))
            else:
                # 有图段子
                self.file.write(
                    u'{"author":"%s","content":"%s","img":"%s","type":"100"}\n' % (story[0], story[1], story[2]))
                print(u"第%d页\t发布人:%s\n%s\n图片:%s\n赞:%s\n" % (page, story[0], story[1], story[2], story[3]))

    # 开始方法
    def start(self):
        print(u"正在读取糗事百科,请稍后...")
        while self.pageIndex <= 13:
            # 加载内容
            self.loadPage()
            # 从全局list中获取一页的段子
            pageStories = self.stories[0]
            # 将全局list中第一个元素删除，因为已经取出
            del self.stories[0]
            # 输出该页的段子
            self.printStory(pageStories, self.pageIndex)
            # 获取完之后页码索引加一，表示下次读取下一页
            self.pageIndex += 1
        else:
            print("完毕")


if __name__ == '__main__':
    spiderQSBK = QSBK()
    spiderQSBK.start()
