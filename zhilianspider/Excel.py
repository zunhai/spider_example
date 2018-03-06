# -*- coding:utf-8 -*-
 
'''关于xlwt写入表格的风格的一些测试'''
 
import xlwt
 
def xlwttest():
    wk = xlwt.Workbook(encoding="utf-8")
    sheet_test = wk.add_sheet("test")
 
    # 设置列宽
    for c in range(5):
        sheet_test.col(c).width = 256 * 20
 
    # 颜色测试
    for fsize in range(100):
        font = xlwt.Font()
        # font.name = "Arial"    #字体名称
        # font.bold = True  # 字体加粗
        font.height = 20 * 11  # 字体决定了行高，后面一个数字可以决定字体型号
        font.colour_index = fsize
        style_1 = xlwt.XFStyle()
        style_1.font =font
        sheet_test.write(fsize,0,"字体颜色代号{}".format(fsize),style_1)
    # 背景色测试
    for bgnum in range(100):
        patterni = xlwt.Pattern()
        patterni.pattern = xlwt.Pattern.SOLID_PATTERN
        patterni.pattern_fore_colour = bgnum
        style_2 = xlwt.XFStyle()
        style_2.pattern = patterni
        sheet_test.write(bgnum,1,"背景色代号{}".format(bgnum),style_2)
 
    # 另一种设置风格的方式，更便捷
    for n in range(100):
        style_3 = xlwt.easyxf("font: name Times New Roman,color-index 20,bold on")
        sheet_test.write(n,2,"另一种风格使用",style_3)
 
    # 插入图片测试，但是图片的格式是bmp的才行，这是个大坑啊
    '''
    insert_bitmap(img, x, y, x1, y1, scale_x=0.1, scale_y=2)
    img表示要插入的图像地址
    x表示行
    y表示列
    x1表示相对原来位置向下偏移的像素
    y1表示相对原来位置向右偏移的像素
    scale_x表示相对原图宽的比例，图片可放大缩小
    scale_y表示相对原图高的比例，图片可放大缩小
    '''
    for i in range(4):
        sheet_test.insert_bitmap("gakki.bmp",i,3,2,2,0.1,0.1)
 
    合并单元格测试
    '''
    write_merge(x, x + h, y, w + y, string, sytle)
    x表示行，y表示列，w表示跨列个数，h表示跨行个数，string表示要写入的单元格内容，style表示单元格样式
    注意，x，y，w，h，都是以0开始计算的
    '''
    sheet_test.write_merge(0,0+3,4,4+3,"合并测试")
 
    # 保存表格
    wk.save("xlwt_test.xls")
 
if __name__ == '__main__':
    xlwttest()