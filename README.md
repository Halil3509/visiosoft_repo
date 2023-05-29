Merhabalar, ben Halil İbrahim. Yukarıda bahsettiğim sistem, sokaktaki levhaların (Information Plate) ve Mağaza yazılarının (Shop Sign) tespit işlemini içemektedir. Bu uygulamasının yapımında object detection modeli olarak 
Yolov5 modelini kullandım. 

<h3> Yolov5 nedir?  </h3> </br>

<img src = 'https://user-images.githubusercontent.com/26833433/127574988-6a558aa1-d268-44b9-bf6b-62d4c605cc72.jpg'>

YOLOv5, birçok farklı uygulama alanında kullanılabilir. Nesne algılama, otonom sürüş, güvenlik sistemleri, nesne takibi, nesne sayımı ve benzeri birçok görsel işleme probleminde kullanılabilecek genel bir algoritmadır.

YOLOv5, daha hızlı ve daha doğru sonuçlar elde etmek için bir dizi geliştirme içerir. İleriye dönük öğrenme, tamamlayıcı bağlantılar (skip connections), büyük ölçekli veri setleriyle eğitim ve çok çeşitli nesne türlerini algılama yetenekleri gibi özelliklerle birlikte gelir.

YOLOv5, önceden eğitilmiş bir model olarak kullanılabildiği gibi, kullanıcının özelleştirebileceği bir eğitim süreci de sunar. Bu şekilde, kullanıcı, kendi veri setine veya belirli bir uygulamaya odaklanmak için modeli özelleştirebilir ve eğitebilir.

<h3> Yolo Algoritması Nasıl Çalışır?  </h3> </br>

1. Giriş Görüntüsünü Bölme:
İlk adımda, giriş görüntü küçük kare bölgelere ayrılır. Bu bölgelere "anchor box" denir ve her biri belirli bir nesne sınıfını temsil eder. Her kare bölgeye bir çerçeve tahmin edilir.

2. Öznitelik Çıkarımı:
YOLO, derin bir sinir ağı kullanarak görüntüden özniteliklerin çıkarılmasını gerçekleştirir. Bu işlem, genellikle önceden eğitilmiş bir sinir ağı olan bir evrişimli sinir ağı (Convolutional Neural Network - CNN) ile yapılır. CNN, görüntüdeki önemli desenleri ve öznitelikleri belirlemek için farklı katmanlarda konvolüsyon işlemleri uygular.

3. Bölge Özelliklerinin Tahmini:
Öznitelik çıkarımı sonrasında, her bir bölge için sınıflandırma ve konum tahmini yapılır. Bu tahminler, önceden tanımlanan sınıf etiketlerini ve çerçeve koordinatlarını içerir. Her bir bölge için sınıflandırma tahmini, o bölgedeki nesnenin hangi sınıfa ait olduğunu gösterirken, konum tahmini, nesnenin çerçeve koordinatlarını (sol üst köşe koordinatı, genişlik ve yükseklik) belirtir.

4. Çerçeve Düzenleme:
Tahmin edilen çerçeve koordinatları, bölgenin orijinal görüntü koordinatlarına dönüştürülür. Bu, bölgenin tam konumunu belirlemek için yapılan bir adımdır.

5. Sonuç Filtrasyonu:
Çerçeve tahminlerinin birçoğu genellikle aşırı tahminlere ve düşük güvenlik skorlarına sahiptir. Bu nedenle, son adımda, belirli bir güvenlik skoru eşiğini geçmeyen çerçeveler filtrelenir. Ayrıca, çakışan çerçeveler arasından en yüksek güvenlik skoruna sahip olan çerçeve seçilir.

<img src= 'https://user-images.githubusercontent.com/35373818/138246321-65a8ff3c-df6e-4df5-a12e-6977e5b844a8.jpeg'>


<h3> Prediction İşlemini Nasıl Yaparım? </h3> </br>
1. Öncelikle, <i> prediction_script.py </i> dosyası klonlaması yapılan yolov5 klasörünün bir içinde olmalıdır. </br>
2. Ardından konsola <i> python prediction_script.py </i> yazarak default parametreler üzerinden prediction işlemimizi gerçekleştirebiliriz. </br>
3. Örnek olarak bir model ağırlığını parametre olarak verecek olursak: <i> python prediction_script.py --weights path/to/best.pt </i> </br>

<h3> Örnek Sonuçlar </h3>

<img src ="https://github.com/Halil3509/visiosoft_repo/blob/main/results_5/val_batch1_pred.jpg?raw=true">


