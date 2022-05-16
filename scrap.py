from zacatrus import zacatrus_request
from juegosenlamesa import juegosenlamesa_request
from dracotienda import dracotienda_request
from jugamosuna import jugamosuna_request
from Dungeon_marvels import dugeonmarvels_request
from mathom import mathon_request
import concurrent.futures
from loguru import logger
from database import create_connection,create_game
data = []
pool = [dracotienda_request,dugeonmarvels_request,mathon_request,jugamosuna_request,zacatrus_request,juegosenlamesa_request]
conn = create_connection("boardgames.db")
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(unit) for unit in pool]
    for future in concurrent.futures.as_completed(futures):
        for game in future.result():
            create_game(conn,(game["Title"],game["Price"],game["Old_Price"],game["Discount"],game["URL"],"None",game["Available"]))
        logger.info("Thread completed: data -> "+ str(len(future.result())))
