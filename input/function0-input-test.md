# Function0 input test

Author: Frank Hu

test in python 2.7.9, 20150507

## standard test of function 0 input

- input 1: `url = 'http://www.douban.com/doulist/38390646/'`
  - 有2本书的书单
- output 1: `doulist_content = ['http://book.douban.com/subject/1139336/', 'http://book.douban.com/subject/25724948/']`

---

- input 2: `url = 'http://www.douban.com/doulist/37668712/'`
  - 有11本书的书单
- output 2: `doulist_content = [['http://book.douban.com/subject/6811366/', 'http://book.douban.com/subject/21372167/', 'http://book.douban.com/subject/1322408/', 'http://book.douban.com/subject/2328178/', 'http://book.douban.com/subject/1230487/', 'http://book.douban.com/subject/1974704/', 'http://book.douban.com/subject/4929844/', 'http://book.douban.com/subject/4836530/', 'http://book.douban.com/subject/6510688/', 'http://book.douban.com/subject/1462696/', 'http://book.douban.com/subject/1065156/']]`

---

- input 3: `url = 'http://www.douban.com/doulist/14090587/'`
  - 作者群书单:第一页有25本书
- output 3: `doulist_content = ['http://book.douban.com/subject/1059751/', 'http://book.douban.com/subject/1223043/', 'http://book.douban.com/subject/26326498/', 'http://book.douban.com/subject/25967509/', 'http://book.douban.com/subject/10352395/', 'http://book.douban.com/subject/6047885/', 'http://book.douban.com/subject/25850377/', 'http://book.douban.com/subject/2370630/', 'http://book.douban.com/subject/1898860/', 'http://book.douban.com/subject/26288194/', 'http://book.douban.com/subject/25881360/', 'http://book.douban.com/subject/10430741/', 'http://book.douban.com/subject/26335642/', 'http://book.douban.com/subject/2227196/', 'http://book.douban.com/subject/26279190/', 'http://book.douban.com/subject/26340992/', 'http://book.douban.com/subject/25901055/', 'http://book.douban.com/subject/1071227/', 'http://book.douban.com/subject/1883617/', 'http://book.douban.com/subject/26306686/', 'http://book.douban.com/subject/26357758/', 'http://book.douban.com/subject/26150549/', 'http://book.douban.com/subject/26354161/', 'http://book.douban.com/subject/1065165/', 'http://book.douban.com/subject/4836530/']`