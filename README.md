# Welcome to Bonagit Store! :chocolate_bar:

## Tugas 2 PBP - Shaine Glorvina Mathea
Link Deployment PWS : http://shaine-glorvina-bonagitstore.pbp.cs.ui.ac.id/

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, saya membuat direktori dan repositori baru pada GitHub untuk project e-commerce ini. Kemudian, saya menghubungkan direktori lokal dengan repositori saya dengan cara ```git branch -M main``` kemudian ```git remote add origin https://github.com/glorvibop/bonagit-store.git```

Selanjutnya, saya melanjutkan dengan mengikuti Tutorial 0 untuk mengatur Django, yang meliputi langkah-langkah seperti mengaktifkan _virtual environment_ (untuk memastikan project saya terisolasi) dan menginstall dependencies yang diperlukan. Kemudian, saya melakukan beberapa modifikasi pada ```settings.py``` dan menambahkan berkas ```.gitignore``` untuk mengelola file yang tidak perlu diunggah ke repositori. Proses selanjutnya adalah pembuatan aplikasi Django, konfigurasi routing, dan berbagai persiapan lain sebagaimana diuraikan dalam Tutorial 0.

Setelah melakukan hal yang disebut di atas, saya membuka PWS (Pacil Web Service) untuk membuat project baru. Saya melakukan modifikasi pada ```settings.py```, menambahkan URL deployment PWS, yaitu shaine-glorvina-bonagitstore.pbp.cs.ui.ac.id, dan melanjutkan prosedur deployment PWS sesuai dengan instruksi dalam Tutorial 0.

Di dalam aplikasi utama, saya mendefinisikan sebuah model ```ChocolateProduct``` yang mencakup atribut ```name_product``` dengan tipe data ```CharField```, ```price``` dengan tipe data ```FloatField```, ```description``` dengan tipe data ```TextField```, ```type``` dengan tipe data ```CharField```, dan ```cocoa_ratio``` dengan tipe data ```IntegerField```. Hal ini merupakan langkah fundamental karena model bertindak sebagai blueprint untuk data yang disimpan, diproses, dan dikelola dalam aplikasi saya.

Kemudian, saya melanjutkan pengembangan aplikasi e-commerce saya yang berfokus pada penjualan chocolate bar dengan memodifikasi ```views.py```. Dalam file ini, saya menampilkan data dari model dan menghubungkannya dengan template. Fungsi ```show_main``` mengatur variabel konteks dengan nilai seperti product name, price, description, type,  cocoa ratio, yang kemudian ditampilkan melalui template ```main.html```. Template tersebut saya modifikasi sesuai dengan keinginan saya agar terlihat lebih menarik. Terakhir, saya menyambungkan repository dengan PWS, lalu push ke PWS dengan ```git push pws main:master``` untuk melakukan deployment.

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![flowchart untuk pbp](https://github.com/user-attachments/assets/36b3d355-83fa-4207-9570-fac7ec54425d)
- Client send request (mengirimkan HTTP request ke server Django)
- Server Django memproses request yang diterima dengan mencocokkan URL yang diminta ke pola-pola yang terdefinisi dalam file ```urls.py```. File ini berperan penting dalam mengelola rute URL yang terkait dengan aplikasi utama.
- Request diproses oleh ```views.py``` yang mengambil dan memproses data dari database melalui ```models.py```. ```models.py``` sendiri bertanggung jawab untuk mengatur dan mengelola data dari aplikasi. Setelah menyelesaikan tindakan sebelumnya, ```views.py``` menentukan jenis respons yang dikirimkan kembali ke client (umumnya menggunakan template HTML).
- Setelah ```views.py``` mengumpulkan data yang diperlukan, data dikirim ke sebuah berkas HTML yang berfungsi sebagai template. Berkas ini memperlihatkan tampilan akhir yang dapat dilihat oleh client.
- Django merespon dengan mengirimkan HTML yang sudah diproses sebagai respon kembali ke client.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
```Git``` adalah _version control system_ yang paling umum digunakan. Sebagai _version control system_, ```Git``` memungkinkan developers untuk melihat riwayat modifikasi yang lengkap, mengidentifikasi siapa yang membuat perubahan, kapan, dan mengapa. Hal ini berarti ```Git``` bersigat dinamis, adaptif, dan penting untuk menganalisis bug.

Fitur utama ```Git``` meliputi _Branching and Merging_ yang developers untuk mengerjakan bagian proyek yang berbeda secara bersamaan tanpa mengganggu satu sama lain. Kelebihan ini memastikan perubahan dapat di-merge kembali ke main branch dengan mulus dan menjaga integritas kode.

Selain itu, ```Git``` mendukung development yang terdistribusi. Hal mempercepat proses rilis perangkat lunak dengan memungkinkan pembaruan yang sering dan kecil, sehingga mempercepat siklus rilis secara keseluruhan.

#### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena sebelumnya kami telah mempelajari bahasa pemrograman Python yang juga digunakan dalam Django. Di lingkungan industri, Django merupakan salah satu framework yang umum digunakan dan menawarkan simplicity, flexibility, reliability, dan scalability. Hal ini berarti Django telah memiliki komunitas yang cukup luas. Django juga memiliki syntax yang relatif mudah dan memiliki web server sendiri membuatnya lebih secure dari framework lain.

### 5. Mengapa model pada Django disebut sebagai ORM?
Models pada Django disebut sebagai ORM (_Object Relational Mapping_) karena Models pada Django menyediakan sebuah lapisan abstraksi yang memungkinkan developers untuk melakukan pemetaan data (_mapping_) tanpa perlu menulis SQL secara manual. Sebagai gantinya, developers bisa berinteraksi dengan database menggunakan bahasa Python.