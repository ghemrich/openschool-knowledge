# 1. hét – Bevezetés és alapok

> **Dokumentáció:** [W3Schools – Python bevezető](https://www.w3schools.com/python/python_intro.asp) | [Változók](https://www.w3schools.com/python/python_variables.asp) | [Adattípusok](https://www.w3schools.com/python/python_datatypes.asp)

## 1. óra: A Python világa

### Mi a programozás?
A programozás azt jelenti, hogy utasításokat írunk a számítógépnek, amelyeket sorban végrehajt.

### Első program

```python
# Ez egy megjegyzés – a Python nem futtatja
print("Hello, világ!")
print("Üdv a Python világában!")
```

### A `print()` függvény
Szöveg kiírására szolgál. A szöveget idézőjelek közé tesszük.

```python
print("Ez egy szöveg")
print('Ez is szöveg')
print("Eredmény:", 2 + 3)
```

---

## 2. óra: Változók és típusok

### Változók
A változó egy „doboz", amiben adatot tárolunk.

```python
nev = "Anna"
kor = 16
atlag = 4.5
diak = True
```

### Alaptípusok

| Típus | Leírás | Példa |
|-------|--------|-------|
| `int` | Egész szám | `42` |
| `float` | Tizedes tört | `3.14` |
| `str` | Szöveg | `"alma"` |
| `bool` | Logikai érték | `True`, `False` |

### A `type()` függvény

```python
x = 42
print(type(x))  # <class 'int'>

y = "hello"
print(type(y))  # <class 'str'>
```

### Gyakorlat
Készíts programot, amely kiírja a neved, a korod és a kedvenc tantárgyadat!

```python
nev = "Kiss Anna"
kor = 16
tantargy = "informatika"

print("Név:", nev)
print("Kor:", kor)
print("Kedvenc tantárgy:", tantargy)
```
