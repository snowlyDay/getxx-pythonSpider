# encoding=utf-8

import urllib.request as urllib

from bs4 import BeautifulSoup
import os 

debug = True # 设置是否打印log
def log(message):
    if debug:
        print( message)

def download_image(url, save_path): 
    ''' 根据图片url下载图片到save_path '''
    try:
        urllib.urlretrieve(url, save_path)
        log('Downloaded a image: ' + save_path)
    except Exception  as e:
        print ('An error catched when download a image:',e)

def load_page_html(url):
    ''' 得到页面的HTML文本 '''
    log('Get a html page : ' + url)
    return urllib.urlopen(url).read()

def down_page_images(page, save_dir):
    ''' 下载第page页的图片 '''
    html_context = load_page_html('http://qiubaichengren.com/%d.html' % page)
    soup = BeautifulSoup(html_context)
    for ui_module_div in soup.findAll('div', {'class': 'ui-module'}):
        img_tag = ui_module_div.find('img')
        if img_tag is not None and img_tag.has_attr('alt') and img_tag.has_attr('src'):
            alt = img_tag.attrs['alt'] # 图片的介绍
            src = img_tag.attrs['src'] # 图片的地址
            filename = '%s%s' % (alt, src[-4:]) # 取后四位（有的图片后缀是'.jpg'而有的是'.gif'）
            download_image(src, save_dir + filename)

def download_qbcr(frm=1, page_count=1, save_dir='./'):
    for x in range(frm, frm + page_count):
        log('Page :'+ str(x))
        down_page_images(x, save_dir)

def main():
    base_path = os.path.abspath('.')
    path  = base_path+"\深藏不露/"
    if not os.path.exists(path):
          os.mkdir(path)
    # print(path)
    download_qbcr(frm=1, page_count=50, save_dir=path)

if __name__ == '__main__':
    main()