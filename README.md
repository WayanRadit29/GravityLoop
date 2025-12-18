
# 🌌 Gravity Loop

**Gravity Loop** adalah game 2D berbasis fisika gravitasi yang dikembangkan menggunakan **Python** dan **Pygame**, dengan fokus pada penerapan **Object-Oriented Programming (OOP)**, **state-based game architecture**, dan **desain gameplay berbasis constraint**.

Game ini dikembangkan sebagai **proyek akademik** sekaligus **prototype publik**, sehingga dokumentasi ini menggabungkan sudut pandang teknis, edukatif, dan showcase.

---

## 👥 Tim Pengembang

**Wayan Raditya Putra**

* Arsitektur sistem dan game engine
* Mekanika gravitasi, orbit, dan release
* Desain level dan balancing difficulty
* Sistem obstacle dan hazard

**Belva**

* UI/UX dan visual layout
* Menu, transisi state, dan overlay
* Integrasi aset visual dan polish tampilan

---

## 🧩 Konsep Gameplay

Pada Gravity Loop, pemain **tidak bisa bergerak bebas**:

* tidak bisa berjalan
* tidak bisa berhenti
* tidak bisa mengarahkan arah gerak secara langsung

Satu-satunya cara berpindah adalah:

1. Tertarik gravitasi planet terdekat
2. Masuk ke orbit
3. Melepaskan diri (**release**) pada waktu yang tepat

Kesalahan timing akan menyebabkan pemain:

* meleset ke luar layar
* bertabrakan dengan meteor
* tersedot black hole
* gagal mencapai roket penyelamat

Kontrol game dirancang **sengaja minimal** (satu input utama) agar fokus sepenuhnya pada **timing, pemahaman fisika, dan spatial awareness**.

---

## 🎮 Mekanika Inti

* Planet dengan gaya gravitasi yang menangkap player ke orbit
* Orbit bersifat otomatis dan terus berjalan tanpa input
* Release dari orbit menentukan lintasan selanjutnya
* Level bersifat **deterministik** (tanpa RNG gameplay kritikal)
* Tidak ada fase “melayang kosong” tanpa pegangan planet

---

## 🧠 Filosofi Desain

Gravity Loop menerapkan **constraint-based design**:

* pemain selalu berada dalam batasan fisika
* keputusan kecil berdampak besar
* kesalahan bukan karena kontrol, tapi karena timing dan perencanaan

Setiap level dirancang sebagai **puzzle fisika**, bukan sekadar rintangan reaktif.

---

## 🧱 Arsitektur Sistem (OOP)

Struktur game dibangun secara modular:

* `GameEngine`
  Mengelola game loop, state, dan integrasi seluruh sistem

* `LevelManager`
  Mendefinisikan isi level (planet, meteor, black hole, spawn)

* `Player`
  Mengelola orbit, release, status hidup, dan collision

* `Planet`
  Menyediakan gaya gravitasi dan mekanisme orbit

* `Meteor`
  Obstacle statis dan dinamis

* `MeteorSpawner`
  Spawner terarah (non-random) berbasis emitter

* `BlackHole`
  Hazard gravitasi fatal sebagai choke point

* UI States:

  * Lobby
  * Level Select
  * Playing
  * Game Over

Pendekatan ini memisahkan dengan jelas:

* logika gameplay
* desain level
* UI dan visual
* state management

---

## 🧪 Desain Level

### Level 1 – EASY

Fokus: pengenalan mekanik

* Planet sedikit dan berdekatan
* Orbit stabil dan lambat
* Tidak ada obstacle
* Player otomatis masuk orbit awal tanpa input

### Level 2 – PYRHA (MEDIUM)

Fokus: timing dan pressure

* Jarak planet lebih jauh
* Orbit lebih cepat
* Meteor statis sebagai zona bahaya
* Meteor spawner terarah dari posisi tertentu
* Memaksa pemain mengatur release dengan presisi

### Level 3 – HARD

Fokus: penguasaan total

* 5 planet dengan jarak jauh
* Orbit cepat dan tidak forgiving
* 1 black hole besar sebagai choke point
* Kombinasi meteor statis dan spawner
* Tidak ada shortcut langsung ke roket
* Menuntut perencanaan lintasan secara penuh

---

## 🎯 Tujuan Pembelajaran (Akademik)

Melalui proyek ini, pengembang mempraktikkan:

* Prinsip OOP:

  * Encapsulation
  * Inheritance
  * Polymorphism
* State-based game architecture
* Simulasi fisika sederhana (gravitasi & orbit)
* Desain level deterministik berbasis parameter
* Kolaborasi tim menggunakan Git & GitHub

---

## 🛠️ Teknologi

* **Bahasa:** Python 3
* **Library:** Pygame
* **Paradigma:** Object-Oriented Programming
* **Tools:** Git, GitHub, VS Code

---

## ▶️ Cara Menjalankan

```bash
git clone https://github.com/<username>/GravityLoop.git
cd GravityLoop
pip install pygame
python main.py
```

---


## 📜 Lisensi

MIT License © 2025

---
