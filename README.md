# Opetussovellus
### Tietokannat-ja-web-ohjelmointi

## Kuvaus
Sovelluksen avulla voidaan järjestää verkkokursseja, joissa on tekstimateriaalia ja automaattisesti tarkastettavia tehtäviä. Jokainen käyttäjä on opettaja tai opiskelija.

### Sovelluksen ominaisuuksia:
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Opiskelija näkee listan kursseista ja voi liittyä kurssille.
- Opiskelija voi lukea kurssin tekstimateriaalia sekä ratkoa kurssin tehtäviä.
- Opiskelija pystyy näkemään tilaston, mitkä kurssin tehtävät hän on ratkonut.
- Opettaja pystyy luomaan uuden kurssin, muuttamaan olemassa olevaa kurssia ja poistamaan kurssin.
- Opettaja pystyy lisäämään kurssille tekstimateriaalia ja tehtäviä. Tehtävä voi olla ainakin monivalinta tai tekstikenttä, johon tulee kirjoittaa oikea vastaus.
- Opettaja pystyy näkemään kurssistaan tilaston, keitä opiskelijoita on kurssilla ja mitkä kurssin tehtävät kukin on ratkonut.

### Käyttö ohjeet
1. Klonaa repo:
```
git clone https://github.com/Adamygire/educational-app.git
```
2. Siirry repoon:
```
cd educational-app
```
3. Luo virtuaali environmentin:
```
python -m venv venv
source venv/bin/activate
```
4. Asenna riippuvuudet:
```
pip install -r requirements.txt
```
5. Suorita ohjelmistoa:
```
flask run
```

### Roolit
- Vieras: henkilö, jolla ei ole käyttäjätunnusta järjestelmässä.
- Käyttäjä: henkilö, joka voi kirjautua järjestelmässä.
- Admin: henkilö, jolla on kaikki oikeudet järjestelmässä.
- Opettaja: henkilö, joka hallinnoi kursseja ja tehtäviä.
- Opiskelija: henkilö, joka voi liittyä kursille ja tehdä kursin tehtävät.

## User story

### Vierailijan toiminnot:
- [x] Voi vierailla sivustolla.
- [x] Voi rekisteröityä osoitteessa /signup.

### Käyttäjän toiminnot:
- [x] Käyttäjä voi tehdä kaiken sen mitä vierailija voi tehdä.
- [x] Käyttäjä voi kirjautua sisään osoitteessa /signin.
- [x] Käyttäjä voi kirjautua ulos osoitteessa /signout.


### Opettajan toiminnot:
- [x] Opettajan voi tehdä kaiken sen mitä vierailija sekä järjestelmään kirjautunut käyttäjä voi tehdä.
- [x] Opettaja pystyy luomaan uuden kurssin, muuttamaan olemassa olevaa kurssia ja poistamaan kurssin.
- [x] Opettaja pystyy lisäämään kurssille tekstimateriaalia ja tehtäviä.
- [x] Opettaja pystyy näkemään kurssistaan tilaston, keitä opiskelijoita on kurssilla ja mitkä kurssin tehtävät kukin on ratkonut.


### Opiskelija toiminnot:
- [x] Opiskelija voi tehdä kaiken sen mitä vierailija sekä järjestelmään kirjautunut käyttäjä voi tehdä.
- [x] Opiskelija näkee listan kursseista ja voi liittyä kurssille.
- [x] Opiskelija voi lukea kurssin tekstimateriaalia.
- [x] Opiskelija voi ratkoa kurssin tehtäviä.
- [x] Opiskelija pystyy näkemään tilaston, mitkä kurssin tehtävät hän on ratkonut.

