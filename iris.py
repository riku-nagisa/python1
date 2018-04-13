from sklearn.datasets import load_iris
from sklearn import tree


# アヤメのデータを読み込む
iris = load_iris()

# アヤメの素性(説明変数)はリスト
# # 順にがく片の幅，がく片の長さ，花弁の幅，花弁の長さ
# print(iris.data)

# アヤメの種類(目的変数)は3種類(3値分類)

print(iris.data.shape)
# モデルを作成
clf = tree.DecisionTreeClassifier(max_depth = 3)
clf = clf.fit(iris.data, iris.target)

# 作成したモデルを用いて予測を実行
predicted = clf.predict(iris.data)

# 予測結果の出力(正解データとの比較)
print('=============== predicted ===============')
print(predicted)
print('============== correct_ans ==============')
print(iris.target)

 
