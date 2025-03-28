import re


def process_math_content(content: str) -> str:
    """
    Обрабатывает содержимое математического выражения:
      - Обрезает лишние пробелы и переносы строк.
      - Восстанавливает команды LaTeX, если вместо "\" получена табуляция.
      - Заменяет управляющие команды:
            \quad -> 2 пробела,
            \;    -> удаляется,
            \cdot -> ⋅,
            \notin -> ∉.
      - Заменяет основные LaTeX-команды (например, \div, \times, \dots, \text{...}) на соответствующие символы.
      - Выполняет расширенную замену дополнительных LaTeX-команд, таких как \subseteq, \to, \geq, \cup и т.д.
      - Убирает экранирование фигурных скобок.
      - Нормализует пробелы вокруг операторов и знаков препинания.

      Дополнительно: если вместо "\notin" в результате интерпретации встречается перенос строки,
      за которым следует "otin", исправляем на нужный символ.
    """
    content = content.strip()

    # Исправляем ошибку с переносом строки для "otin" (вместо "\notin")
    content = re.sub(r'\n(otin)', r' ∉ ', content)

    # Восстанавливаем обратные слэши, если вместо них получена табуляция
    content = content.replace("\t", "\\")
    content = re.sub(r'\\imes', r'\\times', content)
    content = re.sub(r'\\ext', r'\\text', content)

    # Заменяем управляющие команды
    content = re.sub(r'\\quad', '  ', content)  # 2 пробела
    content = re.sub(r'\\;', '', content)  # удаляем \;
    content = re.sub(r'\\cdot', '⋅', content)  # \cdot -> ⋅

    # Коррекция минуса (замена длинного минуса на дефис)
    content = re.sub(r'−', '-', content)

    # Обработка не принадлежности
    content = re.sub(r'\\notin', ' ∉ ', content)

    # Прочие базовые замены LaTeX-команд
    content = re.sub(r'\\div', '÷', content)
    content = re.sub(r'\\times', '×', content)
    content = re.sub(r'\\dots', '…', content)
    content = re.sub(r'\\text\s*\{([^}]*)\}', r'\1', content)

    # Расширенная замена LaTeX-команд (дополнительные символы)
    replacements = {
        r'\\subseteq': ' ⊆ ',
        r'\\supseteq': ' ⊇ ',
        r'\\subset': ' ⊂ ',
        r'\\supset': ' ⊃ ',
        r'\\o': ' → ',
        r'\\to': ' → ',
        r'\\Rightarrow': ' → ',
        r'\\leftarrow': ' ← ',
        r'\\gets': ' ← ',
        r'\\geq': ' ≥ ',
        r'\\le': ' ≤ ',
        r'\\neq': ' ≠ ',
        r'\\not=': ' ≠ ',
        r'\\forall': '∀',
        r'\\exists': '∃',
        r'\\cup': '∪',
        r'\\cap': '∩',
        r'\\infty': '∞',
        r'\\land': '∧',
        r'\\lor': '∨',
        r'\\implies': '⇒',
        r'\\iff': '⇔',
        r'\\sum': '∑',
        r'\\prod': '∏',
        r'\\int': '∫',
        r'\\sigma': 'σ',
        r'\\ne' : ' ≠ ',
        r'\\Longleftrightarrow': '  ⟺  ',
        r'\\\wedge': ' ∧ '

    }
    for latex_cmd, symbol in replacements.items():
        content = re.sub(latex_cmd, symbol, content)

    # Убираем экранирование фигурных скобок
    content = re.sub(r'\\\{', '{', content)
    content = re.sub(r'\\\}', '}', content)

    # Замена команд \in и \mid
    content = re.sub(r'\\in', '∈', content)
    content = re.sub(r'\\mid', '|', content)

    # Добавляем пробелы вокруг операторов
    content = re.sub(r'\s*=\s*', ' = ', content)
    content = re.sub(r'\s*\+\s*', ' + ', content)
    content = re.sub(r'\s*-\s*', ' - ', content)
    content = re.sub(r'\s*×\s*', ' × ', content)

    # Удаляем все вхождения команды тонкого пробела "\,"
    content = content.replace('\\,', '')
    # Нормализуем пробел после запятых
    content = re.sub(r',\s*', ', ', content)

    # Удаляем лишние пробелы
    content = re.sub(r'\s+', ' ', content)

    # Нормализуем окончания строк
    content = content.replace('\r\n', '\n')
    # Опционально: сводим несколько последовательных переводов строк к одному:
    content = re.sub(r'\n{2,}', '\n', content)

    return content.strip()


def remove_math_delimiters(text: str) -> str:
    """
    Удаляет математические окружения для блочных (\[...\]) и встроенных (\(...\)) выражений,
    обрабатывая их содержимое через process_math_content.
    """
    text = re.sub(r'\\\[\s*(.*?)\s*\\\]', lambda m: process_math_content(m.group(1)), text, flags=re.DOTALL)
    text = re.sub(r'\\\(\s*(.*?)\s*\\\)', lambda m: process_math_content(m.group(1)), text, flags=re.DOTALL)
    return text


def normalize_chatgpt_notation(text: str) -> str:
    """
    Преобразует текст с особенной нотацией ChatGPT в обычный Markdown.

    Этапы:
      1. Исправление повторов форматирующих фрагментов (например, "*x=1*x=1*x=1*" → "*x=1*").
      2. Удаление тройного повторения любых последовательностей.
      3. Преобразование математических выражений:
           – Убираются окружения (\[...\] и \( ... \));
           – Заменяются LaTeX-команды на соответствующие символы;
           – Убираются лишние пробелы и управляющие последовательности.
    """
    # Исправляем случаи, когда "\notin" было искажено (перенос строки + "otin")
    text = re.sub(r'\n(otin)', r' ∉', text)

    # Шаг 1: Исправление повторов форматирующих фрагментов.
    for delim in ['*', '_', '$', '`']:
        pattern = re.compile(
            rf'{re.escape(delim)}(?P<content>.+?){re.escape(delim)}'
            rf'(?P=content){re.escape(delim)}'
            rf'(?P=content){re.escape(delim)}'
        )
        text = pattern.sub(lambda m: f'{delim}{m.group("content")}{delim}', text)

    # Шаг 2: Удаление тройного повторения любых последовательностей.
    pattern = re.compile(r'(?P<dup>.{2,}?)(?P=dup)(?P=dup)')
    while True:
        new_text = pattern.sub(lambda m: m.group("dup"), text)
        if new_text == text:
            break
        text = new_text

    # Шаг 3: Преобразование математических выражений.
    text = remove_math_delimiters(text)

    lines = [line.strip() for line in text.splitlines() if line.strip() != '']
    text = "\n".join(lines)
    return text


if __name__ == "__main__":
    sample_text = """Рассмотрим множества  
\[
A = \{1,2,3,4,5\},\quad B = \{3,4,5,6\}.
\]

### (а) \(U_4 = \{(x,y) \mid x + 2y = 10\}\)

Нужно выбрать \(x \in A\) и \(y \in B\) так, чтобы выполнялось равенство \(x + 2y = 10\).

Перебираем значения \(y\) из \(B\) и вычисляем \(x = 10 - 2y\):

- Для \(y=3\): \(x = 10 - 2\cdot3 = 4\).  
  Так как \(4 \in A\), пара \((4,3)\) подходит.
- Для \(y=4\): \(x = 10 - 2\cdot4 = 2\).  
  \(2 \in A\), получаем пару \((2,4)\).
- Для \(y=5\): \(x = 10 - 2\cdot5 = 0\).  
  \(0 \notin A\) — пара не подходит.
- Для \(y=6\): \(x = 10 - 2\cdot6 = -2\).  
  \(-2 \notin A\) — пара не подходит.

Таким образом,  
\[
U_4 = \{(4,3),\,(2,4)\}.
\]

---

### (б) \(V_4 = \{(x,y) \mid x \ne y\}\)

Пары рассматриваем из декартова произведения \(A \times B\).  
При этом \(x \in A\), \(y \in B\), и нужно, чтобы \(x\) не равнялось \(y\).

Перечислим все пары и исключим те, где \(x=y\):

- Для \(x=1\) (так как \(1\) не встречается в \(B\), все пары подходят):
  \[
  (1,3),\,(1,4),\,(1,5),\,(1,6)
  \]
- Для \(x=2\) (2 не встречается в \(B\)):
  \[
  (2,3),\,(2,4),\,(2,5),\,(2,6)
  \]
- Для \(x=3\) (3 встречается в \(B\), поэтому исключаем \((3,3)\)):
  \[
  (3,4),\,(3,5),\,(3,6)
  \]
- Для \(x=4\) (4 встречается в \(B\), исключаем \((4,4)\)):
  \[
  (4,3),\,(4,5),\,(4,6)
  \]
- Для \(x=5\) (5 встречается в \(B\), исключаем \((5,5)\)):
  \[
  (5,3),\,(5,4),\,(5,6)
  \]

Итак,  
\[
V_4 = \{(1,3),\,(1,4),\,(1,5),\,(1,6),\,(2,3),\,(2,4),\,(2,5),\,(2,6),\,(3,4),\,(3,5),\,(3,6),\,(4,3),\,(4,5),\,(4,6),\,(5,3),\,(5,4),\,(5,6)\}.
\]

---

Ответы:

- \(U_4 = \{(4,3), (2,4)\}\)
- \(V_4 = \{(1,3), (1,4), (1,5), (1,6),\; (2,3), (2,4), (2,5), (2,6),\; (3,4), (3,5), (3,6),\; (4,3), (4,5), (4,6),\; (5,3), (5,4), (5,6)\}\).
    """
    normalized_text = normalize_chatgpt_notation(sample_text)
    print("Преобразованный текст:")
    print(normalized_text)
