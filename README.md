# terezapetrova00_projekt3_webscraping

Třetí projekt na Python Akademii od Engeta.

Popis projektu

Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlédnutí najdete zde - https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ.

Instalace knihoven

Knihovny, které jsou použity v kódu jsou uloženy v souboru requirements.txt. Pro instalaci doporučuji použít nové virtuální prostředí a spustit následovně:
pip3 --version
pip3 install -r requirements.txt

Spuštění projektu

Spuštění souboru main.py v rámci příkazového řádku požaduje dva argumenty.

python main.py "URL" "soubor.csv"
příklad: python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102" (výběr obce Beroun) "vysledky_beroun.csv" => vygeneruje se soubor ve formátu csv, kde jsou obsaženy výsledky za okres Beroun dle obcí

Průběh stahování:
Načítám seznam obcí…
Nalezeno obcí: 85
– Zpracovávám: Bavoryně (534421)
– Zpracovávám: Beroun (531057)
– Zpracovávám: Běštín (531073)
– Zpracovávám: Broumy (531081)
– Zpracovávám: Březová (531090)
– Zpracovávám: Bubovice (531103)
– Zpracovávám: Bykoš (534145)
– Zpracovávám: Bzová (531120)
– Zpracovávám: Cerhovice (531138)
– Zpracovávám: Drozdov (531154)
– Zpracovávám: Felbabka (531162)
– Zpracovávám: Hlásná Třebaň (531171)
– Zpracovávám: Hořovice (531189)
– Zpracovávám: Hostomice (531201)
– Zpracovávám: Hředle (531219)
– Zpracovávám: Hudlice (531227)
– Zpracovávám: Hvozdec (531235)
– Zpracovávám: Hýskov (531243)
– Zpracovávám: Chaloupky (531251)
– Zpracovávám: Chlustina (534455)
– Zpracovávám: Chodouň (534447)
– Zpracovávám: Chrustenice (533670)
– Zpracovávám: Chyňava (531294)
– Zpracovávám: Jivina (531308)
– Zpracovávám: Karlštejn (531316)
– Zpracovávám: Komárov (531324)
– Zpracovávám: Koněprusy (531332)
– Zpracovávám: Korno (533793)
– Zpracovávám: Kotopeky (534072)
– Zpracovávám: Králův Dvůr (533203)
– Zpracovávám: Kublov (531375)
– Zpracovávám: Lážovice (533939)
– Zpracovávám: Lhotka (533335)
– Zpracovávám: Libomyšl (531448)
– Zpracovávám: Liteň (531456)
– Zpracovávám: Loděnice (531464)
– Zpracovávám: Lochovice (531472)
– Zpracovávám: Lužce (534404)
– Zpracovávám: Malá Víska (533319)
– Zpracovávám: Málkov (534218)
– Zpracovávám: Měňany (531529)
– Zpracovávám: Mezouň (531537)
– Zpracovávám: Mořina (531545)
– Zpracovávám: Mořinka (533912)
– Zpracovávám: Nenačovice (533602)
– Zpracovávám: Nesvačily (534269)
– Zpracovávám: Neumětely (531588)
– Zpracovávám: Nižbor (531596)
– Zpracovávám: Nový Jáchymov (531600)
– Zpracovávám: Olešná (531626)
– Zpracovávám: Osek (531634)
– Zpracovávám: Osov (531642)
– Zpracovávám: Otmíče (534111)
– Zpracovávám: Otročiněves (531669)
– Zpracovávám: Podbrdy (534285)
– Zpracovávám: Podluhy (531685)
– Zpracovávám: Praskolesy (531693)
– Zpracovávám: Rpety (531715)
– Zpracovávám: Skřipel (533963)
– Zpracovávám: Skuhrov (531740)
– Zpracovávám: Srbsko (531758)
– Zpracovávám: Stašov (531766)
– Zpracovávám: Suchomasty (531782)
– Zpracovávám: Svatá (531791)
– Zpracovávám: Svatý Jan pod Skalou (531804)
– Zpracovávám: Svinaře (531812)
– Zpracovávám: Tetín (531839)
– Zpracovávám: Tlustice (531847)
– Zpracovávám: Tmaň (531855)
– Zpracovávám: Točník (534463)
– Zpracovávám: Trubín (533106)
– Zpracovávám: Trubská (531880)
– Zpracovávám: Újezd (531901)
– Zpracovávám: Velký Chlumec (531910)
– Zpracovávám: Vinařice (534234)
– Zpracovávám: Vižina (534048)
– Zpracovávám: Vráž (531944)
– Zpracovávám: Všeradice (531952)
– Zpracovávám: Vysoký Újezd (531961)
– Zpracovávám: Zadní Třebaň (531979)
– Zpracovávám: Zaječov (531995)
– Zpracovávám: Záluží (532002)
– Zpracovávám: Zdice (532011)
– Zpracovávám: Žebrák (532029)
– Zpracovávám: Železná (599417)
Hotovo!

Výstup dle přiloženého souboru vysledky_beroun.csv
