#!/usr/bin/env python
import logging

def getParameters(filename):
    logging.basicConfig(filename=filename,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='w')

    #Creating an object
    logger=logging.getLogger()

    #Setting the threshold of logger to DEBUG
    logger.setLevel(logging.INFO)
    return logger

