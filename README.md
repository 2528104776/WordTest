# WordTest
It helps people to memorize words.

1.用户打开excel文件，根据中文翻译填写单词，自动提示对错。

2.工作流程: 读取本地文件 -> 提取单词 -> 谷歌翻译 -> 写入excel

tip:
<1.本程序调用了谷歌翻译API,自动写入了excel公式。
<2.原单词在A列字体颜色设置为白色，不可见,点击A列某一具体单元格,公式栏则显示原单词。
<3.支持自定义导入单词,导入的要求:将txt文件放在和<WordTest.py>文件相同路径下。
