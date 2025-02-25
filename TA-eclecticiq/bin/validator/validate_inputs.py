"""Validate Inputs."""
import ta_eclecticiq_declare  # pylint: disable=W0611 # noqa: F401
import os
import splunk.admin as admin

import datetime


from splunktaucclib.rest_handler.endpoint.validator import Validator
from validator.logger_manager import setup_logging

from constants.general import (
    DOMAIN,
    EMAIL,
    FILEHASH,
    IP,
    MAX_INTERVAL,
    MIN_INTERVAL,
    PORT,
    START_DATE,
    URI,
    URL,
)

from constants.messages import (
    BACKFILL_TIME_OLDER,
    FUTURE_DATE_IS_NOT_ACCEPTABLE,
    INTERVAL_IS_BETWEEN_MIN_AND_MAX_INTERVAL,
    INTERVAL_MUST_BE_BETWEEN_MIN_AND_MAX_INTERVAL,
    MAXIMUM_FIVE_OUTGOING_FEEDS,
    SELECT_ATLEAST_ONE_OBSERVABLE_TYPE,
    SELECT_ATLEAST_ONE_OBSERVABLE_TYPE_TO_BE_INGESTED,
    START_DATE_INCORRECT,
    START_DATE_NOT_VALID_FORMAT,
    UNIQUE_VALUES_FOR_OUTGOING_FEEDS_ALLOWED,
)
from constants.general import STR_ONE


logger = setup_logging("ta_eclecticiq_inputs")


class GetSessionKey(admin.MConfigHandler):  # type: ignore
    """Inheriting admin.MConfigHandler to get the current user's session key."""

    def __init__(self):
        """Set the session key as parameter to use while getting entities from Splunk REST."""
        self.session_key = self.getSessionKey()


class ValidateInputs(Validator):  # type: ignore
    """Inheriting the Validator Class for creating custom validations."""

    def __init__(self, *args, **kwargs):  # pylint: disable=W0613
        """Create instance of ValidateAccount class along with Super class parameters Setting the my_app parameter as main TA directory name."""
        super().__init__()
        self.my_app = __file__.split(os.sep)[-4]

    @staticmethod
    def check_outgoing_feed_length(outgoing_feed_ids):
        """Validate outgoing-feeds length.

        :param date: outgoing_feed_ids
        :type date: str
        :return: True if the outgoing-feeds is unique otherwise False
        :rtype: boolean
        """
        feed_ids = outgoing_feed_ids.split(",")

        if len(feed_ids) > 5:
            return False
        return True

    @staticmethod
    def validate_outgoing_feed_integer_only(outgoing_feed_ids):
        """Validate the interval is between 60s and 90 days.

        :param date: interval
        :type date: str
        :return: True if interval lies between min and max interval else False
        :rtype: boolean
        """
        try:
            feed_ids = outgoing_feed_ids.split(",")
            feed_ids = list(filter(None, feed_ids))
            value = [int(value) for value in feed_ids]
            logger.info(value)
        except ValueError:
            logger.error("Outgoing feed is not an integer value")
            return False
        return True

    @staticmethod
    def validate_unique_values(outgoing_feed_ids):
        """Validate unique outgoing-feeds only.

        :param date: outgoing_feed_ids
        :type date: str
        :return: True if the outgoing-feeds is unique otherwise False
        :rtype: boolean
        """
        feed_ids = outgoing_feed_ids.split(",")
        feed_ids = list(filter(None, feed_ids))
        if len(feed_ids) > len(list(set(feed_ids))):
            logger.info(UNIQUE_VALUES_FOR_OUTGOING_FEEDS_ALLOWED)
            return False
        return True

    @staticmethod
    def check_future_date(date):
        """Check start date provided by user is greater then current datetime.

        :param date: date
        :type date: str
        :return: True if the start date is not greater than current date else False
        :rtype: boolean
        """
        start_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        current_date = datetime.datetime.now()
        if start_date > current_date:
            return False
        return True

    @staticmethod
    def check_start_date_days(backfill_date):
        """Check Start date provided by user is not more than 90 days.

        :param backfill_date: datetime
        :type backfill_date: str
        :return: True if the date is not older than 90 days else False
        :rtype: boolean
        """
        start_date = datetime.datetime.strptime(backfill_date, "%Y-%m-%dT%H:%M:%S.%f")
        current_date = datetime.datetime.now()
        backfill_time = current_date - start_date

        if backfill_time.days < 90:
            return True
        return False

    @staticmethod
    def validate_format(date):
        """Validate Start date provided by user is in valid format.

        :param date: datetime
        :type date: str
        :return: True if the date is in valid format else False
        :rtype: boolean
        """
        try:
            res = bool(datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f"))
        except ValueError as error:
            logger.error(error)
            res = False
        return res

    @staticmethod
    def check_observable_types(data):
        """Validate atleast one observable type is selected.

        :param date: datetime
        :type date: str
        :return: True if atleast one observable type selected else False
        :rtype: boolean
        """
        observable_types = [DOMAIN, EMAIL, PORT, IP, URI, FILEHASH, URL]
        is_selected = False
        for key, value in data.items():
            if key in observable_types and value == STR_ONE:
                is_selected = True

        return is_selected

    @staticmethod
    def validate_interval(interval):
        """Validate the interval is between 60s and 90 days.

        :param date: interval
        :type date: str
        :return: True if interval lies between min and max interval else False
        :rtype: boolean
        """
        try:
            if isinstance(int(interval), int):
                if (  # pylint: disable=R1705
                    MIN_INTERVAL <= int(interval) <= MAX_INTERVAL
                ):
                    logger.info(INTERVAL_IS_BETWEEN_MIN_AND_MAX_INTERVAL)
                    return True
                else:
                    return False
            return True
        except ValueError:
            return True

    def validate(self, value, data):  # pylint: disable=W0613,R0911
        """
        Check if the url and api token provided by user is valid or not.

        :param value: value given in the Name field of configuration page/account.
        (Not required but only keeping as this method will be called with it by rest module.)
        :type value: str
        :param data: all the inputs provided by user in configuration page/account tab while saving.
        :type proxy: dict
        :return True or False
        """
        start_date = data[START_DATE]
        is_valid_format = ValidateInputs.validate_format(start_date)
        if not is_valid_format:
            logger.error(START_DATE_NOT_VALID_FORMAT)
            self.put_msg(START_DATE_NOT_VALID_FORMAT)
            return is_valid_format
        is_valid_backfill_days = ValidateInputs.check_start_date_days(start_date)
        if not is_valid_backfill_days:
            logger.info(BACKFILL_TIME_OLDER)
            self.put_msg(BACKFILL_TIME_OLDER)
            return is_valid_backfill_days

        is_valid_date = ValidateInputs.check_future_date(start_date)
        if not is_valid_date:
            logger.info(FUTURE_DATE_IS_NOT_ACCEPTABLE)
            self.put_msg(START_DATE_INCORRECT)
            return is_valid_date

        is_valid_length = ValidateInputs.check_outgoing_feed_length(
            data["outgoing_feeds"]
        )
        logger.info(is_valid_length)

        if not is_valid_length:
            logger.info(MAXIMUM_FIVE_OUTGOING_FEEDS)
            self.put_msg(MAXIMUM_FIVE_OUTGOING_FEEDS)
            return False
        outgoing_feed_integer_only = ValidateInputs.validate_outgoing_feed_integer_only(
            data["outgoing_feeds"]
        )
        if not outgoing_feed_integer_only:
            logger.info("Only numerical values allowed for outgoing feeds!")
            self.put_msg("Only numerical values allowed for outgoing feeds!")
            return False
        is_unique_values = ValidateInputs.validate_unique_values(data["outgoing_feeds"])
        if not is_unique_values:
            self.put_msg(UNIQUE_VALUES_FOR_OUTGOING_FEEDS_ALLOWED)
            return False

        is_selected = ValidateInputs.check_observable_types(data)

        if not is_selected:
            logger.info(SELECT_ATLEAST_ONE_OBSERVABLE_TYPE)
            self.put_msg(SELECT_ATLEAST_ONE_OBSERVABLE_TYPE_TO_BE_INGESTED)
            return is_selected

        is_valid_interval = ValidateInputs.validate_interval(data["interval"])

        if not is_valid_interval:
            logger.info(INTERVAL_MUST_BE_BETWEEN_MIN_AND_MAX_INTERVAL)
            self.put_msg(INTERVAL_MUST_BE_BETWEEN_MIN_AND_MAX_INTERVAL)
            return is_valid_interval

        return True
