# Knn Tahmin
iris veriseti kullanılarak yapılmıştır.
Verisetindeki etiketlerin silinmesi gerekmektedir. Sadece hücrelerdeki eksik verileri tahmin etmektedir.

# Kurulum
```
pip3 install -r requirenments
```

# Kullanım

- Elinizdeki verisetinin etiketlerini temizleyin
- Tahmin etmesini istediğiniz hücrenin satırını ```knn_sorgu.xlsx``` adlı excel dosyasının içine yapıştırın.
- Çıktı olarak ```knn_tahmin.xlsx``` adlı bir çıktı vermektedir

## Eksikleri

- Satırların son hücrelerindeki veriler eksik olursa tahmin etmiyor
- Kod yazımı karışık


