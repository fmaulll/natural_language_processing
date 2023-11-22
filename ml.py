# Import library
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk 
import pandas as pd
import string
import re

data = [
    {"text": "Rusaknya Jalan Di Jl. Gatot Subroto Dari Simpang Lima Hingga Simpang Jl. Malabar Kota Bandung Rusaknya jalan dari jalan gatot subroto, terutama dari simpang lima hingga simpang jl. malabar. telah dilampirkan juga bukti foto jelas pada lampiran dibawah. tetapi hanya bagian simpang malabar saja, sedangkan bagian lain tidak sempat. dinas terkait bisa mengadakan survei dahulu mana saja bagian yg", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Saluran Air Tersumbat Mohon dibersihkan oleh dinas terkait ,saluran air tersumbat di persimpangan jl.dr.wahidin - jl.dr.rum (depan rumah nomor 5 dan 7), posisi di kota bandung ,kelurahan pasirkaliki kecamatan cicendo.saluran ini sudah diperbaiki oleh dinas bina marga namun sayang aliran air tidak berfungsi", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Jalan Rusak Bergelombang Jl. Gatot Subroto Dari Simpang Jl. Laswi Hingga Simpang Jl. Maleer Iii Kepada dinas terkait yg berwenang silahkan mengadakan survei kondisi yang sangat memprihatinkan dari jl.gatot subroto, khususnya dari simpang jl. laswi hingga simpang jl. maleer iii. jalan ini mengalami banyak masalah, seperti permukaan bergelombang, aspal terkelupas, tambalan yang bergelombang,", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Permohonan Perbaikan Jalan Pemukiman Warga Yang Rusak Permohonan perbaikan jalan warga yang rusak part 4selamat pagi kepada instansi dan lembaga yang terkait untuk menangani masalah ini kami atau saya pribadi yang menyampaikan tentang kerusakan jalan ini,meminta agar segera dilakukan perbaikan di jl mutiara 4 bandung kelurahan turangga", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Jalan Berlubang Mohon dibantu pinggir jalan / trotoar berlubang lumayan cukup dalam . posisi dekat griya pahlawan", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Saluran Air Tidak Kunjung Diselesaikan Lokasi: jalan terusan pesantren, rt04 rw11, sukamiskin, arcamanik, kota bandung kronologi: pengerjaan saluran air dengan menggali parit dan membongkar akses masuk ke rumah warga dilakukan kira2 pada pertengahan juli 2023, hingga kini galian tsb tidak diselesaikan.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Lantai Trotoar Pecah Assalamualaikum wr. wb sampurasun", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Plat Beton Penutup Saluran Air Ambrol Ijin lapor lubang di jalan dursasana seberang tps pasar pamoyanan. akibat sering dilewati mobil gara2 bak sampahnya agak ditengah jalan dan akibat kena beban backhoe waktu pengangkutan sampah hari sabtu 9/9/2023", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Laporan Kerusakan Jembatan Jalan Terjadi retak jembatan penghubung jalan di jln sukarma, kecamatan bojongloa kaler, kelurahan babakan asih. kode pos 40232. mohon bantuannya.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Lubang Di Jl. Suniaraja, Belokan Sebelum Masuk Jl. Pasar Barat Kami ingin melaporkan adanya lubang besar di jl. suniaraja, tepatnya pada belokan sebelum masuk jl. pasar barat. lubang ini merupakan potensi bahaya bagi pengguna jalan dan kendaraan yang melintas.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Kerusakan Jalan Ada jalan amblas, berlubang cukup besar di jl. lengkong besar no.42 bandung", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Pengaspalan Ulang Flyover Pelangi Mohon untuk dilakukan pengaspalan ulang pada flyover pelangi antapani, bandung dikarenakan aspal flyover tersebut tidak rata dan membuat pengendara motor kesulitan untuk bermanuver dengan stabil, terutama dari arah jl. jakarta menuju jl. trs. jakarta di sisi paling kiri. terima kasih.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Saluran Air Tidak Kunjung Diselesaikan Lokasi: jalan terusan pesantren, rt04 rw11, sukamiskin, arcamanik, kota bandung kronologi: pengerjaan saluran air dengan menggali parit dan membongkar akses masuk ke rumah warga dilakukan kira2 pada pertengahan juli 2023, hingga kini galian tsb tidak diselesaikan. warga kesulitan keluar masuk rumah terlebih ada lansia yang jika ada keadaan darurat akan sulit untuk keluar rumah. update 23 sep: dari informasi pak rw kami pada 22 sep, pekerjaan tidak dapat dilanjutkan pada tanggal 23 sep karena pergantian kepada pemborong awal bernama soni. pemborong bernama soni ini yang menyebabkan pekerjaan terkatung-katung selama 2 bulan. pekerjaan sempat dilakukan oleh pemborong lain, namun kenapa harus kembali kepada pemborong lama yang tidak jelas pekerjaannya. mohon perhatiannya, kami sangat terganggu dengan situasi ini. kami sudah cukup bersabar dengan situasi ini, maka sekali lagi kami harap bisa segera diselesaikan.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Gorong-Gorong Rusak Tutup gorong-gorong di jalan gatot subroto rusak membahayakan pejalan kaki. tepatnya di sebrang bengkel iphone gatot subroto bandung", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Tutup Saluran Air Tengah Jalan Rusak, Membahayakan Mohon bantuan perbaikan tutup saluran air di tengah jalan dr. setiabudi arah cihampelas. list besi mencuat, bisa merusak roda atau melukai pengendara khususnya motor. foto maps lokasi dan kerusakan yang dimaksud terlampir. mohon bantuan segera, karena sudah terpantau 2 minggu tidak ada perubahan. terima kasih.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Pelebaran Jalan Dan Jembatan Di Kota Bandung Selamat malam, ini dengan warga bandung, mau menyampaikan mengenai jalan-jalan di kota bandung, terutama di jalan terusan psm, jalan cidurian, jalan kawaluyaan kiaracondong, jalan gatot subroto dari blk bandung sampai jembatan sungai, jalan terusan babakan sari kiaracondong, jalan di samping fly over jalan jakarta - jalan supratman, jalan di samping fly over antapani, dsb. untuk bisa dilakukan pelebaran jalan dan jembatan karena jalan-jalan yang disebutkan tadi sering menimbulkan kemacetan karena penyempitan jalan, terutama di jam-jam sibuk dan kalau ada satu kendaraan yang parkir bisa menimbulkan kemacetan. dimohon untuk segera dilakukan pelebaran jalan dan jembatan karena bisa menimbulkan kemacetan parah. proyek double track/jalur ganda ka kiaracondong-cicalengka aja bisa. masa pelebaran jalan di kawasan bandung timur ngak bisa. supaya bisa dilakukan pelebaran jalan dan jembatan secepatnya. dan juga untuk jalan terusan buah batu, jalan terusan mohammad toha, jalan terusan kopo juga dilebarkan karena sering menimbulkan kemacetan. mohon segera direalisasikan pelebaran jalan supaya mengurai kemacetan yang sudah cukup dan sangat parah. dan juga relokasi bangunan yang terdampak pelebaran jalan juga harus jadi perhatian. supaya tidak ada yang dirugikan. terima kasih.", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},
    {"text": "Drainase Bawah Beton Mampet Dan Keluar Air Kotor Hitam Di Jalan Gelap Nyawang Selokan bawah beton mampet dan keluar air kotor hitam di jalan gelap nyawang depan bmg itb", "category": "Dinas Sumberdaya Air dan Bina Marga Kota Bandung"},

    {"text": "Parkir Mobil Di Atas Jembatan Cikapundung Acara Di Sabuga ItbMohon dishub dapat menertibkan parkir mobil di sepanjang jembatan cikapundung jl. siliwangi, terkait ada acara di sabuga itb. acara pagi ini sabtu 11 november 2023karena selain mengganggu lalin yang lebih bahaya adalah merusak fungsi jembatan yang sudah cukup tua dibangun akan rusak oleh beban parkir mobil yang ada di atasnya.haturnuhun", "category": "Dinas Perhubungan Kota"},
    {"text": "Tombol Pejalan Kaki Tidak BerfungsiAssalamualaikum wr. wbyth. pj. walikota bandungbahwa tombol pejalan kaki tidak berfungsi, mohon untuk diperbaiki agar bisa digunakan kembali.terima kasihwassalamualaikum wr. wb sumber video:https://photos.app.goo.gl/x1tbq6fnwbefpgdba", "category": "Dinas Perhubungan Kota"},
    {"text": "Lampu Tombol Penyebrangan Jalan MatiAssalamualiakum wr. wbyth pj. walkot bandungbahwasanya lampu penyebrangan jalan mati/rusak, mohon untuk memperbaiki lampu tersebut agar bisa digunakan kembaliterima kasihwassalamualaikum wr. wb lokasi : depan masjid raya bandung", "category": "Dinas Perhubungan Kota"},
    {"text": "Lampu Penerangan Jalan Mati Lampu penerangan jalan di jalan gedebage selatan sekitar kantor kecamatan sudah seminggu mati mohon perhatiannya!", "category": "Dinas Perhubungan Kota"},
    {"text": "Persimpangan Melawan Arus Membahayakan Di Cijerah & Jl Jend SudirmanTolong kepada yg berwenang untuk diadakannya kembali (dulu pernah ada) pembatas tengah (yg saya tandai warna hijau pada foto) agar tidak ada pemotor yg mememotong jalur karena sangat membahayakan dan sering ada yg senggolan/kecelakaan, selain itu juga sering menimbukan kemacetan, jangan sampai menunggu ada korban jiwa baru ditindak. mohon tindakannya segera terimakasih.sebagai tambahan kalau bisa dibuat permanen atau bahannya jangan tali pasti akan ada yg gunting.", "category": "Dinas Perhubungan Kota"},
    {"text": "Parkir Di Area Kampus Itb GaneshaSelamat pagi/siang/sore/malam, perkenalkan saya kebetulan seorang mahasiswa yang sedang menempuh pendidikan di kampus itb ganesha yang berasal dari luar bandung. saya izin bertanya mengenai manajemen parkir yang ada di sekitar area kampus itb (terutama jl. skanda dan jl. gelap", "category": "Dinas Perhubungan Kota"},
    {"text": "Lampu Pju Jalan Kecubung Bandung Mati Lampu pju jalan kecubung antara rumah no 12 da 14 mati total , sehingga rumah disekitarnya gelap. mohon bantuannya untuk ditindaklanjuti", "category": "Dinas Perhubungan Kota"},
    {"text": "Informasi Lowongan Magang Selamat sore, izin bertanya apakah dinas perhubungan kota bandung membuka lowongan magang bagi mahasiswa fresh graduated lulusan s1 perencanaan wilayah dan kota?", "category": "Dinas Perhubungan Kota"},
    {"text": "Minim Penerangan Jalan Assalamualaikum, ijinkan saya sebagai warga menyampaikan keprihatinan pada kondisi jalan yang ramai tetapi minim penerangan di jl.bukit jarian kota bandung, jalan tersebut banyak aktivitas mahasiswa dan juga warga serta pengunjung rumah sakit tetapi tidak ada lampu penerangan yang memadai mulai dari pertigaan bukit jarian-ciumbuleuit s/d rumah sakit paru rotinsulu. mohon sekiranya mendapatkan atensi dari dinas terkait agar menambah lampu yang ada. saat ini ada pjl swadaya masyarakat yang menggunakan tenaga surya tetapi tidak efektif, jika sekiranya dapat diganti dengan listrik dan lampu led pju akan lebih baik agar wilayah tersebut terang. hatur nuhun", "category": "Dinas Perhubungan Kota"},
    {"text": "Biaya Parkir Tidak Berdasarkan Aturan Yang Berlaku Parkir di sebrang pasar kiaracondong, dan membawa mobil tipe innova lalu parkir 1 jam, dikenakan biaya 15rb, dan tukang parkir menggunakan kuitansi yang sudah di cap bertuliskan dishub. tolong di tertibkan pungli seperti ini, ditambah sudah merusak citra dishub dengan mencantumkan dishub di cap kuitansinya, saya memiliki bukti berupa foto.", "category": "Dinas Perhubungan Kota"},
    {"text": "Parkir Mobil Di Atas Jembatan Cikapundung Acara Di Sabuga Itb Mohon dishub dapat menertibkan parkir mobil di sepanjang jembatan cikapundung jl. siliwangi, terkait ada acara di sabuga itb. acara pagi ini sabtu 11 november 2023karena selain mengganggu lalin yang lebih bahaya adalah merusak fungsi jembatan yang sudah cukup tua dibangun akan rusak oleh beban", "category": "Dinas Perhubungan Kota"},
    {"text": "Tombol Pejalan Kaki Tidak Berfungsi Assalamualaikum wr. wb yth. pj. walikota bandung Lampu Penerangan Jalan Mati ampu penerangan jalan di jalan gedebage selatan sekitar kantor kecamatan sudah seminggu mati mohon perhatiannya!", "category": "Dinas Perhubungan Kota"},
    {"text": "Persimpangan Melawan Arus Membahayakan Di Cijerah & Jl Jend Sudirman Tolong kepada yg berwenang untuk diadakannya kembali (dulu pernah ada) pembatas tengah (yg saya tandai warna hijau pada foto) agar tidak ada pemotor yg mememotong jalur karena sangat membahayakan dan sering ada yg senggolan/kecelakaan, selain itu juga sering menimbukan kemacetan, jangan sampai menunggu ada korban jiwa baru ditindak. mohon tindakannya segera terimakasih. sebagai tambahan kalau bisa dibuat permanen atau bahannya jangan tali pasti akan ada yg gunting.", "category": "Dinas Perhubungan Kota"},
    {"text": "Parkir Di Area Kampus Itb Ganesha Selamat pagi/siang/sore/malam, perkenalkan saya kebetulan seorang mahasiswa yang sedang menempuh pendidikan di kampus itb ganesha yang berasal dari luar bandung. saya izin bertanya mengenai manajemen parkir yang ada di sekitar area kampus itb (terutama jl. skanda dan jl. gelap nyawang) yang kebetulan saat ini sebagai satu-satunya opsi tempat parkir kendaraan mobil bagi mahasiswa yang tidak kebagian parkir di area itb. apakah di area jl. skanda dan jl. gelap nyawang ini dikelola oleh petugas parkir yang terdaftar resmi dari dishub bandung atau tidak? sebab saya seringkali melihat tukang parkir yang berjaga di sekitar area ini sangat banyak jumlahnya berjejeran walaupun masih di satu area saja dan beberapa dari mereka bahkan tidak menggunakan rompi petugas parkir dishub. belum lagi terkadang mereka mematok parkir yang seenaknya saja bahkan ada aturan yang menurut saya tidak masuk akal dimana kejadian ini dialami oleh teman saya yang membawa kendaraan. kebetulan saat itu saya dan teman saya secara terpaksa harus parkir di area jl. skanda sekitar pukul 14.00 wib untuk ke kampus dan dimintai tarif parkir sebesar rp10.000. setelah itu, kami pulang dari kampus sekitar pukul 5-6 sore dan kebetulan di saat itu juga dimintai uang parkir kembali dengan alasan tukang parkir yang berjaga beda shift. saat itu kami dimintai parkir kembali sebesar rp5.000. jujur saya sangat miris dengan manajemen parkir yang ada di area ini yang saya yakini sebagian besar dikelola oleh ormas/preman yang berkedok menjadi tukang parkir dengan mental miskin hanya meminta-minta di lahan umum. oleh karena itu, saya sangat mohon kepada para bapak/ibu yang memiliki kewenangan di dishub bandung agar lebih memberikan perhatian lebih dan benar-benar bisa mengalokasikan petugas resmi serta menindak tegas para petugas2 yang meresahkan agar pengelolaan parkir di kota bandung ini bisa lebih terkelola dengan baik dengan manajemen yang teratur. saya sebagai mahasiswa yang membawa kendaraan juga setiap hari harus menghadapi kejadian2 seperti ini mengingat itb sendiri kurang memperhatikan demand parkir mobil para mahasiswanya. oleh karena itu, saya sangat mohon atas perhatiannya terkait pengelolaan parkir di sekitar area kampus itb ini. terimakasih.", "category": "Dinas Perhubungan Kota"},
    {"text": "Lampu Pju Jalan Kecubung Bandung Mati Lampu pju jalan kecubung antara rumah no 12 da 14 mati total , sehingga rumah disekitarnya gelap. mohon bantuannya untuk ditindaklanjuti", "category": "Dinas Perhubungan Kota"},
    {"text": "Informasi Lowongan Magang Selamat sore, izin bertanya apakah dinas perhubungan kota bandung membuka lowongan magang bagi mahasiswa fresh graduated lulusan s1 perencanaan wilayah dan kota?", "category": "Dinas Perhubungan Kota"},
    {"text": "Minim Penerangan Jalan Assalamualaikum, ijinkan saya sebagai warga menyampaikan keprihatinan pada kondisi jalan yang ramai tetapi minim penerangan di jl.bukit jarian kota bandung, jalan tersebut banyak aktivitas mahasiswa dan juga warga serta pengunjung rumah sakit tetapi tidak ada lampu penerangan yang memadai mulai dari pertigaan bukit jarian-ciumbuleuit s/d rumah sakit paru rotinsulu. mohon sekiranya mendapatkan atensi dari dinas terkait agar menambah lampu yang ada. saat ini ada pjl swadaya masyarakat yang menggunakan tenaga surya tetapi tidak efektif, jika sekiranya dapat diganti dengan listrik dan lampu led pju akan lebih baik agar wilayah tersebut terang. hatur nuhun", "category": "Dinas Perhubungan Kota"},
    
    {"text": "", "category": "Dinas Perhubungan Kota"},
]

# Convert text to lowercase for each entry in the dataset

def remove_punctuation(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)

def delete_links(input_text):
    pettern = r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))'''
    out_text = re.sub(pettern, ' ', input_text)
    return out_text

def delete_repeated_characters(input_text):
    pattern = r'(.)\1{2,}'
    out_text = re.sub(pattern, r"\1\1", input_text)
    return out_text

def clean_text(input_text):
    replace = r'[/(){}\[\]|@âÂ,;\?\'\"\*…؟–’،!&\+-:؛-]'
    out_text = re.sub(replace, " ", input_text)
    words = nltk.word_tokenize(out_text)
    words = [word for word in words if word.isalpha()]
    out_text = ' '.join(words)
    return out_text
# Remove punctuation for each entry in the dataset
for entry in data:
    entry["text"] = remove_punctuation(entry["text"].lower())
    entry["text"] = delete_links(entry["text"])
    entry["text"] = delete_repeated_characters(entry["text"])
    entry["text"] = clean_text(entry["text"])

# Print the modified dataset
for entry in data:
    print(entry["text"])

# Baca dataset
dataset = pd.DataFrame(data)
dataset.to_csv("dataset_laporan_masyarakat.csv", index=False)

# Bagi dataset menjadi data pelatihan dan data pengujian
X_train, X_test, y_train, y_test = train_test_split(dataset['text'], dataset['category'], random_state=42)

# Buat model dengan pipeline
model = make_pipeline(TfidfVectorizer(stop_words=stopwords.words('indonesian'), tokenizer=PorterStemmer().stem), MultinomialNB())

# Latih model
model.fit(X_train, y_train)

# Prediksi kategori laporan pada data pengujian
predictions = model.predict(X_test)

# Evaluasi kinerja model
accuracy = metrics.accuracy_score(y_test, predictions)
print(f"Akurasi: {accuracy}")

# Gunakan model untuk mengklasifikasikan laporan masyarakat baru
new_report = ["Lampu Pju Jalan Kecubung Bandung Mati Lampu pju jalan kecubung antara rumah no 12 da 14 mati total , sehingga rumah disekitarnya gelap. mohon bantuannya untuk ditindaklanjuti".lower()]
predicted_category = model.predict(new_report)
print(f"Prediksi Kategori: {predicted_category}")

