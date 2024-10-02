# Welcome to Bonagit Store! :chocolate_bar:

> Link Deployment PWS : [Bonagit Store](http://shaine-glorvina-bonagitstore.pbp.cs.ui.ac.id/)

<details>
<summary>
  <span style="font-size:16px;"><b>Tugas 2: Implementasi Model-View-Template (MVT) pada Django</b></span>
</summary>

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, saya membuat direktori dan repositori baru pada GitHub untuk project e-commerce ini. Kemudian, saya menghubungkan direktori lokal dengan repositori saya dengan cara ```git branch -M main``` kemudian ```git remote add origin https://github.com/glorvibop/bonagit-store.git```

Selanjutnya, saya melanjutkan dengan mengikuti Tutorial 0 untuk mengatur Django, yang meliputi langkah-langkah seperti mengaktifkan _virtual environment_ (untuk memastikan project saya terisolasi) dan menginstall dependencies yang diperlukan. Kemudian, saya melakukan beberapa modifikasi pada ```settings.py``` dan menambahkan berkas ```.gitignore``` untuk mengelola file yang tidak perlu diunggah ke repositori. Proses selanjutnya adalah pembuatan aplikasi Django, konfigurasi routing, dan berbagai persiapan lain sebagaimana diuraikan dalam Tutorial 0.

Setelah melakukan hal yang disebut di atas, saya membuka PWS (Pacil Web Service) untuk membuat project baru. Saya melakukan modifikasi pada ```settings.py```, menambahkan URL deployment PWS, yaitu ```shaine-glorvina-bonagitstore.pbp.cs.ui.ac.id```, dan melanjutkan prosedur deployment PWS sesuai dengan instruksi dalam Tutorial 0.

Di dalam aplikasi utama, saya mendefinisikan sebuah model ```ChocolateProduct``` yang mencakup atribut ```name_product``` dengan tipe data ```CharField```, ```price``` dengan tipe data ```FloatField```, ```description``` dengan tipe data ```TextField```, ```type``` dengan tipe data ```CharField```, dan ```cocoa_ratio``` dengan tipe data ```IntegerField```. Hal ini merupakan langkah fundamental karena model bertindak sebagai blueprint untuk data yang disimpan, diproses, dan dikelola dalam aplikasi saya.

Kemudian, saya melanjutkan pengembangan aplikasi e-commerce saya yang berfokus pada penjualan chocolate bar dengan memodifikasi ```views.py```. Dalam file ini, saya menampilkan data dari model dan menghubungkannya dengan template. Fungsi ```show_main``` mengatur variabel konteks dengan nilai seperti product name, price, description, type,  cocoa ratio, yang kemudian ditampilkan melalui template ```main.html```. Template tersebut saya modifikasi sesuai dengan keinginan saya agar terlihat lebih menarik. Terakhir, saya menyambungkan repository dengan PWS, lalu push ke PWS dengan ```git push pws main:master``` untuk melakukan deployment.

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![flowchart untuk tugas 2 individu pbp](https://github.com/user-attachments/assets/36b3d355-83fa-4207-9570-fac7ec54425d)
- Client send request (mengirimkan HTTP request ke server Django)
- Server Django memproses request yang diterima dengan mencocokkan URL yang diminta ke pola-pola yang terdefinisi dalam file ```urls.py```. File ini berperan penting dalam mengelola rute URL yang terkait dengan aplikasi utama.
- Request diproses oleh ```views.py``` yang mengambil dan memproses data dari database melalui ```models.py```. ```models.py``` sendiri bertanggung jawab untuk mengatur dan mengelola data dari aplikasi. Setelah menyelesaikan tindakan sebelumnya, ```views.py``` menentukan jenis respons yang dikirimkan kembali ke client (umumnya menggunakan template HTML).
- Setelah ```views.py``` mengumpulkan data yang diperlukan, data dikirim ke sebuah berkas HTML yang berfungsi sebagai template. Berkas ini memperlihatkan tampilan akhir yang dapat dilihat oleh client.
- Django merespon dengan mengirimkan HTML yang sudah diproses sebagai respon kembali ke client.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
```Git``` adalah _version control system_ yang paling umum digunakan. Sebagai _version control system_, ```Git``` memungkinkan developers untuk melihat riwayat modifikasi yang lengkap, mengidentifikasi siapa yang membuat perubahan, kapan, dan mengapa. Hal ini berarti ```Git``` bersigat dinamis, adaptif, dan penting untuk menganalisis bug.

Fitur utama ```Git``` meliputi _Branching and Merging_ yang developers untuk mengerjakan bagian proyek yang berbeda secara bersamaan tanpa mengganggu satu sama lain. Kelebihan ini memastikan perubahan dapat di-merge kembali ke main branch dengan mulus dan menjaga integritas kode.

Selain itu, ```Git``` mendukung development yang terdistribusi. Hal mempercepat proses rilis perangkat lunak dengan memungkinkan pembaruan yang sering dan kecil, sehingga mempercepat siklus rilis secara keseluruhan.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena sebelumnya kami telah mempelajari bahasa pemrograman Python yang juga digunakan dalam Django. Di lingkungan industri, Django merupakan salah satu framework yang umum digunakan dan menawarkan simplicity, flexibility, reliability, dan scalability. Hal ini berarti Django telah memiliki komunitas yang cukup luas. Django juga memiliki syntax yang relatif mudah dan memiliki web server sendiri membuatnya lebih secure dari framework lain.

### 5. Mengapa model pada Django disebut sebagai ORM? 
Models pada Django disebut sebagai ORM (_Object Relational Mapping_) karena Models pada Django menyediakan sebuah lapisan abstraksi yang memungkinkan developers untuk melakukan pemetaan data (_mapping_) tanpa perlu menulis SQL secara manual. Sebagai gantinya, developers bisa berinteraksi dengan database menggunakan bahasa Python.
</details>

<details>
<summary>
  <span style="font-size:16px;"><b>Tugas 3: Implementasi Form dan Data Delivery pada Django</b></span>
</summary>

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery merupakan aspek penting dalam pengimplementasian suatu platform karena bertujuan untuk memastikan bahwa pertukaran data antar komponen sistem (seperti antara _frontend_ dan _backend_ atau antar _microservices_) dilakukan dengan cara yang efisien, aman, dan konsisten. Data Delivery menjadi penting karena kebutuhan pertukaran informasi yang tepat secara real-time dan memfasilitasi komunikasi yang seamless antar komponen yang berbeda dalam sistem.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik karena lebih _readable_ bagi manusia maupun mesin. JSON juga lebih ringan dibandingkan XML dan lebih mudah diolah oleh bahasa umum di web development seperti JavaScript. Oleh karena itu, JSON lebih populer karena performanya yang lebih efisien dalam konteks pengiriman data di web.

### 3. Jelaskan fungsi dari method ```is_valid()``` pada form Django dan mengapa kita membutuhkan method tersebut?
Method ```is_valid()``` digunakan pada objek form untuk memvalidasi data dan juga error handling. Metode ini berfungsi sebagai filter untuk data yang masuk serta memastikan bahwa hanya data yang telah disaring dan bersih yang diterima oleh database.

### 4. Mengapa kita membutuhkan ```csrf_token``` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan ```csrf_token``` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan ```csrf_token``` saat membuat form di Django untuk memastikan bahwa form yang dikirimkan oleh user benar-benar dari user aslinya. Singkatnya, ```csrf_token``` melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF) yaitu serangan keamanan yang memanfaatkan sesi terautentikasi user untuk melakukan aksi tidak sah pada aplikasi web tanpa persetujuan mereka.

Jika tidak menambahkan ```csrf_token``` pada form Django, penyerang dapat memanfaatkan celah tersebut untuk melakukan aksi jahat seperti mengirimkan permintaan palsu atas nama user tanpa izin (eksploitasi data). Permintaan jahat tersebut akan dieksekusi karena tidak ada ```csrf_token``` untuk memverifikasi permintaan yang menyebabkan platform menganggap permintaan itu sah.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, saya membuat form untuk menerima input, sehingga nantinya data baru bisa ditampilkan dengan membuat file ```forms.py``` di direktori ```main```. Lalu, saya membuat view untuk handling form input user dan menyimpan ke database dengan memodifikasi sedikit method ```show_main``` dan menambahkan method baru ```create_product_entry pada``` untuk menghasilkan form yang dapat menambahkan data Product Entry (ada pada file ```views.py```). Tidak lupa saya untuk membuat template HTML pada ```main/templates``` dengan nama file ```create_product_entry.html```untuk membuat form.

Setelah itu, saya menambahkan method untuk setiap fungsi views yang akan dibuat. Fungsi tersebut disupport dengan pertama melakukan import terhadap HttpResponse dan serializers. Lalu, menambahkan method ```show_xml``` dan ```show_json``` pada ```views.py``` untuk menyimpan hasil query dari seluruh data yang ada pada entry ChocolateProduct. Untuk melihat objek dalam format XML dan JSON by ID, saya juga menambahkan method baru yang menerima parameter id juga, yaitu ```show_xml_by_id``` dan ```show_json_by_id```. Dengan menggunakan parameter id kita dapat meilihat per objek by idnya masing-masing.

Terakhir, saya juga menambahkan path URL ke dalam variabel ```urlpatterns``` pada ```urls.py``` di ```main``` untuk mengakses fungsi yang sudah di-import pada poin sebelumnya.

### 6. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
- XML
![hasil askes URL xml](https://github.com/user-attachments/assets/d69ce312-bdd6-43a5-96a0-166ccebe9dce)

- JSON
![hasil askes URL json](https://github.com/user-attachments/assets/7c1a781b-efa8-477b-9b28-18c52e609b55)

- XML by ID
![hasil askes URL xml by id](https://github.com/user-attachments/assets/4318594b-1d1d-402b-8e38-1594d3ea1670)

- JSON by ID
![hasil askes URL json by id](https://github.com/user-attachments/assets/87099bb8-005d-41b6-a5f8-a8ef1a25c8a4)
</details>

<details>
<summary>
  <span style="font-size:16px;"><b>Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django</b></span>
</summary>

### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
```HttpResponseRedirect()``` dan ```redirect()``` adalah dua metode di Django untuk mengelola pengalihan user ke URL yang berbeda, tetapi keduanya memiliki perbedaan yang signifikan dalam penggunaan dan fleksibilitas. ```HttpResponseRedirect()``` hanya mengambil single argumen yaitu URL. Sementara itu, ```redirect()``` adalah fungsi shortcut yang lebih fleksibel, mendukung nama view, model, atau URL sebagai argumen, dan secara otomatis menghasilkan URL yang sesuai untuk pengalihan.

### 2. Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan antara model Product dengan User dilakukan melalui field ForeignKey yang didefinisikan dalam model ```ChocoalteProduct```. Field ForeignKey ini menunjuk ke model ```User``` yang memungkinkan setiap produk terhubung dengan satu user tertentu (menciptakan relasi _many-to-one_). Parameter ```on_delete=models.CASCADE``` menentukan bahwa jika user dihapus, semua produk yang terhubung dengan user tersebut juga akan dihapus, memastikan integritas data.

### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah proses verifikasi identitas user (biasanya melalui username dan password) untuk memastikan user adalah benar-benar siapa yang dia claim. Sementara itu, authorization adalah langkah selanjutnya setelah autentikasi, yang menentukan hak akses user terhadap sumber daya tertentu dalam aplikasi. Pada saat login, Django terlebih dahulu melakukan authentication untuk memverifikasi identitas user. Setelah terverifikasi, Django kemudian melakukan authorization untuk menentukan akses apa saja yang boleh dilakukan oleh user tersebut.

Django menggunakan ```django.contrib.auth``` untuk authentication, yang mengelola login, logout, dan sesi user. Untuk authorization, Django mengatur hak akses melalui sistem permissions yang memungkinkan pengaturan izin spesifik untuk user atau grup. Dekorator seperti ```@login_required``` digunakan untuk membatasi akses ke fungsi tertentu hanya untuk user yang terautentikasi.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat user yang login dengan session yang disimpan dalam cookies. Session ID yang selalu unik akan disimpan pada browser user dan database setelah user berhasil login. Setiap akses halaman, Django memeriksa session ID ini untuk verifikasi login. Selain itu, cookies juga bisa menyimpan preferensi user dan melacak aktivitasnya. Namun, cookies tidak selalu aman. Cookies yang tidak aman bisa dicuri melalui serangan seperti cross-site scripting  XSS. Django memperkuat keamanan cookies dengan opsi HttpOnly yang membatasi akses JavaScript dan Secure yang memaksa penggunaan HTTPS.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama-tama, saya mengimplementasikan fitur authentication di aplikasi Django dengan mengimplementasikan fungsi registrasi, login, dan logout. Prosesnya dimulai dengan memodifikasi ```views.py``` untuk menambahkan fungsi ```register``` yang memanfaatkan form bawaan Django. Saya juga membuat halaman HTML, ```register.html```, untuk form tersebut dan mendefinisikan URL yang sesuai dalam ```urlpatterns``` untuk mengakses halaman register.

Setelah mengatur register, saya melanjutkan dengan implementasi fungsi login menggunakan modul ```authenticate``` dan ```login``` dari Django. Saya menambahkan fungsi ```login_user``` di ```views.py``` dan membuat halaman ```login.html``` yang menyediakan form login. URL untuk halaman login juga saya tambahkan pada ```urlpatterns```. Untuk logout, saya menambahkan fungsi yang memanggil logout yaitu ```logout_user``` dari Django di ```views.py```, lalu memodifikasi ```main.html``` dengan menambahkan hyperlink tag untuk logout, dan membuat URL yang sesuai untuk aksi tersebut. Setelah mengimplementasikan fungsi registrasi, login, dan logout, saya menyisipkan decorator ```@login_required(login_url='/login')``` di atas fungsi ```show_main``` agar halaman main hanya dapat diakses oleh user yang sudah login.

Selanjutnya, saya menghubungkan model ```ChocolateProduct``` dengan ```User``` menggunakan ForeignKey. Ini memungkinkan setiap produk yang dibuat saling terikat dengan user yang membuatnya. Dengan ini, terciptalah relasi _many-to-one_ dimana setiap produk dihubungkan ke satu user dan satu user bisa memiliki banyak produk. Saya memodifikasi fungsi ```create_product_entry``` untuk menyimpan produk baru dengan mengasosiasikannya dengan user yang login. Saya juga memastikan bahwa hanya produk yang terkait dengan user yang login yang ditampilkan di main page.

Terakhir, saya menambahkan fitur untuk menyimpan dan menampilkan waktu login terakhir user menggunakan cookies. Di fungsi ```login_user```, saya mengatur cookie ```last_login``` setelah user berhasil login. Saya juga memodifikasi fungsi ```logout_user``` untuk menghapus cookie tersebut. Informasi waktu login terakhir ditampilkan di main page.
</details>

<details>
<summary>
  <span style="font-size:16px;"><b>Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS</b></span>
</summary>

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
CSS menentukan prioritas selector berdasarkan konsep _specificity_. Prioritas pengamblian CSS selecetor dari terendah ke tertinggi:
- Universal Selector
- Type Selector
- Class, pseudo-class, attribute selector
- ID Selector
- Inline Styles
- !important

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design sangat penting karena tidak semua user memiliki device (desktop, table, ponsel, dsb.) yang sama. Jika sebuah design hanya disesuaikan untuk satu ukuran layar, user akan mengalami kesulitan mengakses fitur-fitur situs pada perangkat lain. Sekarang, hampir semua website sudah menerapkan responsive design untuk memastikan aksesibilitas yang baik di berbagai perangkat. Salah satu contoh website responsive adalah [Pinterest](https://id.pinterest.com/). Namun, ada juga website yang sengaja dibuat non-responsive untuk keperluan demonstrasi seperti [Non-Responsive Website](https://dequeuniversity.com/library/responsive/1-non-responsive)

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
![margin border padding content](https://github.com/user-attachments/assets/37c65fa1-e33d-4010-883d-fc7b3f42252c)
- Margin merupakan ruang di luar border elemen yang memberikan jarak antar elemen satu dengan yang lain
- Border merupakan garis yang mengelilingi elemen (berada di antara margin dan padding). Border digunakan untuk membatasi elemen dan bisa diatur ketebalannya, jenisnya (seperti solid atau dashed), serta warnanya.
- Padding merupakan ruang di dalam elemen yang memberikan jarak antara content suatu elemen dengan bordernya.

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox dan Grid adalah dua sistem tata letak CSS yang memfasilitasi pembuatan layout responsive dengan kemudahan pengaturan yang berbeda. 

- Flexbox fokus pada distribusi ruang dalam satu dimensi, memungkinkan elemen disusun secara horizontal atau vertikal di dalam kontainer. Ini sangat berguna untuk tata letak yang memerlukan penyesuaian seperti meratakan atau memusatkan elemen dengan properti seperti justify-content dan align-items. 
- Grid Layout adalah metode yang lebih kompleks dan menawarkan dua dimensi (baris dan kolom) yang mendukung pengaturan elemen yang lebih detail dan presisi menggunakan properti seperti grid-template-columns dan grid-template-rows. 

Flexbox cocok untuk tata letak sederhana seperti navigasi atau kolom produk, sedangkan Grid ideal untuk desain yang lebih kompleks dengan banyak elemen seperti layout halaman dengan area header, konten, dan sidebar yang terdefinisi dengan baik. Penggunaan kedua sistem ini memperkaya fleksibilitas dalam desain web modern, memungkinkan pembuatannya menjadi lebih dinamis dan adaptif.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Pertama, saya membuat fitur edit dan delete menu dengan menambahkan 2 function baru pada direktori ```main/views.py``` yaitu function ```edit_product``` dan ```delete_product```. Kemudian, saya membuat template untuk menampilkan view tersebut dengan menghubungkan CDN Tailwind CSS ke file ```templates/base.html```. Setelah menghubungkan Tailwind, saya membuat file ```main/templates/edit_product.html``` dan langsung styling dengan TailwindCSS. Tak lupa, saya juga mengintegrasi dengan route website dan menambahkan routing pada ```urls.py``` untuk kedua function yang telah dibuat pada ```views.py```.

Saya juga menambahkan beberapa gambar pada website saya agar tampilannya lebih menarik. Untuk melakukan hal ini, saya membuat konfigurasi static files dengan membuat direktori ```static``` yang berisi subdirektori ```css``` dan ```image``` untuk file-file yang dibutuhkan. Setelah itu, saya memodifikasi file ```settings.py``` dengan menambahkan barisan kode pada ```MIDDLEWARE``` dan ```STATIC_URL``` seperti yang ada di Tutorial 4 agar Django dapat mengelola file statis secara otomatis.

Pada direktori ```static/css``` saya menambahkan file ```global.css``` untuk melakukan styling yang diperlukan dalam website saya. Jangan lupa untuk selalu menambahkan ```{% load static %}``` pada setiap template yang ingin menggunakan static files yang telah dibuat. Saya juga telah membuat ```navbar.html``` untuk menampilkan navabar pada setiap template. Jangan lupa untuk selalu menambahkan ```{% include '<nama-file>'% }```. Saya juga membuat ```card_food.html``` serta c``card_info.html``` pada ```main/templates```. Terakhir, saya melakukan styling dengan TailwindCSS untuk setiap file.html sampai mendapatkan layout dan design yang saya inginkan.

</details>