# Környezet beállítás

Ez a dokumentum leírja, milyen szoftvereket kell telepítened a Projekt Labor kurzushoz, és hogyan állítsd be a fejlesztői környezetet.

---

## 1. Git és GitHub

### 1.1 Git telepítése

**Windows:**
```bash
# Töltsd le és telepítsd: https://git-scm.com/download/win
# Telepítés közben: "Use Git from the Windows Command Prompt" opciót válaszd
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update && sudo apt install git
```

**macOS:**
```bash
xcode-select --install
```

### 1.2 Git konfiguráció

```bash
git config --global user.name "Vezetéknév Keresztnév"
git config --global user.email "email@example.com"
```

### 1.3 GitHub fiók

1. Regisztrálj: [github.com](https://github.com)
2. Állíts be SSH kulcsot a push/pull-hoz:
   ```bash
   ssh-keygen -t ed25519 -C "email@example.com"
   cat ~/.ssh/id_ed25519.pub
   ```
3. Másold be a publikus kulcsot: GitHub → Settings → SSH and GPG keys → New SSH key

---

## 2. Docker és Docker Compose

A Projekt Labor Docker Compose-t használ a fejlesztői és éles környezethez is. Ez a legfontosabb szoftver — nélküle nem tudsz dolgozni.

### 2.1 Telepítés

**Windows:**
1. Töltsd le: [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Telepítés után: engedélyezd a WSL 2 backend-et (a telepítő felajánlja)
3. Ellenőrizd:
   ```bash
   docker --version
   docker compose version
   ```

**Linux (Ubuntu/Debian):**
```bash
# A hivatalos Docker repó használata ajánlott (nem az apt-os docker.io)
# https://docs.docker.com/engine/install/ubuntu/
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Hogy ne kelljen sudo a docker parancsokhoz:
sudo usermod -aG docker $USER
# Jelentkezz ki és vissza, hogy érvényesüljön
```

**macOS:**
1. Töltsd le: [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Ellenőrizd:
   ```bash
   docker --version
   docker compose version
   ```

### 2.2 Ellenőrzés

```bash
docker run hello-world
```

Ha a `Hello from Docker!` üzenetet láttad, minden rendben.

---

## 3. Python 3.12+

A backend Python 3.12-t használ.

**Windows:**
1. Töltsd le: [python.org](https://www.python.org/downloads/)
2. Telepítésnél: **pipeld be az "Add Python to PATH"** opciót!
3. Ellenőrizd:
   ```bash
   python --version
   ```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update && sudo apt install python3.12 python3.12-venv python3-pip
```

**macOS:**
```bash
brew install python@3.12
```

> **Megjegyzés:** A fejlesztés közben a Docker containerben fut a Python, de lokálisan is kell a tesztek futtatásához és az Alembic migrációkhoz.

---

## 4. Node.js 20+

Az Astro frontend (Modul 5) Node.js-t igényel.

**Minden platform (ajánlott: nvm):**
```bash
# nvm telepítése (Node Version Manager)
# https://github.com/nvm-sh/nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash

# Terminál újraindítása után:
nvm install 20
nvm use 20
node --version
npm --version
```

**Windows (alternatíva):**
1. Töltsd le: [nodejs.org](https://nodejs.org/) (LTS verzió)
2. Telepítés → ellenőrzés:
   ```bash
   node --version
   npm --version
   ```

> **Megjegyzés:** Az első 4 modulhoz nem kell Node.js — elég a Modul 5 előtt telepítened.

---

## 5. VS Code

### 5.1 Telepítés

Töltsd le: [code.visualstudio.com](https://code.visualstudio.com/)

### 5.2 Ajánlott kiegészítők

| Kiegészítő | Mire kell |
|------------|-----------|
| Python (ms-python.python) | Python nyelvi támogatás, debugging |
| Pylance (ms-python.vscode-pylance) | Intelligens kódkiegészítés |
| Docker (ms-azuretools.vscode-docker) | Docker fájlok kezelése |
| GitLens (eamodio.gitlens) | Git történet, blame, diff |
| Ruff (charliermarsh.ruff) | Python linter és formatter |
| Astro (astro-build.astro-vscode) | Astro fájlok támogatása (Modul 5-től) |

**Telepítés parancssorból:**
```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-azuretools.vscode-docker
code --install-extension eamodio.gitlens
code --install-extension charliermarsh.ruff
code --install-extension astro-build.astro-vscode
```

---

## 6. PostgreSQL kliens (opcionális)

A PostgreSQL Docker containerben fut, de hasznos, ha lokálisan is tudsz csatlakozni az adatbázishoz:

**pgAdmin (grafikus):**
- Töltsd le: [pgadmin.org](https://www.pgadmin.org/download/)

**psql (parancssori):**
```bash
# Ubuntu/Debian
sudo apt install postgresql-client

# macOS
brew install libpq && brew link --force libpq

# Windows: a PostgreSQL telepítővel jön
```

**Csatlakozás a fejlesztői adatbázishoz:**
```bash
psql -h localhost -U openschool -d openschool
# Jelszó: a .env fájlban megadott DB_PASSWORD
```

---

## 7. Ellenőrzőlista

Minden szoftver telepítve és működik:

- [ ] `git --version` → 2.x+
- [ ] `docker --version` → 24.x+
- [ ] `docker compose version` → 2.x+
- [ ] `docker run hello-world` → sikeres
- [ ] `python3 --version` → 3.12+
- [ ] `node --version` → 20+ (Modul 5 előtt elég)
- [ ] VS Code telepítve, kiegészítők beállítva
- [ ] GitHub fiók + SSH kulcs beállítva
