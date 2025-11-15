import requests
import json
import os
import argparse
import re
import time

def parse_key_file(filename):
    """
    Считывает файл с Bitcoin адресами и приватными ключами,
    возвращает массив с парами (адрес, приватный ключ в HEX)
    """
    result = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Используем регулярные выражения для поиска адресов и ключей
        pattern = r'Public Addr: ([1-9A-HJ-NP-Za-km-z]+)\s*Priv \(WIF\): [^\n]+\s*Priv \(HEX\): 0x([0-9A-Fa-f]+)'
        matches = re.findall(pattern, content)
        
        for address, priv_key_hex in matches:
            # Убираем ведущие нули из HEX ключа
            clean_priv_key = priv_key_hex.lstrip('0') or '0'
            result[address] = clean_priv_key
            
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    
    return result

def getRange(idPuzzle, numberRange):
	url = f"https://honestpool.ru/api/v1/getRange?idPuzzle={idPuzzle}&numberRange={numberRange}"
	response = requests.get(url)
	try:
		return response.json()
	except Exception as e:
		print(e)
	else:
		pass
	finally:
		pass

def setRange(idPuzzle, numberRange, checkProofAddresses = {}, comment = ''):
	url = "https://honestpool.ru/api/v1/setRange"
	data = {"idPuzzle": idPuzzle, "numberRange": numberRange, "checkProofAddresses": json.dumps(checkProofAddresses), "comment": comment}
	response = requests.post(url, data=data)
	try:
		return response.json()
	except Exception as e:
		print(e)
	else:
		pass
	finally:
		pass

def out_default(text):
	print("\033[0m {}" .format(text))
def out_red(text):
	print("\033[31m {}" .format(text))
def out_yellow(text):
	print("\033[33m {}" .format(text))
def out_blue(text):
	print("\033[34m {}" .format(text))
def out_green(text):
	print("\033[32m {}" .format(text))
def out_text_bold(text):
	print("\033[1m {}" .format(text))
def out_bg_green_text_white(text):
	print("\033[42m\033[37m {}" .format(text))

if __name__ == "__main__":
	# tmp's
	#main_path = "C:/bitcoin/VanitySearchHomlol/x64/Release/" # заменить на нужный путь или оставить пустыл если файл находится в одной папке вместе с VanitySearch
	main_path = ""
	name_in_file = "in.txt"
	quantity = 0

	# Создаем парсер аргументов
	parser = argparse.ArgumentParser(description="Параметры для работы скрипта.")

	# Добавляем аргументы
	parser.add_argument('-p', '--puzzle', type=int, default=71, help='Номер пазла. По умолчанию 71')
	parser.add_argument('-n', '--number', type=str, default='random', help='Номер области(части). По умолчанию random')
	parser.add_argument('-c', '--comment', type=str, default='BITCOIN PUZZLE HoMLoL POOL bc1qdn2wng73y80phr7kul5aa24n850f5c82zwq27h', help='Комментарий после завершения области')
	parser.add_argument('-t', '--test', action="store_true", help='ТЕСТОВЫЙ РЕЖИМ ПАЗЛА №70, СОСТОИТ ИЗ 17179869184 ОБЛАСТЕЙ, ДЛЯ БЫСТРОГО ПРОХОЖДЕНИЯ ОБЛАСТИ, КАЖДАЯ ОБЛАСТЬ 2^36. Для того чтобы был FOUND нужно указать номер области -n 11063563977. По умолчанию выключен')

	# Парсим аргументы
	args = parser.parse_args()

	__TEST__ = args.test

	if __TEST__: # ТЕСТОВЫЙ РЕЖИМ ПАЗЛА №70, СОСТОИТ ИЗ 17179869184 ОБЛАСТЕЙ, ДЛЯ БЫСТРОГО ПРОХОЖДЕНИЯ ОБЛАСТИ, КАЖДАЯ ОБЛАСТЬ 2^36. Для того чтобы был FOUND нужно указать номер области -n 11063563977
		__PUZZLE__ = 70
		__NUMBER__ = args.number
		__COMMENT__ = args.comment
	else:
		__PUZZLE__ = args.puzzle
		__NUMBER__ = args.number
		__COMMENT__ = args.comment

	while True:
		os.system('cls')

		mass_checked_range = {}

		out_yellow('-----------------------------------------------------------------------------')
		out_yellow('----------------------- BITCOIN PUZZLE POOL от HoMLoL -----------------------')
		out_yellow('-----------------------------------------------------------------------------')
		out_yellow('-- Site: https://honestpool.ru                                             --')
		out_yellow('-- Git: https://honestpool.ru                                              --')
		out_yellow('-- VanitySearch: https://github.com/FixedPaul/VanitySearch-Bitcrack        --')
		out_yellow('-- Questions/Offers: TG @homlol_official                                   --')
		out_yellow('-- Group: TG @homlol_pool                                                  --')
		out_yellow('-- Donate BTC: bc1qdn2wng73y80phr7kul5aa24n850f5c82zwq27h                  --')
		out_yellow('-----------------------------------------------------------------------------')

		_getRange = getRange(__PUZZLE__, __NUMBER__)

		if _getRange['ok'] == True:

			__ADDRESS__ = _getRange['targetAddress']
			numberRange_for_send = _getRange['numberRange']

			if __TEST__ or __PUZZLE__ == 70:
				print('\n')
				out_yellow('-' * 29)
				out_yellow('- !!!WARNING!!! - TEST MODE -')
				out_yellow('-' * 29)
				print('\n')

			print(f'\033[0m* ID puzzle: {_getRange['idPuzzle']}')
			print(f'* Range number: {_getRange['numberRange']}')
			print(f'* Target Address: \033[42m\033[37m{_getRange['targetAddress']}')
			print(f'\033[0m* Proof addresses:')
			file_path = f'{main_path}{name_in_file}'
			with open(file_path, 'w', encoding='utf-8') as file:
				file.write(str(_getRange['targetAddress'])+"\n") # TARGET ADDRESS
				for i in _getRange['proofAddresses']:
					file.write(str(i)+"\n") # PROOF ADDRESS
					print(f'\t - {i}')
			print(f'* Bits: {_getRange['bits']}')
			print(f'* Range hex: {_getRange['startRangeHex']}:{_getRange['endRangeHex']}')
			print(f'* Start VanitySearch: {_getRange['bits']}')

			#tmp file output
			name_file_output = f"out_{_getRange['idPuzzle']}_{_getRange['numberRange']}.txt"
			name_out_file = f"{main_path}tmp_files_output_{_getRange['idPuzzle']}/{name_file_output}"

			if not os.path.exists(f"{main_path}tmp_files_output_{_getRange['idPuzzle']}"):
				os.makedirs(f"{main_path}tmp_files_output_{_getRange['idPuzzle']}")

			os.system(f'{main_path}VanitySearch.exe -gpuId 0 -i {main_path}{name_in_file} -o {name_out_file} -start {_getRange['startRangeHex']} -range {_getRange['bits']}')


			key_pairs = parse_key_file(f'{name_out_file}')

			if __ADDRESS__ in key_pairs: # если нашли основной ключ!!!!
				out_green('-' * 101)
				out_green('-' * 101)
				out_green('-- !!! НАЙДЕНО !!! !!! НАЙДЕНО !!! !!! НАЙДЕНО !!! !!! НАЙДЕНО !!! !!! НАЙДЕНО !!! !!! НАЙДЕНО !!! --')
				out_green('--                                                                                                 --')
				out_green('--                                                                                                 --')
				out_green(f'-- ADDRESS: {__ADDRESS__}')
				out_green(f'-- PRIVATE KEY: {key_pairs[__ADDRESS__]}')
				out_green('--                                                                                                 --')
				out_green('--                                                                                                 --')
				out_green('-- !!! НАЙДЕНО !!! !!! НАЙДЕНО !!! !!! НАЙДЕНО !!! !!! НАЙДЕНО !!! !!! НАЙДЕНО !!! !!! НАЙДЕНО !!! --')
				out_green('-' * 101)
				out_green('-' * 101)
				with open("FOUND!!!!!!!!.txt", "a", encoding="utf-8") as f:
					f.write(f"\n-------------------- FOUND --------------------\nPRIVATE KEY HEX: {key_pairs[__ADDRESS__]}\nADDRESS: {__ADDRESS__}\n----------------------------------------\n")
				break;
			else: # если нет, отправляем инфу в пул
				if not key_pairs:
					out_red("* Error: Not data for send")
					with open("LOG_ERROR.txt", "a", encoding="utf-8") as f:
						f.write("\n* Error: Not data for send\n")
				else:
					_setRange = setRange(__PUZZLE__, numberRange_for_send, key_pairs, __COMMENT__)

					if _setRange['ok'] == True:
						if __NUMBER__ != 'random':
							__NUMBER__ = 'random'
						print(_setRange['text'])
						out_green('Успешно пройденный диапазон!')
						out_yellow('Запуск через 5 секунд... Ожидайте...')
						time.sleep(5) # Задержка на 5 секунд
					else:
						with open("LOG_ERROR.txt", "a", encoding="utf-8") as f:
							f.write(f'\nERROR: {_setRange['text']}\n')
						out_red(f'ERROR: {_setRange['text']}')
						out_yellow('Запуск через 5 секунд... Ожидайте...')
						time.sleep(5) # Задержка на 5 секунд
		else:
			if __NUMBER__ != 'random':
				__NUMBER__ = 'random'
			out_red(f'ERROR: {_getRange['text']}')
			with open("LOG_ERROR.txt", "a", encoding="utf-8") as f:
				f.write(f'\nERROR: {_getRange['text']}\n')
			out_yellow('Запуск через 5 секунд... Ожидайте...')
			time.sleep(5) # Задержка на 5 секунд
