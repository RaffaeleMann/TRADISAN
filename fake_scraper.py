import csv
import newspaper
from newspaper import news_pool

config = newspaper.Config()
config.browser_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
config.number_threads = 20
config.memoize_articles= False

databaseitalia = newspaper.build(url='https://www.databaseitalia.it/category/salute/', config=config)
thelivingspirits = newspaper.build(url='https://www.thelivingspirits.net/', config=config)
dionidream = newspaper.build(url='https://dionidream.com/', config=config)
zerohedge = newspaper.build(url='https://www.zerohedge.com/', config=config)
disquisendo = newspaper.build(url='https://disquisendo.wordpress.com/', config=config)
eventiavversi = newspaper.build(url='https://www.eventiavversinews.it/', config=config)
nexusedizioni = newspaper.build(url='https://nexusedizioni.it/it/S/news/ambiente-e-salute/medicina-e-salute/', config=config)
dagospia = newspaper.build(url='https://www.dagospia.com/rubrica-39/salute', config=config)
pianetablunews = newspaper.build(url='https://www.pianetablunews.it/category/salute/', config=config)
scienzaeconoscenza = newspaper.build(url='https://www.scienzaeconoscenza.it/', config=config)
provitaefamiglia = newspaper.build(url='https://www.provitaefamiglia.it/blog', config=config)
filosofiaescienza = newspaper.build(url='http://www.filosofiaescienza.it/category/medicina/', config=config)
comedonchisciotte = newspaper.build(url='https://comedonchisciotte.org/', config=config)
chesuccede = newspaper.build(url='https://www.chesuccede.it/lifestyle/salute/', config=config)
byoblu_covid19 = newspaper.build(url='https://www.byoblu.com/tag/covid19/', config=config)
byoblu_salute = newspaper.build(url='https://www.byoblu.com/tag/salute/', config=config)
essereinformati = newspaper.build(url='https://essere-informati.it/category/salute/', config=config)
eticamente = newspaper.build(url='https://www.eticamente.net/category/benessere', config=config)
grandeinganno = newspaper.build(url='https://grandeinganno.it/', config=config)
ilfattaccio = newspaper.build(url='https://www.ilfattaccio.org/', config=config)
raffaelepalermonews = newspaper.build(url='https://raffaelepalermonews.com/covid-19/', config=config)
silenziefalsita = newspaper.build(url='https://www.silenziefalsita.it/salute/', config=config)
voxnews_salute = newspaper.build(url='https://voxnews.info/category/salute/', config=config)
voxnews_coronavirus = newspaper.build(url='https://voxnews.info/category/salute/coronavirus/', config=config)
guarireoggi = newspaper.build(url='http://guarireoggi.blogspot.com/', config=config)
lastella = newspaper.build(url='https://lastella.altervista.org/category/salute/', config=config)
ingannati = newspaper.build(url='https://www.ingannati.it/category/covid/', config=config)
thecancermagazine = newspaper.build(url='http://thecancermagazine.blogspot.com/', config=config)
vivoinsalute = newspaper.build(url='https://www.vivoinsalute.com/', config=config)
vacciniinforma_malattie = newspaper.build(url='https://vacciniinforma.com/malattie/', config=config)
vacciniinforma_medicina = newspaper.build(url='https://vacciniinforma.com/medicina/', config=config)
medicinenon = newspaper.build(url='https://www.medicinenon.it/', config=config)
eurosalus = newspaper.build(url='https://www.eurosalus.com/?refresh_ce', config=config)
comilva = newspaper.build(url='https://www.comilva.org/informazione', config=config)
assis = newspaper.build(url='https://www.assis.it/', config=config)
alleanzadellasalute = newspaper.build(url='http://www.alleanzadellasalute.info/', config=config)
liberamenteservo = newspaper.build(url='https://www.liberamenteservo.com/benessere/', config=config)
sadefenza = newspaper.build(url='''https://sadefenza.blogspot.com/search/label/Salute%20e%20Benessere''', config=config)
socialbuzz = newspaper.build(url='http://socialbuzz.it/benessere/', config=config)
sulatestagiannilannes = newspaper.build(url='http://sulatestagiannilannes.blogspot.com/search/label/sanit%C3%A0', config=config)
ilparagone = newspaper.build(url='https://www.ilparagone.it/salute/', config=config)
mag24cloud = newspaper.build(url='https://www.mag24.cloud/category/benessere/', config=config)
controinformazione_dittatura_sanitaria = newspaper.build(url='https://www.controinformazione.info/category/dittatura-sanitaria/', config=config)
controinformazione_crisi_sanitarie = newspaper.build(url='https://www.controinformazione.info/category/crisi-sanitarie/', config=config)
lacrunadellago_coronavirus = newspaper.build(url='https://www.lacrunadellago.net/category/coronavirus/', config=config)
lacrunadellago_dittatura_sanitaria = newspaper.build(url='https://www.lacrunadellago.net/category/dittatura-sanitaria/', config=config)

papers = [databaseitalia, thelivingspirits, dionidream, zerohedge, disquisendo, eventiavversi, nexusedizioni, dagospia, pianetablunews, scienzaeconoscenza, provitaefamiglia, filosofiaescienza, comedonchisciotte, chesuccede, byoblu_covid19, byoblu_salute, essereinformati, eticamente, grandeinganno, ilfattaccio, raffaelepalermonews, silenziefalsita, voxnews_salute, voxnews_coronavirus, guarireoggi, lastella, ingannati, thecancermagazine, vivoinsalute, vacciniinforma_malattie, vacciniinforma_medicina, medicinenon, eurosalus, comilva, assis, alleanzadellasalute, liberamenteservo, sadefenza, socialbuzz, sulatestagiannilannes, ilparagone, mag24cloud, controinformazione_dittatura_sanitaria, controinformazione_crisi_sanitarie, lacrunadellago_coronavirus, lacrunadellago_dittatura_sanitaria]
news_pool.set(papers, threads_per_source=20)
news_pool.join()

for site in papers:
    for article in site.articles:
        article.parse()

        with open('/home/luca/Scrivania/TRADISAN - FASE 1/fake.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([article.publish_date, article.title, article.text, article.images, article.url])