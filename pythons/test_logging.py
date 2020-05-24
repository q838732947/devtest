import logging
import time
# logging.basicConfig(level=logging.DEBUG)

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='test_logging.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

# https://www.cnblogs.com/yyds/p/6901864.html
def test():
    # pytest 默认不打印这些日志，只有用python *.py才会看到
    logging.debug("This is a debug log.")
    logging.info("This is a info log.")
    logging.warning("This is a warning log.")
    logging.error("This is a error log.")
    logging.critical("This is a critical log.")




def test_1():
    log = logging.getLogger('test_1')
    time.sleep(1)
    log.debug('after 1 sec')
    time.sleep(1)
    log.debug('after 2 sec')
    time.sleep(1)
    log.debug('after 3 sec')
    assert 1, 'should pass'
    string="chenling"
    dic={"key":"value","a":1}
    log.debug(f"myname is {string}")
    log.debug(f"my dic is {dic}")


def test_2():
    log = logging.getLogger('test_1')
    time.sleep(1)
    log.debug('after 1 sec')
    time.sleep(1)
    log.debug('after 2 sec')
    time.sleep(1)
    log.debug('after 3 sec')
    assert 0, 'failing for demo purposes'


if __name__ == '__main__':
    test()
# pytest -s test_logging.py