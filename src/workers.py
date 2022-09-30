# -*- coding: utf-8 -*-
from PySide6.QtCore import QRunnable, pyqtSignal, QObject



class Worker(QRunnable):
	players_list_signal = pyqtSignal(list)
	new_release_signal = pyqtSignal(bool)


	def run(self):
		try:
			self.new_release_signal.emit(utils.check_new_release())
			players_list = []
			index_list = [0]
			cached_line = ""
			playing = False
			username = None
			while not username:
				username = utils.get_username()
			logger.info("Buscando nueva partida...")
			while True:
				if playing:
					logger.info("Sigue jugando, durmiendo...")
					time.sleep(60)
					logger.info("Desperté.")
				game_founded, index_list, cached_line, playing = utils.find_new_game(index_list, cached_line, playing=playing)
				if game_founded:
					logger.info("Hay nueva partida, guardo lo previo y emito señal.")
					success = utils.update_prev_games_players(index_list[-1], username)
					if not success:
						logger.error("Error obteniendo la lista de jugadores previos.")
					players_list = utils.get_players(index_list[-1], username)
					self.players_list_signal.emit(players_list)
					snipers = utils.get_snipers(players_list)
					if snipers:
						self.snipers_signal.emit(snipers)
		except Exception as ex:
			logger.exception(ex)