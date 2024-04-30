import pdfkit

url = 'https://www.hinatazaka46.com/s/official/diary/member/list?ima=0000&ct=6'
url = 'https://www.hinatazaka46.com/s/official/diary/member/list?ima=0000&page=1&ct=6&cd=member'
url = 'https://www.hinatazaka46.com/s/official/diary/member/list?ima=0000&page=2&ct=6&cd=member'
options = {                                                 # PDFの書式を設定
            'page-size': 'A4',
            'margin-top': '0',
            'margin-right': '0',
            'margin-left': '0',
            'margin-bottom': '0',
            'zoom': '1.0',
            'encoding': "UTF-8",
            'javascript-delay': '30000'                     # javascriptの完了を30s間待つ(数式の表示等)
          }
pdfkit.from_url(url, 'watlab-home.pdf', options=options)    # URLからPDFを作成

for i in range(1,78)