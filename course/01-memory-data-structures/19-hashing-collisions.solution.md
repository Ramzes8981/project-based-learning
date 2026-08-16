# Разбор упражнения 1.19

После удаления A в slot 3 должен остаться TOMBSTONE. Lookup B обязан пройти slot 3 и проверить slot 4/далее. Если поставить EMPTY, search может преждевременно завершиться.

При insert нельзя немедленно занять первый tombstone до проверки remainder probe chain на existing same key. Без этого update может превратиться в duplicate insertion.
