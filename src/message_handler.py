class Handler:
    def __init__(self):
        pass

    def on_message(self, msg):
        pass

    def on_error(self, msg):
        pass


class DatabaseHandler(Handler):
    def __init__(self, db_client):
        self.client = db_client

    def on_message(self, msg):
        # TODO: store message in database(maybe reddis oslt) -> a different job/script can then process the data
        # something like self.db_client.store(msg)
        pass

    def on_error(self, msg):
        pass


class LogHandler(Handler):
    def __init__(self, logger):
        self.logger = logger

    def on_message(self, message):
        self.logger.debug(message)

    def on_error(self, message):
        self.logger.exception(message)
