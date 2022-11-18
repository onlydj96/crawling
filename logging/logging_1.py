import logging

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level="WARNING")
    logger.info('aaa')
    logger.warning('bbb')
    logger.error('ccc')

if __name__ == '__main__':
    main()