# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request as req
import sqlite3
from contextlib import closing

url="http://su-gi-rx.com/2017/07/16/python_4/"
dbname='database.db'
conn=sqlite3.connect(dbname)
c=conn.cursor()
table_name = 'test'

def get_html():
    #urlopen()でデータ取得
    res=req.urlopen(url)

    #BeautifulSoup()で解析
    soup=BeautifulSoup(res,'html.parser')

    #任意のデータを抽出
    title1=soup.find("h1").string
    #print("title=",title1)

    p_list=soup.find_all("p")
    #print("text=",p_list)

    return [(str(title1),str(p_list))]

def create_table(tname):

    #executeメソッドでＳＯＬ文を実行する
    create_table='''create table if NOT EXISTS {0} (title varchar(64),p_list varchar(32))'''.format(tname)
    c.execute(create_table)

def insert_data(tname,data):
    insert_sql='insert into {0} (title,p_list) values(?,?)'.format(tname)
    c.executemany(insert_sql,test)
    conn.commit()

if __name__=='__main__':
    create_table(table_name)
    test=get_html()
    insert_data(table_name,test)

    select_sql = 'select * from {0}'.format(table_name)

    for row in c.execute(select_sql):
        print(row)

    conn.close()
