# HonestPool

**Честный BITCOIN PUZZLE POOL от HoMLoL**

Добро пожаловать в честный пул с открытым исходным кодом, использующий ПО VanitySearch от [https://github.com/FixedPaul/VanitySearch-Bitcrack](https://github.com/FixedPaul/VanitySearch-Bitcrack), а также открытым API. Всё максимально честно, открыто и прозрачно!

## Как это работает?

Диапазоны пазлов разбиты на области. Для 71-го пазла это 67 108 864 областей. Для каждой области генерируются 5 проверочных адресов, которые нужно указать, чтобы завершить область.

## Какое ПО используется?

Используется ПО VanitySearch от [https://github.com/FixedPaul/VanitySearch-Bitcrack](https://github.com/FixedPaul/VanitySearch-Bitcrack).

Вы можете скачать его как из этого репозитория, так и по ссылке выше. Код и структура в ПО не изменялись — это было сделано для большего доверия.

## Автоматизация

Да! Всю автоматизацию выполняет Python-скрипт. По API он отправляет запрос на получение области, после чего добавляет адреса для поиска в файл `in.txt` и запускает VanitySearch. Для структуризации он сохраняет найденные ключи в папку `tmp_files_output_{номер пазла}` (например, `tmp_files_output_71`) под названием файла `out_{номер пазла}_{номер области}.txt` (например, `out_71_1.txt`).

После завершения работы VanitySearch скрипт парсит файл с найденными ключами (`tmp_files_output_71/out_71_1.txt`), проверяет, есть ли искомый адрес (`1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU`). Если такой адрес найден, он выводит информацию и завершает работу, а также добавляет запись в файл `FOUND!!!!!!!!.txt`. Если искомый адрес не найден, скрипт отправляет найденные проверочные адреса с закрытыми ключами на сервер через API, чтобы подтвердить и завершить область.

Думаю, всем понятно, что всё максимально прозрачно и честно!

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
