import logging
import time
import numpy
import matplotlib.pyplot as plt

from Tracker import Tracker


logger = logging.getLogger(__name__)


def main():
    """ Executes the program.
    """
    tracker = Tracker()
    data = []
    plt.ion()
    while True:
        time.sleep(0.5)
        down_speed = 8 * (tracker.get_current_download_speed() / (2**20))
        up_speed = 8 * (tracker.get_current_upload_speed() / (2**20))
        data.append([down_speed, up_speed])
        print('Total data used : ' +
              str(round(tracker.get_total_data_used() / (2**20), 3)) +
              ' Mo.')
        plt.plot(data)
        plt.draw()
        plt.pause(0.0001)
        plt.clf()

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s ' +
                                  '-- %(levelname)s ' +
                                  '-- [%(filename)s:%(lineno)s ' +
                                  '-- %(funcName)s() ] ' +
                                  '-- %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    try:
        main()
    except Exception as e:
        logger.exception('Une erreur inattendue est survenue.')