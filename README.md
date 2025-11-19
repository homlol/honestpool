# HonestPool

# EN

**Honest BITCOIN PUZZLE POOL by HoMLoL**

Welcome to the honest, open-source pool using VanitySearch software from [https://github.com/FixedPaul/VanitySearch-Bitcrack](https://github.com/FixedPaul/VanitySearch-Bitcrack), along with an open API. Everything is maximally honest, open, and transparent!

## INFO
- Site: https://honestpool.ru
- Questions/Offers: TG @homlol_official
- Group: TG @homlol_pool

## Run
```
pip install -r requirements.txt
python StartScript.py
python StartScript.py -p 71
python StartScript.py -p 71 -n 487238
```
start.bat

## How does it work?

Puzzle ranges are divided into segments. For Puzzle 71, this means 67,108,864 segments. For each segment, 5 verification addresses are generated that need to be provided to complete the segment.

## What software is used?

The VanitySearch software from [https://github.com/FixedPaul/VanitySearch-Bitcrack](https://github.com/FixedPaul/VanitySearch-Bitcrack) is used.

You can download it either from this repository or from the link above. The code and structure in the software have not been modified - this was done for greater trust.

## Automation

Yes! All automation is handled by a Python script (StartScript.py). Via the API, it sends a request to get a segment, then adds the addresses to search for in the `in.txt` file and launches VanitySearch. For organization, it saves the found keys in the folder `tmp_files_output_{puzzle number}` (e.g., `tmp_files_output_71`) under the filename `out_{puzzle number}_{segment number}.txt` (e.g., `out_71_1.txt`).

After VanitySearch finishes, the script parses the file with the found keys (`tmp_files_output_71/out_71_1.txt`), checks if the target address (`1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU`) is present. If such an address is found, it outputs the information and terminates, also adding an entry to the `FOUND!!!!!!!!.txt` file. If the target address is not found, the script sends the found verification addresses along with their private keys to the server via the API to confirm and complete the segment.

I think it's clear to everyone that everything is maximally transparent and honest!

## StartScript.py
```
usage: StartScript.py [-h] [-p PUZZLE] [-n NUMBER] [-c COMMENT] [-t]

Parameters for script operation.

options:
  -h, --help            show this help message and exit
  -p PUZZLE, --puzzle PUZZLE
                        Puzzle number. Default is 71
  -n NUMBER, --number NUMBER
                        Segment number. Default is random
  -c COMMENT, --comment COMMENT
                        Comment after completing the segment
  -t, --test            TEST MODE FOR PUZZLE №70, CONSISTS OF 17179869184 SEGMENTS, FOR FAST SEGMENT COMPLETION,
                        EACH SEGMENT IS 2^36. To get FOUND, you need to specify segment number -n 11063563977.
                        Default is off
```

## API

**Base URL:** [https://honestpool.ru](https://honestpool.ru)

### `GET` /api/v1/getRange

| Parameter     | Type    | Required | Default Value | Information                           |
|--------------|--------|--------------|-----------------------|--------------------------------------|
| `idPuzzle`   | string | No          | 71                    | Puzzle number. Default is 71. Test puzzle is 70. |
| `numberRange`| string | No          | random                | Segment number. Default is random.  |

#### Request Examples

- https://honestpool.ru/api/v1/getRange
- https://honestpool.ru/api/v1/getRange?idPuzzle=71&numberRange=838640

#### Response Example

```json
{
  "ok": true,
  "idPuzzle": 71,
  "targetAddress": "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU",
  "startRangeHex": "40ccbef00000000000",
  "endRangeHex": "40ccbf000000000000",
  "numberRange": "838640",
  "bits": 44,
  "proofAddresses": [
    "15ZFxTfWZD8k855RUzPmshHHxVj4ErrH4s",
    "13xxGjoyPoWgCRRBWsMZVQoW8TMq2GjWo6",
    "19bLF3s55frjneyhuuXeprhqjaow1moESj",
    "14RDhNecss1CQMD3wQ3dJmCKX48QFWwetS",
    "17WLn2GAiAQWtzhJc7kobWeF1DL2WBKMWK"
  ]
}
```

### `POST` /api/v1/setRange

| Parameter              | Type    | Required | Information                                   |
|-----------------------|--------|--------------|----------------------------------------------|
| `idPuzzle`            | string | Yes          | Puzzle number.                                |
| `numberRange`         | string | Yes          | Segment number.                              |
| `checkProofAddresses` | json   | Yes          | Verification addresses with private keys in JSON format. |
| `comment`             | string | No          | Comment for the completed segment.             |

#### Request Example

**URL:** https://honestpool.ru/api/v1/setRange  
**Method:** POST  
**Request Body:**

```json
{
  "idPuzzle": "71",
  "numberRange": "1",
  "checkProofAddresses": "{\"1AD4QW5Q6gibLdjwGyBDyyJrY54cvKQxGP\": \"405864A632D8FE0326\", \"1GspY6uX82kPCVeWQSTqTCKxu49f3EWf7x\": \"405864A635033E0461\", \"1HiodgLdFnuEANN61EEZRb7MCn6KSsRvxG\": \"405864A636719CC264\", \"1L1hBgmfEWrkpGczia2itvMYFN8cwb6Uuz\": \"405864A63AE54145CD\", \"1H3T5xWX3gNZ4ZPB7fgecvAsy2hFqk6G8C\": \"405864A63D52D0422A\"}",
  "comment": "pool comment"
}
```

#### Response Example

```json
{
  "ok": true,
  "text": "You have successfully completed the range 1 in 71 puzzles"
}
```
Limit: **60 requests per 1 hour**

If the limit is exceeded more than 10 times in 7 days, your IP will be blocked for 24 hours.

# For server costs and motivation to continue supporting the project
### BTC: bc1q3plfvghrdsh768h3ukejs8zy5ev4jsr76tjtgk
### ETH: 0xa97888173A0A41242294299BE1b81Fe72433ac06
### USDT(TRC20): TNf8KHmmwEiVGSQyqVyKuZ8f95zEdnb3ND
### TON: UQDVvbUuncGxvGEqUUuchRfH7a_p8I3S7_6dMsuTkIw7amtL

# RU

**Честный BITCOIN PUZZLE POOL от HoMLoL**

Добро пожаловать в честный пул с открытым исходным кодом, использующий ПО VanitySearch от [https://github.com/FixedPaul/VanitySearch-Bitcrack](https://github.com/FixedPaul/VanitySearch-Bitcrack), а также открытым API. Всё максимально честно, открыто и прозрачно!

## INFO
- Site: https://honestpool.ru
- Questions/Offers: TG @homlol_official
- Group: TG @homlol_pool

## Запуск
```
pip install -r requirements.txt
python StartScript.py
python StartScript.py -p 71
python StartScript.py -p 71 -n 487238
```
start.bat

## Как это работает?

Диапазоны пазлов разбиты на области. Для 71-го пазла это 67 108 864 областей. Для каждой области генерируются 5 проверочных адресов, которые нужно указать, чтобы завершить область.

## Какое ПО используется?

Используется ПО VanitySearch от [https://github.com/FixedPaul/VanitySearch-Bitcrack](https://github.com/FixedPaul/VanitySearch-Bitcrack).

Вы можете скачать его как из этого репозитория, так и по ссылке выше. Код и структура в ПО не изменялись — это было сделано для большего доверия.

## Автоматизация

Да! Всю автоматизацию выполняет Python-скрипт(StartScript.py). По API он отправляет запрос на получение области, после чего добавляет адреса для поиска в файл `in.txt` и запускает VanitySearch. Для структуризации он сохраняет найденные ключи в папку `tmp_files_output_{номер пазла}` (например, `tmp_files_output_71`) под названием файла `out_{номер пазла}_{номер области}.txt` (например, `out_71_1.txt`).

После завершения работы VanitySearch скрипт парсит файл с найденными ключами (`tmp_files_output_71/out_71_1.txt`), проверяет, есть ли искомый адрес (`1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU`). Если такой адрес найден, он выводит информацию и завершает работу, а также добавляет запись в файл `FOUND!!!!!!!!.txt`. Если искомый адрес не найден, скрипт отправляет найденные проверочные адреса с закрытыми ключами на сервер через API, чтобы подтвердить и завершить область.

Думаю, всем понятно, что всё максимально прозрачно и честно!

## StartScript.py
```
usage: StartScript.py [-h] [-p PUZZLE] [-n NUMBER] [-c COMMENT] [-t]

Параметры для работы скрипта.

options:
  -h, --help            show this help message and exit
  -p PUZZLE, --puzzle PUZZLE
                        Номер пазла. По умолчанию 71
  -n NUMBER, --number NUMBER
                        Номер области(части). По умолчанию random
  -c COMMENT, --comment COMMENT
                        Комментарий после завершения области
  -t, --test            ТЕСТОВЫЙ РЕЖИМ ПАЗЛА №70, СОСТОИТ ИЗ 17179869184 ОБЛАСТЕЙ, ДЛЯ БЫСТРОГО ПРОХОЖДЕНИЯ
                        ОБЛАСТИ, КАЖДАЯ ОБЛАСТЬ 2^36. Для того чтобы был FOUND нужно указать номер области -n
                        11063563977. По умолчанию выключен
```

## API

**Базовый URL:** [https://honestpool.ru](https://honestpool.ru)

### `GET` /api/v1/getRange

| Параметр     | Тип    | Обязательный | Значение по умолчанию | Информация                           |
|--------------|--------|--------------|-----------------------|--------------------------------------|
| `idPuzzle`   | string | Нет          | 71                    | Номер пазла. По умолчанию 71. Тестовый пазл — 70. |
| `numberRange`| string | Нет          | random                | Номер области. По умолчанию random.  |

#### Примеры запросов

- https://honestpool.ru/api/v1/getRange
- https://honestpool.ru/api/v1/getRange?idPuzzle=71&numberRange=838640

#### Пример ответа

```json
{
  "ok": true,
  "idPuzzle": 71,
  "targetAddress": "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU",
  "startRangeHex": "40ccbef00000000000",
  "endRangeHex": "40ccbf000000000000",
  "numberRange": "838640",
  "bits": 44,
  "proofAddresses": [
    "15ZFxTfWZD8k855RUzPmshHHxVj4ErrH4s",
    "13xxGjoyPoWgCRRBWsMZVQoW8TMq2GjWo6",
    "19bLF3s55frjneyhuuXeprhqjaow1moESj",
    "14RDhNecss1CQMD3wQ3dJmCKX48QFWwetS",
    "17WLn2GAiAQWtzhJc7kobWeF1DL2WBKMWK"
  ]
}
```

### `POST` /api/v1/setRange

| Параметр              | Тип    | Обязательный | Информация                                   |
|-----------------------|--------|--------------|----------------------------------------------|
| `idPuzzle`            | string | Да           | Номер пазла.                                |
| `numberRange`         | string | Да           | Номер области.                              |
| `checkProofAddresses` | json   | Да           | Проверочные адреса с закрытыми ключами в формате JSON. |
| `comment`             | string | Нет          | Комментарий к пройденной части.             |

#### Пример запроса

**URL:** https://honestpool.ru/api/v1/setRange  
**Метод:** POST  
**Тело запроса:**

```json
{
  "idPuzzle": "71",
  "numberRange": "1",
  "checkProofAddresses": "{\"1AD4QW5Q6gibLdjwGyBDyyJrY54cvKQxGP\": \"405864A632D8FE0326\", \"1GspY6uX82kPCVeWQSTqTCKxu49f3EWf7x\": \"405864A635033E0461\", \"1HiodgLdFnuEANN61EEZRb7MCn6KSsRvxG\": \"405864A636719CC264\", \"1L1hBgmfEWrkpGczia2itvMYFN8cwb6Uuz\": \"405864A63AE54145CD\", \"1H3T5xWX3gNZ4ZPB7fgecvAsy2hFqk6G8C\": \"405864A63D52D0422A\"}",
  "comment": "pool comment"
}
```

#### Пример ответа

```json
{
  "ok": true,
  "text": "You have successfully completed the range 1 in 71 puzzles"
}
```
Лимит: **60 запросов за 1 час**

При привышении лимита более 10-ти раз за 7 дней, ваш ip будет заблокирован на 24 час.

# На оплату сервера и мотивацию дальше поддерживать проект
### BTC: bc1q3plfvghrdsh768h3ukejs8zy5ev4jsr76tjtgk
### ETH: 0xa97888173A0A41242294299BE1b81Fe72433ac06
### USDT(TRC20): TNf8KHmmwEiVGSQyqVyKuZ8f95zEdnb3ND
### TON: UQDVvbUuncGxvGEqUUuchRfH7a_p8I3S7_6dMsuTkIw7amtL
