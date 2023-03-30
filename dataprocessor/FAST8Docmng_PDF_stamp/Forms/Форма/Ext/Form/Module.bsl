﻿
&НаСервере
Процедура fast8ПроштамповатьФайлНаСервере()
	
	Если Не ПроверитьЗаполнение() Тогда
		Возврат;
	КонецЕсли;
	
	ШтрихкодированиеСервер.ВставитьРегистрационныйШтамп(Объект.ФайлPDF, Новый Структура, "");
	ОбщегоНазначенияКлиентСервер.СообщитьПользователю("Готово");
	
КонецПроцедуры // fast8ПроштамповатьФайлНаСервере()

&НаКлиенте
Процедура fast8ПроштамповатьФайл(Команда)
	
	fast8ПроштамповатьФайлНаСервере();
	
КонецПроцедуры // fast8ПроштамповатьФайл()

&НаСервере
Процедура fast8ИнсталлироватьБиблиотекиPythonНаСервере()
	
	ЗапуститьПриложение("pip install reportlab", "C:\python_docmng\", Истина);
	ЗапуститьПриложение("pip install PyPDF2", "C:\python_docmng\", Истина);
	ЗапуститьПриложение("pip install PyCryptodome", "C:\python_docmng\", Истина);
	ОбщегоНазначенияКлиентСервер.СообщитьПользователю("Готово");
	
КонецПроцедуры // fast8ИнсталлироватьБиблиотекиPythonНаСервере()

&НаКлиенте
Процедура fast8ИнсталлироватьБиблиотекиPython(Команда)
	
	fast8ИнсталлироватьБиблиотекиPythonНаСервере();
	
КонецПроцедуры // fast8ИнсталлироватьБиблиотекиPython()

&НаСервере
Процедура fast8ИнсталлироватьСкриптыНаСервере()
	
	СоздатьКаталог("C:\python_docmng\");
	
	ОбработкаОбъект = РеквизитФормыВЗначение("Объект");
	ОбработкаОбъект.ПолучитьМакет("fast8_docmng_base").Записать("C:\python_docmng\fast8_docmng_base.py", КодировкаТекста.UTF8);
	ОбработкаОбъект.ПолучитьМакет("fast8_pdf_stamp").Записать("C:\python_docmng\fast8_pdf_stamp.py", КодировкаТекста.UTF8);
	ОбщегоНазначенияКлиентСервер.СообщитьПользователю("Готово");
	
КонецПроцедуры // fast8ИнсталлироватьСкриптыНаСервере()

&НаКлиенте
Процедура fast8ИнсталлироватьСкрипты(Команда)
	
	fast8ИнсталлироватьСкриптыНаСервере();
	
КонецПроцедуры // fast8ИнсталлироватьСкрипты()
