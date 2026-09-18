# -*- coding: utf-8 -*-

import logger

_initialized = False


def initialize():

    global _initialized

    if _initialized:
        return

    logger.initialize()

    logger.info("----------------------------------")
    logger.info("TopoGuard iniciado")
    logger.info("----------------------------------")

    _initialized = True