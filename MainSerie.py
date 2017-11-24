import Serie

serie1 = Serie.Serie("Stranger Things", 2, False, "Thriller", "Duffer Brothers")
serie2 = Serie.Serie("Games of Thrones", 7, False, "Accion", "George R.R. Martin")
serie3 = Serie.Serie("Los Simpsons", 25, False, "Comedia", "Matt Groening")
serie4 = Serie.Serie("Rick & Morty", 3, False, "Comedia", "Justin Roiland")
serie5 = Serie.Serie("Big Bang", 11, False, "Sitcom", "Chuck Lorre")

juego1 = Serie.Videojuego("CS:GO", 1500, False, "FPS", "Valve")
juego2 = Serie.Videojuego("PUBG", 1400, False, "Shooter", "BlueHole")
juego3 = Serie.Videojuego("Middle Earth: Shadow of War", 15, False, "Accion", "WB Games")
juego4 = Serie.Videojuego("GTA V", 650, False, "Aventura", "Rockstar")
juego5 = Serie.Videojuego("Metal Gear Solid V", 8, False, "Aventura", "Konami")

juego1.entregar()
juego3.entregar()
juego5.entregar()

serie1.entregar()
serie3.entregar()
serie5.entregar()

listaSeries = [serie1, serie2, serie3, serie4, serie5]
listaJuegos = [juego1, juego2, juego3, juego4, juego5]

seriesEntregadas=0
juegosEntregados=0
numTemporadas=0
nHoras=0
serieConMasTemporadas=""
juegoConMasHoras=""

for e in listaSeries:
    if e.entregado is True:
        seriesEntregadas=seriesEntregadas+1
        print(e.getTitulo()+" entregada.")
    if e.getNTemporadas() > numTemporadas:
        numTemporadas=e.getNTemporadas()
        serieConMasTemporadas=e.getTitulo()


for e in listaJuegos:
    if e.entregado is True:
        juegosEntregadas=juegosEntregados+1
        print(e.getTitulo()+" entregado.")
    if e.getHorasEstimadas() > nHoras:
        nHoras=e.getHorasEstimadas()
        juegoConMasHoras=e.getTitulo()

print("El juego con mas horas es: "+juegoConMasHoras+" con "+str(nHoras)+" horas.")
print("La serie con mas temporadas es: "+serieConMasTemporadas+" con "+str(numTemporadas)+" temporadas.")