import pdfkit
import requests
from bs4 import BeautifulSoup

class Def:
  # PDFを作成する関数
  def pdf(self, url, pdfname):
    options = {  # PDFの書式を設定
        'page-size': 'A4',
        'margin-top': '0',
        'margin-right': '0',
        'margin-left': '0',
        'margin-bottom': '0',
        'zoom': '1.0',
        'encoding': "UTF-8",
        'javascript-delay': '30000'  # JavaScriptの完了を30秒間待つ（数式の表示等）
    }
    pdfkit.from_url(url, pdfname, options=options)  # URLからPDFを作成

  # タイトルを取得する関数
  def title(self, url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.find(class_='c-blog-article__title')  # タイトルを取得
    if title:
        pdfname = title.text.strip() + '.pdf'  # テキストから前後の空白を削除
        return pdfname
    else:
        return "Title not found.pdf"  # タイトルが見つからなかった場合
    
  # メイン関数
  def main(self, url):
    pdfname = self.title(url)  # タイトルを取得
    self.pdf(url, pdfname)  # PDFを作成

if __name__ == '__main__':
  for i in range(0, 79):
    if i == 0:
      url = "https://www.hinatazaka46.com/s/official/diary/member/list?ima=0000&ct=6"
      Def().main(url)
    else:
      url = "https://www.hinatazaka46.com/s/official/diary/member/list?ima=0000&page=" + str(i) + "&ct=6&cd=member"
      Def().main(url)
