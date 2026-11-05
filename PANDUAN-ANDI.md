# Panduan P06 untuk Andi — Portal PMB ke Vercel

Identitas proyek: **Andi Syafira — NIM 24024600037**. Folder siap pakai: `D:\project\cloudcomputing\P06\pmb-portal-24024600037`.

## 1. Unggah ke GitHub akun `firakampus256-bot`

Buka https://github.com/new lalu isi:

- Repository name: `pmb-portal-24024600037`
- Visibility: **Public**
- Jangan centang README, .gitignore, atau license.

Klik **Create repository**. Di halaman repositori kosong, klik **uploading an existing file**, lalu seret berkas berikut dari folder proyek:

- `app.py`
- `requirements.txt`
- `.python-version`
- `vercel.json`
- `test_app.py`
- `README.md`
- folder `templates` (berisi `index.html`)
- folder `api` (berisi `index.py`) — folder wajib dibuat dengan cara menyeret foldernya langsung

Jangan unggah `.venv`, `__pycache__`, atau berkas lokal lain. Tulis commit message `Tugas P06 Flask Cloud Computing`, lalu **Commit changes**.

## 2. Deploy di Vercel

1. Buka https://vercel.com/signup, pilih **Continue with GitHub**, izinkan akses. Kalau sudah punya akun Vercel, lewati langkah ini.
2. Klik **Add New** → **Project** → **Import Git Repository** → pilih `pmb-portal-24024600037`.
3. Framework Project terdeteksi **Flask**. Biarkan Build Command dan Output Directory apa adanya.
4. Buka **Environment Variables**, tambahkan:
   - `APP_VERSION` = `v1`
   - `PMB_GELOMBANG` = `Gelombang 1`
5. Klik **Deploy** dan tunggu sampai selesai.

## 3. Kirim bukti

Link berbentuk `https://pmb-portal-24024600037.vercel.app`. Buka link itu, lalu periksa:

- Halaman menampilkan **Flask App with CI/CD Test, NIM: 24024600037** dan nama **Andi Syafira**.
- Menu **Health Check** menampilkan `{"status":"ok"}`.
- Menu **API Info** menampilkan JSON dengan `"nim": "24024600037"`.

Kumpulkan link production tersebut ke dosen.
