## Sovelluksen asennusohjeet omalle koneelle

Sovellus on websovellus, jonka toimintaympäristö on selain. Tästä syystä ohjelmalle ei ole varsinaisia asennusohjeita, vaan ohjeet kirjataan sovelluksen lokaalin käyttöympäristön luomista varten. Sovelluksen suunniteltu toimintaympäristö on kuitenkin erillinen verkkopalvelin tai Herokua vastaava alusta.

*Asennusohjeissa oletetaan, että käyttäjälle on tuttua komentorivin käyttö. Ohjeet on kirjoitettu Linux tai MacOS käyttäjille - Windows tuki on rajoitettua*

### Ennen sovelluksen lataamista
0. Varmista, että koneellesi on asennettu Python ja sqlite3. Nämä ovat sovelluksen lokaalin version kannalta pakollisia. Voit käyttää esimerkiksi alla olevia komentoja. Mikäli käytät Linuxia on koneellasi hyvin todennäköisesti Python valmiiksi asennettuna.
```
$ sudo apt-get update
$ sudo apt-get install python3
$ sudo apt-get install sqlite3
```
+ Mikäli käytät MacOS -laitetta, suosittelen käyttämään Homebrew nimistä paketinhallintaohjelmistoa, joka toimii Linuxin apt-get:in tapaan. Asenna Homebrew ja suorita seuraavat komennot
```
$ brew install python3
$ brew install sqlite3
```
1. Mikäli lataat sovelluksen ZIP pakkauksena, on sinulla oltava pakkausten purkamiseen soveltuva ohjelma, esimerkiksi 7zip.

2. Koneellasi on oltava jokin verkkoselain, jotta voit katsella projektin luomia sivunäkymiä.

3. Projekti on jaoteltu useisiin kansioihin ja tiedostoihin, joiden selaaminen kansiosta tai komentoriviltä voi olla hankalaa. Suosittelen käyttämään jonkinlaista IDE ohjelmistoa, esimerkiksi ilmaista Visual Studio Codea, jossa on hyvä Python tuki ja mukiinmenevä integroitu git käyttöliittymä.

4. (Mikäli haluat kloonata projektin, on koneellasi oltava asennettuna myös Git)


### Asennus step-by-step pakatun tiedoston kautta

1. **Lataa sovellus pakattuna ZIP-tiedostona sovelluksen [Github](https://github.com/Dforssi/dyykkimestarit) -sivulta Clone or download painikkeen kautta**

2. **Pura tiedosto haluamaasi kansioon koneellasi**

3. **Navigoi komentorivin kautta kansioon, johon purit projektin pakkauksen**

4. **Luo Pythonin virtuaaliympäristö ja ota se käyttöön seuraavilla komennoilla**
```
$ python3 -m venv venv
$ source venv/bin/activate
```

5. **Python3:ssa on laajennusten asentamiseen käyttettävä Pip valmiiksi asennettuna, asennetaan sovelluksen käyttämä Flask -kirjasto**
```
$ pip install Flask
```
+ Voit myös tässä vaiheessa päivittää pip:in uudempaan versioon
```
$ pip install --upgrade pip 
```

6. **Asenna sovelluksen requirements.txt määrittelemät riippuvuudet, jotta sovellus toimii oikein**
```
$ pip install -r requirements.txt
```
+ Pip osaa etsiä omatoimisesti tiedostoon määritellyt riippuvuudet ja asentaa ne.

7. **Voit nyt käyttää sovellusta käynnistämällä sen seuraavalla komennolla**
```
$ python3 run.py
```

8. **Navigoi osoitteeseen http://127.0.0.1:5000**

9. **Voit nyt käyttää sovellusta lokaalissa verkkoympäristössä**

### Git kloonaus

1. **Kopioi [Github](https://github.com/Dforssi/dyykkimestarit) -sivulta Clone or download painikkeen takaa löytyvä linkki**

2. **Navigoi komentorivillä haluamaasi kansioon, johon projektin kloonikansio tulee**

3. **Kloonaa kansio**
```
$ git clone <github sivulta löytämäsi linkki> <nimi kansiolle>
```
+ Tämä operaatio kopioi projektin githubista määrittelemääsi kansioon

4. **Referoi ZIP -tiedoston asennusohjeita kohdasta 3. eteenpäin**