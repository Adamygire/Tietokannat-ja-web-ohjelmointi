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

### Roolit
- Vieras: henkilö, jolla ei ole käyttäjätunnusta järjestelmässä.
- Käyttäjä: henkilö, joka voi kirjautua järjestelmässä.
- Admin: henkilö, jolla on kaikki oikeudet järjestelmässä.
- Opettaja: henkilö, joka hallinnoi kursseja ja tehtäviä.
- Opiskelija: henkilö, joka voi liittyä kursille ja tehdä kursin tehtävät.

## User story

### Vierailijan toiminnot:
- [ ] Voi vierailla sivustolla.
- [ ] Voi rekisteröityä osoitteessa /signup.

### Käyttäjän toiminnot:
- [ ] Käyttäjä voi tehdä kaiken sen mitä vierailija voi tehdä.
- [ ] Käyttäjä voi kirjautua sisään osoitteessa /signin.
- [ ] Käyttäjä voi kirjautua ulos osoitteessa /signout.


### Opettajan toiminnot:
- [ ] Opettajan voi tehdä kaiken sen mitä vierailija sekä järjestelmään kirjautunut käyttäjä voi tehdä.
- [ ] Opettaja pystyy luomaan uuden kurssin, muuttamaan olemassa olevaa kurssia ja poistamaan kurssin.
- [ ] Opettaja pystyy lisäämään kurssille tekstimateriaalia ja tehtäviä.
- [ ] Opettaja pystyy näkemään kurssistaan tilaston, keitä opiskelijoita on kurssilla ja mitkä kurssin tehtävät kukin on ratkonut.


### Opiskelija toiminnot:
- [ ] Opiskelija voi tehdä kaiken sen mitä vierailija sekä järjestelmään kirjautunut käyttäjä voi tehdä.
- [ ] Opiskelija näkee listan kursseista ja voi liittyä kurssille.
- [ ] Opiskelija voi lukea kurssin tekstimateriaalia sekä ratkoa kurssin tehtäviä.
- [ ] Opiskelija pystyy näkemään tilaston, mitkä kurssin tehtävät hän on ratkonut.


### Järjestelmänvalvojan toiminnot:
- [ ] Järjestelmänvalvoja voi tehdä kaiken sen mitä vierailija sekä järjestelmään kirjautunut käyttäjä voi tehdä.
- [ ] Järjestelmänvalvoja voi hallinnoida kursseja, tehtävia, sekä tunnuksia.
