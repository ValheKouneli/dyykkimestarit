# Tietokantasovellus - Sukelluskeskus Dyykkimestarit työaikaseuranta
Tietokantasovellus, kesä 2018

[Heroku](https://dyykkitsoha.herokuapp.com/)

[Asennusohjeet](https://github.com/Dforssi/dyykkimestarit/blob/master/documentation/asennusohje.md)

[Käyttöohjeet](https://github.com/Dforssi/dyykkimestarit/blob/master/documentation/kaytto_ohje.md)

##### Käyttäjätunnukset:

| Käyttäjätunnus   | Salasana   |
| ---------------- | ---------- |
| admin            | admin123   |
| tester           | tester123  |

Järjestemään voi myös luoda omia käyttäjätunnuksia tällä hetkellä.

Viikoittaiset etapit on tallennettu releaseina. Uusin koodi pyörii masterissa, mutta releaseista voi tarkastaa mitä milläkin viikolla on ollut valmiina.

[User Storyt ja SQL lauseet](https://github.com/Dforssi/dyykkimestarit/blob/master/documentation/user_stories.md)

[Skeema / Tietokantakaavio](https://github.com/Dforssi/dyykkimestarit/blob/master/documentation/tietokantakaavio.md)

## Kuvaus
Valitsin aiheekseni hieman muokatun version aiheaihioissa olleesta projektin työaikaseurannasta. Toteutan kuvitteellisen sukelluskeskuksen työaikaseurannan, jossa työtä voidaan kirjata sekä seurata työlajeittain. Tällaisia työlajeja ovat esimerkiksi kurssien ohjaamiset, asiakkaiden sukellusretkien toteutus, varustehuolto ja toimistotyöt. Projekteja korvaamaan käytetään kursseja ja retkiä. Nämä tapahtumat saattavat osallistujamäärästä tai haastavuudesta johtuen vaatia enemmän osallistujia tai matkustamista, jolloin työaikaseurantaan tulee myös työvuorosuunnittelullinen elementti, joskin projektin tarkoituksena ei ole tehdä työvuorolistoja lääkärikeskus -aiheen mukaisesti.

### Perustoimintoja
* Kirjautuminen sivustolle
* Työaikakirjauksen teko (Lisää uusi tietokantaan, lue kirjaus tietokannasta, muokkaa kirjausta, poista kirjaus)
* Kurssin, retken tai muun tapahtuman perustaminen (Lisää uusi tietokantaan, lue kirjaus tietokannasta, muokkaa kirjausta, poista kirjaus)
* Työntekijän liittäminen tapahtumaan
* Työntekijän poistaminen tapahtumasta
* Keskuksen johtajan raportit
* Työntekijän henkilökohtainen raportti

### Suunniteltuja lisätoimintoja
* Työvuorosuunnittelullinen käyttöliittymä johtajan näkymään 
* Uusien kurssien ja tapahtumien luonti tulevaisuuteen (näkyminen työntekijöiden näkymässä) (CRUD -operaatiot, tietokantataulu)
* Varoitukset, mikäli kursseille ja tapahtumiin suunnitelluilla kouluttajilla ei ole tarvittavia valmiuksia kyseiseen tapahtumaan
