import urllib2

#index = []

def add_to_index(index,keyword,url):
       i=0
       flag=0
       for e in index:
            if e[0]==keyword:
                flag=1
                break
            i=i+1
       if flag==0:
                index.append([keyword,[url]])
       if flag==1:
                    index[i][1].append(url)

def add_page_to_index(index,url,content):
    split_content=content.spilt()
    for e in split_content:
        add_to_index(index,e,url)
        


def lookup(index,keyword):
    for search in index:
        if keyword==search[0]:
            return search[1]
    return []  
      

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
    index=[]

    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
	    content=urllib2.urlopen(page).read()
	    add_page_to_index(index,page,content)
            union(next_depth, get_links(contents))
            crawled.append(page)
      
    return index

