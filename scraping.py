import re
import requests
from bs4 import BeautifulSoup
# Make a request
# article_url = 'https://www.liputan6.com/news/read/4896858/negara-suntik-modal-ke-bsi-wapres-maruf-minta-kesepakatan-sesuai-aturan'
article_url = 'https://akurat.co/rusia-resmi-nyatakan-perang-sejumlah-ledakan-terdengar-di-kota-kota-ukraina'
# article_url ='https://www.antaranews.com/berita/2723205/menaker-berdialog-dengan-kasbi-dengar-aspirasi-revisi-aturan-jht'
# article_url= 'https://international.sindonews.com/read/695263/41/breaking-news-putin-luncurkan-operasi-militer-rusia-di-ukraina-timur'
# article_url = 'https://www.republika.co.id/berita/r7sxar409/who-umumkan-tren-penurunan-kasus-covid19-inikah-tanda-akhir-pandemi'
url = article_url + '?&page=all&single=1';
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

np = soup.select('div.post-content')
np1 = soup.select('div.detail-desc')
np2 = soup.select('div.blog-content')
p = soup.select('p')
result =[]

for a in p:
  for z in soup.findAll(["span", "strong", "em", "b", "i", "iframe", "a", "section", "label", "header", "blockquote", "h2", "li", "h1"]):
    z.decompose()
    for x in soup.findAll('div', {'class':['wrap_next_artikel', 'wrap_footer']}):
      x.decompose()

  result.append(a.text.strip())
for b in np:
  result.append(b.text.strip())
for c in np1:
  z = soup.find('div', attrs={'class':'ads300 mt20 adsload'})
  z = soup.find('div', attrs={'class':'box-outlink'})
  z.decompose()
  result.append(c.text.strip())
for e in np2:
  # for z in soup.findAll(["script", "style"]):
  #   z.decompose()
  result.append(e.text.strip())

for r in result:
  if len(r)>0:
    print(r)
