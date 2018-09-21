from dcat.base import Base


class Project(Base):
    def list(self, **kwargs):
        return self._request(
            "GET",
            self._get_url()
            )

    def create(self, name, slug=None):
        payload = {
            "name": name,
        }

        if slug is not None:
            payload["slug"] = slug

        return self._request(
            "POST",
            self._get_url(),
            payload
            )

    def modify(self, drn, name=None):
        payload = {}
        if name is not None:
            payload['name'] = name

        return self._request(
            "PUT",
            self._get_url(drn),
            payload
            )

    def delete(self, drn):
        return self._request(
            "DELETE",
            self._get_url(drn)
            )
