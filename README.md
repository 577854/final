<h1>Innlevering 2 for maskinlæring i faget DAT156</h1>
<h2>Gruppemedlemmer: Gudsteinn Arnarson og Jørgen Ullebø Hjartøy</h2>
<h3>Instruksjoner</h3>
Inne i mappen ML2 kan du finne filen ML-Oblig2-Copy3.ipynb. Denne filen kan åpnes og reprodusere filen transfor&predict.jpblib som er modellen vår for denne innleveringen. 
I mappen deployment-flask kan du finne filen som deployer modellen vår ved bruk av flask. 
I mappen data finner du dataene som ML-Oblig2-Copy3.ipynb bruker for å lage modellen vår.

<h3>Rapport</h3>
Oppgaven gikk ut på å lage en maksinlærings modell og så sette den i drift. Det ble gitt ut noen valg av dataset en kunne sette seg inn i og så begynne å jobbe med det
valgte datasettet. 
<br>
<br>
Vi var 2 stykker på gruppen og har hatt et veldig hektisk og arbeidskrevende semester. Vi startet med å velge settet "Customer Revenue Prediction". 
Etter 3-4 dager med arbeid på dette settet så vi at vi aldri ville bli ferdie med denne oppgaven grunnet kompleksiteten i datasettene og ikke minst størrelsen på datasettene. 
Det tok oss altfor lang tid å laste ned datasettet og å håndtere dem. Vi hadde rett og slett ikke gode nok datamaskiner til å jobbe med slike store datasett. 
Etter dette hadde vi lite tid på å bli ferdige med innleveringen så for at vi skulle bli ferdige bestemte vi oss for å veøge et av de lettere datasettene. 
Gruppen gikk da for å jobbe med "Adult Census Income". I denne oppgaven får man et dataset som man må splitte opp i et treningsset og et test set. Målet i ppgaven er å 
lage en modell som forrutser om en person vil tjene mer eller mindre enn 50 tusen dollar i året ut ifra forskjellige attributter.
<br>
<br>
Vi startet med å analysere dataene og jobbe med dem slik vi hadde gjort i forrige innlevering. etter noen dager hadde vi laget en modell som tok inn alle attributter som 
ble gitt i datasettet(bortsett fra income selvfølgelig). denne modellen ga en treffsikkerhet på ca. 84 prosent. 
Da gruppen starte med deployment så vi at det ble mye å fylle inn hele 12 attributter. Vi valgte de som var mest relevante og endte opp med 8 attributter som input i 
web applikasjonen. Etter å ha fått modellen til å funke så vi at outputen ikke så veldig riktig ut. Vi gikk tilbake til modellen og utformet en modell som bare tar inn de 
attributtene som blir spurt om i web applikasjonen. Vi ofret ca. 2 prosent treffsikkerhet, men modellen så ut til å fungere mye bedre nå. Det eneste som kanskje kan være feil i modellen er at når den printer ut prediction og uncertanty får vi noen rare tall som vi ikke tror stemmer helt.
<br>
<br>
Det kan også nevnes at den gamle modellen og den gamle notebooken ligger i deployment-flask sine mapper sammen med de oppdaterte filene som er i bruk i web applikasjonen. 