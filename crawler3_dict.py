import urllib2

#index = []

def add_to_index(index,keyword,url):
    if keyword in index:
	index[keyword].append(url)
    else:
        index[keyword]=[url]

def add_page_to_index(index,url,content):
    split_content=content.spilt()
    for e in split_content:
        add_to_index(index,e,url)



def lookup(index,keyword):
    if keyword in index:
	return index[keyword]
    else:
	return None


def find_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_links(page):
    links = []
    while True:
        url,endposition = find_next_target(page)
        if url:
            links.append(url)
            page = page[endposition:]
        else:
            break
    return links

def crawling_web(seed):
    tocrawl = [seed]
    crawled = []
    index={}

    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content=urllib2.urlopen(page).read()
            add_page_to_index(index,page,content)
            union(next_depth, get_links(contents))
            crawled.append(page)

    return index

