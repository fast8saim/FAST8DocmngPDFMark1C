# FAST8 saim 10.03.2023
# Скрипт установки штампа регистрации в PDF-файле для 1С:Документооборот
# Базовый скрипт. Обеспечивает отказоустойчивость и снятие ошибок выполнения основного скрипта.

import traceback
import sys
import os

script_dir = os.getcwd()

if len(sys.argv) == 9 and sys.argv[1] == "1cdocmng":
    
    params = {
        'source_file': sys.argv[2],
        'result_file': sys.argv[3],
        'x_coordinat': int(sys.argv[4]),
        'y_coordinat': int(sys.argv[5]),
        'string_one': sys.argv[6],
        'string_two': sys.argv[7]
        }

    error_log = sys.argv[8]

    try:
        exec(open(f'{script_dir}\\fast8_pdf_stamp.py', "r", encoding = "utf").read(), params)
    except:
        print(traceback.format_exc())

        file = open(error_log, "w")
        file.write(traceback.format_exc())
        file.close()

else:
    print('Недостаточно параметров для запуска скрипта')
