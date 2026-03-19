# 11. hét – Haladó CSS és projekt

> **Dokumentáció:** [W3Schools – CSS animációk](https://www.w3schools.com/css/css3_animations.asp) | [CSS átmenetek](https://www.w3schools.com/css/css3_transitions.asp) | [CSS változók](https://www.w3schools.com/css/css3_variables.asp)

## CSS változók (Custom Properties)

A CSS változók segítségével értékeket definiálhatsz egyszer és használhatod többször:

```css
:root {
    --fo-szin: #2c3e50;
    --akcent-szin: #3498db;
    --hatter-szin: #ecf0f1;
    --kerekites: 8px;
}

h1 { color: var(--fo-szin); }
a { color: var(--akcent-szin); }
body { background-color: var(--hatter-szin); }
.kartya { border-radius: var(--kerekites); }
```

> **Előny:** Ha változtatni kell egy színt, elég egy helyen módosítani.

---

## Átmenetek (transitions)

Sima animáció CSS tulajdonság változásakor:

```css
.gomb {
    background-color: #3498db;
    transition: background-color 0.3s ease;
}

.gomb:hover {
    background-color: #2980b9;
}
```

```css
transition: <tulajdonság> <időtartam> <görbe>;
```

| Görbe | Hatás |
|-------|-------|
| `ease` | Lassan kezd, gyorsít, lassan fejez be |
| `linear` | Egyenletes |
| `ease-in` | Lassan indul |
| `ease-out` | Lassan áll meg |

---

## Árnyékok

### Box shadow

```css
.kartya {
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.kartya:hover {
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}
```

### Text shadow

```css
h1 {
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}
```

---

## Transform

```css
.elem:hover {
    transform: scale(1.05);     /* Nagyítás */
    transform: rotate(5deg);    /* Forgatás */
    transform: translateY(-5px); /* Felfelé mozgatás */
}
```

---

## Projekt tippek

Egy komplett weboldal készítésekor:
1. Tervezd meg a szerkezetet szemantikus HTML-lel
2. Definiáld a színeket és értékeket CSS változókba
3. Használj Flexbox-ot az elrendezéshez
4. Tedd reszponzívvá media query-kkel
5. Adj hozzá átmeneteket és árnyékokat a végén
