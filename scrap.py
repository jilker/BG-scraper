import pyexcel
from zacatrus import zacatrus_request
from juegosenlamesa import juegosenlamesa_request
from dracotienda import dracotienda_request
from jugamosuna import jugamosuna_request
from Dungeon_marvels import dugeonmarvels_request
from mathom import mathon_request
import concurrent.futures
from loguru import logger

data = []
pool = [dracotienda_request,dugeonmarvels_request,mathon_request,jugamosuna_request,zacatrus_request,juegosenlamesa_request]
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(unit) for unit in pool]
    for future in concurrent.futures.as_completed(futures):
        data+=(future.result())
        logger.info("Thread completed: data -> "+ str(len(data)))
logger.debug("Saving...")
pyexcel.save_as(records=data, dest_file_name = "dest_file.xls")
