from loguru import logger

logger.add("meu_log.log")


def soma(x, y):
   try:
        soma = x + y
        logger.info(f"voce digitou valores corretos, parabéns {soma}") # se tudo funcionar!
        return soma
   except:
        logger.critical("voce tem que digitar valores corretos")

soma(2, 3)
soma(2, 7)
soma(2, "3")