## Suunnitellut toiminnallisuudet

Tämän otsikon alle on kirjattu kurssin alkaessa sovellukselle suunniteltuja toimintoja siinä muodossa kuin ne silloin olivat.

>## Kuvaus
>Valitsin aiheekseni hieman muokatun version aiheaihioissa olleesta projektin työaikaseurannasta. Toteutan kuvitteellisen sukelluskeskuksen työaikaseurannan, jossa työtä voidaan kirjata sekä seurata työlajeittain. Tällaisia työlajeja ovat esimerkiksi kurssien ohjaamiset, asiakkaiden sukellusretkien toteutus, varustehuolto ja toimistotyöt. Projekteja korvaamaan käytetään kursseja ja retkiä. Nämä tapahtumat saattavat osallistujamäärästä tai haastavuudesta johtuen vaatia enemmän osallistujia tai matkustamista, jolloin työaikaseurantaan tulee myös työvuorosuunnittelullinen elementti, joskin projektin tarkoituksena ei ole tehdä työvuorolistoja lääkärikeskus -aiheen mukaisesti.

>#### Perustoimintoja
>* Kirjautuminen sivustolle
>* Työaikakirjauksen teko (Lisää uusi tietokantaan, lue kirjaus tietokannasta, muokkaa kirjausta, poista kirjaus)
>* Kurssin, retken tai muun tapahtuman perustaminen (Lisää uusi tietokantaan, lue kirjaus tietokannasta, muokkaa kirjausta, poista kirjaus)
>* Työntekijän liittäminen tapahtumaan
>* Työntekijän poistaminen tapahtumasta
>* Keskuksen johtajan raportit
>* Työntekijän henkilökohtainen raportti
>
>#### Suunniteltuja lisätoimintoja
>* Työvuorosuunnittelullinen käyttöliittymä johtajan näkymään 
>* Uusien kurssien ja tapahtumien luonti tulevaisuuteen (näkyminen työntekijöiden näkymässä) (CRUD -operaatiot, tietokantataulu)
>* Varoitukset, mikäli kursseille ja tapahtumiin suunnitelluilla kouluttajilla ei ole tarvittavia valmiuksia kyseiseen tapahtumaan

## Toteutuneet toiminnallisuudet ja puutteet, 25.6.2018

Alustava kuvaukseni oli kunnianhimoinen, ja projektin edetessä huomasinkin, että kaikkien ominaisuuksien toteuttaminen on mahdotonta omien aikarajoitteideni puitteissa. Pyrinkin keskittymään perusominaisuuksien hiomiseen ja helpon käyttöliittymän tekemiseen, jotta projektin perustoiminnallisuus olisi erinomaisella tasolla. Tavoitteenani oli pitää projekti jatkuvasti toimivassa tilassa, jossa onnistuinkin kohtalaisen hyvin. Alkuperäisistä toiminnoista toteutuivat kirjautuminen, työaikakirjauksen teko CRUD nelikkoineen, tapahtuman teko CRUD nelikkoineen, työntekijän liittäminen edellä mainittuun tapahtumaan ja raportit etusivun muodossa, joka näyttää henkilökohtaiset sekä kokonaislaskelmat kirjauksista. Työvuorosuunnittelullinen käyttöliittymä, eli tapahtumien luonti, toteutui myös ADMIN roolituksen taakse. Tapahtumien luonnista tuli yksittäinen ominaisuus aluksi jostain syystä eroteltujen "uusi tapahtuma" ja "kurssi, retki tai muu" ominaisuuksien sijasta, joka olikin loogisempi ratkaisu. Työntekijän poistaminen tapahtumasta toteutui muokkauksen kautta, jolloin työntekijän tilalle voidaan vaihtaa toinen työntekijä.

Puutteita jäi erityisesti työtehtävien tyypityksen toteuttamisessa. Tällä hetkellä järjestelmässä olevalla tehtävän tunnistenumerolla ei ole funktiota, ajatuksena oli luoda sen taakse erilaisia tehtäväkuvauksia. Raportit jäivät myös torsoksi, laskenta rajoittuu tehtävien määrään ja työtunteihin. Työtehtävän tunnisteen lisäksi myös työntekijän sertifikaattien hyödyntäminen tapahtumien suunnitelussa sekä niiden validoinnisssa jäi tekemättä kokonaan. Työvuorosuunnittelullista näkymää tuli vain tapahtumien listauksen ja luomisen verran, tämäkin jäi hieman torsoksi.

Muutamia erittäin haastavia korjauksia, kuten autorisointi joka oli toista viikkoa kesken erinäisten virhetilanteiden vuoksi, lukuunottamatta onnistuin mielestäni hyvin ja olen tyytyväinen lopputulokseen, vaikka parannettavaakin jäi vielä.