#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------
#Title: 入力された西暦を和暦に変換する。
#Author: Shunsuke Wada
#Data: 2020/3/18(金)
#Memo: 645年から2022年までの和暦に対応
#-------------------------------------------

a = int(input('西暦を入力してください。\n'))

#飛鳥時代(大化)
if(a >= 645 and a <= 649):
    str_nengo = '大化'
    int_year = a - 644
    if(int_year == 1):
        print('西暦', a, '年は飛鳥時代の', str_nengo, '元年です。\n',sep = '' )
    else:
        print('西暦', a, '年は飛鳥時代の', str_nengo, int_year, '年です。\n', sep = '')

#飛鳥時代(白雉)
elif(a >= 650 and a <= 654):
    str_nengo = '白雉'
    int_year = a - 649
    if(int_year == 1):
        int_lastYear = a - 644 
        str_lastYear = '大化'
        print('西暦', a, '年は飛鳥時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は飛鳥時代の', str_nengo, int_year, '年です。\n', sep = '')

#飛鳥時代(朱鳥)
elif(a == 686):
    str_nengo = '朱鳥'
    int_year = a - 685
    if(int_year == 1):
        print('西暦', a, '年は飛鳥時代の', str_nengo, '元年です。\n', sep = '')

#飛鳥時代(大宝)
elif(a >= 701 and a <= 703):
    str_nengo = '大宝'
    int_year = a - 700
    if(int_year == 1):
        print('西暦', a, '年は飛鳥時代の', str_nengo, '元年です。\n', sep = '')
    else:
        print('西暦', a, '年は飛鳥時代の', str_nengo, int_year, '年です。\n', sep = '')

#飛鳥時代(慶雲)
elif(a >= 704 and a <= 707):
    str_nengo = '慶雲'
    int_year = a - 703
    if(int_year == 1):
        int_lastYear = a - 700
        str_lastYear = '大宝'
        print('西暦', a, '年は飛鳥時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は飛鳥時代の', str_nengo, int_year, '年です。\n', sep = '')

#飛鳥時代(和銅)
elif(a >= 708 and a <= 709):
    str_nengo = '和銅'
    int_year = a - 707
    if(int_year == 1):
        int_lastYear = a - 703
        str_lastYear = '慶雲'
        print('西暦', a, '年は飛鳥時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は飛鳥時代の', str_nengo, int_year, '年です。\n', sep = '')

#奈良時代(和銅)
elif(a >= 710 and a <= 714):
    str_nengo = '和銅'
    int_year = a - 707
    if(int_year >= 1):
        print('西暦', a, '年は奈良時代の', str_nengo, int_year, '年です。\n', sep = '')

#奈良時代(霊亀)
elif(a >= 715 and a <= 716):
    str_nengo = '霊亀'     
    int_year = a - 714
    if(int_year == 1):
        int_lastYear = a - 707
        str_lastYear = '和銅'
        print('西暦', a, '年は奈良時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は奈良時代の', str_nengo, int_year, '年です。\n', sep = '')

#奈良時代(養老)
elif(a >= 717 and a <= 723):
    str_nengo = '養老'
    int_year = a - 716
    if(int_year == 1):
        int_lastYear = a - 714
        str_lastYear = '霊亀'
        print('西暦', a, '年は奈良時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は奈良時代の', str_nengo, int_year, '年です。\n', sep = '')

#奈良時代(神亀)
elif(a >= 724 and a <= 728 ):
    str_nengo = '神亀'
    int_year = a - 723
    if(int_year == 1):
        int_lastYear = a - 716
        str_lastYear = '養老'
        print('西暦', a, '年は奈良時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は奈良時代の', str_nengo, int_year, '年です。\n', sep = '')

#奈良時代(天平)
elif(a >= 729 and a <= 748 ):
    str_nengo = '天平'
    int_year = a - 728
    if(int_year == 1):
        int_lastYear = a - 723
        str_lastYear = '神亀'
        print('西暦', a, '年は奈良時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は奈良時代の', str_nengo, int_year, '年です。\n', sep = '')

#奈良時代(天平感宝)
elif(a == 749):
    str_nengo = '天平感宝'
    int_year = a - 748
    if(int_year == 1):
        int_lastYear = a - 728
        str_lastYear = '天平'
        print('西暦', a, '年は奈良時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')

#奈良時代(天平宝字)
elif(a == 757):
    str_nengo = '天平宝字'
    int_year = a - 756
    if(int_year == 1):
        print('西暦', a, '年は奈良時代の', str_nengo, '元年です。\n', sep = '')

#奈良時代(天平神護)
elif(a == 765):
    str_nengo = '天平神護'
    int_year = a - 764
    if(int_year == 1):
        print('西暦', a, '年は奈良時代の', str_nengo, '元年です。\n', sep = '')

#奈良時代(天平感宝)
elif(a == 767):
    str_nengo = '神護景雲'
    int_year = a - 766
    if(int_year == 1):
        print('西暦', a, '年は奈良時代の', str_nengo, '元年です。\n', sep = '')

#奈良時代(宝亀)
elif(a >= 770 and a <= 780):
    str_nengo = '宝亀'
    int_year = a - 769
    if(int_year == 1):
        print('西暦', a, '年は奈良時代の', str_nengo, '元年です。\n', sep = '')
    else:
        print('西暦', a, '年は奈良時代の', str_nengo, int_year, '年です。\n', sep = '')

#奈良時代(天応)
elif(a == 781):
    str_nengo = '天応'
    int_year = a - 780
    if(int_year == 1):
        int_lastYear = a - 769 
        str_lastYear = '宝亀'
        print('西暦', a, '年は奈良時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')

#奈良時代(延暦)
elif(a >= 782 and a <= 793):
    str_nengo = '延暦'
    int_year = a - 781
    if(int_year == 1):
        int_lastYear = a - 780
        str_lastYear = '天応'
        print('西暦', a, '年は奈良時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は奈良時代の', str_nengo, int_year, '年です。\n', sep = '')

#平安時代(延暦)
elif(a >= 794 and a <= 802):
    str_nengo = '延暦'
    int_year = a - 781
    if(int_year >= 1):
        print('西暦', a, '年は平安時代の', str_nengo, int_year, '年です。\n', sep = '')

#平安時代(大同)
elif(a >= 806 and a <= 809):
    str_nengo = '大同'
    int_year = a - 805
    if(int_year == 1):
        print('西暦', a, '年は平安時代の', str_nengo, '元年です。\n', sep = '')
    else:
        print('西暦', a, '年は平安時代の', str_nengo, int_year, '年です。\n', sep = '')

#平安時代(弘仁)
elif(a >= 810 and a <= 823):
    str_nengo = '弘仁'
    int_year = a - 809
    if(int_year == 1):
        int_lastYear = a - 805
        str_lastYear = '大同'
        print('西暦', a, '年は平安時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は平安時代の', str_nengo, int_year, '年です。\n', sep = '')

#平安時代(天長)
elif(a >= 824 and a <= 833):
    str_nengo = '天長'
    int_year = a - 823
    if(int_year == 1):
        int_lastYear = a - 809
        str_lastYear = '弘仁'
        print('西暦', a, '年は平安時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は平安時代の', str_nengo, int_year, '年です。\n', sep = '')

#平安時代(承和)
elif(a >= 834 and a <= 847):
    str_nengo = '承和'
    int_year = a - 833
    if(int_year == 1):
        int_lastYear = a - 823
        str_lastYear = '天長'
        print('西暦', a, '年は平安時代の', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は平安時代の', str_nengo, int_year, '年です。\n', sep = '')



#明治
elif(a >= 1868 and a <= 1911):
    str_nengo = '明治'
    int_year = a - 1867
    if(int_year == 1):
        int_lastYear = a - 1864
        str_lastYear = '慶応'
        print('西暦', a, '年は', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は', str_nengo, int_year, '年です。\n', sep = '')

#大正
elif(a >= 1912 and a <= 1925):
    str_nengo = '大正'
    int_year = a - 1911
    if(int_year == 1):
        iint_lastYear = a - 1867
        str_lastYeat = '明治'
        print('西暦', a, '年は', str_nengo, '元年(', str_lastYear, int_lastYear,'年)です。\n', sep = '')
    else:
        print('西暦', a, '年は', str_nengo, int_year, '年です。\n', sep = '')

#昭和
elif(a >= 1926 and a <= 1988):
    str_nengo = '昭和'
    int_year = a - 1925
    if(int_year == 1):
        int_lastYear = a - 1911
        str_lastYear = '大正'
        print('西暦', a,'年は', str_nengo, '元年(', str_lastYear, int_lastYear, '年)です。\n', sep = '' )
    else:
        print('西暦', a, '年は', str_nengo, int_year, '年です。\n', sep = '')

#平成
elif(a >= 1989 and a <= 2018):
    str_nengo = '平成'
    int_year = a - 1988
    if(int_year == 1):
        intlastYear = a - 1925
        str_lastYear = '昭和'
        print('西暦', a, '年は', str_nengo, '元年は(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は', str_nengo, int_year, '年です。\n', sep = '')

#令和
elif(a >= 2019 and a <= 2022):
    str_nengo = '令和'
    int_year = a - 2018
    if(int_year == 1):
        int_lastYear = a - 1988
        str_lastYear = '平成'
        print('西暦', a, '年は', str_nengo, '元年は(', str_lastYear, int_lastYear, '年)です。\n', sep = '')
    else:
        print('西暦', a, '年は', str_nengo, int_year, '年です。\n', sep = '')

elif(a < 645):
    print('西暦', a, '年は、かなり古い時代のため和暦がありません。\n', sep = '')

elif(a > 2022):
    print('西暦', a, '年は、未来に行ってます。\n', sep = '')

else:
    print('西暦', a, '年は、年表記の欠番です。\n', sep = '')
