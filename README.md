# iDoulist 爱豆列
## 简述
- 我们观察到在豆瓣进行图书豆列管理时的一些问题:
  1. 不能实现在指定豆列中找书,当豆列很长(如开智书单)时尤其麻烦
  2. 无法比较几个豆列是否重叠
  3. 无法导出豆列(及书籍信息)到文件永久保存
- 我们认为这些问题都可以通过人工重复劳动来解决,但繁琐并耗时,不是长久之计.对于开智群友更是时间的巨大浪费.
- 所以 iDoulist 被设计来解决豆列的这些问题, 帮助我们更加方便地使用豆瓣的大量书籍信息.


## 如何安装使用: 
- 在 OS X 10.10.4 测试正常
- Python 2.7.9
- 需要安装的依赖包
  - 用于输出到文件 jinja2
  - 用于输出到豆列网页 pyobjc-core, pyobjc, PyAutoGUI
  - 用于输出标签云 numpy, matplotlib
- 下载 zip 或 clone 项目到本地, 运行 `iDoulist/iDoulist_main.py`
- 功能使用
  - 输入列表: 支持输入`豆列`或`想读/已读/未读链接`
     - 豆列例: `http://www.douban.com/doulist/37723990/`
     - 在读例: `http://book.douban.com/people/irislee0923/do`
  - iDoulist 通过建立一个**书单**存储图书. 导入时, 可把一个豆列或两个豆列按指定模式导入到书单; 导出时, 将把这个书单的内容导出
  - 输出到豆列: 
    - 正确输出到豆列, 需要在当前屏幕中有一个豆瓣页面, 并显示出"添加内容"的绿色按钮(参考 `iDoulist/output/add_button.png`)
      - 如果软件始终无法识别到有效按钮(提示`没有找到有效的"添加内容"按钮, 请检查后再次导出.`), 请在本地截取绿色按钮图片, 覆盖到 `iDoulist/output/add_button.png`
    - 运行过程中由于 PyAutoGUI 会进行鼠标键盘操作, 不建议同时进行任何其它操作.
    - 长豆列的导入可能会需要几分钟甚至几十分钟
    - 如需停止, 可把鼠标移动到屏幕左上角(启动 PyAutoGUI 的[`Fail-Safes`](http://pyautogui.readthedocs.org/en/latest/introduction.html#fail-safes) 功能), 或进入 terminal 按 Ctrl-C
    - 目前原型测试仅在 Chrome (42.0.2311.152) 中进行过, 不保证其它浏览器可运行(特别是按钮图片在不同浏览器中可能不同). 但原则上, 其它浏览器更改图片后应可运行.

## 项目成员
- [Frank Hu](https://github.com/Frank-the-Obscure), [教程](https://www.gitbook.com/book/frank-the-obscure/pythoncamp0/details)
- [Iris Lee](https://github.com/nicetag), 教程?
- [zshaolin](https://github.com/zshaolin), [教程](https://github.com/zshaolin/pythoncamp0)
- [huhu zhu](https://github.com/huhu8), [教程](https://github.com/huhu8/pythoncamp0)