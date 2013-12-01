# GrandpaAdoramaScraper.py
import urllib2 as url

global ResultList

ResultList = []


def ArticleCheck(WD):
    Page = url.urlopen('http://www.adorama.com/catalog.tpl?op=article_' + WD)
    RawP = Page.read()
    IsJim = RawP.find('Jim_Bailey')
    if IsJim > -1:
        GoodURL = 'http://www.adorama.com/catalog.tpl?op=article_' + WD
        ResultList.append(GoodURL)

Item = 0

for i in range(1, 13):
    si = str(i)
    F = si.zfill(2)

    for j in range(1, 32):
        sj = str(j)
        M = sj.zfill(2)

        for k in range(2, 11):
            sk = str(k)
            L = sk.zfill(2)
            pDate = F + M + L
            Item += 1
            print "Checking Combination " + str(Item)
            ArticleCheck(pDate)
print "Done"
print
print
print
print
print ResultList
