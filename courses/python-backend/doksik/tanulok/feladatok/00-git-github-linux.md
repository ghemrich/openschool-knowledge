# Kiegészítő gyakorlatok – 0. hét: Git, GitHub, parancssor

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 0.1 – Fájl jogosultságok ⭐
Hozz létre 3 fájlt a terminálban. Használd a `chmod` parancsot: az első legyen csak olvasható, a második írható-olvasható, a harmadik végrehajtható is. Listázd ki `ls -la`-val, és másold a kimenetet egy `jogosultsagok.txt` fájlba.

### 0.2 – Pipe-ok és szűrés ⭐
Készíts egy `szavak.txt` fájlt legalább 20 szóval. Használd a terminálban:
- `cat szavak.txt | sort` → ábécé sorrend
- `cat szavak.txt | wc -l` → sorok száma
- `cat szavak.txt | grep "a"` → csak az 'a'-t tartalmazó sorok

Írd a parancsokat és kimenetüket egy `pipe_pelda.txt` fájlba.

### 0.3 – Git stash ⭐⭐
Módosíts egy fájlt commitolás nélkül. Használd a `git stash` parancsot a változtatások félretételéhez. Csinálj egy másik commitot, majd hozd vissza a stash-t (`git stash pop`). Dokumentáld a lépéseket.

### 0.4 – Git revert ⭐⭐
Készíts 3 commitot. Az utolsó commitot vondd vissza `git revert HEAD`-del (ne használj `reset`-et!). Nézd meg a `git log`-ot – mi a különbség a `revert` és a `reset` között? Írd le 2-3 mondatban egy `revert_vs_reset.txt` fájlba.

### 0.5 – SSH kulcs ⭐⭐⭐
Generálj SSH kulcsot (`ssh-keygen`). Add hozzá a GitHub fiókedhoz. Klónozz le egy repót SSH-val (`git clone git@github.com:...`). Dokumentáld a lépéseket egy `ssh_setup.md` fájlba.
