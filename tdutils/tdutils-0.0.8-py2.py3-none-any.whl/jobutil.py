"""
Python client for logging job results via a postgrest interface.

This class logs the outcome of scripted tasks in a pre-configured database whose API
is made available via postgrest (https://postgrest.com/).

The CONGIG and instance parameters must match the job database schema.

#TODO: handle ID updates
"""
import arrow

from .pgrestutil import Postgrest


CONFIG = {
    "destination_field": "destination",
    "end_date_field": "end_date",
    "id_field": "id",
    "message_field": "message",
    "name_field": "name",
    "records_processed_field": "records_processed",
    "source_field": "source",
    "start_date_field": "start_date",
    "status_field": "status",
}


class Job(Postgrest):
    """
    Class to interact with job control API. Extends Postgrest utility to work with jobs schema.
    """

    def __init__(self, url, auth=None, destination=None, name=None, source=None):
        super().__init__(url, auth=auth)

        self.destination = destination
        self.name = name
        self.source = source

        self.destination_field = CONFIG["destination_field"]
        self.end_date_field = CONFIG["end_date_field"]
        self.id_field = CONFIG["id_field"]
        self.name_field = CONFIG["name_field"]
        self.message_field = CONFIG["message_field"]
        self.records_processed_field = CONFIG["records_processed_field"]
        self.source_field = CONFIG["source_field"]
        self.start_date_field = CONFIG["start_date_field"]
        self.status_field = CONFIG["status_field"]

        self.data = None

    def most_recent(self, status="success"):
        """Return end date of the most-recent job run."""

        url = f"{self.url}?{self.name_field}=eq.{self.name}&{self.status_field}=eq.{status}&order={self.end_date_field}.desc&limit=1"
        res = self._query("SELECT", url)

        try:
            return arrow.get(res[0][self.start_date_field]).timestamp

        except (IndexError, KeyError) as e:
            return None

    def start(self):
        """Start a new job with given name."""
        data = {
            self.name_field: self.name,
            self.start_date_field: arrow.now().format(),
            self.status_field: "in_progress",
            self.source_field: self.source,
            self.destination_field: self.destination,
        }

        self.data = self._query("INSERT", self.url, data=data)[0]
        return self.data

    def result(self, _result, message=None, records_processed=0):
        """Update job status to specified result. """

        if _result not in ["success", "error"]:
            raise Exception("Unknown result specified.")

        data = {
            self.id_field: self.data[self.id_field],
            self.end_date_field: arrow.now().format(),
            self.status_field: _result,
            self.message_field: message,
            self.records_processed_field: records_processed,
        }

        self.data = self._query("UPDATE", self.url, data=data)[0]
        return self.data

    def delete(self):
        """Delete all job entries of specified name."""

        print(
            f"""
            WARNING: You are about to delete all jobs with name {self.name}.
            """
        )

        answer = input("Type 'Yes' to continue: ")

        if answer.upper() == "YES":
            url = f"{self.url}?{self.name_field}=eq.{self.name}"
            return self._query("DELETE", url)

        else:
            raise Exception("Delete aborted.")

