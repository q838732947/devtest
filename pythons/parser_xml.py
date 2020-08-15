import xml.sax

import xml.dom.minidom


def write_xml():
    # 在内存中创建一个空的文档
    doc = xml.dom.minidom.Document()
    # 创建一个根节点companys对象
    root = doc.createElement('companys')
    print('添加的xml标签为：', root.tagName)

    # 给根节点添加属性
    root.setAttribute('name', '公司信息')
    # 将根节点添加到文档对象中
    doc.appendChild(root)

    # 给根节点添加一个叶子节点
    company = doc.createElement('gloryroad')
    # 叶子节点下再嵌套叶子节点
    name = doc.createElement('name')
    # 给节点添加文本节点
    name.appendChild(doc.createTextNode('光荣之路'))

    ceo = doc.createElement('CEO')
    ceo.appendChild(doc.createTextNode('吴老师'))
    # 将各叶子节点添加到父节点company中
    company.appendChild(name)
    company.appendChild(ceo)
    # 将company节点添加到根节点companys中
    root.appendChild(company)

    # 此处需要用codecs.open可以指定编码方式
    fp = open('company.xml', 'w', encoding='utf-8')
    # 将内存中的xml写入到文件
    doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding='utf-8')
    fp.close()


def read_xml(filepath):
    DOMTree = xml.dom.minidom.parse(filepath)
    booklist = DOMTree.documentElement
    print(booklist.toxml())
    print(booklist.firstChild)
    books = booklist.getElementsByTagName
    print(booklist.getElementsByTagName('book')[0].toxml())


class BookHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.title = ""
        self.author = ""
        self.pageNumber = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "book":
            print("*****book*****")
            category = attributes["category"]
            print("category:", category)

    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "title":
            print("title:", self.title)
        elif self.CurrentData == "author":
            print("author", self.author)
        elif self.CurrentData == "pageNumber":
            print("pageNumber", self.pageNumber)
        self.CurrentData = ""

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "author":
            self.author = content
        elif self.CurrentData == "pageNumber":
            self.pageNumber = content


def sax_parser():
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # 重写 ContextHandler
    Handler = BookHandler()
    parser.setContentHandler(Handler)
    parser.parse("book.xml")


def dom_parser():
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse("book.xml")
    collection = DOMTree.documentElement
    if collection.hasAttribute("booklist"):
        print("Root element : %s" % collection.getAttribute("booklist"))
    # 在集合中获取所有book
    books = collection.getElementsByTagName("book")
    # 打印book的详细信息
    for book in books:
        print("*****Book*****")
        if book.hasAttribute("category"):
            print("category:%s" % book.getAttribute("category"))

        title = book.getElementsByTagName("title")[0]
        print("title:%s" % title.childNodes[0].data)
        author = book.getElementsByTagName("author")[0]
        print("author:%s" % author.childNodes[0].data)
        pageNumber = book.getElementsByTagName("pageNumber")[0]
        print("pageNumber:%s" % pageNumber.childNodes[0].data)


def main():
    # write_xml()
    # read_xml(filepath="book.xml")
    # sax_parser()
    dom_parser()


if __name__ == '__main__':
    main()
